# routes.rpy
# -------------------------------
# REGISTRO DAS ROTAS (vagas de scene_1_quarto)
# -------------------------------
# chosen_job vem da escolha da vaga em scene_1_quarto. Vazio = rota saúde
# (saves antigos e o caminho original).
default chosen_job = ""

# init 1: roda depois de DEVELOPERS (logic/state_flags.rpy) e CONTACTS_ORDER
# (data/friends_data.rpy), para a saúde reaproveitar as listas originais.
init 1 python:
    ROUTES = {
        "saude": {
            "empresa": _("Instituto XX"),
            "produto": _("ByeByeFumo"),
            "team": DEVELOPERS,
            "stakeholders": ["doutora_1", "doutora_2"],
            "contacts_order": CONTACTS_ORDER,
            # As doutoras têm disponibilidade controlada à mão nas cenas;
            # set_available só mexe na equipe.
            "stakeholders_manuais": True,
        },
        "startup": {
            "empresa": _("Trocado"),
            "produto": _("app Trocado"),
            "team": ["st_mentora", "st_techlead", "st_mobile", "st_qualidade"],
            "stakeholders": ["st_ceo", "st_estudante"],
            "contacts_order": [
                "st_mentora", "st_techlead", "st_mobile", "st_qualidade",
                "st_ceo", "st_estudante",
            ],
            "stakeholders_manuais": False,
        },
        "corporativo": {
            "empresa": _("Grupo Vértice"),
            "produto": _("SGC"),
            "team": ["co_mentora", "co_legado", "co_dev", "co_qualidade"],
            "stakeholders": ["co_supervisora", "co_solicitante"],
            "contacts_order": [
                "co_mentora", "co_legado", "co_dev", "co_qualidade",
                "co_supervisora", "co_solicitante",
            ],
            "stakeholders_manuais": False,
        },
    }

    def current_route():
        # Rota em jogo; qualquer valor desconhecido cai na saúde.
        return store.chosen_job if store.chosen_job in ROUTES else "saude"

    def route_data(route=None):
        return ROUTES[route or current_route()]

    def route_team(route=None):
        # Equipe da rota (a amizade que conta no final).
        return list(route_data(route)["team"])

    def route_contact_ids(route=None):
        # Ids cuja disponibilidade set_available controla: a equipe e, fora
        # da saúde, também os stakeholders.
        data = route_data(route)
        ids = list(data["team"])
        if not data["stakeholders_manuais"]:
            ids += data["stakeholders"]
        return ids

    def route_contacts_order(route=None):
        # Ordem dos contatos na grade do celular.
        return list(route_data(route)["contacts_order"])


# Registros, conquistas e final da rota saúde (contrato em logic/learning.rpy).
# As cenas da saúde chamam registrar() com estes ids; as conquistas leem os
# itens que as cenas já põem em `inventario`.
init 1 python:
    ROUTES["saude"]["records"] = [
        {
            "id": "saude_reg_ciclo",
            "title": _("Ciclo de vida do software"),
            "text": _("O projeto segue seis etapas: elicitação, especificação, design e arquitetura, codificação, testes e validação, implantação. Quanto mais clareza no início, menos retrabalho depois."),
        },
        {
            "id": "saude_reg_entrevista",
            "title": _("Elicitação por entrevista"),
            "text": _("Prepare perguntas abertas, peça exemplos do dia a dia e ouça com atenção. Muitos requisitos importantes aparecem fora do roteiro, quando a pessoa conta a própria rotina."),
        },
        {
            "id": "saude_reg_classificacao",
            "title": _("Classificação de requisitos"),
            "text": _("Separe o que é requisito funcional (o que o sistema faz), o que é requisito de usabilidade ou outro não funcional, e o que é só opinião ou desejo. Na dúvida, volte aos stakeholders."),
        },
        {
            "id": "saude_reg_casos_uso",
            "title": _("Casos de uso"),
            "text": _("Cada caso de uso descreve um fluxo de quem usa o sistema, como o UC1: Cadastro de Paciente. Documente também os fluxos alternativos e as exceções, como o paciente que esqueceu o CPF."),
        },
        {
            "id": "saude_reg_inspecao",
            "title": _("Inspeção de requisitos"),
            "text": _("Antes de documentar, procure informação ausente, ambígua ou estranha. Sem detalhe, cada pessoa implementa de um jeito. Critérios de aceitação devem prever os valores de fronteira."),
        },
        {
            "id": "saude_reg_arquitetura",
            "title": _("Arquitetura e trade-offs"),
            "text": _("Um monolito é mais simples de implantar e depurar; microsserviços isolam testes e escalam partes críticas, mas exigem mais integração e monitoramento. Registre a decisão e o motivo."),
        },
        {
            "id": "saude_reg_testes",
            "title": _("Testes e segurança"),
            "text": _("Testes de unidade acham falhas cedo; testes de integração acham erros entre módulos. Revise papéis de acesso e entradas vulneráveis a SQL Injection, e teste a restauração do backup."),
        },
        {
            "id": "saude_reg_implantacao",
            "title": _("Implantação"),
            "text": _("O deploy depende de um checklist: documentação num só lugar, testes passando na pipeline, backup com restauração testada e plano de rollback. Servidor próprio, nuvem e contêineres têm custos diferentes."),
        },
    ]

    # Só conquistas que as cenas concedem hoje. conquista_guardiao_privacidade
    # fica de fora: scene_19 fixa a maturidade em 85 e nunca chega aos 91.
    ROUTES["saude"]["achievements"] = [
        {"id": "selo_codigo_sem_bugs", "inv": "selo_codigo_sem_bugs",
         "title": _("Código sem Bugs"),
         "desc": _("Terminou a codificação sem bugs detectados.")},
        {"id": "conquista_bug_vuln", "inv": "conquista_bug_vuln",
         "title": _("Caça a Bugs e Vulnerabilidades"),
         "desc": _("Encontrou pelo menos três bugs ou vulnerabilidades nos testes.")},
        {"id": "medalha_estudioso", "inv": "medalha_estudioso",
         "title": _("Medalha de Estudo"),
         "desc": _("Acertou todas as perguntas da tarde de estudos técnicos.")},
        {"id": "checklist_qualidade", "inv": "checklist_qualidade",
         "title": _("Checklist de Qualidade"),
         "desc": _("Buscou o checklist de qualidade para revisar requisitos e código.")},
        {"id": "badge_codigo_limpo", "inv": "badge_codigo_limpo",
         "title": _("Código Limpo"),
         "desc": _("Revisou a função e a validação antes da entrega.")},
        {"id": "badge_demo_colaborativa", "inv": "badge_demo_colaborativa",
         "title": _("Demo Colaborativa"),
         "desc": _("Apresentou a entrega à equipe em uma demonstração.")},
        {"id": "badge_pr_transparente", "inv": "badge_pr_transparente",
         "title": _("PR Transparente"),
         "desc": _("Documentou as decisões técnicas no pull request.")},
        {"id": "mindfulness_dev", "inv": "mindfulness_dev",
         "title": _("Mindfulness Dev"),
         "desc": _("Descansou e terminou o código pela manhã, sem virar a noite.")},
    ]

    ROUTES["saude"]["final"] = "final_saude"

    def final_saude():
        # Mesma regra da scene_21 (que continua calculando final_grade por
        # conta própria): soma da amizade dos 8 developers e dois selos.
        amizade_total = sum(getattr(store, "amizade_" + cid) for cid in DEVELOPERS)
        if (amizade_total >= 40 and "selo_codigo_sem_bugs" in store.inventario
                and "conquista_bug_vuln" in store.inventario):
            return "excelente"
        elif amizade_total >= 30:
            return "bom"
        return "ok"
