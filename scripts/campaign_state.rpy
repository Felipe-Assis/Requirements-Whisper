default campaign_active = False
default campaign_results = {}
default campaign_last_project = ""
default campaign_started_projects = []

init python:
    import copy

    CAMPAIGN_PROJECTS = {
        "lab": {"title": "Laboratório", "object": "Agenda da bancada", "place": "Universidade", "image": "images/bg/laboratorio.png", "challenge": "Duas equipes. Um microscópio. Quem pode confirmar?"},
        "expenses": {"title": "Gastos", "object": "Celular e comprovantes", "place": "Startup", "image": "images/bg/startup.png", "challenge": "Dois almoços ou dois registros? Confira antes de apagar."},
        "tickets": {"title": "Chamados", "object": "Registro de turno", "place": "Central de atendimento", "image": "images/bg/suporte.png", "challenge": "Resolvido para quem? Acompanhe os dois lados do balcão."},
    }

    def campaign_memory(project_id):
        return copy.deepcopy(store.campaign_results.get(project_id, {}))

    def campaign_mark_started(project_id):
        if project_id not in CAMPAIGN_PROJECTS:
            return False
        if project_id not in store.campaign_started_projects:
            store.campaign_started_projects = store.campaign_started_projects + [project_id]
        return True

    def campaign_record(project_id, summary):
        result = copy.deepcopy(summary)
        result["clock"] = copy.deepcopy(getattr(store, "campaign_clock", {}))
        if project_id == "expenses":
            result["layout"] = campaign_layout(project_id)
        store.campaign_results = dict(store.campaign_results, **{project_id: result})
        store.campaign_last_project = project_id

    def campaign_archive_lab():
        summaries = {
            "reliable": "A agenda protege reservas e preparo do microscópio.",
            "repaired": "A equipe reproduziu o incidente e entregou uma revisão verificada.",
            "waiting": "A investigação ganhou responsável; a agenda ainda não foi entregue.",
            "unowned": "Uma proteção ficou fora da entrega; o incidente continua aberto.",
        }
        outcome = lab_ending()
        pending = {
            "waiting": "Retomar autorização e próxima entrega com Carlos e Júlio.",
            "unowned": "Confirmar responsável e prazo para corrigir a proteção que ficou fora da entrega.",
            "reliable": "Acompanhar a adoção e conferir a pesquisa de integração.",
            "repaired": "Acompanhar a revisão na bancada e conferir a pesquisa de integração.",
        }[outcome]
        pending += " Retorno combinado: " + store.lab_return_milestone + "; responsáveis: " + store.lab_commitment_owner + "."
        campaign_record("lab", {
            "title": "Laboratório", "outcome": outcome, "summary": summaries[outcome],
            "pending": pending,
            "plan": list(store.lab_plan), "initial_plan": list(store.lab_initial_plan),
            "sidequest": store.lab_sidequest, "repaired": store.lab_repaired,
            "commitment_status": store.lab_commitment_status, "delivery": store.lab_delivery,
            "return_milestone": store.lab_return_milestone, "commitment_owner": store.lab_commitment_owner,
            "facts": list(store.lab_evidence),
        })

    def campaign_reset():
        store.campaign_active = True
        store.campaign_results = {}
        store.campaign_last_project = ""
        store.campaign_started_projects = []
        store.campaign_clock = {}
        store.campaign_layouts = {}
        store.notebook_read = []
        student_reset()

