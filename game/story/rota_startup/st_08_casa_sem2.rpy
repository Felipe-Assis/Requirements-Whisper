# st_08_casa_sem2.rpy
# Rota Startup, semana 2, sexta, 20h00 a 22h00. Bíblia: docs/rotas/startup.md (st_08).

label st_08_casa_sem2:
    $ set_available("all")
    $ set_time(20, 0)

    play music music_streets_focused fadein 1.0
    scene bg transito_noite
    with fade

    play sound "audio/effects/bus.ogg"
    "{i}Sexta-feira, oito da noite. O ônibus sai de Botafogo devagar, preso no trânsito da praia. Você abre o notebook no colo.{/i}"
    "{i}As anotações da semana estão ali, em ordem:{/i}"
    "• O episódio da [NOME_ST_ESTUDANTE]: almoço de R$ 20, sinal caindo, toque repetido, total errado.\n• A regra: excluir com confirmação e ver o total atualizado.\n• O conflito: total confiável primeiro; importação do banco como hipótese.\n• As quatro colunas da parede de vidro."
    "{i}Quando o ônibus entra no túnel, você olha o celular por reflexo. O app está quieto. Desta vez, nada para lançar.{/i}"

    $ advance_minutes(50)
    play music music_home_dreamy fadein 1.5
    scene bg quarto_noite
    with fade

    "{i}Em casa, mochila na cadeira, tênis largados no canto. O celular vibra antes de você sentar.{/i}"
    play sound "audio/effects/cell_vibration.ogg"
    show st_estudante portrait at left_zoom
    with dissolve
    st_estudante "(mensagem) Oi! Lembrei de uma coisa depois da entrevista. Olha isso."
    "{i}Chega uma foto: um caderno de papel com capa de flores, cada página dividida em data, gasto e valor. Bandejão, R$ 4,50. Ônibus, R$ 4,30. Xerox, R$ 3.{/i}"
    st_estudante "(mensagem) É aqui que eu confiro quando o app erra. Toda noite. Minha colega de república faz igual."
    hide st_estudante
    with dissolve
    "{i}Um caderno paralelo para conferir o app. É a solução de contorno que a pessoa inventa quando o sistema não dá conta. E é a prova mais forte de que a necessidade é real.{/i}"

    $ advance_minutes(15)
    play sound "audio/effects/cell_vibration.ogg"
    show st_techlead portrait at left_zoom
    with dissolve
    st_techlead "(mensagem) Boa noite, [player_name]. A [NOME_ST_QUALIDADE] me contou do gasto duplicado no túnel."
    st_techlead "(mensagem) Veja bem: fiquei curioso. Você lembra o horário exato? Se tiver, quero cruzar com os registros do servidor."
    "{i}Você confere a anotação da semana passada e responde: sexta, por volta das 19h40, entrando no túnel, lanche de R$ 7, dois toques em Salvar.{/i}"
    st_techlead "(mensagem) Perfeito. Com horário, um bug deixa de ser fantasma. Vou cruzar com os registros e te chamo quando tiver uma resposta."
    $ add_friendship_point("st_techlead", 1)
    hide st_techlead
    with dissolve

    $ advance_minutes(20)
    "{i}Você abre os slides da disciplina de Engenharia de Software. Na aula de elicitação, a lista de técnicas parecia simples: entrevista, questionário, observação, análise de documentos.{/i}"
    "{i}Na prática, elas se misturaram na mesma semana. As 37 avaliações apontaram onde cavar. A entrevista explicou por quê. E o caderno da [NOME_ST_ESTUDANTE] mostrou o que ela faz quando ninguém está olhando.{/i}"
    "Quem será que ainda está online?"

    call screen contacts_screen

    window hide
    pause 0.8
    window show

    $ advance_minutes(35)
    "{i}Você fecha o notebook. Na última página, uma frase escrita à mão: \"Perguntar pela última vez em que aconteceu.\"{/i}"

    scene black
    with fade

    window hide
    pause 1.0
    window show

    "{i}Fim da Semana 2\n\nPergunte pela última vez em que aconteceu. Adjetivo vira tarefa; conflito vira objetivo comum.{/i}"

    return
