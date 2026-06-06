label scene_8_cafe_informal:
    $ set_available()
    play music music_coffee_break_energized fadein 1.0
    scene bg empresa_cafe_tarde
    with fade

    $ advance_minutes(12)
    "{i}No meio da tarde, após um intenso período de revisão de requisitos, você percebe que parte da equipe está reunida na cafeteria do escritório.{/i}"
    with dissolve
    "{i}O aroma do café recém-passado se espalha pelo ambiente.{/i}"

    show developer_coding neutral at left_zoom
    show developer_test enthusiastic at right_zoom

    developer_coding "Ei, [player_name], vem sentar com a gente! Precisamos de um intervalo para recarregar as ideias."
    developer_test "E quem sabe a gente não aproveita para falar de bugs e de memes também?"

    "{i}Você se senta ao lado deles, pegando uma caneca de café. O papo começa leve e descontraído.{/i}"

    menu:
        "Sobre o que você quer conversar?"
        "Pergunto sobre experiências em projetos anteriores.":
            $ add_friendship_point("developer_coding", 1)
            show developer_coding serious at left_zoom
            developer_coding "Já trabalhei em projetos grandes, e te digo: cada time é único. O segredo é sempre aprender com os erros dos outros (e com os nossos, claro)."
            show developer_test enthusiastic at right_zoom
            developer_test "Eu entrei nesse mundo porque adorava resolver problemas desde pequeno. Hoje, cada bug é um desafio divertido pra mim."
        "Falo sobre tecnologia nova ou tendências.":
            $ add_friendship_point("developer_test", 1)
            show developer_test confident at right_zoom
            developer_test "Já viu aquele novo framework de testes automatizados? Fiquei viciado, deixa o deploy muito mais seguro."
            show developer_coding thinking at left_zoom
            developer_coding "Sou um pouco cético com novidades... mas admito que tecnologia bem escolhida faz diferença no longo prazo."
        "Prefiro perguntar sobre hobbies e vida fora do trabalho.":
            $ add_friendship_point("developer_test", 1)
            $ add_friendship_point("developer_coding", 1)
            show developer_coding neutral at left_zoom
            developer_coding "Gosto de cozinhar para relaxar, acredita? Nada como um bom risoto depois de um dia de deploy tenso."
            show developer_test positive at right_zoom
            developer_test "Eu corro todo dia, inclusive para pensar melhor nos problemas. Esporte limpa a mente!"
        "Peço dicas de como não se perder com tantas tarefas.":
            $ add_friendship_point("developer_coding", 1)
            show developer_coding thinking at left_zoom
            developer_coding "Organização é tudo! Uso checklist até para lembrar de tomar café. E sempre tento fechar o que comecei antes de abrir coisa nova."
            show developer_test enthusiastic at right_zoom
            developer_test "Eu faço mini-metas diárias, tipo: hoje resolvo pelo menos um bug cabeludo!"
        "Conto um perrengue engraçado que vivi em outro estágio.":
            $ add_friendship_point("developer_test", 1)
            show developer_test enthusiastic at right_zoom
            developer_test "Hahaha, todo dev já passou por isso! Um dia deletei a base de dados de teste achando que era produção!"
            show developer_coding neutral at left_zoom
            developer_coding "O importante é rir dos perrengues e aprender. E nunca, jamais, deployar na sexta-feira à noite!"

    $ advance_minutes(10)
    with dissolve
    "{i}A conversa esquenta, misturando histórias engraçadas, confissões de bugs e dicas profissionais. O grupo se diverte e aprende junto.{/i}"

    # Segunda rodada de diálogo - o grupo propõe perguntas ao jogador
    show developer_test thinking at right_zoom
    developer_test "Aliás, [player_name], você prefere testar seu próprio código ou acha melhor outra pessoa revisar?"

    menu:
        "Como você responde?"
        "Gosto de revisar o código dos outros e receber revisão também.":
            $ add_friendship_point("developer_coding", 1)
            show developer_coding positive at left_zoom
            developer_coding "Ótimo espírito de equipe! Code review bem feito salva projetos inteiros."
        "Prefiro revisar meu próprio código, me faz aprender com os próprios erros.":
            $ add_friendship_point("developer_test", 1)
            show developer_test confident at right_zoom
            developer_test "Isso é importante, mas feedback externo traz visões novas também!"
        "O ideal é combinar os dois, né?":
            $ add_friendship_point("developer_test", 1)
            $ add_friendship_point("developer_coding", 1)
            show developer_coding neutral at left_zoom
            developer_coding "Exato! Revisão cruzada e autoanálise fazem um dev crescer rápido."

    $ advance_minutes(6)
    with dissolve

    # Intervenção surpresa
    show developer_ai positive at center_zoom
    developer_ai "Falando em crescer, alguém topa um hackathon no fim de semana? Só não vale perder pro time de QA de novo, hein!"
    hide developer_ai

    "{i}Entre goles de café, você percebe que está se integrando mais à equipe. O ambiente é leve, e o clima de camaradagem motiva todo mundo.{/i}"

    hide developer_test
    hide developer_coding

    play music music_office_relaxed fadein 1.5
    scene bg escritorio_interior_tarde
    with dissolve
    $ advance_minutes(7)
    "{i}Revigorado(a) pelo café e pela conversa, você retorna ao trabalho com novas ideias e a certeza de que não está sozinho(a) nessa jornada.{/i}"

    return
