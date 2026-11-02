# co_12_casa_sem3.rpy
# Semana 3, sexta, 19h às 22h. Releitura do rascunho (co_escrita_*), mensagem
# do Jorge com a foto de 2008, contatos e cartão da semana.
# Fonte: docs/rotas/corporativo.md, co_12.

label co_12_casa_sem3:
    $ set_available('all')
    $ set_time(19, 0)

    play music music_streets_focused fadein 1.0
    scene bg transito_noite
    with fade

    "{i}Sexta-feira, sete da noite. O ônibus anda devagar pela avenida, e você consegue um lugar na janela.{/i}"

    if co_escrita_status == "rascunho":
        "{i}No celular, você abre o rascunho que guardou na quinta, sobre reabrir chamado. Lido de novo, com a cabeça mais fria:{/i}"
        $ narrator(__("Requisito: ") + co_escrita_requisito)
        $ narrator(__("Critério: ") + co_escrita_criterio)
        "{i}Algumas palavras você trocaria. Mas a ideia está lá: quem reabre, por quê, e o que a pessoa vê depois. Segunda, o [NOME_CO_SOLICITANTE] vai dizer se entende o mesmo.{/i}"
    else:
        "{i}Você lembra do exercício sobre reabrir chamado, que ficou pendente na quinta. O rascunho continua guardado no notebook, esperando uma segunda tentativa.{/i}"
        "{i}Sem pressa. Pendência registrada não se perde.{/i}"

    "{i}Pela janela, uma fila de caminhões da empresa de energia passa no sentido contrário. Alguém, em algum lugar, vai abrir um chamado hoje à noite.{/i}"

    play music music_home_reflecting fadein 1.5
    scene bg quarto_noite
    with fade
    $ set_time(20, 15)

    "{i}Em casa, você larga a mochila e abre o notebook. Antes de esquecer, escreve na primeira página da semana:{/i}"
    "Falta alguma coisa? Quem, quando, sob qual condição.\nTem duas leituras? \"Rápida\" não é número."
    "Briga com outra regra? Leva para quem é dona dela."
    "{i}Três linhas. Parecem simples, mas pegaram defeitos que iam virar semanas de retrabalho.{/i}"

    $ advance_minutes(40)
    play sound "audio/effects/cell_vibration.ogg"
    show co_legado portrait at left_zoom
    with dissolve
    co_legado "(mensagem no grupo da equipe) Achei no armário uma foto do lançamento do SGC, 2008. Repararam no cabelo? Eu também tinha."
    co_legado "(mensagem no grupo da equipe) A gente comemorou com pão de queijo e uma queda do servidor às onze da noite."

    menu (tipo="conversa"):
        "Como você responde ao [NOME_CO_LEGADO]?"
        "Quem são os outros da foto?":
            $ add_friendship_point("co_legado", 1)
            co_legado "(mensagem) O de gravata era o gerente do projeto. Hoje dá aula de violão. Os dois de camiseta preta eram os DBAs. Um deles batizou a Tia Neide."
            co_legado "(mensagem) E a moça de crachá da central, no canto, testando a primeira tela? É a [NOME_CO_MENTORA]. Não conta que eu contei."
        "Dá para colocar essa foto no wiki do SGC?":
            $ add_friendship_point("co_qualidade", 1)
            hide co_legado
            show co_qualidade portrait at left_zoom
            with dissolve
            co_qualidade "(mensagem no grupo da equipe) Mais um ponto para a documentação. Coloca com data e nomes, [NOME_CO_LEGADO]. Foto sem legenda daqui a dez anos é mistério."
        "Curtir a foto.":
            "{i}Você deixa um coração na foto. [NOME_CO_LEGADO] responde com um polegar e mais nada, como bom veterano.{/i}"

    hide co_legado
    hide co_qualidade
    with dissolve

    "{i}A semana pesou, mas foi boa. Talvez valha mandar mensagem para mais alguém antes de dormir.{/i}"

    call screen contacts_screen

    $ set_time(22, 0)
    scene black
    with fade
    window hide
    pause 1.1
    window show

    "Fim da Semana 3\n\nAprendizado: requisito bom é aquele que duas pessoas leem e entendem a mesma coisa."

    return
