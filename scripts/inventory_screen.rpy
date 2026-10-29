default inventory = []
default selected_item = None

screen inventory_screen():
    modal True
    zorder 100
    key "game_menu" action Hide("inventory_screen")
    key "K_i" action Hide("inventory_screen")
    add Solid("#08151de8")
    frame:
        style "rw_panel"
        align (0.5, 0.45)
        xsize 1580
        ysize 780
        vbox:
            spacing 24
            hbox:
                xfill True
                text "Seu inventário" style "rw_heading"
                textbutton "Fechar" style "rw_action" action Hide("inventory_screen") xalign 1.0 id "inventory_close"
            text "Selecione um objeto para saber como ele pode ajudar." style "rw_caption"
            if not inventory:
                null height 70
                text "Sua mochila ainda está vazia." style "rw_heading" size 36
                text "Os objetos que você pegar aparecerão aqui." style "rw_caption"
            else:
                hbox:
                    spacing 36
                    viewport:
                        xsize 650
                        ysize 460
                        mousewheel True
                        draggable True
                        scrollbars "vertical"
                        vbox:
                            spacing 12
                            for item_id in inventory:
                                $ info = item_data.get(item_id)
                                textbutton (info["name"] if info else "Objeto guardado"):
                                    style "rw_action"
                                    xfill True
                                    selected selected_item == item_id
                                    action SetVariable("selected_item", item_id)
                    vbox:
                        spacing 20
                        xsize 780
                        if selected_item in inventory and selected_item in item_data:
                            $ info = item_data[selected_item]
                            add info["icon"] xysize (330, 260) fit "contain"
                            text info["name"] style "rw_heading" size 34
                            text info["desc"] style "rw_caption" xmaximum 760
                            if selected_item == "notebook" and notebook_in_bag:
                                text "Guardado na mochila." color "#51c8b6" size 26
                            if selected_item == "notebook" and notebook_available:
                                textbutton "Consultar registros" style "rw_action" action [Hide("inventory_screen"), Show("learning_notebook")] id "inventory_notebook"
                        else:
                            text "Escolha um objeto na lista." style "rw_caption"
            text "Esc ou I também fecha o inventário." style "rw_caption" size 24

screen inv_quick():
    zorder 20
    key "K_i" action Show("inventory_screen")
    frame:
        background Solid("#142b38ee")
        padding (20, 12)
        align (0.98, 0.025)
        hbox:
            spacing 24
            $ avatar_label = {"ideias": "Ideias", "codigo": "Código", "dialogo": "Diálogo"}.get(player_avatar, "Ideias")
            text "[player_name] · [avatar_label]" color "#eaf3f7" size 26 yalign 0.5
            textbutton "Inventário · I" style "rw_action" action Show("inventory_screen") id "inventory_open"
