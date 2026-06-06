default selected_item_description = ""

# Tabela de dados dos itens da Mochila (Fase 4.3).
# Ordem de exibicao explicita no grid 5x2.
define ITENS_ORDER = ["notebook", "celular", "bloco_de_notas", "caneta", "garrafinha"]

# Descricoes movidas para fora dos handlers `hovered` inline dos tiles.
define ITENS_DESC = {
    "notebook": "{b}Notebook{/b} {vspace=10} {i}Ferramenta essencial de qualquer dev. Carregado de códigos, sonhos e deadlines.{/i}",
    "celular": "{b}Celular{/b} {vspace=10} {i}Usado para comunicação com colegas de equipe, anotações rápidas e, claro, memes no grupo.{/i}",
    "bloco_de_notas": "{b}Bloco de Notas{/b} {vspace=10} {i}Útil para anotar requisitos durante entrevistas ou reuniões importantes.{/i}",
    "caneta": "{b}Caneta Azul{/b} {vspace=10} {i}Companheira fiel para anotar qualquer coisa, inclusive ideias geniais ou rabiscos.{/i}",
    "garrafinha": "{b}Garrafinha de Água{/b} {vspace=10} {i}Hidratação é vida. Não esqueça de beber água!{/i}",
}

# Tile unico parametrizado: reproduz UM tile atual.
# Visuais/props identicos; celular abre os contatos, os demais sao display-only (NullAction).
screen inventory_tile(item_id):
    if getattr(store, "item_" + item_id):
        imagebutton:
            idle "item [item_id]_idle"
            hover "item [item_id]_hover"
            hovered SetVariable("selected_item_description", ITENS_DESC[item_id])
            unhovered SetVariable("selected_item_description", "")
            if item_id == "celular":
                action [Hide("inventory_screen"), Show("contacts_screen")]
            else:
                action NullAction()

screen inventory_screen():
    tag inventory
    modal True
    zorder 100

    frame:
        background "#0008"
        xalign 0.5
        yalign 0.5
        xsize 740
        ysize 550

        vbox:
            spacing 15

            text "Mochila" size 40 color "#ffffff"

            hbox:
                spacing 50

                grid 5 2 spacing 15:

                    for item_id in ITENS_ORDER:
                        use inventory_tile(item_id)

                # Área de descrição embaixo do grid
            frame:
                background "#2228"
                xsize 725
                yalign 0.0

                text "[selected_item_description]":
                    color "#ffffff"
                    size 20
                    xalign 0.5

            textbutton "Fechar" action Return() xalign 0.5

# Botão de acesso ao inventário
screen inventory_button():
    if inventory_enabled:
        imagebutton:
            idle "item mochila_idle"
            hover "item mochila_aberta_vazia_idle"
            action ShowMenu("inventory_screen")
            xpos 30
            ypos 30
            xysize (120,120)
            focus_mask True
