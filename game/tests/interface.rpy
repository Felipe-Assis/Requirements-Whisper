# Chat offline, perfil, acessibilidade e resumo do epílogo.
testsuite interface:
    before testcase:
        python hide:
            renpy._rw_prefs = (persistent.texto_maior, _preferences.text_cps, _preferences.transitions)
        if not screen "main_menu":
            run MainMenu(confirm=False)
        pause until screen "main_menu"

    after testcase:
        python hide:
            persistent.texto_maior, _preferences.text_cps, _preferences.transitions = renpy._rw_prefs
            del renpy._rw_prefs

    testcase chat_offline_sem_rede:
        run Start()
        pause until screen "say"
        $ chosen_job = "startup"
        $ amigo_selecionado = "st_mentora"
        run Jump("chat_amigo")
        advance until screen "chat_with_backend"
        type "Oi, tudo bem?"
        keysym "K_RETURN"
        pause 0.2
        assert eval len(chat_history) == 2 and tuple(chat_history[0]) == ("user", "Oi, tudo bem?")
        assert eval chat_history[1][0] == "assistant" and chat_history[1][1]
        assert eval not is_waiting and pending_response is None
        click "Fechar"
        pause 0.2
        assert not screen "chat_with_backend"

    testcase nome_vazio_vira_alex:
        run Start()
        advance until screen "input"
        keysym "K_RETURN"
        advance until screen "choice"
        assert eval player_name == "Alex"
        click "Feminino"
        advance until eval player_gender == "Feminino"
        assert eval player_age == ""

    testcase nome_sem_tags:
        run Start()
        advance until screen "input"
        type "Ana [x]\\"
        keysym "K_RETURN"
        advance until screen "choice"
        assert eval player_name == "Ana x"

    testcase preferencias_acessibilidade:
        run ShowMenu("preferences")
        pause until screen "preferences"
        pause until "Português"
        run SetField(persistent, "texto_maior", False)
        click id "pref_texto_maior"
        assert eval persistent.texto_maior
        run SetField(_preferences, "text_cps", 40)
        click id "pref_texto_instantaneo"
        assert eval _preferences.text_cps == 0
        run SetField(_preferences, "transitions", 2)
        click id "pref_sem_transicoes"
        assert eval _preferences.transitions == 0
        keysym "K_ESCAPE"
        pause 0.2
        assert not screen "preferences"

    testcase texto_maior_em_falas_e_escolhas:
        $ persistent.texto_maior = True
        run Start()
        pause until screen "say"
        assert eval texto_maior_ativo()
        run Jump("rw_teste_planejamento")
        advance until screen "choice"
        assert eval renpy.get_widget("choice", "choice_scroll") is not None
        keysym "K_DOWN"
        keysym "K_RETURN"
        pause 0.2
        assert eval len(planejamento_sel) == 1

    testcase resumo_do_epilogo:
        run Start()
        pause until screen "say"
        $ chosen_job = "saude"
        $ registrar("saude_reg_ciclo")
        $ decisao("rw_d1", True)
        $ inventario.append("medalha_estudioso")
        run Jump("scene_epilogo_conquistas_final")
        advance until screen "resumo_rota"
        assert eval "1 de 8" in renpy.get_widget("resumo_rota", "resumo_registros").text[0]
        assert eval [a["id"] for a in route_achievements() if achievement_unlocked(a)] == ["medalha_estudioso"]
        keysym "K_PAGEDOWN"
        click id "resumo_continuar"
        pause 0.2
        assert not screen "resumo_rota"
