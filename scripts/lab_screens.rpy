# A pasta usa as mesmas preferências de leitura da jornada guiada.
init python:
    def lab_ui_apply(callback, *args):
        # Function devolve valores ao call screen; editar não deve sair da atividade.
        callback(*args)

    def lab_ui_size(base):
        return base + (6 if persistent.rw_large_text or renpy.variant("small") else 0)

    def lab_ui_phase():
        return {"investigation": "Investigação", "definition": "Requisitos", "planning": "Planejamento", "negotiation": "Acordo", "delivery": "Demonstração", "followup": "Retorno", "ending": "Encerramento"}.get(lab_phase, "Projeto")

    def lab_ui_result(result):
        return {"allowed": "Reserva aceita", "conflict": "Conflito bloqueado", "preparation_required": "Intervalo de preparação protegido", "invalid": "Horário inválido"}.get(result, str(result))

style lab_panel is rw_panel:
    background Solid("#142b38f5")
    padding (28, 24)

style lab_card is frame:
    background Solid("#203b46")
    padding (24, 20)

style lab_body is rw_caption:
    color "#eaf3f7"

style lab_note is rw_caption:
    color "#b9cdd4"

style lab_button is rw_action:
    background Solid("#294651")
    hover_background Solid("#e7b565")
    selected_background Solid("#cfa35e")
    insensitive_background Solid("#1c323d")
    padding (22, 16)
    yminimum 66
    xminimum 0

style lab_button_text is rw_action_text:
    color "#eaf3f7"
    hover_color "#122532"
    selected_color "#122532"
    insensitive_color "#91a5ad"

style lab_primary is lab_button:
    background Solid("#e7b565")
    hover_background Solid("#ffdc9f")
    insensitive_background Solid("#1c323d")

style lab_primary_text is lab_button_text:
    color "#122532"
    insensitive_color "#91a5ad"

transform lab_result_enter:
    alpha 0.0
    linear 0.14 alpha 1.0

transform lab_result_still:
    alpha 1.0

screen lab_scene_image(picture, width, height):
    # Cover preserva a proporção; o viewport limita a arte à área do cenário.
    viewport:
        xysize (width, height)
        fixed:
            xysize (width, height)
            add picture xysize (width, height) fit "cover"

# O mesmo marco mantém a leitura e o acesso à pasta entre as atividades.
screen lab_workspace(title, subtitle):
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
                spacing 30
                text title style "rw_heading" size 44 xsize 1280
                textbutton "Consultar pasta · N" style "lab_button" text_size 26 action Show("lab_journal") id "lab_workspace_journal"
            text subtitle style "lab_note" size 25 xmaximum 1740
    key "K_n" action Show("lab_journal")
    frame:
        style "lab_panel"
        xpos 40 ypos 188 xsize 1840 ysize 700
        transclude
    use lab_status

screen lab_status():
    frame:
        background Solid("#142b38")
        xpos 40 ypos 904 xsize 1220 ysize 144
        padding (26, 12)
        vbox:
            spacing 8
            text "REGISTRO DA EQUIPE" size 20 color "#e7b565"
            text (lab_feedback or "Sem cronômetro. Compare as fontes e revise suas escolhas quando precisar.") style "lab_body" size 24 xmaximum 1150

screen lab_continue(label, action, enabled=True, widget_id="lab_continue"):
    textbutton label:
        style "lab_primary"
        xpos 1290 ypos 922 xsize 590 yminimum 82
        text_size 30
        action action
        sensitive enabled
        id widget_id

screen lab_map():
    modal True
    zorder 40
    $ essential_count = sum(e in lab_evidence for e in ("sheets", "preparation", "interview"))
    use lab_workspace("Conheça o laboratório", "Segunda-feira · descubra o problema antes de propor uma solução."):
        hbox:
            spacing 30
            frame:
                background Solid("#0d222e")
                padding (0, 0)
                xsize 1100 ysize 650
                fixed:
                    if renpy.loadable("images/bg/laboratorio.png"):
                        use lab_scene_image("images/bg/laboratorio.png", 1100, 650)
                    else:
                        use lab_scene_image("images/bg/escritorio_interior_vazio.png", 1100, 650)
                    add Solid("#08151d70")
                    frame:
                        background Solid("#142b38ed") padding (20, 14)
                        xpos 24 ypos 20 xsize 1048
                        text "O trabalho acontece entre equipamentos, pessoas e registros." style "lab_body" size 28
                    for place, caption, position in [("laboratorio", "Bancada e reservas", (44, 372)), ("conversa", "Conversa com Carlos", (602, 260)), ("equipe", "Mesa da equipe · opcional", (472, 504))]:
                        textbutton caption:
                            style "lab_button" text_size 28
                            xpos position[0] ypos position[1]
                            action Return(place)
                            id ("lab_hotspot_" + place)
            viewport:
                xsize 620 ysize 650
                mousewheel True draggable True arrowkeys True pagekeys True
                scrollbars "vertical"
                vbox:
                    spacing 18
                    xsize 580
                    text "Sua investigação" style "rw_heading" size 36
                    text lab_objective() style "lab_body" size lab_ui_size(28) xmaximum 570
                    text (str(essential_count) + "/3 fontes essenciais registradas") color "#e7b565" size 28
                    text "Escolha um local pelo cenário ou pela lista:" style "lab_note" size 26
                    for place, caption, detail in [("laboratorio", "Bancada e reservas", "Planilhas e preparo dos equipamentos"), ("conversa", "Conversa com Carlos", "Como a equipe usa a agenda"), ("equipe", "Mesa da equipe · opcional", "Por que existe uma planilha paralela")]:
                        textbutton (caption + "\n{size=24}" + detail + "{/size}"):
                            style "lab_button" text_size 28 xfill True
                            action Return(place)
                            id ("lab_map_" + place)
                    if essential_count < 3:
                        text "Para seguir: observe as duas pistas da bancada e converse com Carlos." style "lab_note" size 25
    use lab_continue(("Organizar os requisitos" if essential_count == 3 else "Faltam fontes para seguir"), Return("continue"), essential_count == 3, "lab_map_continue")

screen lab_location_screen(location):
    modal True
    zorder 40
    $ place_title = {"laboratorio": "Bancada e reservas", "equipe": "Mesa da equipe", "conversa": "Conversa com Carlos"}.get(location, "Laboratório")
    $ sources = {"laboratorio": ["sheets", "preparation"], "equipe": ["offline"], "conversa": ["interview"]}.get(location, [])
    use lab_workspace(place_title, "Observe uma fonte. O relato completo entra na pasta após a conversa."):
        hbox:
            spacing 30
            frame:
                background Solid("#0d222e") padding (0, 0)
                xsize 1060 ysize 650
                fixed:
                    if location == "laboratorio" and renpy.loadable("images/bg/laboratorio.png"):
                        use lab_scene_image("images/bg/laboratorio.png", 1060, 650)
                    else:
                        use lab_scene_image("images/bg/escritorio_interior_vazio.png", 1060, 650)
                    if location == "conversa":
                        add "images/characters/carlos/thinking.png" xysize (550, 600) fit "contain" align (0.6, 1.0)
                    for index, eid in enumerate(sources):
                        textbutton ("Examinar: " + LAB_EVIDENCE[eid]["title"]):
                            style "lab_button" text_size 27
                            xpos 36 ypos (70 + index * 380) xmaximum 940
                            action Return(eid)
                            id ("lab_source_hotspot_" + eid)
            viewport:
                id "lab_sources_scroll"
                xsize 660 ysize 640
                mousewheel True draggable True arrowkeys True pagekeys True
                scrollbars "vertical"
                vbox:
                    spacing 22
                    xsize 620
                    text "Fontes deste local" style "rw_heading" size 34
                    text "As mesmas ações do cenário, em uma lista acessível." style "lab_note" size 26
                    for eid in sources:
                        frame:
                            style "lab_card" xfill True
                            vbox:
                                spacing 14
                                text LAB_EVIDENCE[eid]["title"] style "rw_heading" size 30
                                text LAB_EVIDENCE[eid]["source"] style "lab_note" size 25
                                if eid in lab_evidence:
                                    text "Registrado na pasta" color "#51c8b6" size 26
                                    text LAB_EVIDENCE[eid]["text"] style "lab_body" size lab_ui_size(27)
                                textbutton ("Rever fonte" if eid in lab_evidence else "Examinar fonte"):
                                    style "lab_button" text_size 27
                                    action Return(eid)
                                    id ("lab_source_" + eid)
    use lab_continue("Voltar aos locais", Return("back"), True, "lab_location_back")

screen lab_board():
    modal True
    zorder 40
    default selected_evidence = None
    $ board_ready = lab_links.get("conflict") == "sheets" and lab_links.get("preparation") == "preparation"
    use lab_workspace("Da evidência ao requisito", "Selecione uma fonte à esquerda. Depois, escolha a regra que ela sustenta à direita."):
        hbox:
            spacing 30
            vbox:
                spacing 14
                xsize 740
                text "1. Escolha a evidência" style "rw_heading" size 32
                viewport:
                    xsize 740 ysize 570
                    mousewheel True draggable True arrowkeys True pagekeys True
                    scrollbars "vertical"
                    vbox:
                        spacing 14
                        xsize 700
                        for eid in lab_evidence:
                            button:
                                style "lab_button" xfill True
                                selected selected_evidence == eid
                                action SetScreenVariable("selected_evidence", eid)
                                id ("lab_evidence_" + eid)
                                vbox:
                                    spacing 10
                                    text (LAB_EVIDENCE[eid]["title"] + (" · selecionada" if selected_evidence == eid else "")) style "lab_button_text" size lab_ui_size(27)
                                    text LAB_EVIDENCE[eid]["source"] style "lab_button_text" size 24
                                    if selected_evidence == eid:
                                        text LAB_EVIDENCE[eid]["text"] style "lab_button_text" size lab_ui_size(25)
                        if not lab_evidence:
                            text "As fontes aparecerão aqui após a investigação." style "lab_note" size 28
            vbox:
                spacing 14
                xsize 970
                text "2. Ligue à regra do projeto" style "rw_heading" size 32
                viewport:
                    id "lab_rules_scroll"
                    xsize 970 ysize 570
                    mousewheel True draggable True arrowkeys True pagekeys True
                    scrollbars "vertical"
                    vbox:
                        spacing 16
                        xsize 930
                        for rule_id in ("conflict", "preparation", "clarity"):
                            frame:
                                style "lab_card" xfill True padding (20, 14)
                                vbox:
                                    spacing 12
                                    text LAB_ITEMS[rule_id]["title"] style "rw_heading" size lab_ui_size(28)
                                    if rule_id in lab_links:
                                        $ linked = lab_links[rule_id]
                                        $ supported = linked == {"conflict": "sheets", "preparation": "preparation", "clarity": "interview"}[rule_id]
                                        text (("Fonte confirmada: " if supported else "Hipótese a revisar: ") + LAB_EVIDENCE[linked]["title"]) color ("#51c8b6" if supported else "#e7b565") size 25
                                    else:
                                        text "Sem fonte vinculada" style "lab_note" size 25
                                    textbutton ("Ligar fonte selecionada" if selected_evidence else "Selecione uma fonte primeiro"):
                                        style "lab_button" text_size 26
                                        sensitive selected_evidence is not None
                                        action Function(lab_ui_apply, lab_link, rule_id, selected_evidence)
                                        id ("lab_rule_" + rule_id)
    use lab_continue("Planejar a entrega", Return(True), board_ready, "lab_board_continue")

screen lab_planning():
    modal True
    zorder 40
    use lab_workspace("Uma semana, três pontos", "Monte uma entrega possível. Retirar um item permite experimentar outro plano."):
        hbox:
            spacing 30
            viewport:
                id "lab_plan_scroll"
                xsize 1130 ysize 650
                mousewheel True draggable True arrowkeys True pagekeys True
                scrollbars "vertical"
                vbox:
                    spacing 16
                    xsize 1090
                    for item_id in ("conflict", "preparation", "clarity"):
                        frame:
                            style "lab_card" xfill True
                            vbox:
                                spacing 10
                                hbox:
                                    spacing 18
                                    text LAB_ITEMS[item_id]["title"] style "rw_heading" size lab_ui_size(29) xsize 780
                                    text (str(LAB_ITEMS[item_id]["cost"]) + " pt") color "#e7b565" size 29
                                text LAB_ITEMS[item_id]["description"] style "lab_body" size lab_ui_size(26)
                                if item_id == "preparation":
                                    text "Depende de: proteção contra conflito." style "lab_note" size 25
                                textbutton (("Retirar: " if item_id in lab_plan else "Adicionar: ") + LAB_ITEMS[item_id]["title"]):
                                    style "lab_button" text_size 26
                                    selected item_id in lab_plan
                                    action Function(lab_ui_apply, lab_toggle_plan, item_id)
                                    id ("lab_plan_" + item_id)
            vbox:
                spacing 22
                xsize 580
                text "Capacidade da semana" style "rw_heading" size 34
                text (str(lab_plan_cost()) + " / 3 pontos") size 60 bold True color "#e7b565"
                hbox:
                    spacing 12
                    for point in range(3):
                        frame:
                            background Solid("#e7b565" if point < lab_plan_cost() else "#294651")
                            xsize 160 ysize 18 padding (0, 0)
                text "O plano escolhido" style "rw_heading" size 30
                if lab_plan:
                    for item_id in lab_plan:
                        text ("• " + LAB_ITEMS[item_id]["title"]) style "lab_body" size lab_ui_size(27) xmaximum 570
                else:
                    text "Adicione pelo menos um item para conversar sobre a entrega." style "lab_note" size lab_ui_size(28)
                text "O que ficar de fora precisa entrar no acordo com a equipe. Testar não acrescenta regras ao plano." style "lab_note" size lab_ui_size(26) xmaximum 570
    use lab_continue("Conversar sobre este plano", Return(True), lab_plan_ready(), "lab_plan_continue")

screen lab_demo():
    modal True
    zorder 40
    default selected_case = None
    $ case_details = {"overlap": ("Microscópio", "14h30–15h30", "O horário cruza uma reserva existente."), "adjacent": ("Microscópio", "15h00–16h00", "Começa no instante em que a reserva anterior termina."), "preparation": ("Microscópio", "15h05–16h05", "Há cinco minutos livres. A técnica precisa de dez."), "other": ("Centrífuga", "14h00–15h00", "Outro equipamento pode ter uma reserva no mesmo horário.")}
    $ demo_subtitle = "Revisão 2 em verificação · a versão anterior continua em uso." if lab_delivery == "revision_pending" else "Protótipo de investigação · compare os resultados com as necessidades observadas." if lab_commitment == "investigar_agora" and lab_delivery == "not_delivered" else "Revisão " + str(lab_revision) + " · compare o pacote com as necessidades antes de confirmar o uso."
    use lab_workspace("Demonstração da agenda", demo_subtitle):
        hbox:
            spacing 30
            viewport:
                id "lab_calendar_scroll"
                xsize 1000 ysize 650
                mousewheel True draggable True arrowkeys True pagekeys True
                scrollbars "vertical"
                vbox:
                    xsize 960 spacing 18
                    hbox:
                        spacing 20
                        text "Agenda · reservas" style "rw_heading" size 34
                        text ("VERSÃO " + str(lab_revision)) color "#e7b565" size 25 yalign 0.5
                    if "clarity" in lab_plan:
                        frame:
                            style "lab_card" xsize 960
                            vbox:
                                spacing 14
                                text "Consulta unificada" style "rw_heading" size 28
                                hbox:
                                    spacing 28
                                    vbox:
                                        xsize 420 spacing 8
                                        text "Reserva anterior · Ana" style "lab_body" size 26
                                        text "Microscópio · 14h00–15h00" style "lab_body" size 26
                                    vbox:
                                        xsize 420 spacing 8
                                        text "Tentativa de reserva" style "lab_body" size 26
                                        text ((case_details[selected_case][0] + " · " + case_details[selected_case][1]) if selected_case else "Escolha um caso de teste") style "lab_body" size 26
                    else:
                        text "Consulta por registros" style "rw_heading" size 28
                        textbutton "Consultar reserva anterior":
                            style "lab_button" text_size 28
                            action Show("lab_reservation_reference")
                            id "lab_existing_open"
                        text "Equipamento e horário anteriores ficam no registro separado. O calendário legível reuniria as duas consultas." style "lab_note" size lab_ui_size(25)
                    fixed:
                        xsize 960 ysize 215
                        add Solid("#0d222e")
                        for index, hour in enumerate(("14h00", "14h30", "15h00", "15h30", "16h00", "16h30")):
                            text hour xpos (22 + index * 160) ypos 16 color "#b9cdd4" size 24
                            add Solid("#294651") xpos (22 + index * 160) ypos 55 xsize 2 ysize 138
                        if "clarity" in lab_plan:
                            frame:
                                background Solid("#3e6879") padding (16, 14)
                                xpos 24 ypos 66 xsize 320 ysize 68
                                text "Ana · reserva mantida" size 25 color "#eaf3f7"
                        if selected_case:
                            frame:
                                background Solid("#e7b565") padding (16, 14)
                                xpos (24 + int((LAB_CASES[selected_case]["candidate"][1] - 840) * 320 / 60)) ypos 146 xsize 320 ysize 54
                                text ("Tentativa · " + ("centrífuga" if selected_case == "other" else case_details[selected_case][1])) size 22 color "#122532"
                    if selected_case:
                        text case_details[selected_case][2] style "lab_note" size lab_ui_size(26)
                        if selected_case in lab_test_results:
                            text lab_ui_result(lab_test_results[selected_case]) style "rw_heading" size 32 color "#e7b565" id "lab_test_result" at (lab_result_enter if _preferences.transitions else lab_result_still)
                    else:
                        text "Escolha um caso ao lado. O resultado ficará registrado na pasta." style "lab_note" size lab_ui_size(27)
            viewport:
                xsize 710 ysize 650
                mousewheel True draggable True arrowkeys True pagekeys True
                scrollbars "vertical"
                vbox:
                    spacing 16 xsize 670
                    text "Casos de teste" style "rw_heading" size 34
                    for case_id in ("overlap", "adjacent", "preparation", "other"):
                        button:
                            style "lab_button" xfill True
                            selected selected_case == case_id
                            action [SetScreenVariable("selected_case", case_id), Function(lab_ui_apply, lab_run_test, case_id)]
                            id ("lab_test_" + case_id)
                            vbox:
                                spacing 8
                                text LAB_CASES[case_id]["title"] style "lab_button_text" size lab_ui_size(28)
                                text (case_details[case_id][0] + " · " + case_details[case_id][1]) style "lab_button_text" size 25
                                if case_id in lab_test_results:
                                    text lab_ui_result(lab_test_results[case_id]) style "lab_button_text" size 24
                    text "Um resultado aceito pode revelar uma regra ausente. A implementação só muda após uma decisão da equipe." style "lab_note" size 25
    use lab_continue("Levar os resultados à equipe", Return(True), bool(lab_test_results), "lab_demo_continue")

screen lab_reservation_reference():
    modal True
    zorder 145
    key "game_menu" action Hide("lab_reservation_reference")
    add Solid("#08151de8")
    frame:
        style "lab_panel"
        align (0.5, 0.5) xsize 1120
        vbox:
            spacing 24
            text "Registro da reserva anterior" style "rw_heading" size 42
            text "Ana · reserva mantida" style "rw_heading" size 34 color "#99ccff" id "lab_existing_owner"
            text "Microscópio · 14h00–15h00" style "lab_body" size lab_ui_size(32)
            text "Preservada em todos os testes. Uma tentativa recusada não substitui este agendamento." style "lab_note" size lab_ui_size(28)
            textbutton "Voltar à agenda · Esc" style "lab_button" text_size 28 action Hide("lab_reservation_reference") default_focus True id "lab_existing_close"

screen lab_journal():
    modal True
    zorder 140
    key "game_menu" action Hide("lab_journal")
    key "K_n" action Hide("lab_journal")
    add Solid("#08151df5")
    frame:
        style "lab_panel"
        xpos 150 ypos 70 xsize 1620 ysize 940
        vbox:
            spacing 20
            hbox:
                spacing 40
                text "Pasta de trabalho" style "rw_heading" size 44 xsize 1070
                textbutton "Fechar · N / Esc" style "lab_button" text_size 27 action Hide("lab_journal") default_focus True id "lab_journal_close"
            text (lab_ui_phase() + " · " + lab_objective()) style "lab_note" size 27
            viewport:
                id "lab_journal_scroll"
                xsize 1560 ysize 650
                mousewheel True draggable True arrowkeys True pagekeys True
                scrollbars "vertical"
                vbox:
                    spacing 20 xsize 1490
                    text "Evidências e fontes" style "rw_heading" size 34
                    if not lab_evidence:
                        text "Nenhuma fonte registrada. Visite a bancada e converse com Carlos." style "lab_note" size 28
                    for eid in lab_evidence:
                        frame:
                            style "lab_card" xfill True
                            vbox:
                                spacing 10
                                text LAB_EVIDENCE[eid]["title"] style "rw_heading" size 30
                                text LAB_EVIDENCE[eid]["source"] style "lab_note" size 25
                                text LAB_EVIDENCE[eid]["text"] style "lab_body" size lab_ui_size(28)
                    text "Projeto e compromisso" style "rw_heading" size 34
                    frame:
                        style "lab_card" xfill True
                        vbox:
                            spacing 12
                            if lab_initial_plan:
                                text ("Plano inicial: " + ", ".join(LAB_ITEMS[i]["title"] for i in lab_initial_plan)) style "lab_body" size lab_ui_size(28)
                            else:
                                text ("Plano em discussão: " + (", ".join(LAB_ITEMS[i]["title"] for i in lab_plan) or "ainda não definido")) style "lab_body" size lab_ui_size(28)
                            if lab_repaired:
                                text ("Revisão 2 · nova rodada: " + ", ".join(LAB_ITEMS[i]["title"] for i in lab_plan)) style "lab_body" size lab_ui_size(28)
                            text ("Entrega: " + ("revisão 2 em verificação; versão anterior em uso" if lab_delivery == "revision_pending" else "adiada · investigação em andamento" if lab_commitment == "investigar_agora" and lab_delivery == "not_delivered" else "ainda não realizada" if lab_delivery == "not_delivered" else "revisão reparada entregue" if lab_delivery == "repaired" else "pacote confirmado na bancada")) style "lab_body" size lab_ui_size(28)
                            text ("Acordo: " + {"base_primeiro": "Entregar a base antes da integração", "investigar_agora": "Investigar integração nesta semana", "": "ainda não combinado"}.get(lab_commitment, lab_commitment)) style "lab_body" size lab_ui_size(28)
                            if lab_commitment:
                                text ("Responsáveis: " + lab_commitment_owner + " · retorno na " + lab_return_milestone) style "lab_note" size lab_ui_size(26)
                            else:
                                text "Responsáveis e retorno serão combinados com a equipe." style "lab_note" size lab_ui_size(26)
                            text ("Situação: " + {"open": "em aberto", "fulfilled": "cumprido", "pending": "pendente", "revised": "revisado", "renegotiated": "renegociado"}.get(lab_commitment_status, lab_commitment_status)) style "lab_note" size 26
                            for case_id, result in lab_test_results.items():
                                text (LAB_CASES[case_id]["title"] + ": " + lab_ui_result(result)) style "lab_body" size lab_ui_size(26)
                            if lab_repaired:
                                text "Reparação registrada. Evidências e acordo anteriores foram preservados." color "#51c8b6" size 27
            text "A pasta não altera seu plano. Role com mouse, setas ou Page Up / Page Down." style "lab_note" size 24

screen lab_hud():
    zorder 20
    if lab_active:
        key "K_n" action Show("lab_journal")
        frame:
            background Solid("#142b38f5")
            xpos 30 ypos 20 xsize 1860
            padding (24, 15)
            hbox:
                spacing 24
                vbox:
                    spacing 7 xsize 1400
                    text ("LABORATÓRIO · " + lab_ui_phase()) color "#e7b565" size 23
                    text lab_objective() style "lab_body" size lab_ui_size(27) xmaximum 1390
                textbutton "Pasta de trabalho · N" style "lab_button" text_size 26 action Show("lab_journal") yalign 0.5 id "lab_journal_open"

screen lab_final(ending):
    modal True
    zorder 40
    $ final_text = {"reliable": ("Uma agenda em que a equipe confia", "A entrega protege os conflitos e o preparo do microscópio. A equipe pode trabalhar com uma regra que corresponde às fontes.", "Mantenham o retorno combinado para acompanhar a adoção e decidir os próximos passos."), "waiting": ("Uma resposta ainda em construção", "A semana foi usada para investigar. A integração não foi entregue, e a equipe ainda aguarda a próxima decisão.", "Retomem a proteção das reservas e transformem a pesquisa em um novo acordo com prazo e responsáveis."), "repaired": ("A confiança também se repara", "A equipe reconheceu a lacuna e revisou a agenda. A nova versão protege o conflito e o preparo sem apagar o acordo anterior.", "Acompanhem o uso da versão corrigida e confirmem se a rotina da técnica foi atendida."), "unowned": ("O risco precisa de um responsável", "A versão entregue deixou uma proteção de fora. O problema veio do escopo implementado, e não do ato de testá-lo.", "Uma correção precisa de responsável, retorno e uma regra confirmada pela fonte.")}.get(ending)
    use lab_workspace("O retorno da equipe", "O resultado acompanha o que foi investigado, planejado e combinado."):
        hbox:
            spacing 45
            vbox:
                xsize 1090 spacing 26
                text final_text[0] style "rw_heading" size 48 color "#e7b565" xmaximum 1080
                text final_text[1] style "lab_body" size lab_ui_size(32) xmaximum 1060
                frame:
                    style "lab_card" xfill True
                    vbox:
                        spacing 14
                        text "O próximo cuidado" style "rw_heading" size 32 id "lab_final_care"
                        text final_text[2] style "lab_body" size lab_ui_size(28)
                text "Sua pasta continua disponível para comparar as decisões desta campanha." style "lab_note" size 27
            vbox:
                xsize 590 spacing 22
                text "Trajeto do projeto" style "rw_heading" size 34
                text (str(len(lab_evidence)) + " fontes registradas") style "lab_body" size 29
                text (str(len(lab_test_results)) + " casos experimentados") style "lab_body" size 29
                text ("Versão " + str(lab_revision) + (" · revisão em verificação" if lab_delivery == "revision_pending" else " · investigação, sem entrega" if lab_delivery == "not_delivered" else " · reparação entregue" if lab_delivery == "repaired" else " · entrega inicial")) style "lab_body" size 29
                textbutton "Jogar a campanha novamente" style "lab_primary" text_size 27 xfill True action Return("replay") id "lab_final_replay"
                textbutton "Voltar ao menu" style "lab_button" text_size 28 xfill True action Return("menu") id "lab_final_menu"
                textbutton "Conhecer a jornada guiada" style "lab_button" text_size 27 xfill True action Return("legacy") id "lab_final_legacy"
