# co_07_cafe.rpy
# Semana 2, sexta, 15h30 às 16h15. Café com Jorge e Kauã: reescrever ou conviver?
# Planta a ideia de estrangulamento (figueira mata-pau) sem o nome técnico.
# Só menus sociais. Fonte: docs/rotas/corporativo.md, co_07.

label co_07_cafe:
    $ set_available("co_mentora", "co_qualidade", "co_supervisora", "co_solicitante")
    $ set_time(15, 30)

    play music music_coffee_break_energized fadein 1.0
    scene bg empresa_cafe_tarde
    with fade

    "{i}Sexta-feira, 15h30. O café do andar tem cheiro de pão de queijo e uma máquina de expresso que só funciona com tapa.{/i}"

    show co_dev neutral at left_zoom
    show co_legado neutral at right_zoom
    with dissolve

    co_dev "[player_name], olha isso. Achei hoje lendo o código do fechamento."
    "{i}[NOME_CO_DEV] vira o celular. Na tela, um trecho de código antigo com um comentário em letras maiúsculas: \"NAO MEXER - JT 2010\".{/i}"
    co_dev "JT. [NOME_CO_LEGADO] Takeda. Tô certo ou tô certo?"
    show co_legado thinking at right_zoom
    co_legado "Culpado. Sexta à noite, 2010. O cálculo do prazo do SLA pula feriado, e os feriados estão escritos à mão no código."
    co_legado "Toda virada de ano alguém acrescenta uma linha. Ninguém nunca teve coragem de trocar por uma tabela."
    co_dev "Catorze anos de linhas de feriado. Isso já é sítio arqueológico."

    menu (tipo="conversa"):
        "Sobre o que você puxa assunto?"

        "[NOME_CO_LEGADO], como era programar em 2008?":
            $ add_friendship_point("co_legado", 1)
            show co_legado neutral at right_zoom
            co_legado "Java 6, servidor no subsolo e deploy de madrugada, copiando arquivo na mão."
            co_legado "Teste era ligar para a central e perguntar se a tela abriu. Se a Neusa dizia que sim, estava aprovado."

        "[NOME_CO_DEV], por que você escolheu trabalhar com legado?":
            $ add_friendship_point("co_dev", 1)
            show co_dev thinking at left_zoom
            co_dev "Sinceridade? Precisava do emprego."
            show co_dev neutral at left_zoom
            co_dev "Fiquei porque descobri que gosto de mistério. Cada rotina estranha aqui é um episódio de série policial."

        "Qual o código mais estranho que vocês já viram aqui?":
            $ add_friendship_point("co_legado", 1)
            show co_legado thinking at right_zoom
            co_legado "Ah, aí eu conto a da Tia Neide inteira. Em 2009, o servidor do SGC caía todo dia às três da tarde."
            co_legado "Alguém escreveu um código que salvava tudo às 14h55, por precaução. Funcionou, mas ninguém sabia por que o servidor caía."
            co_legado "Três semanas depois, descobrimos. A dona Neide, da limpeza, desligava o ar-condicionado da sala às três para economizar luz."
            co_legado "O servidor esquentava e desmaiava. A gente fez um cartaz, ela virou nossa maior aliada, e o servidor ganhou o nome dela."
            co_dev "E o código das 14h55?"
            co_legado "Ainda está lá. Isso aí tem história."

    $ advance_minutes(15)
    show co_dev neutral at left_zoom
    co_dev "Mas falando sério: um dia o SGC vai ter que morrer. Não dá para viver de comentário \"não mexer\" para sempre."
    show co_legado neutral at right_zoom
    co_legado "Sistema grande não morre, [NOME_CO_DEV]. É substituído aos pedaços."
    co_legado "Já viu figueira mata-pau? Ela nasce em cima de uma árvore velha e vai descendo raiz em volta dela."
    co_legado "Anos depois, a árvore velha some lá dentro e a figueira fica de pé sozinha. Ninguém derrubou nada num dia só."
    show co_dev thinking at left_zoom
    co_dev "Ou seja: em vez de demolir o prédio, a gente vai construindo do lado e mudando os moradores aos poucos."
    co_legado "Isso. E com a central atendendo o tempo todo, que ninguém aqui pode parar."

    menu (tipo="conversa"):
        "Na discussão sobre reescrever, você..."

        "[NOME_CO_DEV], o que você trocaria primeiro, se pudesse?":
            $ add_friendship_point("co_dev", 1)
            show co_dev neutral at left_zoom
            co_dev "A consulta do chamado, fácil. É onde mais gente sofre e onde o SGC menos ajuda."
            co_dev "Se ela funcionar fora do SGC, as ligações de \"e meu chamado?\" da [NOME_CO_SUPERVISORA] despencam. Bora!"

        "[NOME_CO_LEGADO], o que você nunca deixaria mudar sem teste?":
            $ add_friendship_point("co_legado", 1)
            show co_legado serious at right_zoom
            co_legado "O fechamento de chamado e a rotina das 72 h. Os dois mexem em número que vai para a diretoria."
            co_legado "Mexeu sem teste, o relatório do mês seguinte conta a história errada. E ninguém percebe até ser tarde."

        "Prefiro ouvir mais antes de opinar.":
            show co_legado neutral at right_zoom
            co_legado "Prudente."
            co_dev "Prudente demais. Mas tudo bem, a gente te convence até a semana 8."

    $ set_time(16, 15)
    "{i}O expresso finalmente sai, depois do terceiro tapa. Os três voltam para as mesas.{/i}"
    co_dev "Vou pedir para tombarem aquele comentário. Patrimônio histórico do Grupo Vértice."
    co_legado "Se tombarem, eu exijo placa."

    hide co_dev
    hide co_legado
    with dissolve

    return
