label scene_5_preparacao_entrevista:
    # Padding: manhã agitada, atraso, correria
    scene bg quarto_manha
    with dissolve

    "O alarme toca mais uma vez... Você percebe que perdeu a hora!"
    play sound "audio/alarm_clock.ogg"
    "Num salto, você se veste, arruma a mochila às pressas e corre para não perder o ônibus."
    scene bg transito_manha
    with fade
    "Enquanto espera o ônibus, você sente aquele frio na barriga: hoje é dia de entrevistar os stakeholders do projeto."
    "O trânsito parece mais lento que o normal. Você aproveita para revisar rapidamente suas anotações no celular."
    play sound "audio/bus.ogg"
    pause 0.8

    scene bg escritorio_interior_manha
    with dissolve

    # Chegada ao escritório, developer_requirements já está lá
    show developer_requirements thinking at left_zoom
    developer_requirements "Bom dia, [player_name]! Achei que você não ia chegar... Tudo bem por aí?"
    menu:
        "Como você responde?"
        "Desculpe o atraso, o ônibus demorou demais.":
            developer_requirements "Sem problemas! Acontece com todo mundo. O importante é estar aqui agora."
        "Fiquei revisando as perguntas no caminho para não fazer feio na entrevista!":
            $ amizade_developer_requirements += 1
            developer_requirements "Ótimo! Proatividade faz toda diferença nessas horas. Mostra que você está realmente comprometido."
        "Quase perdi a hora, mas prometo que foi só hoje!":
            developer_requirements "Relaxa, não sou chefe para brigar por isso! Só não vai virar rotina, hein?"

    "Você percebe um café recém-passado na copa da empresa."
    menu:
        "Deseja pegar um café para você e para developer_requirements?"
        "Sim, pego dois cafés e ofereço um para ela.":
            $ amizade_developer_requirements += 1
            "Você pega duas xícaras e entrega uma para [NOME_DEVELOPER_REQUIREMENTS]."
            developer_requirements "Poxa, valeu! Começar o dia com café e boa companhia é ótimo."
        "Só pego para mim, preciso acordar!":
            "Você pega seu café e sente o calor da xícara ajudar a despertar."
        "Prefiro não tomar café agora.":
            "Você decide esperar mais um pouco antes de tomar café."

    hide developer_requirements

    # Orientação sobre a entrevista, reforço de amizade e contexto técnico
    show developer_requirements enthusiastic at left_zoom
    developer_requirements "Hoje você vai participar da entrevista com dois stakeholders: o diretor médico e uma das enfermeiras que mais usam o sistema."
    developer_requirements "Prepare perguntas que ajudem a entender tanto as necessidades técnicas quanto o dia a dia deles."
    developer_requirements "Lembre-se: perguntas abertas ajudam a extrair mais detalhes, e ouvir com atenção é tão importante quanto perguntar certo!"
    developer_requirements "Se precisar de um roteiro, está tudo no seu notebook. Mas pode improvisar se sentir confiança."

    "Vocês seguem juntos até a sala de reuniões. O clima é de leve tensão, mas também de expectativa pelo que você pode aprender hoje."

    hide developer_requirements

    # Transição/padding antes da próxima cena
    scene black
    with fade
    "Alguns minutos depois, tudo pronto para começar a entrevista..."
