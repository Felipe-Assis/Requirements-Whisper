# state_player.rpy
#
# Saved player profile vars collected in scene_1_quarto (nome, gênero, idade).
# Declared here as `default`s so they exist in the store/saves before any
# runtime assignment. init -1 keeps them defined ahead of scene start.

init -1:
    default player_name = ""
    default player_gender = ""
    default player_age = ""
