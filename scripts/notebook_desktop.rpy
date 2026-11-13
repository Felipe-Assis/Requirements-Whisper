default notebook_read = []

init python:
    import hashlib
    import json

    NOTEBOOK_SENDERS = {"lab": "Sabrina", "expenses": "Lia", "tickets": "Rodrigo"}
    NOTEBOOK_DEMANDS = {
        "lab": "Duas equipes receberam confirmação para usar o mesmo microscópio. Compare as reservas e converse com a bancada antes de propor as regras da agenda.",
        "expenses": "A lista de gastos parece repetir um almoço. Quero conferir os lançamentos com você. Antes de apagar, confirme qual registro deve sair e o que acontece se eu cancelar.",
        "tickets": "O suporte vê Resolvido, mas a solicitante ainda vê Em atendimento. Confira o registro e a resposta que chega para ela; precisamos entender onde os dois lados se separaram.",
    }

    def notebook_message_key(prefix, payload):
        content = json.dumps(payload, ensure_ascii=False, sort_keys=True)
        return prefix + "_" + hashlib.sha256(content.encode("utf-8")).hexdigest()[:16]

    def notebook_started_projects():
        return set(getattr(store, "campaign_started_projects", [])) | set(getattr(store, "campaign_results", {}))

    def notebook_messages():
        messages = []
        started = notebook_started_projects()
        for project_id, project in CAMPAIGN_PROJECTS.items():
            sender = NOTEBOOK_SENDERS[project_id]
            messages.append({"id": "invite_" + project_id, "sender": sender, "subject": "Convite · " + project["title"], "body": project["challenge"] + "\n\nO pedido está na mesa da equipe. Você pode escolher por qual projeto começar.", "project": project_id, "kind": "invite"})
            if project_id in started:
                messages.append({"id": "demand_" + project_id, "sender": sender, "subject": "Demanda · " + project["title"], "body": NOTEBOOK_DEMANDS[project_id], "project": project_id, "kind": "demand"})
            result = getattr(store, "campaign_results", {}).get(project_id)
            if result:
                payload = {key: result.get(key, "") for key in ("outcome", "summary", "pending")}
                body = "Resultado registrado\n" + payload["summary"] + "\n\nPróximo passo\n" + (payload["pending"] or "Ainda sem próximo passo registrado.")
                clock = result.get("clock", {})
                milestone = " · ".join(str(clock[key]) for key in ("day", "time") if clock.get(key))
                if milestone:
                    body += "\n\nMarco do retorno: " + milestone
                messages.append({"id": notebook_message_key("return_" + project_id, payload), "sender": sender, "subject": "Retorno · " + project["title"], "body": body, "project": project_id, "kind": "return"})
        agreement = getattr(store, "student_agreement", "")
        if agreement:
            pending = getattr(store, "student_agreed_schedule", {}) != getattr(store, "student_schedule", {})
            body = agreement
            if pending:
                body += "\n\nA agenda mudou depois desta conversa. Retome o acordo comigo para atualizar a combinação."
            messages.append({"id": notebook_message_key("agreement", {"text": agreement, "pending": pending}), "sender": "Sabrina", "subject": "Nossa combinação para a semana", "body": body, "project": "student", "kind": "agreement"})
        selected = getattr(store, "ticket_selected", "")
        history = getattr(store, "ticket_records", {}).get(selected, {}).get("history", [])
        if "tickets" in started and "log" in getattr(store, "ticket_evidence", []) and history:
            messages.append({"id": notebook_message_key("history_tickets_" + selected, list(history)), "sender": "Rodrigo · atendimento", "subject": "Registro do chamado #" + selected, "body": "Histórico do atendimento\n\n" + "\n\n".join(history), "project": "tickets", "kind": "history"})
        return messages

    def notebook_mark_read(message_id):
        if not any(message["id"] == message_id for message in notebook_messages()):
            return False
        if message_id not in store.notebook_read:
            store.notebook_read = store.notebook_read + [message_id]
        return True

screen campaign_bag():
    modal True
    zorder 125
    key "game_menu" action Hide("campaign_bag")
    add Solid("#06121ae8")
    frame:
        style "artifact_paper"
        align (0.5, 0.5) xsize 1660 ysize 930
        vbox:
            spacing 22
            hbox:
                spacing 24
                text "Minha mochila" style "artifact_heading" size 40 xsize 1260
                textbutton "Fechar · Esc" style "artifact_button" text_size 26 action Hide("campaign_bag") id "campaign_bag_close"
            viewport:
                id "campaign_bag_scroll"
                ysize 770
                mousewheel True draggable True arrowkeys True pagekeys True scrollbars "vertical"
                hbox:
                    spacing 32
                    vbox:
                        xsize 730 spacing 16
                        add "images/items/mochila_com_notebook.png" xysize (700, 610) fit "contain"
                        text "Documentos e mensagens acompanham você entre os projetos." style "artifact_muted" size lab_ui_size(27)
                    vbox:
                        xsize 800 spacing 22
                        text "Notebook" style "artifact_heading" size 34
                        button:
                            style "artifact_button" xfill True
                            action [Hide("campaign_bag"), Show("campaign_desktop")]
                            id "campaign_bag_notebook"
                            vbox:
                                spacing 18
                                add "images/items/notebook_aberto.png" xysize (620, 420) fit "contain" xalign 0.5
                                text "Abrir notebook" style "artifact_button_text" size 32
                        text item_data["notebook"]["desc"] style "artifact_ink" size lab_ui_size(28)
                        text "Consulte os documentos do projeto ou leia a caixa de entrada." style "artifact_muted" size lab_ui_size(27)

screen campaign_desktop():
    modal True
    zorder 130
    default notebook_tab = "documents"
    default notebook_selected = None
    $ notebook_mail = notebook_messages()
    $ notebook_unread = sum(message["id"] not in notebook_read for message in notebook_mail)
    key "game_menu" action Hide("campaign_desktop")
    add Solid("#06121ae8")
    frame:
        style "artifact_paper"
        align (0.5, 0.5) xsize 1760 ysize 960
        vbox:
            spacing 18
            hbox:
                spacing 20
                fixed:
                    xsize 1160 ysize 60
                    text "Notebook" style "artifact_heading" size 38 yalign 0.5
                textbutton "Mochila" style "artifact_button" text_size 26 action [Hide("campaign_desktop"), Show("campaign_bag")] id "notebook_bag"
                textbutton "Fechar · Esc" style "artifact_button" text_size 26 action Hide("campaign_desktop") id "notebook_close"
            hbox:
                spacing 16
                textbutton "Documentos" style "artifact_button" text_size 28 selected notebook_tab == "documents" action [SetScreenVariable("notebook_tab", "documents"), SetScreenVariable("notebook_selected", None)] id "notebook_tab_documents"
                textbutton ("Caixa de entrada · " + str(notebook_unread) + " não lidas") style "artifact_button" text_size 28 selected notebook_tab == "inbox" action [SetScreenVariable("notebook_tab", "inbox"), SetScreenVariable("notebook_selected", None)] id "notebook_tab_inbox"
            if notebook_tab == "inbox" and notebook_selected:
                textbutton "Voltar à caixa de entrada" style "artifact_button" text_size 26 action SetScreenVariable("notebook_selected", None) id "notebook_inbox_back"
            viewport:
                id "notebook_content_scroll"
                ysize 680
                mousewheel True draggable True arrowkeys True pagekeys True scrollbars "vertical"
                vbox:
                    spacing 20 xsize 1650
                    if notebook_tab == "documents":
                        use artifact_bar("Documentos", "Dossiês dos projetos e registros de trabalho")
                        frame:
                            style "artifact_card" xfill True
                            vbox:
                                spacing 18
                                text "Dossiê dos projetos" style "artifact_heading" size 32
                                text "Compare escopo, resultado e próximo passo dos retornos arquivados." style "artifact_ink" size lab_ui_size(28)
                                textbutton "Abrir dossiê" style "artifact_button" text_size 28 action Show("campaign_journal") id "notebook_document_campaign"
                        frame:
                            style "artifact_card" xfill True
                            vbox:
                                spacing 18
                                text "Laboratório · fontes e plano atual" style "artifact_heading" size 32
                                text ("Evidências consultadas, regras escolhidas, acordo e testes desta rodada." if lab_active else "Disponível durante o caso do laboratório.") style "artifact_muted" size lab_ui_size(28)
                                textbutton "Abrir registros do laboratório" style "artifact_button" text_size 28 sensitive lab_active action Show("lab_journal") id "notebook_document_lab"
                    elif notebook_selected:
                        $ notebook_message = next((message for message in notebook_mail if message["id"] == notebook_selected), None)
                        if notebook_message:
                            use artifact_bar(notebook_message["subject"], "De: " + notebook_message["sender"])
                            frame:
                                style "artifact_card" xfill True
                                text notebook_message["body"].replace("{", "{{") substitute False style "artifact_ink" size lab_ui_size(29) xmaximum 1550 id "notebook_message_body"
                        else:
                            text "O registro mudou. Volte à caixa de entrada para consultar a versão atual." style "artifact_muted" size lab_ui_size(28)
                    else:
                        use artifact_bar("Caixa de entrada", "Convites, demandas e retornos da equipe")
                        frame:
                            background None padding (18, 0)
                            hbox:
                                spacing 22
                                fixed:
                                    xsize 322 ysize 35
                                    text "REMETENTE" style "artifact_muted" size 23
                                fixed:
                                    xsize 992 ysize 35
                                    text "ASSUNTO" style "artifact_muted" size 23
                                text "LEITURA" style "artifact_muted" size 23
                        for message in notebook_mail:
                            button:
                                style "artifact_button" xfill True
                                action [SetScreenVariable("notebook_selected", message["id"]), Function(lab_ui_apply, notebook_mark_read, message["id"])]
                                id ("notebook_message_" + message["id"])
                                hbox:
                                    spacing 22
                                    fixed:
                                        xsize 322 ysize 74
                                        text message["sender"] style "artifact_button_text" size lab_ui_size(26) xmaximum 322 yalign 0.5
                                    fixed:
                                        xsize 992 ysize 74
                                        text message["subject"] style "artifact_button_text" size lab_ui_size(26) xmaximum 992 yalign 0.5
                                    text ("Lida" if message["id"] in notebook_read else "Não lida") style "artifact_button_text" size 25 yalign 0.5
