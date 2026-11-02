# chat_styles.rpy
# -------------------------------
# Estilos da tela de chat (screen chat_with_backend). O painel usa os
# estilos nb_* (scripts/mechanics/notebook_screen.rpy).
# -------------------------------

style chat_log_viewport is viewport:
    xfill True

# Mesma linguagem dos botões nb_*: foco = fundo na cor de destaque com texto
# escuro; desabilitado = fundo escuro com texto apagado.
style chat_send_button is button:
    padding (24, 14)
    background Solid("#2a333d")
    hover_background Solid(gui.accent_color)
    insensitive_background Solid("#171f27")

style chat_send_button_text is text:
    size 24
    bold True
    color "#ffffff"
    hover_color "#101820"
    insensitive_color "#7d8894"

style chat_autor_text is text:
    size 18
    color "#c0c8d0"

style user_msg_frame:
    background Solid("#24425e")
    padding (14, 10)
    xalign 1.0
    xmaximum 720

style assistant_msg_frame:
    background Solid("#2a333d")
    padding (14, 10)
    xalign 0.0
    xmaximum 720
