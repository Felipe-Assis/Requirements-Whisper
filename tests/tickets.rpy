testsuite tickets:
    before testcase:
        if not screen "main_menu":
            run MainMenu(confirm=False)
        pause until screen "main_menu"

    testcase investigate_fix_and_publish:
        parameter policy = ["peer_review", "publish_followup"]
        run Start("tickets_campaign")
        advance until screen "ticket_investigation"
        assert eval ticket_active and ticket_evidence == []
        click id "ticket_source_panel"
        assert screen "ticket_investigation"
        click id "ticket_source_message"
        click id "ticket_source_log"
        click id "ticket_source_shift"
        assert eval ticket_sources_ready() and "shift" in ticket_evidence
        click id "ticket_investigation_continue"
        advance until screen "ticket_triage"
        click id "ticket_priority_241"
        assert eval ticket_selected == "241" and ticket_prioritized
        click id "ticket_triage_continue"
        advance until screen "ticket_workbench"
        click id "ticket_demo_old"
        assert screen "ticket_workbench"
        assert eval ticket_reproduced and ticket_demo_result == "divergent"
        assert eval ticket_demo_records["241"]["internal_status"] == "Resolvido"
        assert eval ticket_demo_records["241"]["public_status"] == "Em atendimento"
        click id "ticket_patch_atomic"
        move id "ticket_workbench_scroll"
        keysym "K_PAGEDOWN"
        click id "ticket_test_resolved"
        assert eval ticket_tests.get("resolved") == "published"
        assert eval ticket_demo_records["241"]["public_solution"] != ticket_demo_records["241"]["internal_note"]
        move id "ticket_workbench_scroll"
        keysym "K_PAGEDOWN"
        click id "ticket_test_empty"
        assert eval ticket_tests.get("empty") == "blocked"
        assert eval ticket_demo_records["241"]["internal_status"] == "Em atendimento"
        move id "ticket_workbench_scroll"
        keysym "K_PAGEDOWN"
        click id "ticket_test_other"
        assert eval ticket_tests.get("other") == "isolated"
        assert eval ticket_demo_records["242"] == ticket_records["242"]
        assert eval ticket_tests_ready()
        click id "ticket_workbench_continue"
        advance until screen "ticket_delivery"
        click id "ticket_solution_internal"
        assert eval ticket_draft == TICKET_CASES["241"]["note"]
        click id "ticket_solution_public"
        if eval policy == "peer_review":
            click id "ticket_policy_review"
        else:
            click id "ticket_policy_followup"
        click id "ticket_owner_sabrina"
        assert eval ticket_owner == "Sabrina" and "09h" in ticket_next_step
        click id "ticket_delivery_continue"
        advance until screen "ticket_return"
        if eval policy == "peer_review":
            assert eval ticket_delivery == "review_pending"
            assert eval ticket_records["241"]["public_status"] == "Em atendimento"
            click id "ticket_review"
            assert eval ticket_delivery == "reviewed"
        else:
            assert eval ticket_delivery == "published"
            click id "ticket_followup_confirm"
            assert eval ticket_ending() == "followed_up"
        assert eval ticket_records["241"]["public_status"] == "Resolvido"
        click id "ticket_return_continue"
        advance until screen "ticket_final"
        assert eval campaign_results["tickets"]["priority"] == "241"
        assert eval campaign_results["tickets"]["pending"] == ""
        click id "ticket_final_hub"
        advance until screen "campaign_hub_screen"
        assert eval not ticket_active

    testcase team_pending_can_be_recovered:
        run Start("tickets_campaign")
        advance until screen "ticket_investigation"
        $ ticket_collect("panel")
        $ ticket_collect("message")
        $ ticket_collect("log")
        $ ticket_prioritize("242")
        $ ticket_demo("old", "resolved")
        $ ticket_choose_patch("atomic")
        $ ticket_demo("new", "resolved")
        $ ticket_demo("new", "empty")
        $ ticket_demo("new", "other")
        run Jump("tickets_delivery")
        advance until screen "ticket_delivery"
        click id "ticket_solution_public"
        click id "ticket_policy_review"
        click id "ticket_owner_rodrigo"
        assert eval ticket_owner == "" and "turno" in ticket_feedback
        click id "ticket_owner_team"
        click id "ticket_delivery_continue"
        advance until screen "ticket_return"
        assert eval ticket_ending() == "unowned" and ticket_delivery == "not_delivered"
        assert eval ticket_records["242"]["public_status"] == "Em atendimento"
        click id "ticket_recover"
        assert screen "ticket_return"
        assert eval ticket_delivery == "review_pending"
        click id "ticket_review"
        assert eval ticket_ending() == "reviewed"
        assert eval ticket_records["241"]["public_status"] == "Em atendimento"
        assert eval ticket_records["243"]["public_status"] == "Em atendimento"

    testcase reopens_with_reason_and_keeps_history:
        parameter known_case = [True, False]
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
        run Jump("tickets_followup")
        advance until screen "ticket_return"
        $ ticket_previous_history = list(ticket_records["241"]["history"])
        if eval known_case:
            move id "ticket_return_scroll"
            keysym "K_PAGEDOWN"
            click id "ticket_reopen_known"
            assert eval ticket_reopen_known_case
        else:
            move id "ticket_return_scroll"
            keysym "K_PAGEDOWN"
            keysym "K_PAGEDOWN"
            click id "ticket_reopen"
            assert eval ticket_records["241"]["public_status"] == "Resolvido"
            assert eval "motivo" in ticket_feedback
            click id "ticket_reopen_reason_input"
            type "O problema continua em outro computador."
            click id "ticket_reopen"
            assert eval not ticket_reopen_known_case
        assert eval ticket_records["241"]["public_status"] == "Reaberto"
        assert eval ticket_records["241"]["history"][:len(ticket_previous_history)] == ticket_previous_history
        if eval known_case:
            click id "ticket_followup_repair"
            assert eval ticket_ending() == "repaired"
        else:
            assert eval ticket_ending() == "reopened"
            assert eval renpy.get_widget("ticket_return", "ticket_followup_repair") is None
        assert eval len(ticket_records["241"]["history"]) > len(ticket_previous_history)
        assert eval ticket_records["242"]["public_status"] == "Em atendimento"
        click id "ticket_return_continue"
        advance until screen "ticket_final"
        assert eval campaign_results["tickets"]["outcome"] == ("repaired" if known_case else "reopened")
