# Capturas para revisão humana, opcionais para não criar baselines por acidente.
testsuite visual:
    enabled False

    testcase desktop:
        if not screen "main_menu":
            run MainMenu(confirm=False)
        pause until screen "main_menu"
        pause 0.6
        screenshot "review/main_menu.png"
        click "Acessibilidade"
        pause until screen "rw_accessibility"
        pause 0.6
        screenshot "review/accessibility.png"
        run Return()
        run Start()
        advance until screen "pointclick_quarto_1"
        screenshot "review/room.png"
        click id "room_advance"
        advance until screen "pointclick_quarto_2"
        click id "room_advance"
        advance until screen "player_formulario"
        screenshot "review/profile.png"
        click id "profile_default"
        advance until screen "choice"
        $ persistent.rw_large_text = True
        screenshot "review/choices_large.png"
        $ chosen_job = "IDT-UFRJ"
        run Hide("inv_quick")
        run Jump("scene_2_estagio")
        advance
        pause 0.6
        screenshot "review/dialogue_large.png"
        advance until screen "choice"
        screenshot "review/mission_large.png"
        click "Peço que Carlos conte"
        advance until screen "choice"
        click "Pergunto o que Carlos precisa conseguir"
        advance until screen "choice"
        click "Uma reserva das 14h às 15h"
        advance until screen "choice"
        click "Pergunto se é necessário um intervalo"
        advance until screen "choice"
        screenshot "review/review_large.png"
        click "Planejar a primeira entrega"
        advance until screen "choice"
        screenshot "review/planning_large.png"
        keysym "K_PAGEDOWN"
        pause 0.2
        screenshot "review/planning_scrolled_large.png"
        click "Voltar ao resumo da missão"
        pause until "Planejar a primeira entrega"
        $ persistent.rw_large_text = False
