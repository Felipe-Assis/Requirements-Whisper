# co_11_inspecao.rpy
# Semana 3, quinta, 14h às 18h30. Inspeção (decisões 10 a 12), conflito com a
# rotina das 72 h decidido pela Rosângela, escrita livre (co_reabrir) e
# conquista co_conq_inspetor. Fonte: docs/rotas/corporativo.md, co_11.

label co_11_inspecao:
    $ set_available("co_legado", "co_dev", "co_supervisora", "co_solicitante")
    $ set_time(14, 0)

    play music music_office_focused_2 fadein 1.0
    scene bg escritorio_interior_tarde
    with fade

    "{i}Quinta-feira, duas da tarde. A mesa do canto virou sala de inspeção: o documento de requisitos projetado na parede, três cópias impressas e um pacote de biscoito aberto.{/i}"

    show co_qualidade neutral at right_zoom
    with dissolve
    co_qualidade "Boas-vindas à parte que todo mundo diz que é chata. E que mais economiza retrabalho."
    show co_mentora neutral at left_zoom
    with dissolve
    co_mentora "A [NOME_CO_QUALIDADE] conduz. Eu observo e dou palpite quando ela deixar."

    show co_qualidade thinking at right_zoom
    co_qualidade "Checklist curto. Para cada requisito, cinco perguntas:"
    "Falta alguma coisa?\nTem duas leituras?\nBriga com outra regra?"
    "É estranho ao contexto?\nDá para testar?"
    co_qualidade "[player_name], começa você. Primeiro item."

    "\"RF-05: O solicitante pode reabrir um chamado resolvido.\""

    menu:
        "O que você aponta no RF-05?"
        "Faltam as condições: quem pode reabrir, até quando, se o motivo é obrigatório e o que acontece com a solução anterior.":
            $ co_acerto("co_ok_insp_ausente")
            show co_qualidade neutral at right_zoom
            co_qualidade "Isso. Informação ausente. A frase parece completa porque é curta, mas deixa quatro perguntas sem resposta."
        "Está completo; o desenvolvedor decide os detalhes.":
            $ co_erro("co_ok_insp_ausente")
            co_qualidade "O [NOME_CO_DEV] escolheria 30 dias. A [NOME_CO_SUPERVISORA] espera 7. A diferença só aparece no teste de aceitação, com a tela pronta e a central olhando."
        "O problema é o verbo: troque 'pode' por 'deve'.":
            $ co_erro("co_ok_insp_ausente")
            co_qualidade "Obrigar alguém a reabrir não faz sentido. E trocar o verbo não preenche a lacuna: continua sem prazo, sem motivo e sem regra para a solução anterior."

    if not co_ok_insp_ausente:
        co_mentora "Lê de novo como se você fosse testar amanhã. O que você precisaria perguntar antes?"
        menu:
            "Que perguntas o requisito não responde?"
            "Quem, até quando, com qual motivo e o que acontece com a solução anterior.":
                show co_qualidade neutral at right_zoom
                co_qualidade "Isso. Cada pergunta sem resposta vira uma decisão tomada às pressas por quem está codando. Agora fica anotada."

    $ advance_minutes(25)
    co_qualidade "Próximo."
    "\"RNF-01: A consulta do chamado deve ser rápida mesmo nos horários de pico.\""

    menu:
        "O que fazer com o RNF-01?"
        "Trocar por 'deve ser muito rápida e eficiente'.":
            $ co_erro("co_ok_insp_ambiguo")
            co_qualidade "Continua sem número. Como alguém reprova esse teste? Para o [NOME_CO_DEV], dez segundos é rápido. Para o atendente com cliente na linha, não é."
        "Tirar o requisito; desempenho é problema da infraestrutura.":
            $ co_erro("co_ok_insp_ambiguo")
            co_qualidade "O Farol lê o mesmo Oracle da central. Sem requisito, ninguém testa carga, e no pico das nove a tela do atendente trava junto."
        "Definir tempo, percentual, carga e onde medir, como fizemos na classificação.":
            $ co_acerto("co_ok_insp_ambiguo")
            show co_qualidade neutral at right_zoom
            co_qualidade "Isso. 3 s para 95\% das consultas, com 1.500 usuários, no pico das 9h. Agora o teste de carga tem uma meta."

    if not co_ok_insp_ambiguo:
        co_mentora "Procura as palavras que cada pessoa leria de um jeito."
        menu:
            "Quais palavras têm mais de uma leitura?"
            "'Rápida' e 'pico': substituir por 3 s, 95\%, 1.500 usuários, 9h.":
                show co_qualidade neutral at right_zoom
                co_qualidade "Isso. Ambiguidade se resolve com número que a [NOME_CO_SUPERVISORA] e o [NOME_CO_DEV] leem igual."

    $ advance_minutes(25)
    show co_qualidade serious at right_zoom
    co_qualidade "Agora o que a [NOME_CO_MENTORA] anotou na segunda. Dois itens lado a lado."
    "\"RF-03: O sistema deve impedir que um chamado seja resolvido sem descrição.\""
    "\"RN-07 (herdada do SGC): chamados de Reset de senha são resolvidos automaticamente após 72 h sem retorno.\""

    menu:
        "O que fazer com RF-03 e RN-07?"
        "Apagar a RN-07; é regra velha do legado.":
            $ co_erro("co_ok_insp_inconsistente")
            co_qualidade "Ela fecha uns 300 chamados de senha por semana. Sem ela, a fila da central volta a crescer. Regra velha tem motivo: essa nasceu de uma greve."
        "Apontar o conflito e levar a decisão à [NOME_CO_SUPERVISORA], dona da regra, com uma proposta.":
            $ co_acerto("co_ok_insp_inconsistente")
            show co_qualidade neutral at right_zoom
            co_qualidade "Isso. Inconsistência não se resolve na mesa da equipe. Leva para quem é dona do processo, já com uma sugestão."
        "Manter as duas; o código decide qual roda primeiro.":
            $ co_erro("co_ok_insp_inconsistente")
            co_qualidade "Aí o comportamento depende da ordem de execução. Um teste aprova, outro reprova, e ninguém sabe qual está certo."

    if not co_ok_insp_inconsistente:
        co_mentora "As duas regras têm motivo. A pergunta é quem tem autoridade para escolher."
        menu:
            "Quem pode decidir qual regra vale?"
            "Quem é dona do processo: a [NOME_CO_SUPERVISORA].":
                show co_qualidade neutral at right_zoom
                co_qualidade "Isso. A gente mostra o conflito e uma proposta. Quem decide é quem responde pela central."

    co_mentora "Proposta: a rotina continua, mas grava uma descrição padrão e registra a ação na trilha. Manda para ela, [player_name]."
    "{i}Você escreve para [NOME_CO_SUPERVISORA] com o conflito, a proposta e o motivo. A resposta chega antes do biscoito acabar.{/i}"

    hide co_mentora
    hide co_qualidade
    play sound "audio/effects/cell_vibration.ogg"
    show co_supervisora portrait at left_zoom
    with dissolve
    co_supervisora "(mensagem) A rotina fica. Sem ela minha fila de senha explode. Mas quero a frase \"Encerrado automaticamente após 72 h sem retorno do solicitante\" no campo Solução."
    co_supervisora "(mensagem) E na trilha aparece \"sistema\" como autor. Na auditoria, ninguém da minha equipe responde por fechamento que não fez."
    hide co_supervisora
    with dissolve

    show co_mentora neutral at left_zoom
    show co_qualidade neutral at right_zoom
    with dissolve
    co_qualidade "Registrado. RF-03 ganha uma exceção com dona, motivo e data. Agora as duas regras falam a mesma língua."

    $ advance_minutes(30)
    show co_qualidade thinking at right_zoom
    co_qualidade "Último, e esse é bônus. Apareceu no documento ontem à noite:"
    "\"RF-12: O Farol deve ter um chatbot com avatar 3D para receber o solicitante.\""
    co_qualidade "Autor: [NOME_CO_DEV]. Comentário dele: \"brincadeira, mas e se?\". Estranho ao contexto, sem necessidade de ninguém. Cortado."
    co_mentora "Ele vai reclamar no café."
    co_qualidade "Vou registrar a reclamação. Prioridade baixa."

    $ advance_minutes(20)
    show co_mentora neutral at left_zoom
    co_mentora "Agora uma escrita sua. O [NOME_CO_SOLICITANTE] pediu para reabrir chamado quando a solução não funciona. Escreve o requisito e um critério de aceitação."
    co_mentora "Depois você mesmo revisa com quatro perguntas: quem age, sob quais condições, que resultado dá para observar e que caso deve ser recusado."
    "O jogo não corrige o texto. Ele guarda o que você escrever e a sua autoavaliação."

    hide co_mentora
    hide co_qualidade
    with dissolve

    call exercicio_escrita("co_reabrir", _("A pessoa solicitante precisa reabrir um chamado resolvido quando a solução falhar. Ela deve informar o motivo; o chamado volta a Em atendimento e preserva a solução anterior no histórico."))
    $ co_sincronizar_escrita()

    show co_mentora neutral at left_zoom
    show co_qualidade neutral at right_zoom
    with dissolve
    if co_escrita_status == "rascunho":
        co_mentora "Rascunho guardado. Na próxima semana a gente lê junto com o [NOME_CO_SOLICITANTE] e vê se ele entende o mesmo que você."
    else:
        co_mentora "Ficou pendente, e tudo bem. Pendência registrada é melhor que texto apressado. Dá para retomar depois."

    $ co_registrar("co_reg_inspecao")

    scene bg escritorio_interior_noite
    with fade
    $ set_time(18, 15)
    show co_mentora neutral at left_zoom
    show co_qualidade neutral at right_zoom
    with dissolve
    "{i}Lá fora, a cidade já acendeu as luzes. O documento tem marcas em quase toda página.{/i}"
    co_qualidade "Quatro horas, três defeitos, uma regra resolvida com a dona e um avatar 3D a menos. Dia produtivo."

    menu:
        "Como você reage à inspeção?"
        "Agradeço o olhar crítico. Achei coisa que eu não veria por conta própria.":
            $ add_friendship_point("co_qualidade", 1)
            co_qualidade "É isso. Inspeção não é caça ao erro de alguém. É o documento sendo lido por mais olhos antes de virar código."
        "Sinto insegurança com tanto detalhe. Será que um dia acerto tudo?":
            $ add_friendship_point("co_mentora", 1)
            show co_mentora serious at left_zoom
            co_mentora "Ninguém revisa sozinho. Por isso a gente inspeciona junto. Eu escrevi \"o sistema deve ser ágil\" em 2009 e ninguém me demitiu."
        "Acho cansativo, mas entendo o motivo.":
            co_qualidade "Chato hoje, barato amanhã. Defeito achado no papel custa uma conversa. No código, custa uma RFC."

    $ co_conceder("co_conq_inspetor")

    $ set_time(18, 30)
    hide co_mentora
    hide co_qualidade
    with dissolve
    "{i}Você salva o documento revisado e fecha o notebook. Pela primeira vez, o requisito parece um acordo, não um palpite.{/i}"

    return
