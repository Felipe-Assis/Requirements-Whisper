screen campaign_workspace(title, subtitle):
    modal True
    zorder 40
    add Solid("#08151d")
    frame:
        background Solid("#142b38")
        xpos 40 ypos 28 xsize 1840 ysize 142
        padding (30, 16)
        vbox:
            spacing 10
            hbox:
                spacing 18
                text title style "rw_heading" size 42 xsize 1040
                textbutton "Projetos · N" style "lab_button" text_size 25 xsize 240 action Show("campaign_journal") id "campaign_journal_open"
                textbutton "Mochila · I" style "lab_button" text_size 25 xsize 230 action Show("campaign_bag") id "campaign_bag_open"
                textbutton "Salvar" style "lab_button" text_size 25 xsize 150 action ShowMenu("save") id "campaign_save"
            text subtitle style "lab_note" size 25 xmaximum 1740
    key "K_n" action Show("campaign_journal")
    key "K_i" action Show("campaign_bag")
    frame:
        style "lab_panel"
        xpos 40 ypos 188 xsize 1840 ysize 700
        transclude

screen campaign_footer(feedback):
    frame:
        background Solid("#142b38")
        xpos 40 ypos 904 xsize 1220 ysize 144
        padding (26, 12)
        vbox:
            spacing 8
            text campaign_clock_caption() size 20 color "#e7b565"
            text feedback style "lab_body" size 24 xmaximum 1150

screen campaign_hub_screen():
    modal True
    zorder 40
    use campaign_workspace("A mesa da equipe", "Três projetos, pessoas diferentes. Os resultados ficam nesta partida; salve para continuar depois."):
        hbox:
            spacing 30
            frame:
                background Solid("#0d222e") padding (0, 0)
                xsize 1050 ysize 650
                fixed:
                    use lab_scene_image("images/bg/startup_mesa.png", 1050, 650)
                    use scene_object("notebook", "Laboratório", Return("lab"), "campaign_hotspot_lab", 760, 435, 220, 150)
                    use scene_object("phone", "Gastos", Return("expenses"), "campaign_hotspot_expenses", 100, 405, 170, 165)
                    use scene_object("laptop", "Chamados", Return("tickets"), "campaign_hotspot_tickets", 425, 365, 300, 210)
                    use scene_pin("Cidade · minha semana", Return("city"), "campaign_city", 40, 185)
                    frame:
                        background Solid("#142b38ed") padding (20, 14)
                        xpos 25 ypos 25 xsize 1000
                        text "Cada objeto leva a um lugar. Escolha a ordem; revisitar começa uma nova versão desse caso." style "lab_body" size 27
            viewport:
                xsize 700 ysize 650
                mousewheel True draggable True scrollbars "vertical" arrowkeys True pagekeys True
                id "campaign_projects_scroll"
                vbox:
                    spacing 18
                    textbutton "Faculdade e oficina · opcional" style "lab_button" text_size 26 action Return("city") id "campaign_city_list"
                    for project_id, project in CAMPAIGN_PROJECTS.items():
                        frame:
                            style "lab_card" xsize 665
                            vbox:
                                spacing 10
                                text project["place"] style "rw_heading" size 32
                                text (campaign_results.get(project_id, {}).get("summary", project["challenge"])) style "lab_body" size lab_ui_size(25) xmaximum 610
                                textbutton (("Revisitar · " if project_id in campaign_results else "Investigar · ") + project["title"]) style "lab_button" text_size 27 action Return(project_id) id ("campaign_project_" + project_id)
    use campaign_footer(str(len(campaign_results)) + " de 3 projetos com retorno registrado. Um retorno pode incluir entrega adiada ou correção pendente.")
    use lab_continue("Reunir os resultados", Return("ending"), len(campaign_results) == 3, "campaign_ending_open")

screen campaign_result_card(project_id):
    $ result = campaign_results.get(project_id, {})
    $ archived_clock = result.get("clock", {})
    frame:
        style "artifact_paper" xfill True
        vbox:
            spacing 18
            use artifact_bar("Dossiê · " + CAMPAIGN_PROJECTS[project_id]["title"], CAMPAIGN_PROJECTS[project_id]["place"] + " · último retorno arquivado" if result else "Nenhuma rodada arquivada. Investigue o projeto pela mesa da equipe.")
            if result:
                hbox:
                    spacing 20
                    vbox:
                        xsize 450 spacing 12
                        text "01  ESCOPO REGISTRADO" style "artifact_muted" size 23
                        add Solid("#52656b") xsize 450 ysize 3
                        if project_id == "lab":
                            text ("Regras escolhidas: " + "; ".join(LAB_ITEMS[item]["title"] for item in result.get("plan", [])) + ".") style "artifact_ink" size lab_ui_size(25)
                        elif project_id == "tickets":
                            text ("Chamado priorizado: #" + result.get("priority", "—")) style "artifact_heading" size 27
                            text result.get("impact", "") style "artifact_ink" size lab_ui_size(25)
                        else:
                            text ("Pesquisa bancária escolhida antes da correção da lista." if result.get("outcome") == "waiting" else "Correção da lista de gastos de Lia: cancelar, confirmar a exclusão e desfazer.") style "artifact_ink" size lab_ui_size(25)
                            text ("Comportamentos verificados: " + str(len(result.get("checks", []))) + " de 3.") style "artifact_muted" size 24
                    vbox:
                        xsize 450 spacing 12
                        text "02  ENTREGA E RETORNO" style "artifact_muted" size 23
                        add Solid("#52656b") xsize 450 ysize 3
                        text result.get("summary", "Ainda sem retorno registrado.") style "artifact_ink" size lab_ui_size(25)
                        if archived_clock:
                            text ("Registro: " + archived_clock.get("day", "") + " · " + archived_clock.get("time", "")) style "artifact_muted" size 23
                        if project_id == "tickets" and result.get("next_step"):
                            text ("Último repasse: " + result["next_step"]) style "artifact_muted" size 24
                    vbox:
                        xsize 450 spacing 12
                        text "03  PRÓXIMO PASSO" style "artifact_muted" size 23
                        add Solid("#8a5623") xsize 450 ysize 3
                        text (result.get("pending", "") or "Nenhuma nova ação registrada para este caso.") style "artifact_note" size lab_ui_size(25)
                        if project_id == "lab":
                            text ("Responsáveis: " + result.get("commitment_owner", "não registrados")) style "artifact_muted" size 24
                            text ("Marco combinado: " + result.get("return_milestone", "não registrado")) style "artifact_muted" size 24
            else:
                text CAMPAIGN_PROJECTS[project_id]["challenge"] style "artifact_ink" size lab_ui_size(27)
            if project_id == "expenses" and result.get("layout"):
                text "Anexo · interface montada e amostra arquivada" style "artifact_heading" size 27
                vbox:
                    spacing 8 xsize 900
                    for module in result["layout"]:
                        frame:
                            style "artifact_card" xfill True
                            vbox:
                                spacing 6
                                text CAMPAIGN_MODULES[module] style "artifact_heading" size 25
                                if module == "balance":
                                    text (exp_money(result.get("total", 0))) style "artifact_ink" size 30
                                elif module == "records":
                                    for row in result.get("rows", []):
                                        text (row["code"] + " · " + row["name"] + " · " + exp_money(row["amount"])) style "artifact_ink" size 24
                                else:
                                    text "Excluir com confirmação · Cancelar · Desfazer" style "artifact_ink" size 24
                if not result.get("delivered"):
                    text "Protótipo arquivado; a existência desta tela não significa entrega." style "artifact_note" size 25

screen campaign_journal():
    modal True
    zorder 150
    add Solid("#06121aee")
    key "game_menu" action Hide("campaign_journal")
    key "K_n" action Hide("campaign_journal")
    frame:
        style "lab_panel" align (0.5, 0.5) xsize 1700 ysize 950
        vbox:
            spacing 20
            hbox:
                text "Dossiês da equipe" style "rw_heading" size 42 xsize 1310
                textbutton "Fechar · Esc" style "lab_button" action Hide("campaign_journal") id "campaign_journal_close"
            text "Marcos de cada caso. Revisitar só substitui este registro ao chegar ao novo retorno." style "lab_note" size 27
            viewport:
                id "campaign_journal_scroll"
                ysize 700 xfill True mousewheel True draggable True scrollbars "vertical" arrowkeys True pagekeys True
                vbox:
                    spacing 20
                    for project_id in CAMPAIGN_PROJECTS:
                        use campaign_result_card(project_id)
                    frame:
                        style "artifact_paper" xfill True
                        vbox:
                            spacing 12
                            text "Anexo pessoal · minha semana" style "artifact_heading" size 34
                            text student_summary() style "artifact_ink" size lab_ui_size(26)
                            if student_course_done:
                                textbutton "Reabrir dica da oficina" style "artifact_button" action Show("student_tip_screen")

screen campaign_closing():
    modal True
    zorder 40
    use campaign_workspace("Dossiês · balanço dos três projetos", "Entregas, retornos e próximos passos. Uma rodada encerrada pode deixar trabalho pendente."):
        viewport:
            id "campaign_closing_scroll"
            ysize 640 mousewheel True draggable True scrollbars "vertical" arrowkeys True pagekeys True
            vbox:
                spacing 20
                for project_id in CAMPAIGN_PROJECTS:
                    use campaign_result_card(project_id)
    use campaign_footer("Não existe nota por escolher o caminho mais bonito. Compare o efeito em cada pessoa e o trabalho que ainda falta.")
    use lab_continue("Voltar à mesa da equipe", Return(True), True, "campaign_closing_back")

