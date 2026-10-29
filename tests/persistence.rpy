testsuite persistence:
    before testcase:
        if not screen "main_menu":
            run MainMenu(confirm=False)
        pause until screen "main_menu"
        run Start()
        run SetVariable("chosen_job", "IDT-UFRJ")
        run Hide("inv_quick")
        run Jump("scene_2_estagio")
        advance until screen "choice"

    after testcase:
        $ renpy.unlink_save("qa-requirements-roundtrip")

    testcase save_restores_decisions:
        click "Peço que Carlos conte"
        advance until screen "choice"
        assert eval mission_score == 1 and mission_elicitation
        $ renpy.take_screenshot()
        $ renpy.save("qa-requirements-roundtrip")
        click "Pergunto o que Carlos precisa conseguir"
        advance until screen "choice"
        assert eval mission_score == 2 and mission_ambiguity
        $ renpy.load("qa-requirements-roundtrip")
        pause until screen "choice"
        assert eval mission_score == 1 and mission_elicitation and not mission_ambiguity
        assert "Pergunto o que Carlos precisa conseguir"

    testcase rollback_does_not_duplicate_score:
        click "Peço que Carlos conte"
        advance until screen "choice"
        assert eval mission_score == 1
        run Rollback() until "Peço que Carlos conte"
        assert eval mission_score == 0 and not mission_elicitation
        click "Pergunto qual tecnologia"
        advance until screen "choice"
        click "Carlos, você pode contar"
        advance until screen "choice"
        assert eval mission_score == 0 and not mission_elicitation
