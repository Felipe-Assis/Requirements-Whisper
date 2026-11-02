# autopiloto.rpy
# -------------------------------
# PILOTO AUTOMÁTICO DE PONTA A PONTA (só testes; game/tests/ fica fora do build)
# -------------------------------
# Joga uma rota inteira, sem rede, de label start até o menu final do
# epílogo, pelo fluxo real: nome e gênero em scene_1, escolha da vaga, todas
# as falas, menus, escrita livre, planejamento e as telas chamadas
# (contacts_screen, chat offline, resumo do epílogo).
#
# Funciona por um callback periódico (config.periodic_callbacks, ~20 vezes
# por segundo) que olha a interação atual e a encerra com o valor que o
# jogador produziria (renpy.end_interaction): True numa fala ou tela de
# fechar, o valor da opção num menu, o texto num input. Desligado, o
# callback só retorna: no jogo normal (de desenvolvimento) não muda nada.
#
# Modos de escolha (sempre entre as opções menos tentadas daquele menu):
#   primeira          a primeira delas
#   ultima            a última
#   aleatorio:<n>     sorteio com semente n
# Preferir a menos tentada evita laço infinito em menus de revisão que voltam
# ao mesmo ponto; um menu visitado mais de LIMITE_VISITAS vezes conta como laço.
# Planejamento e escrita têm roteiro próprio por modo (coberturas 0/1/2,
# revisão interna, confirmado/pendente/reescrever).
#
# Tempo livre (intermissões): no cartão de abertura escolhe "Abrir o mapa"
# ou, na estratégia "pular", "Pular o tempo livre"; no mapa devolve uma opção
# de im_opcoes() ou "encerrar"; pula as telas de deslocamento e transição e
# fecha o resumo e o ponto de parada. Estratégias do mapa:
#   prioridade   (padrão de "primeira") mentoria > observar > ajudar >
#                estudar > conversar > descansar, para cobrir pistas e mentoria
#   ultima       (padrão de "ultima") semanas pares encerram logo; ímpares
#                usam a prioridade invertida
#   aleatorio    (padrão de "aleatorio:n") sorteio, 15% de chance de encerrar
#   pular        pula todo tempo livre (prova de que nada obrigatório depende dele)
# RW_AUTOPILOTO_MAPA=prioridade|ultima|aleatorio|pular sobrepõe o padrão.
#
# Uso em testcase (ponta_a_ponta.rpy):
#     $ autopiloto.ligar("startup", "primeira")
#     run Start()
#     pause until eval autopiloto.terminou() timeout 900
# Erros de execução viram falha do teste (o motor de testes os captura).
#
# Uso avulso (registra TODOS os erros e segue, como "Ignorar"; ao fim grava
# um JSON e fecha o jogo):
#     set RW_AUTOPILOTO=startup:aleatorio:7
#     set RW_AUTOPILOTO_RELATORIO=C:\caminho\relatorio.json
#     set RW_AUTOPILOTO_FORCAR=Virar a noite|outra opção   (opcional)
#     python.exe renpy.py <projeto> --savedir <pasta>
# tests/autopiloto.ps1 roda a matriz de rotas x modos assim.

init 999 python in autopiloto:
    import os
    import sys
    import json
    import time
    import io
    import random as _random
    import types
    import store

    renpy = store.renpy
    config = store.config

    LIMITE_VISITAS = 25
    LIMITE_INTERACOES = 40000
    LIMITE_ERROS = 40
    LIMITE_VOLTAS_MAPA = 20
    PRIORIDADE_MAPA = ["mentoria", "observar", "ajudar", "estudar", "conversar", "descansar"]

    # Índice da vaga no menu de scene_1 ("1. ...", "2. ...", "3. ...").
    VAGA = {"saude": "1. ", "startup": "2. ", "corporativo": "3. "}

    # Rótulos de cena esperados em cada rota (conferidos no relatório).
    CENAS = {
        "saude": [
            "scene_1_quarto", "scene_2_escritorio", "scene_3_reuniao_inicial",
            "scene_4_retorno_casa", "scene_5_preparacao_entrevista",
            "scene_6_entrevista_stakeholders", "scene_7_avaliacao_requisitos",
            "scene_8_cafe_informal", "scene_9_retorno_casa_sem2",
            "scene_10_criacao_casos_uso", "scene_11_almoco_equipe",
            "scene_12_especificacao_requisitos", "scene_13_retorno_casa_sem3",
            "scene_14_discussao_arquitetura", "scene_15_aniversario_surpresa",
            "scene_16_reuniao_gerenciamento", "scene_17_tarde_estudos_tecnicos",
            "scene_18_codificacao_implementacao", "scene_19_testes_seguranca",
            "scene_20_deploy_final", "scene_21_avaliacao_final",
        ],
        "startup": ["scene_1_quarto", "scene_2_escritorio", "rota_startup"] + [
            "st_01_chegada", "st_02_reuniao_ciclo", "st_03_casa_sem1",
            "st_04_preparacao", "st_05_entrevista", "st_06_classificacao",
            "st_07_social", "st_08_casa_sem2", "st_09_historias", "st_10_almoco",
            "st_11_inspecao", "st_12_casa_sem3", "st_13_arquitetura",
            "st_14_comemoracao", "st_15_gestao", "st_16_codificacao",
            "st_17_testes_seguranca", "st_18_lancamento",
        ],
        "corporativo": ["scene_1_quarto", "scene_2_escritorio", "rota_corporativo"] + [
            "co_01_chegada", "co_02_ciclo_legado", "co_03_casa_sem1",
            "co_04_preparacao", "co_05_entrevista", "co_06_avaliacao", "co_07_cafe",
            "co_08_casa_sem2", "co_09_historias", "co_10_almoco", "co_11_inspecao",
            "co_12_casa_sem3", "co_13_arquitetura", "co_14_comemoracao",
            "co_15_gestao", "co_16_codificacao", "co_17_testes_seguranca",
            "co_18_implantacao_avaliacao",
        ],
    }

    TEXTOS_ESCRITA = [
        ("A pessoa responsável pode corrigir o valor de um registro, desde que o novo valor seja maior que zero.",
         "Dado um registro de R$ 20, quando a pessoa muda para R$ 15 e confirma, então a lista e o total mostram R$ 5 a menos."),
        ("Quem {b}corrige{/b} [valor] e 100% das vezes",
         "Dado [x], quando {i}confirma{/i}, então 50% muda"),
    ]

    # Estado do piloto: objeto comum (fora de save e rollback).
    ap = types.SimpleNamespace(ativo=False, avulso=False, fim=False)

    def _mapa_padrao(modo):
        if modo == "ultima":
            return "ultima"
        if modo.startswith("aleatorio"):
            return "aleatorio"
        return "prioridade"

    def _novo_estado(rota, modo, forcar=(), mapa=None):
        if rota not in CENAS:
            raise Exception("autopiloto: rota desconhecida %r" % (rota,))
        ap.rota = rota
        ap.modo = modo
        ap.forcar = list(forcar)
        semente = None
        if modo.startswith("aleatorio"):
            partes = modo.split(":")
            semente = int(partes[1]) if len(partes) > 1 else 0
        ap.rng = _random.Random(semente if semente is not None else 0)
        ap.ativo = True
        ap.fim = False
        ap.inicio = time.time()
        ap.interacoes = 0
        ap.visitas = {}
        ap.tentadas = {}
        ap.escolhas = []
        ap.labels = []
        ap.erros = []
        ap.imagens_ausentes = []
        ap.imagens_nao_encontradas = []
        ap.audios_ausentes = []
        ap.telas = {}
        ap.planos = {}
        ap.plano_atual = None
        ap.escrita_n = 0
        ap.escrita_reescreveu = set()
        ap.chat_enviado = False
        ap.chats = []
        ap.contatos_vistos = 0
        ap.resumo_registros = None
        ap.relatorio = None
        ap.iniciou = False
        ap.mapa = mapa or os.environ.get("RW_AUTOPILOTO_MAPA") or _mapa_padrao(modo)
        ap.voltas_mapa = {}
        ap.mapa_escolhas = []
        diag = store.IM_DIAG
        ap.diag_ini = (len(diag.genericos), len(diag.relogio_volta), len(diag.telas))

    def ligar(rota, modo="primeira", forcar=(), mapa=None):
        """
        Liga o piloto para `rota` e `modo` (ver o topo do arquivo). `forcar`:
        trechos de texto de opções que, quando aparecem num menu, são
        escolhidas antes de qualquer outra (para ramos raros). `mapa`:
        estratégia do tempo livre (padrão conforme o modo).
        """
        _novo_estado(rota, modo, forcar, mapa)
        _aplicar_prefs()

    def concluir(motivo="ok"):
        """Fecha o percurso e monta o relatório (testes que não vão ao epílogo)."""
        _finalizar(motivo)

    def _aplicar_prefs():
        # Texto instantâneo e sem transições: o percurso fica rápido e as
        # telas são as mesmas. desligar() devolve os valores anteriores.
        prefs = store._preferences
        ap.prefs_antigas = (prefs.text_cps, prefs.transitions, prefs.afm_enable)
        prefs.text_cps = 0
        prefs.transitions = 0
        prefs.afm_enable = False
        ap.autosave_antigo = config.has_autosave
        config.has_autosave = False

    def desligar():
        if not ap.ativo:
            return
        ap.ativo = False
        prefs = store._preferences
        prefs.text_cps, prefs.transitions, prefs.afm_enable = ap.prefs_antigas
        config.has_autosave = ap.autosave_antigo

    def terminou():
        return ap.fim

    def relatorio():
        return ap.relatorio

    # ---------------- registro de problemas ----------------

    def _erro(tipo, texto):
        ap.erros.append({"tipo": tipo, "label": _label_atual(), "texto": texto})
        if len(ap.erros) >= LIMITE_ERROS:
            _finalizar("limite de erros")

    def _label_atual():
        return ap.labels[-1] if ap.labels else None

    def _label_callback(label, abnormal):
        if ap.ativo and not label.startswith("_"):
            ap.labels.append(label)

    config.label_callbacks.append(_label_callback)

    _img_original = config.missing_image_callback

    def _img_ausente(fn):
        if ap.ativo and not fn.startswith("gui/"):
            ap.imagens_ausentes.append({"arquivo": fn, "label": _label_atual()})
        return _img_original(fn) if _img_original else None

    config.missing_image_callback = _img_ausente

    _ImageNotFound = renpy.display.image.ImageNotFound
    _inf_init = _ImageNotFound.__init__

    def _inf_init_registra(self, tag, *attributes):
        if ap.ativo:
            ap.imagens_nao_encontradas.append({"imagem": " ".join((tag,) + attributes), "label": _label_atual()})
        _inf_init(self, tag, *attributes)

    _ImageNotFound.__init__ = _inf_init_registra

    def _arquivo_audio(f):
        if not isinstance(f, str):
            return None
        if f.startswith("<"):
            f = f[f.find(">") + 1:]
        return f

    def _envolve_audio(func):
        def envolvida(filenames, *args, **kwargs):
            if ap.ativo:
                lista = filenames if isinstance(filenames, (list, tuple)) else [filenames]
                for f in lista:
                    f = _arquivo_audio(f)
                    if f and not renpy.loadable(f):
                        ap.audios_ausentes.append({"arquivo": f, "label": _label_atual()})
            return func(filenames, *args, **kwargs)
        return envolvida

    renpy.audio.music.play = _envolve_audio(renpy.audio.music.play)
    renpy.audio.music.queue = _envolve_audio(renpy.audio.music.queue)

    def _exception_handler(te):
        # Só no modo avulso: registra e segue como "Ignorar".
        if not (ap.ativo and ap.avulso):
            return False
        buf = io.StringIO()
        try:
            # renpy.error na store é a função; a classe está no módulo.
            modulo = sys.modules["renpy.error"]
            te.format(modulo.NonColoredExceptionPrintContext(buf, filter_private=True, emit_context=False))
            texto = buf.getvalue()
        except Exception as e:
            texto = "%r (falha ao formatar: %r)" % (te, e)
        _erro("excecao", texto[-3000:])
        return True

    # ---------------- escolhas ----------------

    def _ordenar(candidatos):
        # candidatos: lista de índices; devolve o escolhido conforme o modo.
        if ap.modo == "primeira":
            return candidatos[0]
        if ap.modo == "ultima":
            return candidatos[-1]
        return ap.rng.choice(candidatos)

    def _escolher_menu(itens):
        captions = tuple(str(i.caption) for i in itens)
        local = renpy.game.context().current
        chave = (str(local), captions)
        visitas = ap.visitas.get(chave, 0) + 1
        ap.visitas[chave] = visitas
        if visitas > LIMITE_VISITAS:
            _erro("laco", "menu visitado %d vezes: %r" % (visitas, captions))
            _finalizar("laço de menu")
            return None

        validos = [n for n, i in enumerate(itens) if i.action is not None]
        if not validos:
            _erro("menu", "menu sem opção válida: %r" % (captions,))
            return None

        # Menu final do epílogo: fim do percurso.
        if any(c.startswith("Encerrar") for c in captions) and any("créditos" in c for c in captions):
            _finalizar("ok")
            return None

        # Escolha da vaga em scene_1.
        if all(c[:3] in ("1. ", "2. ", "3. ") for c in captions):
            for n, c in enumerate(captions):
                if c.startswith(VAGA[ap.rota]):
                    return n

        for trecho in ap.forcar:
            for n in validos:
                if trecho in captions[n]:
                    return n

        plano = _escolha_plano(itens, captions)
        if plano is not None:
            return plano

        # Entre as opções menos tentadas neste menu, escolhe conforme o modo.
        tentadas = ap.tentadas.setdefault(chave, {})
        menor = min(tentadas.get(n, 0) for n in validos)
        n = _ordenar([n for n in validos if tentadas.get(n, 0) == menor])
        tentadas[n] = tentadas.get(n, 0) + 1
        return n

    # ---------------- planejamento ----------------

    def _plano_alvo(pid):
        # Cobertura alvo da k-ésima chamada da atividade `pid`.
        info = ap.planos.setdefault(pid, {"chamadas": 0, "conferencias": [], "base": None})
        if info["base"] is None:
            if ap.modo == "primeira":
                info["base"] = 2
            elif ap.modo == "ultima":
                info["base"] = 0
            else:
                info["base"] = ap.rng.choice([0, 1, 2])
        alvo = min(2, info["base"] + info["chamadas"])
        info["chamadas"] += 1
        return alvo

    def _plano_desejado(alvo):
        itens = list(store.itens)
        cap = min(store.capacidade, len(itens))
        nec = store.planejamento_indices(itens, store.necessarios)
        extras = [i for i in range(len(itens)) if i not in nec]
        nec_ordem = list(nec)
        if ap.modo.startswith("aleatorio"):
            ap.rng.shuffle(nec_ordem)
            ap.rng.shuffle(extras)
        elif ap.modo == "ultima":
            nec_ordem.reverse()
            extras.reverse()
        alvo = min(alvo, cap)
        return set(nec_ordem[:alvo] + extras[:cap - alvo])

    def _escolha_plano(itens, captions):
        valores = [getattr(i.action, "value", None) for i in itens]
        eh_plano = any(isinstance(v, tuple) and len(v) == 2 and v[0] in ("add", "del", "conferir") for v in valores)
        eh_fecho = "Revisar os itens escolhidos" in captions and "Concluir com este plano" in captions
        if not (eh_plano or eh_fecho):
            return None

        pid = store.pid
        if eh_plano:
            if ap.plano_atual is None or ap.plano_atual["pid"] != pid or ap.plano_atual.get("concluido"):
                ap.plano_atual = {"pid": pid, "desejado": _plano_desejado(_plano_alvo(pid)),
                                  "revisoes": 0, "concluido": False}
            desejado = ap.plano_atual["desejado"]
            sel = list(store.planejamento_sel)
            for n, v in enumerate(valores):
                if v and v[0] == "del" and v[1] not in desejado:
                    return n
            for n, v in enumerate(valores):
                if v and v[0] == "add" and v[1] in desejado:
                    return n
            for n, v in enumerate(valores):
                if v and v[0] == "conferir":
                    nec = store.planejamento_indices(list(store.itens), store.necessarios)
                    ap.planos[pid]["conferencias"].append(len([i for i in sel if i in nec]))
                    return n
            # Plano inalcançável: escolhe a primeira adição livre.
            for n, v in enumerate(valores):
                if v and v[0] == "add":
                    return n
            return 0

        # Depois de conferir: revisar (uma vez, nos modos aleatórios) ou concluir.
        atual = ap.plano_atual
        revisar = ap.modo.startswith("aleatorio") and atual["revisoes"] == 0 and ap.rng.random() < 0.5
        if revisar:
            atual["revisoes"] += 1
            atual["desejado"] = _plano_desejado(ap.rng.choice([0, 1, 2]))
            return captions.index("Revisar os itens escolhidos")
        atual["concluido"] = True
        return captions.index("Concluir com este plano")

    # ---------------- escrita ----------------

    def _texto_escrita(etapa):
        idx = 1 if (ap.modo.startswith("aleatorio") and ap.rng.random() < 0.5) else 0
        if ap.modo == "ultima":
            idx = 1
        return TEXTOS_ESCRITA[idx][etapa - 1]

    def _revisao_escrita():
        eid = store.eid
        if ap.modo == "primeira":
            acao = "confirmado"
        elif ap.modo == "ultima":
            acao = "pendente"
        else:
            if eid not in ap.escrita_reescreveu and ap.rng.random() < 0.4:
                ap.escrita_reescreveu.add(eid)
                acao = "reescrever"
            else:
                acao = ap.rng.choice(["confirmado", "pendente"])
        if acao == "confirmado":
            store.escrita_marcas = [True, True, True, True]
        elif acao == "pendente" and ap.modo.startswith("aleatorio"):
            store.escrita_marcas = [ap.rng.random() < 0.5 for i in range(4)]
        return acao

    # ---------------- contatos e chat ----------------

    def _botoes_contato():
        scr = renpy.get_screen("contacts_screen")
        achados = []

        def visita(d):
            acao = getattr(d, "action", None)
            if isinstance(d, renpy.display.behavior.Button) and acao:
                lista = acao if isinstance(acao, (list, tuple)) else [acao]
                for a in lista:
                    if isinstance(a, store.SetVariable) and a.field == "amigo_selecionado":
                        achados.append((a.value, acao))
        if scr is not None:
            scr.visit_all(visita)
        return achados

    def _contatos():
        ap.contatos_vistos += 1
        if ap.rota == "saude" or not ap.modo.startswith("aleatorio"):
            return True
        if ap.rng.random() < 0.5:
            return True
        offline = [(cid, a) for cid, a in _botoes_contato() if store.chat_is_offline(cid)]
        if not offline:
            return True
        cid, acao = ap.rng.choice(offline)
        ap.chats.append({"contato": cid, "label": _label_atual()})
        ap.chat_enviado = False
        renpy.run(acao)
        return None

    def _chat():
        if not store.chat_is_offline(store.amigo_selecionado):
            # Nunca usa a rede: fecha sem enviar.
            return True
        if not ap.chat_enviado:
            ap.chat_enviado = True
            store.send_and_update_chat("Oi! Como foi seu dia?")
            return None
        if store.is_waiting or store.pending_response is not None:
            return None
        if len(store.chat_history) < 2:
            _erro("chat", "chat offline sem resposta de %s" % store.amigo_selecionado)
        return True

    # ---------------- tempo livre ----------------

    def _escolher_mapa():
        sem = store.im_semana_atual
        ap.voltas_mapa[sem] = ap.voltas_mapa.get(sem, 0) + 1
        if ap.voltas_mapa[sem] > LIMITE_VOLTAS_MAPA:
            _erro("laco", "mapa da semana %s aberto %d vezes" % (sem, ap.voltas_mapa[sem]))
            return "encerrar"
        ops = store.im_opcoes(sem)
        if not ops:
            return "encerrar"
        if ap.mapa == "ultima":
            if sem % 2 == 0:
                return "encerrar"
            ordem = PRIORIDADE_MAPA[::-1]
            escolha = min(ops, key=lambda o: ordem.index(o["acao"]))
        elif ap.mapa == "aleatorio":
            if ap.rng.random() < 0.15:
                return "encerrar"
            escolha = ap.rng.choice(ops)
        else:
            escolha = min(ops, key=lambda o: PRIORIDADE_MAPA.index(o["acao"]))
        ap.mapa_escolhas.append([sem, escolha["poi"], escolha["acao"], escolha["alvo"]])
        return escolha["valor"]

    def _dados_tempo_livre():
        regs = store.im_feitas.get(ap.rota, {})
        diag = store.IM_DIAG
        g, r, t = ap.diag_ini
        return {
            "intermissoes": ap.labels.count("im_intermissao"),
            "intermissoes_puladas": sum(1 for x in regs.values() if x.get("pulada")),
            "acoes_intermissao": {k: [list(a) for a in v["acoes"]] for k, v in regs.items()},
            "energia": {k: v.get("energia_fim") for k, v in regs.items()},
            "pistas": sorted(store.pistas),
            "pistas_usadas": sorted(store.pistas_usadas),
            "mentoria": store.mentoria_passos.get(ap.rota, 0),
            "conquistas_extra": [a["id"] for a in store.conquistas_extra_obtidas()],
            "extras": list(store.extras_contagem()),
            "conteudo_generico": sorted(set(diag.genericos[g:])),
            "relogio_volta": list(diag.relogio_volta[r:]),
            "telas_deslocamento": list(diag.telas[t:]),
            "mapa_estrategia": ap.mapa,
            "mapa_escolhas": ap.mapa_escolhas,
        }

    # ---------------- fim ----------------

    def _final_da_rota():
        if ap.rota == "saude":
            return getattr(store, "final_grade", None)
        if ap.rota == "startup":
            return store.st_final_grade()
        return getattr(store, "co_final_resultado", None)

    def _finalizar(motivo):
        if ap.fim:
            return
        ap.fim = True
        try:
            final = _final_da_rota()
        except Exception as e:
            final = "erro: %r" % (e,)
        try:
            final_rota = store.route_final_grade()
        except Exception as e:
            final_rota = "erro: %r" % (e,)
        visitadas = set(ap.labels)
        faltando = [c for c in CENAS[ap.rota] if c not in visitadas]
        rel = {
            "rota": ap.rota,
            "modo": ap.modo,
            "motivo": motivo,
            "chegou_epilogo": "scene_epilogo_conquistas_final" in visitadas,
            "cenas_faltando": faltando,
            "final_cena": final,
            "final_rota": final_rota,
            "resumo_registros": ap.resumo_registros,
            "registros": list(store.registros_contagem()),
            "decisoes": list(store.resumo_decisoes()),
            "escritas": list(store.resumo_escritas()),
            "escritas_detalhe": {k: dict(v) for k, v in store.escritas.items()},
            "planejamentos": {k: dict(v) for k, v in store.planejamentos.items()},
            "conquistas": [a["id"] for a in store.route_achievements() if store.achievement_unlocked(a)],
            "chosen_job": store.chosen_job,
            "amizade_equipe": {c: store.get_friendship_point(c) for c in store.route_team()},
            "interacoes": ap.interacoes,
            "escolhas": ap.escolhas,
            "segundos": round(time.time() - ap.inicio, 1),
            "erros": ap.erros,
            "imagens_ausentes": ap.imagens_ausentes,
            "imagens_nao_encontradas": ap.imagens_nao_encontradas,
            "audios_ausentes": ap.audios_ausentes,
            "chats": ap.chats,
            "planos_piloto": ap.planos,
            "contatos_vistos": ap.contatos_vistos,
            "telas": ap.telas,
        }
        try:
            rel.update(_dados_tempo_livre())
        except Exception as e:
            rel["tempo_livre_erro"] = repr(e)
        ap.relatorio = rel
        destino = os.environ.get("RW_AUTOPILOTO_RELATORIO")
        if destino:
            with open(destino, "w", encoding="utf-8") as f:
                json.dump(rel, f, ensure_ascii=False, indent=1, default=str)
        if ap.avulso:
            renpy.quit()

    # ---------------- laço principal ----------------

    def _rastreabilidade(scope):
        # Quadro: liga cada critério ao requisito e ao teste certos. No modo "ultima" o piloto
        # liga a lacuna a um teste qualquer (não acha a falta), para exercitar o bug na semana de
        # testes; nos outros modos deixa a lacuna sem teste (acha a falta). Depois, continua.
        if scope.get("fase", "quadro") != "quadro":
            return True
        qid = scope["qid"]
        dados = store.rast_dados(qid)
        lig = {}
        for c in dados["criterios"]:
            teste = c["teste"]
            if c["id"] == dados["lacuna"] and ap.modo == "ultima" and dados["testes"]:
                teste = dados["testes"][0]["id"]
            lig[c["id"]] = [c["de"], teste]
        return ("conferir", lig)

    def _ambiguidade(scope):
        # Marca exatamente as palavras vagas; as reescritas passam pelo menu comum (choice).
        if scope.get("fase", "marcar") != "marcar":
            return True
        return ("conferir", list(store.amb_vagas(scope["aid"])))

    def _tela(nome):
        ap.telas[nome] = ap.telas.get(nome, 0) + 1

    def _tick():
        if not ap.ativo or ap.fim:
            return

        if renpy.get_screen("main_menu"):
            if ap.avulso and not ap.iniciou:
                # As preferências salvas carregam depois do init: reaplica.
                ap.iniciou = True
                _aplicar_prefs()
                renpy.run(store.Start())
            return

        # Não interfere em menus do jogo (Preferências, Mochila) abertos à mão.
        if renpy.context()._menu:
            return

        ap.interacoes += 1
        if ap.interacoes > LIMITE_INTERACOES:
            _erro("limite", "mais de %d interações" % LIMITE_INTERACOES)
            _finalizar("limite de interações")
            return

        valor = True
        choice = renpy.get_screen("choice")
        if choice is not None:
            itens = choice.scope.get("items") or []
            n = _escolher_menu(itens)
            if n is None:
                return
            item = itens[n]
            ap.escolhas.append((_label_atual(), str(item.caption)))
            valor = item.action()
        elif renpy.get_screen("im_abertura_cartao"):
            _tela("im_abertura_cartao")
            valor = "pular" if ap.mapa == "pular" else "mapa"
        elif renpy.get_screen("im_transicao"):
            _tela("im_transicao")
        elif renpy.get_screen("im_deslocamento"):
            _tela("im_deslocamento")
        elif renpy.get_screen("im_mapa"):
            _tela("im_mapa")
            valor = _escolher_mapa()
        elif renpy.get_screen("im_resumo"):
            _tela("im_resumo")
        elif renpy.get_screen("im_parada"):
            _tela("im_parada")
        elif renpy.get_screen("escrita_revisao"):
            _tela("escrita_revisao")
            valor = _revisao_escrita()
        elif renpy.get_screen("escrita_input"):
            _tela("escrita_input")
            etapa = renpy.get_screen("escrita_input").scope.get("etapa", 1)
            valor = _texto_escrita(etapa)
        elif renpy.get_screen("input"):
            _tela("input")
            if ap.modo == "primeira":
                valor = "Ana"
            elif ap.modo == "ultima":
                valor = ""
            else:
                valor = ap.rng.choice(["Bia", "Caio [x]", "{b}Duda", ""])
        elif renpy.get_screen("chat_with_backend"):
            _tela("chat_with_backend")
            valor = _chat()
        elif renpy.get_screen("contacts_screen"):
            _tela("contacts_screen")
            valor = _contatos()
        elif renpy.get_screen("resumo_rota"):
            _tela("resumo_rota")
            w = renpy.get_widget("resumo_rota", "resumo_registros")
            ap.resumo_registros = w.text[0] if w is not None else None
        elif renpy.get_screen("notebook_registros"):
            _tela("notebook_registros")
        elif renpy.get_screen("rast_escolher"):
            # Seletor aberto por clique; o piloto liga tudo direto no quadro.
            _tela("rast_escolher")
            renpy.hide_screen("rast_escolher")
            valor = None
        elif renpy.get_screen("rast_quadro"):
            _tela("rast_quadro")
            valor = _rastreabilidade(renpy.get_screen("rast_quadro").scope)
        elif renpy.get_screen("amb_marcar"):
            _tela("amb_marcar")
            valor = _ambiguidade(renpy.get_screen("amb_marcar").scope)

        if valor is not None:
            renpy.end_interaction(valor)

    config.periodic_callbacks.append(_tick)

    # Modo avulso por variável de ambiente.
    _env = os.environ.get("RW_AUTOPILOTO")
    if _env:
        _partes = _env.split(":", 1)
        _forcar = [t for t in os.environ.get("RW_AUTOPILOTO_FORCAR", "").split("|") if t]
        _novo_estado(_partes[0], _partes[1] if len(_partes) > 1 else "primeira", _forcar)
        ap.avulso = True
        config.exception_handler = _exception_handler
