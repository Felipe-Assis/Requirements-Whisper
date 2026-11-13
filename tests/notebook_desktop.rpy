testsuite notebook_desktop:
    before testcase:
        if not screen "main_menu":
            run MainMenu(confirm=False)
        pause until screen "main_menu"
        run Start("campaign_start")
        advance until screen "campaign_hub_screen"

    after testcase:
        $ renpy.unlink_save("qa-notebook-desktop")
        run Hide("campaign_desktop")
        run Hide("campaign_bag")
        run Hide("campaign_journal")
        run Hide("lab_journal")

    testcase notebook_opens_documents_without_leaving_activity:
        run Jump("lab_campaign")
        advance until screen "lab_map"
        keysym "K_i"
        pause until screen "campaign_bag"
        click id "campaign_bag_notebook"
        pause until screen "campaign_desktop"
        assert not screen "campaign_bag"
        assert screen "lab_map"
        click id "notebook_document_campaign"
        pause until screen "campaign_journal"
        keysym "K_ESCAPE"
        assert screen "campaign_desktop"
        click id "notebook_document_lab"
        pause until screen "lab_journal"
        keysym "K_ESCAPE"
        assert screen "campaign_desktop"
        click id "notebook_close"
        assert screen "lab_map"
        assert not screen "campaign_desktop"

    testcase inbox_marks_read_and_save_restores_ids:
        click id "campaign_bag_open"
        pause until screen "campaign_bag"
        click id "campaign_bag_notebook"
        pause until screen "campaign_desktop"
        click id "notebook_tab_inbox"
        click id "notebook_message_invite_lab"
        assert eval notebook_read == ["invite_lab"]
        assert "De: Sabrina"
        assert screen "campaign_hub_screen"
        $ renpy.take_screenshot()
        $ renpy.save("qa-notebook-desktop")
        $ notebook_read = []
        $ renpy.load("qa-notebook-desktop")
        pause until screen "campaign_hub_screen"
        assert eval notebook_read == ["invite_lab"]
        keysym "K_i"
        pause until screen "campaign_bag"
        click id "campaign_bag_notebook"
        pause until screen "campaign_desktop"
        click id "notebook_tab_inbox"
        click id "notebook_message_invite_lab"
        assert eval notebook_read == ["invite_lab"]
        keysym "K_ESCAPE"
        assert screen "campaign_hub_screen"

    testcase pending_return_and_new_revision_have_distinct_read_state:
        $ campaign_record("lab", {"outcome": "waiting", "summary": "A agenda ainda não foi entregue.", "pending": "Pedir autorização."})
        $ campaign_record("expenses", {"outcome": "delivered", "summary": "Correção conferida com Lia.", "pending": "Acompanhar o uso."})
        $ notebook_lab_return = next(message["id"] for message in notebook_messages() if message["kind"] == "return" and message["project"] == "lab")
        $ notebook_mark_read(notebook_lab_return)
        $ campaign_record("lab", {"outcome": "waiting", "summary": "Pesquisa devolvida; entrega ainda pendente.", "pending": "Retomar autorização."})
        assert eval notebook_lab_return in notebook_read
        assert eval next(message["id"] for message in notebook_messages() if message["kind"] == "return" and message["project"] == "lab") not in notebook_read
        assert eval any(message["project"] == "expenses" and message["kind"] == "return" and "Correção conferida com Lia." in message["body"] for message in notebook_messages())
        assert eval campaign_results["lab"]["outcome"] == "waiting"
