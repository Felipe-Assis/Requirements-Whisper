# Relógio do canto. O Ren'Py esconde as telas de sobreposição (overlay_screens) enquanto uma tela
# modal está aberta, como o mapa do tempo livre. Por isso o desenho fica em `relogio_caixa`, que o
# mapa usa direto (screens im_mapa), e `top_right_clock` só o mostra nas demais situações.
screen relogio_caixa():
    frame:
        background None
        xalign 1.0
        yalign 0.0
        padding (16, 10)
        has vbox
        spacing 2

        # Relógio
        add "images/items/clock.png" xalign 1.0 yalign 0.0 xysize (64,64)

        # Horário (formato HH:MM)
        text "[game_hour:02d]:[game_minute:02d]":
            color "#F5F5DC"
            size 22
            bold True
            xalign 0.5
            yalign 0.0
            outlines [(2, "#00000099", 0, 0)]

screen top_right_clock():
    zorder 70
    if show_clock and not main_menu and not _menu and not renpy.get_screen("im_transicao") and not renpy.get_screen("im_mapa"):
        use relogio_caixa
