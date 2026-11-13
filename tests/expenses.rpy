# Estado salvável e jornadas por IDs, sem substituir a lógica de domínio.
label exp_test_checkpoint:
    $ exp_reset()
    $ exp_inspect("receipt")
    $ exp_inspect("ledger")
    $ exp_inspect("lia")
    $ exp_set_plan("core")
    $ exp_apply_change("defer")
    $ exp_apply_change("total")
    $ exp_apply_change("undo")
    $ exp_build("pair")
    "A candidata está pronta para o teste de confirmação."
    menu:
        "Abrir confirmação no teste":
            $ exp_request_delete("meal18")
        "Manter lista intacta no teste":
            pass
    call screen exp_ledger
    return

testsuite expenses:
    before testcase:
        if not screen "main_menu":
            run MainMenu(confirm=False)
        pause until screen "main_menu"

    after testcase:
        $ renpy.unlink_save("qa-expenses-pending")

    testcase investigate_build_deliver_and_return:
        run Start("expenses_campaign")
        advance until screen "exp_investigation"
        click id "exp_receipt_hotspot"
        click id "exp_source_ledger"
        click id "exp_source_lia"
        assert eval set(exp_sources) == {"receipt", "ledger", "lia"}
        click id "exp_investigate_continue"
        pause until screen "campaign_app_builder"
        click id "builder_select_records"
        click id "builder_slot_0"
        assert eval campaign_layout("expenses")[0] == "records"
        click id "campaign_builder_continue"
        advance until screen "exp_ledger"
        assert eval not exp_built and exp_total() == 10000
        click id "exp_remove_meal18"
        assert eval exp_pending == "meal18" and exp_total() == 8000
        click id "exp_cancel"
        assert eval exp_before_reproduced and exp_total() == 8000
        click id "exp_before_continue"
        advance until screen "exp_planning"
        click id "exp_plan_core"
        advance until screen "exp_implementation"
        click id "exp_change_defer"
        click id "exp_change_total"
        click id "exp_change_undo"
        click id "exp_implementation_continue"
        advance until screen "choice"
        click "Parear com Júlio e explicar cada mudança"
        advance until screen "exp_ledger"
        assert eval exp_built and exp_total() == 10000 and exp_reviewer == "pair"
        click id "exp_remove_meal18"
        assert eval exp_total() == 10000
        click id "exp_cancel"
        assert eval exp_total() == 10000 and "cancel" in exp_checks
        keysym "K_PAGEDOWN"
        assert eval renpy.get_widget("exp_ledger", "exp_ledger_scroll").yadjustment.value > 0
        click id "exp_remove_bus"
        click id "exp_confirm"
        assert eval exp_total() == 8000 and not exp_demo_ready()
        move id "exp_ledger_scroll"
        keysym "K_PAGEDOWN"
        click id "exp_undo"
        assert eval exp_recovered and exp_total() == 10000
        move id "exp_ledger_scroll"
        keysym "K_PAGEDOWN"
        click id "exp_edit_zero"
        assert eval exp_total() == 10000 and "inválido" in exp_feedback
        click id "exp_edit_positive"
        assert eval exp_total() == 11000 and exp_sidequest
        move id "exp_ledger_scroll"
        keysym "K_PAGEDOWN"
        click id "exp_undo"
        assert eval exp_total() == 10000
        move id "exp_ledger_scroll"
        keysym "K_PAGEUP"
        click id "exp_remove_meal18"
        click id "exp_confirm"
        assert eval exp_demo_ready() and exp_total() == 8000
        click id "exp_demo_continue"
        advance until screen "exp_final"
        assert eval exp_delivered and exp_outcome() == "recovered"
        assert eval campaign_memory("expenses")["total"] == 8000
        assert eval campaign_memory("expenses")["layout"][0] == "records"
        click id "exp_final_hub"
        advance until screen "campaign_hub_screen"

    testcase banking_research_remains_pending:
        run Start("expenses_campaign")
        advance until screen "exp_investigation"
        $ exp_set_plan("bank")
        run Jump("exp_bank_priority")
        advance until screen "choice"
        click "Manter a pesquisa e registrar a correção pendente"
        advance until screen "exp_final"
        assert eval exp_outcome() == "waiting" and not exp_delivered
        assert eval campaign_memory("expenses")["outcome"] == "waiting"
        assert eval "acesso" in campaign_memory("expenses")["pending"]

    testcase bank_priority_can_be_renegotiated:
        run Start("expenses_campaign")
        advance until screen "exp_investigation"
        $ exp_set_plan("bank")
        run Jump("exp_bank_priority")
        advance until screen "choice"
        click "Retomar a correção com Lia e Júlio"
        advance until screen "exp_implementation"
        assert eval exp_plan == "core" and exp_renegotiated and not exp_delivered

    testcase save_restores_pending_confirmation_and_undo:
        run Start("exp_test_checkpoint")
        advance until screen "choice"
        click "Abrir confirmação no teste"
        pause until screen "exp_ledger"
        assert eval exp_pending == "meal18" and exp_total() == 10000
        $ renpy.take_screenshot()
        $ renpy.save("qa-expenses-pending")
        click id "exp_confirm"
        assert eval exp_total() == 8000 and exp_undo_rows is not None
        $ renpy.load("qa-expenses-pending")
        pause until screen "exp_ledger"
        assert eval exp_pending == "meal18" and exp_total() == 10000 and exp_undo_rows is None
        click id "exp_cancel"
        assert eval exp_total() == 10000 and exp_pending == ""
        click id "exp_remove_meal18"
        click id "exp_confirm"
        $ renpy.take_screenshot()
        $ renpy.save("qa-expenses-pending")
        move id "exp_ledger_scroll"
        keysym "K_PAGEDOWN"
        click id "exp_undo"
        assert eval exp_total() == 10000
        $ renpy.load("qa-expenses-pending")
        pause until screen "exp_ledger"
        assert eval exp_total() == 8000 and exp_undo_rows is not None
        move id "exp_ledger_scroll"
        keysym "K_PAGEDOWN"
        click id "exp_undo"
        assert eval exp_total() == 10000

    testcase two_removals_can_restore_the_corrected_sandbox:
        run Start("exp_test_checkpoint")
        advance until screen "choice"
        click "Manter lista intacta no teste"
        pause until screen "exp_ledger"
        move id "exp_ledger_scroll"
        keysym "K_PAGEDOWN"
        click id "exp_remove_bus"
        click id "exp_confirm"
        click id "exp_remove_book"
        click id "exp_confirm"
        move id "exp_ledger_scroll"
        keysym "K_PAGEDOWN"
        click id "exp_undo"
        assert eval exp_total() == 8000 and not any(row["id"] == "bus" for row in exp_rows)
        assert eval not exp_demo_ready()
        click id "exp_restore"
        assert eval exp_total() == 10000 and exp_checks == [] and exp_built
        assert eval exp_rows == exp_fixture() and exp_undo_rows is None
        move id "exp_ledger_scroll"
        keysym "K_PAGEUP"
        click id "exp_remove_meal18"
        click id "exp_cancel"
        click id "exp_remove_meal18"
        click id "exp_confirm"
        move id "exp_ledger_scroll"
        keysym "K_PAGEDOWN"
        click id "exp_undo"
        move id "exp_ledger_scroll"
        keysym "K_PAGEUP"
        click id "exp_remove_meal18"
        click id "exp_confirm"
        assert eval exp_demo_ready() and exp_total() == 8000

    testcase rollback_restores_pending_choice:
        run Start("exp_test_checkpoint")
        advance until screen "choice"
        click "Abrir confirmação no teste"
        pause until screen "exp_ledger"
        assert eval exp_pending == "meal18"
        run Rollback() until "Manter lista intacta no teste"
        assert eval exp_pending == "" and exp_total() == 10000
        click "Manter lista intacta no teste"
        pause until screen "exp_ledger"
        assert eval exp_pending == "" and exp_total() == 10000
