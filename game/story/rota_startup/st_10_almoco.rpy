# st_10_almoco.rpy
# Rota Startup, semana 3, terça, 12h30 a 13h30. Fonte: docs/rotas/startup.md (st_10).
# Cena social: marmita coletiva, pistas para a arquitetura e para usabilidade.

label st_10_almoco:
    $ set_available("st_estudante")
    $ set_time(12, 30)

    play music music_coffee_break_friendly fadein 1.0
    scene bg refeitorio_tarde
    with fade

    "{i}Terça é dia de marmita coletiva na copa do coworking. Cada pessoa traz um prato, e a mesa comprida vira um bufê improvisado.{/i}"
    "{i}Tem arroz de forno, farofa de banana, salada de feijão-fradinho e um bolo de cenoura que ninguém assume ter trazido.{/i}"

    show st_mentora neutral at left_zoom
    with dissolve
    st_mentora "Chegou na hora, [player_name]! Pega um prato antes que o Davi repita pela terceira vez."
    show st_mobile neutral at right_zoom
    with dissolve
    st_mobile "Segunda vez. É a segunda. Tô em fase de crescimento."
    hide st_mentora
    hide st_mobile
    with dissolve

    "{i}A mesa se divide sozinha em duas rodas. Numa ponta, Otávio e Davi falam de mensagens de celular. Na outra, Tainá e Lorena riem de alguma avaliação da loja.{/i}"

    menu:
        "Onde você senta?"
        "Com Otávio e Davi.":
            $ add_friendship_point("st_techlead", 1)
            $ add_friendship_point("st_mobile", 1)

            show st_techlead neutral at left_zoom
            show st_mobile neutral at right_zoom
            with dissolve
            st_techlead "Senta aí. O Davi acabou de dizer que SMS é coisa de museu."
            st_mobile "Eu disse que é coisa de código de verificação. Museu foi você que falou."
            st_techlead "Veja bem: em 2004 eu ajudei a construir um internet banking por SMS. O cliente mandava \"SALDO\" e recebia o saldo de volta."
            st_techlead "Funcionava. Quase sempre. Quando a operadora engasgava, a mensagem chegava duas vezes. E o saldo também."
            st_mobile "Pera. O banco mandava o saldo duas vezes ou descontava duas vezes?"
            show st_techlead thinking at left_zoom
            st_techlead "Depende do dia. É por isso que eu tenho cabelo branco onde ainda tenho cabelo."
            "{i}Davi ri alto. Você lembra do almoço da Bia aparecendo duas vezes no app.{/i}"

            menu:
                "O que você pergunta?"
                "Como vocês resolviam a mensagem duplicada?":
                    $ add_friendship_point("st_techlead", 1)
                    st_techlead "Mal. A gente comparava o texto e o horário e torcia."
                    st_techlead "Um dia te conto a versão certa. Ela tem a ver com o que a Bia viu no ônibus."
                "Davi, você usaria SMS banking hoje?":
                    $ add_friendship_point("st_mobile", 1)
                    st_mobile "Só se o meu celular virasse um tijolo. Mas pensa: rodava em qualquer aparelho, sem internet boa."
                    st_mobile "É o que eu tento fazer no Trocado. Se roda no celular mais barato da loja, roda em qualquer um."

            if get_friendship_point("st_techlead") >= 4:
                show st_techlead neutral at left_zoom
                st_techlead "Sabe, [player_name]? É bom ensinar alguém que pergunta o porquê. Pouca gente pergunta."
            if get_friendship_point("st_mobile") >= 4:
                st_mobile "E você já é oficialmente da roda do almoço. Vai ter que trazer um prato semana que vem, viu?"

            hide st_techlead
            hide st_mobile
            with dissolve

        "Com Tainá e Lorena.":
            $ add_friendship_point("st_mentora", 1)
            $ add_friendship_point("st_qualidade", 1)

            show st_mentora neutral at left_zoom
            show st_qualidade neutral at right_zoom
            with dissolve
            st_qualidade "Senta aqui. A gente tava lendo uma avaliação: \"o app é bom, mas meu total tem personalidade própria\"."
            st_mentora "Pelo menos é engraçada. As do banco não eram."
            st_mentora "Passei cinco anos no atendimento. Todo dia alguém ligava achando que tinha perdido dinheiro. Igual a Bia."
            show st_mentora thinking at left_zoom
            st_mentora "Na maioria das vezes o dinheiro estava lá. O que sumia era a confiança. Saí quando percebi que queria consertar a causa, não atender a consequência."
            st_qualidade "E eu saí da sala de aula pelo mesmo motivo, só que com redação."

            menu:
                "O que você pergunta?"
                "O que você aprendeu no atendimento do banco?":
                    $ add_friendship_point("st_mentora", 1)
                    st_mentora "Que ninguém liga para reclamar de botão. A pessoa liga porque ficou com medo."
                    st_mentora "Então eu sempre pergunto: o que essa pessoa estava tentando fazer quando sentiu medo?"
                "Como é um teste de usabilidade na prática?":
                    $ add_friendship_point("st_qualidade", 1)
                    show st_qualidade thinking at right_zoom
                    st_qualidade "Primeiro, você dá uma tarefa: \"lance o almoço de hoje e apague o que saiu errado\". Segundo, fica em silêncio e observa. Terceiro, anota onde a pessoa travou."
                    st_qualidade "O mais difícil é o segundo. Dá vontade de apontar o botão. Oxe, mas aí você estraga o teste."

            if get_friendship_point("st_mentora") >= 4:
                show st_mentora neutral at left_zoom
                st_mentora "Gosto de almoçar com você, [player_name]. Você pergunta como quem quer mesmo saber a resposta."
            if get_friendship_point("st_qualidade") >= 4:
                show st_qualidade neutral at right_zoom
                st_qualidade "Quando tiver o teste com os calouros, guardo uma cadeira para você na sala de observação."

            hide st_mentora
            hide st_qualidade
            with dissolve

    $ advance_minutes(35)

    show st_ceo neutral at center_zoom
    with dissolve
    st_ceo "Time! Não posso ficar, só vim pegar farofa."
    st_ceo "Notícia quente: consegui reunião com um fundo na semana que vem! Eles querem ver tração!"
    "{i}Ele enche o prato, acena com o garfo e sai falando ao telefone antes que alguém responda.{/i}"
    hide st_ceo
    with dissolve

    "{i}A mesa fica em silêncio por um segundo. As duas rodas se juntam de novo em volta da travessa de farofa, agora vazia.{/i}"

    show st_qualidade thinking at left_zoom
    show st_techlead neutral at right_zoom
    with dissolve
    st_qualidade "Tração, ele disse. Cadê a evidência de que alguém volta a usar o app depois da primeira semana?"
    st_techlead "Calma. Ele vai perguntar isso para a gente antes de o fundo perguntar para ele. Dá tempo de ter a resposta."
    show st_qualidade neutral at left_zoom
    st_qualidade "Primeiro, o total certo. Segundo, gente voltando. Terceiro, aí sim, o fundo."
    st_techlead "Essa ordem eu assino. Só não conta para ele que eu concordei tão rápido."
    "{i}Tainá ri, e Davi aproveita a distração para cortar mais um pedaço do bolo.{/i}"
    st_techlead "Davi, quem trouxe esse bolo?"
    "{i}Davi mastiga devagar e não responde. Ninguém assume de novo.{/i}"
    hide st_qualidade
    hide st_techlead
    with dissolve
    $ advance_minutes(20)
    $ set_time(13, 30)
    "{i}Uma e meia. Os pratos voltam para as mochilas, e a equipe volta para a mesa longa do andar de cima.{/i}"

    return
