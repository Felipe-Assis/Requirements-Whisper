# ambiguidade.rpy
# -------------------------------
# CAÇA À AMBIGUIDADE: marcar palavras vagas e torná-las verificáveis
# -------------------------------
# Uso nas cenas (caminho principal, nunca numa intermissão):
#     call amb_atividade("st_amb_total") from _amb_st09
# Dados por rota em data/ambiguidade_dados.rpy (ROUTES[rota]["ambiguidades"]).
#
# Etapas:
# 1. Marcar (tela amb_marcar, fase "marcar"): vagas e iscas são botões; o
#    texto comum não é clicável. Marcado = colchetes + sublinhado, e o estado
#    vai escrito no alt. Teclado: setas, Enter alterna, botão Conferir (Tab
#    no Ren'Py é o atalho de pular falas, não de foco).
# 2. Conferir: "Você achou 2 de 3 palavras vagas...". Se faltou vaga, diz
#    quantas e deixa marcar de novo; na segunda conferência as que faltaram
#    aparecem indicadas com a explicação (fase "conferido").
# 3. Tornar verificável: um menu (tipo="trabalho") por vaga, com as 3
#    reescritas numa ordem embaralhada fixa por id. Distrator mostra a
#    consequência e volta ao menu.
# 4. Resultado (fase "resultado"): o requisito reescrito.
# decisao() só na primeira tentativa: "<aid>_marcar" (achou todas as vagas sem
# marcar isca na primeira conferência) e "<aid>_<termo>" (reescrita adequada
# de primeira). Chamar de novo com o mesmo id não sobrescreve nada disso.
#
# Autopiloto: na tela amb_marcar, fase "marcar" (scope["fase"]), devolva
# ("conferir", [termos marcados]); nas fases "conferido" e "resultado",
# devolva True. Os menus de reescrita são a tela choice de sempre.

# aid -> {"marcadas_primeira": [termos], "iscas_primeira": [termos],
#         "faltaram": [vagas que o jogo precisou indicar], "trocas": {termo: índice
#         da reescrita escolhida em "opcoes"}, "primeira_ok": {termo: bool},
#         "concluido": bool}
default amb_resultados = {}

# Atividade em curso: {"aid", "marcadas", "conferencias", "retorno", "fila",
# "escolha", "feedback"}. Fica no save: retomar no meio da atividade funciona.
default amb_atual = {}

init python:
    import zlib as _amb_zlib
    import random as _amb_random

    def amb_dados(aid):
        """Dados da atividade `aid`, procurando em todas as rotas."""
        for rota in ROUTES:
            dados = ROUTES[rota].get("ambiguidades", {})
            if aid in dados:
                return dados[aid]
        raise Exception("amb: atividade desconhecida: %s" % aid)

    def amb_termos(aid, tipo=None):
        """Termos destacados na ordem do texto: [(tipo, termo, texto)]."""
        return [s for s in amb_dados(aid)["segmentos"]
                if isinstance(s, tuple) and (tipo is None or s[0] == tipo)]

    def amb_vagas(aid):
        return [s[1] for s in amb_termos(aid, "vaga")]

    def amb_texto_termo(aid, termo):
        for s in amb_termos(aid):
            if s[1] == termo:
                return __(s[2])
        return termo

    def amb_iniciar(aid):
        amb_dados(aid)
        store.amb_atual = {"aid": aid, "marcadas": [], "conferencias": 0, "retorno": {},
                           "fila": [], "escolha": None, "feedback": None}
        if aid not in store.amb_resultados:
            store.amb_resultados[aid] = {"trocas": {}, "primeira_ok": {}, "concluido": False}

    def amb_conferir(aid, retorno=None):
        """
        Confere as marcas (as do retorno da tela, ou as atuais). Devolve
        "rever" (faltou vaga na primeira conferência) ou "fechado".
        """
        if isinstance(retorno, (tuple, list)) and len(retorno) == 2 and retorno[0] == "conferir":
            marcadas = list(retorno[1])
        else:
            marcadas = list(store.amb_atual.get("marcadas", []))
        vagas = amb_vagas(aid)
        iscas = [s[1] for s in amb_termos(aid, "isca")]
        marcadas = [t for t in vagas + iscas if t in marcadas]
        achadas = [t for t in vagas if t in marcadas]
        iscas_marcadas = [t for t in iscas if t in marcadas]
        faltam = [t for t in vagas if t not in marcadas]

        atual = store.amb_atual
        atual["marcadas"] = marcadas
        atual["conferencias"] += 1
        n = atual["conferencias"]

        res = store.amb_resultados[aid]
        if "marcadas_primeira" not in res:
            res["marcadas_primeira"] = achadas
            res["iscas_primeira"] = iscas_marcadas
            decisao(aid + "_marcar", not faltam and not iscas_marcadas)

        fase = "rever" if (faltam and n < 2) else "fechado"
        if fase == "fechado" and "faltaram" not in res:
            res["faltaram"] = faltam
        atual["retorno"] = {"conferencia": n, "achadas": len(achadas), "total": len(vagas),
                            "iscas": iscas_marcadas, "faltam": faltam, "fase": fase}
        return fase

    def amb_resumo(ret):
        """Frase da conferência: quantas vagas achou e quantas iscas marcou."""
        if not ret:
            return ""
        if ret["achadas"] == 1:
            frase = __("Você achou 1 de {total} palavras vagas").format(total=ret["total"])
        else:
            frase = __("Você achou {achadas} de {total} palavras vagas").format(achadas=ret["achadas"], total=ret["total"])
        k = len(ret["iscas"])
        if k == 1:
            frase += __(" e marcou 1 termo que não é vago")
        elif k > 1:
            frase += __(" e marcou {k} termos que não são vagos").format(k=k)
        return frase + "."

    def amb_ordem(aid, termo):
        # Ordem embaralhada fixa por id: a mesma em toda partida.
        n = len(amb_dados(aid)["vagas"][termo]["opcoes"])
        ordem = list(range(n))
        _amb_random.Random(_amb_zlib.crc32((aid + ":" + termo).encode("utf-8"))).shuffle(ordem)
        return ordem

    def amb_pergunta(aid, termo):
        vaga = amb_dados(aid)["vagas"][termo]
        return __("“{termo}”: {porque} Como tornar este trecho verificável?").format(
            termo=amb_texto_termo(aid, termo), porque=__(vaga["porque"]))

    def amb_menu(aid, termo):
        opcoes = amb_dados(aid)["vagas"][termo]["opcoes"]
        return [(__(opcoes[i]["texto"]), i) for i in amb_ordem(aid, termo)]

    def amb_escolher(aid, termo, i):
        """
        Registra a escolha da reescrita. Adequada: grava a troca, tira o termo
        da fila e devolve None. Distrator: devolve o feedback para mostrar.
        """
        opcao = amb_dados(aid)["vagas"][termo]["opcoes"][i]
        res = store.amb_resultados[aid]
        if termo not in res["primeira_ok"]:
            res["primeira_ok"][termo] = bool(opcao.get("adequada"))
            decisao(aid + "_" + termo, bool(opcao.get("adequada")))
        if opcao.get("adequada"):
            res["trocas"][termo] = i
            if termo in store.amb_atual["fila"]:
                store.amb_atual["fila"].remove(termo)
            return None
        return __(opcao["feedback"]) + " " + __("Escolha outra reescrita.")

    def amb_adequada(aid, termo):
        opcoes = amb_dados(aid)["vagas"][termo]["opcoes"]
        return [i for i, o in enumerate(opcoes) if o.get("adequada")][0]

    def amb_resultado(aid):
        """Requisito reescrito, com as trocas em negrito entre colchetes."""
        dados = amb_dados(aid)
        if dados.get("resultado"):
            return __(dados["resultado"])
        trocas = store.amb_resultados.get(aid, {}).get("trocas", {})
        partes = []
        for s in dados["segmentos"]:
            if isinstance(s, tuple) and s[0] == "vaga":
                i = trocas.get(s[1], amb_adequada(aid, s[1]))
                partes.append("{b}[[" + __(dados["vagas"][s[1]]["opcoes"][i]["texto"]) + "]{/b}")
            elif isinstance(s, tuple):
                partes.append(__(s[2]))
            else:
                partes.append(__(s))
        return "".join(partes)

    def amb_concluir(aid):
        store.amb_resultados[aid]["concluido"] = True

    def amb_tokens(aid):
        """
        Texto corrido em pedaços para um hbox que quebra linha: ("txt", palavra)
        com o espaço seguinte já incluído (espaço rígido), ("esp",) para um
        espaço antes de um termo e ("termo", tipo, termo, texto).
        """
        tokens = []
        for s in amb_dados(aid)["segmentos"]:
            if isinstance(s, tuple):
                tokens.append(("termo",) + tuple(s))
                continue
            s = __(s)
            if s[:1].isspace():
                tokens.append(("esp",))
            palavras = s.split()
            for k, p in enumerate(palavras):
                fim = (k < len(palavras) - 1) or s[-1:].isspace()
                tokens.append(("txt", p + (u" " if fim else "")))
        return tokens

    def amb_validar(aid):
        """Lista de problemas nos dados (vazia = ok). Usada pelos testes."""
        erros = []
        d = amb_dados(aid)
        vagas = amb_vagas(aid)
        iscas = [s[1] for s in amb_termos(aid, "isca")]
        if not (2 <= len(vagas) <= 4):
            erros.append("%s: %d vagas (esperado 2 a 4)" % (aid, len(vagas)))
        if set(vagas) != set(d["vagas"]):
            erros.append("%s: vagas do texto e do dicionário diferem" % aid)
        if set(iscas) != set(d.get("iscas", {})):
            erros.append("%s: iscas do texto e do dicionário diferem" % aid)
        for termo, v in d["vagas"].items():
            adequadas = [o for o in v["opcoes"] if o.get("adequada")]
            if len(adequadas) != 1 or len(v["opcoes"]) != 3:
                erros.append("%s/%s: precisa de 3 opções com 1 adequada" % (aid, termo))
            for o in v["opcoes"]:
                if not o.get("adequada") and not o.get("feedback"):
                    erros.append("%s/%s: distrator sem feedback" % (aid, termo))
            if not v.get("porque"):
                erros.append("%s/%s: sem porque" % (aid, termo))
        return erros


label amb_atividade(aid):
    $ amb_iniciar(aid)

label .marcar:
    call screen amb_marcar(aid, "marcar")
    if amb_conferir(aid, _return) == "rever":
        jump .marcar
    call screen amb_marcar(aid, "conferido")
    $ amb_atual["fila"] = amb_vagas(aid)

label .trocar:
    if not amb_atual["fila"]:
        jump .fim
    $ narrator(amb_pergunta(aid, amb_atual["fila"][0]), interact=False)
    $ amb_atual["escolha"] = renpy.display_menu(amb_menu(aid, amb_atual["fila"][0]), _kwargs={"tipo": "trabalho"})
    $ amb_atual["feedback"] = amb_escolher(aid, amb_atual["fila"][0], amb_atual["escolha"])
    if amb_atual["feedback"]:
        $ narrator(amb_atual["feedback"])
    jump .trocar

label .fim:
    $ amb_concluir(aid)
    call screen amb_marcar(aid, "resultado")
    return


# -------------------------------
# Tela
# -------------------------------
style amb_termo is button:
    background Solid("#2b3d50")
    hover_background Solid(gui.accent_color)
    selected_background Solid("#6b4a12")
    selected_hover_background Solid(gui.accent_color)
    padding (8, 2, 8, 2)

style amb_termo_text is text:
    color "#ffffff"
    hover_color "#101820"
    selected_hover_color "#101820"

screen amb_marcar(aid, fase="marcar"):
    modal True
    zorder 130

    $ maior = texto_maior_ativo()
    $ tam = 40 if maior else 32
    $ tam_ui = 30 if maior else 25
    $ esp = int(tam * 0.3)
    $ dados = amb_dados(aid)
    $ ret = amb_atual.get("retorno", {})
    $ marcadas = amb_atual.get("marcadas", [])
    $ termos_ok = [s[1] for s in amb_termos(aid, "vaga")]
    $ tokens = amb_tokens(aid)
    $ primeiro = [tk[2] for tk in tokens if tk[0] == "termo"][0]

    add Solid("#000000c8")

    frame:
        style "nb_painel"
        align (0.5, 0.5)
        xsize 1640
        ysize 1000
        padding (48, 32)

        vbox:
            spacing 16
            text _("Caça à ambiguidade") style "nb_titulo"
            text dados["contexto"] style "nb_dica" size tam_ui italic True

            viewport:
                style_prefix "nb"
                id "amb_rolagem"
                ysize (700 if fase != "resultado" else 640)
                xfill True
                mousewheel True
                draggable True
                pagekeys True
                scrollbars "vertical"
                vscrollbar_unscrollable "hide"
                # A barra não recebe foco do teclado: as setas ficam nos botões.
                vscrollbar_keyboard_focus False
                vbox:
                    spacing 18
                    xsize 1500

                    if fase == "marcar":
                        text _("Marque os trechos que cada pessoa leria de um jeito: os que não dá para testar como estão. Alguns termos destacados parecem vagos, mas já estão definidos.") style "nb_texto" size tam_ui xmaximum 1480

                    if fase == "resultado":
                        text _("Requisito reescrito") style "nb_secao" size tam_ui
                        frame:
                            style "nb_cartao"
                            text amb_resultado(aid) style "nb_texto" size tam xmaximum 1430 line_spacing 8
                        text _("Cada trecho entre colchetes agora tem um resultado que alguém consegue conferir.") style "nb_dica" size tam_ui xmaximum 1480
                    else:
                        frame:
                            style "nb_cartao"
                            hbox:
                                box_wrap True
                                box_wrap_spacing 10
                                spacing 0
                                # xmaximum, não xsize: com largura mínima, o hbox espalha a
                                # sobra de cada linha entre as palavras.
                                xmaximum 1430
                                for tk in tokens:
                                    if tk[0] == "esp":
                                        null width esp
                                    elif tk[0] == "txt":
                                        text tk[1] style "nb_texto" size tam yalign 0.5
                                    elif fase == "marcar":
                                        $ marcado = tk[2] in marcadas
                                        button:
                                            style "amb_termo"
                                            id ("amb_termo_" + tk[2])
                                            yalign 0.5
                                            selected marcado
                                            default_focus (tk[2] == primeiro)
                                            alt ((__(tk[3]) + __(", marcada como vaga")) if marcado else (__(tk[3]) + __(", não marcada")))
                                            action ToggleSetMembership(amb_atual["marcadas"], tk[2])
                                            if marcado:
                                                text ("[[" + __(tk[3]) + "]") style "amb_termo_text" size tam bold True underline True
                                            else:
                                                text tk[3] style "amb_termo_text" size tam
                                    elif tk[1] == "vaga":
                                        text ("[[" + __(tk[3]) + "]") style "nb_texto" size tam bold True underline True color "#ffd36b" yalign 0.5
                                    elif tk[2] in marcadas:
                                        text ("{s}" + __(tk[3]) + "{/s}") style "nb_texto" size tam color "#c0c8d0" yalign 0.5
                                    else:
                                        text tk[3] style "nb_texto" size tam yalign 0.5

                    if fase == "marcar":
                        if marcadas:
                            text (__("Marcados agora: ") + ", ".join(amb_texto_termo(aid, t) for t in marcadas) + " ({n})".format(n=len(marcadas))):
                                style "nb_texto"
                                size tam_ui
                                id "amb_estado"
                                xmaximum 1480
                        else:
                            text _("Nada marcado ainda.") style "nb_texto" size tam_ui id "amb_estado"

                    if ret and fase != "resultado":
                        frame:
                            style "nb_cartao"
                            vbox:
                                spacing 10
                                text amb_resumo(ret) style "nb_secao" size tam_ui id "amb_resumo" xmaximum 1420
                                for t in ret["iscas"]:
                                    text (__("“{termo}” não é vago: ").format(termo=amb_texto_termo(aid, t)) + __(dados["iscas"][t])) style "nb_texto" size tam_ui xmaximum 1420
                                if fase == "marcar" and ret["faltam"]:
                                    if len(ret["faltam"]) == 1:
                                        text _("Falta 1 trecho vago. Releia o requisito, marque e confira de novo.") style "nb_texto" size tam_ui color "#ffd36b" xmaximum 1420
                                    else:
                                        text __("Faltam {n} trechos vagos. Releia o requisito, marque e confira de novo.").format(n=len(ret["faltam"])) style "nb_texto" size tam_ui color "#ffd36b" xmaximum 1420
                                if fase == "conferido":
                                    for t in termos_ok:
                                        if t in ret["faltam"]:
                                            text (__("[[{termo}] · vago (indicado agora): ").format(termo=amb_texto_termo(aid, t)) + __(dados["vagas"][t]["porque"])) style "nb_texto" size tam_ui xmaximum 1420
                                        else:
                                            text (__("[[{termo}] · vago (você marcou): ").format(termo=amb_texto_termo(aid, t)) + __(dados["vagas"][t]["porque"])) style "nb_texto" size tam_ui xmaximum 1420
                                    text _("Agora, um trecho de cada vez: escolha como torná-lo verificável.") style "nb_dica" size tam_ui xmaximum 1420

            hbox:
                spacing 24
                if fase == "marcar":
                    textbutton _("Conferir"):
                        style "nb_botao"
                        text_size tam_ui
                        id "amb_conferir"
                        action Return(("conferir", list(marcadas)))
                    text _("Setas escolhem um termo; Enter marca ou desmarca.") style "nb_dica" size (tam_ui - 4) yalign 0.5
                else:
                    textbutton _("Continuar"):
                        style "nb_botao"
                        text_size tam_ui
                        id "amb_continuar"
                        default_focus True
                        action Return(True)
