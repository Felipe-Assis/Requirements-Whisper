# A bancada reutiliza o quadro e a tipografia da campanha, com fontes próprias.
screen exp_investigation():
    zorder 40
    modal True
    use campaign_workspace("Um almoço, dois lançamentos", "GASTOS · compare o comprovante, a lista e a fala de quem pagou."):
        hbox:
            spacing 32
            frame:
                style "artifact_paper" xsize 700 ysize 640
                vbox:
                    spacing 20
                    button:
                        style "artifact_button"
                        background Solid("#fffdf7") hover_background Solid("#fff8e6")
                        padding (30, 24)
                        xfill True ysize 345
                        action Function(lab_ui_apply, exp_inspect, "receipt")
                        id "exp_receipt_hotspot"
                        vbox:
                            spacing 18
                            text "CANTINA · RECIBO C-071" style "artifact_heading" size 32
                            add Solid("#a9b6b5") xsize 580 ysize 2
                            text "terça · 12h14" style "artifact_muted" size 28
                            text "1 almoço" style "artifact_ink" size 38
                            text "R$ 20,00" style "artifact_heading" size 60 color "#286b66"
                            text "Pago por Lia · abrir comprovante" style "artifact_ink" size 27
                    text "Um valor igual também pode ser outra compra. Investigue a origem antes de apagar." style "artifact_muted" size lab_ui_size(28)
            frame:
                style "artifact_paper"
                xsize 1010 ysize 640
                vbox:
                    spacing 14
                    text "Fontes da investigação" style "artifact_heading" size 34
                    hbox:
                        spacing 10
                        for source_id, source_label in (("receipt", "Comprovante"), ("ledger", "Lançamentos"), ("lia", "Ouvir Lia")):
                            textbutton (source_label + (" · lido" if source_id in exp_sources else "")):
                                style "artifact_button" text_size 25
                                action Function(lab_ui_apply, exp_inspect, source_id)
                                selected exp_source == source_id
                                id ("exp_source_" + source_id)
                    frame:
                        style "artifact_card" xfill True ysize 365
                        viewport:
                            mousewheel True draggable True arrowkeys True pagekeys True scrollbars "vertical"
                            vbox:
                                spacing 18 xsize 870
                                if exp_source:
                                    text EXP_SOURCES[exp_source][0] style "artifact_heading" size 31
                                    text EXP_SOURCES[exp_source][1] style "artifact_ink" size lab_ui_size(29)
                                else:
                                    text "Selecione uma fonte para ler. O recibo à esquerda também abre a primeira fonte." style "artifact_muted" size 30
                    text (str(len(exp_sources)) + " de 3 fontes registradas · " + ("Lia confirmou que AL-18 repete o mesmo pagamento." if "lia" in exp_sources else "Confirme com Lia se os registros representam o mesmo pagamento.")) style "artifact_muted" size 25
    use campaign_footer(exp_feedback)
    use lab_continue("Experimentar a versão atual", Return("continue"), len(exp_sources) == 3, "exp_investigate_continue")


screen exp_planning():
    zorder 40
    modal True
    use campaign_workspace("O que cabe nesta rodada?", "GASTOS · as duas prioridades têm valor, mas consomem a mesma rodada da equipe."):
        frame:
            style "artifact_paper" xfill True ysize 644
            viewport:
                ysize 600 xfill True mousewheel True draggable True arrowkeys True pagekeys True scrollbars "vertical"
                vbox:
                    spacing 25
                    text "Lia quer confiar no saldo. Também gostaria de parar de digitar compras do banco." style "artifact_ink" size lab_ui_size(31)
                    hbox:
                        spacing 30
                        button:
                            style "artifact_button" xsize 835 ysize 330
                            action Return("core") id "exp_plan_core"
                            vbox:
                                spacing 18
                                text "Corrigir a lista primeiro" style "artifact_heading" size 36
                                text "Confirmar, cancelar, recalcular e desfazer. Júlio revisa com você; Lia valida os exemplos." style "artifact_ink" size lab_ui_size(29)
                                text "Entrega nesta rodada. Acesso bancário fica para pesquisa com responsável e retorno." style "artifact_muted" size 27
                        button:
                            style "artifact_button" xsize 835 ysize 330
                            action Return("bank") id "exp_plan_bank"
                            vbox:
                                spacing 18
                                text "Investigar o banco primeiro" style "artifact_heading" size 36
                                text "Júlio verifica consentimento, formato dos dados e acesso de testes. A resposta pode mudar o escopo." style "artifact_ink" size lab_ui_size(29)
                                text "Sem prometer integração. A correção da lista fica adiada; Lia confere o caderno no intervalo." style "artifact_muted" size 27
                    text "Critério da correção: Cancelar mantém R$ 100,00; Confirmar AL-18 leva a R$ 80,00; Desfazer recupera a lista. O transporte continua." style "artifact_muted" size lab_ui_size(28)
    use campaign_footer(exp_feedback)

screen exp_implementation():
    zorder 40
    modal True
    use campaign_workspace("Da falha à mudança", "GASTOS · aplique uma mudança por vez e leve a candidata para revisão da equipe."):
        frame:
            style "artifact_paper" xfill True ysize 640
            viewport:
                ysize 600 xfill True mousewheel True draggable True arrowkeys True pagekeys True scrollbars "vertical"
                vbox:
                    spacing 16
                    text "Antes: a pergunta de confirmação já removia a linha. Cancelar chegava tarde." style "artifact_ink" size lab_ui_size(29)
                    for change_id in ("defer", "total", "undo"):
                        button:
                            style "artifact_button" xfill True yminimum 120
                            selected_background Solid("#c5e2d9")
                            action Function(lab_ui_apply, exp_apply_change, change_id)
                            selected change_id in exp_changes
                            id ("exp_change_" + change_id)
                            vbox:
                                spacing 10
                                text (("Aplicada · " if change_id in exp_changes else "Aplicar · ") + EXP_CHANGES[change_id][0]) style "artifact_heading" size 31
                                text EXP_CHANGES[change_id][1] style "artifact_ink" size lab_ui_size(27)
                    text "Júlio confere o ponto da alteração e os IDs. Você demonstra o comportamento com os dados de Lia." style "artifact_muted" size 26
    use campaign_footer(exp_feedback)
    use lab_continue("Revisar com Júlio", Return("review"), len(exp_changes) == 3, "exp_implementation_continue")

# A ordem montada pelo jogador continua no produto que Lia experimenta.
screen exp_product_module(section):
    if section == "balance":
        frame:
            style "artifact_card" xfill True
            hbox:
                spacing 24
                vbox:
                    spacing 4
                    text "TOTAL REGISTRADO" style "artifact_muted" size 22
                    text ("Total: " + exp_money(exp_total())) style "artifact_heading" size 42 id "exp_total"
                text (str(len(exp_rows)) + " lançamentos na amostra") style "artifact_muted" size 23 yalign 0.5
    elif section == "records":
        vbox:
            spacing 0
            frame:
                background Solid("#dce6e5") padding (16, 12) xfill True
                hbox:
                    spacing 12
                    for caption, width in (("#", 36), ("A · ID", 100), ("B · DESCRIÇÃO", 290), ("C · VALOR", 160), ("D · AÇÃO", 180)):
                        fixed:
                            xsize width ysize 32
                            text caption style "artifact_muted" size 22
            for row_number, row in enumerate(exp_rows, 1):
                frame:
                    background Solid("#ffffff") padding (16, 10) xfill True
                    hbox:
                        spacing 12 yalign 0.5
                        fixed:
                            xsize 36 ysize 66
                            text str(row_number) style "artifact_muted" size 23 yalign 0.5
                        fixed:
                            xsize 100 ysize 66
                            text row["code"] style "artifact_muted" size 26 yalign 0.5
                        fixed:
                            xsize 290 ysize 66
                            text row["name"] style "artifact_ink" size 27 xmaximum 290 yalign 0.5
                        fixed:
                            xsize 160 ysize 66
                            text exp_money(row["amount"]) style "artifact_ink" size 27 yalign 0.5
                        textbutton "Remover":
                            style "artifact_button" text_size 24
                            sensitive not exp_pending
                            action Function(lab_ui_apply, exp_request_delete, row["id"])
                            id ("exp_remove_" + row["id"])
                add Solid("#d5ddda") xsize 966 ysize 1
    elif section == "actions":
        hbox:
            spacing 12
            if exp_built:
                textbutton "Desfazer":
                    style "artifact_button" text_size 26
                    sensitive exp_undo_rows is not None and not exp_pending
                    action Function(lab_ui_apply, exp_undo) id "exp_undo"
            textbutton "Repor amostra de teste":
                style "artifact_button" text_size 24 sensitive not exp_pending
                action Function(lab_ui_apply, exp_restore_fixture) id "exp_restore"

screen exp_ledger():
    zorder 40
    modal True
    use campaign_workspace(("Candidata corrigida · ensaio" if exp_built else "Candidata antiga · reproduza a falha"), "GASTOS · amostra de teste. Você pode errar, desfazer e repetir sem alterar os gastos reais de Lia."):
        viewport:
            id "exp_ledger_scroll"
            ysize 615 xfill True
            mousewheel True draggable True arrowkeys True pagekeys True scrollbars "vertical"
            hbox:
                spacing 32
                frame:
                    style "artifact_paper" xsize 1010
                    vbox:
                        spacing 16
                        use artifact_bar("Lia · controle de gastos", "Amostra de teste · valores em reais")
                        for section in campaign_layout("expenses"):
                            use exp_product_module(section)
                frame:
                    style "artifact_paper" xsize 650
                    vbox:
                        spacing 17
                        if exp_built:
                            text "Demonstre os três comportamentos" style "artifact_heading" size 33
                            text (("Feito" if "cancel" in exp_checks else "A fazer") + " · abrir Remover e Cancelar sem perder dados.") style "artifact_ink" size lab_ui_size(27)
                            text (("Feito" if "confirm" in exp_checks else "A fazer") + " · confirmar uma remoção e conferir o total.") style "artifact_ink" size lab_ui_size(27)
                            text (("Feito" if "undo" in exp_checks else "A fazer") + " · desfazer a última alteração.") style "artifact_ink" size lab_ui_size(27)
                            text "Finalize só sem AL-18: AL-17, livro e transporte devem somar R$ 80,00." style "artifact_muted" size lab_ui_size(27)
                            text "Desfazer recupera a última alteração. Repor amostra de teste restaura todos os dados e reinicia os três critérios." style "artifact_muted" size 24
                            text "Extra · corrigir o transporte na amostra" style "artifact_heading" size 28
                            hbox:
                                spacing 12
                                textbutton "Testar R$ 0,00":
                                    style "artifact_button" text_size 25 sensitive not exp_pending
                                    action Function(lab_ui_apply, exp_edit, "bus", 0) id "exp_edit_zero"
                                textbutton "Editar para R$ 30,00":
                                    style "artifact_button" text_size 25 sensitive not exp_pending
                                    action Function(lab_ui_apply, exp_edit, "bus", 3000) id "exp_edit_positive"
                            text "Depois da edição, use Desfazer para voltar ao valor comprovado. Valor zero deve ser recusado." style "artifact_muted" size 24
                            textbutton "Registrar ensaio pendente":
                                style "artifact_button" text_size 24 sensitive not exp_pending
                                action Return("pending") id "exp_demo_pending"
                        else:
                            text "Lia ia cancelar a operação" style "artifact_heading" size 35
                            text "1. Abra Remover em AL-18.\n2. Observe a lista e o total.\n3. Escolha Cancelar.\n4. Confira se a linha voltou." style "artifact_ink" size lab_ui_size(31)
                            text "Esperado: Cancelar mantém os quatro lançamentos e R$ 100,00. Nesta candidata, o que aconteceu?" style "artifact_muted" size lab_ui_size(29)
                            if exp_before_reproduced:
                                text "Falha registrada: Cancelar perdeu uma linha." style "artifact_ink" color "#286b66" size 28
    use campaign_footer(exp_feedback)
    if exp_built:
        use lab_continue("Entregar a correção", Return("deliver"), exp_demo_ready(), "exp_demo_continue")
    else:
        use lab_continue("Levar a falha para a equipe", Return("continue"), exp_before_reproduced and not exp_pending, "exp_before_continue")
    if exp_pending:
        add Solid("#06121cce")
        frame:
            style "artifact_paper"
            xpos 425 ypos 335 xsize 1070 yminimum 350
            vbox:
                spacing 24
                $ pending_row = next(row for row in exp_fixture() if row["id"] == exp_pending)
                text ("Remover " + pending_row["code"] + " · " + pending_row["name"] + "?") style "artifact_heading" size 38
                text ("A lista ainda está intacta. Só Confirmar executa a remoção." if exp_built else "Observe a lista ao fundo. Esta é a versão anterior, em teste.") style "artifact_ink" size lab_ui_size(29)
                hbox:
                    spacing 25
                    textbutton "Cancelar":
                        style "artifact_button" text_size 30
                        action Function(lab_ui_apply, exp_cancel_delete) default_focus True id "exp_cancel"
                    textbutton "Confirmar remoção":
                        style "artifact_primary" text_size 30
                        action Function(lab_ui_apply, exp_confirm_delete) id "exp_confirm"


screen exp_final():
    zorder 40
    modal True
    $ result = exp_result()
    use campaign_workspace("O retorno de Lia", "GASTOS · o resultado corresponde à entrega e aos compromissos desta rodada."):
        frame:
            style "artifact_paper" xfill True ysize 644
            viewport:
                ysize 600 xfill True mousewheel True draggable True arrowkeys True pagekeys True scrollbars "vertical"
                vbox:
                    spacing 28
                    text ({"waiting": "A pesquisa tem dono; a correção está pendente", "pending": "O ensaio ainda precisa continuar", "recovered": "Errar no ensaio ajudou a proteger os dados", "reliable": "O saldo voltou a fazer sentido"}[result["outcome"]]) style "artifact_heading" size 43 color "#286b66" xmaximum 1650
                    text result["summary"] style "artifact_ink" size lab_ui_size(33) xmaximum 1640
                    frame:
                        style "artifact_card" xfill True
                        vbox:
                            spacing 15
                            text "Próximo compromisso" style "artifact_heading" size 32
                            text result["pending"] style "artifact_ink" size lab_ui_size(29) xmaximum 1570
                    text ("Extra registrado: edição positiva aceita e total recalculado na amostra." if exp_sidequest else "A edição positiva ficou fora do ensaio desta rodada.") style "artifact_muted" size lab_ui_size(27)
                    text ("A equipe renegociou a prioridade com Lia antes de retomar a correção." if exp_renegotiated else "Integração bancária continua dependendo de consentimento e acesso de testes.") style "artifact_muted" size lab_ui_size(27)
    use campaign_footer("Fontes, resultado e pendências ficam na pasta de projetos.")
    use lab_continue("Voltar à pasta de projetos", Return("hub"), True, "exp_final_hub")
