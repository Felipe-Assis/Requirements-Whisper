label st_02_reuniao_ciclo:
    # Equipe inteira na sala; stakeholders ainda não são contatos.
    $ set_available()
    $ set_time(10, 0)

    play music music_office_concentrated_1 fadein 1.0
    scene bg sala_reunioes_manha
    with fade

    "{i}Quarta-feira, dez da manhã. O aquário, como a equipe chama a salinha de vidro do coworking, mal comporta cinco pessoas e um quadro branco.{/i}"
    "{i}Antes que todo mundo se sente, a porta abre. Entra um homem de colete azul-petróleo, com o celular ainda na mão.{/i}"

    show st_ceo neutral at center_zoom
    with dissolve
    st_ceo "Pessoal, dois minutos, prometo! [player_name], né? Vinícius, CEO. Boas-vindas à revolução do trocado!"
    st_ceo "Notícia quente: o fundo da Maré quer ver tração no demo day. Tração! Gente usando, gente voltando, gráfico subindo."
    st_ceo "Eu era bolsista, sabia? Contava moeda no fim do mês. Esse app é o que eu queria ter tido. Então bora fazer ele voar!"
    play sound "audio/effects/phone_rining.ogg"
    st_ceo "É o investidor. Tainá, conduz? Depois me conta tudo!"
    hide st_ceo
    with dissolve
    stop sound
    $ advance_minutes(5)

    "{i}A porta de vidro fecha. Por alguns segundos, ninguém fala.{/i}"
    show st_mobile neutral at right_zoom
    with dissolve
    st_mobile "Duas vezes “tração” em dois minutos. Ganhei a aposta, Lorena."
    show st_mentora neutral at left_zoom
    with dissolve
    st_mentora "Ele quer o bem dos estudantes, viu? Só fala em pitch. A gente traduz."

    # O ciclo de vida no quadro
    show st_mentora thinking at left_zoom
    "{i}Tainá pega a caneta e escreve seis palavras em círculo no quadro: descobrir, especificar, construir, testar, lançar, medir.{/i}"
    st_mentora "Na faculdade você deve ter visto isso como um projeto longo, uma etapa depois da outra. Aqui o ciclo é o mesmo."
    st_mentora "Ele não some, ele encolhe. Cada volta dura uma semana."
    st_mentora "Segunda a gente decide o que entra. Na sexta, alguma coisa já está na mão de estudante, ou pelo menos num teste com alguém de verdade."
    $ advance_minutes(15)

    # O quadro Kanban
    show expression "images/artifacts/st_quadro_kanban.png" as st_kanban at artefato_tela
    with dissolve
    st_mentora "Esse é o nosso quadro. Cinco colunas: descoberta, pronto para desenvolver, fazendo, revisão e pronto."
    st_mentora "Repara no limite da coluna Fazendo: no máximo duas tarefas por pessoa. Quer puxar a terceira? Primeiro termina uma ou pede ajuda."
    st_mobile "Esse limite já me salvou de mim mesmo. Eu abro seis coisas e não fecho nenhuma."
    hide st_mobile
    with dissolve
    st_mentora "Do Scrum a gente pegou só três rituais: planejamento na segunda, uma conversa de dez minutos todo dia, em pé, e revisão na sexta, mostrando o que ficou pronto."
    st_mentora "O resto a gente deixou na prateleira. Somos sete. Ritual demais come o tempo de quem constrói."
    hide st_kanban
    with dissolve
    $ advance_minutes(15)

    # Otávio, Davi e Lorena completam o ciclo
    show st_techlead thinking at right_zoom
    with dissolve
    st_techlead "Deixa eu pôr um pé no freio. Startup tem fama de pular etapa: especificação nunca, teste depois."
    st_techlead "Veja bem: cozinha de restaurante pequeno também lava a panela. Só lava menos panelas."
    st_techlead "MVP não é desculpa para pular etapa. É para fazer cada etapa menor."
    hide st_techlead
    with dissolve

    show st_mobile thinking at right_zoom
    with dissolve
    st_mobile "E tem um detalhe que pega todo mundo que vem de web: app não é site."
    st_mobile "Cada versão passa pela revisão da Apple e do Google. Pode levar horas, pode levar dias. Depois, cada pessoa ainda precisa atualizar."
    st_mobile "Mano, não dá para dar F5 no celular de 800 pessoas. Se sair bug, ele fica lá até a próxima versão passar na loja."
    hide st_mobile
    with dissolve

    show st_qualidade neutral at right_zoom
    with dissolve
    st_qualidade "E o ciclo só termina quando a gente mede."
    st_qualidade "Primeiro: lançou. Segundo: o estudante voltou a usar? Terceiro: ele confiou no total? Sem essas respostas, a gente só publicou. Não aprendeu nada."
    $ advance_minutes(20)

    # Decisão pedagógica: o que é MVP
    show st_mentora neutral at left_zoom
    st_mentora "[player_name], todo mundo aqui fala MVP o tempo todo. Quero saber o que você entende por isso."

    menu:
        st_mentora "Para a equipe, o que é um MVP?"
        "A menor versão que resolve um problema real e nos deixa aprender com estudantes de verdade.":
            $ st_decidir("st_d02_mvp", True)
            st_mentora "Isso. O “mínimo” é sobre escopo, não sobre qualidade."
            st_mentora "Um app que só lança gasto e mostra o total, mas mostra o total certo, já ensina muita coisa. Um app com vinte telas e o total errado não ensina nada."
        "O app completo, só que sem acabamento, para lançar logo.":
            $ st_decidir("st_d02_mvp", False)
            show st_qualidade neutral at center_zoom
            show st_techlead serious at right_zoom
            with dissolve
            st_techlead "Aí a gente entrega tudo meio quebrado e não sabe qual parte falhou. Foi assim que nasceu o total errado."
            st_techlead "E o estudante não sabe que é MVP. Ele só sabe que a conta dele não bate. A nota 3,4 vem daí."
            hide st_techlead
            show st_qualidade neutral at right_zoom
            with dissolve
        "Um protótipo bonito para impressionar os investidores.":
            $ st_decidir("st_d02_mvp", False)
            show st_qualidade serious at right_zoom
            st_qualidade "Protótipo sem usuário não mede nada. No demo day vão perguntar quem usa e quem voltou."
            st_qualidade "E tela bonita não conserta o total errado de ninguém."
            show st_qualidade neutral at right_zoom

    if not st_d02_mvp:
        # Revisão orientada depois de um distrator.
        menu:
            st_mentora "Junta o que eles disseram. O que sobra?"
            "Então o MVP precisa resolver um problema e gerar aprendizado com gente real?":
                st_mentora "Exato. Pensa no total do mês."
                st_mentora "Um MVP que só lança gasto e mostra o total certo já responde a pergunta que importa: o estudante confia e volta a usar? Isso a gente mede."
                st_mentora "Medalha e tela bonita podem vir depois, se os dados pedirem."

    st_mentora "Anota aí: ciclo inteiro, em voltas curtas. MVP pequeno no escopo, não na qualidade. E, em app, cada volta ainda passa pela loja."
    $ registrar("st_reg_mvp")
    $ advance_minutes(20)

    # Social: como aprender por aqui
    show st_mobile neutral at center_zoom
    with dissolve
    menu:
        st_mentora "Última pergunta, essa sem resposta certa. Como você prefere aprender por aqui?"
        "Fazendo junto, em par.":
            $ add_friendship_point("st_mobile", 1)
            st_mobile "Fechou! Amanhã a gente pareia. Eu dirijo, você navega, depois troca."
        "Observando e anotando primeiro.":
            $ add_friendship_point("st_mentora", 1)
            st_mentora "Bom. Anota tudo e me traz as dúvidas no fim do dia. Dúvida anotada não se perde."
        "Vendo os usuários usarem o app.":
            $ add_friendship_point("st_qualidade", 1)
            st_qualidade "Oxe, gostei. Quando eu for observar estudante usando o app, te chamo. Você vai ver coisa que nenhuma reunião mostra."
    $ advance_minutes(15)

    hide st_mobile
    hide st_qualidade
    with dissolve
    st_mentora "Por hoje é isso. Segunda tem planejamento, e a coluna de descoberta está cheia de pergunta sem resposta."
    hide st_mentora
    with dissolve
    $ advance_minutes(30)
    "{i}Meio-dia. Tainá apaga o quadro, mas deixa as seis palavras em círculo no canto.{/i}"
    "{i}Você sai do aquário pensando que pequeno e malfeito não são a mesma coisa. E que alguém, em algum ônibus, está lançando um gasto agora sem saber se o total vai bater.{/i}"

    return
