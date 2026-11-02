# Notebook de registros: contagem, abrir/fechar pela Mochila e pelo teclado.
testsuite notebook:
    before testcase:
        if not screen "main_menu":
            run MainMenu(confirm=False)
        pause until screen "main_menu"
        run Start()
        pause until screen "say"
        $ chosen_job = "saude"

    testcase conta_e_fecha:
        run Show("notebook_registros")
        pause until screen "notebook_registros"
        assert eval "0 de 8 registros" in renpy.get_widget("notebook_registros", "notebook_progresso").text[0]
        $ registrar("saude_reg_ciclo")
        pause 0.2
        assert eval "1 de 8 registros" in renpy.get_widget("notebook_registros", "notebook_progresso").text[0]
        keysym "K_PAGEDOWN"
        keysym "K_n"
        assert not screen "notebook_registros"
        run Show("notebook_registros")
        pause until screen "notebook_registros"
        keysym "K_ESCAPE"
        assert not screen "notebook_registros"
        assert screen "say"

    testcase abre_pela_mochila:
        $ item_notebook = True
        $ registrar("saude_reg_testes")
        run ShowMenu("inventory_screen")
        pause until screen "inventory_screen"
        click id "inv_notebook"
        pause until screen "notebook_registros"
        assert not screen "inventory_screen"
        assert eval "1 de 8 registros" in renpy.get_widget("notebook_registros", "notebook_progresso").text[0]
        click id "notebook_fechar"
        pause 0.2
        assert not screen "notebook_registros"
        assert screen "say"

    testcase mochila_pelo_teclado:
        $ item_notebook = True
        $ item_celular = True
        run ShowMenu("inventory_screen")
        pause until screen "inventory_screen"
        keysym "K_i"
        pause 0.2
        assert not screen "inventory_screen"
        run ShowMenu("inventory_screen")
        pause until screen "inventory_screen"
        keysym "K_ESCAPE"
        pause 0.2
        assert not screen "inventory_screen"

    testcase registrar_e_decisao_sem_duplicar:
        $ registrar("saude_reg_ciclo")
        $ registrar("saude_reg_ciclo")
        $ registrar("id_que_nao_existe")
        assert eval registros == {"saude_reg_ciclo"}
        assert eval registros_contagem() == (1, 8)
        $ decisao("rw_decisao", False)
        $ decisao("rw_decisao", True)
        $ decisao("rw_outra", True)
        assert eval aprendizagem == {"rw_decisao": False, "rw_outra": True}
        assert eval resumo_decisoes() == (1, 1)
