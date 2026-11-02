# st_14_comemoracao.rpy
# Rota Startup, semana 4, sexta. Festa dos mil estudantes no terraço e
# volta para casa. Fonte: docs/rotas/startup.md, seção st_14_comemoracao.

label st_14_comemoracao:
    $ set_available("st_estudante")
    $ set_time(18, 0)

    play music music_coffee_break_energized fadein 1.0
    scene bg startup_terraco_noite
    with fade

    "{i}Sexta-feira, fim de tarde. A notícia correu pelo grupo da equipe às três da tarde: o beta passou de mil estudantes cadastrados.{/i}"
    "{i}Ninguém comprou anúncio. Foi boca a boca, de república em república. Vinícius encomendou pizza e chamou todo mundo para o terraço do casarão.{/i}"
    "{i}Lá em cima, um varal de lâmpadas amarelas cruza o deck de madeira. Ao fundo, o Pão de Açúcar aparece escuro contra o céu de Botafogo.{/i}"

    show st_ceo neutral at center_zoom
    with dissolve
    st_ceo "Mil! Mil estudantes, gente! Três meses atrás eram oitenta, e metade era primo de alguém aqui."
    st_ceo "A pizza chega em vinte minutos. Até lá, todo mundo ajuda a deixar isso aqui com cara de festa!"

    show st_mobile neutral at right_zoom
    show st_mentora neutral at left_zoom
    with dissolve
    st_mobile "Eu cuido do som. Alguém me salva dessa playlist de pitch do Vinícius?"
    st_mentora "E alguém precisa lembrar que copo não nasce sozinho na mesa."

    menu (tipo="conversa"):
        "Como você ajuda na festa?"

        "Monto a playlist com o Davi.":
            $ add_friendship_point("st_mobile", 1)
            st_mobile "Bora! Regra única: nada de música de elevador. E uma do jogo de sábado, pra dar sorte."
            "{i}Vocês discutem cada faixa como se fosse code review. A playlist final tem forró, rock nacional e uma trilha de videogame que só Davi reconhece.{/i}"

        "Escrevo no quadro os nomes dos beta testers que mais mandaram feedback, com a Bia no topo.":
            $ add_friendship_point("st_qualidade", 1)
            hide st_mobile
            show st_qualidade neutral at right_zoom
            with dissolve
            "{i}Você pega o quadro branco portátil e escreve, com letra grande: “Valeu, beta testers!”. Embaixo, os nomes de quem mais mandou feedback. A Bia em primeiro.{/i}"
            st_qualidade "Oxe... Você leu as avaliações pra montar isso?"
            "{i}Lorena tira os óculos e passa a mão nos olhos.{/i}"
            st_qualidade "Desculpa, me pegou. Essas pessoas escrevem pra gente às onze da noite, irritadas, e ainda assim explicam direitinho o que aconteceu. Quase ninguém agradece a elas."

        "Preparo o guaraná com gelo e os copos para todo mundo.":
            $ add_friendship_point("st_mentora", 1)
            st_mentora "Salvou a festa. Sabe que no banco a gente comemorava meta com bolo seco na copa? Isso aqui é outro nível."
            "{i}Vocês enchem os copos lado a lado. Tainá conta, rindo, que a primeira reunião da Trocado foi numa mesa de bar, com o app desenhado num guardanapo.{/i}"

    hide st_ceo
    hide st_mobile
    hide st_mentora
    hide st_qualidade
    with dissolve

    $ advance_minutes(40)
    "{i}A pizza chega. Alguém derruba guaraná no deck, alguém ri alto demais, e por alguns minutos ninguém fala de prazo.{/i}"

    show st_qualidade thinking at left_zoom
    show st_techlead neutral at right_zoom
    with dissolve
    "{i}Perto do guarda-corpo, Lorena olha o celular, depois a festa, e fala baixinho para você e Otávio:{/i}"
    st_qualidade "Tô feliz, juro. Mas mil cadastros não quer dizer mil pessoas usando. Cadê a evidência de que elas voltam?"
    st_qualidade "A retenção ainda tá em 22%%. Primeiro, a gente comemora. Segundo, a gente não confunde as duas coisas."
    st_techlead "Concordo. Segunda isso entra na pauta. Hoje é dia de pizza."

    hide st_qualidade
    hide st_techlead
    with dissolve

    $ advance_minutes(30)
    show st_ceo neutral at center_zoom
    with dissolve
    st_ceo "Atenção, time! Brinde! E quem faz o brinde é a pessoa mais nova da casa. [player_name], a palavra é sua!"
    "{i}Sete copos de guaraná se erguem na sua direção. Você respira fundo.{/i}"

    menu (tipo="conversa"):
        "O que você diz no brinde?"

        "“Aos mil, e aos que vão continuar usando.”":
            $ add_friendship_point("st_techlead", 1)
            show st_techlead neutral at right_zoom
            with dissolve
            st_techlead "Essa é a métrica certa."
            "{i}Otávio ergue a caneca esmaltada, cheia de guaraná, e Lorena faz um sinal de positivo do outro lado do terraço.{/i}"

        "“Ao time que me recebeu tão bem.”":
            $ add_friendship_point("st_mentora", 1)
            show st_mentora neutral at left_zoom
            with dissolve
            st_mentora "Ah, assim não vale. Agora todo mundo vai ficar com cara de emoção."
            "{i}Tainá bate o copo no seu com força demais. Um pouco de guaraná cai no seu tênis, e ninguém se importa.{/i}"

        "“Ao próximo bug que a gente vai achar antes do usuário.”":
            $ add_friendship_point("st_qualidade", 1)
            show st_qualidade neutral at left_zoom
            with dissolve
            st_qualidade "Esse brinde é meu. Vou imprimir e colar no monitor."
            "{i}Davi solta um “uhuuul” de quem não tem certeza se o bug é dele.{/i}"

    st_ceo "Aos mil! E aos próximos!"

    hide st_ceo
    hide st_techlead
    hide st_mentora
    hide st_qualidade
    with dissolve

    $ set_time(20, 40)
    "{i}Mais tarde, a música baixa e a equipe se espalha pelos puffs. Você vai até o guarda-corpo pegar um pouco de vento. Otávio já está lá.{/i}"

    show st_techlead thinking at center_zoom
    with dissolve
    st_techlead "Startup cansa, viu. Dá vontade de provar alguma coisa virando a noite."
    st_techlead "Veja bem: ninguém aqui precisa disso. Código escrito às quatro da manhã eu revejo às dez, e sempre acho alguma coisa."
    st_techlead "Vai pra casa cedo hoje. Segunda a gente precisa da sua cabeça descansada, não de heroísmo."
    if energia_cansaco():
        st_techlead "E pelo seu jeito, você sabe do que eu tô falando. Pega um pedaço de pizza pra viagem e vai."
    "{i}Ele bate de leve no guarda-corpo, como quem encerra o assunto, e volta para a mesa da pizza.{/i}"

    hide st_techlead
    with dissolve

    # Volta para casa.
    $ set_available("all")
    $ set_time(21, 30)
    play music music_home_dreamy fadein 1.5
    scene bg quarto_noite
    with fade

    "{i}Em casa, você tira o tênis com cheiro de guaraná e se joga na cama. O celular vibra.{/i}"
    play sound "audio/effects/cell_vibration.ogg"
    show st_estudante portrait at left_zoom
    st_estudante "(mensagem) Égua, mil! Metade da minha república tá lá agora. Tipo assim: não me façam passar vergonha, hein?"
    hide st_estudante

    "{i}Você ri olhando a tela. Mil pessoas confiaram no app o bastante para baixar. A pergunta de Lorena continua na sua cabeça: quantas vão voltar?{/i}"
    "{i}Talvez valha mandar uma mensagem para alguém da equipe antes de dormir.{/i}"

    call screen contacts_screen

    scene black
    with fade
    window hide
    pause 1.1
    window show

    "{i}Fim da Semana 4\n\nComemorar é importante. Saber o que o número mede também.{/i}"

    return
