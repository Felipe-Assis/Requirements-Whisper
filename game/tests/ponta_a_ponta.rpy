# Percurso completo de cada rota com o piloto automático (autopiloto.rpy),
# modo determinístico "primeira": de label start até o menu final do epílogo.
# Qualquer exceção no caminho falha o teste (o motor de testes a captura).
# Para outros modos e para registrar todos os erros de uma vez, use
# tests/autopiloto.ps1.
testsuite ponta_a_ponta:
    before testcase:
        if not screen "main_menu":
            run MainMenu(confirm=False)
        pause until screen "main_menu"

    after testcase:
        $ autopiloto.desligar()

    testcase rota_completa:
        parameter rota = ["saude", "startup", "corporativo"]
        $ autopiloto.ligar(rota, "primeira")
        run Start()
        pause until eval autopiloto.terminou() timeout 600
        assert eval autopiloto.relatorio()["motivo"] == "ok"
        assert eval autopiloto.relatorio()["chosen_job"] == rota
        assert eval autopiloto.relatorio()["cenas_faltando"] == []
        assert eval autopiloto.relatorio()["final_cena"] in ("excelente", "bom", "ok")
        assert eval autopiloto.relatorio()["final_cena"] == autopiloto.relatorio()["final_rota"]
        assert eval autopiloto.relatorio()["resumo_registros"] == "Notebook: %d de 8 registros" % registros_contagem()[0]
        assert eval registros_contagem()[0] > 0
        assert eval autopiloto.relatorio()["erros"] == []
        assert eval autopiloto.relatorio()["imagens_nao_encontradas"] == []
        assert eval autopiloto.relatorio()["audios_ausentes"] == []
        assert eval [i["arquivo"] for i in autopiloto.relatorio()["imagens_ausentes"]] == []

    # Saúde pelas últimas opções, com o ramo raro da scene_18: abordagem
    # inovadora (fica tarde) e virar a noite, em vez de descansar.
    testcase saude_virar_a_noite:
        $ autopiloto.ligar("saude", "ultima", forcar=["Virar a noite"])
        run Start()
        pause until eval autopiloto.terminou() timeout 600
        assert eval autopiloto.relatorio()["motivo"] == "ok"
        assert eval autopiloto.relatorio()["cenas_faltando"] == []
        assert eval any(c.startswith("Virar a noite") for l, c in autopiloto.relatorio()["escolhas"])
        assert eval "scene_18_2_codificacao_final" not in autopiloto.ap.labels
        assert eval autopiloto.relatorio()["final_cena"] == autopiloto.relatorio()["final_rota"]
        assert eval autopiloto.relatorio()["erros"] == [] and autopiloto.relatorio()["imagens_ausentes"] == []

    # Conversar pelo celular no meio de uma cena não pode encerrar a cena:
    # depois do chat, a st_03 continua na cozinha.
    testcase chat_pela_cena_continua_a_cena:
        run Start()
        pause until screen "say"
        $ chosen_job = "startup"
        $ contato_st_mentora = True
        $ set_available("st_mentora")
        $ renpy.pop_call()
        run Jump("st_03_casa_sem1")
        advance until screen "contacts_screen"
        click "Tainá"
        advance until screen "chat_with_backend"
        click "Fechar"
        advance until "colega de república"
