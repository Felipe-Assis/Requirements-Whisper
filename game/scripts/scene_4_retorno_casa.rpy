label scene_4_retorno_casa:
    $ disponivel_developer_ai = True
    $ disponivel_developer_coding = True
    $ disponivel_developer_management = True
    $ disponivel_developer_requirements = True
    $ disponivel_developer_project = True
    $ disponivel_developer_quality = True
    $ disponivel_developer_security = True
    $ disponivel_developer_test = True
    # Transição: ônibus/cidade à noite
    play music music_streets_focused fadein 1.8
    scene bg transito_noite
    with dissolve

    $ advance_minutes(120) # Viagem de volta para casa
    "O dia chega ao fim e, depois de um longo expediente, você embarca no ônibus para casa."
    "As luzes da cidade passam rápido pela janela enquanto você relembra tudo o que aconteceu hoje no escritório."
    play sound "audio/bus.ogg"
    pause 1.2

    # Chegando em casa
    play music music_home_reflecting fadein 2.0
    scene bg quarto_noite
    with fade
    $ advance_minutes(180)

    "De volta ao seu quarto, você senta na cama, tira o notebook da mochila e decide revisar as anotações do dia."
    show expression "images/items/notebook.png" as notebook at center_zoom
    pause 0.5

    "Você abre o arquivo de anotações:"
    window hide
    pause 1.0
    window show

    "• Etapas do ciclo de desenvolvimento\n• Importância de requisitos bem definidos\n• Valor da comunicação e integração da equipe\n• Primeiras impressões dos colegas"

    $ advance_minutes(7)
    # Simulando uso do notebook/celular
    "Enquanto termina de organizar as ideias, seu celular vibra com uma notificação de mensagem."
    play sound "audio/cell_vibration.ogg"
    pause 0.6

    show developer_requirements portrait at left_zoom
    developer_requirements "(mensagem pelo app) Olá, [player_name]! Parabéns pelo seu primeiro dia! Se precisar de qualquer coisa, pode contar comigo. Amanhã começamos a preparar as entrevistas com os stakeholders. Inclusive, não esquece de revisar o questionário clínico que está no drive da equipe!"
    "Você sorri e sente um leve alívio por estar sendo bem acolhido(a) na equipe."
    hide developer_requirements
    $ add_friendship_point("developer_requirements", 1)
    $ advance_minutes(2)

    "Tem mais gente online, talvez seja bom eu continuar com o celular e conversar com mais alguém?"

    call screen contacts_screen

    # Pequena transição de tempo
    "Decide tomar um banho rápido e fazer um lanche, refletindo sobre os desafios e aprendizados do dia."
    play music music_home_dreamy fadein 1.5
    scene bg cozinha_noite
    with dissolve
    $ advance_minutes(20)
    "No caminho para a cozinha, você cruza com seu colega de república."
    show npc_roommate neutral at right_zoom
    npc_roommate "E aí, [player_name]! Sobreviveu ao primeiro dia? Se precisar de dicas sobre transporte ou comida barata perto da empresa, só perguntar!"
    hide npc_roommate
    "Vocês conversam rapidamente e logo você volta para o quarto."

    scene bg quarto_noite
    with dissolve
    $ advance_minutes(5)

    "Deitado(a), você pega o celular novamente e faz uma pequena anotação para não esquecer:"
    "Hoje percebi como a teoria sobre metodologias ágeis vista na faculdade realmente faz sentido no mundo real."
    "A colaboração da equipe e a comunicação constante foram essenciais para entender como o trabalho flui na prática."

    # Reflexão do jogador (monólogo)
    "Talvez amanhã eu tente interagir mais com a equipe e observar melhor como cada um contribui para o projeto..."
    "Por agora, é hora de descansar."
    $ advance_minutes(10)

    stop music fadeout 1.5
    scene black
    with fade
    "Fim da Semana 1"

    window hide
    pause 1.0
    window show

    # Reflexão acadêmica
    "Aprendizado da semana: Metodologias ágeis não são só um tema de prova. São parte do dia a dia do desenvolvimento de software e fazem toda diferença para a equipe."

    return
