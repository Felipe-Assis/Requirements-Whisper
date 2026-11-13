# A bancada usa os mesmos passos e regras tanto no ensaio quanto na revisão.
label lab_dev_test_bench:
    call screen lab_development_bench
    jump campaign_hub

testsuite lab_development:
    before testcase:
        python hide:
            renpy._lab_dev_test_preferences = persistent.rw_large_text
        if not screen "main_menu":
            run MainMenu(confirm=False)
        pause until screen "main_menu"
        run Start("lab_campaign")
        advance until screen "lab_map"
        $ campaign_active = True
        $ lab_plan = ["conflict", "preparation"]
        $ lab_dev_reset()
        run Jump("lab_dev_test_bench")
        pause until screen "lab_development_bench"

    after testcase:
        python hide:
            persistent.rw_large_text = renpy._lab_dev_test_preferences
            del renpy._lab_dev_test_preferences
        $ renpy.unlink_save("qa-lab-development")
        $ campaign_active = False
        run Hide("lab_development_bench")

    testcase edit_sequence_and_repeat_regression:
        click id "lab_dev_test_invalid"
        assert eval lab_dev_results["invalid"]["dirty"]
        assert eval len(lab_dev_results["invalid"]["reservations"]) == 2
        assert eval not lab_dev_ready()
        assert "Mutação indevida"
        click id "lab_dev_select_validate"
        click id "lab_dev_place_0"
        assert eval lab_dev_order == ["validate", "save", "rules"]
        assert eval lab_dev_results == {}
        click id "lab_dev_select_rules"
        move id "lab_dev_cases_scroll"
        keysym "K_PAGEDOWN"
        click id "lab_dev_place_1"
        assert eval lab_dev_order == ["validate", "rules", "save"]
        move id "lab_dev_cases_scroll"
        keysym "K_PAGEUP"
        keysym "K_PAGEUP"
        click id "lab_dev_test_invalid"
        assert eval "invalid" in lab_dev_results
        click id "lab_dev_test_overlap"
        assert eval "overlap" in lab_dev_results
        click id "lab_dev_test_preparation"
        assert eval "preparation" in lab_dev_results
        click id "lab_dev_test_other"
        assert eval lab_dev_ready()
        assert eval lab_dev_results["invalid"]["reservations"] == [("microscopio", 840, 900)]
        assert eval lab_dev_results["overlap"]["result"] == "conflict"
        assert eval lab_dev_results["preparation"]["result"] == "preparation_required"
        assert eval lab_dev_results["other"]["result"] == "allowed"
        move id "lab_dev_cases_scroll"
        keysym "K_PAGEDOWN"
        click id "lab_dev_review_pair"
        assert eval lab_dev_mode == "pair"
        assert eval lab_dev_results["adjacent"]["result"] == "preparation_required"
        assert eval "Júlio" in lab_dev_feedback and "15h" in lab_dev_feedback
        assert eval lab_test_results == {}

    testcase omitted_rules_remain_omitted:
        $ lab_plan = ["clarity"]
        $ lab_dev_order = ["validate", "rules", "save"]
        click id "lab_dev_test_invalid"
        click id "lab_dev_test_overlap"
        click id "lab_dev_test_preparation"
        click id "lab_dev_test_other"
        assert eval lab_dev_ready()
        assert eval lab_dev_results["overlap"]["result"] == "allowed"
        assert eval lab_dev_results["preparation"]["result"] == "allowed"
        assert eval lab_plan == ["clarity"]
        assert "Limitação: este pacote aceita sobreposição."
        assert "Limitação: este pacote não protege o preparo."

    testcase save_restores_sequence_and_results_with_large_text:
        $ persistent.rw_large_text = True
        $ lab_dev_order = ["validate", "rules", "save"]
        click id "lab_dev_test_overlap"
        move id "lab_dev_cases_scroll"
        keysym "K_PAGEDOWN"
        keysym "K_PAGEDOWN"
        click id "lab_dev_review_solo"
        assert eval lab_dev_mode == "solo"
        $ renpy.take_screenshot()
        $ renpy.save("qa-lab-development")
        $ lab_dev_reset()
        assert eval lab_dev_results == {}
        $ renpy.load("qa-lab-development")
        pause until screen "lab_development_bench"
        assert eval lab_dev_order == ["validate", "rules", "save"]
        assert eval lab_dev_results["overlap"]["result"] == "conflict"
        assert eval lab_dev_mode == "solo"
        assert eval lab_dev_revision == 1
        assert eval not lab_dev_ready()
