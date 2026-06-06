label scene_1_quarto:
    $ player_gender = ""
    $ player_name = ""
    $ player_age = ""
    $ inventory = []

    scene bg quarto_manha
    with fade

    $ renpy.music.set_volume(1.0, delay=0, channel="music")
    $ renpy.music.set_volume(1.0, delay=0, channel="sound")
    play sound "audio/effects/alarm_clock.ogg"
    play music music_home_dreamy fadein 1.5
    "BIP BIP BIP... O som do alarme ecoa pelo quarto iluminado pela manhã."
    $ advance_minutes(2)
    pause 0.8
    "Ainda sonolento, você se senta na cama e logo se lembra: hoje é dia de buscar um estágio!"
    $ advance_minutes(1)
    pause 0.6

    $ show_clock = True

    # O jogador pega o notebook na mesa (inventário)
    "Você olha ao redor do quarto, respira fundo e decide começar o dia. Seu notebook está em cima da escrivaninha, quase te chamando."
    show expression "images/items/notebook_fechado.png" as notebook at center_zoom
    "Você pega o notebook, sentindo o peso da responsabilidade — e da expectativa."
    $ add_to_inventory("notebook")
    $ advance_minutes(2)
    hide notebook
    with dissolve

    # Pega o celular
    "Em cima do criado-mudo, seu celular vibra com uma notificação sobre oportunidades de estágio."
    show expression "images/items/celular.png" as celular at left_zoom
    "Você pega o celular, pensando em como a tecnologia pode ser sua aliada na busca de hoje."
    $ add_to_inventory("celular")
    $ advance_minutes(1)
    hide celular
    with dissolve

    # Pega bloco de notas e caneta
    "Na mochila, você encontra seu velho bloco de notas e uma caneta azul — essenciais para anotar qualquer insight durante o processo."
    show expression "images/items/bloco_de_notas.png" as bloco at right_zoom
    "Você adiciona o bloco de notas ao seu kit."
    $ add_to_inventory("bloco_de_notas")
    pause 0.3
    hide bloco
    with dissolve
    show expression "images/items/caneta.png" as caneta at right_zoom
    "A caneta não pode faltar. Afinal, ideias importantes vêm sem avisar!"
    $ add_to_inventory("caneta")
    pause 0.3
    hide caneta
    with dissolve

    show screen inventory_button

    $ advance_minutes(2)
    "Pronto! Tudo à mão. Agora falta o mais importante: garantir que seu currículo esteja em dia."
    with dissolve

    # Preenchendo o currículo
    "Você liga o notebook, conecta à internet e percebe que precisa atualizar seu currículo antes de começar a busca."
    show item notebook_fechado as notebook at center_zoom
    pause 0.6
    $ advance_minutes(3)

    $ player_name = renpy.input(_("Nome completo:"))
    $ player_name = player_name.strip()
    while player_name == "":
        $ player_name = renpy.input(_("Por favor, digite um nome válido:"))
        $ player_name = player_name.strip()

    menu:
        "Qual seu gênero?"
        "Feminino":
            $ player_gender = "Feminino"
        "Masculino":
            $ player_gender = "Masculino"
        "Outro":
            $ player_gender = "Outro"
    $ advance_minutes(2)

    $ player_age = renpy.input(_("Qual sua idade?"))
    $ player_age = player_age.strip()
    while not player_age.isdigit() or int(player_age) < 12 or int(player_age) > 99:
        $ player_age = renpy.input(_("Por favor, digite uma idade válida (12-99):"))
        $ player_age = player_age.strip()
    $ player_age = int(player_age)
    $ advance_minutes(2)

    hide notebook
    with dissolve

    "Ótimo, [player_name]! Currículo atualizado. Agora sim, hora de procurar vagas de estágio."
    play sound "audio/effects/computer_typing.ogg"
    $ advance_minutes(4)
    "Você se levanta, pega o notebook e senta à escrivaninha, decidido(a) a começar a busca pelas melhores vagas."
    $ advance_minutes(1)

#     # --- CHAT INTEGRADO ---
#     $ chat_history = []
#     "Talvez seja uma boa hora para tirar uma dúvida com o assistente virtual da universidade sobre os requisitos das vagas na área de TI."
#     call chat_amigo
#     "Conversa finalizada."
#     $ advance_minutes(3)
#     # ----------------------

    "Após alguns minutos navegando pelos principais sites de recrutamento, três oportunidades chamam sua atenção:"
    with dissolve
    $ advance_minutes(4)

    menu:
        "Para qual vaga deseja se candidatar?"
        "1. Participar do desenvolvimento de um sistema web para a área da saúde, em parceria com uma universidade":
            $ chosen_job = "saude"
            "Você sente um frio na barriga, mas a ideia de contribuir em um projeto que pode impactar a vida das pessoas te anima."
            "{i}Projeto: Desenvolvimento do Sistema XYZ – sistema web para acompanhamento clínico de pacientes do Instituto XX.{/i}"
            "O desafio é grande: envolverá desde a coleta de requisitos com profissionais de saúde até o desenvolvimento de dashboards e integração com app móvel."
            "A possibilidade de aprendizado técnico e impacto social é ainda maior."
        "2. Desenvolvimento mobile em uma startup de tecnologia voltada para educação financeira":
            $ chosen_job = "startup"
            "Startups costumam ser ambientes dinâmicos e cheios de desafios."
            "Quem sabe seja a chance de crescer rápido e aprender com um time enxuto e criativo?"
        "3. Estágio em manutenção de sistemas legados em uma grande corporação nacional":
            $ chosen_job = "corporativo"
            "Estabilidade, benefícios e a experiência de atuar em uma empresa tradicional."
            "Talvez seja uma boa forma de entender a rotina e os processos de equipes grandes."
    $ advance_minutes(4)

    "Você anota todos os detalhes da vaga e finaliza a candidatura pelo notebook."
    play sound "audio/effects/computer_typing.ogg"
    $ advance_minutes(1)

    "Depois de terminar, sente que merece um pouco de organização. Hora de preparar tudo para o novo desafio."
    # Adicionando a mochila agora, como gesto simbólico de se preparar para sair
    show expression "images/items/mochila.png" as mochila at left_zoom
    "Você pega sua mochila preferida, pronta para receber todos os itens essenciais."
    $ add_to_inventory("mochila")
    "Ao acessar a MOCHILA (canto esquerdo superior) você verá seus itens"
    "Na mochila, você pode acessar seu CELULAR e visualizar seus CONTATOS"
    "Pode clicar em um CONTATO para conversar com seu amigo!"
    "E também é possível visualizar o seu nível de AMIZADE."
    "No entanto, você não pode mandar mensagens em alguns momentos."
    "Exemplo, não faz sentido enviar mensagens quando estiver no mesmo cômodo que a pessoa."
    pause 0.6
    hide mochila


    show expression "images/items/garrafinha.png" as garrafinha at right_zoom
    "Ah, quase esqueci da minha garrafinha!"
    $ add_to_inventory("garrafinha")
    pause 0.6
    hide garrafinha



    with dissolve

    "Em seguida, confere no espelho se está apresentável para o dia."
    "Troca de roupa, arruma o cabelo, respira fundo e se sente pronto(a) para essa nova fase!"
    $ advance_minutes(2)

    stop music fadeout 1.5
    "Agora é só esperar a resposta das empresas..."
    pause 0.8
    scene black with fade
    "..."
    pause 1.2

    jump scene_2_escritorio
