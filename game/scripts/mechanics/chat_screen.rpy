# chat_screen.rpy
# -------------------------------
# UI/FLUXO DO CHAT (apenas screen + label)
# -------------------------------
# Dados:    AMIGOS_DATA + bootstrap de current_assistant_id -> data/friends_data.rpy
# Backend:  is_web / normalize_resposta / send_* / send_and_update_chat -> python/chat_backend.rpy
# user_id:  generate_user_id + default user_id -> python/user_id.rpy
# Estilos:  chat_log_viewport / chat_send_button / *_msg_frame -> ui/styles/chat_styles.rpy

# --- TELA DE CHAT ---
screen chat_with_backend(char_name=NOME_DEVELOPER_REQUIREMENTS, char_image="images/characters/developer_requirements/portrait.png"):
    frame:
        xsize 600
        xalign 0.5
        yalign 0.5
        background "#111c"
        padding (32, 32)
        has vbox

        text _("Bate-papo") size 28 bold True xalign 0.5

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
            text _("[char_name] está digitando...") color "#ff9" size 18 xalign 0.5

        hbox:
            xfill True
            spacing 6
            input id "chat_input" value VariableInputValue("user_input") length 200 size 20 xmaximum 400 ymaximum 36 xalign 0.0
            textbutton _("Enviar") action [
                Function(send_and_update_chat, user_input)
            ] text_size 20 style "chat_send_button" sensitive (not is_waiting and user_input.strip() != "") xalign 1.0

        textbutton _("Fechar") action Return() xalign 1.0 text_size 16

    key "K_RETURN" action If(not is_waiting and user_input.strip() != "", Function(send_and_update_chat, user_input))

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

            # --- Incrementa afinidade dinamicamente (via helper com clamp 0..10) ---
            add_friendship_point(amigo_selecionado, 1)

        else:
            char_name = _("Contato")
            char_image = "images/characters/doutora_1/portrait.png"
            renpy.store.current_assistant_id = "asst_default"
    "Você decide conversar com [char_name]."
    call screen chat_with_backend(char_name=char_name, char_image=char_image)
    "Você fecha o app de conversas."
    return
