# co_13_arquitetura.rpy
# Semana 4, terça. Arquitetura de transição (decisão 13), trilha de auditoria
# (decisão 14), menu social com Kauã e negociação do pedido do WhatsApp.
# Fonte: docs/rotas/corporativo.md, seção co_13.

label co_13_arquitetura:
    # Manhã: equipe na sala; Edson ainda não chegou.
    $ set_available("co_supervisora", "co_solicitante")
    $ set_time(9, 0)

    play music music_office_concentrated_2 fadein 1.0
    scene bg sala_reunioes_manha
    with fade

    "{i}Semana 4, terça-feira. No quadro da sala de reuniões, alguém escreveu em letras grandes: ARQUITETURA DO FAROL.{/i}"
    "{i}[NOME_CO_DEV] já está de pé ao lado da tela, com o notebook cheio de adesivos aberto e a cara de quem dormiu pouco.{/i}"

    show co_dev neutral at right_zoom
    with dissolve
    co_dev "Bora! Fiz uma proposta no fim de semana. Um microsserviço para cada parte: chamados, perfis, histórico, notificações."
    co_dev "A gente reescreve o SGC inteiro, liga tudo num sábado e aposenta o Java 6 de vez. Código limpo e teste desde o primeiro dia."

    show co_legado thinking at left_zoom
    with dissolve
    co_legado "Isso aí tem história, [NOME_CO_DEV]. Deixa eu contar o que está pendurado no SGC hoje."
    co_legado "São 14 relatórios. Um deles vai para a diretoria todo dia primeiro. Tem a rotina das 72 h, que fecha uns 300 chamados de senha por semana."
    co_legado "E tem a integração com o RH, que bloqueia o acesso de quem sai da empresa. Essa ninguém lembra até o dia em que ela para."
    $ advance_minutes(20)

    show co_mentora neutral at center_zoom
    with dissolve
    co_mentora "Vamos por partes. Ninguém aqui discorda de que o SGC precisa mudar. A pergunta é como mudar sem parar a central."
    co_mentora "[player_name], você ouviu os dois. Qual estratégia faz sentido para o Farol?"

    menu (tipo="trabalho"):
        "Qual estratégia para o Farol?"
        "Construir o Farol dentro do SGC, acrescentando telas no JSF antigo.":
            $ co_erro("co_ok_arquitetura")
            hide co_mentora
            show co_qualidade serious at center_zoom
            with dissolve
            co_qualidade "Sem testes automatizados, cada tela nova mexe em código que ninguém entende inteiro."
            co_qualidade "E cada ajuste vira RFC no coração do sistema. A gente passaria as oito semanas na fila do CAB."
            hide co_qualidade
            show co_mentora neutral at center_zoom
            with dissolve
        "Construir o Farol ao lado do SGC, atrás de uma camada que traduz os dados, e assumir uma função por vez.":
            $ co_acerto("co_ok_arquitetura")
            show co_legado neutral at left_zoom
            co_legado "A figueira mata-pau. Agora tem nome técnico: estrangulamento."
            co_mentora "O sistema novo cresce em volta do velho e assume uma função de cada vez. Se uma parte der errado, o resto continua de pé."
        "Reescrever tudo em microsserviços e desligar o SGC num grande dia de virada.":
            $ co_erro("co_ok_arquitetura")
            show co_legado serious at left_zoom
            co_legado "São 16 anos de regra, 14 relatórios e a rotina das 72 h. Num único dia de virada, qualquer esquecimento para a central inteira."
            co_legado "E oito semanas não dão nem para listar tudo. A reescrita de 2016 morreu assim, depois de 14 meses."

    if not co_ok_arquitetura:
        co_mentora "Vamos olhar por outro lado. A central atende 1.300 chamados por dia e não pode parar nem um sábado inteiro. Como trocar uma parte sem parar o resto?"
        menu (tipo="trabalho"):
            "Como você reformula?"
            "Uma parte por vez, ao lado do sistema velho, com um tradutor no meio.":
                show co_legado neutral at left_zoom
                co_legado "Isso. Lembra da figueira mata-pau? Agora tem nome técnico: estrangulamento."
                co_mentora "O Farol cresce ao lado do SGC e assume uma função por vez. Se algo falhar, a central continua no sistema de sempre."

    show co_dev thinking at right_zoom
    co_dev "Tá, e esse tradutor no meio?"
    co_mentora "É a camada anticorrupção. Ela conversa com o SGC na língua dele e entrega para o Farol os dados já arrumados."
    co_dev "Nome de série policial. Mas entendi: o Farol nem precisa saber que o SGC chama \"Em atendimento\" de código 3."
    $ advance_minutes(25)

    hide co_legado
    hide co_mentora
    hide co_dev
    with dissolve
    show expression "images/artifacts/co_farol_arquitetura.png" as co_diagrama at artefato_tela
    with dissolve
    "{i}[NOME_CO_MENTORA] projeta o diagrama. À esquerda, o SGC com o JSF e o Oracle. No meio, a camada anticorrupção e a API de chamados. À direita, o módulo Farol.{/i}"
    "{i}Uma seta tracejada leva ao aviso por WhatsApp, o desejo do [NOME_CO_SOLICITANTE] que ficou registrado sem data. Embaixo, uma tabela nova: historico_chamado.{/i}"
    hide co_diagrama
    with dissolve

    show co_qualidade thinking at left_zoom
    with dissolve
    co_qualidade "Agora os dados. O chamado vem do SGC e, no Farol, é só leitura. Ninguém escreve nele por fora."
    co_qualidade "Depois vêm solicitante, atendente, perfil e usuario_perfil, que liga cada pessoa aos perfis dela. E a tabela nova de histórico."
    co_qualidade "A [NOME_CO_SUPERVISORA] quer saber quem mudou o quê em cada chamado. A auditoria interna também. Como a gente guarda isso?"

    menu (tipo="trabalho"):
        "Como guardar quem mudou o quê no chamado?"
        "Gravar num arquivo de log no servidor.":
            $ co_erro("co_ok_auditoria")
            show co_legado serious at right_zoom
            with dissolve
            co_legado "Arquivo de log gira e some. Não dá para consultar por chamado, e qualquer administrador edita."
            co_legado "Em 2017 a gente perdeu três meses de log numa troca de disco. Ninguém percebeu até a auditoria pedir."
        "Uma coluna \"última alteração\" na tabela de chamados.":
            $ co_erro("co_ok_auditoria")
            co_qualidade "Guarda só a última. Se o chamado mudou cinco vezes, perdemos quatro."
            co_qualidade "E a tabela é do SGC. Mexer nela precisaria de RFC, que é justamente o que combinamos evitar."
        "Uma tabela de histórico só de inclusão: quem, perfil, quando, ação, valor anterior e novo; ninguém altera nem apaga.":
            $ co_acerto("co_ok_auditoria")
            co_qualidade "Isso. Cada mudança vira uma linha nova. Se alguém errar, corrige com outra linha, e as duas ficam lá."
            co_qualidade "Registro que dá para apagar não serve para auditoria."

    if not co_ok_auditoria:
        co_qualidade "Pensa na [NOME_CO_SUPERVISORA] sentada com a auditoria interna, como em 2021. O que ela precisaria mostrar?"
        menu (tipo="trabalho"):
            "Como você reformula?"
            "Cada mudança, com autor e horário, sem possibilidade de edição.":
                co_qualidade "Então é uma tabela de histórico só de inclusão: quem, perfil, quando, ação, valor anterior e novo."
                co_qualidade "Ninguém altera, ninguém apaga. Erro se corrige com uma linha nova."

    co_qualidade "A rotina das 72 h também grava ali, com o usuário \"sistema\". Do jeito que a [NOME_CO_SUPERVISORA] decidiu na inspeção."
    $ advance_minutes(40)

    hide co_qualidade
    hide co_legado
    with dissolve
    "{i}A reunião termina. Todo mundo recolhe as canecas, menos [NOME_CO_DEV], que fica olhando o slide dos microsserviços.{/i}"
    show co_dev serious at right_zoom
    show co_legado neutral at left_zoom
    with dissolve
    co_dev "Passei o domingo desenhando aquilo. Eu entendi o motivo, de verdade. Mas dá uma pena."

    menu (tipo="conversa"):
        "O que você diz?"
        "\"Sua ideia de serviços pode ser o destino. O estrangulamento é o caminho até lá.\"":
            $ add_friendship_point("co_dev", 1)
            show co_dev neutral at right_zoom
            co_dev "Destino e caminho. Gostei. Então eu guardo o desenho para daqui a uns anos."
            co_dev "E faço a primeira parte direito, para o resto ter onde se apoiar."
        "\"[NOME_CO_LEGADO], valeu por mostrar as dependências antes de a gente começar.\"":
            $ add_friendship_point("co_legado", 1)
            co_legado "Alguém tinha que estragar a festa. Melhor hoje do que num sábado às 3h da manhã."
            co_legado "E, [NOME_CO_DEV], seu desenho não foi à toa. Metade daquelas caixas vai existir um dia."
        "Deixar o assunto morrer e voltar para a mesa.":
            co_dev "Tá. Bora almoçar, que eu tô com fome de microsserviço."

    hide co_dev
    hide co_legado
    with dissolve

    # Tarde: Edson e Kauã com o jogador; o resto da equipe fora.
    $ set_available("co_mentora", "co_legado", "co_qualidade", "co_supervisora")
    $ set_time(14, 30)
    scene bg escritorio_interior_tarde
    with fade

    "{i}À tarde, você ajuda [NOME_CO_DEV] a passar o diagrama a limpo quando um colete refletivo aparece no corredor.{/i}"
    show co_solicitante neutral at left_zoom
    with dissolve
    co_solicitante "Fala! Vim entregar um relatório na diretoria e aproveitei para passar aqui."
    co_solicitante "Vou direto: dá para colocar o aviso por WhatsApp na primeira entrega? Meu técnico não abre a intranet. Abre o celular."

    show co_dev thinking at right_zoom
    with dissolve
    co_dev "Dá para fazer, [NOME_CO_SOLICITANTE], mas não é só um botão."
    co_dev "Precisa de contrato com um provedor oficial da API. Precisa de parecer do jurídico, porque é telefone pessoal do funcionário, dado pessoal na LGPD. E precisa de teste de segurança."
    co_dev "Se entrar agora, a consulta e o bloqueio da descrição vazia atrasam. Não cabe tudo em oito semanas."
    show co_solicitante thinking at left_zoom
    co_solicitante "Entendi o tamanho. Mas meu problema continua lá na Baixada."
    "{i}Os dois olham para você. De manhã, [NOME_CO_MENTORA] pediu que você conduzisse essa conversa se ela aparecesse: mostrar o impacto, combinar a prioridade e registrar o acordo.{/i}"
    $ co_negociacao_sem_atalho = True

label .negociar:
    menu (tipo="negociacao"):
        "Como você conduz o pedido do WhatsApp?"
        "Incluir o WhatsApp e manter o prazo sem falar de capacidade.":
            $ co_negociacao_sem_atalho = False
            co_dev "Eu teria de cortar o bloqueio da descrição vazia. Não sobra semana para os dois."
            co_solicitante "Aí eu recebo aviso de um chamado que diz \"Resolvido\" sem dizer nada. Isso eu já tenho hoje."
            "{i}Prometer tudo no mesmo prazo só esconde o corte. Vale tentar outro caminho.{/i}"
            jump .negociar
        "Entregar consulta e bloqueio primeiro; investigar o WhatsApp na próxima rodada, sem data.":
            $ co_negociacao_opcao = "base_primeiro"
            $ co_negociacao_acordo = __("Entregar primeiro a consulta e o bloqueio sem descrição para todos. {solicitante} e {dev} investigam o aviso por WhatsApp na próxima rodada, antes de estimar uma data.").format(solicitante=NOME_CO_SOLICITANTE, dev=NOME_CO_DEV)
            co_solicitante "Então primeiro eu vejo o que fizeram no chamado. O aviso vem depois, quando souberem o tamanho."
            co_dev "E sem data inventada. A gente investiga junto e só depois estima."
        "Recusar porque o escopo já foi escrito.":
            $ co_negociacao_sem_atalho = False
            co_solicitante "Meu técnico continua sem abrir a intranet."
            co_dev "O registro pode mudar. A gente precisa é mostrar o efeito de cada escolha."
            "{i}Escopo escrito não é muro. O pedido merece uma resposta com o impacto, não um não seco.{/i}"
            jump .negociar
        "Investigar o WhatsApp agora e renegociar a data de liberação.":
            $ co_negociacao_opcao = "investigar_agora"
            $ co_negociacao_acordo = __("{dev} investiga agora o aviso por WhatsApp. Na janela da semana 8, o Farol entra para a central e para o piloto da equipe de {solicitante}; a liberação para todos fica para a janela seguinte, preservando a consulta e o bloqueio.").format(solicitante=NOME_CO_SOLICITANTE, dev=NOME_CO_DEV)
            co_solicitante "Piloto com a minha equipe? Melhor ainda. A gente testa na rua, não na imaginação."
            co_dev "E a consulta e o bloqueio continuam no plano. Só a liberação para todos espera uma janela."

    "{i}Você escreve o acordo no quadro e lê em voz alta:{/i}"
    "\"[co_negociacao_acordo]\""

    menu (tipo="negociacao"):
        "O texto diz o que os dois combinaram?"
        "Rever o acordo":
            jump .negociar
        "Confirmar com os dois":
            $ co_negociacao_completa = True
            show co_solicitante neutral at left_zoom
            co_solicitante "Fechado. Pela primeira vez alguém me explica o porquê em vez de só dizer não."
            show co_dev neutral at right_zoom
            co_dev "Vou colar esse texto na página do Farol no wiki. A [NOME_CO_QUALIDADE] vai gostar: está registrado."
            $ co_conceder("co_conq_acordo")

    $ advance_minutes(90)
    hide co_solicitante
    hide co_dev
    with dissolve

    "{i}Perto das 17h, você abre o notebook e resume o dia: o Farol cresce ao lado do SGC, atrás de um tradutor, e assume uma função por vez.{/i}"
    "{i}A trilha é uma tabela só de inclusão. E pedido novo no meio do caminho se trata assim: mostrar o impacto, combinar a prioridade e registrar o acordo.{/i}"
    $ co_registrar("co_reg_transicao")
    $ co_conceder("co_conq_transicao")
    $ set_time(17, 0)

    return
