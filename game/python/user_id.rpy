# user_id.rpy
# -------------------------------
# Identificador único de jogador para o backend do chat.
# -------------------------------
# generate_user_id() fica em `init -1` (antes do `default user_id`).
# script.rpy chama generate_user_id() em `label start` (resolve globalmente).

init -1 python:
    import random
    def generate_user_id():
        return "USER" + str(random.randint(100000, 999999999))

default user_id = None
