# co_08_casa_sem2.rpy
# Semana 2, sexta, 20h às 22h. Volta para casa, revisão do notebook e mensagem do
# Kauã. Termina com a tela de contatos e o cartão da semana.
# Fonte: docs/rotas/corporativo.md, co_08.

label co_08_casa_sem2:
    $ set_available('all')
    $ set_time(20, 0)

    play music music_streets_focused fadein 1.0
    scene bg transito_noite
    with fade

    play sound "audio/effects/bus.ogg"
    "{i}O ônibus sai do centro devagar, preso no trânsito de sexta. Você encosta a cabeça na janela.{/i}"
    "{i}Uma rotina de 2013 fechando chamados sozinha. Um manual que ainda fala de um estado extinto. Um técnico parado um dia inteiro na base, esperando uma resposta que já existia.{/i}"
    "{i}Nada disso estava em documento nenhum. Estava nos dados, no código e na cabeça das pessoas.{/i}"
    $ advance_minutes(50)

    play music music_home_dreamy fadein 1.5
    scene bg quarto_noite
    with fade

    "{i}No quarto, você larga a mochila e abre o notebook.{/i}"
    show item notebook_fechado as notebook at center_zoom
    pause 0.7

    "Você relê as anotações da semana:\n• O episódio do Wellington e o dia de campo perdido\n• O que o [NOME_CO_SOLICITANTE] precisa: abrir o chamado pelo número e ver estado, quem pegou e o que foi feito\n• 18\% das ligações da central são cobrança de andamento\n• As quatro colunas: funcional, não funcional, restrição e desejo"
    "{i}Você sublinha uma frase da [NOME_CO_MENTORA]: \"Quando duas fontes discordam, aí tem pergunta boa.\"{/i}"
    hide notebook
    $ advance_minutes(20)

    play sound "audio/effects/cell_vibration.ogg"
    show co_dev portrait at left_zoom
    with dissolve
    co_dev "(mensagem) Olha o que eu fiz kkk"
    "{i}É uma foto do comentário \"NAO MEXER - JT 2010\", agora dentro de uma moldura dourada desenhada, com uma plaquinha embaixo: \"Patrimônio tombado\".{/i}"
    co_dev "(mensagem) Já mandei imprimir. Segunda vai para a parede do lado do calendário da [NOME_CO_QUALIDADE]."

    menu (tipo="conversa"):
        "Como você responde ao [NOME_CO_DEV]?"

        "Tombado pelo patrimônio. Ninguém mexe.":
            $ add_friendship_point("co_dev", 1)
            co_dev "(mensagem) kkkkk exatamente. Só com RFC e escolta armada."

        "Encaminho ao [NOME_CO_LEGADO] pedindo a história completa.":
            $ add_friendship_point("co_legado", 1)
            hide co_dev
            show co_legado portrait at left_zoom
            with dissolve
            "{i}Dez minutos depois, chega uma mensagem do [NOME_CO_LEGADO]. É longa.{/i}"
            co_legado "(mensagem) Era sexta, 2010, onze da noite. O prazo do SLA estava contando o Carnaval como dia útil e a diretoria queria o relatório na segunda."
            co_legado "(mensagem) Escrevi os feriados à mão, testei com três chamados e deixei o aviso para ninguém estragar. Era para trocar na semana seguinte."
            co_legado "(mensagem) A semana seguinte ainda não chegou. Diz para o [NOME_CO_DEV] que a moldura podia ser de madeira. Dourado é exagero."
            hide co_legado

        "Não respondo hoje.":
            "{i}A foto arranca uma risada. Você deixa o celular na mesa e decide responder na segunda.{/i}"

    hide co_dev
    with dissolve

    $ advance_minutes(15)
    "{i}Antes de dormir, você pega o celular de novo.{/i}"
    "Quem será que ainda está online?"

    call screen contacts_screen

    window hide
    pause 0.8
    window show

    "{i}Na faculdade, levantar requisitos parecia perguntar o que as pessoas querem. Esta semana mostrou outra coisa: primeiro, perguntar o que aconteceu.{/i}"
    "{i}Você fecha o notebook e apaga a luz.{/i}"
    $ set_time(22, 0)

    scene black
    with fade

    window hide
    pause 1.0
    window show

    "Fim da Semana 2\n\nAprendizado: antes de perguntar o que querem, pergunte o que aconteceu."

    return
