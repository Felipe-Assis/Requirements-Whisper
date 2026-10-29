default alarm_off = False
default notebook_taken = False
default mochila_taken = False
default notebook_in_bag = False
default clothes_changed = False

init python:
    def finish_player_profile():
        # Nomes aparecem nas falas; remova tags de formatação do Ren'Py.
        name = player_name.replace("{", "").replace("}", "").strip()
        store.player_name = name or "Alex"

style rw_panel is frame:
    background Solid("#142b38f5")
    padding (36, 32)

style rw_heading is text:
    color "#eaf3f7"
    size 46
    bold True

style rw_caption is text:
    color "#d0dedb"
    size 28

style rw_action is button:
    background Solid("#294651")
    hover_background Solid("#51c8b6")
    selected_background Solid("#51c8b6")
    padding (24, 18)
    xminimum 280
    yminimum 72

style rw_action_text is button_text:
    color "#eaf3f7"
    hover_color "#122532"
    selected_color "#122532"
    size 30

screen room_action(step, heading, description, picture, action_label, flag):
    modal True
    $ advance = [SetVariable(flag, True), Return(True)]
    frame:
        style "rw_panel"
        xpos 80
        ypos 150
        xsize 650
        vbox:
            spacing 28
            text "PREPARAÇÃO · [step]/5" color "#51c8b6" size 25
            text heading style "rw_heading" xmaximum 575
            text description style "rw_caption" xmaximum 575
            null height 12
            textbutton action_label style "rw_action" action advance xfill True default_focus True id "room_advance"
            text "Clique no objeto ou use as setas e Enter. Não há limite de tempo." style "rw_caption" size 24 xmaximum 575
    button:
        xpos 820
        ypos 170
        xsize 940
        ysize 650
        background Solid("#142b38")
        hover_background Solid("#51c8b6")
        padding (8, 8)
        action advance
        alt action_label
        add picture xysize (924, 634) fit "contain" align (0.5, 0.5)
    text action_label xpos 820 ypos 850 color "#eaf3f7" size 30

screen pointclick_quarto_1():
    use room_action(1, "Um novo começo", "Desligue o despertador. Hoje você vai procurar seu primeiro estágio em software.", "images/items/alarme.png", "Desligar despertador", "alarm_off")

screen pointclick_quarto_2():
    use room_action(2, "Seu ponto de partida", "Abra o notebook para conhecer as oportunidades e escolher um projeto.", "images/items/notebook_aberto.png", "Abrir notebook", "notebook_taken")

screen pointclick_quarto_3():
    use room_action(3, "Tudo à mão", "Pegue sua mochila para levar o material ao estágio.", "images/items/mochila.png", "Pegar mochila", "mochila_taken")

screen pointclick_guardar_notebook():
    use room_action(4, "Prepare o material", "Guarde o notebook na mochila. Você ainda poderá consultá-lo no inventário.", "images/items/mochila_aberta_vazia.png", "Guardar notebook", "notebook_in_bag")

screen pointclick_guarda_roupa():
    use room_action(5, "Hora de sair", "Escolha uma roupa confortável para conhecer sua equipe. Sua aparência não muda suas oportunidades.", "images/items/armario.png", "Trocar de roupa e sair", "clothes_changed")

screen player_formulario():
    modal True
    zorder 50
    add Solid("#122532ee")
    frame:
        style "rw_panel"
        align (0.5, 0.44)
        xsize 1280
        vbox:
            spacing 24
            text "Quem vive esta história?" style "rw_heading"
            text "Personalize seu personagem ou continue como Alex. Use um nome fictício." style "rw_caption"
            text "Nome do personagem (opcional)" style "rw_caption"
            frame:
                background Solid("#294651")
                padding (20, 14)
                xsize 900
                input:
                    value VariableInputValue("player_name")
                    length 24
                    exclude "{}[]\\\n\r"
                    color "#eaf3f7"
                    size 36
                    xsize 850
            text "Emblema do perfil (só muda sua identificação)" style "rw_caption"
            hbox:
                spacing 18
                for badge_id, badge_name in [("ideias", "Ideias"), ("codigo", "Código"), ("dialogo", "Diálogo")]:
                    textbutton (badge_name + (" · selecionado" if player_avatar == badge_id else "")):
                        style "rw_action"
                        selected player_avatar == badge_id
                        action SetVariable("player_avatar", badge_id)
                        id ("profile_badge_" + badge_id)
            hbox:
                spacing 24
                use profile_badge(player_avatar)
                vbox:
                    spacing 10
                    text "Prévia do emblema" style "rw_caption"
                    text ("Seu perfil: " + (player_name.strip() or "Alex")) style "rw_caption" substitute False
            text "Não pedimos idade nem dados de contato. O perfil fica neste jogo." style "rw_caption" size 24
            hbox:
                spacing 24
                textbutton "Continuar" style "rw_action" action [Function(finish_player_profile), Return(True)] id "profile_continue"
                textbutton "Usar Alex" style "rw_action" action [SetVariable("player_name", "Alex"), Return(True)] id "profile_default"
