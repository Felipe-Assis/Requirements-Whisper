# co_10_almoco.rpy
# Semana 3, terça, 12h30 às 13h30. Almoço no refeitório: escolha de mesa
# (co_almoco_mesa) e falas que mudam com a amizade. Só menus sociais.
# Fonte: docs/rotas/corporativo.md, co_10.

label co_10_almoco:
    $ set_available("co_supervisora", "co_solicitante")
    $ set_time(12, 30)

    play music music_coffee_break_friendly fadein 1.0
    scene bg refeitorio_tarde
    with fade

    "{i}Terça-feira, meio-dia e meia. O refeitório do Grupo Vértice ocupa um andar inteiro: filas de bandejas, cheiro de feijão e centenas de conversas ao mesmo tempo.{/i}"
    "{i}Na saída do bufê, a equipe se divide sem combinar. [NOME_CO_LEGADO] e [NOME_CO_QUALIDADE] pegam uma mesa perto da janela. [NOME_CO_MENTORA] e [NOME_CO_DEV] ficam numa mesa do meio, olhando alguma coisa no celular dele.{/i}"
    "{i}Você para um segundo com a bandeja na mão.{/i}"

    menu:
        "Onde você senta?"
        "Com [NOME_CO_LEGADO] e [NOME_CO_QUALIDADE], perto da janela.":
            $ add_friendship_point("co_legado", 1)
            $ add_friendship_point("co_qualidade", 1)
            $ co_almoco_mesa = "jorge_ingrid"
        "Com [NOME_CO_MENTORA] e [NOME_CO_DEV], na mesa do meio.":
            $ add_friendship_point("co_mentora", 1)
            $ add_friendship_point("co_dev", 1)
            $ co_almoco_mesa = "valeria_kaua"

    if co_almoco_mesa == "jorge_ingrid":
        show co_legado neutral at left_zoom
        show co_qualidade neutral at right_zoom
        with dissolve
        co_legado "Senta aí, [player_name]. Esta é a mesa dos veteranos e dos desconfiados."
        co_qualidade "Eu sou a desconfiada. Ele é o veterano. Divisão justa."
        co_legado "O estrogonofe de quarta nunca falhou desde 2008. Único sistema da empresa sem incidente registrado."
        co_qualidade "Porque ninguém abriu chamado. Não quer dizer que não houve incidente."

        menu:
            "Que assunto você puxa?"
            "[NOME_CO_QUALIDADE], qual foi o pior incidente que você já viu?":
                $ add_friendship_point("co_qualidade", 1)
                show co_qualidade serious at right_zoom
                co_qualidade "Uma sexta de 2019. Uma mudança pequena no fechamento subiu às cinco da tarde, sem plano de volta."
                co_qualidade "Quebrou o relatório mensal da diretoria, e a central ficou duas horas sem conseguir fechar chamado."
                co_qualidade "No post-mortem, ninguém perguntou quem errou. A gente perguntou o que deixou o erro passar. Foi dali que veio a regra de nada subir sem RFC."
            "[NOME_CO_LEGADO], você vai sentir falta daqui?":
                $ add_friendship_point("co_legado", 1)
                show co_legado thinking at left_zoom
                co_legado "Falta? Eu nem saí ainda."
                "{i}Ele olha pela janela por um tempo um pouco longo demais. [NOME_CO_QUALIDADE] para o garfo no meio do caminho.{/i}"
                co_legado "Tem lugar que vira casa sem a gente perceber. Pergunta difícil para uma terça. Come, que esfria."
            "O que é um post-mortem sem culpados?":
                co_qualidade "É a reunião depois de um incidente. Conta o que aconteceu, hora a hora, e procura o que falhou no processo, não em quem."
                co_qualidade "Quando a pessoa tem medo de ser punida, ela esconde o erro. Aí a gente nunca aprende."

    else:
        show co_mentora neutral at left_zoom
        show co_dev neutral at right_zoom
        with dissolve
        co_mentora "Chega mais, [player_name]. O [NOME_CO_DEV] está me mostrando o pico das nove como se fosse novidade."
        co_dev "É novidade em gráfico! Olha a curva. Segunda depois de feriado parece uma montanha."

        menu:
            "Que assunto você puxa?"
            "[NOME_CO_MENTORA], como você saiu da central para a TI?":
                $ add_friendship_point("co_mentora", 1)
                co_mentora "Em 2004 eu atendia telefone ao lado da [NOME_CO_SUPERVISORA]. A gente dividia baia, fone e reclamação."
                co_mentora "Eu anotava num caderno tudo que o sistema da época fazia de errado. Quando o SGC chegou, a TI precisou de alguém que conhecesse as filas."
                co_mentora "Eu era a chata que sempre perguntava \"e o atendente, como faz?\". Em 2009 isso virou profissão."
            "[NOME_CO_DEV], o que você estuda fora do trabalho?":
                $ add_friendship_point("co_dev", 1)
                show co_dev thinking at right_zoom
                co_dev "IA para prever pico de chamados. Se eu souber que a segunda depois do feriado tem muito mais pedido de senha, a central escala mais gente."
                co_mentora "E a [NOME_CO_SUPERVISORA] vai perguntar de onde saiu o número."
                co_dev "Por isso eu já tô montando a planilha. Aprendi com ela que número sem fonte não entra na reunião."
            "Como vocês decidem o que entra numa versão?":
                co_mentora "Primeiro, o que resolve o problema de quem sofre com ele. Depois, o que cabe no tempo que a equipe tem de verdade."
                co_mentora "Daqui a duas semanas a gente senta para decidir isso junto. Você vai ver que sempre sobra pedido e falta gente."

    $ advance_minutes(50)
    hide co_legado
    hide co_qualidade
    hide co_mentora
    hide co_dev
    with dissolve

    scene bg escritorio_interior_tarde
    with fade
    "{i}Na volta, a equipe se encontra de novo no elevador, cada um com um café de copinho na mão.{/i}"

    show co_legado neutral at left_zoom
    with dissolve
    if get_friendship_point("co_legado") >= 4:
        co_legado "[player_name], quer ver o PL/SQL da rotina das 72 h? Isso aí tem história, e o código conta metade dela. A outra metade eu conto."
        "{i}Vocês combinam meia hora na sexta, com a tela dele e a caneca de 2008 entre os dois.{/i}"
    else:
        co_legado "Bom almoço. Agora é digestão e PL/SQL, nessa ordem."

    show co_qualidade neutral at right_zoom
    with dissolve
    if get_friendship_point("co_qualidade") >= 4:
        co_qualidade "Quinta de manhã tem CAB. Se quiser assistir como ouvinte, ponho seu nome na lista. Leva caneta: sempre aparece pergunta difícil."
    else:
        co_qualidade "De volta ao plano de testes. Ele não se revisa sozinho."

    $ set_time(13, 30)
    hide co_legado
    hide co_qualidade
    with dissolve

    return
