testsuite notebook:
    before testcase:
        if not screen "main_menu":
            run MainMenu(confirm=False)
        pause until screen "main_menu"
        run Start()
        run Hide("inv_quick")
        run SetVariable("notebook_available", True)
        run Show("learning_hud")

    testcase discovery_and_keyboard:
        run SetVariable("chosen_job", "Startup")
        run Jump("scene_2_estagio")
        advance until screen "choice"
        assert eval not any(known for title, known, content in learning_records())
        keysym "K_n"
        pause until screen "learning_notebook"
        assert eval renpy.get_widget("learning_notebook", "notebook_progress").text[0].startswith("0 de 6")
        keysym "K_ESCAPE"
        assert not screen "learning_notebook"
        click "Pergunto qual tecnologia"
        advance until screen "choice"
        click "Carlos, você pode contar"
        advance until screen "choice"
        assert eval mission_stage == 1 and not mission_elicitation
        keysym "K_n"
        pause until screen "learning_notebook"
        assert eval renpy.get_widget("learning_notebook", "notebook_progress").text[0].startswith("1 de 6")
        assert eval [known for title, known, content in learning_records()] == [True, False, False, False, False, False]
        keysym "K_n"
        assert not screen "learning_notebook"
        assert screen "choice"

    testcase complete_and_long_text:
        run SetVariable("chosen_job", "IDT-UFRJ")
        run Jump("scene_2_estagio")
        advance until screen "choice"
        run SetVariable("mission_stage", 4)
        run SetVariable("mission_edge_criterion", "Caso limite confirmado.")
        run SetVariable("negotiation_complete", True)
        run SetVariable("negotiation_agreement", "Acordo confirmado.")
        run SetVariable("transfer_complete", True)
        run SetVariable("transfer_requirement", "{b}Rascunho [literal] " * 12)
        run SetVariable("transfer_criterion", "Resultado esperado. " * 20)
        run SetField(persistent, "rw_large_text", True)
        keysym "K_n"
        pause until screen "learning_notebook"
        assert eval renpy.get_widget("learning_notebook", "notebook_progress").text[0].startswith("6 de 6")
        keysym "K_PAGEDOWN"
        pause 0.2
        click id "notebook_close"
        assert not screen "learning_notebook"
        run SetField(persistent, "rw_large_text", False)
        run Jump("scene_2_estagio")
        advance until screen "choice"
        assert eval not any(known for title, known, content in learning_records())

    testcase optional_name_and_badge:
        advance until screen "pointclick_quarto_1"
        click id "room_advance"
        advance until screen "pointclick_quarto_2"
        click id "room_advance"
        advance until screen "player_formulario"
        run SetVariable("player_name", "")
        click id "profile_badge_dialogo"
        assert eval player_avatar == "dialogo"
        assert "Diálogo · selecionado"
        click id "profile_continue"
        advance until screen "choice"
        assert eval player_name == "Alex"
