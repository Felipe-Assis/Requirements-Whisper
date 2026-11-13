default ticket_active = False
default ticket_phase = "investigation"
default ticket_evidence = []
default ticket_source = ""
default ticket_selected = "241"
default ticket_prioritized = False
default ticket_records = {}
default ticket_demo_records = {}
default ticket_demo_version = "old"
default ticket_demo_result = ""
default ticket_reproduced = False
default ticket_patch = ""
default ticket_tests = {}
default ticket_policy = ""
default ticket_draft = ""
default ticket_owner = ""
default ticket_next_step = ""
default ticket_delivery = "not_delivered"
default ticket_followup_status = "open"
default ticket_reopen_reason = ""
default ticket_reopen_known_case = False
default ticket_feedback = ""
default ticket_events = []

init python:
    import copy

    TICKET_SOURCES = {
        "panel": {"title": "Painel interno", "source": "Observação · suporte", "text": "Rodrigo encerrou o chamado #241 no painel. O suporte lê Resolvido e uma nota técnica. A tela da solicitante ainda mostra Em atendimento."},
        "message": {"title": "Mensagem da solicitante", "source": "Relato · Ana, secretaria", "text": "Ana escreveu: 'Ainda aparece Em atendimento. Não sei o que foi feito nem o que devo tentar. Liguei de novo e abriram outro atendimento.' Ela precisa ver o estado e uma solução que consiga usar."},
        "log": {"title": "Registro do atendimento", "source": "Histórico · chamado #241", "text": "14h10: suporte conferiu permissões. 14h25: alterou apenas o estado interno. Não há evento de publicação para Ana. A nota técnica contém detalhes de acesso; ela não deve virar resposta pública por cópia automática."},
        "shift": {"title": "Passagem de turno · opcional", "source": "Escala confirmada · Rodrigo e Sabrina", "text": "Rodrigo encerra o turno hoje e não estará amanhã. Sabrina confirmou disponibilidade às 09h para revisão ou acompanhamento. Se você consultar a escala agora, essa disponibilidade fica visível na entrega; um repasse genérico continuará sem responsável."},
    }
    TICKET_CASES = {
        "241": {"title": "Matrícula bloqueada", "requester": "Ana · secretaria", "impact": "12 estudantes sem concluir matrícula até o meio-dia.", "public": "As permissões de matrícula foram corrigidas. Entre novamente no portal e abra Matrícula > Confirmar. Se continuar bloqueada, reabra este chamado informando o turno e a mensagem exibida.", "note": "Grupo MATRICULA reatribuído na conta de Ana; detalhe de acesso restrito ao suporte.", "reopen": "No turno da noite, a matrícula continua bloqueada após entrar novamente no portal.", "repair": "A permissão foi aplicada também ao turno da noite. Entre novamente no portal e confirme a matrícula; informe neste chamado se a mensagem persistir."},
        "242": {"title": "Exportação do financeiro", "requester": "Beto · financeiro", "impact": "Duas pessoas corrigem o arquivo manualmente; fechamento é amanhã.", "public": "A exportação agora usa ponto e vírgula. Baixe outro arquivo em Relatórios > Exportar CSV e abra com separador ponto e vírgula. Reabra este chamado se as colunas ainda ficarem juntas.", "note": "Serializador CSV alterado no servidor; log interno inclui dados de configuração.", "reopen": "No turno da noite, o CSV novo ainda abre com as colunas juntas.", "repair": "O formato foi conferido também no computador do turno da noite. Baixe um novo CSV; escolha ponto e vírgula ao importar."},
        "243": {"title": "Aviso por e-mail atrasado", "requester": "Lia · biblioteca", "impact": "Uma pessoa consulta o portal manualmente; o atendimento segue disponível.", "public": "A fila de avisos voltou a enviar mensagens. Confira o e-mail e a pasta de spam. O estado atual também está no portal. Se faltar um aviso novo, reabra este chamado com o horário.", "note": "Fila SMTP reprocessada; identificadores internos ficam no registro restrito.", "reopen": "No turno da noite, um aviso novo não chegou ao e-mail nem ao spam.", "repair": "O envio do turno da noite foi corrigido. Confira os novos avisos; se outro faltar, informe o horário neste chamado."},
    }
    TICKET_PATCHES = {
        "internal": "Alterar apenas o painel interno",
        "atomic": "Publicar estado e solução juntos, só neste chamado",
        "broadcast": "Marcar todos os chamados como resolvidos",
    }
    TICKET_TEST_LABELS = {"resolved": "Estado e solução para a pessoa", "empty": "Solução vazia não resolve", "other": "Outros chamados ficam intactos"}
    TICKET_RESULTS = {"divergent": "Divergência reproduzida: suporte diz Resolvido; solicitante ainda espera.", "published": "Estado Resolvido e solução pública aparecem juntos.", "blocked": "Solução vazia recusada: nenhum estado ou histórico foi alterado.", "empty_resolved": "Defeito: o painel encerrou sem uma solução pública.", "isolated": "Só o chamado escolhido mudou; os outros registros ficaram intactos.", "leaked": "Defeito: a operação alterou chamados que não foram atendidos."}

    def ticket_initial_records():
        return {key: {"internal_status": "Em atendimento", "public_status": "Em atendimento", "public_solution": "", "internal_note": case["note"], "history": ["14h10 · Atendimento iniciado; sem publicação de solução."]} for key, case in TICKET_CASES.items()}

    def ticket_reset():
        store.ticket_active = True
        store.ticket_phase = "investigation"
        store.ticket_evidence = []
        store.ticket_source = ""
        store.ticket_selected = "241"
        store.ticket_prioritized = False
        store.ticket_records = ticket_initial_records()
        store.ticket_demo_records = ticket_initial_records()
        store.ticket_demo_version = "old"
        store.ticket_demo_result = ""
        store.ticket_reproduced = False
        store.ticket_patch = ""
        store.ticket_tests = {}
        store.ticket_policy = ""
        store.ticket_draft = ""
        store.ticket_owner = ""
        store.ticket_next_step = ""
        store.ticket_delivery = "not_delivered"
        store.ticket_reopen_reason = ""
        store.ticket_reopen_known_case = False
        store.ticket_followup_status = "open"
        store.ticket_feedback = "Leia as três fontes. O registro de turno é uma investigação opcional."
        store.ticket_events = []

    def ticket_collect(source_id):
        if source_id not in TICKET_SOURCES:
            return False
        if source_id not in store.ticket_evidence:
            store.ticket_evidence = store.ticket_evidence + [source_id]
        store.ticket_source = source_id
        store.ticket_feedback = TICKET_SOURCES[source_id]["title"] + " · fonte registrada."
        return True

    def ticket_sources_ready():
        return all(source in store.ticket_evidence for source in ("panel", "message", "log"))

    def ticket_prioritize(ticket_id):
        if ticket_id not in TICKET_CASES or store.ticket_delivery != "not_delivered":
            return False
        if store.ticket_selected != ticket_id:
            store.ticket_tests = {}
            store.ticket_reproduced = False
            store.ticket_draft = ""
        store.ticket_selected = ticket_id
        store.ticket_prioritized = True
        store.ticket_demo_records = ticket_initial_records()
        store.ticket_feedback = ticket_priority_impact()
        return True

    def ticket_priority_impact():
        waiting = ["#" + key + ": " + case["impact"] for key, case in TICKET_CASES.items() if key != store.ticket_selected]
        return "Primeiro: #" + store.ticket_selected + ". Continuam esperando nesta rodada: " + " ".join(waiting)

    def ticket_choose_patch(patch):
        if patch not in TICKET_PATCHES or store.ticket_delivery != "not_delivered":
            return False
        if store.ticket_patch != patch:
            store.ticket_tests = {}
        store.ticket_patch = patch
        store.ticket_feedback = "Versão de teste: " + TICKET_PATCHES[patch] + ". Repita os três casos depois de mudar o patch."
        return True

    def ticket_apply_resolution(records, ticket_id, solution, patch):
        # A cópia impede publicar metade da transição ou alterar o histórico anterior.
        changed = copy.deepcopy(records)
        if patch == "atomic" and not solution.strip():
            return changed, "blocked"
        targets = list(changed) if patch == "broadcast" else [ticket_id]
        for target in targets:
            changed[target]["internal_status"] = "Resolvido"
            if patch != "internal":
                changed[target]["public_status"] = "Resolvido"
                changed[target]["public_solution"] = solution
            changed[target]["history"] = changed[target]["history"] + ["Suporte: Resolvido" + (" · solução publicada: " + solution if patch != "internal" else " · somente registro interno")]
        return changed, "published" if patch != "internal" else "divergent"

    def ticket_demo(version, case):
        if version not in ("old", "new") or case not in TICKET_TEST_LABELS:
            return False
        if version == "new" and not store.ticket_patch:
            store.ticket_feedback = "Escolha um patch antes de testar a nova versão."
            return False
        original = ticket_initial_records()
        selected = store.ticket_selected
        solution = "" if case == "empty" else TICKET_CASES[selected]["public"]
        patch = "internal" if version == "old" else store.ticket_patch
        changed, result = ticket_apply_resolution(original, selected, solution, patch)
        if case == "empty" and result != "blocked":
            result = "empty_resolved"
        elif case == "other":
            result = "isolated" if all(changed[key] == original[key] for key in original if key != selected) else "leaked"
        store.ticket_demo_records = changed
        store.ticket_demo_version = version
        store.ticket_demo_result = result
        if version == "old" and case == "resolved" and result == "divergent":
            store.ticket_reproduced = True
        if version == "new":
            store.ticket_tests = dict(store.ticket_tests, **{case: result})
        store.ticket_feedback = TICKET_RESULTS[result]
        return result

    def ticket_tests_ready():
        return store.ticket_reproduced and store.ticket_patch == "atomic" and all(store.ticket_tests.get(case) == result for case, result in (("resolved", "published"), ("empty", "blocked"), ("other", "isolated")))

    def ticket_set_policy(policy):
        if policy not in ("peer_review", "publish_followup") or store.ticket_delivery != "not_delivered":
            return False
        if store.ticket_policy != policy:
            store.ticket_owner = ""
            store.ticket_next_step = ""
        store.ticket_policy = policy
        store.ticket_feedback = "A revisão espera a colega antes de publicar." if policy == "peer_review" else "A publicação será imediata; a colega acompanha o uso e a reabertura."
        return True

    def ticket_choose_solution(choice):
        if choice not in ("public", "internal", "empty") or store.ticket_delivery != "not_delivered":
            return False
        case = TICKET_CASES[store.ticket_selected]
        store.ticket_draft = {"public": case["public"], "internal": case["note"], "empty": ""}[choice]
        store.ticket_feedback = "Texto público preparado." if choice == "public" else "O encerramento precisa de uma orientação pública. A nota técnica fica restrita ao suporte."
        return True

    def ticket_handoff(owner):
        if owner not in ("sabrina", "team", "rodrigo"):
            return False
        if owner != "sabrina":
            store.ticket_owner = ""
            store.ticket_next_step = ""
            store.ticket_feedback = "Rodrigo não estará no próximo turno. Consulte a escala e combine com alguém disponível." if owner == "rodrigo" else "Repasse para a equipe registrado como pendente: falta alguém assumir o próximo passo."
            return owner == "team"
        if not store.ticket_policy:
            store.ticket_feedback = "Escolha primeiro quando a publicação deve acontecer."
            return False
        store.ticket_owner = "Sabrina"
        action = "revisar a solução antes de publicar" if store.ticket_policy == "peer_review" else "conferir o uso com a solicitante e acompanhar reaberturas"
        store.ticket_next_step = "Sabrina · terça-feira às 09h · " + action + "."
        store.ticket_feedback = "Disponibilidade confirmada. " + store.ticket_next_step
        return True

    def ticket_submit():
        if store.ticket_delivery != "not_delivered":
            return False
        if not ticket_sources_ready() or not ticket_tests_ready():
            store.ticket_feedback = "A entrega espera as fontes, a reprodução e os três testes da versão escolhida."
            return False
        case = TICKET_CASES[store.ticket_selected]
        if store.ticket_draft != case["public"]:
            store.ticket_feedback = "Publicação bloqueada: escreva uma solução útil para a pessoa; não copie a nota interna nem deixe vazio."
            return False
        if not store.ticket_owner or not store.ticket_next_step:
            store.ticket_feedback = "Entrega pendente: 'para a equipe' não confirma quem fará o próximo passo. Você pode recuperar o repasse no retorno."
            return False
        if store.ticket_policy == "peer_review":
            changed = copy.deepcopy(store.ticket_records)
            changed[store.ticket_selected]["internal_status"] = "Aguardando revisão"
            changed[store.ticket_selected]["history"] += ["Solução preparada; publicação aguarda revisão de Sabrina na terça-feira às 09h."]
            store.ticket_records = changed
            store.ticket_delivery = "review_pending"
            store.ticket_feedback = "Enviado para revisão. A pessoa ainda vê Em atendimento; nada foi publicado antes da revisão."
        elif store.ticket_policy == "publish_followup":
            store.ticket_records, result = ticket_apply_resolution(store.ticket_records, store.ticket_selected, store.ticket_draft, "atomic")
            store.ticket_delivery = "published"
            store.ticket_feedback = "Estado e solução publicados juntos. O acompanhamento combinado continua aberto."
        else:
            return False
        store.ticket_events = store.ticket_events + [store.ticket_delivery]
        return True

    def ticket_review():
        if store.ticket_delivery != "review_pending" or not store.ticket_owner or not store.ticket_next_step:
            return False
        store.ticket_records, result = ticket_apply_resolution(store.ticket_records, store.ticket_selected, store.ticket_draft, "atomic")
        store.ticket_delivery = "reviewed"
        store.ticket_followup_status = "reviewed"
        store.ticket_next_step = "Sabrina · terça-feira às 09h · revisão realizada; estado e solução publicados após a conferência."
        store.ticket_events = store.ticket_events + ["reviewed"]
        store.ticket_feedback = "Sabrina conferiu estado, orientação pública e sigilo da nota. A solução foi publicada após a revisão."
        return True

    def ticket_reopen(reason):
        if not isinstance(reason, str) or not reason.strip():
            store.ticket_feedback = "Reabrir exige um motivo: descreva o que continua impedindo o uso."
            return False
        if store.ticket_records[store.ticket_selected]["public_status"] != "Resolvido":
            return False
        changed = copy.deepcopy(store.ticket_records)
        record = changed[store.ticket_selected]
        record["internal_status"] = "Reaberto"
        record["public_status"] = "Reaberto"
        record["history"] += ["Solicitante reabriu · motivo: " + reason.strip()]
        store.ticket_records = changed
        store.ticket_reopen_known_case = False
        store.ticket_followup_status = "reopened"
        store.ticket_next_step = "Sabrina · investigar com Júlio o motivo registrado e combinar o próximo retorno."
        store.ticket_events = store.ticket_events + ["reopened"]
        store.ticket_feedback = "Reaberto com motivo. A solução anterior continua no histórico; Sabrina deve conferir o caso relatado."
        return True

    def ticket_reopen_simulated_case():
        if not ticket_reopen(TICKET_CASES[store.ticket_selected]["reopen"]):
            return False
        store.ticket_reopen_known_case = True
        store.ticket_feedback = "Caso simulado registrado: a falha do turno da noite pode ser reproduzida com Sabrina e Júlio."
        return True

    def ticket_followup(action):
        if not store.ticket_owner or not store.ticket_next_step:
            return False
        status = store.ticket_records[store.ticket_selected]["public_status"]
        if action == "confirm" and status == "Resolvido" and store.ticket_followup_status != "confirmed":
            changed = copy.deepcopy(store.ticket_records)
            changed[store.ticket_selected]["history"] += ["Terça-feira às 09h · " + TICKET_CASES[store.ticket_selected]["requester"] + " confirmou o uso com Sabrina."]
            store.ticket_records = changed
            store.ticket_followup_status = "confirmed"
            store.ticket_next_step = "Sabrina · terça-feira às 09h · conferência de uso realizada com a pessoa solicitante."
            store.ticket_events = store.ticket_events + ["followup_confirmed"]
            store.ticket_feedback = "A solicitante confirmou o uso com Sabrina. O acompanhamento combinado foi realizado."
            return True
        if action == "repair" and status == "Reaberto" and store.ticket_reopen_known_case:
            solution = TICKET_CASES[store.ticket_selected]["repair"]
            store.ticket_records, result = ticket_apply_resolution(store.ticket_records, store.ticket_selected, solution, "atomic")
            store.ticket_followup_status = "repaired"
            store.ticket_next_step = "Sabrina e Júlio · caso simulado do turno da noite reproduzido, corrigido e publicado."
            store.ticket_events = store.ticket_events + ["repaired"]
            store.ticket_feedback = "Sabrina conferiu o turno relatado; Júlio corrigiu e a nova solução foi publicada sem apagar a anterior."
            return True
        return False

    def ticket_ending():
        if not store.ticket_owner or not store.ticket_next_step:
            return "unowned"
        if store.ticket_followup_status in ("reopened", "repaired"):
            return store.ticket_followup_status
        if store.ticket_delivery == "review_pending":
            return "review_pending"
        if store.ticket_delivery == "reviewed":
            return "reviewed"
        if store.ticket_delivery == "published":
            return "followed_up" if store.ticket_followup_status == "confirmed" else "followup_pending"
        return "not_delivered"

    def ticket_return_text():
        policy = "revisão por colega antes de publicar" if store.ticket_policy == "peer_review" else "publicação imediata com acompanhamento de reaberturas"
        prefix = "Política escolhida: " + policy + ". "
        if store.ticket_followup_status == "reopened":
            return prefix + "A pessoa reabriu com motivo. A solução anterior foi preservada; a investigação continua pendente. " + store.ticket_next_step
        if store.ticket_followup_status == "repaired":
            return prefix + "A verificação do caso simulado foi realizada; a nova solução foi publicada. " + store.ticket_next_step
        if store.ticket_followup_status == "confirmed":
            return prefix + "A conferência de uso foi realizada e registrada no histórico. " + store.ticket_next_step
        if store.ticket_delivery == "review_pending":
            return prefix + "Solução preparada; publicação aguarda a revisão combinada para terça-feira às 09h. " + store.ticket_next_step
        if store.ticket_delivery == "reviewed":
            return prefix + "Revisão realizada; estado e solução foram publicados após a conferência. " + store.ticket_next_step
        if store.ticket_delivery == "published":
            return prefix + "Estado e solução publicados juntos; o acompanhamento permanece pendente. " + store.ticket_next_step
        return prefix + "Entrega pendente. O chamado continua Em atendimento; confirme responsável e próximo passo para recuperar o repasse."

    def ticket_summary():
        outcome = ticket_ending()
        titles = {"unowned": "Repasse sem responsável", "review_pending": "Publicação aguarda revisão", "reviewed": "Publicado após revisão", "followup_pending": "Publicado; acompanhamento pendente", "followed_up": "Publicação acompanhada", "reopened": "Reaberto com motivo", "repaired": "Retorno corrigido e registrado", "not_delivered": "Entrega pendente"}
        pending = ""
        if outcome in ("unowned", "not_delivered"):
            pending = "Confirmar responsável disponível e próximo passo antes da entrega."
        elif outcome == "review_pending":
            pending = "Sabrina precisa revisar a solução antes de publicar."
        elif outcome == "followup_pending":
            pending = "Sabrina precisa conferir o uso e acompanhar reaberturas."
        elif outcome == "reopened":
            pending = "Sabrina precisa verificar o motivo da reabertura com Júlio."
        waiting = "Os outros dois chamados continuam Em atendimento; não foram resolvidos por esta publicação."
        return {"title": "Chamados", "outcome": outcome, "summary": titles[outcome] + " · #" + store.ticket_selected + ". " + waiting, "pending": pending, "owner": store.ticket_owner, "next_step": store.ticket_next_step, "policy": store.ticket_policy, "priority": store.ticket_selected, "impact": ticket_priority_impact(), "tests": dict(store.ticket_tests), "events": list(store.ticket_events), "history": list(store.ticket_records[store.ticket_selected]["history"]), "shift_checked": "shift" in store.ticket_evidence, "known_reopen_case": store.ticket_reopen_known_case}
