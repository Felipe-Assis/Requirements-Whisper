testsuite lab_journey:
    before testcase:
        if not screen "main_menu":
            run MainMenu(confirm=False)
        pause until screen "main_menu"

    testcase investigate_plan_and_return:
        run Start("lab_campaign")
        advance until screen "lab_map"
        assert eval lab_active and lab_evidence == []
        click id "lab_map_conversa"
        pause until screen "lab_location_screen"
        click id "lab_source_interview"
        advance until screen "lab_location_screen"
        assert eval "interview" in lab_evidence
        click id "lab_location_back"
        pause until screen "lab_map"
        click id "lab_map_equipe"
        pause until screen "lab_location_screen"
        click id "lab_source_offline"
        advance until screen "lab_location_screen"
        assert eval lab_sidequest
        click id "lab_location_back"
        pause until screen "lab_map"
        click id "lab_map_laboratorio"
        pause until screen "lab_location_screen"
        click id "lab_source_sheets"
        advance until screen "lab_location_screen"
        assert eval "sheets" in lab_evidence
        move id "lab_sources_scroll"
        keysym "K_PAGEDOWN"
        click id "lab_source_preparation"
        advance until screen "lab_location_screen"
        assert eval "preparation" in lab_evidence
        click id "lab_location_back"
        pause until screen "lab_map"
        assert eval all(eid in lab_evidence for eid in ("sheets", "preparation", "interview"))
        click id "lab_map_continue"
        advance until screen "lab_board"
        move id "lab_evidence_interview"
        keysym "K_PAGEDOWN"
        click id "lab_evidence_sheets"
        click id "lab_rule_conflict"
        click id "lab_evidence_preparation"
        move id "lab_rule_conflict"
        keysym "K_PAGEDOWN"
        click id "lab_rule_preparation"
        click id "lab_board_continue"
        advance until screen "lab_planning"
        click id "lab_plan_conflict"
        click id "lab_plan_preparation"
        click id "lab_plan_continue"
        advance until screen "choice"
        click "Entregar o plano primeiro"
        advance until screen "choice"
        click "Confirmar com Carlos e Júlio"
        advance until screen "lab_demo"
        assert eval lab_delivery == "not_delivered"
        click id "lab_test_overlap"
        assert eval lab_test_results.get("overlap") == "conflict"
        click id "lab_test_preparation"
        assert eval lab_test_results.get("preparation") == "preparation_required"
        click id "lab_demo_continue"
        advance until screen "choice"
        assert eval lab_phase == "followup"
        assert eval lab_delivery == "base_delivered"
        click "Trazer o retorno da investigação"
        advance until screen "lab_final"
        assert eval lab_ending() == "reliable"
        assert eval lab_commitment_status == "fulfilled"
        assert eval "adoption_reviewed" in lab_events
        click id "lab_final_menu"
        pause until screen "main_menu"
        assert eval not lab_active

    testcase investigation_is_not_delivery:
        run Start("lab_campaign")
        advance until screen "lab_map"
        $ lab_collect("sheets")
        $ lab_collect("preparation")
        $ lab_collect("interview")
        $ lab_toggle_plan("conflict")
        $ lab_toggle_plan("preparation")
        run Jump("lab_negotiation")
        advance until screen "choice"
        click "Investigar a integração agora"
        advance until screen "choice"
        click "Confirmar com Carlos e Júlio"
        advance until screen "choice"
        click "Experimentar a confirmação centralizada"
        advance until screen "lab_demo"
        assert eval lab_delivery == "not_delivered"
        click id "lab_test_overlap"
        assert eval lab_test_results.get("overlap") == "conflict"
        click id "lab_demo_continue"
        advance until screen "choice"
        click "Trazer o retorno da investigação"
        advance until screen "lab_final"
        assert eval lab_ending() == "waiting"
        assert eval "temporary_confirmation" in lab_events
        assert eval lab_commitment_status == "fulfilled"

    testcase omission_can_be_repaired_or_kept_visible:
        parameter repair = [True, False]
        run Start("lab_campaign")
        advance until screen "lab_map"
        $ lab_collect("sheets")
        $ lab_collect("preparation")
        $ lab_collect("interview")
        $ lab_toggle_plan("clarity")
        $ lab_confirm_commitment("base_primeiro")
        $ lab_mark_delivery()
        run Jump("lab_followup")
        advance until screen "choice"
        click "Renegociar o retorno"
        advance until screen "choice"
        assert eval lab_commitment_status == "renegotiated"
        if eval repair:
            click "Reproduzir e reparar o incidente"
            advance until screen "lab_demo"
            assert eval lab_delivery == "revision_pending"
            click id "lab_test_overlap"
            assert eval lab_test_results.get("overlap") == "conflict"
            click id "lab_test_preparation"
            assert eval lab_test_results.get("preparation") == "preparation_required"
            click id "lab_demo_continue"
            advance until screen "lab_final"
            assert eval lab_ending() == "repaired"
            assert eval lab_delivery == "repaired"
            assert eval lab_revision == 2 and lab_repaired
            assert eval "clarity" in lab_plan and lab_initial_plan == ["clarity"]
        else:
            click "Registrar o impacto e deixar a revisão pendente"
            advance until screen "lab_final"
            assert eval lab_ending() == "unowned"
            assert eval not lab_repaired
        assert eval "incident_observed" in lab_events
