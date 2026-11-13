default student_introduced = False
default student_schedule = {"tuesday": None, "thursday": None}
default student_visits = []
default student_evidence = []
default student_study_renegotiated = False
default student_course_done = False
default student_agreement = ""
default student_agreed_schedule = {}
default student_feedback = "Escolha um local ou organize as duas noites da semana."

init python:
    STUDENT_SLOTS = {"tuesday": "Terça à noite", "thursday": "Quinta à noite"}
    STUDENT_ACTIVITIES = {"study": "Grupo de estudo", "workshop": "Oficina / curso", "overtime": "Plantão extra", "rest": "Descanso"}
    STUDENT_PLACES = {"campus": "Campus · grupo de estudo", "workshop": "Oficina comunitária · curso de protótipo"}
    STUDENT_FACTS = {
        "campus": "O grupo se reúne terça à noite. A colega pode combinar quinta se você conversar antes; a troca precisa ficar explícita.",
        "workshop": "O curso gratuito de protótipo funciona na quinta à noite, na oficina do outro lado da cidade. A vaga ocupa essa noite, incluindo o deslocamento.",
    }
    STUDENT_TIP = "Exemplo de usabilidade: antes de excluir um registro, mostre qual item será afetado. Cancelar deve preservar os dados; depois de confirmar, ofereça desfazer. Teste as três ações com uma pessoa."

    def student_reset():
        store.student_introduced = False
        store.student_schedule = {"tuesday": None, "thursday": None}
        store.student_visits = []
        store.student_evidence = []
        store.student_study_renegotiated = False
        store.student_course_done = False
        store.student_agreement = ""
        store.student_agreed_schedule = {}
        store.student_feedback = "Escolha um local ou organize as duas noites da semana."

    def student_assign(slot, activity):
        if slot not in STUDENT_SLOTS or activity not in STUDENT_ACTIVITIES:
            store.student_feedback = "Escolha uma das duas noites e uma atividade da lista."
            return False
        if slot == "thursday" and store.student_course_done:
            store.student_feedback = "Quinta concluída: você participou do curso. Essa noite fica no histórico e não pode receber outro compromisso nesta semana."
            return False
        if activity == "workshop" and slot != "thursday":
            store.student_feedback = "A oficina oferece o curso somente quinta à noite, incluindo o deslocamento. Sua agenda foi preservada."
            return False
        if activity == "study" and slot != "tuesday" and not store.student_study_renegotiated:
            store.student_feedback = "O grupo se reúne terça. Use ‘Combinar estudo na quinta’ antes de reservar outro horário."
            return False
        current = store.student_schedule[slot]
        if current and current != activity:
            store.student_feedback = "Essa noite já tem um compromisso. Libere a noite antes de escolher outro; nada foi substituído."
            return False
        store.student_schedule = dict(store.student_schedule, **{slot: activity})
        store.student_feedback = STUDENT_SLOTS[slot] + ": " + STUDENT_ACTIVITIES[activity] + ". Você pode liberar e reorganizar."
        return True

    def student_clear(slot):
        if slot not in STUDENT_SLOTS:
            return False
        if slot == "thursday" and store.student_course_done:
            store.student_feedback = "Quinta concluída: o curso e o deslocamento já aconteceram. Essa noite permanece no histórico desta semana."
            return False
        store.student_schedule = dict(store.student_schedule, **{slot: None})
        store.student_feedback = STUDENT_SLOTS[slot] + " liberada. O acordo anterior fica no caderno até uma nova conversa com Sabrina."
        return True

    def student_renegotiate_study():
        store.student_study_renegotiated = True
        store.student_feedback = "A colega pode estudar quinta. O novo horário fica combinado quando você o reservar na agenda."
        return True

    def student_visit(place):
        if place not in STUDENT_PLACES:
            return False
        if place not in store.student_visits:
            store.student_visits = store.student_visits + [place]
        return True

    def student_location_clock(place):
        if place == "campus":
            for slot, day in (("tuesday", "Terça-feira"), ("thursday", "Quinta-feira")):
                if store.student_schedule[slot] == "study":
                    return day, "20h", "night"
            return "Visita ao campus", "16h", "day"
        if store.student_course_done:
            return "Quinta-feira", "20h", "night"
        return "Visita à oficina", "16h", "day"

    def student_inspect(place):
        if place not in STUDENT_FACTS:
            return False
        if place not in store.student_evidence:
            store.student_evidence = store.student_evidence + [place]
        store.student_feedback = STUDENT_FACTS[place]
        return True

    def student_take_course():
        if store.student_course_done:
            store.student_feedback = "O curso de quinta já foi concluído. Você pode reabrir a dica no caderno."
            return False
        if "workshop" not in store.student_visits or store.student_schedule["thursday"] != "workshop":
            store.student_feedback = "Para participar, visite a oficina e reserve a quinta para o curso. Você pode seguir os projetos sem fazer isso."
            return False
        store.student_course_done = True
        store.student_feedback = "Quinta concluída na oficina. A dica de usabilidade fica no caderno; essa noite permanece no histórico da semana."
        return True

    def student_agreement_pending():
        return bool(store.student_agreement) and store.student_agreed_schedule != store.student_schedule

    def student_agree():
        overtime = [STUDENT_SLOTS[slot].lower() for slot, activity in store.student_schedule.items() if activity == "overtime"]
        study = [STUDENT_SLOTS[slot].lower() for slot, activity in store.student_schedule.items() if activity == "study"]
        review = ("Sabrina reserva revisão do estágio no plantão de " + " e ".join(overtime) + ".") if overtime else "Sabrina replaneja a revisão do estágio para o horário regular, sem plantão extra."
        group = ("Estudo com a colega: " + " e ".join(study) + ".") if study else "Com a colega, fica combinado buscar outro horário de estudo, fora dessas duas noites."
        store.student_agreement = review + " " + group
        store.student_agreed_schedule = dict(store.student_schedule)
        store.student_feedback = "Acordo registrado. Compromissos ainda não realizados podem ser reorganizados."
        return True

    def student_summary():
        visits = ", ".join(STUDENT_PLACES[place] for place in store.student_visits) or "nenhum local ainda"
        agenda = "; ".join(STUDENT_SLOTS[slot] + ": " + STUDENT_ACTIVITIES.get(activity, "sem compromisso") for slot, activity in store.student_schedule.items())
        text = "Visitas: " + visits + ". Agenda: " + agenda + ". "
        text += store.student_agreement or "Ainda sem acordo com Sabrina; esta atividade é opcional."
        if student_agreement_pending():
            text += " A agenda mudou: retome a conversa para atualizar o acordo."
        for place in store.student_evidence:
            text += " Pista: " + STUDENT_FACTS[place]
        if store.student_course_done:
            text += " Quinta concluída na oficina, incluindo o deslocamento. Dica de usabilidade do curso: " + STUDENT_TIP
        return text

screen student_city_screen():
    modal True
    zorder 40
    use campaign_workspace("Entre o estágio e a faculdade", campaign_clock_caption() + " · visitas, pistas e agenda ficam salvas nesta partida."):
        hbox:
            spacing 30
            fixed:
                xsize 1000 ysize 650
                use lab_scene_image(campaign_clock["image"], 1000, 650)
                frame:
                    background Solid("#142b38ed") padding (20, 14)
                    xpos 25 ypos 25 xsize 950
                    text "Da empresa, dois caminhos pela cidade. Cada local traz uma pista para planejar sua semana." style "lab_body" size 28
                use scene_pin("Campus", Return("campus"), "student_hotspot_campus", 145, 320)
                use scene_pin("Oficina", Return("workshop"), "student_hotspot_workshop", 825, 335)
            viewport:
                xsize 730 ysize 650 mousewheel True draggable True scrollbars "vertical" arrowkeys True pagekeys True
                vbox:
                    spacing 18 xsize 690
                    text "Escolha pelo cenário ou pela lista" style "rw_heading" size 32
                    for place, caption in STUDENT_PLACES.items():
                        textbutton (caption + (" · visitado" if place in student_visits else " · visitar")) style "lab_button" text_size 26 xfill True action Return(place) id ("student_map_" + place)
                    text "Terça: grupo de estudo. Quinta: curso na oficina, com o trajeto incluído." style "lab_body" size lab_ui_size(25)
                    for slot, caption in STUDENT_SLOTS.items():
                        text (caption + ": " + STUDENT_ACTIVITIES.get(student_schedule[slot], "sem compromisso")) style "lab_note" size 26
                    textbutton "Organizar minhas noites" style "lab_button" text_size 27 xfill True action Return("schedule") id "student_schedule_open"
                    if student_course_done:
                        textbutton "Reabrir dica do curso" style "lab_button" text_size 26 action Show("student_tip_screen") id "student_tip_open"
    use campaign_footer(student_feedback)
    use lab_continue("Voltar aos projetos", Return("hub"), True, "student_city_back")

screen student_location_screen(place):
    modal True
    zorder 40
    use campaign_workspace(STUDENT_PLACES[place], campaign_clock_caption() + " · Visitar não reserva uma noite automaticamente."):
        hbox:
            spacing 30
            fixed:
                xsize 1000 ysize 650
                use lab_scene_image(("images/bg/campus_noite_mesa.png" if campaign_clock["lighting"] == "night" else "images/bg/campus_mesa.png") if place == "campus" else campaign_clock["image"], 1000, 650)
                use scene_object(("notebook" if place == "campus" else "clipboard"), ("Caderno do grupo" if place == "campus" else "Horário da oficina"), Function(lab_ui_apply, student_inspect, place), "student_object", (365 if place == "campus" else 90), (420 if place == "campus" else 145), 240, 165)
            viewport:
                xsize 730 ysize 650 mousewheel True draggable True scrollbars "vertical" arrowkeys True pagekeys True
                vbox:
                    spacing 18 xsize 690
                    text ("Campus · sala do grupo de estudo" if place == "campus" else "Centro comunitário · sala de protótipos") style "rw_heading" size 32
                    text (("Na noite reservada para o estudo, o caderno do grupo está sobre a mesa." if campaign_clock["lighting"] == "night" else "Antes das aulas, uma colega deixa o horário do grupo no caderno da mesa.") if place == "campus" else ("Depois do curso, o mural e o exemplo de usabilidade continuam disponíveis." if student_course_done else "Na visita da tarde, você encontra protótipos de papel e o mural com o horário do curso gratuito.")) style "lab_body" size lab_ui_size(26)
                    textbutton ("Ler caderno do grupo" if place == "campus" else "Ler mural da oficina") style "lab_button" text_size 26 xfill True action Function(lab_ui_apply, student_inspect, place) id "student_inspect_list"
                    textbutton "Organizar minhas noites" style "lab_button" text_size 26 xfill True action Return("schedule") id "student_location_schedule"
                    if place == "workshop":
                        textbutton ("Revisar exemplo do curso" if student_course_done else "Participar do curso · opcional") style "lab_button" text_size 26 xfill True action (Show("student_tip_screen") if student_course_done else Return("course")) id "student_course"
                    if place in student_evidence:
                        text "PISTA REGISTRADA" color "#e7b565" size 24
                        text STUDENT_FACTS[place] style "lab_body" size lab_ui_size(25)
                    if place == "workshop" and student_course_done:
                        text STUDENT_TIP style "lab_body" size lab_ui_size(25)
    use campaign_footer(student_feedback)
    use lab_continue("Voltar ao mapa", Return("map"), True, "student_location_back")

screen student_schedule_screen():
    modal True
    zorder 40
    use campaign_workspace("Minha agenda · duas noites na semana", "20h · Planejamento em casa. Libere a noite antes de trocar; atividades concluídas ficam no histórico."):
        viewport:
            id "student_schedule_scroll"
            ysize 640 xfill True mousewheel True draggable True scrollbars "vertical" arrowkeys True pagekeys True
            frame:
                style "artifact_paper" xfill True
                vbox:
                    spacing 14
                    text "FACULDADE / ESTÁGIO / TEMPO PESSOAL · não é preciso preencher as duas noites." style "artifact_muted" size 22
                    hbox:
                        spacing 24
                        hbox:
                            spacing 20
                            for slot, caption in STUDENT_SLOTS.items():
                                frame:
                                    style "artifact_card" xsize 530
                                    vbox:
                                        spacing 10
                                        text ("TERÇA" if slot == "tuesday" else "QUINTA") style "artifact_heading" size 32
                                        frame:
                                            background Solid("#dce6e5") padding (14, 10) xfill True
                                            text "NOITE · um compromisso" style "artifact_muted" size 23
                                        text STUDENT_ACTIVITIES.get(student_schedule[slot], "Noite livre") style "artifact_heading" size lab_ui_size(28)
                                        text ("Concluído · curso e trajeto" if slot == "thursday" and student_course_done else "Reservado · libere para trocar" if student_schedule[slot] else "Escolha um cartão ou deixe livre") style "artifact_muted" size 23
                                        for choices in (("study", "workshop"), ("overtime", "rest")):
                                            hbox:
                                                spacing 12
                                                for activity in choices:
                                                    textbutton STUDENT_ACTIVITIES[activity]:
                                                        style "artifact_button" text_size 24 xsize 230
                                                        selected student_schedule[slot] == activity
                                                        action Function(lab_ui_apply, student_assign, slot, activity)
                                                        id ("student_" + slot + "_" + activity)
                                        textbutton "Liberar noite" style "artifact_button" text_size 24 xfill True action Function(lab_ui_apply, student_clear, slot) id ("student_clear_" + slot)
                        vbox:
                            spacing 16 xsize 590
                            text "Horários disponíveis" style "artifact_heading" size 29
                            text "Terça: grupo de estudo. Quinta: oficina, com o trajeto de ônibus incluído na reserva." style "artifact_ink" size lab_ui_size(25)
                            textbutton "Combinar estudo na quinta" style "artifact_button" text_size 25 xfill True action Function(lab_ui_apply, student_renegotiate_study) id "student_renegotiate"
                            if student_study_renegotiated:
                                text "Colega: quinta também funciona, se você reservar esse horário." style "artifact_note" size 24
                            text "Sem plantão extra, Sabrina reorganiza a revisão no horário regular. Se o grupo não couber, combine outro horário com sua colega." style "artifact_ink" size lab_ui_size(25)
                            textbutton "Conversar com Sabrina" style "artifact_primary" text_size 27 xfill True action Return("talk") id "student_talk"
                            if student_agreement:
                                text ("Agenda alterada; converse de novo." if student_agreement_pending() else "Acordo atualizado no caderno.") style "artifact_note" size 24
    use campaign_footer(student_feedback)
    use lab_continue("Voltar ao mapa", Return("map"), True, "student_schedule_back")

screen student_course_confirmation():
    modal True
    zorder 40
    use campaign_workspace("Participar do curso na quinta?", "Avançar para o curso conclui a quinta à noite desta semana, incluindo o trajeto de ônibus."):
        frame:
            style "artifact_paper" xfill True
            vbox:
                spacing 24
                use artifact_bar("Reserva · oficina comunitária", "QUINTA / NOITE · curso gratuito de protótipo + trajeto de ônibus")
                text "Você irá à oficina na quinta, participará do curso e voltará para casa. Depois, essa noite ficará no histórico e não poderá receber plantão, estudo ou outro compromisso." style "artifact_ink" size lab_ui_size(31) xmaximum 1560
                text "Se quiser reorganizar primeiro, volte ao planejamento." style "artifact_muted" size lab_ui_size(28)
                textbutton "Voltar ao planejamento" style "artifact_button" text_size 29 action Return(False) id "student_course_cancel"
    use campaign_footer("Sua quinta está reservada para a oficina. Confirme quando quiser realizar essa atividade.")
    use lab_continue("Avançar para quinta · ir ao curso", Return(True), True, "student_course_confirm")

screen student_tip_screen():
    modal True
    zorder 160
    add Solid("#06121aee")
    key "game_menu" action Hide("student_tip_screen")
    frame:
        style "artifact_paper" align (0.5, 0.5) xsize 1250
        vbox:
            spacing 25
            text "Caderno · dica do curso" style "artifact_heading" size 40
            text (STUDENT_TIP if student_course_done else "O curso é opcional. Sua dica aparecerá aqui depois da participação na oficina.") style "artifact_ink" size lab_ui_size(29)
            textbutton "Fechar · Esc" style "artifact_button" action Hide("student_tip_screen") id "student_tip_close"

label student_city:
    if not student_introduced:
        $ student_introduced = True
        $ campaign_set_clock("home", "Semana do estudante", "08h", "morning")
        scene expression Transform(campaign_clock["image"], xysize=(1920, 1080), fit="cover")
        player "Entre o estágio e a faculdade, sobraram duas noites nesta semana. Posso estudar, conhecer a oficina, pegar um plantão ou descansar."
        "A oficina fica do outro lado da cidade. O curso é opcional e não impede nenhum dos projetos do estágio."
    jump student_city_map

label student_city_map:
    $ campaign_set_clock("city", "Passeio pela cidade", "16h", "day")
    call screen student_city_screen
    if _return == "hub":
        jump campaign_hub
    elif _return == "schedule":
        jump student_city_schedule
    elif _return in STUDENT_PLACES:
        $ student_place = _return
        $ student_visit(student_place)
        jump student_city_location
    jump student_city_map

label student_city_location:
    $ student_day, student_time, student_lighting = student_location_clock(student_place)
    $ campaign_set_clock(student_place, student_day, student_time, student_lighting)
    call screen student_location_screen(student_place)
    if _return == "schedule":
        jump student_city_schedule
    elif _return == "course":
        if student_schedule["thursday"] != "workshop":
            $ student_take_course()
            jump student_city_location
        call screen student_course_confirmation
        if _return:
            $ campaign_set_clock("city", "Quinta-feira", "20h", "night")
            scene expression Transform(campaign_clock["image"], xysize=(1920, 1080), fit="cover")
            "Quinta-feira, à noite. Você atravessa a cidade de ônibus e chega à oficina comunitária."
            $ campaign_set_clock("workshop", "Quinta-feira", "20h", "night")
            scene expression Transform(campaign_clock["image"], xysize=(1920, 1080), fit="cover")
            "No curso, o grupo monta uma tela com cartões de papel. Uma pessoa tenta cancelar a exclusão e percebe que o cartão já foi retirado."
            player "O cartão precisa continuar aqui até a confirmação. Se confirmar por engano, também preciso conseguir desfazer."
            "Vocês refazem o protótipo e repetem o teste. Na volta para casa, você registra o exemplo no caderno."
            $ student_take_course()
        else:
            jump student_city_schedule
        jump student_city_location
    jump student_city_map

label student_city_schedule:
    $ campaign_set_clock("home", "Planejamento da semana", "20h", "night")
    scene expression Transform(campaign_clock["image"], xysize=(1920, 1080), fit="cover")
    player "Em casa, às 20h, vou conferir as duas noites e organizar meus compromissos."
    call screen student_schedule_screen
    if _return == "talk":
        $ campaign_set_clock("startup", "Conversa no estágio", "09h", "morning")
        scene expression Transform(campaign_clock["image"], xysize=(1920, 1080), fit="cover")
        show sabrina neutral at colleague_right
        sabrina "Como ficou sua disponibilidade para a revisão do estágio?"
        if "overtime" in student_schedule.values():
            player "Reservei tempo para o plantão. Podemos usar os horários da agenda para revisar o estágio."
            sabrina "Combinado. Vou usar os horários que você reservou, sem contar com as outras noites."
        else:
            player "Não reservei plantão nesta semana. Quero preservar minhas outras atividades e o descanso."
            sabrina "Tudo bem. Eu replanejo a revisão para o horário regular do estágio."
        if "study" in student_schedule.values():
            player "O estudo com minha colega também ficou na agenda."
            sabrina "Deixe esse horário protegido no nosso combinado."
        else:
            player "O grupo não coube nessas duas noites. Vou combinar outro horário com minha colega."
            "Sua colega aceita buscar um horário entre as aulas."
            sabrina "Então fica assim, sem prometer dois compromissos na mesma noite."
        $ student_agree()
        hide sabrina
        jump student_city_schedule
    jump student_city_map
