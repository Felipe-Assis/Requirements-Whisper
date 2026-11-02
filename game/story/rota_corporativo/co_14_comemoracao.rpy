# co_14_comemoracao.rpy
# Semana 4, sexta. Surpresa dos 25 anos de casa do Jorge, aposentadoria em
# março e a homenagem (conquista social Memória Viva). Volta para casa.
# Fonte: docs/rotas/corporativo.md, seção co_14.

label co_14_comemoracao:
    $ set_available("co_supervisora", "co_solicitante")
    $ set_time(16, 0)

    play music music_office_relaxed fadein 1.0
    scene bg escritorio_interior_tarde
    with fade

    "{i}Sexta-feira, fim da semana 4. O andar está no ritmo de sexta: menos telefone, mais conversa no corredor.{/i}"

    show co_mentora thinking at left_zoom
    with dissolve
    co_mentora "[player_name], olha isso. A intranet diz que o [NOME_CO_LEGADO] completa 25 anos de Grupo Vértice hoje."
    co_mentora "Ele não falou nada para ninguém, claro. Vamos fazer uma surpresa? Ele está numa reunião na diretoria e volta às 17h30."
    show co_dev neutral at right_zoom
    with dissolve
    co_dev "Bora! Tenho uma ideia de bolo que vai entrar para a história."
    show co_qualidade neutral at center_zoom
    with dissolve
    co_qualidade "Uma hora e meia. Dá tempo, se cada um pegar uma tarefa. Já estou montando a lista."

    menu:
        "Como você ajuda na surpresa?"
        "Ajudar o [NOME_CO_DEV] com o bolo: a tela do SGC em papel de arroz.":
            $ add_friendship_point("co_dev", 1)
            $ co_contribuicao_festa = "bolo"
            co_dev "Eu desenho a tela cinza, você confere se as abas em degradê estão certas. Fidelidade histórica!"
            "{i}Meia hora depois, o bolo tem até o chamado 48213 com a Solução vazia. Embaixo, em glacê, [NOME_CO_DEV] escreve: \"Resolvido\".{/i}"
        "Ajudar a [NOME_CO_MENTORA] com a vaquinha para uma caneca nova.":
            $ add_friendship_point("co_mentora", 1)
            $ co_contribuicao_festa = "vaquinha"
            co_mentora "Vamos por partes: você passa nas mesas, eu desço para comprar. A loja do térreo grava nome em caneca."
            "{i}Em 40 minutos o andar inteiro contribui. A caneca nova é branca com uma faixa azul, igual à de 2008, só que sem lascas.{/i}"
        "Ajudar a [NOME_CO_QUALIDADE] a circular um cartão coletivo pela central.":
            $ add_friendship_point("co_qualidade", 1)
            $ co_contribuicao_festa = "cartao"
            co_qualidade "Você leva para a central, eu cuido do andar. Meta: 50 assinaturas. Registrado como prioridade alta."
            "{i}O cartão volta com 83 assinaturas. Alguém da central desenhou o servidor Tia Neide de chapéu de festa.{/i}"

    hide co_mentora
    hide co_dev
    hide co_qualidade
    with dissolve

    $ set_time(17, 30)
    scene bg escritorio_interior_festa
    with fade

    "{i}Bandeirinhas no teto, luz apagada, todo mundo escondido atrás das divisórias. Quando [NOME_CO_LEGADO] abre a porta, o andar inteiro grita parabéns.{/i}"
    show co_legado thinking at center_zoom
    with dissolve
    co_legado "Mas o que é isso? Alguém quebrou o fechamento de novo?"
    play sound "audio/effects/cell_vibration.ogg"
    "{i}O grupo da equipe vibra. É um áudio da [NOME_CO_SUPERVISORA]: a central inteira cantando parabéns, desafinada, com o barulho dos headsets ao fundo.{/i}"
    "{i}[NOME_CO_LEGADO] ri, tira os óculos de leitura e fica um tempo olhando para a caneca.{/i}"

    show co_legado serious at center_zoom
    co_legado "Entrei aqui em 1999, consertando planilha de folha de pagamento. Em 2008 me deram um sistema novo para cuidar. Achei que ia ficar dois anos."
    co_legado "Já que estão todos aqui, vou aproveitar. Eu me aposento em março."

    "{i}A sala fica em silêncio. Dá para ouvir o ar-condicionado.{/i}"
    show co_qualidade thinking at right_zoom
    with dissolve
    co_qualidade "E as rotinas noturnas do SGC? Metade delas não está em documento nenhum."
    show co_mentora serious at left_zoom
    with dissolve
    co_mentora "Na TI tem um nome feio para isso: fator ônibus. É uma pergunta simples. Se uma pessoa sair, o que vai embora junto com ela?"
    co_legado "Eu sei. Está tudo aqui na cabeça, e isso é um risco. Eu mesmo devia ter resolvido antes."

    menu:
        "Que homenagem você propõe?"
        "\"Um wiki 'Causos do SGC': o [NOME_CO_LEGADO] conta, a gente grava e registra.\"":
            $ add_friendship_point("co_legado", 1)
            $ co_homenagem_jorge = "wiki"
            if get_friendship_point("co_legado") >= 5:
                show co_legado neutral at center_zoom
                co_legado "Causos do SGC. Gostei do nome. Tem a greve de 2013, a Tia Neide, o comentário de 2010..."
                co_legado "Fechado. Primeira sessão na quarta, depois do almoço. Quem quiser ouvir leva café."
                co_qualidade "Eu levo o gravador e crio a página. Se não está registrado, não aconteceu."
                $ co_conceder("co_conq_memoria")
            else:
                co_legado "Ideia boa. Deixa eu pensar com calma. Hoje não é dia de prometer nada."
                co_mentora "A ideia fica anotada. Quando você quiser, a gente marca."
        "\"Um brinde ao [NOME_CO_LEGADO] e um agradecimento de toda a equipe.\"":
            $ add_friendship_point("co_legado", 1)
            $ co_homenagem_jorge = "brinde"
            "{i}Copos de refrigerante sobem. [NOME_CO_LEGADO] agradece com a voz um pouco embargada.{/i}"
            co_legado "Obrigado, pessoal. E até março eu prometo responder qualquer pergunta. Até as bobas."
            co_mentora "Vamos aproveitar essa promessa. Ainda precisamos pensar em como guardar o que você sabe."
        "\"E agora a Tia Neide se aposenta junto?\"":
            $ co_homenagem_jorge = "piada"
            "{i}A sala cai na risada. [NOME_CO_LEGADO] ri mais alto que todo mundo.{/i}"
            co_legado "A Tia Neide vai durar mais do que eu. Ela nem toma café."
            co_mentora "Ri, mas a pergunta é séria. Precisamos guardar o que vocês dois sabem."

    show co_dev neutral at right_zoom
    co_dev "Hora do bolo! E ninguém corta a parte da Solução vazia, que é patrimônio."
    $ advance_minutes(30)

    hide co_legado
    hide co_mentora
    hide co_dev
    hide co_qualidade
    with dissolve

    # Casa: toda a rota fica disponível para mensagens.
    $ set_available("all")
    $ set_time(21, 0)
    play music music_home_dreamy fadein 1.0
    scene bg quarto_noite
    with fade

    "{i}Em casa, você deixa a mochila na cadeira e pensa na sala em silêncio depois do anúncio.{/i}"
    "{i}O SGC tem 16 anos de código, mas também tem 16 anos de gente. A greve de 2013, o servidor com nome de tia, o comentário de sexta à noite.{/i}"
    "{i}Um sistema legado guarda as decisões de quem o manteve. Quando essas pessoas saem sem contar o porquê, a regra fica e o motivo some.{/i}"
    "Talvez valha mandar uma mensagem para alguém antes de dormir."

    call screen contacts_screen

    scene black
    with fade
    window hide
    pause 1.1
    window show

    "Fim da Semana 4\n\nAprendizado: sistema legado é também memória de gente. Registrar por que uma regra existe protege o sistema e quem vem depois."

    return
