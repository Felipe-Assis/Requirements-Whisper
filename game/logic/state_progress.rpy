#progress.rpy
default progresso_roteiro = 0
default nivel_estresse = 0
default energia_diaria = 5
default inventario = []

default user_input = ""
default server_response = ""
default chat_history = []  # lista de tuplas (autor, mensagem)
default is_waiting = False
default pending_response = None  # buffer transitório: worker thread publica aqui; main thread drena
default chat_offline_idx = {}  # id do contato -> próxima fala da lista "offline" (rodízio)
default chat_amizade_dada = set()  # contatos que já deram +1 no chat desde o último set_available