# Testa o estado sem depender das telas da campanha.
label lab_state_test_checkpoint:
    $ lab_reset()
    $ lab_toggle_plan("conflict")
    "O plano está pronto para combinar a prioridade."
    menu:
        "Confirmar base no teste":
            $ lab_collect("sheets")
            $ lab_link("conflict", "sheets")
            $ lab_confirm_commitment("base_primeiro")
            $ lab_mark_delivery()
        "Confirmar investigação no teste":
            $ lab_collect("interview")
            $ lab_confirm_commitment("investigar_agora")
    "A equipe registrou a prioridade e a fonte consultada."
    menu:
        "Continuar teste de estado":
            return

testsuite lab_state:
    before testcase:
        if not screen "main_menu":
            run MainMenu(confirm=False)
        pause until screen "main_menu"
        run Start()
        run Hide("inv_quick")

    after testcase:
        $ renpy.unlink_save("qa-lab-state-roundtrip")

    testcase calendar_and_plan:
        $ lab_reset()
        assert eval not lab_plan_ready()
        $ result = lab_toggle_plan("preparation")
        assert eval not result and lab_plan == []
        $ result = lab_toggle_plan("conflict")
        assert eval result and lab_plan == ["conflict"]
        $ result = lab_toggle_plan("preparation")
        assert eval result
        assert eval lab_plan_cost() == 3 and lab_plan_ready()
        $ result = lab_toggle_plan("clarity")
        assert eval not result and lab_plan == ["conflict", "preparation"]
        $ result = lab_toggle_plan("conflict")
        assert eval not result and lab_plan == ["conflict", "preparation"]
        assert eval lab_reservation_result(("microscopio", 840, 900), ("microscopio", 870, 930), lab_plan) == "conflict"
        assert eval lab_reservation_result(("microscopio", 840, 900), ("microscopio", 900, 930), ["conflict"]) == "allowed"
        assert eval lab_reservation_result(("microscopio", 840, 900), ("microscopio", 900, 930), lab_plan) == "preparation_required"
        assert eval lab_reservation_result(("microscopio", 840, 900), ("microscopio", 910, 930), lab_plan) == "allowed"
        assert eval lab_reservation_result(("centrifuga", 840, 900), ("centrifuga", 900, 930), lab_plan) == "allowed"
        assert eval lab_reservation_result(("microscopio", 840, 900), ("microscopio", 920, 900), lab_plan) == "invalid"
        assert eval lab_reservation_result(("microscopio", 840, 900), ("centrifuga", 840, 900), lab_plan) == "allowed"

    testcase evidence_and_endings:
        $ lab_reset()
        $ result = lab_link("conflict", "sheets")
        assert eval not result
        $ lab_collect("sheets")
        $ lab_collect("sheets")
        assert eval lab_evidence == ["sheets"]
        $ result = lab_link("preparation", "sheets")
        assert eval not result
        assert eval lab_links["preparation"] == "sheets"
        $ lab_collect("preparation")
        $ result = lab_link("preparation", "preparation")
        assert eval result
        $ lab_toggle_plan("clarity")
        $ lab_confirm_commitment("base_primeiro")
        assert eval lab_delivery == "not_delivered" and "base_delivered" not in lab_events
        assert eval lab_initial_plan == ["clarity"]
        $ lab_mark_delivery()
        assert eval lab_ending() == "unowned"
        $ result = lab_run_test("overlap")
        assert eval result == "allowed"
        $ lab_repair()
        assert eval lab_delivery == "revision_pending" and lab_revision == 2
        assert eval lab_ending() == "unowned" and "repaired" not in lab_events
        $ result = lab_mark_delivery()
        assert eval not result and lab_delivery == "revision_pending"
        assert eval lab_initial_plan == ["clarity"] and "clarity" in lab_plan
        assert eval lab_plan_cost() == 4
        assert eval lab_test_results == {}
        assert eval lab_evidence == ["sheets", "preparation"]
        assert eval lab_commitment == "base_primeiro"
        $ result = lab_run_test("overlap")
        assert eval result == "conflict"
        $ result = lab_mark_delivery()
        assert eval not result and lab_delivery == "revision_pending"
        $ result = lab_run_test("preparation")
        assert eval result == "preparation_required"
        $ result = lab_mark_delivery()
        assert eval result and lab_delivery == "repaired" and lab_ending() == "repaired"
        assert eval lab_events.count("repaired") == 1
        $ lab_reset()
        $ lab_toggle_plan("conflict")
        $ lab_toggle_plan("preparation")
        $ lab_confirm_commitment("base_primeiro")
        $ lab_mark_delivery()
        assert eval lab_test_results == {} and lab_ending() == "reliable"
        $ result = lab_toggle_plan("preparation")
        assert eval not result
        $ lab_confirm_commitment("investigar_agora")
        assert eval lab_delivery == "not_delivered" and lab_ending() == "waiting"
        $ result = lab_mark_delivery()
        assert eval not result and lab_delivery == "not_delivered"
        assert eval lab_commitment_status == "open"
        assert eval lab_commitment_owner and lab_return_milestone
        $ lab_run_test("overlap")
        assert eval lab_ending() == "waiting"

    testcase save_restores_campaign_facts:
        run Jump("lab_state_test_checkpoint")
        advance until screen "choice"
        click "Confirmar base no teste"
        advance until screen "choice"
        assert eval lab_delivery == "base_delivered" and lab_evidence == ["sheets"]
        assert eval lab_initial_plan == ["conflict"]
        $ renpy.take_screenshot()
        $ renpy.save("qa-lab-state-roundtrip")
        $ lab_collect("offline")
        $ lab_repair()
        $ lab_run_test("preparation")
        assert eval lab_sidequest and lab_repaired and lab_revision == 2
        $ renpy.load("qa-lab-state-roundtrip")
        pause until screen "choice"
        assert eval lab_delivery == "base_delivered" and not lab_repaired and lab_revision == 1
        assert eval lab_evidence == ["sheets"] and not lab_sidequest
        assert eval lab_links == {"conflict": "sheets"}
        assert eval lab_initial_plan == ["conflict"] and lab_plan == ["conflict"]
        assert eval lab_test_results == {} and "repaired" not in lab_events
        assert eval lab_commitment == "base_primeiro" and lab_ending() == "unowned"

    testcase rollback_restores_choice_and_sources:
        run Jump("lab_state_test_checkpoint")
        advance until screen "choice"
        click "Confirmar base no teste"
        advance until screen "choice"
        assert eval lab_delivery == "base_delivered" and lab_evidence == ["sheets"]
        run Rollback() until "Confirmar investigação no teste"
        assert eval lab_commitment == "" and lab_delivery == "not_delivered"
        assert eval lab_events == [] and lab_evidence == [] and lab_links == {}
        assert eval lab_initial_plan == []
        click "Confirmar investigação no teste"
        advance until screen "choice"
        assert eval lab_commitment == "investigar_agora" and lab_ending() == "waiting"
        assert eval lab_evidence == ["interview"] and "base_delivered" not in lab_events
        assert eval lab_events.count("commitment_confirmed") == 1
        assert eval lab_initial_plan == ["conflict"]

    testcase replay_and_legacy_defaults:
        assert eval not lab_active and lab_delivery == "not_delivered"
        $ lab_reset()
        $ lab_collect("offline")
        $ lab_toggle_plan("conflict")
        $ lab_confirm_commitment("investigar_agora")
        $ lab_repair()
        $ lab_reset()
        assert eval lab_active and lab_phase == "investigation"
        assert eval not lab_repaired and not lab_sidequest and lab_revision == 1
        assert eval lab_commitment == "" and lab_commitment_status == "open"
        assert eval lab_plan == [] and lab_evidence == [] and lab_events == []
        assert eval lab_initial_plan == []
        assert eval lab_delivery == "not_delivered" and lab_ending() == "waiting"
