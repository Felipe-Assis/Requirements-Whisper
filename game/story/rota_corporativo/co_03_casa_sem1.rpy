# co_03_casa_sem1.rpy
# Rota Corporativo, semana 1, sexta, 19h30 às 22h.
# Fonte: docs/rotas/corporativo.md, cena co_03. Sem variáveis novas.

label co_03_casa_sem1:
    $ set_available('all')
    $ set_time(19, 30)

    play music music_streets_focused fadein 1.5
    scene bg transito_noite
    with fade

    play sound "audio/effects/bus.ogg"
    "{i}Sexta-feira. O ônibus anda devagar pela avenida, e você repassa a semana.{/i}"
    "{i}O crachá provisório ainda no bolso. A sala gelada dos servidores. Um sistema mais velho que alguns colegas de faculdade.{/i}"
    "{i}E o chamado 48213, marcado como Resolvido, sem uma linha sobre o que foi feito.{/i}"
    stop sound fadeout 1.0
    $ advance_minutes(50)

    play music music_home_reflecting fadein 2.0
    scene bg cozinha_noite
    with fade

    show npc_roommate neutral at right_zoom
    with dissolve
    npc_roommate "E aí, [player_name]! Primeira semana em empresa grande. Conta: é só reunião mesmo?"
    "\"Tem reunião, sim\", você responde. \"E até mudança tem formulário. Para mexer no sistema, tem pedido, comitê e horário marcado de madrugada.\""
    npc_roommate "De madrugada? Que horror."
    "\"Lá, três linhas de código já zeraram um relatório da diretoria. Depois de ouvir essa história, o formulário até parece pouco.\""
    npc_roommate "Tá, me convenceu. Mas se pedirem formulário pra fazer café, você me avisa."
    hide npc_roommate
    with dissolve
    $ advance_minutes(30)

    scene bg quarto_noite
    with fade

    "{i}No quarto, você abre o notebook e revisa as anotações da semana.{/i}"
    show item notebook_fechado as notebook at center_zoom
    with dissolve
    "Tipos de manutenção: corretiva, adaptativa, evolutiva, preventiva. O Farol é evolutiva."
    "Caminho de uma mudança: RFC, CAB, janela de sábado, plano de volta e revisão depois."
    "Quem é quem: [NOME_CO_MENTORA] guia, [NOME_CO_LEGADO] lembra, [NOME_CO_DEV] constrói, [NOME_CO_QUALIDADE] confere."
    hide notebook
    with dissolve
    $ advance_minutes(40)

    play sound "audio/effects/cell_vibration.ogg"
    "{i}O celular vibra em cima da cama.{/i}"
    show co_mentora portrait at left_zoom
    with dissolve
    co_mentora "(mensagem) Oi, [player_name]! Separei 30 chamados reais do mês passado, já sem dados pessoais. Segunda a gente lê junto e procura o que se repete."
    hide co_mentora
    with dissolve

    menu:
        "O que você responde para a [NOME_CO_MENTORA]?"

        "\"Valeu! Vou dar uma olhada e anotar as dúvidas.\"":
            $ add_friendship_point("co_mentora", 1)
            co_mentora "(mensagem) Ótimo. Dúvida anotada já é metade da conversa de segunda. Bom descanso!"

        "\"Preciso ler tudo no fim de semana?\"":
            co_mentora "(mensagem) Não. Segunda a gente lê junto. Fim de semana é descanso."

        "Só curtir a mensagem.":
            "{i}Você curte a mensagem e deixa o celular de lado por um instante.{/i}"

    $ advance_minutes(10)
    "{i}Ainda tem gente online. Talvez dê para conversar com mais alguém antes de dormir.{/i}"

    call screen contacts_screen

    $ set_time(22, 0)
    "{i}Você apaga a luz pensando em quantas regras um sistema junta em dezesseis anos, e em quantas delas ninguém lembra.{/i}"

    stop music fadeout 1.5
    scene black
    with fade

    window hide
    pause 1.0
    window show

    "Fim da Semana 1\n\nAprendizado: num sistema legado, o ciclo começa entendendo o que já existe."

    return
