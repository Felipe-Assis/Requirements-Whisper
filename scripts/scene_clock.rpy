default campaign_clock = {}

init python:
    SCENE_VARIANTS = {
        "lab": {"morning": "laboratorio_manha", "afternoon": "laboratorio"},
        "startup": {"morning": "startup_manha", "afternoon": "startup"},
        "support": {"morning": "suporte_manha", "day": "suporte_dia", "rain": "suporte_chuva"},
        "campus": {"day": "campus", "night": "campus_noite"},
        "workshop": {"day": "oficina_dia", "night": "oficina"},
        "home": {"morning": "quarto_dia", "night": "quarto_noite"},
        "city": {"day": "cidade_dia", "night": "cidade_noite"},
    }
    SCENE_PLACES = {"lab": "Laboratório", "startup": "Mesa da equipe", "support": "Atendimento", "campus": "Faculdade", "workshop": "Oficina", "home": "Meu quarto", "city": "Cidade"}
    SCENE_LIGHTS = {"morning": "manhã", "afternoon": "tarde", "day": "dia", "night": "noite", "rain": "chuva"}

    def campaign_set_clock(place, day, time, lighting):
        variant = SCENE_VARIANTS.get(place, {}).get(lighting)
        if not variant:
            raise ValueError("Não existe essa variação de cenário: " + place + "/" + lighting)
        store.campaign_clock = {"place": place, "day": day, "time": time, "lighting": lighting, "image": "images/bg/" + variant + ".png"}

    def campaign_clock_caption():
        clock = store.campaign_clock
        if not clock:
            return "Mesa de projetos · escolha o próximo caso"
        return " · ".join((SCENE_PLACES[clock["place"]], clock["day"], clock["time"], SCENE_LIGHTS[clock["lighting"]]))
