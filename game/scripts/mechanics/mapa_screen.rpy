# mapa_screen.rpy
# -------------------------------
# TELAS DO TEMPO LIVRE: mapa da cidade, deslocamento, transição, abertura,
# fechamento, ponto de parada, HUD de energia e linha do epílogo
# -------------------------------
# Layout de docs/design/mapa-cidade.md §6 e §7. O mapa ocupa a tela inteira e
# é desenhado em camadas, todas vindas de dados (data/mapa_cidade.rpy):
#   1. base da cidade (images/mapa/cidade_base.png; sem a arte, um fundo
#      simples com o nome dos bairros);
#   2. um sprite por lugar (images/mapa/lugares/<id>.png; sem a arte, um
#      retângulo com o nome), que "salta" ao receber foco;
#   3. marcador "Você";
#   4. balões (compacto sem foco, expandido com foco);
#   5. painel do lugar escolhido, barra superior e rodapé.
# "Ver como lista" (e "Texto maior") troca o mapa por uma lista navegável.
#
# Retornos: im_mapa -> ("acao", poi, acao, alvo) ou "encerrar";
# im_abertura_cartao -> "mapa" ou "pular"; as outras -> True.

init python:

    IM_PAINEL_W = 600
    IM_BALAO_COMPACTO_W = 330
    IM_BALAO_EXPANDIDO_W = 470
    IM_BALAO_MAX = 6
    IM_TOPO = 80        # altura da barra superior
    IM_RODAPE = 930     # topo do rodapé (acima do menu rápido)

    def _im_escala():
        return float(config.screen_width) / MAPA_CIDADE["tamanho"][0]

    def _im_img(caminho):
        return caminho if caminho and renpy.loadable(caminho) else None

    def im_bg_disp(bg):
        return "bg " + bg if bg and renpy.has_image("bg " + bg) else Solid("#26313a")

    def im_icone(icone, lado=32):
        """Ícone de atividade (por id de MAPA_ATIVIDADES ou de arquivo)."""
        arquivo = MAPA_ATIVIDADES.get(icone, (None, icone))[1]
        img = _im_img(MAPA_CIDADE.get("pasta_icones", "") + "%s.png" % arquivo)
        return Transform(img, xysize=(lado, lado), fit="contain") if img else None

    def im_retrato(cid, lado):
        caminho = AMIGOS_DATA.get(cid, {}).get("portrait")
        if caminho and renpy.loadable(caminho):
            return Transform(caminho, xysize=(lado, lado), fit="cover")
        return Solid("#46525e", xysize=(lado, lado))

    def im_mapa_base():
        """Camada 1: a base ilustrada ou o fundo provisório com os bairros."""
        base = _im_img(MAPA_CIDADE.get("base"))
        if base:
            return Transform(base, xysize=(config.screen_width, config.screen_height))
        s = _im_escala()
        f = Fixed(xysize=(config.screen_width, config.screen_height))
        f.add(Solid("#2f3d35"))
        # Baía à direita e embaixo, para a cidade ter um contorno.
        f.add(Transform(Solid("#24465a"), xpos=config.screen_width - 90, xysize=(90, config.screen_height)))
        f.add(Transform(Solid("#24465a"), ypos=config.screen_height - 60, xysize=(config.screen_width, 60)))
        for b in MAPA_BAIRROS.values():
            f.add(Text(__(b["nome"]).upper(), size=20, color="#ffffff55", bold=True,
                       xpos=int(b["pos"][0] * s), ypos=int(b["pos"][1] * s), xanchor=0.5, yanchor=0.5))
        return f

    def im_voce_disp():
        img = _im_img(MAPA_CIDADE.get("voce"))
        if img:
            pino = Transform(img, xysize=(72, 72), fit="contain")
        else:
            pino = Fixed(Solid("#ff7a59", xysize=(40, 40), xalign=0.5), xysize=(72, 44))
        return VBox(pino, Text(__("Você"), size=18, bold=True, color="#ffffff",
                               outlines=[(2, "#101820", 0, 0)], xalign=0.5), xalign=0.5)

    def _im_caixa(lid):
        """Geometria do sprite do lugar na tela: x (centro), y (pé), w, h, img, zoom."""
        L = MAPA_LUGARES[lid]
        s = _im_escala()
        x, y = int(L["ancora"][0] * s), int(L["ancora"][1] * s)
        w = int(L["largura"] * s)
        img = _im_img(MAPA_CIDADE.get("pasta_lugares", "") + "%s.png" % lid)
        if img:
            iw, ih = renpy.image_size(img)
            z = float(w) / iw
            return {"x": x, "y": y, "w": w, "h": int(ih * z), "img": img, "zoom": z}
        return {"x": x, "y": y, "w": w, "h": int(w * 0.45), "img": None, "zoom": 1.0}

    def _im_pos_balao(cx, lado, n_linhas, expandido):
        """
        Posição, âncora do balão e posição relativa da ponta, a partir do lado
        preferido; vira para o lado oposto quando a estimativa passa da borda
        (mapa-cidade.md §2.1).
        """
        bw = IM_BALAO_EXPANDIDO_W if expandido else IM_BALAO_COMPACTO_W
        bh = (24 + 70 * n_linhas) if expandido else 76
        x, y, w, h = cx["x"], cx["y"], cx["w"], cx["h"]
        topo = y - h
        if lado == "acima" and topo - 12 - bh < IM_TOPO:
            lado = "abaixo"
        elif lado == "abaixo" and y + 34 + bh > IM_RODAPE:
            lado = "acima"
        elif lado == "direita" and x + w // 2 + 14 + bw > config.screen_width - 8:
            lado = "esquerda"
        elif lado == "esquerda" and x - w // 2 - 14 - bw < 8:
            lado = "direita"
        if lado == "acima":
            return (x, topo - 12), (0.5, 1.0), (0.5, 1.0)
        if lado == "abaixo":
            return (x, y + 34), (0.5, 0.0), (0.5, 0.0)
        if lado == "direita":
            return (x + w // 2 + 14, y - h // 2), (0.0, 0.5), (0.0, 0.5)
        return (x - w // 2 - 14, y - h // 2), (1.0, 0.5), (1.0, 0.5)

    def _im_pos_voce(lid):
        cx = _im_caixa(lid)
        lado = MAPA_LUGARES[lid].get("voce", "esquerda")
        if lado == "direita":
            return (cx["x"] + cx["w"] // 2 + 8, cx["y"]), (0.0, 1.0)
        if lado == "abaixo":
            return (cx["x"], cx["y"] + 30), (0.5, 0.0)
        return (cx["x"] - cx["w"] // 2 - 8, cx["y"]), (1.0, 1.0)

    def _im_trajeto_texto(t):
        if not t["de"] or not t["para"]:
            return ""
        if t["de"] == t["para"]:
            return __("Você está aqui")
        meio = __(MAPA_MEIOS.get(t["meio"], {}).get("nome", "")).lower()
        return __("Daqui: {n} min ({meio})").format(n=t["minutos"], meio=meio)

    def im_mapa_estado(semana, rota=None):
        """
        Tudo o que a tela do mapa mostra, calculado uma vez por interação:
        lugares (com geometria, estado, pessoas, salas e opções), a ordem de
        foco, os textos da barra e o alt de cada lugar.
        """
        rota = im_rota(rota)
        d = im_dados(semana, rota) or {}
        mapa = im_mapa_dados(rota)
        ops = im_opcoes(semana, todas=True, rota=rota)
        pois = im_pois(semana, rota)
        atividade = d.get("atividade", {})
        fechados_lugar = mapa.get("lugares_fechados", {})
        presentes = set(c for q in d.get("agenda", {}).values() for c in q)
        lugar_voce = im_lugar_do_poi(store.im_local, rota)
        mentor = (mentoria_dados(rota) or {}).get("mentor")
        mentoria_ok = mentoria_disponivel(semana, rota) is not None

        # Ordem de foco: lugares na ordem dos POIs, depois os fechados da
        # rota e a casa por último.
        ordem = []
        for p in pois:
            if p.get("lugar") in MAPA_LUGARES and p["lugar"] not in ordem:
                ordem.append(p["lugar"])
        for lid in fechados_lugar:
            if lid not in ordem:
                ordem.append(lid)
        if MAPA_CASA not in ordem:
            ordem.append(MAPA_CASA)

        lugares = {}
        for lid, L in MAPA_LUGARES.items():
            cx = _im_caixa(lid)
            salas = []
            pessoas = []
            for p in pois:
                if p.get("lugar") != lid:
                    continue
                quem = d.get("agenda", {}).get(p["id"], []) if p["estado"] == "aberto" else []
                gente = []
                for cid in quem:
                    icone, frase = atividade.get(cid, (p.get("icone", "programando"), None))
                    marcas = []
                    if cid == mentor and mentoria_ok:
                        marcas.append(__("★ mentoria"))
                    if cid in d.get("ajudar", {}):
                        marcas.append(__("aceita ajuda"))
                    pessoa = {
                        "cid": cid, "nome": im_nome(cid), "sub": __(p.get("sub") or p["nome"]),
                        "icone": icone, "atividade": __(MAPA_ATIVIDADES.get(icone, ("", ""))[0]),
                        "frase": __(frase) if frase else None, "marcas": marcas,
                        "desc": __(AMIGOS_DATA.get(cid, {}).get("desc", "")), "longe": False,
                    }
                    gente.append(pessoa)
                    pessoas.append(pessoa)
                salas.append({"id": p["id"], "nome": __(p["nome"]), "sub": __(p.get("sub") or ""),
                              "bg": im_poi_bg(p["id"], semana, rota), "estado": p["estado"],
                              "motivo": p["motivo"], "gente": gente,
                              "ops": [o for o in ops if o["poi"] == p["id"]]})
            # "Longe": balão acinzentado de quem já é contato e não está na agenda.
            for cid, (lugar_longe, icone, frase) in mapa.get("longe", {}).items():
                if lugar_longe == lid and cid not in presentes and getattr(store, "contato_" + cid, False):
                    pessoas.append({"cid": cid, "nome": im_nome(cid), "sub": __(L["nome"]), "icone": icone,
                                    "atividade": __(MAPA_ATIVIDADES.get(icone, ("", ""))[0]),
                                    "frase": __(frase), "marcas": [], "desc": "", "longe": True})
            casa = lid == MAPA_CASA
            if lid in fechados_lugar:
                estado_lugar = "fechado"
                estado = __(fechados_lugar[lid])
            elif casa:
                estado_lugar = "casa"
                estado = __("Ir para casa encerra o tempo livre")
            elif not salas:
                estado_lugar = "apagado"
                estado = ""
            elif not [s for s in salas if s["estado"] == "aberto"]:
                estado_lugar = "fechado"
                estado = salas[0]["motivo"]
            else:
                estado_lugar = "aberto"
                n = len([p for p in pessoas if not p["longe"]])
                if n == 1:
                    estado = __("1 pessoa")
                elif n:
                    estado = __("{n} pessoas").format(n=n)
                else:
                    acoes_lugar = sorted(set(__(IM_ACOES[o["acao"]]["nome"]) for s in salas for o in s["ops"]))
                    estado = __("Ninguém agora") + ((" · " + " · ".join(acoes_lugar)) if acoes_lugar else "")
            minhas = [o for s in salas for o in s["ops"]]
            ok = [o for o in minhas if o["ok"]]
            if any(o["acao"] == "mentoria" and o["ok"] for o in minhas):
                estado += " · " + __("★ Mentoria {k} de {n}").format(
                    k=mentoria_proximo(rota), n=len(mentoria_dados(rota)["passos"]))
            trajeto = ""
            if lid == lugar_voce:
                trajeto = __("Você está aqui")
            elif salas:
                trajeto = _im_trajeto_texto(im_trajeto(store.im_local, salas[0]["id"], rota))
            alt = __(L["nome"]) + ", " + __(MAPA_BAIRROS[L["bairro"]]["nome"]) + ". "
            if trajeto:
                alt += trajeto + ". "
            if pessoas:
                alt += __("Aqui: {quem}.").format(quem="; ".join(
                    "%s, %s%s" % (p["nome"], p["atividade"], (", " + p["frase"]) if p["frase"] else "") for p in pessoas)) + " "
            elif estado:
                alt += estado + ". "
            if ok:
                alt += __("Ações: {lista}.").format(lista="; ".join(
                    "%s, %s" % (o["rotulo"], __("{n} minutos").format(n=o["minutos"])) for o in ok))
            lugares[lid] = {
                "id": lid, "nome": __(L["nome"]), "bairro": __(MAPA_BAIRROS[L["bairro"]]["nome"]),
                "cx": cx, "balao": L.get("balao", "acima"),
                "estado_lugar": estado_lugar, "focavel": estado_lugar != "apagado",
                "estado": estado, "trajeto": trajeto, "pessoas": pessoas, "salas": salas,
                "n_ok": len(ok), "alt": alt, "voce": lid == lugar_voce, "casa": casa,
            }

        # Desenho: apagados primeiro (por y), depois os focáveis na ordem de foco.
        apagados = sorted([l for l in lugares.values() if not l["focavel"]], key=lambda l: l["cx"]["y"])
        focaveis = [lugares[lid] for lid in ordem if lid in lugares]
        noite = bool(d) and d["inicio"][0] >= 18
        barra = __("Mapa da cidade · Semana {s} · {dia} · {hora} · Tempo livre: faltam {m} min · {energia}").format(
            s=semana, dia=__(d.get("dia", "")), hora=im_hora_texto((store.game_hour, store.game_minute)),
            m=store.im_minutos, energia=energia_hud_texto())
        if lugar_voce:
            barra += " · " + __("Você está em: {lugar}").format(lugar=__(MAPA_LUGARES[lugar_voce]["nome"]))
        return {"lugares": lugares, "apagados": apagados, "focaveis": focaveis, "barra": barra,
                "noite": noite, "voce": lugar_voce}

    def im_foco_inicial(semana, rota=None):
        """Lugar do jogador; senão o primeiro lugar com ação."""
        lid = im_lugar_do_poi(store.im_local, rota)
        if lid:
            return lid
        for o in im_opcoes(semana, rota=rota):
            return im_lugar_do_poi(o["poi"], rota)
        return None

    def im_balao_linha(lg):
        """Texto do balão compacto."""
        gente = lg["pessoas"]
        if len(gente) == 1:
            p = gente[0]
            frase = p["frase"] or p["atividade"]
            # As frases da agenda costumam começar pelo nome ("Bia testando...").
            if frase.startswith(p["nome"] + " "):
                frase = frase[len(p["nome"]) + 1:]
            return "%s · %s" % (p["nome"], frase)
        if len(gente) == 2:
            return __("{a} e {b}").format(a=gente[0]["nome"], b=gente[1]["nome"])
        salas = len(set(p["sub"] for p in gente))
        if salas > 1:
            return __("{n} pessoas em {s} salas").format(n=len(gente), s=salas)
        return __("{n} pessoas").format(n=len(gente))

    def im_primeira_acao(lg):
        """Id da primeira ação disponível do lugar (foco inicial do painel)."""
        for s in lg["salas"]:
            for o in s["ops"]:
                if o["ok"]:
                    return o["valor"]
        return None

    def im_relogio_anim(st, at, ini, fim, dur):
        # Avança em passos de 5 min ao longo da tela de transição.
        t = min(1.0, st / dur) if dur else 1.0
        m = int(ini + (fim - ini) * t)
        if t < 1.0:
            m -= (m - ini) % 5
        texto = "%s → %s" % (im_hora_texto(_im_hm(ini)), im_hora_texto(_im_hm(m)))
        return Text(texto, size=40, bold=True, color="#ffffff"), (None if t >= 1.0 else 0.05)

    def im_transicao_fundo(desl):
        img = _im_img(desl.get("imagem"))
        if img:
            return Transform(img, xysize=(config.screen_width, config.screen_height), fit="cover")
        return im_bg_disp(desl.get("fundo"))

    def im_abertura_info(semana, rota=None):
        rota = im_rota(rota)
        d = im_dados(semana, rota)
        reg = im_registro_semana(semana, rota)
        return {
            "titulo": __("Tempo livre · Semana {n}").format(n=semana),
            "quando": __("{dia}, {ini} às {fim} · {m} min").format(
                dia=__(d["dia"]), ini=im_hora_texto((store.game_hour, store.game_minute)),
                fim=im_hora_texto(store.im_fim), m=store.im_minutos),
            "descontos": [__("−{n} min: {motivo}").format(n=m, motivo=__(motivo)) for motivo, m in reg["descontos"]],
            "energia": energia_hud_texto(),
        }

    config.overlay_screens.append("energia_hud")
    config.overlay_screens.append("im_resumo_epilogo")


# ---------------- estilos ----------------

style im_barra is frame:
    background Solid("#101820cc")
    padding (24, 14)

style im_barra_text is text:
    color "#ffffff"
    size 24

style im_lugar is button:
    background Solid("#3c4b57")
    hover_background Solid(gui.accent_color)
    selected_background Solid("#285a85")
    selected_hover_background Solid(gui.accent_color)
    padding (6, 4)

style im_lugar_text is text:
    color "#ffffff"
    hover_color "#101820"
    selected_hover_color "#101820"
    size 17
    text_align 0.5
    xalign 0.5

style im_nome_lugar is text:
    color "#ffffff"
    size 17
    bold True
    outlines [(2, "#101820", 0, 0)]
    text_align 0.5

style im_balao_borda is frame:
    background Solid("#2B2620")
    padding (3, 3)

style im_balao is frame:
    background Solid("#FBF6EC")
    padding (10, 8)

style im_balao_text is text:
    color "#2B2620"
    size 16

style im_acao is nb_botao:
    padding (16, 10)
    xfill True

style im_acao_text is nb_botao_text:
    size 21

style im_acao_detalhe is text:
    size 17
    color "#d7dde3"
    hover_color "#101820"
    selected_hover_color "#101820"
    insensitive_color "#7d8894"


# ---------------- mapa ----------------

transform im_salta:
    on idle:
        ease 0.15 yoffset 0 zoom 1.0
    on hover, selected_hover:
        ease 0.15 yoffset -12 zoom 1.06
    on selected_idle:
        ease 0.15 yoffset -6 zoom 1.03

transform im_brilho:
    matrixcolor BrightnessMatrix(0.0)
    ease 1.2 matrixcolor BrightnessMatrix(0.08)
    ease 1.2 matrixcolor BrightnessMatrix(0.0)
    repeat

transform im_fechado:
    matrixcolor SaturationMatrix(0.15) * BrightnessMatrix(-0.15)

transform im_apagado:
    matrixcolor SaturationMatrix(0.0) * BrightnessMatrix(-0.2)
    alpha 0.6

transform im_noite:
    matrixcolor TintMatrix("#aab8ff") * BrightnessMatrix(-0.12)

transform im_voce_bob:
    yoffset 0
    ease 0.8 yoffset -4
    ease 0.8 yoffset 0
    repeat

transform im_anda(x0, y0, x1, y1, t=1.0):
    xpos x0 ypos y0
    ease t xpos x1 ypos y1

transform im_zoom_lento(t=2.0):
    zoom 1.0
    linear t zoom 1.03

screen im_mapa(semana):
    modal True
    zorder 50
    default foco = im_foco_inicial(semana)
    default aberto = None
    default lista = bool(persistent.im_mapa_lista) or texto_maior_ativo()
    $ est = im_mapa_estado(semana)

    if lista:
        add Solid("#0d1418")
        use im_mapa_lista(est)
    else:
        use im_mapa_camadas(est, foco, aberto)
        if aberto is not None and aberto in est["lugares"]:
            # Mapa escurecido atrás do painel; clique fora fecha.
            button:
                xysize (config.screen_width, config.screen_height)
                background Solid("#0000004d")
                hover_background Solid("#0000004d")
                action SetScreenVariable("aberto", None)
                alt _("Voltar ao mapa")
            use im_mapa_painel(est, est["lugares"][aberto])
            key "K_BACKSPACE" action SetScreenVariable("aberto", None)

    frame:
        style "im_barra"
        xfill True
        ypos 0
        text est["barra"] style "im_barra_text" id "im_mapa_barra"

    hbox:
        xpos 24 ypos IM_RODAPE + 10
        spacing 20
        textbutton _("Encerrar o tempo livre"):
            style "nb_botao"
            id "im_encerrar"
            action Return("encerrar")
        textbutton (_("Ver como mapa") if lista else _("Ver como lista")):
            style "nb_botao"
            id "im_lista"
            action [ToggleScreenVariable("lista"), SetField(persistent, "im_mapa_lista", not lista), SetScreenVariable("aberto", None)]
        frame:
            background Solid("#101820cc")
            padding (12, 8)
            yalign 0.5
            text _("Tab ou setas escolhem; Enter abre o lugar; Backspace volta ao mapa.") style "nb_dica"


screen im_mapa_camadas(est, foco, aberto=None, desl=None, interativo=True):
    # Camadas do mapa. interativo=False: só desenho (tela de deslocamento).
    fixed:
        xysize (config.screen_width, config.screen_height)
        if est["noite"]:
            at im_noite

        add im_mapa_base()

        # Sprites: apagados (de outras rotas) e depois os da rota.
        for lg in est["apagados"]:
            $ cx = lg["cx"]
            fixed:
                pos (cx["x"], cx["y"]) anchor (0.5, 1.0)
                xysize (cx["w"], cx["h"])
                at im_apagado
                if cx["img"]:
                    add Transform(cx["img"], zoom=cx["zoom"])
                else:
                    add Solid("#3c4b57")

        for lg in est["focaveis"]:
            $ cx = lg["cx"]
            if interativo and aberto is None:
                button:
                    style "im_lugar"
                    pos (cx["x"], cx["y"]) anchor (0.5, 1.0)
                    xysize (cx["w"], cx["h"])
                    selected foco == lg["id"]
                    action [SetScreenVariable("foco", lg["id"]), SetScreenVariable("aberto", lg["id"])]
                    hovered SetScreenVariable("foco", lg["id"])
                    alt lg["alt"]
                    default_focus (foco == lg["id"])
                    if cx["img"]:
                        background None
                        hover_background None
                        selected_background None
                        selected_hover_background None
                    at im_salta
                    use im_lugar_desenho(lg)
            else:
                fixed:
                    pos (cx["x"], cx["y"]) anchor (0.5, 1.0)
                    xysize (cx["w"], cx["h"])
                    if not cx["img"]:
                        add Solid("#3c4b57")
                    use im_lugar_desenho(lg)
            # Nome embaixo do lote (só com a arte; o retângulo já tem o nome).
            if cx["img"]:
                text lg["nome"] style "im_nome_lugar" pos (cx["x"], cx["y"] + 4) xanchor 0.5

        # Marcador "Você".
        if desl is not None and desl.get("marcador") and desl["de"] in est["lugares"] and desl["para"] in est["lugares"]:
            $ ini_voce, anc0 = _im_pos_voce(desl["de"])
            $ fim_voce, anc1 = _im_pos_voce(desl["para"])
            add im_voce_disp() anchor anc1 at im_anda(ini_voce[0], ini_voce[1], fim_voce[0], fim_voce[1], MAPA_TEMPO_MARCADOR)
        elif est["voce"]:
            $ pos_voce, anc = _im_pos_voce(est["voce"])
            if im_transicoes_ligadas():
                add im_voce_disp() pos pos_voce anchor anc at im_voce_bob
            else:
                add im_voce_disp() pos pos_voce anchor anc

        # Balões por cima de tudo; o do lugar em foco (expandido) por último.
        if aberto is None:
            for lg in est["focaveis"]:
                if lg["pessoas"] and not (interativo and foco == lg["id"]):
                    use im_balao(lg, False)
            if interativo and foco in est["lugares"] and est["lugares"][foco]["pessoas"]:
                use im_balao(est["lugares"][foco], True)


screen im_lugar_desenho(lg):
    # Conteúdo do sprite: a arte (com brilho se há gente, cinza se fechado) ou
    # o retângulo com nome e estado escritos.
    $ cx = lg["cx"]
    if cx["img"]:
        if lg["estado_lugar"] == "fechado":
            add Transform(cx["img"], zoom=cx["zoom"]) at im_fechado
        elif lg["pessoas"] and im_transicoes_ligadas():
            add Transform(cx["img"], zoom=cx["zoom"]) at im_brilho
        else:
            add Transform(cx["img"], zoom=cx["zoom"])
    else:
        vbox:
            align (0.5, 0.5)
            spacing 2
            text lg["nome"] style "im_lugar_text" bold True xmaximum cx["w"] - 12
            if lg["estado"]:
                text lg["estado"] style "im_lugar_text" size 14 xmaximum cx["w"] - 12
            if lg["voce"]:
                text _("Você está aqui") style "im_lugar_text" size 14


screen im_balao(lg, expandido):
    # Um balão por lugar, desenhado pela tela (moldura creme, contorno escuro,
    # ponta para o lugar). Compacto: retratos empilhados, ícone e uma linha.
    # Expandido (foco): uma linha por pessoa com sala, atividade e frase.
    $ n = min(len(lg["pessoas"]), IM_BALAO_MAX)
    $ pos_b, anc_b, anc_ponta = _im_pos_balao(lg["cx"], lg["balao"], n, expandido)
    $ longe = all(p["longe"] for p in lg["pessoas"])
    fixed:
        pos pos_b anchor anc_b
        fit_first True
        frame:
            style "im_balao_borda"
            frame:
                style "im_balao"
                background Solid("#d9d6cf" if longe else "#FBF6EC")
                if expandido:
                    vbox:
                        xsize IM_BALAO_EXPANDIDO_W - 26
                        spacing 6
                        for p in lg["pessoas"][:IM_BALAO_MAX]:
                            hbox:
                                spacing 8
                                add im_retrato(p["cid"], 56)
                                if im_icone(p["icone"]):
                                    add im_icone(p["icone"], 32) yalign 0.5
                                vbox:
                                    xsize IM_BALAO_EXPANDIDO_W - 140
                                    text (" · ".join([p["nome"], p["sub"], p["atividade"]] + p["marcas"])) style "im_balao_text" bold True
                                    if p["frase"]:
                                        text p["frase"] style "im_balao_text" size 14
                        if len(lg["pessoas"]) > IM_BALAO_MAX:
                            text _("+{n} pessoas").format(n=len(lg["pessoas"]) - IM_BALAO_MAX) style "im_balao_text" size 14
                else:
                    hbox:
                        spacing 8
                        fixed:
                            xysize (48 + 32 * (min(len(lg["pessoas"]), 4) - 1), 48)
                            for i, p in enumerate(lg["pessoas"][:4]):
                                add im_retrato(p["cid"], 48) xpos 32 * i
                        if len(lg["pessoas"]) > 4:
                            text "+%d" % (len(lg["pessoas"]) - 4) style "im_balao_text" yalign 0.5
                        if im_icone(lg["pessoas"][0]["icone"]):
                            add im_icone(lg["pessoas"][0]["icone"], 32) yalign 0.5
                        text im_balao_linha(lg) style "im_balao_text" yalign 0.5 xmaximum IM_BALAO_COMPACTO_W - 140
        add Transform(Solid("#2B2620", xysize=(16, 16)), rotate=45):
            xpos anc_ponta[0] ypos anc_ponta[1]
            xanchor 0.5 yanchor 0.5


screen im_painel_conteudo(lg, focar=True):
    # Salas, pessoas e ações de um lugar (painel e modo lista).
    $ alvo_foco = im_primeira_acao(lg) if focar else None
    vbox:
        spacing 10
        if lg["casa"]:
            textbutton _("Ir para casa (encerrar o tempo livre)"):
                style "im_acao"
                default_focus focar
                action Return("encerrar")
            if im_minutos >= IM_CEDO_MINUTOS:
                text _("Sobram {n} min: indo agora, você ganha +1 de energia.").format(n=im_minutos) style "nb_dica"
        elif lg["estado_lugar"] == "fechado" and not lg["salas"]:
            text lg["estado"] style "nb_dica"
        for p in lg["pessoas"]:
            if p["longe"]:
                text (p["nome"] + " · " + p["frase"]) style "nb_dica"
        for sala in lg["salas"]:
            hbox:
                spacing 12
                if sala["bg"]:
                    add Transform(im_bg_disp(sala["bg"]), xysize=(128, 72))
                vbox:
                    text sala["nome"] style "nb_secao" size 22
                    if sala["sub"]:
                        text sala["sub"] style "nb_dica" size 17
            if sala["estado"] != "aberto":
                text sala["motivo"] style "nb_dica"
            else:
                if not sala["gente"]:
                    text _("Ninguém agora.") style "nb_dica" size 18
                for p in sala["gente"]:
                    hbox:
                        spacing 12
                        add im_retrato(p["cid"], 72)
                        vbox:
                            xsize 440
                            text (" · ".join([p["nome"]] + p["marcas"])) style "nb_texto" size 21 bold True
                            text (p["frase"] or p["atividade"]) style "nb_texto" size 17
                            if p["desc"]:
                                text p["desc"] style "nb_dica" size 15
                for o in sala["ops"]:
                    button:
                        style "im_acao"
                        sensitive o["ok"]
                        action Return(o["valor"])
                        default_focus (alvo_foco is not None and o["valor"] == alvo_foco)
                        alt "%s. %s.%s" % (o["rotulo"], o["detalhe"], (" " + o["motivo"]) if o["motivo"] else "")
                        hbox:
                            spacing 10
                            if im_icone(MAPA_ICONE_ACAO.get(o["acao"], "")):
                                add im_icone(MAPA_ICONE_ACAO[o["acao"]], 32) yalign 0.5
                            vbox:
                                text o["rotulo"] style "im_acao_text"
                                text o["detalhe"] style "im_acao_detalhe"
                                if o["motivo"]:
                                    text o["motivo"] style "im_acao_detalhe" color "#ffcf8a"
                                else:
                                    if o["aviso"]:
                                        text o["aviso"] style "im_acao_detalhe" color "#ffcf8a"
                                    text _("Depois disso sobram {n} min.").format(n=im_minutos - o["minutos"]) style "im_acao_detalhe"


screen im_mapa_painel(est, lg):
    # Painel do lugar escolhido, do lado oposto ao lugar.
    $ esquerda = MAPA_LUGARES[lg["id"]]["ancora"][0] > MAPA_CIDADE["tamanho"][0] // 2
    frame:
        style "nb_painel"
        xpos (24 if esquerda else config.screen_width - IM_PAINEL_W - 24) ypos IM_TOPO + 10
        xysize (IM_PAINEL_W, IM_RODAPE - IM_TOPO - 20)
        padding (24, 20)
        vbox:
            spacing 8
            text lg["nome"] style "nb_titulo" size 30
            text (lg["bairro"] + ((" · " + lg["trajeto"]) if lg["trajeto"] else "")) style "nb_dica"
            viewport:
                id "im_painel_vp"
                mousewheel True
                scrollbars "vertical"
                style_prefix "nb"
                ysize IM_RODAPE - IM_TOPO - 230
                vbox:
                    xsize IM_PAINEL_W - 70
                    use im_painel_conteudo(lg)
            text _("Sobram {n} min de tempo livre.").format(n=im_minutos) style "nb_dica"
            textbutton _("Voltar ao mapa"):
                style "nb_botao"
                id "im_voltar_mapa"
                action SetScreenVariable("aberto", None)


screen im_mapa_lista(est):
    # Modo lista (acessível): um bloco por lugar aceso, na ordem do teclado,
    # com pessoas e ações.
    frame:
        xpos 24 ypos IM_TOPO + 10
        xysize (config.screen_width - 48, IM_RODAPE - IM_TOPO - 20)
        background Solid("#101820")
        padding (24, 20)
        viewport:
            id "im_lista_vp"
            mousewheel True
            scrollbars "vertical"
            style_prefix "nb"
            vbox:
                spacing 24
                xsize config.screen_width - 140
                for i, lg in enumerate(est["focaveis"]):
                    frame:
                        style "nb_cartao"
                        vbox:
                            spacing 6
                            text lg["nome"] style "nb_titulo" size 28
                            text (" · ".join([x for x in (lg["bairro"], lg["trajeto"], lg["estado"]) if x])) style "nb_dica"
                            use im_painel_conteudo(lg, i == 0)


# ---------------- deslocamento ----------------

screen im_deslocamento(semana, desl):
    # O marcador "Você" anda no mapa (~1 s). Clique, Enter ou Espaço pulam.
    modal True
    zorder 50
    $ est = im_mapa_estado(semana)
    use im_mapa_camadas(est, None, None, desl, False)
    frame:
        style "im_barra"
        xfill True
        text desl["texto"] style "im_barra_text"
    button:
        xysize (config.screen_width, config.screen_height)
        background None
        alt desl["texto"]
        action Return(True)
    key "dismiss" action Return(True)
    timer MAPA_TEMPO_MARCADOR action Return(True)


screen im_transicao(desl, cartao=False):
    # Tela do trajeto (ônibus, metrô, calçada, elevador...) com o relógio
    # correndo; cartao=True (transições desligadas): só o texto. Clique,
    # Enter ou Espaço pulam.
    modal True
    zorder 60
    if cartao:
        add Solid("#101820")
        frame:
            style "nb_painel"
            align (0.5, 0.5)
            xmaximum 1400
            text desl["texto_curto"] style "nb_texto" text_align 0.5
        timer MAPA_TEMPO_CARTAO action Return(True)
    else:
        add im_transicao_fundo(desl) at im_zoom_lento(desl["duracao"])
        frame:
            yalign 1.0
            xfill True
            background Solid("#101820d8")
            padding (40, 24)
            hbox:
                spacing 40
                vbox:
                    text desl["meio_nome"] style "nb_titulo" size 36
                    text desl["texto"] style "nb_texto"
                add DynamicDisplayable(im_relogio_anim, desl["hora_ini"], desl["hora_fim"], desl["duracao"]) yalign 0.5
                text _("Clique para pular.") style "nb_dica" yalign 0.5
        timer desl["duracao"] action Return(True)
    button:
        xysize (config.screen_width, config.screen_height)
        background None
        alt desl["texto"]
        action Return(True)
    key "dismiss" action Return(True)


# ---------------- abertura, fechamento e parada ----------------

screen im_abertura_cartao(semana):
    modal True
    zorder 50
    $ info = im_abertura_info(semana)
    add Solid("#000000c8")
    frame:
        style "nb_painel"
        align (0.5, 0.5)
        xsize 1100
        vbox:
            spacing 16
            text info["titulo"] style "nb_titulo"
            text info["quando"] style "nb_texto"
            for linha in info["descontos"]:
                text linha style "nb_texto" color "#ffcf8a"
            text info["energia"] style "nb_texto"
            text _("Escolha onde passar este tempo. Não cabe tudo. Nada aqui é obrigatório para aprender: o que o projeto pede acontece nas cenas.") style "nb_dica" xmaximum 1000
            hbox:
                spacing 20
                textbutton _("Abrir o mapa"):
                    style "nb_botao"
                    id "im_abrir_mapa"
                    default_focus True
                    action Return("mapa")
                textbutton _("Pular o tempo livre"):
                    style "nb_botao"
                    id "im_pular"
                    action Return("pular")


screen im_resumo(semana):
    modal True
    zorder 50
    $ r = im_resumo_dados(semana)
    add Solid("#000000c8")
    frame:
        style "nb_painel"
        align (0.5, 0.5)
        xsize 1300
        vbox:
            spacing 12
            text _("Fim do tempo livre · Semana [semana]") style "nb_titulo"
            viewport:
                mousewheel True
                scrollbars "vertical"
                style_prefix "nb"
                ymaximum 640
                vbox:
                    spacing 8
                    xsize 1180
                    text _("O que você fez") style "nb_secao"
                    if r["acoes"]:
                        for a in r["acoes"]:
                            text "· " + a style "nb_texto" size 24
                    else:
                        text _("Nada desta vez.") style "nb_texto" size 24
                    if r["amizade"]:
                        text _("Amizade") style "nb_secao"
                        for nome, v in r["amizade"]:
                            text "· %s +%s" % (nome, ("%.1f" % v).replace(".", ",")) style "nb_texto" size 24
                    if r["pistas"]:
                        text _("Pistas novas") style "nb_secao"
                        for t in r["pistas"]:
                            text "· " + t style "nb_texto" size 24
                    if r["extra"]:
                        text _("Registro extra no notebook") style "nb_secao"
                        text "· " + r["extra"] style "nb_texto" size 24
                    text _("Energia: {a} → {b} ({estado})").format(a=r["energia_inicio"], b=r["energia"], estado=energia_estado()) style "nb_texto" size 24
                    if r["trajetos"]:
                        text _("No caminho: {m} min ({n} trajetos)").format(m=r["trajeto_min"], n=r["trajetos"]) style "nb_texto" size 24
                    if r["encerrou_cedo"]:
                        text _("Você foi para casa mais cedo.") style "nb_texto" size 24
                    if r["fora"]:
                        text _("Ficou para outra vez: {lista}.").format(lista=", ".join(r["fora"])) style "nb_dica" xmaximum 1160
                    text _("Escolher é deixar algo de fora: é a mesma conta da capacidade no planejamento.") style "nb_dica" xmaximum 1160
            textbutton _("Continuar"):
                style "nb_botao"
                id "im_resumo_continuar"
                xalign 1.0
                default_focus True
                action Return(True)


screen im_parada(semana, novos):
    # Ponto de parada de aula (fim da semana).
    modal True
    zorder 50
    $ n_reg, total_reg = registros_contagem()
    $ adequadas, com_apoio = resumo_decisoes()
    $ tl = tempo_livre_resumo()
    add Solid("#000000d8")
    frame:
        style "nb_painel"
        align (0.5, 0.5)
        xsize 1300
        vbox:
            spacing 12
            text _("Fim da semana [semana]") style "nb_titulo"
            if novos:
                text _("Registros desta semana") style "nb_secao"
                for t in novos:
                    text "· " + t style "nb_texto" size 24
            text _("Notebook: [n_reg] de [total_reg] registros · Extras: {a} de {b}").format(a=tl["extras"][0], b=tl["extras"][1]) style "nb_texto" size 24
            text _("Decisões adequadas na primeira tentativa: [adequadas] · com revisão orientada: [com_apoio]") style "nb_texto" size 24
            text _("Pistas: {a} · {energia}").format(a=tl["pistas"], energia=energia_hud_texto()) style "nb_texto" size 24
            text _("Bom ponto para parar: o jogo já guardou um salvamento automático.") style "nb_dica"
            hbox:
                spacing 20
                textbutton _("Continuar"):
                    style "nb_botao"
                    id "im_parada_continuar"
                    default_focus True
                    action Return(True)
                textbutton _("Salvar"):
                    style "nb_botao"
                    id "im_parada_salvar"
                    action ShowMenu("save")
                textbutton _("Voltar ao menu"):
                    style "nb_botao"
                    id "im_parada_menu"
                    action MainMenu(confirm=True)


# ---------------- HUD e epílogo ----------------

screen energia_hud():
    # Abaixo do relógio do canto (top_right_clock). Número e texto, e dez
    # quadradinhos cheios ou vazados (a diferença não depende de cor).
    zorder 5
    if energia_mostrar and not main_menu and not _menu and not renpy.get_screen("im_mapa") and not renpy.get_screen("im_deslocamento") and not renpy.get_screen("im_transicao"):
        frame:
            background Solid("#00000080")
            xalign 1.0 ypos 116
            xoffset -16
            padding (12, 8)
            vbox:
                spacing 6
                text energia_hud_texto() size 20 color "#ffffff" xalign 1.0
                hbox:
                    spacing 4
                    xalign 1.0
                    for i in range(ENERGIA_MAX):
                        if i < energia_semana:
                            add Solid("#ffffff", xysize=(14, 14))
                        else:
                            fixed:
                                xysize (14, 14)
                                add Solid("#ffffff")
                                add Solid("#333b44", xysize=(10, 10)) pos (2, 2)


screen im_resumo_tempo_livre():
    # Linha do tempo livre para o resumo do epílogo. Pode ser usada dentro de
    # resumo_rota (use im_resumo_tempo_livre); até lá, im_resumo_epilogo a
    # mostra por cima, no canto livre do painel.
    $ tl = tempo_livre_resumo()
    vbox:
        spacing 2
        text _("Tempo livre: mentoria {a} de {b} · pistas {p} (usadas {u}) · extras {e} de {t}").format(
            a=tl["mentoria"][0], b=tl["mentoria"][1], p=tl["pistas"], u=tl["pistas_usadas"],
            e=tl["extras"][0], t=tl["extras"][1]) style "nb_dica" size 20
        if tl["conquistas"]:
            text _("Do tempo livre: {lista}").format(lista=", ".join(tl["conquistas"])) style "nb_dica" size 20 color gui.accent_color


screen im_resumo_epilogo():
    zorder 111
    if renpy.get_screen("resumo_rota") and im_houve_tempo_livre():
        fixed:
            pos (260, 930)
            xsize 1050
            fit_first True
            use im_resumo_tempo_livre
