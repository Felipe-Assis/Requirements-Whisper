# state_flags.rpy
#
# Inventory item_* flags, per-contact contato_* (met) / disponivel_* (reachable
# now) gating flags, plus the inventory toggle and the selected-contact var.
# All kept at init -1 (same priority as before the split).

init -1:
    default inventory_enabled = True  # Set to True for testing, can change in-game

    default item_bloco_de_notas = False
    default item_caneta = False
    default item_celular = False
    default item_notebook = False
    default item_notebook_fechado = False
    default item_garrafinha = False
    default item_alarme = False
    default item_armario = False
    default item_mochila = False
    default item_mochila_aberta_vazia = False
    default item_mochila_com_agua = False
    default item_mochila_com_notebook = False
    default item_notebook_aberto = False


    # Variáveis de controle de quais contatos estão disponíveis
    default amigo_selecionado = ""

    # Conjunto de contatos já adicionados (preenchido por add_contact).
    default contacts = set()

    default contato_developer_ai = False
    default contato_developer_coding = False
    default contato_developer_management = False
    default contato_developer_requirements = False
    default contato_developer_project = False
    default contato_developer_quality = False
    default contato_developer_security = False
    default contato_developer_test = False
    default contato_doutora_1 = False
    default contato_doutora_2 = False


    default disponivel_developer_ai = False
    default disponivel_developer_coding = False
    default disponivel_developer_management = False
    default disponivel_developer_requirements = False
    default disponivel_developer_project = False
    default disponivel_developer_quality = False
    default disponivel_developer_security = False
    default disponivel_developer_test = False
    default disponivel_doutora_1 = True
    default disponivel_doutora_2 = True

    # Rotas Startup (st_*) e Corporativo (co_*). Disponibilidade controlada
    # por set_available, incluindo os stakeholders.
    default contato_st_mentora = False
    default contato_st_techlead = False
    default contato_st_mobile = False
    default contato_st_qualidade = False
    default contato_st_ceo = False
    default contato_st_estudante = False
    default contato_co_mentora = False
    default contato_co_legado = False
    default contato_co_dev = False
    default contato_co_qualidade = False
    default contato_co_supervisora = False
    default contato_co_solicitante = False

    default disponivel_st_mentora = False
    default disponivel_st_techlead = False
    default disponivel_st_mobile = False
    default disponivel_st_qualidade = False
    default disponivel_st_ceo = False
    default disponivel_st_estudante = False
    default disponivel_co_mentora = False
    default disponivel_co_legado = False
    default disponivel_co_dev = False
    default disponivel_co_qualidade = False
    default disponivel_co_supervisora = False
    default disponivel_co_solicitante = False


init python:
    # Lista canônica dos 8 desenvolvedores (equipe da rota saúde em ROUTES).
    DEVELOPERS = [
        "developer_ai",
        "developer_coding",
        "developer_management",
        "developer_requirements",
        "developer_quality",
        "developer_project",
        "developer_security",
        "developer_test",
    ]

    def set_available(*ids):
        # Reseta os disponivel_* da rota atual (route_contact_ids) e habilita
        # apenas os ids passados; set_available('all') habilita todos da rota.
        # Na saúde isso são só os 8 developers: as doutoras seguem à mão.
        managed = route_contact_ids()
        targets = managed if ids == ("all",) else ids
        for cid in managed:
            setattr(store, "disponivel_" + cid, cid in targets)
        # Nova cena (ou novo momento): o chat volta a poder dar +1 de amizade
        # uma vez por contato.
        store.chat_amizade_dada = set()
