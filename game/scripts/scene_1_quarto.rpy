label scene_1_quarto:
    $ player_gender = ""
    $ player_name = ""
    $ player_age = ""
    $ inventory = []

    scene bg quarto_manha
    with fade

    play sound "audio/alarm_clock.ogg"
    "BIP BIP BIP... O som do alarme ecoa pelo quarto iluminado pela manhã."
    pause 0.8
    "Ainda sonolento, você se senta na cama e logo se lembra: hoje é dia de buscar um estágio!"
    pause 0.6
    "Você olha ao redor do quarto, respira fundo e decide começar o dia."
    with dissolve

    # Preenchendo o 'currículo'
    "Você pega o notebook, abre o navegador e percebe que precisa atualizar seu currículo antes de começar a busca."
    show expression "images/items/notebook.png" as notebook at center_zoom
    pause 0.6

    $ player_name = renpy.input("Nome completo:")
    $ player_name = player_name.strip()
    while player_name == "":
        $ player_name = renpy.input("Por favor, digite um nome válido:")
        $ player_name = player_name.strip()

    menu:
        "Qual seu gênero?"
        "Feminino":
            $ player_gender = "Feminino"
        "Masculino":
            $ player_gender = "Masculino"
        "Outro":
            $ player_gender = "Outro"

    $ player_age = renpy.input("Qual sua idade?")
    $ player_age = player_age.strip()
    while not player_age.isdigit() or int(player_age) < 12 or int(player_age) > 99:
        $ player_age = renpy.input("Por favor, digite uma idade válida (12-99):")
        $ player_age = player_age.strip()
    $ player_age = int(player_age)

    hide notebook
    with dissolve

    "Ótimo, [player_name]! Currículo atualizado. Agora sim, hora de procurar vagas de estágio."
    play sound "audio/computer_typing.ogg"
    "Você se levanta, pega seu notebook em cima da escrivaninha e senta para procurar vagas disponíveis."
    $ inventory.append("notebook")
    pause 0.8

    "Após alguns minutos navegando pelos principais sites de recrutamento, três oportunidades chamam sua atenção:"
    with dissolve

    menu:
        "Para qual vaga deseja se candidatar?"
        "1. Participar do desenvolvimento de um sistema web para a área da saúde, em parceria com uma universidade":
            $ chosen_job = "saude"
            "Você sente um frio na barriga, mas a ideia de contribuir em um projeto que pode impactar a vida das pessoas te anima."
            "O desafio é grande, mas a possibilidade de aprendizado e impacto social é ainda maior."
        "2. Desenvolvimento mobile em uma startup de tecnologia voltada para educação financeira":
            $ chosen_job = "startup"
            "Startups costumam ser ambientes dinâmicos e cheios de desafios."
            "Quem sabe seja a chance de crescer rápido e aprender com um time enxuto e criativo?"
        "3. Estágio em manutenção de sistemas legados em uma grande corporação nacional":
            $ chosen_job = "corporativo"
            "Estabilidade, benefícios e a experiência de atuar em uma empresa tradicional."
            "Talvez seja uma boa forma de entender a rotina e os processos de equipes grandes."

    "Você anota todos os detalhes da vaga e finaliza a candidatura pelo notebook."
    play sound "audio/send_email.ogg"
    "Depois de terminar, sente que merece um pouco de organização."
    "Você pega sua mochila e começa a separar os itens que vai precisar para o novo desafio."
    $ inventory.append("mochila")
    show expression "images/items/mochila.png" as mochila at left_zoom
    pause 0.6

    "Em seguida, confere no espelho se está apresentável para o dia."
    "Troca de roupa, arruma o cabelo, respira fundo e se sente pronto para essa nova fase!"
    hide mochila
    with dissolve

    "Agora é só esperar a resposta das empresas..."
    pause 0.8
    scene black with fade
    "..."
    pause 1.2
    return
