default player_name = "Alex"
default player_gender = ""
default player_avatar = "ideias"

screen profile_badge(badge):
    frame:
        background Solid("#294651")
        padding (18, 12)
        xsize 180
        ysize 110
        vbox:
            align (0.5, 0.5)
            spacing 2
            if badge == "codigo":
                text "</>" color "#51c8b6" size 44 xalign 0.5
                text "Código" color "#eaf3f7" size 24 xalign 0.5
            elif badge == "dialogo":
                text "[ [ ] ]" substitute False color "#51c8b6" size 40 xalign 0.5
                text "Diálogo" color "#eaf3f7" size 24 xalign 0.5
            else:
                text "*" color "#51c8b6" size 48 xalign 0.5
                text "Ideias" color "#eaf3f7" size 24 xalign 0.5

define player = Character("[player_name]", color="#51c8b6")

image sabrina neutral = "images/characters/sabrina/neutral.png"
image sabrina thinking = "images/characters/sabrina/thinking.png"
image sabrina enthusiastic = "images/characters/sabrina/enthusiastic.png"
image carlos confident = "images/characters/carlos/confident.png"
image carlos thinking = "images/characters/carlos/thinking.png"
image carlos serious = "images/characters/carlos/serious.png"
image carlos enthusiastic = "images/characters/carlos/enthusiastic.png"
image julio neutral = "images/characters/julio/neutral.png"
image julio thinking = "images/characters/julio/thinking.png"
image julio retorno = "images/characters/julio/return.png"
image carlos retorno = "images/characters/carlos/return.png"
image lia retorno = "images/characters/lia/return.png"
image rodrigo chuva = "images/characters/rodrigo/rain.png"

transform colleague_left:
    xalign 0.12
    yalign 1.0
    ysize 940
    fit "contain"

transform colleague_right:
    xalign 0.88
    yalign 1.0
    ysize 940
    fit "contain"
