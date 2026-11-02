# co_09_historias.rpy
# Semana 3, segunda, 9h às 17h. História de usuário, casos de uso, critério
# (decisão 8, co_ok_criterio) e caso limite (decisão 9, co_ok_caso_limite);
# registro co_reg_criterio. Fonte: docs/rotas/corporativo.md, co_09.

label co_09_historias:
    $ set_available("co_legado", "co_qualidade", "co_supervisora", "co_solicitante")
    $ set_time(9, 0)

    play music music_office_concentrated_1 fadein 1.0
    scene bg escritorio_interior_manha
    with fade

    "{i}Segunda-feira, semana 3. O ar-condicionado do andar continua no modo inverno. Você chega com o notebook aberto nas anotações da entrevista.{/i}"
    "{i}[NOME_CO_MENTORA] já está na mesa redonda perto da janela, com o caderno vinho e duas canetas de cores diferentes.{/i}"

    show co_mentora neutral at left_zoom
    with dissolve
    co_mentora "Bom dia, [player_name]. Hoje a gente transforma conversa em especificação. Vamos por partes."
    co_mentora "Lembra do episódio do [NOME_CO_SOLICITANTE]? O notebook do Wellington sem VPN, três ligações e um dia de campo perdido."

    show expression "images/artifacts/co_sgc_legado.png" as tela_sgc at artefato_tela
    with dissolve
    co_mentora "E lembra deste aqui. Chamado 48213: Resolvido, campo Solução em branco. Para quem abriu, é como se nada tivesse acontecido."
    hide tela_sgc
    with dissolve

    co_mentora "Uma história de usuário diz quem precisa, o que precisa e para quê. Monta comigo."
    "{i}Vocês escrevem no quadro, riscam e reescrevem até a ideia caber numa frase só:{/i}"
    "\"Como solicitante, quero consultar o estado e a solução registrada do meu chamado, para não precisar ligar para a central.\""
    co_mentora "Repara no \"para\". Ele guarda o motivo. Se a tela ficar bonita e as ligações continuarem, a gente errou."

    $ advance_minutes(40)
    show co_dev neutral at right_zoom
    with dissolve
    co_dev "Bom dia! Cheguei na parte boa? Ouvi falar em história. Tô dentro."
    co_mentora "Chegou na hora dos casos de uso. Puxa uma cadeira, [NOME_CO_DEV]."

    "{i}[NOME_CO_MENTORA] lista os casos de uso do Farol. Ao lado de cada um, o ator que faz a ação:{/i}"
    "UC01 Consultar chamado (solicitante)\nUC02 Registrar solução e resolver (atendente)\nUC03 Reabrir chamado (solicitante)"
    "UC04 Consultar trilha de auditoria (supervisor)\nUC05 Gerenciar perfis (admin)"

    show co_dev thinking at right_zoom
    co_dev "Olha só: os atores já são os perfis. Solicitante, atendente, supervisor, admin. Metade do controle de acesso saiu daqui."
    co_mentora "Exatamente. Agora as exceções do UC01. O que pode dar errado quando alguém consulta?"
    co_dev "O SGC cair. Ele cai toda madrugada de domingo. Tradição da casa."
    co_mentora "Então a consulta mostra o último estado sincronizado, com data e hora. A pessoa sabe que a informação pode estar atrasada."
    co_dev "E se alguém digitar o número do chamado de outra pessoa?"
    co_mentora "Acesso negado. Chamado tem nome, telefone, endereço de subestação. Proteger isso também é requisito."

    $ advance_minutes(45)
    show co_mentora thinking at left_zoom
    co_mentora "Agora a parte que mais importa. Como a gente sabe que essa história ficou pronta? [player_name], qual critério você escreveria?"

    menu:
        "Qual critério verifica a história?"
        "A pessoa solicitante deve receber atendimento de qualidade.":
            $ co_erro("co_ok_criterio")
            co_mentora "É um objetivo importante, mas não diz o que observar no sistema. Quem testa ia olhar para onde? Cada pessoa aprovaria por um motivo diferente."
        "O atendente deve conseguir clicar no botão Resolver.":
            $ co_erro("co_ok_criterio")
            co_mentora "Conseguir clicar não garante o que o [NOME_CO_SOLICITANTE] vai ver do outro lado. No 48213, alguém também clicou em Resolver."
        "Dado um chamado Em atendimento, quando o suporte registra a solução e muda para Resolvido, a consulta do solicitante mostra Resolvido e o texto registrado.":
            $ co_acerto("co_ok_criterio")
            show co_mentora neutral at left_zoom
            co_mentora "Isso. Tem situação inicial, ação e um resultado que qualquer pessoa confere na tela. Dá para aprovar ou reprovar sem discussão."

    if not co_ok_criterio:
        co_mentora "Um critério precisa de três coisas: de onde partimos, o que acontece e o que alguém consegue conferir."
        menu:
            "O que falta para verificar?"
            "Registrar a situação inicial, a ação e o resultado que o solicitante confere.":
                show co_mentora neutral at left_zoom
                co_mentora "Isso. Dado um chamado Em atendimento, quando o suporte registra a solução e muda para Resolvido, a consulta mostra Resolvido e o texto registrado."
                co_mentora "Agora qualquer pessoa da equipe testa do mesmo jeito. Você chegou lá."

    show co_dev thinking at right_zoom
    co_dev "Pera. E se o atendente tentar resolver sem escrever nada? Fim de turno, fila cheia, ele só quer fechar."
    co_mentora "Boa, [NOME_CO_DEV]. Isso é um caso limite. [player_name], o que você propõe?"

    menu:
        "E se o atendente tentar resolver sem descrever a solução?"
        "Preencho automaticamente com 'Resolvido', para não atrasar o atendimento.":
            $ co_erro("co_ok_caso_limite")
            co_mentora "Repetir o estado não explica nada. O [NOME_CO_SOLICITANTE] abriria a consulta e leria \"Resolvido: Resolvido\". É o chamado 48213 de novo, com outra roupa."
        "Proponho manter Em atendimento e orientar o preenchimento, e confirmo com a [NOME_CO_SUPERVISORA].":
            $ co_acerto("co_ok_caso_limite")
            show co_mentora neutral at left_zoom
            co_mentora "Isso. O chamado não muda de estado com a solução vazia, a tela diz o que falta, e quem decide a regra da central é a [NOME_CO_SUPERVISORA]."
        "Mudo o estado e o atendente explica depois por telefone.":
            $ co_erro("co_ok_caso_limite")
            co_mentora "Aí voltam as ligações que o [NOME_CO_SOLICITANTE] quer evitar. E a explicação por telefone não fica registrada em lugar nenhum."

    if not co_ok_caso_limite:
        co_mentora "Pensa no que o [NOME_CO_SOLICITANTE] veria na consulta em cada caso. E em quem é dona do processo da central."
        menu:
            "Como registrar o caso e confirmar?"
            "Descrição vazia mantém Em atendimento e mostra uma orientação; confirmar com a dona da regra.":
                show co_mentora neutral at left_zoom
                co_mentora "Isso. O caso fica escrito, o comportamento fica claro, e a [NOME_CO_SUPERVISORA] confirma porque é a equipe dela que vai preencher."

    show co_mentora serious at left_zoom
    co_mentora "Só uma ressalva. A rotina das 72 h fecha chamados de senha sem descrição nenhuma. Esse caso limite briga com ela."
    co_mentora "Vou anotar para a inspeção de quinta. Não resolve hoje, mas também não some."
    show co_mentora neutral at left_zoom
    co_mentora "Guarda no notebook a história, o critério e o caso limite. Esse trio vai voltar muitas vezes."
    $ co_registrar("co_reg_criterio")

    hide co_mentora
    hide co_dev
    with dissolve

    scene bg escritorio_interior_tarde
    with fade
    $ set_time(14, 30)

    "{i}Depois do almoço, [NOME_CO_DEV] puxa uma cadeira para perto da sua mesa, com o notebook cheio de adesivos.{/i}"
    show co_dev neutral at right_zoom
    with dissolve
    co_dev "Lembra do protótipo que eu te mostrei no primeiro dia? Mexi nele no fim de semana. Não conta pro [NOME_CO_LEGADO] que eu trabalhei no domingo."

    show expression "images/artifacts/co_farol_consulta.png" as tela_farol at artefato_tela
    with dissolve
    "{i}Na tela, um cartão limpo com o chamado 48213: linha do tempo, nome do atendente, uma caixa \"Solução registrada\" e um botão \"Reabrir chamado\".{/i}"
    co_dev "Linha do tempo, quem pegou, o que foi feito. Bem diferente do cinza de 2008, né?"

    show co_mentora neutral at left_zoom
    with dissolve
    co_mentora "Ficou bonito, [NOME_CO_DEV]. Manda um print para o [NOME_CO_SOLICITANTE] ainda hoje. Ele prefere testar a imaginar."
    co_mentora "Só lembra: protótipo serve para conversar. Ele mostra a ideia e ajuda a achar o que falta. Não vai para produção."
    hide tela_farol
    with dissolve

    show co_dev thinking at right_zoom
    co_dev "Entendi, entendi. Mas então... já posso começar a codar?"

    menu:
        "\"Posso começar a codar?\", pergunta [NOME_CO_DEV]."
        "Ainda não. Me ajuda a revisar os critérios? Assim você coda uma vez só.":
            $ add_friendship_point("co_dev", 1)
            show co_dev neutral at right_zoom
            co_dev "Justo. Codar duas vezes é pior que esperar dois dias. Bora revisar."
            "{i}Vocês passam uma hora lendo cada critério em voz alta. [NOME_CO_DEV] acha duas frases que ele mesmo teria implementado de jeitos diferentes.{/i}"
        "Vamos perguntar à [NOME_CO_MENTORA] o que falta.":
            $ add_friendship_point("co_mentora", 1)
            co_mentora "Falta a inspeção. Na quinta, a [NOME_CO_QUALIDADE] conduz: a gente lê cada requisito procurando o que falta, o que tem duas leituras e o que briga com outra regra."
            co_mentora "O conflito com a rotina das 72 h vai estar na pauta. Melhor achar o problema no papel do que no código."
            co_dev "Faz sentido. Até quinta, então, eu só brinco no protótipo."
        "Manda ver.":
            show co_dev neutral at right_zoom
            co_dev "Bora!"
            show co_mentora serious at left_zoom
            co_mentora "Calma, vocês dois. Protótipo, pode mexer à vontade. Código de produção, só depois da inspeção de quinta."
            co_mentora "Se a regra mudar lá, ninguém precisa jogar trabalho fora."

    $ set_time(17, 0)
    hide co_mentora
    hide co_dev
    with dissolve
    "{i}No fim do dia, o quadro está cheio: uma história, cinco casos de uso, um critério e uma pergunta sublinhada duas vezes sobre a rotina das 72 h.{/i}"

    return
