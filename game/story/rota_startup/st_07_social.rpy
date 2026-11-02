# st_07_social.rpy
# Rota Startup, semana 2, quinta, 17h30 a 19h00. Bíblia: docs/rotas/startup.md (st_07).

label st_07_social:
    $ set_available("st_mentora", "st_techlead", "st_ceo", "st_estudante")
    $ set_time(17, 30)

    play music music_coffee_break_energized fadein 1.0
    scene bg empresa_cafe_tarde
    with fade

    "{i}Quinta-feira, fim de expediente. [NOME_ST_MOBILE] fecha o notebook com um estalo e aponta para a escada.{/i}"

    show st_mobile neutral at left_zoom
    with dissolve
    st_mobile "Bora descer? O café do térreo tira o pão de queijo do forno às cinco e meia. Quem chega primeiro pega o quentinho."

    show st_qualidade neutral at right_zoom
    with dissolve
    st_qualidade "Eu vou junto. Li avaliação o dia inteiro, preciso de comida e de gente."

    $ advance_minutes(10)
    play sound "audio/effects/xicara_cafe.ogg"
    "{i}Vocês sentam numa mesinha perto da janela. Três cafés, uma cesta de pão de queijo e um celular de teste que [NOME_ST_MOBILE] não larga nem aqui.{/i}"

    menu:
        "Sobre o que você puxa conversa?"

        "Como foi seu primeiro app, [NOME_ST_MOBILE]?":
            $ add_friendship_point("st_mobile", 1)
            show st_mobile thinking at left_zoom
            st_mobile "Pô, foi aos 17. Uma calculadora de nota: você botava as provas e ela dizia quanto faltava para passar."
            st_mobile "Três colegas usaram. Três! E um deles achou um bug no primeiro dia: se a prova valia zero, o app travava."
            show st_mobile neutral at left_zoom
            st_mobile "Foi ali que eu entendi que usuário sempre acha o caminho que você não testou. Até hoje."
            st_qualidade "No meu caso, o primeiro sistema que eu testei foi uma pilha de redação. Eu era professora de Português antes."

        "Como foi sair da sala de aula para a tecnologia, [NOME_ST_QUALIDADE]?":
            $ add_friendship_point("st_qualidade", 1)
            show st_qualidade thinking at right_zoom
            st_qualidade "Eu dava aula de Português em Campina Grande. Corrigia umas oitenta redações por semana."
            st_qualidade "E corrigir redação ensina a ler requisito, sabia? Primeiro: a frase diz o que parece dizer? Segundo: dá para entender de dois jeitos? Terceiro: tem prova do que está afirmando?"
            show st_qualidade neutral at right_zoom
            st_qualidade "Quando vi um documento de requisitos pela primeira vez, pensei: oxe, é uma redação com consequência."
            st_mobile "E eu, que fiz meu primeiro app aos 17 sem ler nada disso. Uma calculadora de nota. Três usuários."

        "Qual app de banco mais irrita vocês?":
            $ add_friendship_point("st_mobile", 1)
            show st_mobile neutral at left_zoom
            st_mobile "Mano, o que pede para atualizar toda vez que eu abro. Eu só queria ver o saldo!"
            st_qualidade "O meu esconde o extrato atrás de três menus. Toda vez eu acho que mudaram de lugar."
            "{i}Os dois riem juntos, cada um lembrando de uma tela pior que a outra.{/i}"
            show st_qualidade thinking at right_zoom
            st_qualidade "Mas repara: tudo o que a gente acabou de falar é requisito. Reclamação é requisito disfarçado."
            st_mobile "Isso me lembra meu primeiro app, aos 17: uma calculadora de nota. Três usuários. A primeira reclamação virou a primeira correção."

    $ advance_minutes(25)
    show st_mobile thinking at left_zoom
    st_mobile "Falando em bug, amanhã eu abro um PR. Pequeno, prometo."
    st_qualidade "Pequeno de verdade?"
    show st_mobile neutral at left_zoom
    st_mobile "Pequeno de verdade! PR pequeno é PR revisado. PR gigante é PR aprovado sem ler."
    st_qualidade "Anota essa, [player_name]. Ele mesmo vai esquecer daqui a duas semanas."

    show st_mobile thinking at left_zoom
    st_mobile "Outra coisa que aprendi aqui: testo tudo no celular mais barato da loja. Se roda nele, roda em qualquer um."
    st_mobile "O meu celular é rápido demais. Ele mente para mim."
    st_qualidade "A [NOME_ST_ESTUDANTE] usa um de 2019. É nele que a gente tem que pensar."

    $ advance_minutes(20)
    show st_qualidade neutral at right_zoom
    st_qualidade "E vocês, vão descansar no fim de semana? Startup tem esse costume ruim de achar que sábado é dia útil."
    st_mobile "Sábado tem partida online. Isso conta como descanso, né?"
    st_qualidade "Depende de quanto você grita no microfone."
    st_qualidade "Ah, mês que vem eu faço um teste de usabilidade com calouros. Cinco estudantes usando o app na minha frente, sem eu ajudar."
    st_mobile "E sábado, a partida. Tem vaga no time, [player_name]."

    menu:
        "Os dois esperam sua resposta."

        "Topo assistir ao teste de usabilidade com os calouros.":
            $ add_friendship_point("st_qualidade", 1)
            show st_qualidade neutral at right_zoom
            st_qualidade "Oba! Só tem uma regra: a gente não ajuda. Nem um dedinho apontando. O silêncio dói, mas ensina."

        "Topo a partida online de sábado.":
            $ add_friendship_point("st_mobile", 1)
            show st_mobile neutral at left_zoom
            st_mobile "Fechou! Te mando o link. Aviso: eu sou péssimo, mas falo muito."

        "Vou descansar no fim de semana.":
            show st_mobile neutral at left_zoom
            st_mobile "Justo. Descanso também entra na sprint."
            st_qualidade "Melhor resposta da mesa, inclusive."

    $ advance_minutes(25)
    "{i}A cesta esvazia. Lá fora, os postes de Botafogo acendem um por um.{/i}"
    st_mobile "Bora? Amanhã tem conversa diária às dez, e eu quero chegar antes do café acabar."
    st_qualidade "Até amanhã, [player_name]. Obrigada pela companhia."

    hide st_mobile
    hide st_qualidade
    with dissolve

    $ advance_minutes(10)
    "{i}Você sobe a rua até o ponto de ônibus. A semana foi de post-its, entrevista e números, mas o que fica na cabeça é a risada dos dois na mesinha da janela.{/i}"
    "{i}Na Trocado, pelo jeito, a equipe também se constrói no intervalo.{/i}"

    return
