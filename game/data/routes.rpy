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
