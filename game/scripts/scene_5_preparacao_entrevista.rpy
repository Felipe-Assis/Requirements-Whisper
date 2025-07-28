label scene_5_preparacao_entrevista:
    # Manhã agitada no quarto
    play music music_home_dreamy fadein 1.0
    scene bg quarto_manha
    with dissolve

    $ game_hour = 11
    $ game_minute = 30

    $ advance_minutes(7)
    "O alarme toca mais uma vez... Você percebe que perdeu a hora!"
    play sound "audio/effects/alarm_clock.ogg"
    "Num salto, você se veste, arruma a mochila às pressas e corre para não perder o ônibus."
    $ advance_minutes(5)

    scene bg transito_manha
    with fade
    $ advance_minutes(20)
    "Enquanto espera o ônibus, você sente aquele frio na barriga: hoje é dia de entrevistar os stakeholders do projeto."
    "O trânsito parece mais lento que o normal. Você aproveita para revisar rapidamente suas anotações no celular: perguntas sobre funcionalidades, fluxos, restrições e detalhes do dia a dia no Instituto."
    play sound "audio/effects/bus.ogg"
    pause 0.8
    $ advance_minutes(10)

    play music music_office_relaxed fadein 1.0
    scene bg escritorio_interior_manha
    with dissolve
    $ advance_minutes(5)

    # Chegada ao escritório, developer_requirements já está lá
    show developer_requirements thinking at left_zoom
    developer_requirements "Bom dia, [player_name]! Achei que você não ia chegar... Tudo bem por aí?"
    menu:
        "Como você responde?"
        "Desculpe o atraso, o ônibus demorou demais.":
            developer_requirements "Sem problemas! Acontece com todo mundo. O importante é estar aqui agora."
        "Fiquei revisando as perguntas no caminho para não fazer feio na entrevista!":
            $ add_friendship_point("developer_requirements", 1)
            developer_requirements "Ótimo! Proatividade faz toda diferença nessas horas. Mostra que você está realmente comprometido."
        "Quase perdi a hora, mas prometo que foi só hoje!":
            developer_requirements "Relaxa, não sou chefe para brigar por isso! Só não vai virar rotina, hein?"
    $ advance_minutes(3)

    "Você percebe um café recém-passado na copa da empresa."
    menu:
        "Deseja pegar um café para você e para developer_requirements?"
        "Sim, pego dois cafés e ofereço um para ela.":
            $ add_friendship_point("developer_requirements", 1)
            "Você pega duas xícaras e entrega uma para [NOME_DEVELOPER_REQUIREMENTS]."
            developer_requirements "Poxa, valeu! Começar o dia com café e boa companhia é ótimo."
        "Só pego para mim, preciso acordar!":
            "Você pega seu café e sente o calor da xícara ajudar a despertar."
        "Prefiro não tomar café agora.":
            "Você decide esperar mais um pouco antes de tomar café."
    $ advance_minutes(2)

    hide developer_requirements

    # Orientação sobre a entrevista, reforço de amizade e contexto técnico
    show developer_requirements enthusiastic at left_zoom
    developer_requirements "Hoje você vai participar da entrevista com dois stakeholders: o diretor médico e uma das enfermeiras que mais usam o sistema."
    developer_requirements "Prepare perguntas que ajudem a entender tanto as necessidades técnicas quanto o dia a dia deles. Lembre-se: o objetivo é captar dores reais, não só o que o sistema deveria fazer."
    developer_requirements "Perguntas abertas ajudam a extrair mais detalhes. Ouça com atenção, anote pontos-chave e não tenha medo de perguntar sobre situações do cotidiano — muitas vezes surgem requisitos importantes fora do roteiro!"
    developer_requirements "Aliás, seu notebook já tem um roteiro inicial e o questionário clínico do Instituto. Mas se sentir confiança, pode improvisar e aprofundar onde achar necessário. Escuta ativa é tudo!"
    $ advance_minutes(5)

    "Vocês seguem juntos até a sala de reuniões. O clima é de leve tensão, mas também de expectativa pelo que você pode aprender hoje."
    hide developer_requirements

    # Transição/padding antes da próxima cena
    play music music_office_concentrated_2 fadein 0.8
    scene black
    with fade
    $ advance_minutes(3)
    "Alguns minutos depois, tudo pronto para começar a entrevista..."

    return
