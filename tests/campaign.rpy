label campaign_test_builder:
    call screen campaign_app_builder("expenses")
    jump campaign_hub

label campaign_test_checkpoint:
    $ campaign_reset()
    menu:
        "Qual retorno fica no registro?"
        "Registrar laboratório":
            $ campaign_record("lab", {"summary": "Agenda entregue", "facts": ["sheets"]})
        "Registrar pesquisa":
            $ campaign_record("lab", {"summary": "Pesquisa pendente", "facts": []})
    "A equipe arquiva o retorno."
    jump campaign_hub

label campaign_test_saved_hub:
    $ campaign_record("lab", {"summary": "Agenda entregue", "facts": ["sheets"]})
    $ campaign_place_module("expenses", "records", 0)
    $ campaign_record("expenses", {"summary": "Correção entregue"})
    "Os dois retornos foram registrados pela equipe."
    jump campaign_hub

label campaign_test_lab_end:
    $ lab_reset()
    $ lab_collect("sheets")
    $ lab_collect("preparation")
    $ lab_collect("interview")
    $ lab_toggle_plan("conflict")
    $ lab_toggle_plan("preparation")
    $ lab_confirm_commitment("base_primeiro")
    $ lab_mark_delivery()
    jump lab_adoption

label campaign_test_expenses_end:
    $ exp_set_plan("bank")
    jump exp_finish

label campaign_test_tickets_end:
    jump tickets_adoption

testsuite campaign:
    before testcase:
        if not screen "main_menu":
            run MainMenu(confirm=False)
        pause until screen "main_menu"
        run Start("campaign_start")
        advance until screen "campaign_hub_screen"

    testcase hub_journal_and_builder:
        assert eval campaign_active and not campaign_results
        move id "campaign_hotspot_expenses"
        assert screen "campaign_hub_screen"
        click id "campaign_journal_open"
        pause until screen "campaign_journal"
        keysym "K_ESCAPE"
        pause until not screen "campaign_journal"
        assert screen "campaign_hub_screen"
        run Jump("campaign_test_builder")
        pause until screen "campaign_app_builder"
        click id "builder_select_records"
        click id "builder_slot_0"
        assert eval campaign_layout("expenses")[0] == "records"
        assert screen "campaign_app_builder"
        drag id "builder_drag_actions" to id "builder_drop_0" steps 20
        assert eval campaign_layout("expenses")[0] == "actions"
        assert screen "campaign_app_builder"
        click id "campaign_builder_continue"
        pause until screen "campaign_hub_screen"

    testcase save_retains_results_and_layout:
        run Jump("campaign_test_saved_hub")
        advance until screen "campaign_hub_screen"
        $ renpy.take_screenshot()
        $ renpy.save("qa-campaign-hub")
        $ campaign_record("lab", {"summary": "Alterado"})
        $ campaign_place_module("expenses", "actions", 0)
        $ renpy.load("qa-campaign-hub")
        pause until screen "campaign_hub_screen"
        assert eval campaign_memory("lab")["summary"] == "Agenda entregue"
        assert eval campaign_memory("expenses")["layout"][0] == "records"
        assert eval campaign_layout("expenses")[0] == "records"
        click id "campaign_project_lab"
        advance until screen "lab_map"
        assert eval "expenses" in campaign_results and "lab" in campaign_results

    testcase rollback_restores_project_return:
        run Jump("campaign_test_checkpoint")
        advance until screen "choice"
        click "Registrar laboratório"
        advance until screen "campaign_hub_screen"
        assert eval campaign_memory("lab")["summary"] == "Agenda entregue"
        run Rollback() until "Registrar pesquisa"
        assert eval not campaign_results
        click "Registrar pesquisa"
        advance until screen "campaign_hub_screen"
        assert eval campaign_memory("lab")["summary"] == "Pesquisa pendente"

    # Os ensaios de cada domínio têm jornadas próprias. Aqui exercitamos a troca
    # de projeto na mesma partida e os finais reais, sem reset pelo menu.
    testcase project_returns_in_both_orders:
        parameter expenses_first = [True, False]
        click id "campaign_project_lab"
        advance until screen "lab_map"
        run Jump("campaign_test_lab_end")
        advance until screen "lab_final"
        click id "lab_final_hub"
        pause until screen "campaign_hub_screen"
        assert eval campaign_memory("lab")["outcome"] == "reliable"
        if eval expenses_first:
            click id "campaign_hotspot_expenses"
            advance until screen "exp_investigation"
            run Jump("campaign_test_expenses_end")
            advance until screen "exp_final"
            click id "exp_final_hub"
            pause until screen "campaign_hub_screen"
            click id "campaign_hotspot_tickets"
            advance until screen "ticket_investigation"
            run Jump("campaign_test_tickets_end")
            advance until screen "ticket_final"
            click id "ticket_final_hub"
        else:
            click id "campaign_hotspot_tickets"
            advance until screen "ticket_investigation"
            run Jump("campaign_test_tickets_end")
            advance until screen "ticket_final"
            click id "ticket_final_hub"
            pause until screen "campaign_hub_screen"
            click id "campaign_hotspot_expenses"
            advance until screen "exp_investigation"
            run Jump("campaign_test_expenses_end")
            advance until screen "exp_final"
            click id "exp_final_hub"
        pause until screen "campaign_hub_screen"
        assert eval set(campaign_results) == {"lab", "expenses", "tickets"}
        assert eval campaign_memory("expenses")["outcome"] == "waiting"
        assert eval campaign_memory("tickets")["outcome"] == "unowned"
        click id "campaign_ending_open"
        advance until screen "campaign_closing"
        click id "campaign_closing_back"
        pause until screen "campaign_hub_screen"
        assert eval len(campaign_results) == 3

testsuite campaign_visual:
    enabled False

    before testcase:
        if not screen "main_menu":
            run MainMenu(confirm=False)
        pause until screen "main_menu"

    testcase hub_and_builder:
        run Start("campaign_start")
        advance until screen "campaign_hub_screen"
        pause 0.2
        screenshot "campaign/hub.png"
        run Jump("campaign_test_builder")
        pause until screen "campaign_app_builder"
        click id "builder_select_records"
        click id "builder_slot_0"
        pause 0.2
        screenshot "campaign/builder.png"
