# exercicio_escrita (guarda, escapa e retoma) e atividade_planejamento
# (cobertura e revisão).
testsuite atividades:
    before testcase:
        if not screen "main_menu":
            run MainMenu(confirm=False)
        pause until screen "main_menu"
        run Start()
        pause until screen "say"

    testcase escrita_guarda_e_retoma:
        run Jump("rw_teste_escrita")
        advance until screen "escrita_input"
        type "Quem cancela a reserva"
        keysym "K_RETURN"
        pause until eval escrita_atual.get("req") == "Quem cancela a reserva"
        pause 0.2
        type "Dado X, quando Y, entao Z."
        keysym "K_RETURN"
        pause until screen "escrita_revisao"
        click id "escrita_marca_0"
        click id "escrita_marca_1"
        click id "escrita_marca_2"
        assert eval escrita_marcas == [True, True, True, False]
        click id "escrita_marca_3"
        click id "escrita_confirmar"
        advance until "Fim do teste de escrita"
        assert eval escritas["rw_teste"] == {"req": "Quem cancela a reserva", "crit": "Dado X, quando Y, entao Z.", "checks": 4, "status": "confirmado"}
        assert eval resumo_escritas() == (1, 0)
        # Retoma: cada campo começa com o texto anterior.
        run Jump("rw_teste_escrita")
        advance until screen "escrita_input"
        assert eval renpy.get_widget("escrita_input", "input").content == "Quem cancela a reserva"
        keysym "K_RETURN"
        pause until eval renpy.get_widget("escrita_input", "input") is not None and renpy.get_widget("escrita_input", "input").content.startswith("Dado X")
        keysym "K_RETURN"
        pause until screen "escrita_revisao"
        assert eval escrita_marcas == [False, False, False, False]
        click id "escrita_pendente"
        advance until "Fim do teste de escrita"
        assert eval escritas["rw_teste"]["status"] == "pendente" and escritas["rw_teste"]["checks"] == 0
        assert eval escritas["rw_teste"]["req"] == "Quem cancela a reserva"

    testcase escrita_escapa_tags:
        # O teste não digita "{", então o rascunho começa salvo com tags.
        $ escritas["rw_teste"] = {"req": escapar_texto("Quem {b}cancela{/b} [x]"), "crit": "", "checks": 0, "status": "pendente"}
        assert eval escritas["rw_teste"]["req"] == "Quem {{b}cancela{{/b} [[x]"
        run Jump("rw_teste_escrita")
        advance until screen "escrita_input"
        assert eval renpy.get_widget("escrita_input", "input").content == "Quem {b}cancela{/b} [x]"
        keysym "K_RETURN"
        pause 0.2
        type "Resultado [y]"
        keysym "K_RETURN"
        pause until screen "escrita_revisao"
        click id "escrita_pendente"
        advance until "Fim do teste de escrita"
        assert eval escritas["rw_teste"]["req"] == "Quem {{b}cancela{{/b} [[x]"
        assert eval escritas["rw_teste"]["crit"] == "Resultado [[y]"

    testcase confirmar_exige_quatro_pontos:
        run Jump("rw_teste_escrita")
        advance until screen "escrita_input"
        type "Requisito curto."
        keysym "K_RETURN"
        pause until eval escrita_atual.get("req") == "Requisito curto."
        pause 0.2
        keysym "K_RETURN"
        pause until screen "escrita_revisao"
        click id "escrita_confirmar"
        pause 0.2
        assert screen "escrita_revisao"
        click id "escrita_reescrever"
        pause until screen "escrita_input"
        assert eval renpy.get_widget("escrita_input", "input").content == "Requisito curto."

    testcase planejamento_calcula_cobertura:
        run Jump("rw_teste_planejamento")
        advance until screen "choice"
        assert eval planejamento_sel == []
        assert not "Conferir este plano"
        click "Adicionar: Item C extra"
        pause until "Retirar: Item C extra"
        assert not "Conferir este plano"
        click "Adicionar: Item D extra"
        pause until "Conferir este plano"
        assert not "Adicionar:"
        click "Conferir este plano"
        advance until screen "choice"
        assert eval planejamento_resultado["cobertura"] == 0 and planejamentos["rw_plano"]["primeira_cobertura"] == 0
        click "Revisar os itens escolhidos"
        pause until "Retirar: Item C extra"
        click "Retirar: Item C extra"
        pause until "Adicionar: Item A necessário"
        click "Adicionar: Item A necessário"
        pause until "Conferir este plano"
        click "Conferir este plano"
        advance until screen "choice"
        assert eval planejamento_resultado["cobertura"] == 1 and planejamento_resultado["faltando"] == "Item B necessário"
        click "Revisar os itens escolhidos"
        pause until "Retirar: Item D extra"
        click "Retirar: Item D extra"
        pause until "Adicionar: Item B necessário"
        click "Adicionar: Item B necessário"
        pause until "Conferir este plano"
        click "Conferir este plano"
        advance until screen "choice"
        assert eval planejamento_resultado["cobertura"] == 2
        click "Concluir com este plano"
        advance until "Fim do teste de planejamento"
        assert eval _return == 2
        assert eval planejamentos["rw_plano"] == {"selecionados": [0, 1], "cobertura": 2, "total": 2, "primeira_cobertura": 0}
