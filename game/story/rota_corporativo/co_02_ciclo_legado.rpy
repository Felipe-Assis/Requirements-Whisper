# co_02_ciclo_legado.rpy
# Rota Corporativo, semana 1, segunda, 14h às 17h30.
# Fonte: docs/rotas/corporativo.md, cena co_02. Decisão 1 (co_ok_manutencao),
# registro co_reg_manutencao. Sem variáveis novas.

label co_02_ciclo_legado:
    $ set_available()
    $ set_time(14, 0)

    play music music_office_concentrated_1 fadein 1.5
    scene bg sala_reunioes_tarde
    with fade

    "{i}Depois do almoço, a equipe ocupa a sala de reuniões. [NOME_CO_MENTORA] destampa uma caneta e vai até o quadro branco.{/i}"

    show co_mentora neutral at left_zoom
    with dissolve
    co_mentora "Na faculdade, o ciclo de vida costuma começar do zero: levantar, especificar, projetar, codificar, testar, implantar."
    co_mentora "Aqui o sistema já existe e atende a empresa inteira todo dia. Então o ciclo muda um pouco. Vamos por partes."
    "{i}Ela escreve no quadro, uma etapa embaixo da outra:{/i}"
    "1. Entender o que já existe\n2. Levantar o que precisa mudar\n3. Especificar\n4. Projetar a transição"
    "5. Implementar com testes de regressão\n6. Mudar com aprovação\n7. Operar e aprender"
    co_mentora "Teste de regressão confere que o que já funcionava continua funcionando depois da mudança."
    $ advance_minutes(20)

    co_mentora "Manutenção também tem tipos. Corretiva conserta defeito. Adaptativa acompanha uma mudança de ambiente, como uma versão nova do banco de dados."
    co_mentora "Evolutiva acrescenta ou melhora uma função. Preventiva reduz um risco antes que ele vire defeito."
    co_mentora "E o Farol, [player_name]? Em qual delas você acha que ele entra?"
    "{i}Você pensa no chamado 48213. Ninguém está consertando um defeito do SGC. O Farol acrescenta uma coisa que não existia: acompanhar o chamado.{/i}"
    "\"Evolutiva\", você responde."
    co_mentora "Isso. O SGC continua fazendo o que faz. A gente acrescenta uma função ao lado dele."
    $ advance_minutes(15)

    show co_qualidade neutral at right_zoom
    with dissolve
    co_qualidade "Minha parte. A gente usa um pedaço do ITIL, um conjunto de boas práticas para operar serviços de TI. Só o pedaço útil."
    co_qualidade "Incidente: algo parou e precisa voltar a funcionar. Problema: a causa de um ou mais incidentes."
    co_qualidade "Mudança: qualquer alteração planejada em produção. Começa numa RFC, o pedido de mudança: o que muda, impacto, janela, testes, plano de volta e responsáveis."
    co_qualidade "A RFC vai para o CAB, que se reúne às quintas. Aprovada, a mudança entra numa janela, um horário combinado. A nossa é sábado, da meia-noite às quatro."
    co_qualidade "Deu errado? Rollback: volta ao estado anterior. Em lista parece chato. Na madrugada de sábado, é o que deixa todo mundo dormir no domingo."
    $ advance_minutes(20)

    hide co_qualidade
    show co_dev neutral at right_zoom
    with dissolve
    co_dev "Posso ser sincero? Tanto processo pra mexer num sistema de 2008... Era mais fácil reescrever tudo em microsserviços. Começa limpo, sem herança."

    hide co_dev
    show co_legado serious at right_zoom
    with dissolve
    co_legado "Isso aí tem história, [NOME_CO_DEV]. Em 2016 a diretoria aprovou uma reescrita. Equipe nova, tecnologia nova, apresentação bonita."
    co_legado "Catorze meses depois, cancelaram. Toda semana alguém descobria uma regra do SGC que não estava em documento nenhum."
    co_legado "Sobrou uma pasta na rede chamada SGC2_NAO_USAR. Está lá até hoje, de luto."
    co_dev "Tá, mas aquela equipe não tinha a gente."
    co_legado "Eles também diziam isso."

    show co_qualidade thinking at center_zoom
    with dissolve
    co_mentora "[player_name], o Farol vai depender do fechamento de chamados do SGC. O que você faria primeiro?"
    $ advance_minutes(10)

    menu:
        "Antes de mexer no SGC, qual é o primeiro passo?"

        "Reescrever o SGC do zero numa tecnologia nova, para não herdar problemas.":
            $ co_erro("co_ok_manutencao")
            co_legado "A gente herdaria o pior problema: não saber o que o velho fazia. Tem regra lá dentro que nenhum documento cita."
            co_legado "Foi isso que matou a reescrita de 2016."

        "Entender o que o sistema faz hoje e combinar testes de regressão para o que o Farol vai tocar.":
            $ co_acerto("co_ok_manutencao")
            co_mentora "Mudar sem saber o que existe é apostar. Primeiro a gente conhece, depois a gente protege, aí sim a gente muda."
            co_mentora "E a regressão avisa se algo que funcionava parou. Sem ela, quem avisa é a central, às nove da manhã, com a fila cheia."

        "Alterar direto a tela de fechamento; é uma mudança pequena.":
            $ co_erro("co_ok_manutencao")
            co_qualidade "Em 2019 uma mudança pequena no fechamento quebrou o relatório mensal da diretoria."
            co_qualidade "Pequena no código não quer dizer pequena no efeito."

    if not co_ok_manutencao:
        co_mentora "Tudo bem, é para isso que a gente conversa. O que precisamos saber antes de mudar qualquer coisa?"
        menu:
            "Como você reformula?"

            "Primeiro descobrir o que o sistema faz hoje e como vamos perceber se algo parar de funcionar.":
                co_mentora "Isso. Conhecer o comportamento atual e ter testes que avisam se ele quebrar. Aí a mudança deixa de ser aposta."

    co_dev "Tá bom, tá bom. Primeiro explora o mapa, depois entra na fase nova."
    co_legado "Viu? Já está aprendendo, [NOME_CO_DEV]."
    $ advance_minutes(45)

    "{i}A reunião chega ao fim. Enquanto a equipe recolhe as canecas, você aproveita para fazer uma última pergunta.{/i}"

    menu:
        "No fim da reunião, você pergunta..."

        "Ao [NOME_CO_LEGADO]: \"Como vocês descobrem o que o SGC faz sem documentação?\"":
            $ add_friendship_point("co_legado", 1)
            show co_legado thinking at right_zoom
            co_legado "Três jeitos. Olho os dados, leio o código e pergunto para quem usa. Quando os três discordam, tem coisa escondida."
            co_legado "E tem o quarto jeito: a memória deste senhor aqui. É o menos confiável. Pergunte à minha esposa, [player_name]."

        "À [NOME_CO_QUALIDADE]: \"Qual mudança já deu mais errado aqui?\"":
            $ add_friendship_point("co_qualidade", 1)
            show co_qualidade serious at center_zoom
            co_qualidade "Uma sexta-feira de 2019. Três linhas no fechamento subiram sem passar pelo CAB. Na segunda, o relatório mensal da diretoria saiu zerado."
            co_qualidade "Ninguém foi demitido. A gente perguntou o que no processo deixou aquilo passar, não quem errou. Dali veio a regra: nada sobe sem RFC."
            co_qualidade "Foi ali que ganhei a fama de chata do CAB. Fama registrada e aceita."

        "À [NOME_CO_MENTORA]: \"Posso acompanhar você nas conversas com a central?\"":
            $ add_friendship_point("co_mentora", 1)
            co_mentora "Pode e deve. Eu comecei atendendo telefone lá, em 2004. Quem usa o sistema sabe coisas que nenhum documento sabe."
            co_mentora "Logo a gente senta uma manhã ao lado de uma atendente. Leva o caderno."

    $ advance_minutes(10)
    show co_legado neutral at right_zoom
    co_legado "Antes de vocês irem embora: alguém quer conhecer a Tia Neide?"
    co_dev "Ah, não. Lá vem."
    hide co_mentora
    hide co_qualidade
    hide co_legado
    with dissolve

    scene bg sala_servidores
    with fade
    $ advance_minutes(30)

    "{i}A sala de servidores é gelada e barulhenta. Racks pretos piscam em azul e verde até o fim do corredor.{/i}"
    "{i}No canto, destoando de tudo, um rack bege com uma etiqueta de papel amarelada.{/i}"

    show co_legado neutral at center_zoom
    with dissolve
    co_legado "Pessoal, a Tia Neide. Rodou o SGC sozinha por anos. Hoje guarda uma réplica do banco, só para consulta."
    co_legado "Tentaram desligar uma vez, em 2015. Choveu dentro do prédio naquela noite. Coincidência, claro."

    show co_dev serious at right_zoom
    with dissolve
    co_dev "Ele conta isso pra todo estagiário. Faz parte do onboarding."

    show co_mentora neutral at left_zoom
    with dissolve
    co_mentora "[player_name], antes que a gente esqueça: anota o ciclo de hoje no notebook. Os tipos de manutenção e o caminho de uma mudança."
    "{i}Você apoia o notebook na mesa dobrável do canto e escreve enquanto os ventiladores zumbem.{/i}"
    $ co_registrar("co_reg_manutencao")

    hide co_dev
    show co_qualidade neutral at right_zoom
    with dissolve
    co_qualidade "Se não está registrado, não aconteceu. Agora aconteceu."

    $ advance_minutes(60)
    hide co_mentora
    hide co_legado
    hide co_qualidade
    with dissolve
    "{i}Às cinco e meia, a equipe deixa a sala gelada. Você sai com as mãos frias e a cabeça cheia de siglas que, pela primeira vez, fazem sentido.{/i}"

    return
