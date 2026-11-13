label clock_test_room:
    $ campaign_active = True
    $ lab_active = False
    $ campaign_set_clock("support", "Segunda", "14h30", "day")
    show screen campaign_time_hud
    scene expression Transform(campaign_clock["image"], xysize=(1920, 1080), fit="cover")
    "O turno da tarde começa."
    $ campaign_set_clock("support", "Semana seguinte", "10h10", "rain")
    scene expression Transform(campaign_clock["image"], xysize=(1920, 1080), fit="cover")
    "A equipe retorna em dia de chuva."
    jump campaign_hub

testsuite scene_clock:
    before testcase:
        if not screen "main_menu":
            run MainMenu(confirm=False)
        pause until screen "main_menu"

    testcase variants_are_packaged:
        assert eval all(renpy.loadable("images/bg/" + image + ".png") for variants in SCENE_VARIANTS.values() for image in variants.values())
        assert eval all(renpy.loadable("images/characters/" + character + "/" + outfit + ".png") for character, outfit in (("sabrina", "return"), ("lia", "return"), ("julio", "return"), ("carlos", "return"), ("rodrigo", "rain")))
        assert eval all(renpy.loadable("images/objects/" + item + ".png") for item in ("clipboard", "phone", "laptop", "notebook"))

    testcase save_restores_clock_and_scene:
        run Start("clock_test_room")
        pause until "O turno da tarde começa."
        assert eval campaign_clock["time"] == "14h30"
        $ renpy.take_screenshot()
        $ renpy.save("qa-clock-room")
        advance until "A equipe retorna em dia de chuva."
        assert eval campaign_clock["lighting"] == "rain"
        assert eval campaign_clock["image"] == "images/bg/suporte_chuva.png"
        $ renpy.load("qa-clock-room")
        pause until "O turno da tarde começa."
        assert eval campaign_clock["image"] == "images/bg/suporte_dia.png"
        assert eval campaign_clock["time"] == "14h30"
