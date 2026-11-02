# co_06_avaliacao.rpy
# Semana 2, quinta, 14h às 18h. Classificação dos requisitos em quatro colunas.
# Decisões 6 e 7 (co_ok_class_nf, co_ok_class_restricao) e registro
# co_reg_classificacao. Fonte: docs/rotas/corporativo.md, co_06.

label co_06_avaliacao:
    $ set_available("co_legado", "co_dev", "co_supervisora", "co_solicitante")
    $ set_time(14, 0)

    play music music_office_focused fadein 1.0
    scene bg escritorio_interior_tarde
    with fade

    "{i}Quinta-feira à tarde. [NOME_CO_MENTORA] lê no monitor o resumo da entrevista que você escreveu ontem à noite.{/i}"

    show co_mentora thinking at left_zoom
    with dissolve
    co_mentora "Vamos por partes. Quero comentar o que você fez na quarta, não só o que a gente ouviu."

    if co_ok_episodio:
        co_mentora "Você começou pelo episódio. Foi isso que trouxe o Wellington e o dia perdido para a mesa."
    else:
        co_mentora "Com apoio, você chegou ao episódio. Da próxima vez, comece por ele: a história do Wellington valeu mais que qualquer opinião."

    if co_ok_ambiguidade:
        co_mentora "Quando apareceu o \"fácil\", você perguntou pela tarefa. O [NOME_CO_SOLICITANTE] mesmo disse o que precisava ver."
    else:
        co_mentora "No \"fácil\", você precisou de uma segunda pergunta. Tudo bem. O importante é que a tarefa ficou escrita."

    if co_ok_conflito:
        co_mentora "E no conflito você foi atrás do que os dois queriam evitar. O 18\% saiu dali."
    else:
        co_mentora "No conflito, com apoio, você chegou ao que os dois queriam evitar. Guarde isso: dado que os dois aceitam desarma a briga."

    show co_qualidade neutral at right_zoom
    with dissolve
    "{i}[NOME_CO_QUALIDADE] puxa uma cadeira, tablet na mão.{/i}"
    co_qualidade "Se não está registrado, não aconteceu. E se está registrado sem tipo, vai acontecer errado. Vamos separar?"
    "{i}Ela desenha quatro colunas no quadro: Funcional, Não funcional, Restrição, Desejo.{/i}"
    co_qualidade "Primeiro exemplo, de graça: \"a consulta mostra estado, atendente e solução\". Isso é o que o sistema faz. Funcional."

    $ advance_minutes(30)
    show co_qualidade thinking at right_zoom
    co_qualidade "Agora você. Este aqui veio da [NOME_CO_SUPERVISORA]."
    "\"A consulta do chamado deve responder em até 3 s para 95\% dos acessos, com 1.500 usuários simultâneos no pico das 9h.\""

    menu (tipo="trabalho"):
        "Que tipo de requisito é esse?"

        "Funcional: fala da consulta do chamado.":
            $ co_erro("co_ok_class_nf")
            show co_qualidade serious at right_zoom
            co_qualidade "A consulta é funcional. Este trecho fala de quão rápido ela responde e sob qual carga."
            co_qualidade "Se entrar como funcional, ninguém planeja teste de carga. Aí a gente descobre o problema às nove da manhã, em produção."

        "Desejo: seria bom, mas não é necessário.":
            $ co_erro("co_ok_class_nf")
            show co_qualidade serious at right_zoom
            co_qualidade "No pico das 9h, se a consulta pesar no Oracle, a tela do atendente trava junto. São 140 pessoas paradas. Isso não é enfeite."

        "Não funcional: define desempenho, com número, carga e momento.":
            $ co_acerto("co_ok_class_nf")
            show co_qualidade neutral at right_zoom
            co_qualidade "Isso. Fala de como o sistema se comporta, e tem número. Dá para medir e dá para reprovar."

    if not co_ok_class_nf:
        co_qualidade "Pergunta que eu faço sempre: descreve uma ação ou um jeito de se comportar?"
        menu (tipo="trabalho"):
            "Esse item descreve o que o sistema faz ou como ele deve se comportar?"
            "Como ele deve se comportar: é não funcional.":
                show co_qualidade neutral at right_zoom
                co_qualidade "Pronto. Vai para a coluna dois, com teste de carga marcado."

    $ advance_minutes(25)
    show co_qualidade thinking at right_zoom
    co_qualidade "Próximo. Este é meu, confesso."
    "\"O Farol não pode alterar tabelas do SGC sem aprovação do CAB; os dados continuam no Oracle.\""

    menu (tipo="trabalho"):
        "Que tipo de requisito é esse?"

        "Restrição: limita a solução e vem do ambiente e da gestão de mudanças.":
            $ co_acerto("co_ok_class_restricao")
            show co_qualidade neutral at right_zoom
            co_qualidade "Exato. Ninguém usa isso na tela. É uma cerca em volta de como a gente pode construir."

        "Requisito funcional do Farol.":
            $ co_erro("co_ok_class_restricao")
            show co_qualidade serious at right_zoom
            co_qualidade "Não descreve nada que o usuário faz. Limita como a gente pode construir. Funcional sem usuário é sinal de coluna errada."

        "Desejo da equipe de qualidade.":
            $ co_erro("co_ok_class_restricao")
            show co_qualidade serious at right_zoom
            co_qualidade "Se for desejo, alguém altera a tabela \"só um pouquinho\" numa sexta. E a rotina das 72 h para de funcionar sem ninguém perceber."

    if not co_ok_class_restricao:
        co_qualidade "Pensa em quem mandou e no que isso impede."
        menu (tipo="trabalho"):
            "Quem impôs essa regra e o que ela limita?"
            "O ambiente e o CAB; limita a solução, então é restrição.":
                show co_qualidade neutral at right_zoom
                co_qualidade "Isso. Coluna três."

    $ advance_minutes(20)
    show co_qualidade thinking at right_zoom
    co_qualidade "Agora uma joia que apareceu no grupo da equipe: \"tema escuro com mascote\"."
    co_qualidade "Ninguém na entrevista pediu isso. Não resolve ligação nem fila. Coluna quatro: desejo. Fica fora do problema."
    show co_mentora neutral at left_zoom
    co_mentora "E o aviso pelo WhatsApp do [NOME_CO_SOLICITANTE]? Tem necessidade real por trás, mas ainda não sabemos custo nem regra."
    co_qualidade "Desejo também. Registrado, sem data. Desejo não é lixo, é fila de espera."

    co_qualidade "O motivo das colunas: cada tipo se verifica de um jeito. Funcional, com teste de função. Não funcional, com teste de carga."
    co_qualidade "Restrição, com revisão de arquitetura. Desejo, com conversa com quem pediu."
    co_qualidade "E olha, ninguém acerta tudo de primeira. Uma vez eu classifiquei \"relatório em PDF\" como restrição. Passei vergonha no CAB."

    menu (tipo="conversa"):
        "Como você responde?"

        "Quero entender onde acertei e onde errei.":
            $ add_friendship_point("co_qualidade", 1)
            show co_qualidade neutral at right_zoom
            co_qualidade "Gostei. Senta aqui que eu mostro coluna por coluna. Erro registrado é erro que não se repete."

        "[NOME_CO_MENTORA], você lembra do seu primeiro requisito ruim?":
            $ add_friendship_point("co_mentora", 1)
            show co_mentora thinking at left_zoom
            co_mentora "Lembro. 2009, meu primeiro mês na TI. Escrevi: \"o sistema deve ser ágil\"."
            co_mentora "O desenvolvedor me perguntou: ágil quanto? Eu não sabia. Guardo esse papel até hoje."

        "Classificação parece burocracia.":
            show co_qualidade thinking at right_zoom
            co_qualidade "Parece. Mas lembra do 3 s no pico? Na coluna errada, ninguém marca teste de carga. Cada coluna vira um tipo de teste."

    $ co_registrar("co_reg_classificacao")

    $ set_time(18, 0)
    scene bg escritorio_interior_noite
    with fade
    "{i}Às seis, o quadro está cheio e o documento está organizado. Quatro colunas, cada item com um jeito de ser conferido.{/i}"
    "{i}Lá fora, as luzes da cidade acendem. Pela primeira vez, o pedido de [NOME_CO_SOLICITANTE] e o de [NOME_CO_SUPERVISORA] cabem no mesmo papel.{/i}"

    return
