# A pasta usa as mesmas preferências de leitura da jornada guiada.
init python:
    def lab_ui_apply(callback, *args):
        # Function devolve valores ao call screen; editar não deve sair da atividade.
        callback(*args)
        # Uma atividade pode permanecer no mesmo call screen durante várias edições.
        renpy.retain_after_load()

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
                spacing 18
                text title style "rw_heading" size 44 xsize (1140 if campaign_active else 1280)
                textbutton "Consultar pasta · N" style "lab_button" text_size 26 xsize 320 action Show("lab_journal") id "lab_workspace_journal"
                if campaign_active:
                    textbutton "Mochila · I" style "lab_button" text_size 26 xsize 240 action Show("campaign_bag") id "lab_workspace_bag"
            text subtitle style "lab_note" size 25 xmaximum 1740
    key "K_n" action Show("lab_journal")
    if campaign_active:
        key "K_i" action Show("campaign_bag")
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
            text campaign_clock_caption() size 20 color "#e7b565"
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
                    frame:
                        background Solid("#142b38ed") padding (20, 14)
                        xpos 24 ypos 20 xsize 1048
                        text "O trabalho acontece entre equipamentos, pessoas e registros." style "lab_body" size 28
                    use scene_object("clipboard", "Bancada e reservas", Return("laboratorio"), "lab_hotspot_laboratorio", 310, 250, 220, 160)
                    use scene_pin("Conversa com Carlos", Return("conversa"), "lab_hotspot_conversa", 730, 240)
                    use scene_object("laptop", "Mesa da equipe · opcional", Return("equipe"), "lab_hotspot_equipe", 750, 350, 240, 165)
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
                        use lab_scene_image("images/bg/startup_mesa.png", 1060, 650)
                    if location == "conversa":
                        add "images/characters/carlos/thinking.png" xysize (550, 600) fit "contain" align (0.6, 1.0)
                    for eid in sources:
                        if eid == "interview":
                            use scene_pin("Conversar com Carlos", Return(eid), "lab_source_hotspot_interview", 450, 180)
                        else:
                            use scene_object(("laptop" if eid == "offline" else "clipboard"), {"sheets": "Planilhas", "preparation": "Ficha de preparo", "offline": "Cópia local"}[eid], Return(eid), "lab_source_hotspot_" + eid, {"sheets": 400, "preparation": 205, "offline": 480}[eid], {"sheets": 260, "preparation": 190, "offline": 360}[eid], 200, 155)
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
        viewport:
            id "lab_board_scroll"
            ysize 650
            mousewheel True draggable True arrowkeys True pagekeys True
            scrollbars "vertical"
            frame:
                style "artifact_paper" xsize 1730
                vbox:
                    spacing 22
                    use artifact_bar("Registro de requisitos", "Laboratório / Fontes e regras / Documento em revisão")
                    hbox:
                        spacing 28
                        vbox:
                            spacing 14 xsize 630
                            text "1. Escolha a evidência" style "artifact_heading" size 32
                            text "FONTES REGISTRADAS" style "artifact_muted" size 23
                            for eid in lab_evidence:
                                button:
                                    style "artifact_button" xfill True
                                    selected_background Solid("#b9d8d2")
                                    selected selected_evidence == eid
                                    action SetScreenVariable("selected_evidence", eid)
                                    id ("lab_evidence_" + eid)
                                    vbox:
                                        spacing 10
                                        text (LAB_EVIDENCE[eid]["title"] + (" · selecionada" if selected_evidence == eid else "")) style "artifact_ink" size lab_ui_size(27)
                                        text LAB_EVIDENCE[eid]["source"] style "artifact_muted" size 24
                                        if selected_evidence == eid:
                                            text LAB_EVIDENCE[eid]["text"] style "artifact_ink" size lab_ui_size(25)
                            if not lab_evidence:
                                text "As fontes aparecerão aqui após a investigação." style "artifact_muted" size 28
                        vbox:
                            spacing 14 xsize 1010
                            text "2. Ligue à regra do projeto" style "artifact_heading" size 32
                            hbox:
                                spacing 18
                                text "ID" style "artifact_muted" size 23 xsize 70
                                text "DESCRIÇÃO / FONTE / CRITÉRIO" style "artifact_muted" size 23
                            for number, rule_id in enumerate(("conflict", "preparation", "clarity"), 1):
                                frame:
                                    style "artifact_card" xfill True
                                    hbox:
                                        spacing 18
                                        text ("R0" + str(number)) style "artifact_muted" size 25 xsize 70
                                        vbox:
                                            spacing 12 xsize 850
                                            text LAB_ITEMS[rule_id]["title"] style "artifact_heading" size lab_ui_size(28)
                                            text ("Critério: " + LAB_ITEMS[rule_id]["description"]) style "artifact_ink" size lab_ui_size(25)
                                            if rule_id in lab_links:
                                                $ linked = lab_links[rule_id]
                                                $ supported = linked == {"conflict": "sheets", "preparation": "preparation", "clarity": "interview"}[rule_id]
                                                text (("Fonte confirmada: " if supported else "Hipótese a revisar: ") + LAB_EVIDENCE[linked]["title"]) color ("#286b66" if supported else "#8a5623") size lab_ui_size(25)
                                            else:
                                                text "Sem fonte vinculada" style "artifact_muted" size lab_ui_size(25)
                                            textbutton ("Ligar fonte selecionada" if selected_evidence else "Selecione uma fonte primeiro"):
                                                style "artifact_button" text_size 26
                                                sensitive selected_evidence is not None
                                                action Function(lab_ui_apply, lab_link, rule_id, selected_evidence)
                                                id ("lab_rule_" + rule_id)
    use lab_continue("Planejar a entrega", Return(True), board_ready, "lab_board_continue")

screen lab_planning():
    modal True
    zorder 40
    use lab_workspace("Uma semana, três pontos", "Monte uma entrega possível. Retirar um item permite experimentar outro plano."):
        viewport:
            id "lab_plan_scroll"
            ysize 650
            mousewheel True draggable True arrowkeys True pagekeys True
            scrollbars "vertical"
            frame:
                style "artifact_paper" xsize 1730
                vbox:
                    spacing 22
                    use artifact_bar("Quadro da equipe", "Laboratório / Planejamento da primeira entrega / Estimativas em pontos")
                    hbox:
                        spacing 30
                        text "Capacidade da semana" style "artifact_heading" size 30
                        text (str(lab_plan_cost()) + " / 3 pontos") style "artifact_ink" size 34 bold True
                    text "Mova os cartões adicionando ou retirando itens. O acordo só inclui o que está nesta rodada." style "artifact_muted" size lab_ui_size(25)
                    hbox:
                        spacing 22
                        for bucket, caption in (("review", "A avaliar"), ("week", "Nesta rodada"), ("dependency", "Dependência pendente")):
                            frame:
                                background Solid("#e4e9e6") padding (14, 16) xsize 538
                                vbox:
                                    spacing 14
                                    text caption style "artifact_heading" size 29
                                    $ bucket_items = [item for item in ("conflict", "preparation", "clarity") if ("week" if item in lab_plan else "dependency" if item == "preparation" and "conflict" not in lab_plan else "review") == bucket]
                                    text (str(len(bucket_items)) + " item" + ("" if len(bucket_items) == 1 else "s")) style "artifact_muted" size 24
                                    for item_id in bucket_items:
                                        frame:
                                            style "artifact_card" xfill True
                                            vbox:
                                                spacing 12
                                                text LAB_ITEMS[item_id]["title"] style "artifact_heading" size lab_ui_size(29)
                                                text ("Estimativa: " + str(LAB_ITEMS[item_id]["cost"]) + " pt") style "artifact_ink" size 27 bold True
                                                text LAB_ITEMS[item_id]["description"] style "artifact_ink" size lab_ui_size(26)
                                                text ("Depende de: proteção contra conflito." if item_id == "preparation" else "Sem dependência de outro item do pacote.") style "artifact_muted" size lab_ui_size(25)
                                                text ("Situação: no pacote" if item_id in lab_plan else "Situação: fora do pacote") style "artifact_note" size 25
                                                textbutton (("Retirar: " if item_id in lab_plan else "Adicionar: ") + LAB_ITEMS[item_id]["title"]):
                                                    style "artifact_button" text_size lab_ui_size(25) xfill True
                                                    selected item_id in lab_plan
                                                    action Function(lab_ui_apply, lab_toggle_plan, item_id)
                                                    id ("lab_plan_" + item_id)
                                    if not bucket_items:
                                        text "Nenhum item nesta coluna." style "artifact_muted" size lab_ui_size(25)
                    text "O que ficar de fora precisa entrar no acordo com a equipe. Testar não acrescenta regras ao plano." style "artifact_note" size lab_ui_size(26)
    use lab_continue("Conversar sobre este plano", Return(True), lab_plan_ready(), "lab_plan_continue")

screen lab_demo():
    modal True
    zorder 40
    default selected_case = None
    $ case_details = {"overlap": ("Microscópio", "14h30–15h30", "O horário cruza uma reserva existente."), "adjacent": ("Microscópio", "15h00–16h00", "Começa no instante em que a reserva anterior termina."), "preparation": ("Microscópio", "15h05–16h05", "Há cinco minutos livres. A técnica precisa de dez."), "other": ("Centrífuga", "14h00–15h00", "Outro equipamento pode ter uma reserva no mesmo horário.")}
    $ demo_subtitle = "Revisão 2 em verificação · a versão anterior continua em uso." if lab_delivery == "revision_pending" else "Protótipo de investigação · compare os resultados com as necessidades observadas." if lab_commitment == "investigar_agora" and lab_delivery == "not_delivered" else "Revisão " + str(lab_revision) + " · compare o pacote com as necessidades antes de confirmar o uso."
    use lab_workspace("Demonstração da agenda", demo_subtitle):
        viewport:
            id "lab_calendar_scroll"
            ysize 650
            mousewheel True draggable True arrowkeys True pagekeys True
            scrollbars "vertical"
            frame:
                style "artifact_paper" xsize 1730
                vbox:
                    spacing 20
                    use artifact_bar("Agenda do laboratório", "Reservas / Revisão " + str(lab_revision) + " / Ambiente de demonstração")
                    hbox:
                        spacing 28
                        vbox:
                            xsize 960 spacing 18
                            text "Agenda · reservas" style "artifact_heading" size 34
                            if "clarity" in lab_plan:
                                frame:
                                    style "artifact_card" xsize 960
                                    vbox:
                                        spacing 14
                                        text "Consulta unificada" style "artifact_heading" size 28
                                        hbox:
                                            spacing 24
                                            vbox:
                                                xsize 420 spacing 8
                                                text "Reserva anterior · Ana" style "artifact_muted" size 26
                                                text "Microscópio · 14h00–15h00" style "artifact_ink" size lab_ui_size(26)
                                            vbox:
                                                xsize 420 spacing 8
                                                text "Tentativa de reserva" style "artifact_muted" size 26
                                                text ((case_details[selected_case][0] + " · " + case_details[selected_case][1]) if selected_case else "Escolha um caso de teste") style "artifact_ink" size lab_ui_size(26)
                            else:
                                text "Consulta por registros" style "artifact_heading" size 28
                                textbutton "Consultar reserva anterior":
                                    style "artifact_button" text_size 28
                                    action Show("lab_reservation_reference")
                                    id "lab_existing_open"
                                text "Equipamento e horário anteriores ficam no registro separado. O calendário legível reuniria as duas consultas." style "artifact_muted" size lab_ui_size(25)
                            fixed:
                                xsize 960 ysize 245
                                add Solid("#ffffff")
                                for index, hour in enumerate(("14h00", "14h30", "15h00", "15h30", "16h00", "16h30")):
                                    text hour xpos (22 + index * 155) ypos 16 color "#52656b" size 24
                                    add Solid("#d5dddb") xpos (22 + index * 155) ypos 55 xsize 2 ysize 170
                                if "clarity" in lab_plan:
                                    frame:
                                        background Solid("#d1e8e1") padding (14, 12)
                                        xpos 24 ypos 66 xsize 320 ysize 68
                                        text "Ana · reserva mantida" size 25 color "#163b3f"
                                if selected_case:
                                    frame:
                                        background Solid("#f3ddb8") padding (14, 12)
                                        xpos (24 + int((LAB_CASES[selected_case]["candidate"][1] - 840) * 310 / 60)) ypos 146 xsize 320 ysize 70
                                        text ("Tentativa · " + ("centrífuga" if selected_case == "other" else case_details[selected_case][1])) size 24 color "#5c411d"
                            if selected_case:
                                text case_details[selected_case][2] style "artifact_muted" size lab_ui_size(26)
                                if selected_case in lab_test_results:
                                    text lab_ui_result(lab_test_results[selected_case]) style "artifact_heading" size 32 color "#286b66" id "lab_test_result" at (lab_result_enter if _preferences.transitions else lab_result_still)
                            else:
                                text "Escolha um caso ao lado. O resultado ficará registrado na pasta." style "artifact_muted" size lab_ui_size(27)
                        vbox:
                            spacing 16 xsize 680
                            text "Casos de teste" style "artifact_heading" size 34
                            text "EQUIPAMENTO / HORÁRIO / RESULTADO" style "artifact_muted" size 23
                            for case_id in ("overlap", "adjacent", "preparation", "other"):
                                button:
                                    style "artifact_button" xfill True
                                    selected_background Solid("#b9d8d2")
                                    selected selected_case == case_id
                                    action [SetScreenVariable("selected_case", case_id), Function(lab_ui_apply, lab_run_test, case_id)]
                                    id ("lab_test_" + case_id)
                                    vbox:
                                        spacing 8
                                        text LAB_CASES[case_id]["title"] style "artifact_ink" size lab_ui_size(28)
                                        text (case_details[case_id][0] + " · " + case_details[case_id][1]) style "artifact_muted" size 25
                                        if case_id in lab_test_results:
                                            text lab_ui_result(lab_test_results[case_id]) style "artifact_ink" size 24
                            text "Um resultado aceito pode revelar uma regra ausente. A implementação só muda após uma decisão da equipe." style "artifact_note" size lab_ui_size(25)
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
    default journal_section = "sources"
    key "game_menu" action Hide("lab_journal")
    key "K_n" action Hide("lab_journal")
    add Solid("#08151df5")
    frame:
        style "lab_panel"
        xpos 150 ypos 70 xsize 1620 ysize 940
        vbox:
            spacing 16
            hbox:
                spacing 40
                text "Pasta de trabalho" style "rw_heading" size 44 xsize 1070
                textbutton "Fechar · N / Esc" style "lab_button" text_size 27 action Hide("lab_journal") default_focus True id "lab_journal_close"
            text (lab_ui_phase() + " · " + lab_objective()) style "lab_note" size 27
            hbox:
                spacing 12
                for section, caption in (("sources", "Fontes"), ("project", "Projeto"), ("commitments", "Compromissos")):
                    textbutton caption:
                        style "artifact_button" text_size 27 xsize 300
                        selected journal_section == section
                        action SetScreenVariable("journal_section", section)
                        id ("lab_journal_tab_" + section)
            frame:
                style "artifact_paper" xfill True ysize 600
                viewport:
                    id "lab_journal_scroll"
                    xfill True ysize 560
                    mousewheel True draggable True arrowkeys True pagekeys True
                    scrollbars "vertical"
                    vbox:
                        spacing 18 xsize 1460
                        if journal_section == "sources":
                            use artifact_bar("Fontes da investigação", "Registros consultados · laboratório")
                            if not lab_evidence:
                                text "Nenhuma fonte registrada. Visite a bancada e converse com Carlos." style "artifact_muted" size 28
                            for eid in lab_evidence:
                                frame:
                                    style "artifact_card" xfill True
                                    vbox:
                                        spacing 10
                                        text ("ID DA FONTE · " + eid.upper()) style "artifact_muted" size 22
                                        text LAB_EVIDENCE[eid]["title"] style "artifact_heading" size 30
                                        text LAB_EVIDENCE[eid]["source"] style "artifact_muted" size 25
                                        text LAB_EVIDENCE[eid]["text"] style "artifact_ink" size lab_ui_size(28)
                        elif journal_section == "project":
                            use artifact_bar("Projeto do laboratório", "Revisão " + str(lab_revision) + " · escopo, fontes e registros de ensaio")
                            if lab_initial_plan:
                                text ("Plano inicial: " + ", ".join(LAB_ITEMS[i]["title"] for i in lab_initial_plan)) style "artifact_ink" size lab_ui_size(28)
                            else:
                                text ("Plano em discussão: " + (", ".join(LAB_ITEMS[i]["title"] for i in lab_plan) or "ainda não definido")) style "artifact_ink" size lab_ui_size(28)
                            if lab_repaired:
                                text ("Revisão 2 · nova rodada: " + ", ".join(LAB_ITEMS[i]["title"] for i in lab_plan)) style "artifact_note" size lab_ui_size(28)
                            text ("Entrega: " + ("revisão 2 em verificação; versão anterior em uso" if lab_delivery == "revision_pending" else "adiada · investigação em andamento" if lab_commitment == "investigar_agora" and lab_delivery == "not_delivered" else "ainda não realizada" if lab_delivery == "not_delivered" else "revisão reparada entregue" if lab_delivery == "repaired" else "pacote confirmado na bancada")) style "artifact_ink" size lab_ui_size(28)
                            if not lab_links and not lab_plan:
                                text "Nenhum vínculo ou item de escopo registrado. A pasta mostra as decisões à medida que forem tomadas." style "artifact_muted" size 27
                            for item_id, item in LAB_ITEMS.items():
                                if item_id in lab_links or item_id in lab_plan:
                                    frame:
                                        style "artifact_card" xfill True
                                        vbox:
                                            spacing 10
                                            text ("ID DO REQUISITO · " + item_id.upper()) style "artifact_muted" size 22
                                            text item["title"] style "artifact_heading" size 30
                                            text ("Critério do item: " + item["description"]) style "artifact_ink" size lab_ui_size(27)
                                            text ("No plano atual" if item_id in lab_plan else "Fora do plano atual") style "artifact_note" size 25
                                            if item_id in lab_links:
                                                $ source_id = lab_links[item_id]
                                                $ supported = source_id == {"conflict": "sheets", "preparation": "preparation", "clarity": "interview"}[item_id]
                                                text (("Fonte confirmada: " if supported else "Hipótese a revisar: ") + LAB_EVIDENCE[source_id]["title"]) style "artifact_muted" size 25
                                                text LAB_EVIDENCE[source_id]["source"] style "artifact_muted" size 24
                                            else:
                                                text "Fonte ainda não vinculada." style "artifact_muted" size 25
                            text "Registros de ensaio" style "artifact_heading" size 30
                            if not lab_test_results:
                                text "Nenhum resultado registrado para a versão atual. A pasta não executa nem aprova testes." style "artifact_muted" size 27
                            for case_id, result in lab_test_results.items():
                                frame:
                                    style "artifact_card" xfill True
                                    vbox:
                                        spacing 8
                                        text ("CASO · " + case_id.upper()) style "artifact_muted" size 22
                                        text LAB_CASES[case_id]["title"] style "artifact_ink" size lab_ui_size(27)
                                        text ("Resultado observado: " + lab_ui_result(result)) style "artifact_note" size lab_ui_size(26)
                        else:
                            use artifact_bar("Acordo com a equipe", "Prioridade, responsáveis e próximo retorno")
                            text ("Acordo: " + {"base_primeiro": "Entregar a base antes da integração", "investigar_agora": "Investigar integração nesta semana", "": "ainda não combinado"}.get(lab_commitment, lab_commitment)) style "artifact_heading" size 31
                            frame:
                                style "artifact_card" xfill True
                                vbox:
                                    spacing 16
                                    if lab_commitment:
                                        text ("Responsáveis: " + lab_commitment_owner) style "artifact_ink" size lab_ui_size(28)
                                        text ("Marco de retorno: " + lab_return_milestone) style "artifact_ink" size lab_ui_size(28)
                                    else:
                                        text "Responsáveis e retorno serão combinados com a equipe." style "artifact_muted" size lab_ui_size(28)
                                    text ("Situação: " + {"open": "em aberto", "fulfilled": "cumprido", "pending": "pendente", "revised": "revisado", "renegotiated": "renegociado"}.get(lab_commitment_status, lab_commitment_status)) style "artifact_note" size 27
                            if lab_repaired:
                                text "Reparação registrada. Evidências e acordo anteriores foram preservados." style "artifact_note" size 27
            text "Consulta somente. A pasta não altera o plano. Role com mouse, setas ou Page Up / Page Down." style "lab_note" size 24

screen lab_hud():
    zorder 20
    if lab_active:
        key "K_n" action Show("lab_journal")
        if campaign_active:
            key "K_i" action Show("campaign_bag")
        frame:
            background Solid("#142b38f5")
            xpos 30 ypos 20 xsize 1860
            padding (24, 15)
            hbox:
                spacing 18
                vbox:
                    spacing 7 xsize (1230 if campaign_active else 1400)
                    text (lab_ui_phase() + " · " + campaign_clock_caption()) color "#e7b565" size 23
                    text lab_objective() style "lab_body" size lab_ui_size(27) xmaximum (1220 if campaign_active else 1390)
                textbutton "Pasta de trabalho · N" style "lab_button" text_size 26 xsize 320 action Show("lab_journal") yalign 0.5 id "lab_journal_open"
                if campaign_active:
                    textbutton "Mochila · I" style "lab_button" text_size 26 xsize 225 action Show("campaign_bag") yalign 0.5 id "lab_bag_open"

screen lab_final(ending):
    modal True
    zorder 40
    $ final_text = {"reliable": ("Uma agenda em que a equipe confia", "A entrega protege os conflitos e o preparo do microscópio. A equipe pode trabalhar com uma regra que corresponde às fontes.", "Mantenham o retorno combinado para acompanhar a adoção e decidir os próximos passos."), "waiting": ("Uma resposta ainda em construção", "A semana foi usada para investigar. A integração não foi entregue, e a equipe ainda aguarda a próxima decisão.", "Retomem a proteção das reservas e transformem a pesquisa em um novo acordo com prazo e responsáveis."), "repaired": ("A confiança também se repara", "A equipe reconheceu a lacuna e revisou a agenda. A nova versão protege o conflito e o preparo sem apagar o acordo anterior.", "Acompanhem o uso da versão corrigida e confirmem se a rotina da técnica foi atendida."), "unowned": ("O risco precisa de um responsável", "A versão entregue deixou uma proteção de fora. O problema veio do escopo implementado, e não do ato de testá-lo.", "Uma correção precisa de responsável, retorno e uma regra confirmada pela fonte.")}.get(ending)
    use lab_workspace("O retorno da equipe", "O resultado acompanha o que foi investigado, planejado e combinado."):
        hbox:
            spacing 30
            frame:
                style "artifact_paper" xsize 1090 ysize 644
                viewport:
                    ysize 600 xfill True mousewheel True draggable True arrowkeys True pagekeys True scrollbars "vertical"
                    vbox:
                        xsize 1000 spacing 24
                        use artifact_bar("Relatório de retorno · laboratório", "Revisão " + str(lab_revision) + " · resultado e próximo cuidado")
                        text final_text[0] style "artifact_heading" size 42 xmaximum 1000
                        text final_text[1] style "artifact_ink" size lab_ui_size(31) xmaximum 1000
                        frame:
                            style "artifact_card" xfill True
                            vbox:
                                spacing 14
                                text "O próximo cuidado" style "artifact_heading" size 31 id "lab_final_care"
                                text final_text[2] style "artifact_ink" size lab_ui_size(28)
                        text "Sua pasta continua disponível para comparar as decisões desta campanha." style "artifact_muted" size 27
            frame:
                style "artifact_paper" xsize 590 ysize 644
                viewport:
                    ysize 600 xfill True mousewheel True draggable True arrowkeys True pagekeys True scrollbars "vertical"
                    vbox:
                        xsize 510 spacing 18
                        use artifact_bar("Registro da rodada", "Fontes, ensaios e versão")
                        text (str(len(lab_evidence)) + " fontes registradas") style "artifact_ink" size 28
                        text (str(len(lab_test_results)) + " casos experimentados") style "artifact_ink" size 28
                        text ("Versão " + str(lab_revision) + (" · revisão em verificação" if lab_delivery == "revision_pending" else " · investigação, sem entrega" if lab_delivery == "not_delivered" else " · reparação entregue" if lab_delivery == "repaired" else " · entrega inicial")) style "artifact_note" size 28
                        textbutton "Jogar a campanha novamente" style "artifact_primary" text_size 26 xfill True action Return("replay") id "lab_final_replay"
                        if campaign_active:
                            textbutton "Voltar à mesa da equipe" style "artifact_primary" text_size 26 xfill True action Return("hub") id "lab_final_hub"
                        textbutton "Voltar ao menu" style "artifact_button" text_size 27 xfill True action Return("menu") id "lab_final_menu"
                        textbutton "Conhecer a jornada guiada" style "artifact_button" text_size 26 xfill True action Return("legacy") id "lab_final_legacy"
