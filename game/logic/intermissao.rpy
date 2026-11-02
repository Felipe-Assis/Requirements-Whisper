# intermissao.rpy
# -------------------------------
# INTERMISSÕES (TEMPO LIVRE): estado, opções, deslocamento, recompensas,
# PISTAS, MENTORIA e REGISTROS EXTRAS
# -------------------------------
# Referência: docs/design/sistemas-intermissoes.md (§1 a §4, §8 e §10), com a
# decisão posterior do mapa da cidade (data/mapa_cidade.rpy): cada local da
# rota (POI) fica num lugar da cidade; salas do mesmo prédio custam 0 min de
# deslocamento.
#
# Fluxo e labels: scripts/mechanics/intermissao_fluxo.rpy. Telas:
# scripts/mechanics/mapa_screen.rpy. Energia: logic/energia.rpy.
#
# Dados por rota (data/intermissoes_<rota>.rpy, init 3 python):
#   ROUTES[rota]["mapa"] = {
#       "musica": nome de um define music_* (opcional),
#       "inicio": id do POI onde o jogador começa o tempo livre,
#       "lugares_fechados" {lugar: motivo} (opcional; lugar da cidade que
#                 aparece na rota, sempre fechado),
#       "longe" {cid: (lugar, icone, frase)} (opcional; balão acinzentado
#                 quando a pessoa não está na agenda e já é contato),
#       "pois": [{"id", "nome", "lugar" (id em MAPA_LUGARES), "sub" (texto
#                 curto do sub-local), "bg", "bg_semana" {semana: bg}
#                 (opcional), "abre" (semana), "acoes" (["estudar",
#                 "descansar", "observar"]), "icone" (atividade padrão dos
#                 balões, chave de MAPA_ATIVIDADES)}],
#   }
#   ROUTES[rota]["intermissoes"] = {N: {
#       "dia", "inicio" (h, m), "bloco" (min), "mesmo_dia" (bool),
#       "agenda" {poi: [cid]}, "fechados" {poi: motivo},
#       "ajudar" {cid: pista ou None}, "observar" {poi: pista ou None},
#       "estudar" (id do extra ou None),
#       "atividade" {cid: (icone, frase)} (opcional, balões),
#       "observar_amizade" {poi: cid} (opcional; padrão: 1ª pessoa do local),
#       "inicio_poi" (opcional; padrão: mapa["inicio"]),
#   }}
#   ROUTES[rota]["pistas"] = {pid: {"titulo", "texto", "ate_semana", "uso"}}
#   ROUTES[rota]["extras"] = [{"id", "title", "text"}]   (7, um por semana 1-7)
#   ROUTES[rota]["mentoria"] = {"id", "titulo", "mentor", "conquista",
#       "passos": [{"n", "semana_min", "pista", "resumo"}]}
#   ROUTES[rota]["conquistas_extra"] = [{"id", "var", "title", "desc"}]
#
# Regras (§0.1): uma intermissão nunca chama registrar(), decisao() nem as
# atividades pedagógicas; nada aqui muda registros_contagem(), as conquistas
# de route_achievements() ou a regra do final.

# Semana da intermissão em curso (0 = fora de uma intermissão).
default im_semana_atual = 0
# Minutos que restam no bloco e hora prevista de fim.
default im_minutos = 0
default im_fim = (0, 0)
# {rota: {semana: registro}}; o registro está descrito em _im_registro_novo.
default im_feitas = {}
# Minutos a descontar da próxima intermissão (horas extras citadas nas cenas).
default im_hora_extra = 0
# POI onde o jogador está agora ("" fora do tempo livre).
default im_local = ""
# Registros do notebook já mostrados num ponto de parada (para listar os novos).
default im_registros_vistos = set()

# Pistas: ids ganhos e ids lembrados/usados numa cena.
default pistas = set()
default pistas_usadas = set()

# Mentoria: {rota: encontros feitos} e as conquistas extras.
default mentoria_passos = {}
default mentoria_conq_saude = False
default mentoria_conq_startup = False
default mentoria_conq_corporativo = False

# Preferências (fora do save): pular todo tempo livre (aula curta) e ver o
# mapa como lista.
default persistent.im_pular = False
default persistent.im_mapa_lista = False


init python:
    import types as _im_types

    IM_ACOES = {
        "conversar": {"min": 30, "energia": 0, "nome": _("Conversar"), "recompensa": _("Amizade")},
        "observar": {"min": 90, "energia": -1, "nome": _("Observar o uso"), "recompensa": _("Pista de uso")},
        "estudar": {"min": 60, "energia": -1, "nome": _("Estudar"), "recompensa": _("Registro extra")},
        "descansar": {"min": 60, "energia": 2, "nome": _("Descansar"), "recompensa": _("Energia")},
        "ajudar": {"min": 90, "energia": -2, "nome": _("Ajudar"), "recompensa": _("Amizade e pista técnica")},
        "mentoria": {"min": 90, "energia": -1, "nome": _("Mentoria"), "recompensa": _("Amizade e passo da mentoria")},
    }
    # Ordem das ações dentro de um local no painel.
    IM_ORDEM_ACOES = ["mentoria", "ajudar", "conversar", "observar", "estudar", "descansar"]
    IM_AMIZADE = {"conversar": 0.5, "observar": 0.5, "ajudar": 1.0, "mentoria": 1.0}
    IM_TETO_PESSOA = 1.0
    IM_TETO_TOTAL = 2.0
    IM_BLOCO_MINIMO = 60
    IM_MESMO_DIA_MINIMO = 90
    IM_HORA_EXTRA_MAX = 60
    IM_CEDO_MINUTOS = 60
    IM_FIM_SEMANA_ENERGIA = 3

    # Diagnóstico para o autopiloto e para quem escreve conteúdo. Criado no
    # init e só mutado: fica fora do save e do rollback.
    IM_DIAG = _im_types.SimpleNamespace(genericos=[], relogio_volta=[], telas=[])

    # ---------------- dados ----------------

    def im_rota(rota=None):
        return rota or current_route()

    def im_dados(semana, rota=None):
        """Dict da intermissão da semana (None se a rota não tem)."""
        return route_data(rota).get("intermissoes", {}).get(semana)

    def im_mapa_dados(rota=None):
        return route_data(rota).get("mapa", {"pois": []})

    def im_poi(pid, rota=None):
        for p in im_mapa_dados(rota)["pois"]:
            if p["id"] == pid:
                return p
        return None

    def im_nome(cid):
        dados = AMIGOS_DATA.get(cid)
        return __(dados["name"]) if dados else cid

    def im_pois(semana, rota=None):
        """
        Locais da rota com estado na semana: lista de dicts (cópias) com
        "estado" ("aberto", "fechado" ou "futuro") e "motivo" escrito.
        """
        d = im_dados(semana, rota) or {}
        fechados = d.get("fechados", {})
        saida = []
        for p in im_mapa_dados(rota)["pois"]:
            q = dict(p)
            if p.get("abre", 1) > semana:
                q["estado"] = "futuro"
                q["motivo"] = __("Abre na semana {n}").format(n=p.get("abre", 1))
            elif p["id"] in fechados:
                q["estado"] = "fechado"
                q["motivo"] = __(fechados[p["id"]])
            else:
                q["estado"] = "aberto"
                q["motivo"] = None
            saida.append(q)
        return saida

    def im_quem_esta(poi, semana, rota=None):
        d = im_dados(semana, rota) or {}
        return list(d.get("agenda", {}).get(poi, []))

    def im_poi_bg(pid, semana, rota=None):
        p = im_poi(pid, rota)
        if not p:
            return None
        return p.get("bg_semana", {}).get(semana, p.get("bg"))

    # ---------------- registro da semana ----------------

    def _im_registro_novo():
        return {
            "acoes": [],            # [[poi, acao, alvo], ...] na ordem feita
            "amizade": {},          # cid -> amizade ganha nesta intermissão
            "pistas": [],           # pistas ganhas nesta intermissão
            "extra": None,          # registro extra ganho
            "minutos_usados": 0,
            "bloco": 0,             # minutos disponíveis no início
            "descontos": [],        # [[motivo, minutos], ...]
            "encerrou_cedo": False,
            "pulada": False,
            "trajeto_min": 0,       # minutos gastos no caminho
            "trajetos": 0,
            "energia_inicio": store.energia_semana,
            "energia_fim": None,
            "concluida": False,
        }

    def im_registro_semana(semana=None, rota=None, criar=True):
        rota = im_rota(rota)
        semana = semana or store.im_semana_atual
        por_rota = store.im_feitas.get(rota)
        if por_rota is None:
            if not criar:
                return None
            por_rota = store.im_feitas[rota] = {}
        reg = por_rota.get(semana)
        if reg is None and criar:
            reg = por_rota[semana] = _im_registro_novo()
        return reg

    def _im_chave(acao, poi, alvo):
        # Limites por intermissão: conversar e ajudar, 1 por pessoa; observar,
        # 1 por local; estudar, descansar e mentoria, 1 no total.
        if acao in ("conversar", "ajudar"):
            return (acao, alvo)
        if acao == "observar":
            return (acao, poi)
        return (acao,)

    def im_ja_feita(semana, acao, poi, alvo, rota=None):
        reg = im_registro_semana(semana, rota, criar=False)
        if not reg:
            return False
        chave = _im_chave(acao, poi, alvo)
        return any(_im_chave(a, p, t) == chave for p, a, t in reg["acoes"])

    # ---------------- relógio ----------------

    def _im_minutos_do_dia(hm=None):
        if hm is None:
            return store.game_hour * 60 + store.game_minute
        return hm[0] * 60 + hm[1]

    def _im_hm(total):
        total = int(total) % (24 * 60)
        return (total // 60, total % 60)

    def im_hora_texto(hm):
        return "%02d:%02d" % (hm[0], hm[1])

    def im_hora_extra_somar(minutos):
        """Hora extra citada numa cena: tira até 60 min da próxima intermissão."""
        store.im_hora_extra = min(IM_HORA_EXTRA_MAX, store.im_hora_extra + int(minutos))

    def im_iniciar(semana, rota=None):
        """
        Prepara o bloco de tempo livre (§1.3): relógio, minutos, descontos de
        hora extra e energia, local de partida. Devolve o registro da semana.
        """
        rota = im_rota(rota)
        d = im_dados(semana, rota)
        por_rota = store.im_feitas.setdefault(rota, {})
        por_rota[semana] = reg = _im_registro_novo()
        store.im_semana_atual = semana

        inicio = _im_minutos_do_dia(d["inicio"])
        fim = inicio + d["bloco"]
        agora = _im_minutos_do_dia()
        if d.get("mesmo_dia") and agora > inicio:
            comeco = agora
            if fim - agora < IM_MESMO_DIA_MINIMO:
                fim = agora + IM_MESMO_DIA_MINIMO
                aviso = "relogio_volta: %s semana %d, cena terminou %s, bloco previsto até %s" % (
                    rota, semana, im_hora_texto(_im_hm(agora)), im_hora_texto(_im_hm(inicio + d["bloco"])))
                IM_DIAG.relogio_volta.append(aviso)
                renpy.log(aviso)
        else:
            comeco = inicio
            set_time(*d["inicio"])
        bloco = fim - comeco

        descontos = []
        extra = min(store.im_hora_extra, IM_HORA_EXTRA_MAX)
        if extra:
            descontos.append([_("hora extra"), extra])
            store.im_hora_extra = 0
        cansaco = energia_desconto_bloco()
        if cansaco:
            descontos.append([_("cansaço") if cansaco < 60 else _("exaustão"), cansaco])
        for motivo, m in descontos:
            bloco -= m
        bloco = max(IM_BLOCO_MINIMO, bloco)

        store.im_minutos = bloco
        store.im_fim = _im_hm(comeco + bloco)
        store.im_local = d.get("inicio_poi") or im_mapa_dados(rota).get("inicio", "")
        reg["bloco"] = bloco
        reg["descontos"] = descontos
        reg["energia_inicio"] = store.energia_semana
        return reg

    def im_pular(semana, rota=None):
        """Pula o tempo livre: o relógio vai ao fim do bloco, sem ações."""
        reg = im_registro_semana(semana, rota)
        reg["pulada"] = True
        set_time(*store.im_fim)
        store.im_minutos = 0

    def im_encerrar_cedo(semana, rota=None):
        """Encerrar antes: com 60 min ou mais sobrando, +1 de energia."""
        reg = im_registro_semana(semana, rota)
        if store.im_minutos >= IM_CEDO_MINUTOS:
            reg["encerrou_cedo"] = True
            energia_ganhar(1, _("foi para casa mais cedo"))

    def im_encerrar(semana, rota=None):
        """Fecha a intermissão: recuperação de fim de semana e estado zerado."""
        reg = im_registro_semana(semana, rota)
        energia_ganhar(IM_FIM_SEMANA_ENERGIA, _("fim de semana"))
        reg["energia_fim"] = store.energia_semana
        reg["concluida"] = True
        store.energia_mostrar = True
        store.im_semana_atual = 0
        store.im_minutos = 0
        store.im_local = ""

    # ---------------- deslocamento ----------------

    def im_lugar_do_poi(pid, rota=None):
        p = im_poi(pid, rota) if pid else None
        return p.get("lugar") if p else None

    def _im_par(tabela, a, b):
        return tabela.get((a, b)) or tabela.get((b, a))

    def im_trajeto_lugares(lo, ld):
        """
        (minutos, meio) entre dois lugares diferentes da cidade: exceções de
        MAPA_TRAJETOS_LUGAR; mesmo bairro, MAPA_MINUTOS_BAIRRO a pé; bairros
        diferentes, MAPA_TRAJETOS. None se o par de bairros não tem tempo
        (im_validar_mapa acusa).
        """
        par = _im_par(MAPA_TRAJETOS_LUGAR, lo, ld)
        if par:
            return par
        bo, bd = MAPA_LUGARES[lo]["bairro"], MAPA_LUGARES[ld]["bairro"]
        if bo == bd:
            return (MAPA_MINUTOS_BAIRRO, MAPA_MEIO_BAIRRO.get(bo, "calcada"))
        return _im_par(MAPA_TRAJETOS, bo, bd)

    def im_trajeto(origem, destino, rota=None):
        """
        Deslocamento entre dois POIs (mapa-cidade.md §4): {"minutos", "meio",
        "de", "para"} (de/para = lugares). Mesmo POI ou origem desconhecida:
        0 min e meio None. Mesmo lugar: 0 min e o meio interno do prédio (None
        = só um dissolve). Lugares diferentes: im_trajeto_lugares.
        """
        lo = im_lugar_do_poi(origem, rota)
        ld = im_lugar_do_poi(destino, rota)
        r = {"minutos": 0, "meio": None, "de": lo, "para": ld}
        if not lo or not ld or origem == destino:
            return r
        if lo == ld:
            r["meio"] = MAPA_LUGARES[ld].get("interno")
            return r
        r["minutos"], r["meio"] = im_trajeto_lugares(lo, ld) or (40, "onibus")
        return r

    def im_transicoes_ligadas():
        # Mesma preferência "Transições" do menu. Desligada: sem caminhada do
        # marcador e sem imagem; só um cartão de texto curto.
        return _preferences.transitions != 0

    def _im_duracao_transicao(minutos):
        for limite, segundos in MAPA_TEMPO_TRANSICAO:
            if minutos <= limite:
                return segundos
        return MAPA_TEMPO_TRANSICAO[-1][1]

    def im_deslocamento_info(op, rota=None):
        """
        Dados da sequência de deslocamento para a opção `op`, ou None se o
        jogador já está naquele POI. Campos: minutos, meio, meio_nome, texto
        ("Ônibus · Casarão amarelo → Bandejão da universidade · 30 min"),
        texto_curto (com "15:00 → 15:30"), de, para (lugares), marcador (o
        lugar muda), tela (há tela de transição), fundo (displayable ou nome
        de bg), som, volume, som_chegada, hora_ini, hora_fim (minutos do dia),
        duracao (s).
        """
        if op["poi"] == store.im_local:
            return None
        t = im_trajeto(store.im_local, op["poi"], rota)
        destino_poi = im_poi(op["poi"], rota)
        origem_poi = im_poi(store.im_local, rota)
        if t["de"] and t["de"] != t["para"]:
            de, para = __(MAPA_LUGARES[t["de"]]["nome"]), __(MAPA_LUGARES[t["para"]]["nome"])
        else:
            de = __(origem_poi["nome"]) if origem_poi else ""
            para = __(destino_poi["nome"])
        if op["poi"] == "cafe":
            chegada = MAPA_SOM_CAFE
        elif t["de"] != t["para"] and MAPA_LUGARES.get(t["para"], {}).get("predio"):
            chegada = MAPA_SOM_PORTA
        else:
            chegada = None
        return _im_desl_info(t, de, para, chegada, cobra=True)

    def im_deslocamento_casa_info(rota=None):
        """
        Volta para casa ao encerrar o tempo livre (mapa-cidade.md §2.3 e
        §4.3): mesma sequência, mas sem cobrar minutos (o relógio não anda).
        None se o jogador não está num lugar ou já está em casa.
        """
        lo = im_lugar_do_poi(store.im_local, rota)
        if not lo or lo == MAPA_CASA:
            return None
        minutos, meio = im_trajeto_lugares(lo, MAPA_CASA) or (40, "onibus")
        t = {"minutos": minutos, "meio": meio, "de": lo, "para": MAPA_CASA}
        return _im_desl_info(t, __(MAPA_LUGARES[lo]["nome"]), __(MAPA_LUGARES[MAPA_CASA]["nome"]),
                             MAPA_SOM_PORTA, cobra=False)

    def _im_desl_info(t, de, para, chegada, cobra):
        meio = MAPA_MEIOS.get(t["meio"], {}) if t["meio"] else {}
        partes = [p for p in (__(meio["nome"]) if meio else "", "%s → %s" % (de, para) if de else para) if p]
        if t["minutos"]:
            partes.append(__("{n} min").format(n=t["minutos"]))
        texto = " · ".join(partes)
        ini = _im_minutos_do_dia()
        fim = ini + (t["minutos"] if cobra else 0)
        texto_curto = texto
        if cobra:
            texto_curto += " · %s → %s" % (im_hora_texto(_im_hm(ini)), im_hora_texto(_im_hm(fim)))
        som = meio.get("som")
        imagem = None
        if t["meio"]:
            imagem = MAPA_CIDADE.get("pasta_transicoes", "") + t["meio"] + ".png"
        return {
            "minutos": t["minutos"] if cobra else 0, "meio": t["meio"],
            "meio_nome": __(meio["nome"]) if meio else "",
            "texto": texto, "texto_curto": texto_curto,
            "de": t["de"], "para": t["para"],
            "marcador": bool(t["de"]) and t["de"] != t["para"],
            "tela": t["meio"] is not None,
            "imagem": imagem, "fundo": meio.get("fundo"),
            "som": som if som and renpy.loadable(som) else None,
            "volume": meio.get("volume", 1.0),
            "som_chegada": chegada if chegada and renpy.loadable(chegada) else None,
            "hora_ini": ini, "hora_fim": fim, "relogio": cobra,
            "duracao": _im_duracao_transicao(t["minutos"]),
        }

    def im_tocar_som(arquivo, volume=1.0, fadein=0):
        if arquivo:
            renpy.sound.play(arquivo, relative_volume=volume, fadein=fadein)

    def im_pagar_deslocamento(op, desl):
        """Desconta o trajeto, avança o relógio e põe o jogador no POI novo."""
        if desl and desl["minutos"]:
            store.im_minutos -= desl["minutos"]
            advance_minutes(desl["minutos"])
            reg = im_registro_semana()
            reg["minutos_usados"] += desl["minutos"]
            reg["trajeto_min"] = reg.get("trajeto_min", 0) + desl["minutos"]
            reg["trajetos"] = reg.get("trajetos", 0) + 1
        store.im_local = op["poi"]

    def im_avisar_novos(semana, rota=None):
        """Avisa (som e texto) os locais que abrem nesta semana."""
        if semana <= 1:
            return []
        novos = [__(p["nome"]) for p in im_mapa_dados(rota)["pois"] if p.get("abre", 1) == semana]
        for nome in novos:
            renpy.notify(__("Novo no mapa: {nome}").format(nome=nome))
        if novos and renpy.loadable(MAPA_SOM_NOVO_LUGAR):
            renpy.sound.play(MAPA_SOM_NOVO_LUGAR)
        return novos

    # ---------------- opções ----------------

    def _im_texto_energia(e):
        if e > 0:
            return __("+{n} energia").format(n=e)
        if e < 0:
            return __("−{n} energia").format(n=-e)
        return None

    def im_rotulo(acao, alvo, poi=None, rota=None, com_local=False):
        """Rótulo curto da ação ("Conversar com Davi", "Observar o uso")."""
        if acao == "conversar":
            r = __("Conversar com {nome}").format(nome=im_nome(alvo))
        elif acao == "ajudar":
            r = __("Ajudar {nome}").format(nome=im_nome(alvo))
        elif acao == "mentoria":
            m = mentoria_dados(rota) or {}
            k = mentoria_proximo(rota) or len(m.get("passos", []))
            r = __("Mentoria com {nome} ({k} de {n})").format(nome=im_nome(alvo), k=k, n=len(m.get("passos", [])))
        else:
            r = __(IM_ACOES[acao]["nome"])
        if com_local and poi and acao in ("observar", "estudar", "descansar"):
            p = im_poi(poi, rota)
            if p:
                r += " (" + __(p["nome"]) + ")"
        return r

    def _im_amizade_teto(cid, semana, rota=None):
        reg = im_registro_semana(semana, rota, criar=False) or {"amizade": {}}
        dado = reg["amizade"].get(cid, 0.0)
        total = sum(reg["amizade"].values())
        return dado >= IM_TETO_PESSOA or total >= IM_TETO_TOTAL

    def mentoria_disponivel(semana, rota=None):
        """(k, passo) se o próximo encontro pode acontecer nesta semana."""
        m = mentoria_dados(rota)
        k = mentoria_proximo(rota)
        if not m or not k:
            return None
        passo = m["passos"][k - 1]
        if passo["semana_min"] > semana:
            return None
        return (k, passo)

    def _im_montar_opcao(semana, poi, acao, alvo, rota, cansaco):
        base = IM_ACOES[acao]
        desl = im_trajeto(store.im_local, poi, rota)
        minutos = base["min"] + desl["minutos"]
        e = base["energia"]
        feita = im_ja_feita(semana, acao, poi, alvo, rota)
        motivo = None
        if feita:
            motivo = __("Já feito hoje")
        elif minutos > store.im_minutos:
            if desl["minutos"]:
                motivo = __("Falta tempo (precisa de {n} min: {a} + {d} de trajeto)").format(
                    n=minutos, a=base["min"], d=desl["minutos"])
            else:
                motivo = __("Falta tempo (precisa de {n} min)").format(n=minutos)
        elif e < 0 and store.energia_semana < -e:
            motivo = __("Precisa de {n} de energia").format(n=-e)
        partes = [__("{n} min").format(n=base["min"])]
        if desl["minutos"]:
            meio = __(MAPA_MEIOS.get(desl["meio"], {}).get("nome", "")).lower()
            partes[0] = __("{a} min + {d} min de trajeto ({meio}) = {n} min").format(
                a=base["min"], d=desl["minutos"], meio=meio, n=minutos)
        te = _im_texto_energia(e)
        if te:
            partes.append(te)
        partes.append(__(base["recompensa"]))
        aviso = None
        if acao in IM_AMIZADE and acao != "observar" and alvo and _im_amizade_teto(alvo, semana, rota):
            aviso = __("Teto de amizade atingido")
        recomendado = acao == "descansar" and cansaco
        return {
            "poi": poi, "acao": acao, "alvo": alvo,
            "min_acao": base["min"], "min_desloc": desl["minutos"], "minutos": minutos,
            "meio": desl["meio"], "energia": e,
            "rotulo": im_rotulo(acao, alvo, poi, rota) + ((" · " + __("Recomendado")) if recomendado else ""),
            "detalhe": " · ".join(partes),
            "ok": motivo is None, "motivo": motivo, "feita": feita,
            "recomendado": recomendado, "aviso": aviso,
            "valor": ("acao", poi, acao, alvo),
        }

    def im_opcoes(semana, todas=False, rota=None):
        """
        Opções do mapa na semana, na ordem dos locais. Cada opção é um dict:
          poi, acao, alvo, min_acao, min_desloc, minutos (ação + deslocamento),
          meio, energia (variação), rotulo, detalhe (custo e recompensa),
          ok, motivo (por que está desabilitada), feita, recomendado, aviso
          (teto de amizade), valor (o que a tela devolve:
          ("acao", poi, acao, alvo)).
        Por padrão só as disponíveis (lista vazia = nada cabe: o mapa fecha).
        todas=True inclui as desabilitadas, com o motivo escrito.
        Com Cansaço/Exaustão, "Descansar" vem primeiro e marcado "Recomendado".
        """
        rota = im_rota(rota)
        d = im_dados(semana, rota)
        if not d:
            return []
        cansaco = energia_cansaco()
        mentor = (mentoria_dados(rota) or {}).get("mentor")
        mentoria_ok = mentoria_disponivel(semana, rota) is not None
        ops = []
        for poi in im_pois(semana, rota):
            if poi["estado"] != "aberto":
                continue
            pid = poi["id"]
            pares = []
            for cid in d.get("agenda", {}).get(pid, []):
                if cid == mentor and mentoria_ok:
                    pares.append(("mentoria", cid))
                if cid in d.get("ajudar", {}):
                    pares.append(("ajudar", cid))
                pares.append(("conversar", cid))
            if pid in d.get("observar", {}):
                pares.append(("observar", pid))
            extra = d.get("estudar")
            if "estudar" in poi.get("acoes", []) and extra and extra not in store.registros:
                pares.append(("estudar", pid))
            if "descansar" in poi.get("acoes", []):
                pares.append(("descansar", pid))
            pares.sort(key=lambda par: IM_ORDEM_ACOES.index(par[0]))
            for acao, alvo in pares:
                ops.append(_im_montar_opcao(semana, pid, acao, alvo, rota, cansaco))
        if cansaco:
            ops.sort(key=lambda o: 0 if o["acao"] == "descansar" else 1)
        if todas:
            return ops
        return [o for o in ops if o["ok"]]

    def im_preparar(semana, valor, rota=None):
        """Confere o valor devolvido pela tela e devolve a opção (ou None)."""
        if not (isinstance(valor, (tuple, list)) and len(valor) == 4 and valor[0] == "acao"):
            return None
        for o in im_opcoes(semana, rota=rota):
            if tuple(o["valor"]) == tuple(valor):
                return o
        renpy.log("im_preparar: opção indisponível %r" % (valor,))
        return None

    def im_pagar_acao(op):
        """Desconta os minutos da ação e o gasto de energia (antes do conteúdo)."""
        store.im_minutos -= op["min_acao"]
        im_registro_semana()["minutos_usados"] += op["min_acao"]
        if op["energia"] < 0:
            energia_gastar(-op["energia"], IM_ACOES[op["acao"]]["nome"])

    def im_aplicar_recompensa(op, rota=None):
        """Recompensa da ação (depois do conteúdo) e registro em im_feitas."""
        rota = im_rota(rota)
        semana = store.im_semana_atual
        d = im_dados(semana, rota) or {}
        reg = im_registro_semana(semana, rota)
        acao, alvo, poi = op["acao"], op["alvo"], op["poi"]
        advance_minutes(op["min_acao"])
        if acao == "conversar":
            im_amizade(alvo, IM_AMIZADE["conversar"])
        elif acao == "observar":
            pista = d.get("observar", {}).get(poi)
            if pista:
                pista_ganhar(pista)
            cid = d.get("observar_amizade", {}).get(poi)
            if cid is None:
                quem = d.get("agenda", {}).get(poi, [])
                cid = quem[0] if quem else None
            if cid:
                im_amizade(cid, IM_AMIZADE["observar"])
        elif acao == "estudar":
            if d.get("estudar") and im_registrar_extra(d["estudar"], rota):
                reg["extra"] = d["estudar"]
        elif acao == "descansar":
            energia_ganhar(IM_ACOES["descansar"]["energia"], IM_ACOES["descansar"]["nome"])
        elif acao == "ajudar":
            im_amizade(alvo, IM_AMIZADE["ajudar"])
            pista = d.get("ajudar", {}).get(alvo)
            if pista:
                pista_ganhar(pista)
        elif acao == "mentoria":
            im_amizade(alvo, IM_AMIZADE["mentoria"])
            mentoria_avancar(rota)
        reg["acoes"].append([poi, acao, alvo])

    def im_amizade(cid, valor, rota=None):
        """
        Soma amizade respeitando os tetos da intermissão (+1,0 por pessoa e
        +2,0 no total). Fora de uma intermissão, soma sem teto. Devolve o
        quanto somou.
        """
        if not store.im_semana_atual:
            add_friendship_point(cid, valor)
            return valor
        reg = im_registro_semana(rota=rota)
        dado = reg["amizade"].get(cid, 0.0)
        total = sum(reg["amizade"].values())
        ganho = min(valor, IM_TETO_PESSOA - dado, IM_TETO_TOTAL - total)
        if ganho <= 0:
            renpy.notify(__("Teto de amizade desta tarde atingido: a conversa rende, mas a amizade com {nome} não sobe.").format(nome=im_nome(cid)))
            return 0.0
        add_friendship_point(cid, ganho)
        reg["amizade"][cid] = dado + ganho
        return ganho

    # ---------------- conteúdo por convenção de nome ----------------

    def im_label_conteudo(op, rota=None, semana=None):
        """
        Label de conteúdo da ação, na ordem (§1.6):
          im_<rota>_s<N>_<acao>_<alvo>, im_<rota>_<acao>_<alvo>,
          im_generico_<acao>. Mentoria: im_<rota>_mentoria_<k>.
        alvo = id da pessoa (conversar, ajudar) ou do local (observar,
        estudar, descansar). Quando cai no genérico, registra o nome que
        faltou em IM_DIAG.genericos e no log.
        """
        rota = im_rota(rota)
        semana = semana or store.im_semana_atual
        acao, alvo = op["acao"], op["alvo"]
        if acao == "mentoria":
            cands = ["im_%s_mentoria_%d" % (rota, mentoria_proximo(rota) or 0)]
        else:
            cands = ["im_%s_s%d_%s_%s" % (rota, semana, acao, alvo), "im_%s_%s_%s" % (rota, acao, alvo)]
        for c in cands:
            if renpy.has_label(c):
                return c
        IM_DIAG.genericos.append(cands[0])
        renpy.log("intermissao: sem conteudo para %s (usando im_generico_%s)" % (cands[0], acao))
        return "im_generico_" + acao

    def im_label_abertura(semana, rota=None):
        """im_<rota>_abertura_<N>, im_<rota>_abertura ou im_generico_abertura."""
        rota = im_rota(rota)
        for c in ("im_%s_abertura_%d" % (rota, semana), "im_%s_abertura" % rota):
            if renpy.has_label(c):
                return c
        return "im_generico_abertura"

    def im_fala_generica(op, rota=None):
        """Texto da fala genérica (narrador) quando falta o label de conteúdo."""
        rota = im_rota(rota)
        acao, alvo = op["acao"], op["alvo"]
        poi = im_poi(op["poi"], rota)
        local = __(poi["nome"]) if poi else ""
        if acao == "conversar":
            return __("{{i}}Você passa meia hora conversando com {nome} ({local}).{{/i}}").format(nome=im_nome(alvo), local=local)
        if acao == "observar":
            return __("{{i}}Você passa um tempo em {local}, observando como as pessoas trabalham de verdade. Anota o que vê, sem nomes.{{/i}}").format(local=local)
        if acao == "estudar":
            return __("{{i}}Você se acomoda em {local} e estuda com calma o tema da semana.{{/i}}").format(local=local)
        if acao == "descansar":
            if energia_cansaco():
                return __("{{i}}Você para um pouco em {local}. O corpo pede pausa, e desta vez você escuta.{{/i}}").format(local=local)
            return __("{{i}}Você para um pouco em {local}. Respira, olha em volta e deixa a cabeça descansar.{{/i}}").format(local=local)
        if acao == "ajudar":
            return __("{{i}}Você passa uma hora e meia ajudando {nome}. Dá trabalho, mas vocês resolvem juntos.{{/i}}").format(nome=im_nome(alvo))
        if acao == "mentoria":
            m = mentoria_dados(rota) or {"passos": []}
            k = mentoria_proximo(rota) or 0
            resumo = __(m["passos"][k - 1]["resumo"]) if 0 < k <= len(m["passos"]) else ""
            return __("{{i}}Encontro {k} de {n} com {nome}: {resumo}.{{/i}}").format(k=k, n=len(m["passos"]), nome=im_nome(alvo), resumo=resumo)
        return ""

    def im_fala_offline(cid):
        """(personagem, fala) da lista offline do contato, ou None."""
        falas = AMIGOS_DATA.get(cid, {}).get("offline") or []
        quem = getattr(store, cid, None)
        if not falas or not isinstance(quem, ADVCharacter):
            return None
        semana = max(1, store.im_semana_atual)
        return (quem, falas[(semana - 1) % len(falas)])

    def im_mostrar_local(op, rota=None):
        """Fundo do local da ação (a cena de conteúdo pode trocar)."""
        bg = im_poi_bg(op["poi"], store.im_semana_atual, rota)
        if bg:
            renpy.scene()
            renpy.show(("bg", bg))

    def im_tocar_musica(rota=None):
        nome = im_mapa_dados(rota).get("musica")
        arquivo = getattr(store, nome, None) if nome else None
        if arquivo:
            renpy.music.play(arquivo, fadein=1.0, if_changed=True)

    def im_restaurar_musica(antes):
        if antes:
            renpy.music.play(antes, fadein=1.0, if_changed=True)
        else:
            renpy.music.stop(fadeout=1.0)

    # ---------------- registros extras ----------------

    def extras_rota(rota=None):
        """Lista de (extra, descoberto) da rota, na ordem das semanas."""
        return [(e, e["id"] in store.registros) for e in route_data(rota).get("extras", [])]

    def extras_contagem(rota=None):
        dados = extras_rota(rota)
        return (sum(1 for e, ok in dados if ok), len(dados))

    def im_registrar_extra(rid, rota=None):
        """
        Grava um registro extra (opcional) em `registros` e avisa "Anotado no
        notebook (extra): ...". Não conta em registros_contagem().
        """
        if rid in store.registros:
            return False
        for e in route_data(rota).get("extras", []):
            if e["id"] == rid:
                store.registros.add(rid)
                renpy.notify(__("Anotado no notebook (extra): {titulo}").format(titulo=__(e["title"])))
                return True
        renpy.log("im_registrar_extra: id desconhecido na rota %s: %s" % (im_rota(rota), rid))
        return False

    # ---------------- pistas ----------------

    def pista_dados(pid, rota=None):
        """Dict da pista (procura na rota atual e depois nas outras)."""
        p = route_data(rota).get("pistas", {}).get(pid)
        if p:
            return p
        for r in ROUTES:
            p = ROUTES[r].get("pistas", {}).get(pid)
            if p:
                return p
        return None

    def pista_ganhar(pid, semana=None):
        """
        Guarda a pista se a semana não passou de "ate_semana" (fora dessa
        janela a ação acontece, mas a pista não é dada). Avisa "Pista: ...".
        Devolve True se gravou agora.
        """
        p = pista_dados(pid)
        if p is None:
            renpy.log("pista_ganhar: pista desconhecida: %s" % pid)
            return False
        if pid in store.pistas:
            return False
        semana = semana or store.im_semana_atual
        if semana and semana > p.get("ate_semana", 8):
            return False
        store.pistas.add(pid)
        if store.im_semana_atual:
            im_registro_semana()["pistas"].append(pid)
        renpy.notify(__("Pista: {titulo}").format(titulo=__(p["titulo"])))
        return True

    def pista_tem(pid):
        """True se o jogador viu a pista (para opções extras de menu, formato 2)."""
        return pid in store.pistas

    def pista_disponivel(pid):
        """Tem a pista e ainda não a usou (pista_lembrar só aparece assim)."""
        return pid in store.pistas and pid not in store.pistas_usadas

    def pista_usar(pid):
        """Marca a pista como usada. Devolve True se marcou agora."""
        if pid in store.pistas_usadas:
            return False
        store.pistas_usadas.add(pid)
        return True

    # ---------------- mentoria ----------------

    def mentoria_dados(rota=None):
        return route_data(rota).get("mentoria")

    def mentoria_feitos(rota=None):
        return store.mentoria_passos.get(im_rota(rota), 0)

    def mentoria_proximo(rota=None):
        """Número do próximo encontro (1..5) ou None se o arco acabou."""
        m = mentoria_dados(rota)
        if not m:
            return None
        k = mentoria_feitos(rota) + 1
        return k if k <= len(m["passos"]) else None

    def mentoria_avancar(rota=None):
        """
        Registra o encontro: dá a pista do passo (se houver) e, no último,
        a conquista extra. Devolve o número de encontros feitos.
        """
        rota = im_rota(rota)
        m = mentoria_dados(rota)
        k = mentoria_proximo(rota)
        if not m or not k:
            return mentoria_feitos(rota)
        store.mentoria_passos[rota] = k
        passo = m["passos"][k - 1]
        if passo.get("pista"):
            pista_ganhar(passo["pista"])
        if k == len(m["passos"]):
            cid = m.get("conquista") or ("mentoria_conq_" + rota)
            for a in conquistas_extra(rota):
                if a["id"] == cid:
                    setattr(store, a["var"], True)
                    renpy.notify(__("Conquista do tempo livre: {titulo}").format(titulo=__(a["title"])))
        return k

    def conquistas_extra(rota=None):
        """Conquistas do tempo livre (fora de route_achievements())."""
        return list(route_data(rota).get("conquistas_extra", []))

    def conquistas_extra_obtidas(rota=None):
        return [a for a in conquistas_extra(rota) if achievement_unlocked(a)]

    # ---------------- resumos ----------------

    def im_resumo_dados(semana, rota=None):
        """Dados da tela de fechamento da intermissão."""
        rota = im_rota(rota)
        reg = im_registro_semana(semana, rota)
        acoes = [im_rotulo(a, t, p, rota, com_local=True) for p, a, t in reg["acoes"]]
        amizade = [(im_nome(c), v) for c, v in reg["amizade"].items() if v]
        pistas_novas = [__(pista_dados(p)["titulo"]) for p in reg["pistas"] if pista_dados(p)]
        extra = None
        if reg["extra"]:
            for e in route_data(rota).get("extras", []):
                if e["id"] == reg["extra"]:
                    extra = __(e["title"])
        # "Ficou para outra vez": o que estava no mapa e não foi feito.
        fora = []
        vistos = set()
        for o in im_opcoes(semana, todas=True, rota=rota):
            if o["feita"]:
                continue
            r = im_rotulo(o["acao"], o["alvo"], o["poi"], rota, com_local=True)
            if r not in vistos:
                vistos.add(r)
                fora.append(r)
        return {
            "acoes": acoes, "amizade": amizade, "pistas": pistas_novas, "extra": extra,
            "energia_inicio": reg["energia_inicio"], "energia": store.energia_semana,
            "minutos_usados": reg["minutos_usados"], "bloco": reg["bloco"],
            "encerrou_cedo": reg["encerrou_cedo"], "fora": fora[:3],
            "trajeto_min": reg.get("trajeto_min", 0), "trajetos": reg.get("trajetos", 0),
        }

    def im_houve_tempo_livre(rota=None):
        return bool(store.im_feitas.get(im_rota(rota)))

    def tempo_livre_resumo(rota=None):
        """Números do tempo livre para o resumo do epílogo e o ponto de parada."""
        rota = im_rota(rota)
        regs = store.im_feitas.get(rota, {})
        m = mentoria_dados(rota) or {"passos": []}
        pistas_rota = set(route_data(rota).get("pistas", {}))
        return {
            "intermissoes": sum(1 for r in regs.values() if r.get("concluida") and not r.get("pulada")),
            "puladas": sum(1 for r in regs.values() if r.get("pulada")),
            "mentoria": (mentoria_feitos(rota), len(m["passos"])),
            "pistas": len(store.pistas & pistas_rota),
            "pistas_total": len(pistas_rota),
            "pistas_usadas": len(store.pistas_usadas & pistas_rota),
            "extras": extras_contagem(rota),
            "conquistas": [__(a["title"]) for a in conquistas_extra_obtidas(rota)],
        }

    def im_parada_preparar(semana, rota=None):
        """
        Ponto de parada (§8.2): nome do save da próxima semana e os registros
        ganhos desde o último ponto. Devolve os títulos novos.
        """
        rota = im_rota(rota)
        store.save_name = __("Semana {n} · {empresa}").format(n=semana + 1, empresa=__(route_data(rota)["empresa"]))
        titulos = []
        for rec in route_records(rota) + route_data(rota).get("extras", []):
            if rec["id"] in store.registros and rec["id"] not in store.im_registros_vistos:
                titulos.append(__(rec["title"]))
        store.im_registros_vistos = set(store.registros)
        return titulos

    # ---------------- validação (testes) ----------------

    def im_validar_mapa():
        """Problemas nos dados da cidade (data/mapa_cidade.rpy); vazia = ok."""
        erros = []
        if MAPA_CASA not in MAPA_LUGARES:
            erros.append("MAPA_CASA desconhecida %s" % MAPA_CASA)
        for lid, L in MAPA_LUGARES.items():
            if L.get("bairro") not in MAPA_BAIRROS:
                erros.append("lugar %s em bairro desconhecido %r" % (lid, L.get("bairro")))
            if L.get("interno") and L["interno"] not in MAPA_MEIOS:
                erros.append("lugar %s com meio interno desconhecido %s" % (lid, L["interno"]))
        bairros = sorted(MAPA_BAIRROS)
        for i, a in enumerate(bairros):
            for b in bairros[i + 1:]:
                if not _im_par(MAPA_TRAJETOS, a, b):
                    erros.append("sem tempo entre %s e %s" % (a, b))
        meios = [v[1] for v in MAPA_TRAJETOS.values()] + [v[1] for v in MAPA_TRAJETOS_LUGAR.values()]
        meios += list(MAPA_MEIO_BAIRRO.values()) + ["calcada"]
        for meio in meios:
            if meio not in MAPA_MEIOS:
                erros.append("meio desconhecido %s" % meio)
        for par in MAPA_TRAJETOS_LUGAR:
            for lid in par:
                if lid not in MAPA_LUGARES:
                    erros.append("trajeto com lugar desconhecido %s" % lid)
        icones = list(v[1] for v in MAPA_ATIVIDADES.values()) + list(MAPA_ICONE_ACAO.values())
        for icone in icones:
            if icone not in MAPA_ICONES:
                erros.append("arquivo de ícone fora dos %d: %s" % (len(MAPA_ICONES), icone))
        return erros

    def im_validar_dados(rota):
        """Lista de problemas nos dados de tempo livre da rota (vazia = ok)."""
        erros = []
        dados = ROUTES[rota]
        if "mapa" not in dados or "intermissoes" not in dados:
            return ["%s: sem mapa ou intermissoes" % rota]
        validos = set(route_contact_ids(rota)) | set(dados.get("stakeholders", []))
        pois = {p["id"]: p for p in dados["mapa"]["pois"]}
        for p in pois.values():
            if p.get("lugar") not in MAPA_LUGARES:
                erros.append("%s: poi %s em lugar desconhecido %r" % (rota, p["id"], p.get("lugar")))
            if p.get("icone", "programando") not in MAPA_ATIVIDADES:
                erros.append("%s: poi %s com ícone desconhecido" % (rota, p["id"]))
            if not p.get("sub"):
                erros.append("%s: poi %s sem sub" % (rota, p["id"]))
        for lid in list(dados["mapa"].get("lugares_fechados", {})) + [v[0] for v in dados["mapa"].get("longe", {}).values()]:
            if lid not in MAPA_LUGARES:
                erros.append("%s: lugar desconhecido %s" % (rota, lid))
        if dados["mapa"].get("inicio") not in pois:
            erros.append("%s: mapa['inicio'] não é um poi" % rota)
        else:
            # Do lugar-base a cada lugar da rota (e a casa) há tempo definido.
            base = pois[dados["mapa"]["inicio"]].get("lugar")
            for lid in set(p.get("lugar") for p in pois.values()) | set([MAPA_CASA]):
                if base in MAPA_LUGARES and lid in MAPA_LUGARES and lid != base and not im_trajeto_lugares(base, lid):
                    erros.append("%s: sem tempo de %s até %s" % (rota, base, lid))
            for lid in dados["mapa"].get("lugares_fechados", {}):
                if lid in set(p.get("lugar") for p in pois.values()):
                    erros.append("%s: lugar %s fechado e com poi" % (rota, lid))
        pistas_d = dados.get("pistas", {})
        extras_ids = set(e["id"] for e in dados.get("extras", []))
        mentor = (dados.get("mentoria") or {}).get("mentor")
        semanas_mentor = 0
        for n in range(1, 9):
            d = dados["intermissoes"].get(n)
            if not d:
                erros.append("%s: falta a semana %d" % (rota, n))
                continue
            ini = d["inicio"][0] * 60 + d["inicio"][1]
            if ini + d["bloco"] > 24 * 60:
                erros.append("%s s%d: termina depois da meia-noite" % (rota, n))
            for pid, quem in d.get("agenda", {}).items():
                if pid not in pois:
                    erros.append("%s s%d: local desconhecido %s" % (rota, n, pid))
                    continue
                if pois[pid].get("abre", 1) > n:
                    erros.append("%s s%d: %s ainda não abriu" % (rota, n, pid))
                if pid in d.get("fechados", {}) and quem:
                    erros.append("%s s%d: gente em local fechado %s" % (rota, n, pid))
                for cid in quem:
                    if cid not in validos:
                        erros.append("%s s%d: pessoa fora da rota %s" % (rota, n, cid))
                if mentor in quem and n >= 2:
                    semanas_mentor += 1
            presentes = set(c for q in d.get("agenda", {}).values() for c in q)
            for cid, pista in d.get("ajudar", {}).items():
                if cid not in presentes:
                    erros.append("%s s%d: ajudar %s, que não está na agenda" % (rota, n, cid))
                if pista and (pista not in pistas_d or pistas_d[pista]["ate_semana"] < n):
                    erros.append("%s s%d: pista de ajudar inválida %s" % (rota, n, pista))
            for pid, pista in d.get("observar", {}).items():
                if pid not in pois or pois[pid].get("abre", 1) > n or pid in d.get("fechados", {}):
                    erros.append("%s s%d: observar em local indisponível %s" % (rota, n, pid))
                if pista and (pista not in pistas_d or pistas_d[pista]["ate_semana"] < n):
                    erros.append("%s s%d: pista de observar inválida %s" % (rota, n, pista))
            if d.get("estudar") and d["estudar"] not in extras_ids:
                erros.append("%s s%d: extra desconhecido %s" % (rota, n, d["estudar"]))
            # Mentoria + observar com pista no mesmo local precisam caber no
            # bloco, com o trajeto a partir do início (mapa-cidade.md §5).
            if mentor and n >= 2:
                for pid, quem in d.get("agenda", {}).items():
                    if mentor in quem and d.get("observar", {}).get(pid):
                        ida = im_trajeto(d.get("inicio_poi") or dados["mapa"].get("inicio"), pid, rota)["minutos"]
                        if ida + IM_ACOES["mentoria"]["min"] + IM_ACOES["observar"]["min"] > d["bloco"]:
                            erros.append("%s s%d: mentoria + observar em %s não cabem no bloco" % (rota, n, pid))
            for cid, (icone, frase) in d.get("atividade", {}).items():
                if cid not in presentes:
                    erros.append("%s s%d: atividade de quem não está %s" % (rota, n, cid))
                if icone not in MAPA_ATIVIDADES:
                    erros.append("%s s%d: ícone desconhecido %s" % (rota, n, icone))
        m = dados.get("mentoria")
        if m:
            if semanas_mentor < len(m["passos"]):
                erros.append("%s: mentor em só %d semanas (2 a 8)" % (rota, semanas_mentor))
            for passo in m["passos"]:
                pista = passo.get("pista")
                if pista and (pista not in pistas_d or pistas_d[pista]["ate_semana"] < passo["semana_min"]):
                    erros.append("%s: pista de mentoria inválida %s" % (rota, pista))
            ids_extra = [a["id"] for a in dados.get("conquistas_extra", [])]
            if (m.get("conquista") or "mentoria_conq_" + rota) not in ids_extra:
                erros.append("%s: conquista da mentoria fora de conquistas_extra" % rota)
        for a in dados.get("conquistas_extra", []):
            if not hasattr(store, a["var"]):
                erros.append("%s: conquista extra sem default %s" % (rota, a["var"]))
        return erros
