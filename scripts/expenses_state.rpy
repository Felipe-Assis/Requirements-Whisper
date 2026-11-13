# Estado próprio: valores em centavos e cópias nas alterações para save/rollback.
default exp_phase = "investigation"
default exp_sources = []
default exp_source = ""
default exp_rows = []
default exp_pending = ""
default exp_undo_rows = None
default exp_undo_kind = ""
default exp_feedback = ""
default exp_before_reproduced = False
default exp_plan = ""
default exp_changes = []
default exp_built = False
default exp_reviewer = ""
default exp_checks = []
default exp_delivered = False
default exp_sidequest = False
default exp_zero_rejected = False
default exp_recovered = False
default exp_renegotiated = False

init python:
    EXP_SOURCES = {
        "receipt": ("Comprovante · cantina", "RECIBO C-071 · terça, 12h14\nUm almoço · R$ 20,00 · pago por Lia. Um pagamento registrado."),
        "ledger": ("Lista de lançamentos", "AL-17 · almoço · recibo C-071 · R$ 20,00\nAL-18 · almoço · recibo C-071 · R$ 20,00\nLI-04 · livro · R$ 40,00\nTR-09 · transporte · R$ 20,00"),
        "lia": ("Conversa · Lia, estudante", "Lia: paguei um almoço. A conexão caiu, toquei Salvar de novo e apareceram AL-17 e AL-18. Pode remover AL-18. O transporte de R$ 20,00 é outra compra, está certo."),
    }
    EXP_CHANGES = {
        "defer": ("Adiar remoção até Confirmar", "Abrir a pergunta só guarda o ID. Cancelar limpa a pergunta sem tocar na lista."),
        "total": ("Atualizar lista e total juntos", "O total soma os lançamentos atuais em centavos; a remoção usa o ID escolhido."),
        "undo": ("Guardar a última lista para desfazer", "Antes da alteração, guardar uma cópia. Desfazer restaura os valores e a ordem."),
    }

    def exp_fixture():
        return [
            {"id": "meal17", "code": "AL-17", "name": "Almoço · C-071", "amount": 2000},
            {"id": "meal18", "code": "AL-18", "name": "Almoço · C-071", "amount": 2000},
            {"id": "book", "code": "LI-04", "name": "Livro", "amount": 4000},
            {"id": "bus", "code": "TR-09", "name": "Transporte", "amount": 2000},
        ]

    def exp_copy(rows):
        return [dict(row) for row in rows]

    def exp_reset():
        store.exp_phase = "investigation"
        store.exp_sources = []
        store.exp_source = ""
        store.exp_rows = exp_fixture()
        store.exp_pending = ""
        store.exp_undo_rows = None
        store.exp_undo_kind = ""
        store.exp_feedback = "Compare recibo, lançamentos e relato antes de decidir."
        store.exp_before_reproduced = False
        store.exp_plan = ""
        store.exp_changes = []
        store.exp_built = False
        store.exp_reviewer = ""
        store.exp_checks = []
        store.exp_delivered = False
        store.exp_sidequest = False
        store.exp_zero_rejected = False
        store.exp_recovered = False
        store.exp_renegotiated = False

    def exp_total():
        return sum(row["amount"] for row in store.exp_rows)

    def exp_money(cents):
        return "R$ %d,%02d" % (cents // 100, cents % 100)

    def exp_inspect(source):
        if source not in EXP_SOURCES:
            return False
        store.exp_source = source
        if source not in store.exp_sources:
            store.exp_sources = store.exp_sources + [source]
        store.exp_feedback = "Fonte registrada: " + EXP_SOURCES[source][0] + "."
        return True

    def exp_request_delete(row_id):
        if store.exp_pending or not any(row["id"] == row_id for row in store.exp_rows):
            return False
        store.exp_pending = row_id
        if not store.exp_built:
            # Versão anterior reproduzida: a pergunta já altera os dados.
            store.exp_rows = [dict(row) for row in store.exp_rows if row["id"] != row_id]
            store.exp_feedback = "A candidata antiga já removeu a linha. Experimente Cancelar."
        else:
            store.exp_feedback = "A confirmação está aberta. Lista e total ainda não mudaram."
        return True

    def exp_check(check):
        if check not in store.exp_checks:
            store.exp_checks = store.exp_checks + [check]

    def exp_cancel_delete():
        if not store.exp_pending:
            return False
        store.exp_pending = ""
        if store.exp_built:
            exp_check("cancel")
            store.exp_feedback = "Cancelado. Mesmas linhas e mesmo total; nenhum dado removido."
        else:
            store.exp_before_reproduced = True
            store.exp_feedback = "Falha reproduzida: Cancelar fechou a pergunta, mas a linha não voltou."
        return True

    def exp_confirm_delete():
        if not store.exp_pending:
            return False
        row_id = store.exp_pending
        store.exp_pending = ""
        if not store.exp_built:
            store.exp_feedback = "A linha já tinha sido removida antes da resposta. Reponha a amostra e teste Cancelar."
            return True
        store.exp_undo_rows = exp_copy(store.exp_rows)
        store.exp_undo_kind = row_id
        store.exp_rows = [dict(row) for row in store.exp_rows if row["id"] != row_id]
        exp_check("confirm")
        store.exp_feedback = "Somente a linha escolhida saiu. Total recalculado: " + exp_money(exp_total()) + "."
        return True

    def exp_restore_fixture():
        if store.exp_built and any(not any(row["id"] == row_id for row in store.exp_rows) for row_id in ("meal17", "book", "bus")):
            store.exp_recovered = True
        store.exp_rows = exp_fixture()
        store.exp_pending = ""
        store.exp_undo_rows = None
        store.exp_undo_kind = ""
        store.exp_checks = []
        store.exp_feedback = ("Amostra de teste reposta: quatro lançamentos, R$ 100,00. Repita Cancelar, Confirmar e Desfazer; a candidata corrigida foi mantida."
                              if store.exp_built else "Amostra de teste reposta: quatro lançamentos, R$ 100,00.")

    def exp_undo():
        if store.exp_pending or store.exp_undo_rows is None:
            return False
        if store.exp_undo_kind not in ("meal18", "edit"):
            store.exp_recovered = True
        store.exp_rows = exp_copy(store.exp_undo_rows)
        store.exp_undo_rows = None
        store.exp_undo_kind = ""
        exp_check("undo")
        store.exp_feedback = "Última alteração desfeita. Linhas e total foram restaurados."
        return True

    def exp_edit(row_id, amount):
        if not store.exp_built or store.exp_pending:
            return False
        if type(amount) is not int or amount <= 0 or amount > 99999999:
            if amount == 0 and type(amount) is int:
                store.exp_zero_rejected = True
            store.exp_feedback = "Valor inválido. Use um valor maior que zero; a lista foi preservada."
            return False
        if not any(row["id"] == row_id for row in store.exp_rows):
            return False
        store.exp_undo_rows = exp_copy(store.exp_rows)
        store.exp_undo_kind = "edit"
        store.exp_rows = [dict(row, amount=amount) if row["id"] == row_id else dict(row) for row in store.exp_rows]
        store.exp_sidequest = True
        store.exp_feedback = "Transporte atualizado na amostra. Total: " + exp_money(exp_total()) + ". Desfaça para retomar o caso original."
        return True

    def exp_set_plan(plan):
        if plan not in ("core", "bank") or store.exp_built:
            return False
        if store.exp_plan == "bank" and plan == "core":
            store.exp_renegotiated = True
        store.exp_plan = plan
        return True

    def exp_apply_change(change):
        if change not in EXP_CHANGES or store.exp_plan != "core" or store.exp_built:
            return False
        if change not in store.exp_changes:
            store.exp_changes = store.exp_changes + [change]
        store.exp_feedback = EXP_CHANGES[change][1]
        return True

    def exp_build(reviewer):
        if store.exp_plan != "core" or set(store.exp_changes) != set(EXP_CHANGES) or reviewer not in ("pair", "review"):
            return False
        store.exp_built = True
        store.exp_reviewer = reviewer
        store.exp_checks = []
        exp_restore_fixture()
        store.exp_feedback = "Revisão com Júlio pronta. Agora compare Cancelar, Confirmar e Desfazer com a versão anterior."
        return True

    def exp_demo_ready():
        expected = [row for row in exp_fixture() if row["id"] != "meal18"]
        return (store.exp_built and bool(store.exp_reviewer) and not store.exp_pending
                and all(source in store.exp_sources for source in EXP_SOURCES)
                and all(check in store.exp_checks for check in ("cancel", "confirm", "undo"))
                and store.exp_rows == expected and exp_total() == 8000)

    def exp_deliver():
        if not exp_demo_ready():
            store.exp_feedback = "Ainda falta demonstrar os critérios ou restaurar os dados legítimos. Você pode continuar o ensaio."
            return False
        store.exp_delivered = True
        return True

    def exp_outcome():
        if store.exp_plan == "bank":
            return "waiting"
        if not store.exp_delivered:
            return "pending"
        return "recovered" if store.exp_recovered else "reliable"

    def exp_result():
        outcome = exp_outcome()
        summary = {
            "waiting": "Pesquisa bancária iniciada; correção da lista ainda não entregue.",
            "pending": "A falha de cancelamento foi identificada; a revisão ainda precisa concluir seus critérios.",
            "recovered": "Um lançamento legítimo foi restaurado no ensaio; a entrega preserva a lista e fecha em R$ 80,00.",
            "reliable": "Cancelar preserva os dados, confirmar remove AL-18 e desfazer restaura. Lista final: R$ 80,00.",
        }[outcome]
        pending = ("Júlio obtém consentimento e acesso de testes do banco; Lia e equipe retomam a correção na próxima sexta."
                   if outcome == "waiting" else
                   "Você e Júlio retomam o ensaio com Lia na próxima sexta; não publicar a revisão antes dos critérios."
                   if outcome == "pending" else
                   "Júlio verifica consentimento e acesso de testes antes de estimar a integração; retorno com Lia na próxima sexta.")
        return {"title": "Gastos", "outcome": outcome, "summary": summary, "pending": pending,
                "sources": list(store.exp_sources), "checks": list(store.exp_checks),
                "delivered": store.exp_delivered, "sidequest": store.exp_sidequest, "zero_rejected": store.exp_zero_rejected,
                "recovered": store.exp_recovered, "renegotiated": store.exp_renegotiated,
                "reviewer": store.exp_reviewer, "total": exp_total(), "rows": exp_copy(store.exp_rows)}
