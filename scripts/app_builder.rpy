init python:
    def campaign_drop_module(drags, target):
        card = drags[0]
        if target is not None and target.drag_name.startswith("slot_"):
            campaign_place_module("expenses", card.drag_name, int(target.drag_name[5:]))
        card.snap(0, list(CAMPAIGN_MODULES).index(card.drag_name) * 152, 0.15 if preferences.transitions else 0)
        renpy.retain_after_load()
        renpy.restart_interaction()

screen campaign_app_builder(project_id):
    modal True
    zorder 40
    use campaign_workspace("Uma tela que você pode montar", "Lia: quero conferir o lançamento sem perder de vista quanto gastei. Qual informação você coloca primeiro?"):
        hbox:
            spacing 30
            frame:
                style "artifact_paper" xsize 490 ysize 644
                viewport:
                    xfill True ysize 600 mousewheel True draggable True arrowkeys True pagekeys True scrollbars "vertical"
                    vbox:
                        xsize 410 spacing 16
                        use artifact_bar("Editor de interface", "Gastos de Lia · três módulos")
                        text "Escolha por clique ou teclado" style "artifact_heading" size 28
                        for module, caption in CAMPAIGN_MODULES.items():
                            textbutton (("Selecionado · " if campaign_builder_selected == module else "Selecionar · ") + caption):
                                style "artifact_button" text_size 25 xfill True
                                selected campaign_builder_selected == module
                                action SetVariable("campaign_builder_selected", module)
                                id ("builder_select_" + module)
                        text "Colocar na posição:" style "artifact_ink" size 25
                        hbox:
                            spacing 12
                            for slot in range(3):
                                textbutton str(slot + 1) style "artifact_button" text_size 27 xsize 120 action Function(lab_ui_apply, campaign_place_module, project_id, campaign_builder_selected, slot) id ("builder_slot_" + str(slot))
                        text "Ordem atual" style "artifact_heading" size 27
                        for slot, module in enumerate(campaign_layout(project_id)):
                            text (str(slot + 1) + ". " + CAMPAIGN_MODULES[module]) style "artifact_muted" size 24
                        text "A ordem muda a tela da próxima atividade. Organizar a interface não corrige suas regras." style "artifact_muted" size lab_ui_size(25)
            vbox:
                spacing 16
                fixed:
                    xsize 1210 ysize 570
                    # A moldura fica fora do draggroup; somente os três slots recebem cartões.
                    add Solid("#24383e") xpos 710 ypos 0 xsize 440 ysize 570
                    add Solid("#f5f5f1") xpos 720 ypos 10 xsize 420 ysize 548
                    text "Lia · Gastos" style "artifact_heading" size 27 xpos 742 ypos 15
                    text "Prévia da ordem escolhida" style "artifact_muted" size 20 xpos 742 ypos 49
                    draggroup:
                        xsize 1210 ysize 570
                        for slot, module in enumerate(campaign_layout(project_id)):
                            drag:
                                drag_name ("slot_" + str(slot))
                                id ("builder_drop_" + str(slot))
                                draggable False droppable True
                                xpos 725 ypos (82 + slot * 154)
                                frame:
                                    style "artifact_card" padding (18, 14)
                                    xsize 410 ysize 146
                                    vbox:
                                        spacing 8
                                        text (str(slot + 1) + " · " + CAMPAIGN_MODULES[module]) style "artifact_heading" size 25
                                        if module == "balance":
                                            text "R$ 100,00" style "artifact_heading" size 35
                                        elif module == "records":
                                            text "AL-17 · Almoço    R$ 20,00" style "artifact_ink" size 23
                                            text "AL-18 · Almoço    R$ 20,00" style "artifact_muted" size 22
                                        else:
                                            text "Excluir · Cancelar · Desfazer" style "artifact_ink" size 23
                                            text "Ações da próxima atividade" style "artifact_muted" size 21
                        for index, (module, caption) in enumerate(CAMPAIGN_MODULES.items()):
                            drag:
                                drag_name module
                                id ("builder_drag_" + module)
                                draggable True droppable False
                                dragged campaign_drop_module
                                mouse_drop True
                                xpos 0 ypos (index * 152)
                                frame:
                                    style "artifact_paper" padding (24, 20)
                                    xsize 550 ysize 126
                                    hbox:
                                        spacing 20
                                        text "≡" style "artifact_muted" size 40
                                        vbox:
                                            spacing 8
                                            text caption style "artifact_heading" size 30
                                            text "Arrastar para uma posição →" style "artifact_muted" size 24
                text "Arraste os módulos para a tela ou use seleção e posição. A próxima atividade mantém essa ordem com dados e ações funcionais." style "lab_note" size 24 xmaximum 1170
    use campaign_footer(campaign_builder_feedback)
    use lab_continue("Usar esta interface", Return(True), True, "campaign_builder_continue")
