# rastreabilidade.rpy
# -------------------------------
# QUADRO DE RASTREABILIDADE: requisito -> critério -> teste
# -------------------------------
# Uso nas cenas (caminho principal, nunca numa intermissão):
#     call rast_atividade("st_rast_exclusao") from _rast_st16
#     if rast_lacuna_achada("st_rast_exclusao"):
#         ...
#     call rast_lembrar("co_rast_farol") from _rl_co17_rbac   # semana de testes
# Dados por rota em data/rastreabilidade_dados.rpy (ROUTES[rota]["rastreabilidade"]).
#
# Tela rast_quadro: requisitos e testes à esquerda; cada critério com dois
# seletores ("Requisito: R2", "Teste: T4 / nenhum teste cobre"). Clique ou
# Enter abre a escolha; com o seletor em foco, setas esquerda/direita trocam
# o valor. Cada linha repete a ligação em texto ("C4 → R2 → sem teste").
# Conferir: ligação errada ganha "(confira ...)" e a explicação; corrige e
# confere quantas vezes quiser. A lacuna nunca é revelada: escolher um teste
# nela não ganha "(confira)"; na primeira conferência só aparece "Todo
# critério tem teste?"; da segunda em diante, com as ligações certas, o quadro
# fecha ("Quadro conferido") e mostra a cobertura por requisito.
# decisao() só na primeira conferência: "<qid>_ligacoes" e "<qid>_lacuna".
#
# Autopiloto: na tela rast_quadro, fase "quadro" (scope["fase"]), devolva
# ("conferir", {"C1": ["R1", "T1"], ..., "C4": ["R2", None]}) (None = nenhum
# teste cobre); na fase "fechado", devolva True. rast_respostas(qid) dá as
# ligações certas com a lacuna. O menu de rast_lembrar é a tela choice.

# qid -> {"ligacoes": {cid: [req, teste]}, "conferencias": int,
#         "primeira": {"ligacoes_ok": bool, "lacuna_ok": bool},
#         "lacuna_achada": bool, "concluido": bool, "lembrado": bool}
default rast_quadros = {}

# Quadro em curso: {"qid", "ligacoes", "conferencias", "confira": {cid: [req
# errado, teste errado]}, "msgs": [textos], "lacuna_vista", "fechado"}.
default rast_atual = {}

init python:

    def rast_dados(qid):
        """Dados do quadro `qid`, procurando em todas as rotas."""
        for rota in ROUTES:
            dados = ROUTES[rota].get("rastreabilidade", {})
            if qid in dados:
                return dados[qid]
        raise Exception("rast: quadro desconhecido: %s" % qid)

    def rast_criterio(qid, cid):
        for c in rast_dados(qid)["criterios"]:
            if c["id"] == cid:
                return c
        return None

    def rast_iniciar(qid):
        dados = rast_dados(qid)
        # "" = ainda não escolhido; None (só no teste) = nenhum teste cobre.
        store.rast_atual = {"qid": qid, "conferencias": 0, "confira": {}, "msgs": [],
                            "lacuna_vista": False, "fechado": False,
                            "ligacoes": {c["id"]: ["", ""] for c in dados["criterios"]}}
        if qid not in store.rast_quadros:
            store.rast_quadros[qid] = {"ligacoes": {}, "conferencias": 0, "lacuna_achada": False,
                                       "concluido": False, "lembrado": False}

    def rast_completo():
        return all(l[0] != "" and l[1] != "" for l in store.rast_atual["ligacoes"].values())

    def rast_respostas(qid, lacuna=True):
        """Ligações certas ({cid: [req, teste]}); lacuna=False põe um teste na lacuna."""
        dados = rast_dados(qid)
        primeiro_teste = dados["testes"][0]["id"]
        return {c["id"]: [c["de"], c["teste"] if (c["teste"] or lacuna) else primeiro_teste]
                for c in dados["criterios"]}

    def rast_conferir(qid, retorno=None):
        """
        Confere o quadro (as ligações do retorno da tela, ou as atuais).
        Devolve True quando o quadro fecha.
        """
        dados = rast_dados(qid)
        atual = store.rast_atual
        if isinstance(retorno, (tuple, list)) and len(retorno) == 2 and retorno[0] == "conferir":
            for cid, par in dict(retorno[1]).items():
                if cid in atual["ligacoes"]:
                    atual["ligacoes"][cid] = [par[0], par[1]]
        lig = atual["ligacoes"]
        atual["conferencias"] += 1
        n = atual["conferencias"]

        confira = {}
        for c in dados["criterios"]:
            req_errado = lig[c["id"]][0] != c["de"]
            # Na lacuna, qualquer teste conta como "não achou", sem marca.
            teste_errado = (c["id"] != dados["lacuna"]) and lig[c["id"]][1] != c["teste"]
            if req_errado or teste_errado:
                confira[c["id"]] = [req_errado, teste_errado]
        ligacoes_ok = not confira
        lacuna_ok = lig[dados["lacuna"]][1] is None
        if lacuna_ok:
            atual["lacuna_vista"] = True

        q = store.rast_quadros[qid]
        q["conferencias"] = q.get("conferencias", 0) + 1
        if "primeira" not in q:
            q["primeira"] = {"ligacoes_ok": ligacoes_ok, "lacuna_ok": lacuna_ok}
            decisao(qid + "_ligacoes", ligacoes_ok)
            decisao(qid + "_lacuna", lacuna_ok)

        fechar = ligacoes_ok and (lacuna_ok or n >= 2)
        msgs = []
        if ligacoes_ok:
            msgs.append(__("Todas as ligações de requisito e de teste conferem."))
        elif len(confira) == 1:
            msgs.append(__("1 linha está marcada com (confira). Corrija e confira de novo."))
        else:
            msgs.append(__("{n} linhas estão marcadas com (confira). Corrija e confira de novo.").format(n=len(confira)))
        if not lacuna_ok and n == 1:
            msgs.append(__("Todo critério tem teste?"))
        if fechar:
            msgs.append(__("Quadro conferido."))
            q["ligacoes"] = {cid: list(par) for cid, par in lig.items()}
            q["lacuna_achada"] = bool(q.get("lacuna_achada") or atual["lacuna_vista"])
            q["concluido"] = True
        atual["confira"] = confira
        atual["msgs"] = msgs
        atual["fechado"] = fechar
        return fechar

    def rast_lacuna_achada(qid):
        """True se o jogador marcou "nenhum teste cobre" na lacuna antes de o quadro fechar."""
        return bool(store.rast_quadros.get(qid, {}).get("lacuna_achada"))

    def rast_valor_texto(valor, campo):
        if valor == "":
            return __("escolher")
        if valor is None:
            return __("nenhum teste cobre")
        return valor

    def rast_valores(qid, campo):
        dados = rast_dados(qid)
        if campo == 0:
            return [r["id"] for r in dados["requisitos"]]
        return [t["id"] for t in dados["testes"]] + [None]

    def rast_ciclar(qid, cid, campo, passo):
        # Setas esquerda/direita com o seletor em foco.
        valores = rast_valores(qid, campo)
        par = store.rast_atual["ligacoes"][cid]
        i = valores.index(par[campo]) if par[campo] in valores else (-1 if passo > 0 else 0)
        par[campo] = valores[(i + passo) % len(valores)]
        renpy.restart_interaction()

    def rast_ligacao_texto(cid, par):
        teste = __("sem teste") if par[1] is None else rast_valor_texto(par[1], 1)
        return "{c} → {r} → {t}".format(c=cid, r=rast_valor_texto(par[0], 0), t=teste)

    def rast_confira_texto(qid, cid):
        req_errado, teste_errado = store.rast_atual["confira"][cid]
        if req_errado and teste_errado:
            marca = __("(confira o requisito e o teste)")
        elif req_errado:
            marca = __("(confira o requisito)")
        else:
            marca = __("(confira o teste)")
        c = rast_criterio(qid, cid)
        explica = c.get("dica") or c.get("explica")
        if explica:
            explica = __(explica)
        else:
            explica = __("Releia de qual pedido este critério nasceu e qual teste confere exatamente o que ele descreve.")
        return marca + " " + explica

    def rast_cobertura(qid):
        """Linhas "R2: 2 critérios, 1 teste" a partir das ligações do jogador."""
        dados = rast_dados(qid)
        lig = store.rast_atual.get("ligacoes") or store.rast_quadros.get(qid, {}).get("ligacoes", {})
        linhas = []
        for r in dados["requisitos"]:
            crits = [cid for cid, par in lig.items() if par[0] == r["id"]]
            testes = set(lig[cid][1] for cid in crits if lig[cid][1])
            txt_c = __("1 critério") if len(crits) == 1 else __("{n} critérios").format(n=len(crits))
            if not testes:
                txt_t = __("nenhum teste")
            elif len(testes) == 1:
                txt_t = __("1 teste")
            else:
                txt_t = __("{n} testes").format(n=len(testes))
            linhas.append("{r}: {c}, {t}".format(r=r["id"], c=txt_c, t=txt_t))
        return linhas

    # Topo da lista de critérios na tela: painel em y 15 + margem 24 + título
    # (100 px; 140 com texto maior, em que a instrução ocupa duas linhas).
    RAST_TOPO = {False: 139, True: 179}

    def rast_rolar_foco(adj, topo, altura):
        """
        Com o teclado, traz o seletor em foco para dentro da área visível da
        lista de critérios (o Ren'Py não rola o viewport sozinho). Com o
        mouse, não mexe: rolar sob o cursor trocaria o foco de novo.
        """
        if renpy.display.focus.pending_focus_type != "keyboard":
            return
        x, y, w, h = renpy.focus_coordinates()
        if y is None:
            return
        # Folga de 1/3 da área: o próximo seletor precisa já estar visível,
        # porque o Ren'Py só passa o foco para o que está na tela.
        folga = altura // 3
        if y - folga < topo:
            adj.change(max(0, adj.value - (topo - (y - folga))))
        elif y + h + folga > topo + altura:
            adj.change(adj.value + (y + h + folga - topo - altura))

    def rast_texto_lembrar(qid):
        dados = rast_dados(qid)
        if dados.get("lembrar"):
            return __(dados["lembrar"])
        crit = rast_criterio(qid, dados["lacuna"])
        return __("No quadro de rastreabilidade, você marcou um critério sem teste: {criterio}").format(criterio=__(crit["texto"]))

    def rast_validar(qid):
        """Lista de problemas nos dados (vazia = ok). Usada pelos testes."""
        erros = []
        d = rast_dados(qid)
        reqs = set(r["id"] for r in d["requisitos"])
        testes = set(t["id"] for t in d["testes"])
        lacunas = [c["id"] for c in d["criterios"] if c["teste"] is None]
        if lacunas != [d["lacuna"]]:
            erros.append("%s: precisa de exatamente uma lacuna, a de 'lacuna'" % qid)
        for c in d["criterios"]:
            if c["de"] not in reqs:
                erros.append("%s/%s: requisito inexistente %s" % (qid, c["id"], c["de"]))
            if c["teste"] is not None and c["teste"] not in testes:
                erros.append("%s/%s: teste inexistente %s" % (qid, c["id"], c["teste"]))
        if not d.get("explica_lacuna"):
            erros.append("%s: sem explica_lacuna" % qid)
        return erros


label rast_atividade(qid):
    $ rast_iniciar(qid)

label .quadro:
    call screen rast_quadro(qid, "quadro")
    if not rast_conferir(qid, _return):
        jump .quadro
    call screen rast_quadro(qid, "fechado")
    return


# Numa cena posterior (semana de testes): lembra o critério sem teste, se o
# jogador achou a lacuna. Mesma lógica de pista_lembrar; o menu seguinte não muda.
label rast_lembrar(qid):
    if not rast_lacuna_achada(qid) or rast_quadros[qid].get("lembrado"):
        return
    menu (tipo="pista"):
        "Lembrar: o critério sem teste do quadro de rastreabilidade":
            $ rast_quadros[qid]["lembrado"] = True
            $ narrator(rast_texto_lembrar(qid))
        "Seguir sem lembrar":
            pass
    return


# -------------------------------
# Telas
# -------------------------------
style rast_confira_text is nb_texto:
    color "#ffd36b"

screen rast_quadro(qid, fase="quadro"):
    modal True
    zorder 130

    # Seletor em foco (cid, campo), para as setas esquerda/direita, e a
    # rolagem da lista de critérios (segue o foco do teclado).
    default foco = None
    default rolagem = ui.adjustment()

    $ maior = texto_maior_ativo()
    $ tam = 30 if maior else 24
    $ tam_ui = 30 if maior else 24
    $ dados = rast_dados(qid)
    $ lig = rast_atual["ligacoes"]
    $ confira = rast_atual.get("confira", {})
    $ aberto = (fase == "quadro")
    $ altura = 690 if maior else 750
    $ topo = RAST_TOPO[maior]

    if aberto and foco is not None:
        key "focus_left" action Function(rast_ciclar, qid, foco[0], foco[1], -1)
        key "focus_right" action Function(rast_ciclar, qid, foco[0], foco[1], 1)

    add Solid("#000000c8")

    # Posições fixas: o topo da lista de critérios fica sempre em RAST_TOPO[maior]
    # (coordenada de tela), que rast_rolar_foco usa.
    frame:
        style "nb_painel"
        xpos 30
        ypos 15
        xsize 1860
        ysize 1050
        padding (36, 24)

        fixed:
            vbox:
                spacing 8
                text _("Quadro de rastreabilidade") style "nb_titulo"
                if aberto:
                    text _("Ligue cada critério de aceitação ao requisito de onde veio e ao teste que o confere. Se nenhum teste confere o critério, escolha \"nenhum teste cobre\".") style "nb_dica" size (tam_ui - 2) xmaximum 1780
                else:
                    text _("Quadro conferido. Veja a cobertura e continue.") style "nb_dica" size (tam_ui - 2) xmaximum 1780

            hbox:
                ypos (topo - 39)
                spacing 24

                viewport:
                    style_prefix "nb"
                    id "rast_referencia"
                    xsize 580
                    ysize altura
                    mousewheel True
                    draggable True
                    scrollbars "vertical"
                    vscrollbar_unscrollable "hide"
                    # A barra não recebe foco do teclado: as setas ficam nos botões.
                    vscrollbar_keyboard_focus False
                    vbox:
                        spacing 10
                        xsize 550
                        text _("Requisitos") style "nb_secao" size tam_ui
                        for r in dados["requisitos"]:
                            frame:
                                style "nb_cartao"
                                padding (18, 12)
                                text ("{b}" + r["id"] + "{/b} · " + __(r["texto"])) style "nb_texto" size tam xmaximum 510
                        null height 6
                        text _("Testes") style "nb_secao" size tam_ui
                        for t in dados["testes"]:
                            frame:
                                style "nb_cartao"
                                padding (18, 12)
                                # Espaço de largura zero depois de "_": o nome longo quebra linha.
                                text ("{b}" + t["id"] + "{/b} · " + __(t["texto"]).replace("_", "_​")) style "nb_texto" size tam xmaximum 510

                viewport:
                    style_prefix "nb"
                    id "rast_criterios"
                    xsize 1190
                    ysize altura
                    yadjustment rolagem
                    mousewheel True
                    draggable True
                    pagekeys True
                    scrollbars "vertical"
                    vscrollbar_unscrollable "hide"
                    # A barra não recebe foco do teclado: as setas ficam nos botões.
                    vscrollbar_keyboard_focus False
                    vbox:
                        spacing 10
                        xsize 1160
                        if not aberto:
                            frame:
                                style "nb_cartao"
                                padding (18, 12)
                                vbox:
                                    spacing 4
                                    text _("Cobertura por requisito") style "nb_secao" size tam_ui
                                    text "\n".join(rast_cobertura(qid)) style "nb_texto" size tam id "rast_cobertura"
                        text _("Critérios de aceitação") style "nb_secao" size tam_ui
                        for c in dados["criterios"]:
                            $ cid = c["id"]
                            $ par = lig[cid]
                            # Seletores empilhados à direita do texto: as setas para cima
                            # e para baixo passam por todos (requisito, teste, próxima
                            # linha); esquerda e direita ficam livres para trocar o valor.
                            frame:
                                style "nb_cartao"
                                padding (18, 12)
                                vbox:
                                    spacing 8
                                    hbox:
                                        spacing 20
                                        fixed:
                                            xsize (600 if maior else 650)
                                            fit_first "height"
                                            text ("{b}" + cid + "{/b} · " + __(c["texto"])) style "nb_texto" size tam
                                        vbox:
                                            spacing 6
                                            xsize (504 if maior else 454)
                                            textbutton (__("Requisito: ") + rast_valor_texto(par[0], 0)):
                                                style "nb_botao"
                                                text_size tam_ui
                                                padding (20, 8)
                                                xfill True
                                                id ("rast_req_" + cid)
                                                sensitive aberto
                                                default_focus (aberto and cid == dados["criterios"][0]["id"])
                                                alt (__("Critério {c}, requisito: {v}. Enter escolhe; setas esquerda e direita trocam.").format(c=cid, v=rast_valor_texto(par[0], 0)))
                                                hovered [SetScreenVariable("foco", (cid, 0)), Function(rast_rolar_foco, rolagem, topo, altura)]
                                                unhovered SetScreenVariable("foco", None)
                                                action Show("rast_escolher", qid=qid, cid=cid, campo=0)
                                            textbutton (__("Teste: ") + rast_valor_texto(par[1], 1)):
                                                style "nb_botao"
                                                text_size tam_ui
                                                padding (20, 8)
                                                xfill True
                                                id ("rast_teste_" + cid)
                                                sensitive aberto
                                                alt (__("Critério {c}, teste: {v}. Enter escolhe; setas esquerda e direita trocam.").format(c=cid, v=rast_valor_texto(par[1], 1)))
                                                hovered [SetScreenVariable("foco", (cid, 1)), Function(rast_rolar_foco, rolagem, topo, altura)]
                                                unhovered SetScreenVariable("foco", None)
                                                action Show("rast_escolher", qid=qid, cid=cid, campo=1)
                                            text (__("Ligação: ") + rast_ligacao_texto(cid, par)) style "nb_dica" size (tam_ui - 2)
                                    if cid in confira:
                                        text rast_confira_texto(qid, cid) style "rast_confira_text" size tam xmaximum 1110

            vbox:
                ypos (topo - 39 + altura + 12)
                spacing 8
                for m in rast_atual.get("msgs", []):
                    text m style "nb_secao" size tam_ui xmaximum 1780
                hbox:
                    spacing 24
                    if aberto:
                        textbutton _("Conferir quadro"):
                            style "nb_botao"
                            text_size tam_ui
                            id "rast_conferir"
                            sensitive rast_completo()
                            action Return(("conferir", {k: list(v) for k, v in lig.items()}))
                        if rast_completo():
                            text _("Setas para cima e para baixo mudam o foco; Enter abre a escolha; esquerda e direita trocam o valor.") style "nb_dica" size (tam_ui - 4) yalign 0.5 xmaximum 1400
                        else:
                            text _("Escolha o requisito e o teste de todas as linhas para conferir. Setas para cima e para baixo mudam o foco; Enter abre a escolha; esquerda e direita trocam o valor.") style "nb_dica" size (tam_ui - 4) yalign 0.5 xmaximum 1400
                    else:
                        textbutton _("Continuar"):
                            style "nb_botao"
                            text_size tam_ui
                            id "rast_continuar"
                            default_focus True
                            action Return(True)

# Escolha do valor de um seletor (aberta por clique ou Enter).
screen rast_escolher(qid, cid, campo):
    modal True
    zorder 140

    $ maior = texto_maior_ativo()
    $ tam = 30 if maior else 24
    $ dados = rast_dados(qid)
    $ atual = rast_atual["ligacoes"][cid][campo]

    key "game_menu" action Hide("rast_escolher")

    add Solid("#00000080")

    frame:
        style "nb_painel"
        align (0.5, 0.5)
        xsize 1240
        padding (40, 28)

        vbox:
            spacing 10
            if campo == 0:
                text _("[cid]: de qual requisito este critério veio?") style "nb_secao" size tam
            else:
                text _("[cid]: qual teste confere este critério?") style "nb_secao" size tam
            text __(rast_criterio(qid, cid)["texto"]) style "nb_dica" size (tam - 2) xmaximum 1160
            null height 4
            if campo == 0:
                for r in dados["requisitos"]:
                    textbutton ("{b}" + r["id"] + "{/b} · " + __(r["texto"])):
                        style "nb_botao"
                        text_size tam
                        text_xmaximum 1100
                        xfill True
                        padding (20, 10)
                        id ("rast_opcao_" + r["id"])
                        selected (atual == r["id"])
                        default_focus (atual == r["id"] or (atual == "" and r is dados["requisitos"][0]))
                        action [SetDict(rast_atual["ligacoes"][cid], 0, r["id"]), Hide("rast_escolher")]
            else:
                for t in dados["testes"]:
                    textbutton ("{b}" + t["id"] + "{/b} · " + __(t["texto"]).replace("_", "_​")):
                        style "nb_botao"
                        text_size tam
                        text_xmaximum 1100
                        xfill True
                        padding (20, 10)
                        id ("rast_opcao_" + t["id"])
                        selected (atual == t["id"])
                        default_focus (atual == t["id"] or (atual == "" and t is dados["testes"][0]))
                        action [SetDict(rast_atual["ligacoes"][cid], 1, t["id"]), Hide("rast_escolher")]
                textbutton _("Nenhum teste cobre este critério"):
                    style "nb_botao"
                    text_size tam
                    xfill True
                    padding (20, 10)
                    id "rast_opcao_nenhum"
                    selected (atual is None)
                    default_focus (atual is None)
                    action [SetDict(rast_atual["ligacoes"][cid], 1, None), Hide("rast_escolher")]
            null height 4
            textbutton _("Voltar sem mudar (Esc)"):
                style "nb_botao"
                text_size (tam - 2)
                id "rast_opcao_voltar"
                action Hide("rast_escolher")
