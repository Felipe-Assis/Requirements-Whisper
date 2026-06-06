# chat_backend.rpy
# -------------------------------
# CLIENTE HTTP DO CHAT (LLM)
# -------------------------------
# Mantém o split desktop/web e a threading EXATAMENTE como antes:
#   - Desktop: threading.Thread + requests.post (timeout 60s).
#   - Web (emscripten): js.fetch via callback.
# A normalização de resposta é unificada num único normalize_resposta(raw) -> list[str].
# O backend pode retornar: uma string simples, uma JSON list, ou uma lista
# stringificada ("[...]"); normalize_resposta trata os três casos.

# URL base do backend, centralizada num único ponto (ambos os transportes a usam).
define BACKEND_BASE_URL = "http://15.229.14.83:8000"

init python:
    import requests
    import threading


    def is_web():
        try:
            import emscripten
            return True
        except ImportError:
            return False

    def normalize_resposta(resposta_api):
        if isinstance(resposta_api, str):
            try:
                import ast
                resposta_api = ast.literal_eval(resposta_api)
            except:
                resposta_api = [resposta_api]
        if resposta_api is None:
            resposta_api = []
        if isinstance(resposta_api, list):
            return [str(r) for r in resposta_api if isinstance(r, str) and r.strip()]
        return [str(resposta_api)]


    def send_message_to_backend(user_message, callback):
        if is_web():
            # Mostra aviso e retorna vazio no web
            callback(["Funcionalidade de chat indisponível na versão Web. Baixe o jogo para usar este recurso."])
        else:
            respostas = send_message_to_backend_desktop(user_message)
            callback(respostas)

    def send_message_to_backend_desktop(user_message):
        url = BACKEND_BASE_URL + "/chat/message/send"
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
            # Normalização única: trata string / None / list / stringified-list.
            return normalize_resposta(resposta_api)

        except Exception as e:
            print("[DEBUG] Erro ao enviar mensagem:", e)
            return [f"Erro ao enviar mensagem: {e}"]


    def send_message_to_backend_web(user_message, callback):
        from js import fetch, Object
        import json

        url = BACKEND_BASE_URL + "/chat/message/send"
        payload = {
            "user_id": renpy.store.user_id,
            "assistant_id": renpy.store.current_assistant_id,
            "message": user_message
        }

        # Constrói a função para processar a resposta
        def on_response(promise):
            # promise é uma JavaScript Promise
            def on_text(text):
                data = json.loads(text)
                respostas = normalize_resposta(data.get("response", []))
                callback(respostas)
            promise.text().then(on_text)
        # Chama o fetch e passa o callback para tratar a resposta
        fetch(
            url,
            Object.fromEntries([
                ["method", "POST"],
                ["headers", {"Content-Type": "application/json"}],
                ["body", json.dumps(payload)]
            ])
        ).then(on_response)


    def send_and_update_chat(user_message):
        global is_waiting, chat_history, user_input

        chat_history.append(("user", user_message))
        is_waiting = True
        user_input = ""
        renpy.exports.restart_interaction()

        def process_respostas(respostas):
            global is_waiting, chat_history
            print("[DEBUG] Adicionando respostas ao chat_history:", respostas)
            # respostas já vem normalizada (list[str]) por normalize_resposta;
            # aqui só iteramos e anexamos — sem 2º ast.literal_eval.
            if respostas:
                for resposta in respostas:
                    chat_history.append(("assistant", resposta))
            else:
                chat_history.append(("assistant", "Nenhuma resposta recebida."))
            is_waiting = False
            renpy.exports.restart_interaction()

        if is_web():
            # Chama a função de envio passando o processador como callback
            send_message_to_backend(user_message, process_respostas)
        else:
            # Desktop: threading para não travar UI
            import threading
            threading.Thread(target=lambda: send_message_to_backend(user_message, process_respostas)).start()
