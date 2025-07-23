# Arquivo: characters.rpy

define carlos = Character("Carlos", color="#4CA3FF")
define julio = Character("Julio", color="#B8B8B8")
define rodrigo = Character("Rodrigo", color="#FFA500")
define sabrina = Character("Sabrina", color="#FF70A6")

# Imagens do Carlos
image carlos enthusiastic = "images/characters/carlos/enthusiastic.png"
image carlos confident = "images/characters/carlos/confident.png"
image carlos serious = "images/characters/carlos/serious.png"
image carlos thinking = "images/characters/carlos/thinking.png"

# Imagens do Julio
image julio neutral = "images/characters/julio/neutral.png"
image julio serious = "images/characters/julio/serious.png"
image julio thinking = "images/characters/julio/thinking.png"

# Imagens do Rodrigo
image rodrigo serious = "images/characters/rodrigo/serious.png"
image rodrigo thinking = "images/characters/rodrigo/thinking.png"

# Imagens da Sabrina
image sabrina enthusiastic = "images/characters/sabrina/enthusiastic.png"
image sabrina neutral = "images/characters/sabrina/neutral.png"
image sabrina serious = "images/characters/sabrina/serious.png"
image sabrina thinking = "images/characters/sabrina/thinking.png"


transform sprite_zoom:
    zoom 0.55
    xalign 0.5
    yalign 1.0

transform left_zoom:
    xalign 0.0
    yalign 1.0
    zoom 0.6

transform center_zoom:
    xalign 0.5
    yalign 1.0
    zoom 0.6

transform right_zoom:
    xalign 1.0
    yalign 1.0
    zoom 0.6