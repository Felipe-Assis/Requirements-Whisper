# co_16_codificacao.rpy
# Semana 6 da rota Corporativo: testes de caracterização, mudança pequena e
# revisão de pull request. Bíblia: docs/rotas/corporativo.md, co_16.
# Decisões 17 (co_ok_abordagem) e 18 (co_ok_review).

label co_16_codificacao:
    $ set_available("co_mentora", "co_qualidade", "co_supervisora", "co_solicitante")
    $ set_time(9, 0)

    play music music_office_concentrated_1 fadein 1.0
    scene bg escritorio_interior_manha
    with fade

    "{i}Semana 6, segunda-feira, nove da manhã. O quadro da equipe ganhou uma coluna nova: Implementação.{/i}"
    "{i}No seu nome há um cartão só: \"Camada anticorrupção: resolver exige descrição. A rotina das 72 h grava a descrição padrão e registra 'sistema' na trilha.\"{/i}"

    show co_legado neutral at left_zoom
    show co_dev neutral at right_zoom
    with dissolve

    co_legado "Bom dia, [player_name]. Hoje você mexe no coração do fechamento. Sem pressão."
    co_legado "Mentira. Tem pressão, sim. Mas a gente divide."
    if energia_cansaco():
        co_legado "E você chegou com cara de quem não descansou no fim de semana. Café primeiro, código depois. Código com sono vira incidente."
    co_dev "Bora! A camada já recebe os chamados do SGC e traduz para o modelo do Farol. Falta a regra de verdade."
    co_dev "Você implementa a validação da descrição e a exceção da rotina das 72 h. Eu sigo na tela de consulta."

    "{i}Você abre o código. De um lado, o Farol, novo e com testes. Do outro, a ponte para o SGC e dezesseis anos de regras espalhadas.{/i}"

    show co_legado thinking at left_zoom
    with dissolve
    co_legado "Antes de digitar a primeira linha, me conta. Por onde você começa?"

    menu (tipo="trabalho"):
        "Como começar a mudança?"

        "Aproveitar e refatorar a tela de fechamento do SGC, que é confusa.":
            $ co_erro("co_ok_abordagem")
            show co_legado serious at left_zoom
            with dissolve
            co_legado "São 4 mil linhas sem teste. Você mudaria o escopo da RFC e o risco de regressão sem ninguém pedir."
            co_legado "A RFC que vai ao CAB fala da camada, não do JSF. Mexer na tela antiga seria outra mudança, com outro risco."

        "Escrever primeiro testes de caracterização do que o SGC faz hoje, inclusive a rotina das 72 h, e depois fazer a mudança pequena na camada.":
            $ co_acerto("co_ok_abordagem")
            show co_legado neutral at left_zoom
            with dissolve
            co_legado "Isso. Primeiro você fotografa o que o sistema faz, certo ou errado. Depois mexe."
            co_legado "Se alguma coisa mudar sem querer, o teste avisa antes da central."

        "Copiar a consulta SQL do relatório antigo para ganhar tempo.":
            $ co_erro("co_ok_abordagem")
            show co_dev serious at right_zoom
            with dissolve
            co_dev "Essa consulta varre a tabela inteira e tem o bug de fuso de 2014. Copiar é herdar os dois."
            co_dev "No pico das nove, com 140 atendentes lendo o mesmo Oracle, isso trava a tela de todo mundo."

    if not co_ok_abordagem:
        show co_legado thinking at left_zoom
        with dissolve
        co_legado "Vamos de novo, com calma. O que você precisa ter nas mãos antes de alterar?"
        menu (tipo="trabalho"):
            "Como você reformula?"

            "Testes que mostram o comportamento atual, inclusive a rotina das 72 h. Depois, a mudança pequena na camada.":
                show co_legado neutral at left_zoom
                with dissolve
                co_legado "Agora sim. Teste de caracterização registra o que o código faz hoje, mesmo que esteja errado."
                co_legado "O errado a gente corrige depois, com RFC. Hoje a gente só não quer surpresa."

    $ advance_minutes(90)
    hide co_legado
    show co_dev thinking at right_zoom
    with dissolve

    "{i}Você e [NOME_CO_DEV] fazem pair. Um escreve o teste, o outro lê em voz alta o que ele promete.{/i}"
    co_dev "Primeiro teste: chamado de Reset de senha, aberto há 72 h, sem retorno do solicitante. O SGC resolve sozinho e deixa a Solução vazia."
    co_dev "Passou. Acabamos de documentar o defeito mais famoso do prédio."
    co_dev "Segundo: a data de fechamento da rotina. Espera aí."

    play sound "audio/effects/teclado.ogg"
    "{i}O teste falha. Um chamado de Manaus foi aberto no horário local, mas a rotina grava o fechamento sempre no fuso de Brasília, uma hora à frente.{/i}"
    "{i}No relatório das filiais do Norte, os chamados de senha parecem levar 73 horas para fechar, e não 72.{/i}"

    co_dev "Olha isso. É o tal bug de fuso de 2014. Todo mundo desconfiava, ninguém tinha provado. Bora consertar?"

    # Pista do terceiro encontro da mentoria (formato 2): sem ela, a cena segue igual.
    if pista_tem("co_p_norte"):
        menu (tipo="conversa"):
            "Contar o causo do [NOME_CO_LEGADO]: a supervisora de Manaus reclamou disso em 2015" (tipo="pista"):
                $ pista_usar("co_p_norte")
                show co_legado neutral at left_zoom
                with dissolve
                co_legado "A hora do Norte. Em 2015 a gente riu, prometeu olhar e não registrou nada."
                co_legado "Desta vez registra com o causo junto: desde quando, quem reclamou, qual relatório. Aí o problema tem história e tem dono."
                $ add_friendship_point("co_legado", 0.5)
                hide co_legado
                with dissolve
            "Seguir com o [NOME_CO_DEV]":
                pass
    "{i}Você lembra do cartão no quadro. A mudança da RFC é a regra da descrição. O fuso não está lá.{/i}"
    co_dev "É, eu sei. Se eu mexer agora, o relatório do Norte muda e ninguém pediu. É chefão escondido no mapa: a gente marca e volta depois, com equipamento."
    "{i}Vocês ajustam o teste para registrar o comportamento atual, fuso fixo e tudo, e abrem um registro de problema para a próxima rodada.{/i}"
    co_dev "Se não está registrado, não aconteceu. Falei igual à [NOME_CO_QUALIDADE]. Não conta para ela."

    "{i}Com a rede pronta, a mudança cabe em poucas linhas: sem descrição, o chamado continua Em atendimento; na rotina das 72 h, entra o texto padrão e o autor \"sistema\".{/i}"

    # Quadro de rastreabilidade (docs/design/intermissoes-corporativo.md, seção 7.1).
    # A lacuna achada aqui decide como o bug aparece na co_17.
    show co_dev neutral at right_zoom
    co_dev "Antes do almoço, a [NOME_CO_QUALIDADE] pediu o quadro de rastreabilidade do que a gente mexeu. Vai anexo na RFC."
    co_dev "Cada critério liga num requisito e num teste. Se não liga, alguém pergunta no CAB."
    call rast_atividade("co_rast_farol") from _rast_co16
    if rast_lacuna_achada("co_rast_farol"):
        co_dev "Critério sem teste. Bem achado. Escrevo agora: atendente pela URL, acesso negado, tentativa na trilha."
        "{i}O teste novo entra na suíte. Ele falha, como devia: a verificação ainda está só na tela. O [NOME_CO_DEV] anota para corrigir no servidor.{/i}"
    else:
        co_dev "Quadro fechado. Mando para a [NOME_CO_QUALIDADE]."

    $ set_time(14, 0)
    scene bg escritorio_interior_tarde
    with dissolve

    show co_dev neutral at right_zoom
    with dissolve
    co_dev "Abri meu pull request da tela de consulta. Revisa para mim? Segundo olhar sempre acha alguma coisa."

    show expression "images/artifacts/co_farol_consulta.png" as tela_farol at artefato_tela
    with dissolve
    "{i}Na homologação, o Farol mostra o chamado 48213: linha do tempo, nome do atendente, caixa de solução registrada e o botão Reabrir chamado.{/i}"
    "{i}O título do pull request diz: \"Exibir estado e solução; desabilitar Resolver com descrição vazia.\" Todos os testes estão verdes.{/i}"
    hide tela_farol
    with dissolve

    menu (tipo="trabalho"):
        "Que comentário você faz no pull request?"

        "Aprovo: os testes passaram e o [NOME_CO_DEV] tem mais experiência.":
            $ co_erro("co_ok_review")
            play sound "audio/effects/cell_vibration.ogg"
            show co_mentora portrait at left_zoom
            with dissolve
            co_mentora "(mensagem) Vi a aprovação no canal da equipe. Revisão existe justamente para um segundo olhar. Os testes passaram porque nenhum chama a API."
            hide co_mentora
            with dissolve

        "Comento nomes de variáveis e formatação.":
            $ co_erro("co_ok_review")
            co_dev "Valeu, ajusto. Mas olha: passou batido que a API aceita descrição vazia vinda da integração."
            co_dev "A tela bloqueia, mas a integração do SGC passa direto."

        "A regra está só na tela. A API também precisa recusar descrição vazia, com um teste para isso.":
            $ co_acerto("co_ok_review")
            show co_dev thinking at right_zoom
            with dissolve
            co_dev "Pegou. Os testes passavam porque nenhum chamava a API direto."
            co_dev "Botão desabilitado é só a porta da frente. A integração entra pela porta dos fundos."

    if not co_ok_review:
        show co_dev thinking at right_zoom
        with dissolve
        co_dev "Deixa eu fazer a pergunta que a [NOME_CO_QUALIDADE] faria. Por onde mais um chamado pode ser resolvido, além da tela?"
        menu (tipo="trabalho"):
            "Como você reformula o comentário?"

            "Pela API da integração. A validação precisa estar no servidor, com um teste que chame a API com descrição vazia.":
                co_dev "Isso. Eu escrevi a regra onde eu via o botão. Erro meu, sem drama."

    "{i}[NOME_CO_DEV] escreve o teste novo. Ele falha, como devia. A regra vai para o servidor, e o teste passa.{/i}"
    co_dev "Anotado: validação só na tela não vale. A API tem que recusar também."

    $ advance_minutes(120)
    show co_legado neutral at left_zoom
    with dissolve
    co_legado "Sua vez de ouvir, [player_name]. Li seu pull request. Dois comentários."
    co_legado "Primeiro: o teste se chama teste_fechamento_2. Daqui a cinco anos, alguém vê esse nome falhar e não sabe o que quebrou."
    co_legado "Põe o comportamento no nome. Algo como: resolver sem descrição mantém Em atendimento."
    show co_legado thinking at left_zoom
    with dissolve
    co_legado "Segundo: descrição só com espaços. Esse caso eu conheço."
    co_legado "Em 2011 um atendente descobriu que três espaços passavam na validação do SGC. Virou moda na central."
    if "co_p_vazio" in pistas:
        "{i}Você lembra do fim de turno na central, na semana 2. Três espaços, e o SGC aceitou.{/i}"

    menu (tipo="conversa"):
        "Como você reage à revisão do [NOME_CO_LEGADO]?"

        "Agradecer e corrigir os dois pontos agora.":
            $ add_friendship_point("co_legado", 1)
            show co_legado neutral at left_zoom
            with dissolve
            co_legado "É assim. Revisão não é nota, é conversa. Me chama quando subir de novo."

        "Pedir pair ao [NOME_CO_DEV] para o caso dos espaços.":
            $ add_friendship_point("co_dev", 1)
            co_dev "Bora! Fico devendo uma depois da API. Você escreve o teste, eu tento quebrar."

        "\"Mas funciona.\"":
            show co_legado serious at left_zoom
            with dissolve
            co_legado "Funcionar hoje é o mínimo. O teste é para quem mexer aqui daqui a cinco anos."
            co_legado "Pode ser você. Pode ser alguém que nunca vai poder me ligar."

    play music music_office_relaxed fadein 1.5
    scene bg escritorio_interior_tarde
    with fade
    $ set_time(16, 30)

    "{i}Quarta-feira, fim da tarde. Os testes de caracterização rodam a cada commit. O fuso do Norte segue registrado como problema: sem pressa e sem esquecimento.{/i}"

    show expression "images/artifacts/co_farol_consulta.png" as tela_farol at artefato_tela
    with dissolve
    "{i}Na homologação, o chamado 48213 aparece como deveria: Resolvido, com atendente e solução. Um chamado de teste com três espaços na descrição é recusado e fica Em atendimento.{/i}"
    hide tela_farol
    with dissolve

    show co_legado neutral at left_zoom
    show co_dev neutral at right_zoom
    with dissolve
    co_dev "Funciona na homologação! Semana que vem é com a [NOME_CO_QUALIDADE]."
    if co_negociacao_opcao == "investigar_agora":
        co_dev "E à noite eu sigo com o WhatsApp. O provedor mandou o contrato, e o jurídico já está lendo."
    co_legado "Mudança pequena, rede grande. Em 2008 a gente fazia o contrário e chamava de coragem."
    co_legado "Chamava de coragem até a primeira sexta-feira à noite."

    hide co_legado
    hide co_dev
    with dissolve

    # Tempo livre da semana 6 (gancho B): sexta à tarde, antes do cartão.
    call im_intermissao(6) from _im_corporativo_s6

    scene black
    with fade
    window hide
    pause 1.0
    window show

    "Fim da Semana 6\n\nAprendizado: no legado, primeiro você prende uma rede, depois você mexe."

    return
