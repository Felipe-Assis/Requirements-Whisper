# As escolhas passam pela interface e pelo roteiro reais, incluindo o feedback.
testsuite mission:
    before testcase:
        if not screen "main_menu":
            run MainMenu(confirm=False)
        pause until screen "main_menu"
        run Start()
        run Hide("inv_quick")

    testcase success_and_replay:
        parameter (job, acceptance, edge, evidence) = [("IDT-UFRJ", "Uma reserva das 14h às 15h", "Pergunto se é necessário um intervalo", "15h10"), ("Startup", "Ao confirmar a exclusão", "O gasto permanece e o total não muda", "R$ 100"), ("Empresa legada", "Após o suporte resolver o chamado", "Confirmo se devemos impedir", "descrição estiver vazia")]
        run SetVariable("chosen_job", job)
        run Jump("scene_2_estagio")
        advance until screen "choice"
        click "Peço que Carlos conte"
        advance until screen "choice"
        assert eval mission_score == 1
        click "Pergunto o que Carlos precisa conseguir"
        advance until screen "choice"
        assert eval mission_score == 2
        click expression acceptance
        advance until screen "choice"
        assert eval mission_score == 3
        click expression edge
        advance until screen "choice"
        assert eval mission_complete and mission_score == 4
        assert eval mission_elicitation and mission_ambiguity and mission_acceptance and mission_edge_case
        assert eval evidence in mission_edge_criterion
        click "Rever o requisito"
        advance until "Caso limite:"
        assert expression evidence
        advance until screen "choice"
        click "Refazer a missão"
        advance until screen "choice"
        assert eval chosen_job == job
        assert eval mission_score == 0 and not mission_complete
        assert eval not mission_elicitation and not mission_ambiguity and not mission_acceptance and not mission_edge_case
        assert eval mission_edge_criterion == ""

    testcase guided_revision:
        parameter (job, acceptance, edge) = [("IDT-UFRJ", "O calendário deve ter cores", "Permito sempre"), ("Startup", "O aplicativo deve ter um painel", "O gasto some"), ("Empresa legada", "A pessoa solicitante deve receber", "Preencho automaticamente")]
        run SetVariable("chosen_job", job)
        run Jump("scene_2_estagio")
        advance until screen "choice"
        click "Pergunto qual tecnologia"
        advance until screen "choice"
        assert "Carlos, você pode contar"
        assert eval mission_score == 0
        click "Carlos, você pode contar"
        advance until screen "choice"
        click "Registro 'o sistema deve ser fácil'"
        advance until screen "choice"
        assert "O que precisa acontecer"
        click "O que precisa acontecer"
        advance until screen "choice"
        click expression acceptance
        advance until screen "choice"
        assert "Registrar a situação inicial"
        click "Registrar a situação inicial"
        advance until screen "choice"
        click expression edge
        advance until screen "choice"
        assert "Registro o caso limite"
        click "Registro o caso limite"
        advance until "Com apoio, você reformulou"
        assert eval mission_complete and mission_score == 0
        assert eval not mission_elicitation and not mission_ambiguity and not mission_acceptance and not mission_edge_case
        advance until screen "choice"
        click "Experimentar outra vaga"
        advance until screen "choice"
        click "Startup — ajudar estudantes"
        advance until screen "choice"
        assert eval chosen_job == "Startup"
        assert eval mission_context == "registro de gastos de estudantes"
        assert eval mission_score == 0 and not mission_complete

    testcase alternative_distractors:
        run SetVariable("chosen_job", "Empresa legada")
        run Jump("scene_2_estagio")
        advance until screen "choice"
        click "Confirmo se Carlos gostaria"
        advance until screen "choice"
        click "Carlos, você pode contar"
        advance until screen "choice"
        click "Troco 'fácil' por 'moderno'"
        advance until screen "choice"
        click "O que precisa acontecer"
        advance until screen "choice"
        click "O suporte deve conseguir clicar"
        advance until screen "choice"
        click "Registrar a situação inicial"
        advance until screen "choice"
        click "Mudo o estado"
        advance until screen "choice"
        click "Registro o caso limite"
        advance until screen "choice"
        assert eval mission_complete and mission_score == 0
        click "Encerrar e voltar"
        pause until screen "main_menu"
        assert screen "main_menu"
