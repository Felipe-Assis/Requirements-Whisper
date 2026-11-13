testsuite literal_ticket_text:
    before testcase:
        if not screen "main_menu":
            run MainMenu(confirm=False)
        pause until screen "main_menu"

    after testcase:
        run Hide("campaign_desktop")

    testcase reopening_reason_stays_literal_in_history_and_mail:
        run Start("tickets_campaign")
        advance until screen "ticket_investigation"
        $ ticket_collect("panel")
        $ ticket_collect("message")
        $ ticket_collect("log")
        $ ticket_prioritize("241")
        $ ticket_demo("old", "resolved")
        $ ticket_choose_patch("atomic")
        $ ticket_demo("new", "resolved")
        $ ticket_demo("new", "empty")
        $ ticket_demo("new", "other")
        $ ticket_choose_solution("public")
        $ ticket_set_policy("publish_followup")
        $ ticket_handoff("sabrina")
        $ ticket_submit()
        $ literal_reason = "Falha {erro} {b}texto{/b} [player_name] [variavel_inexistente]."
        $ ticket_reopen(literal_reason)
        $ literal_history_index = len(ticket_records["241"]["history"]) - 1
        $ literal_history = "Solicitante reabriu · motivo: " + literal_reason
        $ escaped_history = literal_history.replace("{", "{{")
        assert eval ticket_records["241"]["history"][-1] == literal_history
        run Jump("tickets_followup")
        advance until screen "ticket_return"
        assert eval renpy.get_widget("ticket_return", "ticket_history_" + str(literal_history_index)).get_all_text() == escaped_history
        assert eval renpy.get_widget("ticket_return", "ticket_history_" + str(literal_history_index)).substitute is False
        run Show("campaign_desktop")
        pause until screen "campaign_desktop"
        click id "notebook_tab_inbox"
        $ literal_mail_id = next(message["id"] for message in notebook_messages() if message["kind"] == "history")
        click id ("notebook_message_" + literal_mail_id)
        assert eval escaped_history in renpy.get_widget("campaign_desktop", "notebook_message_body").get_all_text()
        assert eval renpy.get_widget("campaign_desktop", "notebook_message_body").substitute is False
        click id "notebook_close"
        click id "ticket_return_continue"
        advance until screen "ticket_final"
        assert eval renpy.get_widget("ticket_final", "ticket_final_history_" + str(literal_history_index)).get_all_text() == escaped_history
        assert eval renpy.get_widget("ticket_final", "ticket_final_history_" + str(literal_history_index)).substitute is False
        assert eval campaign_results["tickets"]["history"][-1] == literal_history
