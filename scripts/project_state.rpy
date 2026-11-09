default lab_active = False
default lab_phase = "investigation"
default lab_evidence = []
default lab_links = {}
default lab_plan = []
default lab_initial_plan = []
default lab_commitment = ""
default lab_commitment_status = "open"
default lab_delivery = "not_delivered"
default lab_events = []
default lab_sidequest = False
default lab_repaired = False
default lab_test_results = {}
default lab_location = "laboratorio"
default lab_feedback = ""
default lab_revision = 1
default lab_return_milestone = "reunião de sexta-feira da próxima semana"
default lab_commitment_owner = "Júlio e Carlos"

init python:
    LAB_EVIDENCE = {
        "sheets": {
            "title": "Duas reservas, um microscópio",
            "source": "Observação · planilhas do laboratório",
            "text": "Uma planilha reserva o microscópio das 14h às 15h. A outra registra o mesmo equipamento das 14h30 às 15h30. As equipes só descobrem o choque ao chegar.",
        },
        "preparation": {
            "title": "Dez minutos de preparação",
            "source": "Confirmação · técnica do laboratório",
            "text": "A técnica confirma: o microscópio precisa de dez minutos livres entre usos para preparação. A ficha não confirma esse intervalo para os outros equipamentos.",
        },
        "interview": {
            "title": "Carlos precisa confiar na consulta",
            "source": "Relato · conversa com Carlos",
            "text": "Carlos precisa consultar equipamento, data e horário com clareza antes de reservar. Cores bonitas não resolvem uma disponibilidade que muda de uma planilha para outra.",
        },
        "offline": {
            "title": "A planilha que ninguém aposenta",
            "source": "Relato · equipe da bancada",
            "text": "A conexão falha perto da bancada. A equipe mantém uma planilha local para trabalhar. Sem combinar como confirmar uma reserva, trocar a tela apenas cria outro lugar para conferir.",
        },
    }
    LAB_ITEMS = {
        "conflict": {"title": "Impedir reservas sobrepostas", "cost": 2, "description": "Conferir equipamento e intervalo antes de confirmar uma reserva."},
        "preparation": {"title": "Preparação do microscópio", "cost": 1, "description": "Reservar dez minutos entre usos do microscópio. Depende de impedir sobreposições."},
        "clarity": {"title": "Calendário legível", "cost": 1, "description": "Apresentar equipamento e horários de forma clara; não impede conflitos por si só."},
    }
    LAB_CASES = {
        "overlap": {"title": "Mesmo equipamento, horários sobrepostos", "existing": ("microscopio", 840, 900), "candidate": ("microscopio", 870, 930)},
        "adjacent": {"title": "Uma reserva começa quando a outra termina", "existing": ("microscopio", 840, 900), "candidate": ("microscopio", 900, 960)},
        "preparation": {"title": "Cinco minutos entre usos do microscópio", "existing": ("microscopio", 840, 900), "candidate": ("microscopio", 905, 965)},
        "other": {"title": "Equipamentos diferentes no mesmo horário", "existing": ("microscopio", 840, 900), "candidate": ("centrifuga", 840, 900)},
    }

    def lab_reset():
        store.lab_active = True
        store.lab_phase = "investigation"
        store.lab_evidence = []
        store.lab_links = {}
        store.lab_plan = []
        store.lab_initial_plan = []
        store.lab_commitment = ""
        store.lab_commitment_status = "open"
        store.lab_delivery = "not_delivered"
        store.lab_events = []
        store.lab_sidequest = False
        store.lab_repaired = False
        store.lab_test_results = {}
        store.lab_location = "laboratorio"
        store.lab_feedback = "Escolha um lugar no mapa para ouvir as pessoas e examinar as fontes."
        store.lab_revision = 1
        store.lab_return_milestone = "reunião de sexta-feira da próxima semana"
        store.lab_commitment_owner = "Júlio e Carlos"

    def lab_record_event(event):
        if event not in store.lab_events:
            store.lab_events = store.lab_events + [event]

    def lab_collect(evidence_id):
        if evidence_id not in LAB_EVIDENCE:
            store.lab_feedback = "Essa fonte não pertence à investigação."
            return False
        if evidence_id not in store.lab_evidence:
            store.lab_evidence = store.lab_evidence + [evidence_id]
        if evidence_id == "offline":
            store.lab_sidequest = True
        store.lab_feedback = LAB_EVIDENCE[evidence_id]["title"] + ": fonte registrada na pasta de trabalho."
        return True

    def lab_link(rule_id, evidence_id):
        if rule_id not in LAB_ITEMS or evidence_id not in store.lab_evidence:
            store.lab_feedback = "Examine a fonte antes de usá-la para justificar uma regra."
            return False
        links = dict(store.lab_links)
        links[rule_id] = evidence_id
        store.lab_links = links
        supported = {"conflict": "sheets", "preparation": "preparation", "clarity": "interview"}.get(rule_id) == evidence_id
        if supported:
            store.lab_feedback = "Ligação apoiada pela fonte. O comportamento ainda depende do plano da entrega."
        else:
            store.lab_feedback = "Hipótese registrada. Essa fonte não confirma a regra; consulte outra e refaça a ligação."
        return supported

    def lab_plan_cost():
        return sum(LAB_ITEMS[item]["cost"] for item in store.lab_plan if item in LAB_ITEMS)

    def lab_plan_ready():
        plan = store.lab_plan
        return bool(plan) and len(plan) == len(set(plan)) and all(item in LAB_ITEMS for item in plan) and lab_plan_cost() <= 3 and ("preparation" not in plan or "conflict" in plan)

    def lab_toggle_plan(item_id):
        if item_id not in LAB_ITEMS:
            store.lab_feedback = "Escolha um dos itens do plano."
            return False
        # O acordo confirma este escopo. Depois dele, a revisão acontece na reparação.
        if store.lab_commitment:
            store.lab_feedback = "Este plano já foi acordado. Na visita de retorno, combine a reparação para revisar a entrega."
            return False
        plan = list(store.lab_plan)
        if item_id in plan:
            if item_id == "conflict" and "preparation" in plan:
                store.lab_feedback = "Retire a preparação primeiro: ela depende da proteção contra sobreposição."
                return False
            plan.remove(item_id)
        else:
            if item_id == "preparation" and "conflict" not in plan:
                store.lab_feedback = "A preparação depende da proteção contra sobreposição. Adicione essa base primeiro."
                return False
            if lab_plan_cost() + LAB_ITEMS[item_id]["cost"] > 3:
                store.lab_feedback = "A capacidade é de três pontos nesta rodada. Retire outro item para abrir espaço."
                return False
            plan.append(item_id)
        store.lab_plan = plan
        store.lab_feedback = "Plano atualizado: %d de 3 pontos. Você pode revisar antes do acordo." % lab_plan_cost()
        return True

    def lab_confirm_commitment(option):
        if option not in ("base_primeiro", "investigar_agora") or not lab_plan_ready():
            store.lab_feedback = "Confirme um plano válido antes de combinar a prioridade com a equipe."
            return False
        if not store.lab_commitment:
            store.lab_initial_plan = list(store.lab_plan)
        store.lab_commitment = option
        store.lab_commitment_status = "open"
        store.lab_delivery = "not_delivered"
        lab_record_event("commitment_confirmed")
        if option == "base_primeiro":
            store.lab_feedback = "A equipe combinou entregar os itens do plano. A entrega ainda precisa chegar à bancada; a integração continua dependente de pesquisa e confirmação manual."
        else:
            lab_record_event("investigation_started")
            store.lab_feedback = "Júlio e Carlos investigam acesso e conexão; voltam na sexta-feira da próxima semana. O calendário é um protótipo e o processo atual continua."
        return True

    def lab_mark_delivery():
        if store.lab_commitment != "base_primeiro":
            store.lab_feedback = "A entrega continua pendente. O protótipo não substitui o processo atual."
            return False
        if store.lab_repaired:
            if store.lab_test_results.get("overlap") != "conflict" or store.lab_test_results.get("preparation") != "preparation_required":
                store.lab_feedback = "A revisão ainda não chegou à bancada. Repita os testes de sobreposição e de preparação antes de confirmar a entrega."
                return False
            store.lab_delivery = "repaired"
            lab_record_event("repaired")
        else:
            store.lab_delivery = "base_delivered"
            lab_record_event("base_delivered")
        store.lab_feedback = "O pacote confirmado chegou à bancada. As regras entregues são as do plano registrado."
        return True

    def lab_reservation_result(existing, candidate, rules):
        # Minutos no mesmo dia; intervalos [início, fim), sem sobreposição nas pontas.
        def valid(reservation):
            return isinstance(reservation, (tuple, list)) and len(reservation) == 3 and isinstance(reservation[0], str) and bool(reservation[0].strip()) and type(reservation[1]) is int and type(reservation[2]) is int and 0 <= reservation[1] < reservation[2] <= 1440

        if not valid(existing) or not valid(candidate):
            return "invalid"
        def equipment(name):
            name = name.strip().lower()
            return "microscopio" if name in ("microscope", "microscópio") else name

        if equipment(existing[0]) != equipment(candidate[0]):
            return "allowed"
        overlap = existing[1] < candidate[2] and candidate[1] < existing[2]
        if overlap and "conflict" in rules:
            return "conflict"
        if not overlap and "preparation" in rules and equipment(existing[0]) == "microscopio":
            gap = max(existing[1], candidate[1]) - min(existing[2], candidate[2])
            if gap < 10:
                return "preparation_required"
        return "allowed"

    def lab_run_test(case_id):
        if case_id not in LAB_CASES:
            store.lab_feedback = "Escolha um dos casos de teste disponíveis."
            return "invalid"
        case = LAB_CASES[case_id]
        result = lab_reservation_result(case["existing"], case["candidate"], store.lab_plan)
        results = dict(store.lab_test_results)
        results[case_id] = result
        store.lab_test_results = results
        feedback = {
            "allowed": "Tentativa aceita pelas regras deste plano. Compare com a necessidade observada; aceitar um choque revela proteção ausente.",
            "conflict": "Tentativa recusada: o equipamento já está reservado nesse intervalo.",
            "preparation_required": "Tentativa recusada: faltam dez minutos livres para preparar o microscópio entre usos.",
            "invalid": "Tentativa inválida: confira equipamento, início e fim no mesmo dia.",
        }
        store.lab_feedback = feedback[result] + " A reserva anterior permanece."
        return result

    def lab_repair():
        # A reparação ocupa outra rodada; preserva o pacote da primeira entrega.
        store.lab_plan = store.lab_plan + [item for item in ("conflict", "preparation") if item not in store.lab_plan]
        store.lab_revision = 2
        store.lab_delivery = "revision_pending"
        store.lab_repaired = True
        store.lab_test_results = {}
        lab_record_event("revision_prepared")
        store.lab_feedback = "Revisão 2 preparada, com os itens anteriores preservados. Repita os testes de choque e preparação antes da entrega. A capacidade de três pontos era da primeira rodada."
        return True

    def lab_ending():
        if store.lab_delivery == "not_delivered":
            return "waiting"
        if store.lab_delivery == "revision_pending":
            return "unowned"
        if store.lab_delivery == "repaired" and store.lab_repaired:
            return "repaired"
        if "conflict" in store.lab_plan and "preparation" in store.lab_plan:
            return "reliable"
        return "unowned"

    def lab_objective():
        objectives = {
            "investigation": "Investigue as reservas, a preparação e o relato de Carlos; a visita à equipe é opcional.",
            "definition": "Ligue cada regra à fonte que a confirma. Você pode refazer uma hipótese.",
            "planning": "Escolha uma primeira entrega que caiba em três pontos e respeite as dependências.",
            "negotiation": "Combine a prioridade, os responsáveis e a reunião de retorno.",
            "delivery": "Experimente o calendário e compare o comportamento com as evidências.",
            "followup": "Confira o compromisso com a equipe e decida como tratar as pendências.",
            "ending": "Veja o resultado da entrega, sua causa e o que ainda precisa de acompanhamento.",
        }
        return objectives.get(store.lab_phase, "Consulte o projeto na pasta de trabalho.")
