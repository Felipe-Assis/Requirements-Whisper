default player_name = "Alex"
default player_gender = ""
default player_avatar = "ideias"

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
