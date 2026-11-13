# Brilho imediato sinaliza mouse e foco sem animar a cena.
screen scene_object(asset, caption, action, widget_id, x, y, width=210, height=160):
    fixed:
        xpos x ypos y xsize width ysize (height + 42)
        imagebutton:
            idle Transform("images/objects/" + asset + ".png", xysize=(width, height), fit="contain")
            hover Transform("images/objects/" + asset + ".png", xysize=(width, height), fit="contain", matrixcolor=BrightnessMatrix(0.18))
            action action
            alt caption
            focus_mask True
            xysize (width, height)
            padding (0, 0)
            id widget_id
        frame:
            background Solid("#0b1e29c8")
            padding (9, 4)
            xalign 0.5 ypos height
            text caption size 21 color "#eaf3f7" xmaximum (width - 18) text_align 0.5

style scene_pin_button is button:
    background None
    hover_background Solid("#0b1e29dc")
    padding (12, 8)
    yminimum 44

style scene_pin_button_text is text:
    size 23
    color "#eaf3f7"
    hover_color "#e7b565"
    outlines [(2, "#0b1e29", 0, 0)]

screen scene_pin(caption, action, widget_id, x, y):
    textbutton ("● " + caption):
        style "scene_pin_button"
        xpos x ypos y
        action action
        alt caption
        id widget_id
