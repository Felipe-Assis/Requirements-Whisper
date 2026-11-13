# Capturas para revisão visual; não aprovam automaticamente a aparência.
testsuite continuation_visual:
    enabled False

    before testcase:
        python hide:
            renpy._continuation_cps = _preferences.text_cps
            _preferences.text_cps = 0
        if not screen "main_menu":
            run MainMenu(confirm=False)
        pause until screen "main_menu"

    after testcase:
        python hide:
            _preferences.text_cps = renpy._continuation_cps
            del renpy._continuation_cps

    testcase expenses:
        run Start("expenses_campaign")
        advance until screen "exp_investigation"
        pause 0.2
        screenshot "campaign/expenses-investigation.png"
        $ exp_inspect("receipt")
        $ exp_inspect("ledger")
        $ exp_inspect("lia")
        $ exp_set_plan("core")
        $ exp_apply_change("defer")
        $ exp_apply_change("total")
        $ exp_apply_change("undo")
        $ exp_build("pair")
        $ campaign_place_module("expenses", "records", 0)
        run Jump("exp_demo")
        pause until screen "exp_ledger"
        pause 0.2
        screenshot "campaign/expenses.png"

    testcase tickets:
        run Start("tickets_campaign")
        advance until screen "ticket_investigation"
        pause 0.2
        screenshot "campaign/tickets-investigation.png"
        $ ticket_collect("panel")
        $ ticket_collect("message")
        $ ticket_collect("log")
        $ ticket_prioritize("241")
        $ ticket_demo("old", "resolved")
        $ ticket_choose_patch("atomic")
        $ ticket_demo("new", "resolved")
        run Jump("tickets_development")
        pause until screen "ticket_workbench"
        pause 0.2
        screenshot "campaign/tickets.png"
        run Jump("tickets_adoption")
        pause 1.0
        screenshot "campaign/rain.png"

    testcase city:
        run Start("student_test_start")
        advance until screen "student_city_screen"
        click id "student_map_campus"
        pause until screen "student_location_screen"
        click id "student_object"
        move pos (1850, 180)
        pause 0.2
        screenshot "campaign/campus.png"
        move id "student_object"
        pause 0.2
        screenshot "campaign/object-hover.png"
        click id "student_location_schedule"
        advance until screen "student_schedule_screen"
        click id "student_tuesday_study"
        click id "student_thursday_workshop"
        pause 0.2
        screenshot "campaign/schedule.png"
        click id "student_schedule_back"
        pause until screen "student_city_screen"
        click id "student_map_workshop"
        pause until screen "student_location_screen"
        click id "student_object"
        pause 0.2
        screenshot "campaign/workshop.png"

    testcase development:
        run Start("lab_campaign")
        advance until screen "lab_map"
        $ lab_plan = ["conflict", "preparation"]
        $ lab_dev_reset()
        run Jump("lab_dev_test_bench")
        pause until screen "lab_development_bench"
        click id "lab_dev_test_invalid"
        pause 0.2
        screenshot "campaign/development.png"

    testcase notebook_and_dossier:
        run Start("campaign_start")
        advance until screen "campaign_hub_screen"
        $ campaign_record("lab", {"outcome": "waiting", "summary": "A investigação tem responsável; a agenda ainda não foi entregue.", "pending": "Retomar a autorização com Carlos na próxima reunião.", "plan": ["conflict", "preparation"], "commitment_owner": "Carlos e Júlio", "return_milestone": "reunião da coordenação na próxima sexta-feira"})
        click id "campaign_bag_open"
        pause until screen "campaign_bag"
        pause 0.2
        screenshot "campaign/backpack.png"
        click id "campaign_bag_notebook"
        pause until screen "campaign_desktop"
        pause 0.2
        screenshot "campaign/notebook.png"
        click id "notebook_tab_inbox"
        pause 0.2
        screenshot "campaign/inbox.png"
        click id "notebook_message_invite_lab"
        pause 0.2
        screenshot "campaign/email.png"
        click id "notebook_tab_documents"
        click id "notebook_document_campaign"
        pause until screen "campaign_journal"
        pause 0.2
        screenshot "campaign/dossier.png"
        keysym "K_ESCAPE"
        click id "notebook_close"
