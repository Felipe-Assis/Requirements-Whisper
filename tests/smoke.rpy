# Executa no motor Ren'Py: telas, ações e estado do jogo reais.
testsuite global:
    teardown:
        exit

testsuite smoke:
    before testcase:
        if not screen "main_menu":
            run MainMenu(confirm=False)
        pause until screen "main_menu"

    testcase preparation_and_inventory:
        run Start()
        advance until screen "pointclick_quarto_1"
        # O mouse virtual conserva o foco do teste anterior. Comece pelo HUD
        # sem clicar; navegue até o objeto e confirme apenas pelo teclado.
        move id "inventory_open"
        keysym "K_DOWN"
        keysym "K_LEFT"
        keysym "K_RETURN"
        advance until screen "pointclick_quarto_2"
        assert eval alarm_off
        click id "room_advance"
        advance until screen "player_formulario"
        click id "profile_default"
        advance until screen "choice"
        click "IDT-UFRJ — organizar reservas de equipamentos"
        advance until screen "pointclick_quarto_3"
        click id "room_advance"
        advance until screen "pointclick_guardar_notebook"
        click id "room_advance"
        advance until screen "pointclick_guarda_roupa"
        assert eval notebook_in_bag
        assert eval inventory == ["notebook", "mochila"]
        run Show("inventory_screen")
        pause until screen "inventory_screen"
        click "Notebook"
        assert eval selected_item == "notebook"
        keysym "K_ESCAPE"
        assert not screen "inventory_screen"
        click id "room_advance"
        advance until screen "choice"
        assert eval clothes_changed
        assert eval chosen_job == "IDT-UFRJ"

    testcase accessibility_menu:
        click "Acessibilidade"
        pause until screen "rw_accessibility"
        run Return()
        assert screen "main_menu"
