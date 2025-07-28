# --- DICIONÁRIO DE AMIGOS E ASSISTANT_IDS ---
init -1 python:
    import random
    def generate_user_id():
        return "USER" + str(random.randint(100000, 999999999))
default user_id = None


init python:
    AMIGOS_DATA = {
        "developer_ai": {
            "name": NOME_DEVELOPER_AI,
            "portrait": "images/characters/developer_ai/portrait.png",
            "assistant_id": "asst_fbVtwWljzUZhHtmllEphxkYn"
        },
        "developer_requirements": {
            "name": NOME_DEVELOPER_REQUIREMENTS,
            "portrait": "images/characters/developer_requirements/portrait.png",
            "assistant_id": "asst_t5wjZ9SCpAbHNCg7utEcY2et"
        },
        "developer_coding": {
            "name": NOME_DEVELOPER_CODING,
            "portrait": "images/characters/developer_coding/portrait.png",
            "assistant_id": "asst_d8n3ntyqOsHfdBkJA2LqrZFh"
        },
        "developer_management": {
            "name": NOME_DEVELOPER_MANAGEMENT,
            "portrait": "images/characters/developer_management/portrait.png",
            "assistant_id": "asst_DzfYAhfiHWBPKborojHC50lZ"
        },
        "developer_quality": {
            "name": NOME_DEVELOPER_QUALITY,
            "portrait": "images/characters/developer_quality/portrait.png",
            "assistant_id": "asst_YkbAOJa4eudUqFL1NMTLkEAA"
        },
        "developer_project": {
            "name": NOME_DEVELOPER_PROJECT,
            "portrait": "images/characters/developer_project/portrait.png",
            "assistant_id": "asst_UrbLbKIjf7i5bBzDpvwTkAWn"
        },
        "developer_security": {
            "name": NOME_DEVELOPER_SECURITY,
            "portrait": "images/characters/developer_security/portrait.png",
            "assistant_id": "asst_FylyYRTtZVHXYpVpqCxVk6AX"
        },
        "developer_test": {
            "name": NOME_DEVELOPER_TEST,
            "portrait": "images/characters/developer_test/portrait.png",
            "assistant_id": "asst_r5MMYuijOxJHRmqdynMewgWA"
        },
        "doutora_1": {
            "name": NOME_DOUTORA_1,
            "portrait": "images/characters/doutora_1/portrait.png",
            "assistant_id": "asst_nUAGJlGDbfdxhxpADXSRdLwC"
        },
        "doutora_2": {
            "name": NOME_DOUTORA_2,
            "portrait": "images/characters/doutora_2/portrait.png",
            "assistant_id": "asst_0RVJbliiBedg7ADSndhb1BnS"
        },
        # Adicione outros se necessário...
    }

    # Inicializa o assistant_id global para uso no backend
    if not hasattr(renpy.store, "current_assistant_id"):
        renpy.store.current_assistant_id = "asst_default"



init python:
    import requests
    import threading

    def send_message_to_backend(user_message):
        url = "http://15.229.14.83:8000/chat/message/send"
#         payload = {
#             "user_id": "1",
#             "assistant_id": "asst_t5wjZ9SCpAbHNCg7utEcY2et",
#             "message": user_message
#         }
        payload = {
            "user_id": renpy.store.user_id,
            "assistant_id": renpy.store.current_assistant_id,
            "message": user_message
        }
        try:
            response = requests.post(url, json=payload, timeout=60)
            response.raise_for_status()
            data = response.json()
            print("[DEBUG] Resposta recebida do backend:", data)
            resposta_api = data.get("response", [])

            # --- Robustez total ---
            # Se vier string (não lista), tenta parsear para lista
            if isinstance(resposta_api, str):
                try:
                    import ast
                    resposta_api = ast.literal_eval(resposta_api)
                    print("[DEBUG] Parsed str to list:", resposta_api)
                except Exception as e:
                    resposta_api = [resposta_api]

            # Se vier None, vira lista vazia
            if resposta_api is None:
                resposta_api = []

            # Garante lista de strings
            if isinstance(resposta_api, list):
                # Só retorna as strings válidas
                respostas = [str(r) for r in resposta_api if isinstance(r, str) and r.strip()]
                return respostas
            else:
                # Se for string, retorna lista com ela
                return [str(resposta_api)]

        except Exception as e:
            print("[DEBUG] Erro ao enviar mensagem:", e)
            return [f"Erro ao enviar mensagem: {e}"]

    def send_and_update_chat(user_message):
        global is_waiting, chat_history, user_input
        chat_history.append(("user", user_message))
        is_waiting = True
        user_input = ""
        renpy.exports.restart_interaction()
        def task():
            global is_waiting, chat_history
            respostas = send_message_to_backend(user_message)
            print("[DEBUG] Adicionando respostas ao chat_history:", respostas)
            if respostas:
                for resposta in respostas:
                    # --- Limpa colchetes/aspas se resposta for string de lista ---
                    if resposta.startswith("[") and resposta.endswith("]"):
                        try:
                            import ast
                            items = ast.literal_eval(resposta)
                            if isinstance(items, list) and len(items) > 0:
                                for item in items:
                                    chat_history.append(("assistant", item))
                                continue  # Vai para a próxima resposta do loop
                        except:
                            pass
                        # Se falhar, adiciona texto "cru" sem colchetes
                        chat_history.append(("assistant", resposta.strip("[]").strip("'").strip('"')))
                    else:
                        chat_history.append(("assistant", resposta))
            else:
                chat_history.append(("assistant", "Nenhuma resposta recebida."))
            is_waiting = False
            renpy.exports.restart_interaction()
        threading.Thread(target=task).start()


# --- TELA DE CHAT ---
screen chat_with_backend(char_name=NOME_DEVELOPER_REQUIREMENTS, char_image="images/characters/developer_requirements/portrait.png"):
    frame:
        xsize 600
        xalign 0.5
        yalign 0.5
        background "#111c"
        padding (32, 32)
        has vbox

        text "Bate-papo" size 28 bold True xalign 0.5

        # Foto do personagem, centralizada e pequena
        add char_image xpos 0.5 ypos 0.0 xanchor 0.5 yanchor 0.0 zoom 0.18

        text "[char_name]" size 18 xalign 0.5 color "#aac" italic True

        viewport:
            draggable True
            mousewheel True
            ymaximum 350
            style "chat_log_viewport"

            vbox:
                spacing 10
                for autor, msg in chat_history:
                    if autor == "user":
                        frame:
                            style "user_msg_frame"
                            text "[msg]" size 21 color "#77c7ff" xalign 1.0
                    else:
                        frame:
                            style "assistant_msg_frame"
                            text "[msg]" size 21 color "#fff" xalign 0.0

        if is_waiting:
            text "[char_name] está digitando..." color "#ff9" size 18 xalign 0.5

        hbox:
            xfill True
            spacing 6
            input id "chat_input" value VariableInputValue("user_input") length 200 size 20 xmaximum 400 ymaximum 36 xalign 0.0
            textbutton "Enviar" action [
                Function(send_and_update_chat, user_input)
            ] text_size 20 style "chat_send_button" sensitive (not is_waiting and user_input.strip() != "") xalign 1.0

        textbutton "Fechar" action Return() xalign 1.0 text_size 16

    key "K_RETURN" action If(not is_waiting and user_input.strip() != "", Function(send_and_update_chat, user_input))

style chat_log_viewport:
    ysize 350
    xsize 550

style chat_send_button is default
style chat_log_viewport:
    ysize 350
    xsize 550

style chat_send_button is default
style chat_send_button:
    padding (12,6)
    background "#346aff"
    color "#fff"
    hover_background "#5a90fa"
    insensitive_background "#333c"
    size 20
    bold True

style user_msg_frame:
    background "#233a"
    padding (10, 8)
    xalign 1.0
    left_margin 100
    right_margin 0
    top_margin 2
    bottom_margin 2

style assistant_msg_frame:
    background "#2c2c2cdd"
    padding (10, 8)
    xalign 0.0
    left_margin 0
    right_margin 100
    top_margin 2
    bottom_margin 2

# --- LABEL EXEMPLO DE USO ---
# --- LABEL GENÉRICO DE CHAT ---
label chat_amigo:
    $ chat_history = []
    python:
        # Busca os dados do amigo selecionado
        amigo_info = AMIGOS_DATA.get(amigo_selecionado, None)
        if amigo_info:
            char_name = amigo_info["name"]
            char_image = amigo_info["portrait"]
            renpy.store.current_assistant_id = amigo_info["assistant_id"]

            # --- Incrementa afinidade dinamicamente ---
            var_name = f"amizade_{amigo_selecionado}"
            if var_name in store.__dict__:
                store.__dict__[var_name] = min(store.__dict__[var_name] + 1, 10)
            else:
                store.__dict__[var_name] = 1

        else:
            char_name = "Contato"
            char_image = "images/characters/generic_portrait.png"
            renpy.store.current_assistant_id = "asst_default"
    "Você decide conversar com [char_name]."
    call screen chat_with_backend(char_name=char_name, char_image=char_image)
    "Você fecha o app de conversas."
    return
