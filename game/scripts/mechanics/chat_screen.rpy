# chat_screen.rpy
# -------------------------------
# UI/FLUXO DO CHAT (apenas screen + label)
# -------------------------------
# Dados:    AMIGOS_DATA + bootstrap de current_assistant_id -> data/friends_data.rpy
# Backend:  is_web / normalize_resposta / send_* / send_and_update_chat -> python/chat_backend.rpy
#           (contatos com assistant_id None respondem local: send_offline_reply)
# user_id:  generate_user_id + default user_id -> python/user_id.rpy
# Estilos:  chat_log_viewport / chat_send_button / *_msg_frame -> ui/styles/chat_styles.rpy

init python:
    def chat_rolar_para_o_fim(adj):
        # Chamado pelo viewport a cada layout. Só desce quando o conteúdo
        # cresce (mensagem nova), para não impedir a pessoa de rolar para cima.
        if adj.range != getattr(adj, "_rw_range", None):
            adj._rw_range = adj.range
            adj.change(adj.range)

# --- TELA DE CHAT ---
screen chat_with_backend(char_name=NOME_DEVELOPER_REQUIREMENTS, char_image="images/characters/developer_requirements/portrait.png"):
    modal True

    default chat_adj = ui.adjustment(ranged=chat_rolar_para_o_fim)
    $ maior = texto_maior_ativo()
    $ tam = 28 if maior else 22
    $ pode_enviar = (not is_waiting and user_input.strip() != "")

    # Dreno na MAIN thread: tica só enquanto o chat está aberto; aplica a
    # resposta publicada pela worker thread em store.pending_response.
    timer 0.1 repeat True action Function(drain_pending_response)

    add Solid("#000000b0")

    frame:
        style "nb_painel"
        align (0.5, 0.5)
        xsize 960
        padding (36, 30)

        vbox:
            spacing 14

            hbox:
                xfill True
                spacing 18
                add Transform(char_image, xysize=(96, 96), fit="contain") yalign 0.5
                vbox:
                    yalign 0.5
                    spacing 2
                    text "[char_name]" style "nb_titulo" size 36
                    if chat_is_offline(amigo_selecionado):
                        text _("Bate-papo · respostas roteirizadas, sem internet") style "nb_dica"
                    else:
                        text _("Bate-papo") style "nb_dica"
                textbutton _("Fechar"):
                    style "nb_botao"
                    xalign 1.0
                    yalign 0.5
                    id "chat_fechar"
                    action Return()

            viewport:
                style "chat_log_viewport"
                style_prefix "nb"
                id "chat_log"
                ysize (470 if maior else 430)
                yadjustment chat_adj
                draggable True
                mousewheel True
                scrollbars "vertical"
                vscrollbar_unscrollable "hide"

                vbox:
                    spacing 10
                    xsize 860
                    if not chat_history:
                        text _("Nenhuma mensagem ainda. Escreva abaixo e tecle Enter.") style "nb_texto" size tam color "#c0c8d0"
                    # Autor escrito acima de cada balão; lado e cor só reforçam.
                    for autor, msg in chat_history:
                        if autor == "user":
                            vbox:
                                xalign 1.0
                                spacing 2
                                text _("Você") style "chat_autor_text" xalign 1.0
                                frame:
                                    style "user_msg_frame"
                                    text "[msg]" style "nb_texto" size tam
                        else:
                            vbox:
                                xalign 0.0
                                spacing 2
                                text "[char_name]" style "chat_autor_text"
                                frame:
                                    style "assistant_msg_frame"
                                    text "[msg]" style "nb_texto" size tam

            if is_waiting:
                text _("[char_name] está digitando...") style "nb_dica" size tam
            else:
                null height (tam + 6)

            hbox:
                xfill True
                spacing 12
                # Borda na cor de destaque: mostra onde o texto entra.
                frame:
                    background Solid(gui.accent_color)
                    padding (3, 3)
                    xsize 720
                    frame:
                        background Solid("#1f2730")
                        padding (14, 10)
                        xfill True
                        input:
                            id "chat_input"
                            value VariableInputValue("user_input")
                            length 200
                            size tam
                            color "#ffffff"
                            xmaximum 680
                textbutton _("Enviar"):
                    style "chat_send_button"
                    xalign 1.0
                    yalign 0.5
                    sensitive pode_enviar
                    action Function(send_and_update_chat, user_input)

            text _("Enter envia · Esc ou Fechar volta para a cena."):
                style "nb_dica"

    key "K_RETURN" action If(pode_enviar, Function(send_and_update_chat, user_input))
    key "game_menu" action Return()

# --- LABEL EXEMPLO DE USO ---
# --- LABEL GENÉRICO DE CHAT ---
label chat_amigo:
    $ chat_history = []
    $ pending_response = None   # descarta resposta tardia de uma conversa anterior
    $ is_waiting = False
    python:
        # Busca os dados do amigo selecionado
        amigo_info = AMIGOS_DATA.get(amigo_selecionado, None)
        if amigo_info:
            char_name = amigo_info["name"]
            char_image = amigo_info["portrait"]
            renpy.store.current_assistant_id = amigo_info["assistant_id"]

            # +1 de amizade só na primeira conversa com cada contato desde o
            # último set_available; abrir o chat de novo não acumula pontos.
            if amigo_selecionado not in chat_amizade_dada:
                chat_amizade_dada.add(amigo_selecionado)
                add_friendship_point(amigo_selecionado, 1)

        else:
            char_name = _("Contato")
            char_image = "images/characters/doutora_1/portrait.png"
            renpy.store.current_assistant_id = "asst_default"
    "Você decide conversar com [char_name]."
    call screen chat_with_backend(char_name=char_name, char_image=char_image)
    "Você fecha o app de conversas."
    return
