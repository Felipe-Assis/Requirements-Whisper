# learning_activities.rpy
# -------------------------------
# ATIVIDADES: escrita livre com autoavaliação e planejamento com capacidade
# -------------------------------
# Uso nas cenas:
#   call exercicio_escrita("st_escrita_exclusao", _("A estudante precisa ..."))
#   call atividade_planejamento("st_plan_v1", itens, [0, 1], capacidade=2)
#   $ cobertura = _return
# Estado (escritas, planejamentos) e escapar_texto em logic/learning.rpy.
# Estilos nb_* em notebook_screen.rpy.

# Rascunho em edição e respostas da autoavaliação (só durante a atividade).
default escrita_atual = {}
default escrita_marcas = [False, False, False, False]

# Itens escolhidos (índices), última escolha do menu e resultado da conferência.
default planejamento_sel = []
default planejamento_escolha = None
default planejamento_resultado = {}

init python:

    ESCRITA_PERGUNTAS = [
        _("Fica claro quem age?"),
        _("As condições que limitam a ação estão escritas?"),
        _("O critério tem um resultado que dá para observar?"),
        _("Há uma exceção ou um caso que deve ser recusado?"),
    ]

    def escrita_guardar(eid, status):
        # Grava o rascunho atual em escritas[eid]. "confirmado" só vale com
        # os dois campos preenchidos e os quatro pontos conferidos.
        req = store.escrita_atual.get("req", "")
        crit = store.escrita_atual.get("crit", "")
        checks = sum(1 for m in store.escrita_marcas if m)
        if status == "confirmado" and not (req and crit and checks == 4):
            status = "pendente"
        store.escritas[eid] = {"req": req, "crit": crit, "checks": checks, "status": status}
        return status

    def planejamento_indices(itens, necessarios):
        # Aceita índices ou os próprios textos dos itens.
        return [n if isinstance(n, int) else itens.index(n) for n in necessarios]

    def planejamento_legenda(itens, capacidade):
        limite = min(capacidade, len(itens))
        return __("Plano da entrega: {usados} de {limite} vagas usadas. Cada item ocupa uma vaga.").format(
            usados=len(store.planejamento_sel), limite=limite)

    def planejamento_opcoes(itens, capacidade):
        sel = store.planejamento_sel
        limite = min(capacidade, len(itens))
        opcoes = []
        if len(sel) < limite:
            for i, item in enumerate(itens):
                if i not in sel:
                    opcoes.append((__("Adicionar: {item}").format(item=__(item)), ("add", i)))
        for i in sel:
            opcoes.append((__("Retirar: {item}").format(item=__(itens[i])), ("del", i)))
        if len(sel) == limite:
            opcoes.append((__("Conferir este plano"), ("conferir", None)))
        return opcoes

    def planejamento_aplicar(escolha):
        acao, i = escolha
        if acao == "add" and i not in store.planejamento_sel:
            store.planejamento_sel.append(i)
        elif acao == "del" and i in store.planejamento_sel:
            store.planejamento_sel.remove(i)

    def planejamento_conferir(pid, itens, necessarios):
        # Calcula a cobertura do plano atual, grava em planejamentos[pid] e
        # devolve {"cobertura", "total", "faltando": textos que ficaram de fora}.
        idx = planejamento_indices(itens, necessarios)
        sel = list(store.planejamento_sel)
        cobertura = sum(1 for n in idx if n in sel)
        faltando = [__(itens[n]) for n in idx if n not in sel]
        anterior = store.planejamentos.get(pid)
        store.planejamentos[pid] = {
            "selecionados": sel,
            "cobertura": cobertura,
            "total": len(idx),
            "primeira_cobertura": anterior["primeira_cobertura"] if anterior else cobertura,
        }
        return {"cobertura": cobertura, "total": len(idx), "faltando": ", ".join(faltando)}


# -------------------------------
# Escrita livre de requisito + critério, com revisão e autoavaliação
# -------------------------------
label exercicio_escrita(eid, pedido):
    # Escrita livre de um requisito e de um critério de aceitação. Guarda em
    # escritas[eid] = {"req", "crit", "checks", "status"}; chamado de novo
    # com o mesmo eid, retoma o rascunho. O jogo não avalia o significado do
    # texto: quem escreve confere os quatro pontos.
    $ escrita_atual = dict(escritas.get(eid, {"req": "", "crit": ""}))
    $ escrita_marcas = [False, False, False, False]
    if escrita_atual["req"] or escrita_atual["crit"]:
        "Você retoma o rascunho guardado no notebook. Cada campo começa com o texto anterior: edite ou confirme com Enter."
    else:
        "Escreva com suas palavras. Pode ser breve. Depois você mesmo vai revisar o rascunho."

label .redigir:
    $ escrita_atual["req"] = escapar_texto(renpy.input(_("Requisito: quem pode fazer o quê, e sob quais condições?"), default=desescapar_texto(escrita_atual["req"]), length=400, exclude="", screen="escrita_input", show_pedido=pedido, show_etapa=1))
    $ escrita_atual["crit"] = escapar_texto(renpy.input(_("Critério de aceitação: situação inicial, ação e resultado que dá para conferir."), default=desescapar_texto(escrita_atual["crit"]), length=400, exclude="", screen="escrita_input", show_pedido=pedido, show_etapa=2))

    call screen escrita_revisao(pedido)
    if _return == "reescrever":
        jump .redigir

    $ escrita_atual["status"] = escrita_guardar(eid, _return)
    if escrita_atual["status"] == "confirmado":
        "Rascunho guardado como confirmado por você. O jogo não avalia o significado do texto: o próximo passo seria revisar com a equipe e com quem fez o pedido."
    else:
        "Rascunho guardado como pendente. Faltou preencher um campo ou conferir algum dos quatro pontos."
    return


# -------------------------------
# Planejamento com capacidade (ex.: 2 de 4 itens)
# -------------------------------
label atividade_planejamento(pid, itens, necessarios, capacidade=2):
    # Menu em loop: adicionar/retirar itens até a capacidade e conferir.
    # Devolve a cobertura (0..len(necessarios)) em _return e grava em
    # planejamentos[pid]. necessarios = índices (ou textos) de itens.
    $ planejamento_sel = []

label .escolher:
    python:
        narrator(planejamento_legenda(itens, capacidade), interact=False)
        planejamento_escolha = renpy.display_menu(planejamento_opcoes(itens, capacidade))
    if planejamento_escolha[0] != "conferir":
        $ planejamento_aplicar(planejamento_escolha)
        jump .escolher

    $ planejamento_resultado = planejamento_conferir(pid, itens, necessarios)
    if planejamento_resultado["cobertura"] == planejamento_resultado["total"]:
        "Cobertura: [planejamento_resultado['cobertura']] de [planejamento_resultado['total']]. O plano inclui tudo o que a necessidade confirmada pede para esta entrega."
    elif planejamento_resultado["cobertura"] > 0:
        "Cobertura: [planejamento_resultado['cobertura']] de [planejamento_resultado['total']]. Uma parte necessária perdeu a vaga para um extra. Fora do plano: [planejamento_resultado['faltando']]."
    else:
        "Cobertura: 0 de [planejamento_resultado['total']]. As vagas foram para extras e nenhuma parte necessária entrou. Fora do plano: [planejamento_resultado['faltando']]."
    "Extras podem ter valor em outra rodada. Num projeto real, a equipe ainda conferiria tamanho, dependências e riscos antes de assumir o plano."

    menu:
        "O que você quer fazer com este plano?"
        "Revisar os itens escolhidos":
            jump .escolher
        "Concluir com este plano":
            pass
    return planejamento_resultado["cobertura"]


# -------------------------------
# Telas da escrita
# -------------------------------
screen escrita_input(prompt, pedido="", etapa=1):
    modal True
    zorder 130

    $ tam = 40 if texto_maior_ativo() else 32

    add Solid("#000000c8")

    frame:
        style "nb_painel"
        align (0.5, 0.5)
        xsize 1600
        ysize 900

        vbox:
            spacing 22
            text _("Exercício de escrita · campo [etapa] de 2") style "nb_titulo"
            if pedido:
                frame:
                    style "nb_cartao"
                    text pedido style "nb_texto" size (tam - 4) xmaximum 1460
            text prompt style "nb_texto" size tam color gui.accent_color xmaximum 1460
            frame:
                style "nb_cartao"
                ysize 340
                input:
                    id "input"
                    size tam
                    color "#ffffff"
                    xmaximum 1440
            text _("Digite e tecle Enter para concluir o campo. O texto não é corrigido automaticamente."):
                style "nb_texto"
                size 22
                color "#bbbbbb"

screen escrita_revisao(pedido):
    modal True
    zorder 130

    $ tam = 36 if texto_maior_ativo() else 28
    $ marcadas = sum(1 for m in escrita_marcas if m)
    $ pode_confirmar = bool(escrita_atual["req"] and escrita_atual["crit"] and marcadas == 4)

    add Solid("#000000c8")

    frame:
        style "nb_painel"
        align (0.5, 0.5)
        xsize 1600
        ysize 1000

        vbox:
            spacing 16
            text _("Revise seu rascunho") style "nb_titulo"

            viewport:
                style_prefix "nb"
                id "escrita_revisao_texto"
                ysize 330
                xfill True
                mousewheel True
                draggable True
                pagekeys True
                scrollbars "vertical"
                vscrollbar_unscrollable "hide"
                vbox:
                    spacing 10
                    xsize 1460
                    text _("Pedido") style "nb_texto" color gui.accent_color bold True
                    text pedido style "nb_texto" size tam xmaximum 1440
                    text _("Requisito") style "nb_texto" color gui.accent_color bold True
                    # req/crit já estão escapados: a substituição mostra { e [ literais.
                    text (escrita_atual["req"] or __("(vazio)")) style "nb_texto" size tam xmaximum 1440
                    text _("Critério de aceitação") style "nb_texto" color gui.accent_color bold True
                    text (escrita_atual["crit"] or __("(vazio)")) style "nb_texto" size tam xmaximum 1440

            text _("Autoavaliação: marque o que seu rascunho já tem ([marcadas] de 4).") style "nb_texto" bold True

            for i, pergunta in enumerate(ESCRITA_PERGUNTAS):
                textbutton (__(pergunta) + (__(" · sim") if escrita_marcas[i] else __(" · ainda não"))):
                    style "nb_botao"
                    xfill True
                    id ("escrita_marca_%d" % i)
                    selected escrita_marcas[i]
                    action ToggleDict(escrita_marcas, i)

            if not pode_confirmar:
                text _("Para confirmar, preencha os dois campos e marque os quatro pontos. Você também pode guardar como pendente."):
                    style "nb_texto"
                    size 22
                    color "#bbbbbb"

            hbox:
                spacing 20
                textbutton _("Reescrever o rascunho"):
                    style "nb_botao"
                    id "escrita_reescrever"
                    action Return("reescrever")
                textbutton _("Guardar como confirmado"):
                    style "nb_botao"
                    id "escrita_confirmar"
                    sensitive pode_confirmar
                    action Return("confirmado")
                textbutton _("Guardar como pendente"):
                    style "nb_botao"
                    id "escrita_pendente"
                    action Return("pendente")
