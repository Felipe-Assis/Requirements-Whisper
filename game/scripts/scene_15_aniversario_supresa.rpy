label scene_15_aniversario_surpresa:
    scene bg escritorio_interior_tarde
    with dissolve

    "{i}O expediente da tarde segue animado, mas um grupo cochicha ao lado da impressora: hoje é aniversário de [NOME_DEVELOPER_SECURITY].{/i}"
    "{i}Você percebe que a equipe está querendo organizar algo especial, mas ninguém se prontificou ainda.{/i}"

    # Momento didático e de inventário: pensar na logística do evento
    show developer_requirements thinking at left_zoom
    developer_requirements "Acho que ninguém lembrou de comprar bolo... Se der tempo, dá para improvisar alguma coisa."
    show developer_ai positive at right_zoom
    developer_ai "Se cada um trouxer um docinho, já vira festa! Alguém consegue buscar refrigerante?"

    # Minijogo/simulações: Organização de surpresa (escolhas afetam amizade)
    "{i}Você decide assumir a liderança da surpresa. Pode escolher o que organizar:{/i}"
    menu:
        "Como você contribui para o aniversário surpresa?"
        "Fico responsável por comprar o bolo na padaria.":
            $ amizade_developer_security += 2
            $ amizade_developer_requirements += 1
            play sound "audio/cell_vibration.ogg"
            show developer_quality positive at right_zoom2
            developer_quality "Genial, [player_name]! Bolo é o mais importante, todo mundo vai adorar."
            $ inventario.append("bolo")
            hide developer_quality
        "Faço uma vaquinha rápida pelo chat e compro docinhos e salgadinhos.":
            $ amizade_developer_security += 1
            $ amizade_developer_ai += 1
            show developer_ai enthusiastic at right_zoom
            developer_ai "Gostei! Gente unida até no pix, festa colaborativa é sucesso."
            $ inventario.append("docinhos")
            $ inventario.append("salgadinhos")
            hide developer_ai
        "Sugiro fazer cartões de parabéns assinados por toda a equipe.":
            $ amizade_developer_security += 2
            $ amizade_developer_project += 1
            show developer_project positive at right_zoom
            developer_project "Boa! Gestos simples valem muito. Eu topo ajudar a desenhar algo especial."
            $ inventario.append("cartão")
            hide developer_project

    # Minijogo opcional (decoração ou escolha de música)
    "{i}Com a comemoração se aproximando, você pode escolher mais uma ação para incrementar a surpresa:{/i}"
    menu:
        "Deseja cuidar de algum detalhe extra?"
        "Baixar uma playlist divertida para animar a sala.":
            play sound "audio/music_party.ogg"
            show developer_test enthusiastic at left_zoom
            developer_test "Essa seleção tá top! Já quero dançar comendo brigadeiro."
            $ amizade_developer_test += 1
            hide developer_test
        "Providenciar balões e enfeites coloridos.":
            show developer_quality positive at left_zoom
            developer_quality "Adorei a decoração! Vai deixar tudo mais alegre."
            $ amizade_developer_quality += 1
            hide developer_quality
        "Preparar uma apresentação de slides com fotos engraçadas da equipe.":
            show developer_coding positive at left_zoom
            developer_coding "Que nostalgia, [player_name]! Boa ideia para dar boas risadas juntos."
            $ amizade_developer_coding += 1
            hide developer_coding

    # Padding - NPCs comentando, ritmo de preparação
    show developer_requirements positive at left_zoom
    developer_requirements "Vai ficar demais! E tudo feito em equipe, do jeitinho que a gente gosta."
    hide developer_requirements

    "{i}A sala é fechada rapidinho para montar a surpresa. Cada um colabora, um busca bolo, outro pendura balões, outro ajuda a arrumar as mesas.{/i}"
    play sound "audio/ambiente_agitado.ogg"
    pause 1.0

    # Chegada do aniversariante
    show developer_security serious at center_zoom
    developer_security "Pessoal, por que está tudo tão quieto por aqui...?"
    play sound "audio/aplausos.ogg"
    "{i}De repente, todos surgem juntos:{/i}"

    # NPCs em diferentes expressões comemorativas
    show developer_ai enthusiastic at left_zoom
    show developer_test enthusiastic at right_zoom
    show developer_quality positive at right_zoom2
    show developer_coding positive at left_zoom
    developer_ai "Parabéns, [NOME_DEVELOPER_SECURITY]!"
    developer_test "Felicidades, muita segurança nos sistemas e alegria na vida!"
    developer_quality "O checklist de hoje é só felicidade!"
    developer_coding "Hoje ninguém fala de bug, só de brigadeiro!"

    hide developer_ai
    hide developer_test
    hide developer_quality
    hide developer_coding

    show developer_security positive at center_zoom
    developer_security "Nossa, gente... Nem sei o que dizer. Vocês são demais!"
    play sound "audio/feedback_positive.ogg"

    # Possível minijogo: escolha de fala do jogador (para personalizar a homenagem)
    menu:
        "Como você deseja parabenizar [NOME_DEVELOPER_SECURITY]?"
        "Desejo sucesso e agradeço pela parceria no projeto.":
            $ amizade_developer_security += 1
            show developer_security enthusiastic at center_zoom
            developer_security "Valeu, [player_name]! É uma honra trabalhar contigo."
            hide developer_security
        "Brinco sobre 'testar o bolo' para garantir qualidade.":
            $ amizade_developer_quality += 1
            show developer_quality positive at right_zoom
            developer_quality "Hahaha, essa foi boa! Pode confiar que o controle de qualidade aqui é sério."
            hide developer_quality
        "Faço um trocadilho sobre bugs e ataques, arrancando risos da equipe.":
            $ amizade_developer_ai += 1
            show developer_ai positive at left_zoom
            developer_ai "Piada digna de deploy em sexta-feira à noite!"
            hide developer_ai

    "{i}A tarde termina em clima de festa, amizade e descontração. A equipe se sente ainda mais próxima e motivada para os próximos desafios.{/i}"

    # Padding de final de cena e flag para futuras consequências
    $ flag_festa_seguranca = True

    scene bg escritorio_interior_noite
    with fade
    "{i}No fim do dia, todos se despedem com abraços e sorrisos. Você percebe que celebrar juntos é tão importante quanto entregar bons resultados técnicos.{/i}"

    scene bg quarto_noite
    with fade

    "{i}Mais tarde, em casa, você repousa após um dia cheio de risadas e desafios.{/i}"
    "{i}Revê mentalmente os momentos do evento surpresa, as conversas animadas, os olhares de gratidão e o quanto a equipe cresceu junta.{/i}"

    "{i}Você abre o notebook para registrar suas impressões do dia e percebe como pequenas iniciativas, como celebrar aniversários e valorizar os colegas, fortalecem laços e criam um ambiente onde todos se sentem pertencentes.{/i}"

    window hide
    pause 0.8
    window show

    "{i}Lembra-se também das discussões técnicas, dos debates construtivos e das decisões tomadas em equipe para definir a arquitetura do sistema.{/i}"

    "{i}No fim, conclui que projetos de software não são feitos apenas de código, mas de pessoas, colaboração e respeito à diversidade de ideias.{/i}"

    scene black
    with fade
    window hide
    pause 1.2
    window show

    "{i}Fim da Semana 4\n\nAprendizado: O trabalho em equipe e a diversidade técnica são a base para a inovação e o sucesso. Saber ouvir, colaborar e celebrar juntos faz toda diferença — no software e na vida.{/i}"

    return
