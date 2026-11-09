# Capturas opcionais para inspeção humana; não são baselines aprovadas.
testsuite lab_visual:
    enabled False

    before testcase:
        python hide:
            renpy._lab_visual_cps = _preferences.text_cps
            _preferences.text_cps = 0
        if not screen "main_menu":
            run MainMenu(confirm=False)
        pause until screen "main_menu"

    after testcase:
        python hide:
            _preferences.text_cps = renpy._lab_visual_cps
            del renpy._lab_visual_cps

    testcase menu_map_and_sources:
        pause 0.2
        screenshot "review/campaign_menu.png"
        click "Jogar a campanha"
        advance until screen "lab_map"
        pause 0.2
        screenshot "review/campaign_map.png"
        click id "lab_map_laboratorio"
        pause until screen "lab_location_screen"
        pause 0.2
        screenshot "review/campaign_lab.png"
        click id "lab_source_sheets"
        advance until screen "lab_location_screen"
        assert eval "sheets" in lab_evidence

    testcase return_outfit:
        run Start("lab_campaign")
        advance until screen "lab_map"
        $ lab_plan = ["conflict", "preparation"]
        $ lab_confirm_commitment("base_primeiro")
        $ lab_mark_delivery()
        run Jump("lab_followup")
        advance until "Você combinou"
        pause 0.2
        screenshot "review/campaign_return.png"
