default selected_item_description = ""

# Tabela de dados dos itens da Mochila (Fase 4.3), na ordem de exibição.
define ITENS_ORDER = ["notebook", "celular", "bloco_de_notas", "caneta", "garrafinha"]

# Nome curto que aparece embaixo de cada item.
define ITENS_NOME = {
    "notebook": _("Notebook"),
    "celular": _("Celular"),
    "bloco_de_notas": _("Bloco de notas"),
    "caneta": _("Caneta"),
    "garrafinha": _("Garrafinha"),
}

# Descrição mostrada quando o item recebe foco (mouse ou teclado).
define ITENS_DESC = {
    "notebook": _("{b}Notebook{/b}{vspace=10}{i}Ferramenta essencial de qualquer dev. Carregado de códigos, sonhos e deadlines.{/i}{vspace=10}Abra para consultar os registros do projeto."),
    "celular": _("{b}Celular{/b}{vspace=10}{i}Usado para comunicação com colegas de equipe, anotações rápidas e, claro, memes no grupo.{/i}{vspace=10}Abra para ver os contatos e conversar."),
    "bloco_de_notas": _("{b}Bloco de Notas{/b}{vspace=10}{i}Útil para anotar requisitos durante entrevistas ou reuniões importantes.{/i}"),
    "caneta": _("{b}Caneta Azul{/b}{vspace=10}{i}Companheira fiel para anotar qualquer coisa, inclusive ideias geniais ou rabiscos.{/i}"),
    "garrafinha": _("{b}Garrafinha de Água{/b}{vspace=10}{i}Hidratação é vida. Não esqueça de beber água!{/i}"),
}

# Tile de item: fundo escuro; com foco (mouse ou teclado), fundo na cor de
# destaque, para a navegação pelas setas ficar visível.
style inv_tile is button:
    background Solid("#1f2730")
    hover_background Solid(gui.accent_color)
    padding (12, 12)
    xsize 200

style inv_tile_text is nb_texto:
    size 22
    hover_color "#101820"
    xalign 0.5
    text_align 0.5

# Tile unico parametrizado. Celular abre os contatos, notebook abre os
# registros da rota (notebook_screen.rpy); os demais só mostram a descrição.
# hovered tambem dispara no foco por teclado, entao a descricao aparece ao
# navegar com as setas.
screen inventory_tile(item_id):
    if getattr(store, "item_" + item_id):
        button:
            style "inv_tile"
            id ("inv_" + item_id)
            alt ITENS_DESC[item_id]
            hovered SetVariable("selected_item_description", ITENS_DESC[item_id])
            unhovered SetVariable("selected_item_description", "")
            if item_id == "celular":
                action [Hide("inventory_screen"), Show("contacts_screen")]
            elif item_id == "notebook":
                action [Hide("inventory_screen"), Show("notebook_registros")]
            else:
                action NullAction()
            vbox:
                spacing 8
                xalign 0.5
                add ("item " + item_id + "_idle") xalign 0.5
                text ITENS_NOME[item_id] style "inv_tile_text"

screen inventory_screen():
    tag inventory
    modal True
    zorder 100

    # Aberta por ShowMenu: Return() encerra o menu. Por Show (testes), Hide.
    $ fechar_mochila = If(_menu, Return(), Hide("inventory_screen"))
    $ tam = 30 if texto_maior_ativo() else 24
    key "game_menu" action fechar_mochila
    key "K_i" action fechar_mochila

    add Solid("#000000b0")

    frame:
        style "nb_painel"
        align (0.5, 0.5)
        xsize 1180

        vbox:
            spacing 20

            hbox:
                xfill True
                text _("Mochila") style "nb_titulo" yalign 0.5
                textbutton _("Fechar"):
                    style "nb_botao"
                    xalign 1.0
                    id "inventory_fechar"
                    action fechar_mochila

            hbox:
                spacing 18
                for item_id in ITENS_ORDER:
                    use inventory_tile(item_id)

            if not any(getattr(store, "item_" + i) for i in ITENS_ORDER):
                text _("A Mochila está vazia.") style "nb_texto"

            # Descrição do item com foco; altura fixa para a tela não pular.
            frame:
                style "nb_cartao"
                ysize (220 if tam > 24 else 180)
                if selected_item_description:
                    text "[selected_item_description]" style "nb_texto" size tam
                else:
                    text _("Passe o mouse ou use as setas para ver a descrição de um item.") style "nb_texto" size tam color "#c0c8d0"

            text _("Setas escolhem um item, Enter usa, Esc ou I fecha."):
                style "nb_dica"

# Botão de acesso ao inventário
screen inventory_button():
    if inventory_enabled:
        imagebutton:
            idle "item mochila_idle"
            hover "item mochila_aberta_vazia_idle"
            action ShowMenu("inventory_screen")
            alt _("Mochila")
            xpos 30
            ypos 30
            xysize (120,120)
            focus_mask True
