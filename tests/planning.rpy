testsuite planning:
    before testcase:
        if not screen "main_menu":
            run MainMenu(confirm=False)
        pause until screen "main_menu"
        run Start()
        run Hide("inv_quick")

    testcase scope_and_revision:
        parameter (job, acceptance, edge) = [("IDT-UFRJ", "Uma reserva das 14h às 15h", "Pergunto se é necessário um intervalo"), ("Startup", "Ao confirmar a exclusão", "O gasto permanece e o total não muda"), ("Empresa legada", "Após o suporte resolver o chamado", "Confirmo se devemos impedir")]
        run SetVariable("chosen_job", job)
        run Jump("scene_2_estagio")
        advance until screen "choice"
        click "Peço que Carlos conte"
        advance until screen "choice"
        click "Pergunto o que Carlos precisa conseguir"
        advance until screen "choice"
        click expression acceptance
        advance until screen "choice"
        click expression edge
        advance until screen "choice"
        click "Planejar a primeira entrega"
        advance until screen "choice"
        assert eval planning_selected == []
        assert not "Conferir este plano"
        click expression ("Adicionar: " + planning_items[2])
        pause until "Retirar:"
        assert eval len(planning_selected) == 1
        assert not "Conferir este plano"
        click expression ("Adicionar: " + planning_items[3])
        pause until "Conferir este plano"
        assert eval len(planning_selected) == 2
        assert not "Adicionar:"
        click "Conferir este plano"
        advance until screen "choice"
        assert eval planning_complete and planning_coverage == 0
        assert eval len(planning_missing) == 2
        click "Revisar os itens"
        pause until "Retirar:"
        assert eval not planning_complete
        click expression ("Retirar: " + planning_items[2])
        pause until "Adicionar:"
        click expression ("Adicionar: " + planning_items[0])
        pause until "Conferir este plano"
        click "Conferir este plano"
        advance until screen "choice"
        assert eval planning_complete and planning_coverage == 1
        assert eval planning_missing == [planning_items[1]]
        click "Revisar os itens"
        pause until "Retirar:"
        click expression ("Retirar: " + planning_items[3])
        pause until "Adicionar:"
        click expression ("Adicionar: " + planning_items[1])
        pause until "Conferir este plano"
        click "Conferir este plano"
        advance until screen "choice"
        assert eval planning_complete and planning_coverage == 2
        assert eval planning_missing == []
        assert eval mission_score == 4 and mission_complete
        click "Concluir a atividade"
        pause until "Planejar a primeira entrega"
        assert eval chosen_job == job
        click "Planejar a primeira entrega"
        advance until screen "choice"
        assert eval planning_selected == [] and not planning_complete
        click "Voltar ao resumo da missão"
        pause until "Planejar a primeira entrega"
        assert eval mission_score == 4
