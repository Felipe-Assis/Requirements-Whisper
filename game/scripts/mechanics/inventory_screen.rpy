default selected_item_description = ""

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


                    if item_notebook:
                        imagebutton:
                            idle "item notebook_idle"
                            hover "item notebook_hover"
                            hovered SetVariable("selected_item_description", "{b}Notebook{/b} {vspace=10} {i}Ferramenta essencial de qualquer dev. Carregado de códigos, sonhos e deadlines.{/i}")
                            unhovered SetVariable("selected_item_description", "")
                            action NullAction()

                    if item_celular:
                        imagebutton:
                            idle "item celular_idle"
                            hover "item celular_hover"
                            hovered SetVariable("selected_item_description", "{b}Celular{/b} {vspace=10} {i}Usado para comunicação com colegas de equipe, anotações rápidas e, claro, memes no grupo.{/i}")
                            unhovered SetVariable("selected_item_description", "")
                            action [Hide("inventory_screen"), Show("contacts_screen")]


                    if item_bloco_de_notas:
                        imagebutton:
                            idle "item bloco_de_notas_idle"
                            hover "item bloco_de_notas_hover"
                            hovered SetVariable("selected_item_description", "{b}Bloco de Notas{/b} {vspace=10} {i}Útil para anotar requisitos durante entrevistas ou reuniões importantes.{/i}")
                            unhovered SetVariable("selected_item_description", "")
                            action NullAction()

                    if item_caneta:
                        imagebutton:
                            idle "item caneta_idle"
                            hover "item caneta_hover"
                            hovered SetVariable("selected_item_description", "{b}Caneta Azul{/b} {vspace=10} {i}Companheira fiel para anotar qualquer coisa, inclusive ideias geniais ou rabiscos.{/i}")
                            unhovered SetVariable("selected_item_description", "")
                            action NullAction()


                    if item_garrafinha:
                        imagebutton:
                            idle "item garrafinha_idle"
                            hover "item garrafinha_hover"
                            hovered SetVariable("selected_item_description", "{b}Garrafinha de Água{/b} {vspace=10} {i}Hidratação é vida. Não esqueça de beber água!{/i}")
                            unhovered SetVariable("selected_item_description", "")
                            action NullAction()

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

# Função python para adicionar itens
init python:
    def add_to_inventory(item_name):
        store_vars = renpy.store.__dict__
        var_name = f"item_{item_name}"
        if var_name in store_vars:
            setattr(renpy.store, var_name, True)
            renpy.notify(f"Item adicionado ao inventário: {item_name.replace('_',' ').capitalize()}")
        else:
            renpy.notify("Item não reconhecido.")
