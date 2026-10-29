default notebook_available = False

init python:
    def learning_records():
        # O estágio registra descoberta, inclusive após uma revisão orientada.
        return [
            ("Problema relatado", mission_stage >= 1, mission_problem),
            ("Regra confirmada", mission_stage >= 2, mission_rule),
            ("Critério de aceitação", mission_stage >= 3, mission_criterion),
            ("Caso limite", mission_stage >= 4, mission_edge_criterion),
            ("Acordo da equipe", negotiation_complete, negotiation_agreement),
            ("Aplicação final", transfer_complete, "Requisito: " + transfer_requirement + "\n\nCritério: " + transfer_criterion),
        ]

screen learning_notebook():
    modal True
    zorder 120
    key "game_menu" action Hide("learning_notebook")
    key "K_n" action Hide("learning_notebook")
    add Solid("#08151df5")
    $ records = learning_records()
    $ discovered = sum(1 for title, known, content in records if known)
    frame:
        style "rw_panel"
        align (0.5, 0.5)
        xsize 1600
        ysize 920
        vbox:
            spacing 20
            hbox:
                xfill True
                text "Notebook · registros da jornada" style "rw_heading" size 42
                textbutton "Fechar · N / Esc":
                    style "rw_action"
                    action Hide("learning_notebook")
                    default_focus True
                    id "notebook_close"
            text (str(discovered) + " de 6 registros descobertos · consulte sem sair da conversa.") style "rw_caption" id "notebook_progress"
            if mission_context:
                text mission_context style "rw_caption" color "#51c8b6"
            viewport:
                id "notebook_records"
                ysize 470
                xfill True
                mousewheel True
                draggable True
                arrowkeys True
                pagekeys True
                scrollbars "vertical"
                vbox:
                    spacing 20
                    xsize 1450
                    for title, known, content in records:
                        frame:
                            background Solid("#203b46")
                            padding (24, 20)
                            xfill True
                            vbox:
                                spacing 12
                                text (title + (" · registrado" if known else " · pendente")) style "rw_heading" size 32
                                if known:
                                    text content.replace("{", "{{") style "rw_caption" substitute False xmaximum 1360 size (36 if persistent.rw_large_text else 28)
                                else:
                                    text "Continue a conversa para descobrir e registrar este conteúdo." style "rw_caption" xmaximum 1360
            text "Role a página com a roda do mouse, setas ou Page Up / Page Down." style "rw_caption" size 24

screen learning_hud():
    zorder 20
    if notebook_available:
        key "K_n" action Show("learning_notebook")
