# chat_styles.rpy
# -------------------------------
# Estilos da tela de chat (screen chat_with_backend).
# -------------------------------

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
