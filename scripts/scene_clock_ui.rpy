screen campaign_time_hud():
    zorder 19
    if campaign_active:
        key "K_i" action Show("campaign_bag")
        if not lab_active:
            textbutton "Mochila · I":
                style "lab_button" text_size 26
                xpos 1590 ypos 20 xsize 290
                action Show("campaign_bag")
                id "campaign_dialog_bag"
    if campaign_active and not lab_active and campaign_clock:
        frame:
            background Solid("#142b38ed")
            xpos 30 ypos 20 padding (20, 12)
            text campaign_clock_caption() color "#e7b565" size 24 xmaximum 1440
