screen top_right_clock():
    if show_clock:
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
