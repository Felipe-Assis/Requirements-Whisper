# co_15_gestao.rpy
# Semana 5. Calendário de mudanças, retomada do acordo da co_13, planejamento
# com capacidade (2 de 4), RFC para o CAB (decisão 15) e risco da carga do
# histórico (decisão 16). Resumo do ensaio de quarta e da sexta.
# Fonte: docs/rotas/corporativo.md, seção co_15.

label co_15_gestao:
    $ set_available("co_supervisora", "co_solicitante")
    $ set_time(9, 0)

    play music music_office_focused fadein 1.0
    scene bg sala_reunioes_manha
    with fade

    "{i}Semana 5, segunda-feira. [NOME_CO_MENTORA] abre a reunião com o calendário de mudanças projetado na parede.{/i}"

    show co_mentora neutral at center_zoom
    with dissolve
    co_mentora "Vamos por partes. A janela reservada para nós é no sábado da semana 8, das 0h às 4h."
    co_mentora "O CAB se reúne às quintas. Nossa RFC precisa entrar até a quinta da semana 7. Se perder, só na janela seguinte."
    show co_qualidade serious at right_zoom
    with dissolve
    co_qualidade "Uma semana para código, uma para testes e CAB, e a janela logo depois. Quem quiser mudar de ideia, muda hoje."

    if co_negociacao_opcao == "investigar_agora":
        show co_dev thinking at left_zoom
        with dissolve
        co_mentora "Antes, o acordo da semana passada. [NOME_CO_DEV], como foi a investigação do WhatsApp?"
        co_dev "Achei os dois muros: o contrato com o provedor oficial e o parecer do jurídico sobre telefone pessoal. O jurídico pediu 20 dias."
        co_mentora "Então seguimos o combinado. Na janela da semana 8 entram a central e o piloto da equipe do [NOME_CO_SOLICITANTE]. A liberação para todos fica para a janela seguinte."
    else:
        show co_dev neutral at left_zoom
        with dissolve
        co_mentora "Antes, o acordo da semana passada: consulta e bloqueio primeiro, para todos. O WhatsApp fica para a próxima rodada, sem data."
        co_dev "O [NOME_CO_SOLICITANTE] já me perguntou quando a gente começa a investigar. Respondi: depois da janela. Ele mandou um joinha."
    $ advance_minutes(20)

    co_mentora "Agora a capacidade. A camada, a trilha e a reabertura de chamado já estão em andamento. Até a janela, cabem só mais dois itens grandes, e temos quatro candidatos."
    co_mentora "[player_name], monta o plano. Depois a gente confere junto."

    call atividade_planejamento("co_plano", [_("Consulta do solicitante com estado, atendente e solução"), _("Bloquear resolução sem descrição, com a exceção registrada da rotina das 72 h"), _("Tema de cores personalizável no painel da supervisão"), _("Relatório mensal de chamados em PDF")], [0, 1], capacidade=2)
    $ co_plano_cobertura = _return
    $ co_plano_selecionados = list(planejamentos["co_plano"]["selecionados"])
    $ co_plano_completo = True

    if co_plano_cobertura == 2:
        co_mentora "Consulta e bloqueio. O [NOME_CO_SOLICITANTE] diria que é exatamente o que faltou no dia do Wellington."
        co_mentora "E a [NOME_CO_SUPERVISORA] diria que o bloqueio, com a exceção das 72 h registrada, é o que ela aprovou na inspeção."
        co_qualidade "Tema de cores e relatório em PDF vão para o backlog, registrados. Ninguém perde a ideia, só a vaga."
    else:
        if co_plano_cobertura == 1 and 0 in co_plano_selecionados:
            co_mentora "A consulta entrou, mas o bloqueio ficou de fora. A [NOME_CO_SUPERVISORA] diria que, sem ele, o [NOME_CO_SOLICITANTE] consulta e encontra \"Resolvido\" com a Solução vazia, igual a hoje."
        elif co_plano_cobertura == 1:
            co_mentora "O bloqueio entrou, mas a consulta ficou de fora. O [NOME_CO_SOLICITANTE] diria que a solução fica bem escrita num lugar que ele não consegue ver. Ele continuaria ligando para a central."
        else:
            co_mentora "Nenhum dos dois necessários entrou. O tema de cores ninguém pediu. E o SGC já emite um relatório mensal parecido. O [NOME_CO_SOLICITANTE] e a [NOME_CO_SUPERVISORA] continuariam com o mesmo problema de antes."
        co_mentora "O comitê de produto fechou o recorte com a consulta e o bloqueio, que vieram da entrevista. A gente segue com os dois, e o seu plano fica anotado para a conversa de revisão."
    $ advance_minutes(25)

    show co_qualidade thinking at right_zoom
    co_qualidade "Próximo ponto: o CAB. [player_name], como você levaria a implantação até lá?"

    menu (tipo="trabalho"):
        "Como levar a implantação ao CAB?"
        "Registrar uma RFC normal: o que muda, impacto, janela de sábado, testes de regressão, plano de rollback e responsáveis.":
            $ co_acerto("co_ok_cab")
            co_qualidade "Isso. RFC normal, com tudo o que o comitê precisa para decidir sem adivinhar."
            co_qualidade "Plano de rollback é a primeira coisa que eu leio. Se não tem, devolvo antes do CAB. Nada pessoal."
        "Pedir como mudança emergencial, para não esperar a reunião de quinta.":
            $ co_erro("co_ok_cab")
            show co_qualidade serious at right_zoom
            co_qualidade "Emergencial é para restaurar serviço parado. Usar para furar fila faz o CAB desconfiar de todo pedido nosso."
            co_qualidade "Depois de 2019, toda RFC da equipe passou seis meses sendo revisada duas vezes. Não quero repetir."
        "Implantar numa terça às 15h e avisar por e-mail; é um módulo novo.":
            $ co_erro("co_ok_cab")
            show co_qualidade serious at right_zoom
            co_qualidade "O Farol lê o mesmo Oracle da central, no meio do expediente, sem plano de volta combinado."
            co_qualidade "Se travar, 140 atendentes param. E um e-mail não pergunta a ninguém se pode."

    if not co_ok_cab:
        co_mentora "Imagina você do outro lado da mesa, no CAB. O que precisa saber para aprovar uma mudança?"
        menu (tipo="trabalho"):
            "Como você reformula?"
            "O que muda, o impacto, quando, como testamos e como voltamos.":
                show co_qualidade neutral at right_zoom
                co_qualidade "Então é uma RFC normal, com a janela de sábado, os testes de regressão, o plano de rollback e quem responde por cada passo."
                co_qualidade "Te mando o modelo. É menos chato do que parece."

    "{i}Você abre o notebook na página sobre mudança controlada: RFC, CAB, janela, plano de volta, revisão depois. Pela primeira vez, a lista vira tarefa de verdade.{/i}"
    $ advance_minutes(20)

    hide co_dev
    show co_legado serious at left_zoom
    with dissolve
    co_legado "Agora o que me tira o sono: a carga do histórico. São 200 mil descrições do SGC indo para a tabela nova."
    co_legado "Tem texto de 2008, tem gente que colou do Word, tem campo com 4 mil caracteres. Isso aí tem história, e nem toda é bonita."

    # Pista do segundo encontro da mentoria (semanas 3 e 4). Fora da contagem.
    call pista_lembrar("co_p_acentos") from _pl_co15_risco

    menu (tipo="trabalho"):
        "Como tratar o risco da carga do histórico?"
        "Deixar o [NOME_CO_LEGADO] de sobreaviso; ele resolve se der problema.":
            $ co_erro("co_ok_risco")
            co_legado "Em março eu não estarei aqui. Risco com plano é risco gerenciado."
            co_legado "Risco comigo de sobreaviso é sorte. E sorte não entra em RFC."
        "Ensaiar a carga numa cópia de produção, definir um critério de parada e testar o script de reversão.":
            $ co_acerto("co_ok_risco")
            show co_legado neutral at left_zoom
            co_legado "Isso. Com dados de verdade, não com os 50 chamados bonitinhos que o [NOME_CO_DEV] escreveu ontem."
            co_qualidade "E o critério de parada combinado antes. Ninguém decide nada às 2h da manhã."
        "Rodar a carga direto na janela; o script funcionou com 50 chamados de teste.":
            $ co_erro("co_ok_risco")
            co_legado "Os 50 de teste foram escritos ontem. Os de 2008 têm acento de outro padrão, texto colado do Word e campo com 4 mil caracteres."
            co_legado "O script passa no teste e quebra na janela, com a central esperando."

    if not co_ok_risco:
        co_mentora "Como descobrir o problema antes da janela, e não durante?"
        menu (tipo="trabalho"):
            "Como você reformula?"
            "Ensaiar com dados reais e combinar quando parar e como voltar.":
                show co_legado neutral at left_zoom
                co_legado "Isso. Ensaio numa cópia de produção, critério de parada combinado e script de reversão testado."
                co_qualidade "Fica como risco na RFC, com o ensaio como resposta."

    co_qualidade "Então tem ensaio na quarta à noite, numa cópia de produção. Quem fica comigo?"
    if energia_cansaco():
        co_qualidade "E você, pensa bem antes de ficar. Está com olheira de quem já fez a janela."

    # Energia: o ensaio pesa mais e tira 30 min do tempo livre de sexta; a
    # revisão do rollback pesa menos; descansar não gasta.
    menu (tipo="conversa"):
        "Quem fica no ensaio de quarta à noite?"
        "\"Eu fico com você no ensaio.\"":
            $ add_friendship_point("co_qualidade", 1)
            $ energia_gastar(2, _("ensaio de quarta até tarde"))
            $ im_hora_extra_somar(30)
            co_qualidade "Ótimo. Eu levo o checklist, você leva a paciência. Pizza por conta do projeto, já pedi."
        "\"Reviso o roteiro de rollback com o [NOME_CO_LEGADO].\"":
            $ add_friendship_point("co_legado", 1)
            $ energia_gastar(1, _("revisão do rollback depois do expediente"))
            co_legado "Combinado. Te mostro onde o script costuma escorregar. Traz caneta, que eu falo rápido quando o assunto é PL/SQL."
        "\"Vou descansar; tenho prova na quinta.\"":
            co_qualidade "Descanso também é gestão de risco. Boa prova. Eu te mando o resultado do ensaio."

    hide co_mentora
    hide co_legado
    hide co_qualidade
    with dissolve

    $ set_time(14, 0)
    scene bg escritorio_interior_tarde
    with fade

    "{i}À tarde, a equipe escreve a RFC. Você cuida da seção de impacto: quem usa, quais tabelas o Farol lê, o que acontece com a central se algo falhar.{/i}"
    show expression "images/artifacts/co_farol_arquitetura.png" as co_diagrama at artefato_tela
    with dissolve
    "{i}O diagrama da semana passada vai como anexo. Cada caixa ganha um responsável e um teste.{/i}"
    hide co_diagrama
    with dissolve
    show co_dev neutral at right_zoom
    with dissolve
    co_dev "Primeira RFC da sua vida? A minha voltou três vezes. Na terceira eu aprendi o que era plano de rollback."
    hide co_dev
    with dissolve

    # Resumo: ensaio de quarta à noite e sexta.
    $ set_time(22, 30)
    scene bg escritorio_interior_noite
    with fade

    if co_ok_risco:
        "{i}Quarta, 22h30. O ensaio estava no plano desde segunda, e a cópia de produção ficou pronta a tempo.{/i}"
    else:
        "{i}Quarta, 22h30. O ensaio entrou no plano depois da revisão de segunda, e a cópia de produção ficou pronta em cima da hora.{/i}"
    "{i}Na primeira rodada, a validação acusa 2,7\% de descrições com acentos de outro padrão. Texto antigo, de antes de alguém trocar a codificação do banco.{/i}"
    "{i}O script é corrigido ali mesmo e roda de novo. Zero registro corrompido. A equipe transforma o resultado no critério de parada da janela: um único registro corrompido, e a carga volta.{/i}"
    "{i}Na sexta, [NOME_CO_QUALIDADE] lê a RFC de ponta a ponta e devolve com dois comentários pequenos. Nenhum sobre o plano de volta.{/i}"

    # Tempo livre da semana 5 (gancho B): sexta à tarde, antes do cartão.
    call im_intermissao(5) from _im_corporativo_s5

    scene black
    with fade
    window hide
    pause 1.1
    window show

    "Fim da Semana 5\n\nAprendizado: mudança boa tem plano de ida e plano de volta. Capacidade limitada pede escolha, e risco conhecido pede ensaio antes da janela."

    return
