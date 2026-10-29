# Regressões da interface real, com preferências restauradas entre os casos.
testsuite accessibility:
    before testcase:
        python hide:
            renpy._rw_a11y_preferences = (persistent.rw_large_text, _preferences.text_cps, _preferences.transitions)
        if not screen "main_menu":
            run MainMenu(confirm=False)
        pause until screen "main_menu"

    after testcase:
        python hide:
            persistent.rw_large_text, _preferences.text_cps, _preferences.transitions = renpy._rw_a11y_preferences
            del renpy._rw_a11y_preferences

    testcase reading_preferences:
        click "Preferências"
        pause until screen "preferences"
        if eval __import__("os").environ.get("RW_A11Y_CAPTURE") == "1":
            pause 0.6
            screenshot ("review/a11y_preferences_" + ("compact" if renpy.variant("small") else "desktop") + ".png")
        click "Ajustar leitura e acessibilidade"
        pause until screen "rw_accessibility"
        if not eval renpy.variant("small"):
            run SetField(persistent, "rw_large_text", False)
            click "Texto maior: desativado"
            assert eval persistent.rw_large_text
            click "Texto maior: ativado"
            assert eval not persistent.rw_large_text
        run SetField(_preferences, "text_cps", 30)
        click "Ativar texto instantâneo"
        assert eval _preferences.text_cps == 0
        run SetField(_preferences, "transitions", 2)
        keysym "K_PAGEDOWN"
        click id "rw_transitions"
        assert eval _preferences.transitions == 0
        keysym "K_ESCAPE"
        assert not screen "rw_accessibility"

    testcase long_choices_keyboard:
        parameter large = [False, True]
        run Start()
        run Hide("inv_quick")
        $ quick_menu = False
        $ persistent.rw_large_text = large
        $ chosen_job = "Startup"
        $ mission_rule = "Confirmar a exclusão de gastos e atualizar o total."
        $ mission_edge_criterion = "Cancelar mantém os dados e o total."
        run Jump("scene_3_planejamento")
        advance until screen "choice"
        if eval __import__("os").environ.get("RW_A11Y_CAPTURE") == "1":
            pause 0.6
            screenshot ("review/a11y_choices_" + ("compact_" if renpy.variant("small") else "desktop_") + ("large" if large else "normal") + ".png")
        if eval large and not renpy.variant("small"):
            assert eval renpy.get_widget("choice", "choice_scroll").yadjustment.range > 0
        if eval renpy.get_widget("choice", "choice_scroll").yadjustment.range > 0:
            keysym "K_PAGEDOWN"
            pause 0.2
            assert eval renpy.get_widget("choice", "choice_scroll").yadjustment.value > 0
            if eval __import__("os").environ.get("RW_A11Y_CAPTURE") == "1":
                screenshot ("review/a11y_scrolled_" + ("compact_" if renpy.variant("small") else "desktop_") + ("large" if large else "normal") + ".png")
        # O primeiro foco por teclado deve chegar a uma escolha após a rolagem.
        keysym "K_DOWN"
        keysym "K_RETURN"
        pause 0.2
        assert eval planning_selected or not renpy.get_screen("choice")

    testcase empty_history:
        run Start()
        run ShowMenu("history")
        pause until screen "history"
        keysym "K_ESCAPE"
        assert not screen "history"
