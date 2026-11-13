testsuite main_menu_navigation:
    before testcase:
        if not screen "main_menu":
            run MainMenu(confirm=False)
        pause until screen "main_menu"

    testcase new_game_opens_campaign:
        assert not "Iniciar história"
        click id "main_new_game"
        advance until screen "campaign_hub_screen"
        assert eval campaign_active

    testcase legacy_demo_is_identified_in_extras:
        click id "main_extras"
        pause until screen "rw_extras"
        assert "Demo guiada anterior"
        assert "O progresso da demo não é transferido"
        click id "extras_legacy_demo"
        advance until screen "pointclick_quarto_1"
        assert not eval campaign_active
