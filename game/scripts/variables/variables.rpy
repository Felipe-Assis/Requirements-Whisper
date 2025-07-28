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
    default disponivel_doutora_1 = False
    default disponivel_doutora_2 = False

    default game_hour = 7      # Horas (inteiro, 0-23)
    default game_minute = 0    # Minutos (inteiro, 0-59)
    default show_clock = False  # Se quiser poder ocultar facilmente

    # Função para atualizar o horário, se preferir
    init python:
        def set_time(hour, minute):
            store.game_hour = hour
            store.game_minute = minute

        def advance_minutes(minutes):
            total = store.game_hour * 60 + store.game_minute + minutes
            store.game_hour = (total // 60) % 24
            store.game_minute = total % 60