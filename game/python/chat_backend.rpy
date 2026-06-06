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
#
# i18n: as respostas do backend chegam em RUNTIME e NÃO passam pela tradução
# estática do Ren'Py (tl/). Para localizar o chat, mude o BACKEND — ex.: um campo
# "language" no payload, ou assistant_id por idioma em AMIGOS_DATA. Só os literais
# locais aqui (avisos/erros) são traduzíveis via _().

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
            callback([_("Funcionalidade de chat indisponível na versão Web. Baixe o jogo para usar este recurso.")])
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
            return [_("Erro ao enviar mensagem: {e}").format(e=e)]


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


    def process_respostas(respostas):
        # Roda na WORKER thread (desktop) ou no callback do fetch (web).
        # NÃO toca chat_history/is_waiting aqui (mutar store fora da main thread
        # é inseguro no 8.5). Apenas publica no buffer; drain_pending_response()
        # drena na main thread via o timer da screen chat_with_backend.
        store.pending_response = respostas if respostas else []
        renpy.restart_interaction()  # acorda a tela; o timer drena na main thread

    def drain_pending_response():
        # Roda na MAIN thread (via timer da screen). Único ponto que muta
        # chat_history/is_waiting a partir de uma resposta do backend.
        if store.pending_response is not None:
            if store.pending_response:
                for r in store.pending_response:
                    chat_history.append(("assistant", r))
            else:
                chat_history.append(("assistant", _("Nenhuma resposta recebida.")))
            store.pending_response = None
            store.is_waiting = False
            renpy.restart_interaction()

    def __reset_chat_transient():
        # Estado transitório do chat nunca deve sobreviver a save/load/rollback.
        store.is_waiting = False
        store.user_input = ""
        store.server_response = ""
        store.pending_response = None
    config.after_load_callbacks = config.after_load_callbacks + [__reset_chat_transient]


    def send_and_update_chat(user_message):
        global is_waiting, chat_history, user_input

        chat_history.append(("user", user_message))
        is_waiting = True
        user_input = ""
        renpy.exports.restart_interaction()

        if is_web():
            # Chama a função de envio passando o processador como callback
            send_message_to_backend(user_message, process_respostas)
        else:
            # Desktop: threading para não travar UI
            import threading
            threading.Thread(target=lambda: send_message_to_backend(user_message, process_respostas)).start()
