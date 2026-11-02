# co_05_entrevista.rpy
# Semana 2, quarta, 10h às 12h. Entrevista com Rosângela e Edson. Decisões 3, 4 e 5
# (co_ok_episodio, co_ok_ambiguidade, co_ok_conflito), registro co_reg_elicitacao,
# contatos dos stakeholders e conquista co_conq_escuta. Fonte: docs/rotas/corporativo.md, co_05.

label co_05_entrevista:
    $ set_available("co_legado", "co_dev", "co_qualidade")
    $ set_time(10, 0)

    play music music_office_relaxed fadein 1.0
    scene bg sala_reunioes_manha
    with fade

    "{i}Quarta-feira, 10h, na sala de reuniões. [NOME_CO_MENTORA] abre o caderno vinho. Você abre o notebook com o roteiro de segunda.{/i}"

    show co_mentora neutral at left_zoom
    with dissolve
    co_mentora "Lembra: você conduz, eu anoto. Se precisar, eu entro."

    show co_supervisora neutral at center_zoom
    with dissolve
    "{i}[NOME_CO_SUPERVISORA] chega primeiro, com o headset no pescoço e o relatório de SLA impresso e dobrado na mão.{/i}"
    co_supervisora "Bom dia. Tenho até meio-dia. Minha equipe está no pico e eu deixei a fila com o Paulo."
    co_mentora "SLA, [player_name], é o prazo combinado de atendimento. Na central, ele manda em tudo."

    show co_solicitante neutral at right_zoom
    with dissolve
    "{i}[NOME_CO_SOLICITANTE] entra logo depois, de colete refletivo e capacete debaixo do braço.{/i}"
    co_solicitante "Fala, pessoal! Desculpa o colete. Vim direto de uma subestação em Nova Iguaçu."

    co_mentora "[player_name] está no estágio do Projeto Farol e vai conduzir a conversa de hoje. Pode começar, [player_name]."
    "{i}Três pares de olhos se viram para você.{/i}"

    menu:
        "Como você abre a conversa?"

        "Pergunto se preferem um aplicativo ou uma página web.":
            $ co_erro("co_ok_episodio")
            show co_mentora thinking at left_zoom
            "{i}[NOME_CO_MENTORA] se inclina e fala baixo:{/i}"
            co_mentora "Isso já é solução. Ainda não sabemos o que precisa mudar para eles. Se a resposta for \"aplicativo\", a gente vai construir uma coisa sem saber para quê."

        "Peço que contem a última vez em que acompanhar um chamado deu errado.":
            $ co_acerto("co_ok_episodio")
            show co_mentora neutral at left_zoom
            "{i}[NOME_CO_MENTORA] faz um sinal discreto de aprovação.{/i}"
            co_mentora "Um episódio mostra quem sofre, o que acontece e quanto custa. Tudo de uma vez."

        "Pergunto se um aviso automático de chamado resolvido já ajudaria.":
            $ co_erro("co_ok_episodio")
            show co_mentora thinking at left_zoom
            "{i}[NOME_CO_MENTORA] se inclina e fala baixo:{/i}"
            co_mentora "A pergunta sugere a resposta. O [NOME_CO_SOLICITANTE] pode dizer sim por educação, e a gente nunca descobre o problema real."

    if not co_ok_episodio:
        co_mentora "Volta um passo. Peça uma história, não uma opinião."
        menu:
            "Como você reformula a abertura?"
            "[NOME_CO_SOLICITANTE], quando foi a última vez que você precisou saber de um chamado e não conseguiu?":
                show co_mentora neutral at left_zoom
                co_mentora "Isso. Agora é ele quem fala."

    show co_solicitante thinking at right_zoom
    co_solicitante "Semana passada. O notebook do Wellington, um técnico meu, ficou sem VPN. Sem VPN ele não baixa as ordens de serviço."
    co_solicitante "Liguei para a central de manhã. Disseram que estava com o grupo de rede. Liguei de tarde. Disseram que estava em análise."
    co_solicitante "Liguei no outro dia cedo. A terceira pessoa disse que tinha sido resolvido na véspera. Ninguém tinha escrito nada."
    co_solicitante "O Wellington ficou um dia inteiro parado na base, esperando. Um dia de campo perdido."
    show co_supervisora thinking at center_zoom
    "{i}[NOME_CO_SUPERVISORA] franze a testa e anota alguma coisa na margem do relatório.{/i}"

    $ advance_minutes(25)
    show co_solicitante neutral at right_zoom
    co_solicitante "Olha, eu não entendo de sistema. Eu só quero acompanhar fácil, sabe?"

    menu:
        "O que fazer com \"fácil\"?"

        "Registro \"o acompanhamento deve ser fácil\".":
            $ co_erro("co_ok_ambiguidade")
            show co_mentora thinking at left_zoom
            co_mentora "A equipe vai entender \"fácil\" de um jeito e o [NOME_CO_SOLICITANTE] de outro. E ninguém consegue testar isso."

        "Troco por \"intuitivo e moderno\".":
            $ co_erro("co_ok_ambiguidade")
            show co_mentora thinking at left_zoom
            co_mentora "Trocamos um adjetivo por dois. O resultado que ele espera continua sem nome."

        "Pergunto o que ele precisa conseguir fazer nessa situação.":
            $ co_acerto("co_ok_ambiguidade")
            show co_solicitante thinking at right_zoom
            co_solicitante "Conseguir fazer? Hum. Abrir o chamado pelo número e ver o estado, quem pegou e o que foi feito."
            co_solicitante "Se eu tivesse visto isso, não tinha ligado nenhuma vez."

    if not co_ok_ambiguidade:
        co_mentora "\"Fácil\" é o sentimento. A gente precisa da tarefa que está por trás dele."
        menu:
            "Como você pergunta de novo?"
            "O que precisava acontecer para você não ter ligado três vezes?":
                show co_solicitante thinking at right_zoom
                co_solicitante "Eu abrir o chamado pelo número e ver o estado, quem pegou e o que foi feito. Só isso."

    show co_mentora neutral at left_zoom
    co_mentora "Essa regra resolve uma parte. Se a tela é fácil de usar, a gente só descobre vendo pessoas usando. Fica para o teste com o protótipo."

    $ advance_minutes(20)
    show co_supervisora thinking at center_zoom
    co_supervisora "Posso falar? Se ver o que foi feito depende de o atendente escrever a solução, eu já sei onde isso vai parar."
    co_supervisora "Descrição obrigatória aumenta o TMA. Hoje minha equipe está em seis minutos e quarenta por chamado. Já está no limite."
    co_mentora "TMA é o tempo médio de atendimento de cada chamado."
    co_supervisora "O que eu preciso é de relatório de SLA confiável. Não de mais um campo para preencher."
    show co_solicitante neutral at right_zoom
    co_solicitante "Mas se ninguém escreve, eu ligo. E cada ligação minha também é tempo da sua equipe, [NOME_CO_SUPERVISORA]."
    co_supervisora "E cada minuto escrevendo é um minuto a menos atendendo a próxima ligação."
    "{i}Silêncio. Os dois olham para você.{/i}"

    menu:
        "[NOME_CO_SUPERVISORA] e [NOME_CO_SOLICITANTE] puxam para lados opostos. Como você conduz?"

        "Pergunto o que cada um quer evitar e busco um dado que os dois aceitem.":
            $ co_acerto("co_ok_conflito")
            co_supervisora "Evitar? Fila. E retrabalho, atendente respondendo a mesma coisa três vezes."
            co_solicitante "Eu quero evitar a ligação. E o dia perdido do meu técnico."

        "A [NOME_CO_SUPERVISORA] é a gestora do processo; ela decide.":
            $ co_erro("co_ok_conflito")
            show co_solicitante thinking at right_zoom
            "{i}[NOME_CO_SOLICITANTE] cruza os braços e se cala.{/i}"
            show co_mentora serious at left_zoom
            co_mentora "Aí a necessidade do [NOME_CO_SOLICITANTE] some do registro. As ligações continuam, e o projeto perde o motivo de existir."

        "Anoto os dois pedidos como estão e deixo a equipe decidir depois.":
            $ co_erro("co_ok_conflito")
            show co_mentora serious at left_zoom
            co_mentora "Aí uma regra contradiz a outra no documento, e quem decide é quem não conhece a central. Isso volta mais caro na inspeção."

    if not co_ok_conflito:
        show co_mentora neutral at left_zoom
        co_mentora "Os dois querem coisas diferentes, mas talvez temam a mesma. Pergunte isso."
        menu:
            "Como você retoma?"
            "O que cada um de vocês quer evitar?":
                show co_solicitante neutral at right_zoom
                co_supervisora "Fila. E retrabalho, atendente respondendo a mesma coisa três vezes."
                co_solicitante "Ligação. E o dia perdido do meu técnico."

    show co_supervisora thinking at center_zoom
    "{i}Você pergunta quantas ligações da central são de gente cobrando andamento. [NOME_CO_SUPERVISORA] folheia o relatório e corre o dedo por uma coluna.{/i}"
    co_supervisora "Cobrança de andamento... 18\%. Quase uma em cada cinco ligações."
    co_supervisora "Isso é fila. E é retrabalho. Eu nunca tinha olhado por esse lado."
    show co_solicitante neutral at right_zoom
    co_solicitante "Então se a pessoa vê o que foi feito, ela não liga. E sua fila diminui."
    show co_supervisora neutral at center_zoom
    co_supervisora "Eu aceito descrição obrigatória se for curta. E se tiver modelo pronto para os casos comuns: senha, VPN, notebook."
    co_solicitante "Fechado. Prefiro três linhas a nenhuma."
    show co_mentora neutral at left_zoom
    co_mentora "Anotado: descrição curta obrigatória, com modelos prontos. E o motivo: 18\% das ligações."

    $ advance_minutes(30)
    "{i}Com o clima mais leve, outros pedidos aparecem. Você anota cada um.{/i}"
    co_solicitante "Tem outra. Às vezes o chamado diz resolvido e o problema volta no dia seguinte. Eu quero poder reabrir."
    co_supervisora "E eu quero saber quem mudou o quê. Na auditoria interna de 2021, passei uma semana montando planilha para explicar chamado fechado."
    co_supervisora "Atendente não pode ver o mesmo que supervisor. E admin é outra coisa."
    co_supervisora "E a consulta tem que aguentar as nove da manhã. É quando todo mundo liga ao mesmo tempo."
    show co_solicitante thinking at right_zoom
    co_solicitante "Ah, e se der: aviso pelo WhatsApp. Técnico de campo não abre intranet. Abre o celular."
    co_mentora "Tudo anotado. Uma coisa importante: o SGC continua sendo o sistema de registro. O Farol mostra o que está nele, não substitui."

    $ set_time(11, 50)
    co_supervisora "Bom. Meio-dia eu preciso estar na fila."
    show co_solicitante neutral at right_zoom
    co_solicitante "E eu na estrada. Foi a primeira vez que alguém da TI me perguntou o que aconteceu, em vez do que eu quero."

    menu:
        "Como você se despede?"

        "Agradeço à [NOME_CO_SUPERVISORA] pelo dado e peço para observar a central de novo.":
            $ add_friendship_point("co_supervisora", 1)
            show co_supervisora neutral at center_zoom
            co_supervisora "Pode vir. Senta do lado da Neusa de novo, ela gostou de você. Só não marca nada às nove."

        "Peço ao [NOME_CO_SOLICITANTE] que teste o protótipo com a equipe de campo.":
            $ add_friendship_point("co_solicitante", 1)
            show co_solicitante neutral at right_zoom
            co_solicitante "Opa! Manda que eu testo. Prefiro testar do que imaginar. O Wellington vai ser o primeiro."

        "Agradeço aos dois juntos e encerro.":
            co_supervisora "Obrigada pelo tempo."
            co_solicitante "Valeu, pessoal."

    "{i}Antes de sair, os dois passam o contato.{/i}"
    $ add_contact("co_supervisora")
    $ add_contact("co_solicitante")

    hide co_supervisora
    hide co_solicitante
    with dissolve

    show co_mentora neutral at left_zoom
    co_mentora "Um episódio, uma palavra vaga trocada por tarefa e um conflito que virou acordo com um número. Bela manhã."
    co_mentora "Passa tudo para o notebook enquanto está fresco."

    $ co_registrar("co_reg_elicitacao")
    $ co_conceder("co_conq_escuta")

    $ set_time(12, 0)
    hide co_mentora
    with dissolve

    return
