testsuite journey:
    before testcase:
        if not screen "main_menu":
            run MainMenu(confirm=False)
        pause until screen "main_menu"
        run Start()
        run Hide("inv_quick")

    after testcase:
        $ renpy.unlink_save("qa-journey")

    testcase complete_contexts:
        parameter (job, acceptance, edge) = [("IDT-UFRJ", "Uma reserva das 14h às 15h", "Pergunto se é necessário um intervalo"), ("Startup", "Ao confirmar a exclusão", "O gasto permanece e o total não muda"), ("Empresa legada", "Após o suporte resolver o chamado", "Confirmo se devemos impedir")]
        run SetVariable("chosen_job", job)
        run Jump("scene_2_estagio")
        advance until screen "choice"
        assert eval mission_stage == 0
        click "Peço que Carlos conte"
        advance until screen "choice"
        assert eval mission_stage == 1
        click "Pergunto o que Carlos precisa conseguir"
        advance until screen "choice"
        assert eval mission_stage == 2
        click expression acceptance
        advance until screen "choice"
        assert eval mission_stage == 3
        click expression edge
        advance until screen "choice"
        assert eval mission_stage == 4 and mission_complete
        click "Continuar: negociar"
        advance until screen "choice"
        click "Incluir o novo pedido"
        advance until screen "choice"
        assert eval not negotiation_complete
        click "Recusar a mudança"
        advance until screen "choice"
        click "Investigar a integração agora"
        advance until screen "choice"
        assert eval negotiation_option == "investigar_agora"
        click "Rever o acordo"
        advance until screen "choice"
        click "Entregar a regra e o caso limite primeiro"
        advance until screen "choice"
        $ renpy.take_screenshot()
        $ renpy.save("qa-journey")
        run SetVariable("negotiation_agreement", "estado alterado")
        $ renpy.load("qa-journey")
        pause until screen "choice"
        assert eval "próxima rodada" in negotiation_agreement
        click "Confirmar o acordo"
        advance until screen "transfer_input"
        keysym "K_n"
        assert not screen "learning_notebook"
        keysym "K_BACKSPACE"
        type "A pessoa autorizada deve concluir a acao conforme a condicao combinada."
        keysym "K_RETURN"
        pause until eval transfer_requirement != ""
        assert eval transfer_requirement == "A pessoa autorizada deve concluir a acao conforme a condicao combinada."
        pause 0.1
        type "Dado o registro inicial, ao confirmar a acao, conferir o estado e o resultado."
        keysym "K_RETURN"
        pause until screen "transfer_review"
        click "Continuar a autoavalia"
        advance until screen "choice"
        assert eval negotiation_complete and not journey_complete
        click "Reescrever para esclarecer"
        pause until screen "transfer_input"
        keysym "K_RETURN"
        pause until screen "transfer_input"
        keysym "K_RETURN"
        pause until screen "transfer_review"
        click "Continuar a autoavalia"
        advance until screen "choice"
        click "Conferi os pontos"
        advance until screen "choice"
        assert eval journey_complete and transfer_complete
        assert eval transfer_requirement and transfer_criterion
        click "Rever o acordo da entrega"
        advance until screen "choice"
        click "Refazer a missão"
        advance until screen "choice"
        assert eval not journey_complete and not transfer_complete and not negotiation_complete
        assert eval transfer_requirement == "" and transfer_criterion == "" and negotiation_agreement == ""
        assert eval mission_stage == 0 and mission_score == 0

    testcase postponed_transfer_and_exit:
        run SetVariable("chosen_job", "Startup")
        run Jump("scene_2_estagio")
        advance until screen "choice"
        run SetVariable("mission_complete", True)
        run Jump("mission_review_actions")
        pause until screen "choice"
        click "Continuar: negociar"
        advance until screen "choice"
        click "Investigar a integração agora"
        advance until screen "choice"
        click "Confirmar o acordo"
        advance until screen "transfer_input"
        keysym "K_RETURN"
        pause until screen "transfer_input"
        keysym "K_RETURN"
        pause until screen "transfer_review"
        click "Continuar a autoavalia"
        advance until screen "choice"
        assert not "Conferi os pontos"
        click "Continuar sem registrar"
        advance until screen "choice"
        assert eval journey_complete and not transfer_complete and negotiation_complete
        click "Encerrar e voltar"
        pause until screen "main_menu"
    testcase long_draft_large_text:
        $ journey_previous_large = persistent.rw_large_text
        $ persistent.rw_large_text = True
        $ transfer_requirement = "[literal] {i} " + "WWW " * 70
        $ transfer_criterion = "[literal] {b} " + "WWW " * 95
        $ journey_expected_requirement = transfer_requirement.strip()
        $ journey_expected_criterion = transfer_criterion.strip()
        run Jump("transfer_write")
        pause until screen "transfer_input"
        keysym "K_n"
        assert not screen "learning_notebook"
        keysym "K_BACKSPACE"
        screenshot "review/journey_input_large.png"
        keysym "K_RETURN"
        pause until eval transfer_requirement == journey_expected_requirement
        pause 0.1
        keysym "K_RETURN"
        pause until screen "transfer_review"
        assert eval transfer_requirement == journey_expected_requirement
        assert eval transfer_criterion == journey_expected_criterion
        assert eval renpy.get_widget("transfer_review", "transfer_review_scroll").yadjustment.range > 0
        screenshot "review/journey_review_large.png"
        keysym "K_PAGEDOWN"
        pause 0.2
        assert eval renpy.get_widget("transfer_review", "transfer_review_scroll").yadjustment.value > 0
        screenshot "review/journey_review_scrolled.png"
        click "Continuar a autoavalia"
        advance until screen "choice"
        $ persistent.rw_large_text = journey_previous_large
