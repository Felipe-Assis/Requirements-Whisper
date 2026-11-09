# Interações da campanha executadas pelo motor, sem substituir regras por mocks.
testsuite lab_ui:
    before testcase:
        python hide:
            renpy._lab_ui_preferences = (persistent.rw_large_text, _preferences.transitions)
        if not screen "main_menu":
            run MainMenu(confirm=False)
        pause until screen "main_menu"
        run Start("lab_campaign")
        advance until screen "lab_map"

    after testcase:
        python hide:
            persistent.rw_large_text, _preferences.transitions = renpy._lab_ui_preferences
            del renpy._lab_ui_preferences

    testcase revise_evidence_link:
        $ lab_collect("sheets")
        $ lab_collect("preparation")
        $ lab_collect("interview")
        $ lab_phase = "definition"
        run Show("lab_board")
        pause until screen "lab_board"
        click id "lab_evidence_interview"
        click id "lab_rule_conflict"
        assert eval lab_links["conflict"] == "interview"
        assert screen "lab_map"
        assert not screen "lab_location_screen"
        assert "Hipótese a revisar:"
        click id "lab_evidence_sheets"
        click id "lab_rule_conflict"
        assert eval lab_links["conflict"] == "sheets"
        click id "lab_evidence_preparation"
        move id "lab_rules_scroll"
        keysym "K_PAGEDOWN"
        click id "lab_rule_preparation"
        assert eval lab_links["preparation"] == "preparation"
        if eval __import__("os").environ.get("RW_LAB_CAPTURE") == "1":
            screenshot "review/lab_board.png"
        run Hide("lab_board")

    testcase map_has_equivalent_locations:
        if eval __import__("os").environ.get("RW_LAB_CAPTURE") == "1":
            pause 0.2
            screenshot "review/lab_map.png"
        click id "lab_hotspot_laboratorio"
        pause until screen "lab_location_screen"
        assert "Fontes deste local"
        click id "lab_location_back"
        pause until screen "lab_map"

    testcase capacity_feedback_and_revision:
        $ lab_phase = "planning"
        run Show("lab_planning")
        pause until screen "lab_planning"
        click id "lab_plan_preparation"
        assert eval lab_plan == []
        assert eval "depende" in lab_feedback
        click id "lab_plan_conflict"
        click id "lab_plan_preparation"
        assert eval lab_plan_cost() == 3
        assert screen "lab_map"
        assert not screen "lab_location_screen"
        click id "lab_plan_conflict"
        assert eval "conflict" in lab_plan
        assert eval "Retire a preparação primeiro" in lab_feedback
        click id "lab_plan_preparation"
        click id "lab_plan_conflict"
        assert eval lab_plan == []
        if eval __import__("os").environ.get("RW_LAB_CAPTURE") == "1":
            screenshot "review/lab_planning.png"
        run Hide("lab_planning")

    testcase calendar_keeps_existing_reservation:
        $ lab_plan = ["conflict", "preparation"]
        $ lab_phase = "delivery"
        run Show("lab_demo")
        pause until screen "lab_demo"
        click id "lab_test_overlap"
        assert eval lab_test_results["overlap"] == "conflict"
        assert screen "lab_map"
        assert not screen "lab_location_screen"
        assert "Conflito bloqueado"
        click id "lab_test_adjacent"
        assert eval lab_test_results["adjacent"] == "preparation_required"
        click id "lab_test_preparation"
        assert eval lab_test_results["preparation"] == "preparation_required"
        keysym "K_PAGEDOWN"
        click id "lab_test_other"
        assert eval lab_test_results["other"] == "allowed"
        click id "lab_existing_open"
        pause until screen "lab_reservation_reference"
        assert eval renpy.get_widget("lab_reservation_reference", "lab_existing_owner").get_all_text() == "Ana · reserva mantida"
        keysym "K_ESCAPE"
        assert not screen "lab_reservation_reference"
        assert eval all(case["existing"] == ("microscopio", 840, 900) for case in LAB_CASES.values())
        assert eval lab_plan == ["conflict", "preparation"]
        if eval __import__("os").environ.get("RW_LAB_CAPTURE") == "1":
            pause 0.2
            screenshot "review/lab_demo.png"
        run Hide("lab_demo")

    testcase readable_calendar_changes_consultation:
        parameter readable = [False, True]
        $ lab_plan = ["clarity"] if readable else ["conflict"]
        run Show("lab_demo")
        pause until screen "lab_demo"
        click id "lab_test_overlap"
        if eval readable:
            assert "Consulta unificada"
            assert "Microscópio · 14h00–15h00"
            assert eval lab_test_results["overlap"] == "allowed"
        else:
            assert "Consulta por registros"
            click id "lab_existing_open"
            pause until screen "lab_reservation_reference"
            assert eval renpy.get_widget("lab_reservation_reference", "lab_existing_owner").get_all_text() == "Ana · reserva mantida"
            click id "lab_existing_close"
            assert eval lab_test_results["overlap"] == "conflict"
        if eval __import__("os").environ.get("RW_LAB_CAPTURE") == "1":
            pause 0.2
            screenshot ("review/lab_demo_" + ("unified" if readable else "separate") + ".png")
        run Hide("lab_demo")

    testcase repair_is_verified_before_delivery:
        $ lab_plan = ["clarity"]
        $ lab_confirm_commitment("base_primeiro")
        $ lab_mark_delivery()
        $ lab_repair()
        run Show("lab_demo")
        pause until screen "lab_demo"
        assert eval lab_delivery == "revision_pending"
        click id "lab_test_overlap"
        click id "lab_test_preparation"
        assert eval lab_delivery == "revision_pending"
        run Show("lab_journal")
        pause until screen "lab_journal"
        move id "lab_journal_scroll"
        keysym "K_PAGEDOWN"
        assert "Plano inicial: Calendário legível"
        assert "revisão 2 em verificação; versão anterior em uso"
        keysym "K_ESCAPE"
        $ lab_mark_delivery()
        assert eval lab_delivery == "repaired"
        run Hide("lab_demo")

    testcase journal_keyboard_and_large_text:
        parameter large = [False, True]
        $ persistent.rw_large_text = large
        $ _preferences.transitions = 0
        $ lab_collect("sheets")
        $ lab_collect("preparation")
        $ lab_collect("interview")
        $ lab_collect("offline")
        keysym "K_n"
        pause until screen "lab_journal"
        assert "Duas reservas, um microscópio"
        move id "lab_journal_scroll"
        keysym "K_PAGEDOWN"
        pause 0.1
        assert eval renpy.get_widget("lab_journal", "lab_journal_scroll").yadjustment.value > 0
        if eval __import__("os").environ.get("RW_LAB_CAPTURE") == "1":
            screenshot ("review/lab_journal_" + ("large" if large else "normal") + ".png")
        keysym "K_ESCAPE"
        assert not screen "lab_journal"
        assert screen "lab_map"
        assert eval len(lab_evidence) == 4 and lab_plan == []

    testcase final_variants:
        parameter (ending, large) = [("reliable", False), ("reliable", True), ("waiting", False), ("waiting", True), ("repaired", False), ("unowned", False)]
        $ persistent.rw_large_text = large
        $ lab_collect("sheets")
        $ lab_collect("preparation")
        $ lab_collect("interview")
        $ lab_plan = ["clarity"] if ending in ("repaired", "unowned") else ["conflict", "preparation"]
        $ lab_confirm_commitment("investigar_agora" if ending == "waiting" else "base_primeiro")
        if eval ending != "waiting":
            $ lab_mark_delivery()
        if eval ending == "repaired":
            $ lab_repair()
        $ lab_run_test("overlap")
        $ lab_run_test("preparation")
        if eval ending == "repaired":
            $ lab_mark_delivery()
        assert eval lab_ending() == ending
        $ lab_phase = "ending"
        run Show("lab_final", ending=ending)
        pause until screen "lab_final"
        if eval __import__("os").environ.get("RW_LAB_CAPTURE") == "1":
            pause 0.2
            screenshot ("review/lab_final_" + ending + ("_large" if large else "") + ".png")
        pause until id "lab_final_care"
        assert eval renpy.get_widget("lab_final", "lab_final_care").get_all_text() == "O próximo cuidado"
        assert "Jogar a campanha novamente"
        assert "Voltar ao menu"
        assert "Conhecer a jornada guiada"
        run Hide("lab_final")
