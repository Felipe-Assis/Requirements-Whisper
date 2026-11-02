# st_04_preparacao.rpy
# Rota Startup, semana 2, segunda, 9h30 a 11h30. Bíblia: docs/rotas/startup.md (st_04).

label st_04_preparacao:
    $ set_available("st_techlead", "st_mobile")
    $ set_time(9, 30)

    play music music_office_relaxed fadein 1.0
    scene bg startup_coworking_manha
    with fade

    "{i}Segunda-feira, semana 2. O coworking ainda está meio vazio. Tem cheiro de café passado e alguém encostando a bicicleta perto do sofá.{/i}"
    "{i}Na parede de vidro, [NOME_ST_QUALIDADE] colou dezenas de post-its em montinhos de cores diferentes. Cada montinho tem um número escrito à caneta.{/i}"

    show st_qualidade thinking at right_zoom
    with dissolve
    st_qualidade "Bom dia, [player_name]! Juntei tudo o que o beta mandou até agora: avaliações da loja e mensagens do suporte. São 37."
    st_qualidade "Primeiro: 14 falam de total errado. Segundo: 9 dizem que não conseguem apagar um gasto. Terceiro: 6 pedem para conectar o banco. E 3 querem modo escuro."
    st_qualidade "Oxe, o modo escuro sempre aparece. Mas reparou no tamanho dos dois primeiros montinhos?"

    $ advance_minutes(10)
    show st_mentora neutral at left_zoom
    with dissolve
    st_mentora "Bom dia, gente! Olha só essa parede. Só de bater o olho já dá pra ver onde dói."
    st_mentora "[player_name], hoje à tarde tem a entrevista. Vai ser conjunta: a [NOME_ST_ESTUDANTE], que usa o app todo dia, e o [NOME_ST_CEO], que decide o que vai para o demo day."
    show st_mentora serious at left_zoom
    st_mentora "Já te aviso: os dois vão discordar. Faz parte. A gente não está lá para escolher um lado, e sim para entender o que cada um precisa."

    show st_mentora thinking at left_zoom
    st_mentora "E outra coisa. Entrevista é uma técnica entre várias. Essas avaliações contam, o painel de métricas conta, ver alguém usando o app no bandejão também conta."
    st_qualidade "Cada fonte mostra um pedaço. A avaliação diz o que irritou. A métrica diz quantos foram embora. A conversa diz por quê."

    "{i}Você lembra da sexta-feira no ônibus e conta o que aconteceu: o lanche de R$ 7, o túnel, o toque repetido em Salvar e o total subindo R$ 14.{/i}"

    show st_qualidade neutral at right_zoom
    st_qualidade "Oxe! Aconteceu com você também? Então é mais uma evidência. E com horário e lugar, que é o que quase nenhuma avaliação traz."
    "{i}[NOME_ST_QUALIDADE] escreve um post-it novo e cola no montinho do total errado. Agora são 15.{/i}"
    st_mentora "Viu? Você já é fonte de dado. Agora bora montar o roteiro da tarde."

    $ advance_minutes(40)
    "{i}Vocês sentam na ponta da mesa comprida. [NOME_ST_MENTORA] abre o caderno numa página em branco e passa a caneta para você.{/i}"

    menu:
        "Como você prepara o roteiro?"

        "Perguntas abertas sobre situações recentes, com os dados das avaliações para confirmar o que ouvirmos.":
            $ st_decidir("st_d04_roteiro", True)
            show st_mentora neutral at left_zoom
            st_mentora "Isso. Os dados dizem onde cavar; a conversa diz por quê."
            st_mentora "Se a [NOME_ST_ESTUDANTE] contar algo que bate com os 14 post-its, ótimo. Se contar algo que não está em nenhum, melhor ainda."

        "Levar o desenho da tela nova para eles aprovarem.":
            $ st_decidir("st_d04_roteiro", False)
            show st_qualidade serious at right_zoom
            st_qualidade "Eles vão opinar sobre o seu desenho, não sobre o problema deles. A conversa fica presa na sua ideia."
            st_qualidade "E se o desenho resolver a coisa errada, a gente só descobre depois de construir."
            menu:
                "Como você ajusta o roteiro?"
                "Troco por perguntas sobre a última vez que o problema aconteceu e levo os números como apoio.":
                    show st_mentora neutral at left_zoom
                    st_mentora "Agora sim. Desenho vem depois, quando a gente souber o que ele precisa resolver."

        "Um questionário de sim ou não com a lista de funcionalidades.":
            $ st_decidir("st_d04_roteiro", False)
            show st_mentora serious at left_zoom
            st_mentora "Todo mundo responde sim para tudo. Saímos com 20 prioridades e nenhuma razão."
            st_mentora "Pergunta de sim ou não fecha a conversa. A gente quer que ela abra."
            menu:
                "Como você ajusta o roteiro?"
                "Troco por perguntas sobre a última vez que o problema aconteceu e levo os números como apoio.":
                    show st_mentora neutral at left_zoom
                    st_mentora "Perfeito. Com uma história de verdade, os números ganham sentido."

    "{i}O roteiro fica curto: pedir um episódio recente, entender o que a pessoa tentava fazer, o que aconteceu e o que esperava. Os números da parede vão numa folha à parte, só para conferir.{/i}"

    $ advance_minutes(45)
    play sound "audio/effects/xicara_cafe.ogg"
    "{i}Perto das onze, a cafeteira da copa apita. [NOME_ST_MENTORA] e [NOME_ST_QUALIDADE] se levantam para uma pausa.{/i}"

    menu:
        "Na copa, o que você faz?"

        "Ofereço um café para a [NOME_ST_MENTORA] antes da entrevista.":
            $ add_friendship_point("st_mentora", 1)
            show st_mentora neutral at left_zoom
            st_mentora "Ah, obrigada! Sem açúcar, por favor. Quem trabalhou em atendimento de banco aprende a tomar café de qualquer jeito."

        "Pergunto à [NOME_ST_QUALIDADE] qual avaliação mais a marcou.":
            $ add_friendship_point("st_qualidade", 1)
            show st_qualidade thinking at right_zoom
            st_qualidade "Uma estudante que desinstalou porque achou que tinha perdido dinheiro. Ela não tinha perdido nada. O app é que mostrou o gasto duas vezes."
            st_qualidade "Mas, para ela, o susto foi real. Essa eu leio toda vez que alguém diz que é só um detalhe."

        "Fico revisando o roteiro em silêncio.":
            show st_mentora neutral at left_zoom
            st_mentora "Concentração também vale. Só não esquece de beber água antes da tarde."

    $ advance_minutes(25)
    st_mentora "Bora almoçar cedo. Às duas a [NOME_ST_ESTUDANTE] chega do campus, e ela tem aula logo depois."
    hide st_mentora
    hide st_qualidade
    with dissolve

    "{i}Você guarda a folha do roteiro no notebook. Uma pergunta fica sublinhada duas vezes: \"Me conta a última vez em que isso aconteceu?\"{/i}"

    return
