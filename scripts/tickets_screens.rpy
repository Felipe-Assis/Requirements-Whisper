screen ticket_investigation():
    zorder 40
    modal True
    use campaign_workspace("Resolvido para quem?", "Suporte · compare o registro interno com o que a pessoa consegue consultar."):
        hbox:
            spacing 30
            frame:
                style "artifact_paper"
                xsize 540 ysize 644
                viewport:
                    xfill True ysize 600
                    mousewheel True draggable True arrowkeys True pagekeys True
                    scrollbars "vertical"
                    vbox:
                        spacing 16
                        xsize 460
                        use artifact_bar("Atendimento", "Caixa de entrada · fontes do chamado")
                        for source_id in ("panel", "message", "log", "shift"):
                            $ source = TICKET_SOURCES[source_id]
                            textbutton (("Lida · " if source_id in ticket_evidence else "Ler · ") + source["title"]):
                                style "artifact_button" text_size lab_ui_size(26) xfill True
                                action Function(lab_ui_apply, ticket_collect, source_id)
                                id ("ticket_source_" + source_id)
            frame:
                style "artifact_paper"
                xsize 1200 ysize 644
                viewport:
                    xfill True ysize 600
                    mousewheel True draggable True arrowkeys True pagekeys True
                    scrollbars "vertical"
                    vbox:
                        spacing 22
                        xsize 1100
                        if ticket_source:
                            $ source = TICKET_SOURCES[ticket_source]
                            use artifact_bar(source["title"], "Chamado #241 · registro consultável")
                            text source["source"] style "artifact_muted" size 26
                            text source["text"] style "artifact_ink" size lab_ui_size(30)
                        else:
                            text "O suporte encerrou. Ana ligou de novo." style "artifact_heading" size 38
                            text "Não basta encontrar a palavra Resolvido no painel. Abra as fontes e confira o que cada pessoa recebeu." style "artifact_ink" size lab_ui_size(30)
                        text (str(sum(source in ticket_evidence for source in ("panel", "message", "log"))) + "/3 fontes essenciais registradas") color "#286b66" size 28
                        text "O registro de turno é opcional. Você pode voltar às fontes antes de seguir." style "artifact_muted" size 26
    use campaign_footer(ticket_feedback)
    use lab_continue("Abrir a fila de chamados", Return(True), ticket_sources_ready(), "ticket_investigation_continue")


screen ticket_triage():
    zorder 40
    modal True
    use campaign_workspace("Quem espera primeiro?", "Uma validação nesta rodada. Os outros chamados continuam abertos, com o impacto registrado."):
        frame:
            style "artifact_paper" xfill True ysize 644
            vbox:
                spacing 16
                use artifact_bar("Central de atendimento · fila aberta", "Três chamados · uma prioridade para esta rodada")
                hbox:
                    spacing 16
                    text "ID" style "artifact_muted" size 22 xsize 88
                    text "CHAMADO / PESSOA" style "artifact_muted" size 22 xsize 420
                    text "IMPACTO INFORMADO" style "artifact_muted" size 22 xsize 580
                    text "SITUAÇÃO" style "artifact_muted" size 22 xsize 190
                    text "PRIORIDADE" style "artifact_muted" size 22 xsize 260
                viewport:
                    ysize 460 xfill True mousewheel True draggable True arrowkeys True pagekeys True scrollbars "vertical"
                    vbox:
                        spacing 12
                        for ticket_id in ("241", "242", "243"):
                            $ case = TICKET_CASES[ticket_id]
                            frame:
                                style "artifact_card" xfill True
                                hbox:
                                    spacing 16
                                    text ("#" + ticket_id) style "artifact_heading" size 28 xsize 88
                                    vbox:
                                        spacing 12 xsize 420
                                        text case["title"] style "artifact_heading" size 28
                                        text case["requester"] style "artifact_muted" size 24
                                    text case["impact"] style "artifact_ink" size lab_ui_size(26) xsize 580
                                    text "Em atendimento" style "artifact_muted" size 25 xsize 190
                                    textbutton ("Selecionado nesta rodada" if ticket_prioritized and ticket_selected == ticket_id else "Atender primeiro"):
                                        style "artifact_button" text_size 25 xsize 260
                                        action Function(lab_ui_apply, ticket_prioritize, ticket_id)
                                        selected ticket_prioritized and ticket_selected == ticket_id
                                        id ("ticket_priority_" + ticket_id)
    use campaign_footer(ticket_feedback)
    use lab_continue("Validar o chamado escolhido", Return(True), ticket_prioritized, "ticket_triage_continue")

# PageDown fica no painel de ações; viewports irmãos consomem a tecla mesmo sem foco.
screen ticket_perspectives(records):
    $ record = records[ticket_selected]
    hbox:
        spacing 20
        frame:
            style "artifact_paper"
            xsize 582 ysize 644
            viewport:
                mousewheel True draggable True arrowkeys False pagekeys False
                scrollbars "vertical"
                vbox:
                    spacing 16
                    xsize 510
                    use artifact_bar("Central de atendimento", "#" + ticket_selected + " · visão interna")
                    text record["internal_status"] style "artifact_heading" size 34 id "ticket_internal_status"
                    text "Nota restrita ao suporte" style "artifact_muted" size 24
                    frame:
                        style "artifact_card" xfill True
                        text record["internal_note"] style "artifact_ink" size lab_ui_size(25) xmaximum 470
                    text "Histórico preservado" style "artifact_heading" size 28
                    for index, event in enumerate(record["history"]):
                        frame:
                            style "artifact_card" xfill True
                            text event.replace("{", "{{") substitute False style "artifact_muted" size lab_ui_size(24) xmaximum 470 id ("ticket_history_" + str(index))
        frame:
            style "artifact_paper"
            xsize 582 ysize 644
            viewport:
                mousewheel True draggable True arrowkeys False pagekeys False
                scrollbars "vertical"
                vbox:
                    spacing 16
                    xsize 510
                    use artifact_bar("Portal da solicitante", "#" + ticket_selected + " · consulta pública")
                    text TICKET_CASES[ticket_selected]["requester"] style "artifact_muted" size 25
                    text record["public_status"] style "artifact_heading" size 34 id "ticket_public_status"
                    text "Solução publicada" style "artifact_muted" size 24
                    frame:
                        style "artifact_card" xfill True
                        text (record["public_solution"] or "Nenhuma solução publicada. A pessoa ainda precisa perguntar ao suporte.") style "artifact_ink" size lab_ui_size(27) xmaximum 470 id "ticket_public_solution"

screen ticket_workbench():
    zorder 40
    modal True
    use campaign_workspace("Duas telas, uma transição", "Protótipo · cada caso parte de uma cópia nova. Os testes não publicam na fila de atendimento."):
        hbox:
            spacing 24
            frame:
                style "artifact_paper"
                xsize 560 ysize 644
                viewport:
                    xfill True ysize 600
                    mousewheel True draggable True arrowkeys True pagekeys True
                    scrollbars "vertical"
                    id "ticket_workbench_scroll"
                    vbox:
                        spacing 14
                        xsize 486
                        use artifact_bar("Bancada de revisão", "#" + ticket_selected + " · " + TICKET_CASES[ticket_selected]["title"])
                        text ("Exibindo: versão anterior" if ticket_demo_version == "old" else "Exibindo: nova versão de teste") color "#286b66" size 24
                        textbutton "1 · Reproduzir na versão anterior":
                            style "artifact_button" text_size 26 xfill True
                            action Function(lab_ui_apply, ticket_demo, "old", "resolved")
                            id "ticket_demo_old"
                        if ticket_reproduced:
                            text "2 · Escolha o que Júlio altera" style "artifact_ink" size 26
                            for patch in ("internal", "atomic", "broadcast"):
                                textbutton TICKET_PATCHES[patch]:
                                    style "artifact_button" text_size 25 xfill True
                                    selected ticket_patch == patch
                                    action Function(lab_ui_apply, ticket_choose_patch, patch)
                                    id ("ticket_patch_" + patch)
                        if ticket_patch:
                            text "3 · Execute a nova versão" style "artifact_ink" size 26
                            for case in ("resolved", "empty", "other"):
                                textbutton TICKET_TEST_LABELS[case]:
                                    style "artifact_button" text_size 25 xfill True ysize 90
                                    action Function(lab_ui_apply, ticket_demo, "new", case)
                                    id ("ticket_test_" + case)
                                text ("Ainda não testado" if case not in ticket_tests else ("Passou" if ticket_tests[case] == {"resolved": "published", "empty": "blocked", "other": "isolated"}[case] else "Revisar o resultado")) style "artifact_muted" size 23 ysize 30
            use ticket_perspectives(ticket_demo_records)
    use campaign_footer(ticket_feedback)
    use lab_continue("Combinar a publicação", Return(True), ticket_tests_ready(), "ticket_workbench_continue")


screen ticket_delivery():
    zorder 40
    modal True
    use campaign_workspace("Publicar também é um acordo", "Escolha uma orientação pública, quando ela será publicada e quem assume o próximo passo."):
        hbox:
            spacing 24
            frame:
                style "artifact_paper"
                xsize 578 ysize 644
                viewport:
                    xfill True ysize 600
                    mousewheel True draggable True arrowkeys True pagekeys True
                    scrollbars "vertical"
                    vbox:
                        spacing 16
                        xsize 490
                        text "1 · Solução pública" style "artifact_heading" size 32
                        text TICKET_CASES[ticket_selected]["public"] style "artifact_ink" size lab_ui_size(26)
                        textbutton "Usar esta orientação para a pessoa":
                            style "artifact_button" text_size 26 xfill True
                            selected ticket_draft == TICKET_CASES[ticket_selected]["public"]
                            action Function(lab_ui_apply, ticket_choose_solution, "public")
                            id "ticket_solution_public"
                        textbutton "Copiar a nota interna":
                            style "artifact_button" text_size 26 xfill True
                            action Function(lab_ui_apply, ticket_choose_solution, "internal")
                            id "ticket_solution_internal"
                        textbutton "Deixar a solução vazia":
                            style "artifact_button" text_size 26 xfill True
                            action Function(lab_ui_apply, ticket_choose_solution, "empty")
                            id "ticket_solution_empty"
            frame:
                style "artifact_paper"
                xsize 578 ysize 644
                viewport:
                    xfill True ysize 600
                    mousewheel True draggable True arrowkeys True pagekeys True
                    scrollbars "vertical"
                    vbox:
                        spacing 18
                        xsize 490
                        text "2 · Política de publicação" style "artifact_heading" size 32
                        textbutton "Revisão por colega antes de publicar":
                            style "artifact_button" text_size 27 xfill True
                            selected ticket_policy == "peer_review"
                            action Function(lab_ui_apply, ticket_set_policy, "peer_review")
                            id "ticket_policy_review"
                        text "A pessoa espera a revisão. A nota técnica continua interna; estado e solução são publicados juntos depois da conferência." style "artifact_muted" size lab_ui_size(25)
                        textbutton "Publicar e acompanhar reaberturas":
                            style "artifact_button" text_size 27 xfill True
                            selected ticket_policy == "publish_followup"
                            action Function(lab_ui_apply, ticket_set_policy, "publish_followup")
                            id "ticket_policy_followup"
                        text "A pessoa recebe agora. A equipe combina quem confere o uso, recebe um motivo de reabertura e mantém o histórico." style "artifact_muted" size lab_ui_size(25)
            frame:
                style "artifact_paper"
                xsize 578 ysize 644
                viewport:
                    xfill True ysize 600
                    mousewheel True draggable True arrowkeys True pagekeys True
                    scrollbars "vertical"
                    vbox:
                        spacing 16
                        xsize 490
                        text "3 · Passagem de turno" style "artifact_heading" size 32
                        if "shift" in ticket_evidence:
                            text "Escala consultada: Rodrigo sai hoje. Sabrina está disponível na terça-feira às 09h." style "artifact_muted" size lab_ui_size(25)
                        else:
                            textbutton "Conferir a escala de terça-feira":
                                style "artifact_button" text_size 26 xfill True
                                action Function(lab_ui_apply, ticket_collect, "shift")
                                id "ticket_delivery_shift"
                        textbutton "Deixar com Rodrigo":
                            style "artifact_button" text_size 26 xfill True
                            sensitive "shift" not in ticket_evidence
                            action Function(lab_ui_apply, ticket_handoff, "rodrigo")
                            id "ticket_owner_rodrigo"
                        textbutton "Combinar com Sabrina às 09h":
                            style "artifact_button" text_size 26 xfill True
                            selected ticket_owner == "Sabrina"
                            action Function(lab_ui_apply, ticket_handoff, "sabrina")
                            id "ticket_owner_sabrina"
                        textbutton "Repassar para a equipe":
                            style "artifact_button" text_size 26 xfill True
                            action Function(lab_ui_apply, ticket_handoff, "team")
                            id "ticket_owner_team"
                        text (ticket_next_step or "Responsável e próximo passo ainda não confirmados.") style "artifact_ink" size lab_ui_size(25)
                        if ticket_draft and ticket_draft != TICKET_CASES[ticket_selected]["public"]:
                            text "A nota interna não orienta a pessoa e contém detalhes restritos." color "#8a5623" size 25
    use campaign_footer(ticket_feedback)
    use lab_continue("Registrar entrega; voltar terça às 09h", Return(True), bool(ticket_policy) and ticket_draft == TICKET_CASES[ticket_selected]["public"], "ticket_delivery_continue")


screen ticket_return():
    zorder 40
    modal True
    use campaign_workspace("No turno seguinte", "O retorno parte do que você registrou. Publicação, revisão e acompanhamento são estados diferentes."):
        hbox:
            spacing 24
            frame:
                style "artifact_paper"
                xsize 560 ysize 644
                viewport:
                    xfill True ysize 600
                    mousewheel True draggable True arrowkeys True pagekeys True
                    scrollbars "vertical"
                    id "ticket_return_scroll"
                    vbox:
                        spacing 16
                        xsize 486
                        text ticket_return_text() style "artifact_ink" size lab_ui_size(26)
                        if ticket_delivery == "not_delivered":
                            textbutton "Sabrina assume o próximo passo; recuperar repasse":
                                style "artifact_button" text_size 26 xfill True
                                action [Function(lab_ui_apply, ticket_handoff, "sabrina"), Function(lab_ui_apply, ticket_submit)]
                                id "ticket_recover"
                        if ticket_delivery == "review_pending":
                            textbutton "Revisar com Sabrina e publicar":
                                style "artifact_button" text_size 26 xfill True
                                action Function(lab_ui_apply, ticket_review)
                                id "ticket_review"
                        if ticket_records[ticket_selected]["public_status"] == "Resolvido":
                            textbutton ("Uso confirmado · registrado" if ticket_followup_status == "confirmed" else "Conferir o uso com a solicitante"):
                                style "artifact_button" text_size 26 xfill True
                                action Function(lab_ui_apply, ticket_followup, "confirm")
                                sensitive ticket_followup_status != "confirmed"
                                id "ticket_followup_confirm"
                            textbutton "Simular falha no turno da noite":
                                style "artifact_button" text_size 26 xfill True
                                action Function(lab_ui_apply, ticket_reopen_simulated_case)
                                id "ticket_reopen_known"
                            text ("Caso simulado: " + TICKET_CASES[ticket_selected]["reopen"]) style "artifact_muted" size 25
                            text "Outros motivos ficam registrados para Sabrina e Júlio investigarem." style "artifact_muted" size 25
                            frame:
                                background Solid("#ffffff")
                                padding (16, 12)
                                xsize 480
                                input value VariableInputValue("ticket_reopen_reason") length 160 style "input" size 26 color "#23343b" xmaximum 445 id "ticket_reopen_reason_input"
                            textbutton "Reabrir com o motivo registrado":
                                style "artifact_button" text_size 26 xfill True
                                action Function(lab_ui_apply, ticket_reopen, ticket_reopen_reason)
                                id "ticket_reopen"
                        if ticket_records[ticket_selected]["public_status"] == "Reaberto" and ticket_reopen_known_case:
                            textbutton "Sabrina e Júlio verificam o caso simulado":
                                style "artifact_button" text_size 26 xfill True
                                action Function(lab_ui_apply, ticket_followup, "repair")
                                id "ticket_followup_repair"
                        if ticket_records[ticket_selected]["public_status"] == "Reaberto" and not ticket_reopen_known_case:
                            text "Motivo livre registrado. Sabrina precisa investigar com Júlio; nenhuma correção foi presumida." style "artifact_ink" size 25
                        text "Você pode encerrar esta rodada com uma pendência explícita; ela continuará no registro da campanha." style "artifact_muted" size 24
            use ticket_perspectives(ticket_records)
    use campaign_footer(ticket_feedback)
    use lab_continue("Guardar o resultado desta rodada", Return(True), True, "ticket_return_continue")


screen ticket_final():
    zorder 40
    modal True
    $ summary = ticket_summary()
    use campaign_workspace("Registro de chamados", "O estado que chegou à pessoa e os compromissos que continuam abertos."):
        frame:
            style "artifact_paper" xfill True ysize 644
            viewport:
                mousewheel True draggable True arrowkeys True pagekeys True
                scrollbars "vertical"
                ysize 600
                vbox:
                    spacing 22
                    xmaximum 1700
                    text summary["summary"] style "artifact_heading" size 38
                    text summary["impact"] style "artifact_ink" size lab_ui_size(28)
                    text (summary["pending"] or "O próximo passo combinado foi realizado nesta simulação.") style "artifact_ink" size lab_ui_size(30)
                    text (summary["next_step"] or "Sem responsável confirmado.") style "artifact_muted" size 27
                    text "Histórico do chamado escolhido" color "#8a5623" size 28
                    for index, event in enumerate(summary["history"]):
                        text event.replace("{", "{{") substitute False style "artifact_muted" size lab_ui_size(25) id ("ticket_final_history_" + str(index))
    use campaign_footer("O registro preserva as pendências. O atendimento dos outros chamados ainda precisa ser combinado.")
    use lab_continue("Voltar aos projetos", Return(True), True, "ticket_final_hub")
