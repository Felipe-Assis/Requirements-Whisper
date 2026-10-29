label start:
    call scene_1_quarto from _scene_1_quarto
    hide screen learning_hud
    hide screen learning_notebook
    hide screen inv_quick
    hide screen inventory_screen
    $ notebook_available = False
    return
