# scripts/inventory_screen.rpy

default inventory = [] # Lista global de itens (use em variables.rpy se preferir)
default selected_item = None

# Dicionário dos itens possíveis (adicione mais conforme seu jogo cresce)
define item_data = {
    "notebook": {"name": "Notebook", "desc": "Seu fiel companheiro de estudos e estágios.", "icon": "items/notebook.png"},
    "mochila": {"name": "Mochila", "desc": "Carrega tudo que você precisa!", "icon": "items/mochila.png"},
    "celular": {"name": "Celular", "desc": "Útil para se comunicar e pesquisar rápido.", "icon": "items/celular.png"},
    "bloco": {"name": "Bloco de notas", "desc": "Ótimo para anotar requisitos ou ideias.", "icon": "items/bloco.png"},
    "caneta": {"name": "Caneta", "desc": "Sempre tenha uma à mão!", "icon": "items/caneta.png"},
    # ... adicione mais aqui
}

screen inventory_screen():
    modal True
    tag inventory
    frame:
        style_prefix "inventory"
        vbox:
            text "Inventário" size 30
            null height 15
            hbox:
                # Slots do inventário
                for i in range(8):  # Número de slots exibidos
                    if i < len(inventory):
                        $ item = inventory[i]
                        imagebutton:
                            idle item_data[item]["icon"]
                            action SetVariable("selected_item", item)
                            tooltip item_data[item]["name"]
                            focus_mask True
                    else:
                        add "items/slot_empty.png" # Imagem slot vazio
            null height 20
            # Área de descrição do item selecionado
            if selected_item:
                hbox:
                    add item_data[selected_item]["icon"]
                    vbox:
                        text "[item_data[selected_item]['name']]" size 20
                        text "[item_data[selected_item]['desc']]" size 15
            else:
                text "Selecione um item para ver detalhes." size 15
            null height 30
            # Botão para fechar
            textbutton "Fechar" action Hide("inventory_screen")

# Exemplo de botão para abrir o inventário em algum lugar do HUD
screen inv_quick():
    vbox:
        xpos 0.97
        ypos 0.05
        textbutton "Inventário" action Show("inventory_screen")
