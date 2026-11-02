# co_18_implantacao_avaliacao.rpy
# Semana 8 da rota Corporativo: janela de sábado, problema na carga do
# histórico, rollback parcial e avaliação com os stakeholders.
# Bíblia: docs/rotas/corporativo.md, co_18. Decisão 21 (co_ok_janela);
# conquista co_conq_janela; final por co_calcular_final().
# A janela vai da 0h às 4h de sábado: o Farol é ligado antes das 4h e às 4h15
# a equipe fecha o registro da mudança.

label co_18_implantacao_avaliacao:
    $ set_available()
    $ set_time(23, 30)

    play music music_office_concentrated_2 fadein 1.0
    scene bg escritorio_interior_noite
    with fade

    "{i}Semana 8. Sexta-feira, 23h30. O prédio está quase vazio. A janela de mudança começa à meia-noite e fecha às quatro da manhã de sábado.{/i}"
    "{i}A sala do andar virou sala de guerra: pizza fria, dois monitores grandes e o roteiro aprovado pelo CAB impresso sobre a mesa.{/i}"

    show co_mentora neutral at left_zoom
    show co_qualidade neutral at right_zoom
    with dissolve

    co_mentora "Boa noite, gente. Vamos por partes: seis passos, um de cada vez, e ninguém pula nenhum."
    co_qualidade "Lendo. Um: backup verificado. Dois: publicar o Farol desligado. Três: ativar a camada e a regra."
    co_qualidade "Quatro: carga do histórico. Cinco: testes de fumaça. Seis: ligar o Farol para os usuários."
    co_qualidade "Critério de parada da carga: zero registro corrompido. Está na RFC, assinado."
    co_mentora "A [NOME_CO_SUPERVISORA] está de plantão no telefone. Ela disse que vai dormir de headset."

    $ set_time(0, 5)
    scene bg sala_servidores
    with fade

    "{i}Meia-noite e cinco. Na sala de servidores, você confere o backup com [NOME_CO_LEGADO]. No canto, o rack bege da Tia Neide pisca, como quem também está de plantão.{/i}"
    show co_legado thinking at center_zoom
    with dissolve
    co_legado "Backup sem restauração testada é só esperança. Restaurei uma cópia ontem à tarde. Bateu."
    show co_legado neutral at center_zoom
    with dissolve
    co_legado "Passo um, feito. A Tia Neide aprova. Ela não fala, mas eu sei."

    $ set_time(0, 50)
    scene bg escritorio_interior_noite
    with fade

    "{i}Passo dois: o Farol sobe desligado. Passo três: a camada e a regra entram. [NOME_CO_DEV] roda as verificações de leitura em produção: consulta pelo número e conexão com o SGC. Tudo verde.{/i}"

    $ set_time(1, 20)
    "{i}Passo quatro: começa a carga das 200 mil descrições históricas. A barra de progresso anda devagar.{/i}"

    $ set_time(2, 10)
    show co_dev serious at right_zoom
    with dissolve
    co_dev "Opa. A validação acusou registro com caractere quebrado."

    if co_ok_risco:
        co_dev "São 0,4\%. Tudo de uma filial que usava outro padrão de acento em 2009. O ensaio não tinha esse caso."
        show co_legado thinking at left_zoom
        with dissolve
        co_legado "Filial de Belém, aposto. Em 2009 eles tinham um servidor só deles. Isso aí tem história."
    else:
        co_dev "São 3,1\% dos registros. Acento quebrado, aspas coladas do Word, texto cortado no meio."
        show co_legado serious at left_zoom
        with dissolve
        co_legado "O ensaio foi feito tarde e pegou menos casos do que devia. Esses escaparam."

    show co_qualidade serious at center_zoom
    with dissolve
    co_qualidade "Critério de parada: zero registro corrompido. Não deu zero."
    co_qualidade "[player_name], faltam menos de duas horas de janela. Fala o que você faria."

    menu:
        "Faltam menos de duas horas de janela. O que fazer?"

        "Corrigir os registros na mão direto no banco de produção.":
            $ co_erro("co_ok_janela")
            co_qualidade "Isso é mudança não autorizada, sem teste e sem trilha. Se um UPDATE errar, não temos como explicar o que mudou."
            co_qualidade "E às duas da manhã, com sono, o UPDATE erra."

        "Seguir o plano: reverter só a carga do histórico, que é um passo independente, ligar o Farol com o que passou nos testes, registrar um problema e reagendar a carga.":
            $ co_acerto("co_ok_janela")
            hide co_dev
            show co_mentora neutral at right_zoom
            with dissolve
            co_mentora "Para isso serve o critério de parada. Ninguém precisa ser herói às 2h da manhã."

        "Seguir assim; quase ninguém consulta chamado antigo.":
            $ co_erro("co_ok_janela")
            play sound "audio/effects/phone_rining.ogg"
            "{i}O telefone em viva-voz toca. É a [NOME_CO_SUPERVISORA], que ouviu tudo pela linha aberta.{/i}"
            co_supervisora "(telefone) A auditoria interna consulta. E o critério que aprovamos no CAB diz zero registro corrompido."

    if not co_ok_janela:
        hide co_dev
        show co_mentora thinking at right_zoom
        with dissolve
        co_mentora "Calma. O que o plano aprovado diz para esse caso?"
        menu:
            "Como você reformula?"

            "Passou do critério de parada: volta o passo 4, segue o resto e registra o problema.":
                show co_mentora neutral at right_zoom
                with dissolve
                co_mentora "Isso. A carga é um passo independente. Ela volta sozinha, e o resto segue."
                co_mentora "Ninguém precisa ser herói às 2h da manhã. O plano já decidiu por nós quando estávamos descansados."

    $ co_conceder("co_conq_janela")

    co_qualidade "Registrando. Não é incidente: nada parou, ninguém ficou sem serviço. É problema: tem uma causa para investigar com calma."
    co_legado "Rodando o script de reversão do passo quatro. O mesmo que a gente testou no ensaio."
    "{i}Em seis minutos, a tabela de histórico volta ao estado de antes da carga. O resto do Farol continua no lugar.{/i}"

    $ set_time(2, 30)
    hide co_legado
    hide co_qualidade
    hide co_mentora
    show co_dev serious at center_zoom
    with dissolve
    co_dev "Desculpa, gente. Fui eu que escrevi o script da carga. Eu devia ter pegado isso."
    "{i}[NOME_CO_DEV] anda de um lado para o outro, com o fone no pescoço e um copo de café vazio na mão.{/i}"

    menu:
        "[NOME_CO_DEV] está nervoso. O que você faz?"

        "\"Seguimos o roteiro. Foi para isso que ensaiamos.\"":
            $ add_friendship_point("co_dev", 1)
            show co_dev neutral at center_zoom
            with dissolve
            co_dev "É. O roteiro funcionou. Eu é que ainda não tinha acreditado nele."
            co_dev "Bora para o passo cinco."

        "Ajudar a [NOME_CO_MENTORA] a escrever as atualizações para [NOME_CO_SUPERVISORA] e [NOME_CO_SOLICITANTE].":
            $ add_friendship_point("co_mentora", 1)
            show co_mentora neutral at left_zoom
            with dissolve
            co_mentora "Texto curto e sem sigla: o que entrou, o que ficou para depois e quando."
            "{i}Vocês escrevem juntos: \"O Farol entra hoje com consulta e bloqueio. As descrições antigas entram numa próxima janela. Nenhum dado foi perdido.\"{/i}"
            "{i}Enquanto isso, [NOME_CO_DEV] respira fundo e volta para o terminal.{/i}"
            hide co_mentora
            with dissolve

        "\"Vou dar uma volta para esfriar a cabeça.\"":
            "{i}Você vai até a copa, toma um copo d'água e volta. [NOME_CO_LEGADO] está do lado de [NOME_CO_DEV], contando a história da Tia Neide pela terceira vez. Parece funcionar.{/i}"

    $ set_time(3, 40)
    hide co_dev
    with dissolve

    "{i}Passo cinco: testes de fumaça. Consulta pelo número, bloqueio sem descrição, acesso negado por perfil, linha \"sistema\" na trilha. Tudo passa.{/i}"

    if co_negociacao_opcao == "investigar_agora":
        "{i}Passo seis: às 3h52, o Farol é ligado para a central e para o piloto da equipe do [NOME_CO_SOLICITANTE]. A liberação para todos fica para a janela seguinte, como combinado.{/i}"
    else:
        "{i}Passo seis: às 3h52, o Farol é ligado para todos os funcionários do Grupo Vértice.{/i}"

    $ set_time(4, 15)
    show co_qualidade neutral at left_zoom
    show co_legado neutral at right_zoom
    with dissolve
    co_qualidade "Mudança dentro da janela. Registro fechado às 4h15. Se não está registrado, não aconteceu. Está registrado."
    co_legado "Vão para casa. A Tia Neide e eu cuidamos do resto. Brincadeira, eu também vou."

    play music music_office_motivated fadein 1.5
    scene bg central_atendimento_tarde
    with fade
    $ set_time(15, 0)

    "{i}Segunda-feira, três da tarde. Na central, o painel de filas parece mais calmo do que na semana passada.{/i}"

    show co_supervisora neutral at left_zoom
    show co_mentora neutral at center_zoom
    show co_solicitante neutral at right_zoom
    with dissolve

    co_mentora "[NOME_CO_SUPERVISORA], [NOME_CO_SOLICITANTE], obrigada por virem. Hoje quem conduz a conversa é [player_name]."
    "{i}[NOME_CO_MENTORA] se senta e deixa a ponta da mesa para você. Você abre o relatório e começa pelo que aconteceu, não pelo que foi feito.{/i}"
    co_supervisora "Número é comigo. Ligação de cobrança de andamento era 18\% da central. Em dois dias de Farol, caiu para 11\%."
    co_supervisora "Em dois dias. Minha equipe percebeu antes do relatório."
    co_solicitante "Fala! Minha vez. Sábado à tarde, o notebook do Wellington voltou a perder a VPN."
    co_solicitante "O chamado dizia Resolvido, com a solução escrita. Só que não resolveu. Reabri pelo celular, na porta da subestação, com o motivo."

    show expression "images/artifacts/co_farol_consulta.png" as tela_farol at center_zoom
    with dissolve
    "{i}Na tela, o chamado do Wellington aparece de volta Em atendimento. A solução anterior continua guardada no histórico.{/i}"
    hide tela_farol
    with dissolve
    co_solicitante "Ninguém ligou para ninguém. Pela primeira vez."

    $ co_calcular_final()

    if co_final_resultado in ("excelente", "bom"):
        show expression "images/artifacts/co_farol_auditoria.png" as tela_auditoria at center_zoom
        with dissolve
        co_supervisora "O bloqueio e a trilha mudaram minha semana. Pela primeira vez sei o que minha equipe fez sem perguntar."
        hide tela_auditoria
        with dissolve
        co_solicitante "E eu reabri chamado de botina, no meio do mato. Para mim, isso é o sistema."
        co_mentora "[player_name], você conduziu essa conversa como alguém da equipe. Não como quem está de passagem."
        hide co_mentora
        show co_qualidade neutral at center_zoom
        with dissolve
        if co_ok_cab:
            co_qualidade "E a RFC passou no CAB sem nenhuma pergunta. Guardei como modelo para as próximas."
        else:
            co_qualidade "E a RFC passou no CAB e a janela foi cumprida. Vira modelo para as próximas."
        if co_final_resultado == "bom":
            show co_supervisora thinking at left_zoom
            with dissolve
            co_supervisora "Duas coisas para melhorar. Treinamento curto para o turno da noite, que pegou o Farol sem ter visto. E mais modelos de descrição: impressora e acesso a sistema de campo ainda estão sem."
            show co_solicitante thinking at right_zoom
            with dissolve
            co_solicitante "E o aviso. Meu técnico ainda não abre a intranet. Quero saber quando o WhatsApp chega."
    else:
        show co_supervisora thinking at left_zoom
        with dissolve
        co_supervisora "Avançou, e eu reconheço. Mas vou ser honesta."
        if co_ok_episodio and co_ok_conflito:
            co_supervisora "A entrevista foi boa. Depois dela, minha equipe só viu o Farol no teste de aceitação. Faltou trazer a central mais vezes para perto."
        else:
            co_supervisora "No começo vocês chegaram com proposta antes de ouvir a central. Só depois a conversa melhorou."
        show co_solicitante thinking at right_zoom
        with dissolve
        if co_ok_risco:
            co_solicitante "E o aviso. Meu técnico ainda não abre a intranet, e eu ainda não sei quando isso muda."
        else:
            co_solicitante "E a carga do histórico. Com ensaio feito antes, com folga, talvez não precisasse de outra janela."
        co_mentora "É tudo verdade, e dá para transformar em plano."
        co_mentora "Na próxima rodada: uma manhã na central antes de qualquer proposta, o ensaio da carga marcado duas semanas antes da janela e uma data para conversar sobre o aviso."

    hide co_mentora
    hide co_qualidade
    show co_dev neutral at center_zoom
    with dissolve
    if co_negociacao_opcao == "investigar_agora":
        co_dev "Sobre o WhatsApp: o parecer do jurídico chega esta semana. Se vier sem ressalva, a liberação para todos e o aviso entram juntos na próxima janela."
        co_solicitante "Minha equipe do piloto já está mostrando para os outros. Pode mandar."
    else:
        co_dev "Sobre o WhatsApp: como combinamos, a investigação começa na próxima rodada. [NOME_CO_SOLICITANTE], sua equipe ajuda a testar antes de a gente estimar data."
        co_solicitante "Fechado. Prefiro data certa a promessa bonita."
    co_dev "E a carga do histórico já tem nova janela marcada, com o script corrigido e outro ensaio."

    hide co_supervisora
    hide co_solicitante
    hide co_dev
    with dissolve

    $ set_time(18, 0)
    scene bg empresa_exterior_noite
    with fade

    "{i}Seis da tarde. A equipe sai junta pela porta giratória da torre de vidro. O Rio começa a acender as luzes.{/i}"

    if co_conq_memoria:
        show co_legado neutral at center_zoom
        with dissolve
        co_legado "[player_name], já gravei três Causos do SGC no wiki. O da Tia Neide teve doze visualizações. Dez são minhas."
        co_legado "Toma. A caneca de 2008. Guarda até março. Depois você decide se fica com ela ou passa para quem chegar."
        "{i}A caneca branca de faixa azul, lascada na borda, pesa mais do que parece.{/i}"
        hide co_legado
        with dissolve

    if co_amizade_total >= 28:
        show co_mentora neutral at left_zoom
        show co_dev neutral at center_zoom
        show co_qualidade neutral at right_zoom
        with dissolve
        co_mentora "A gente conversou entre nós. Vai ter uma próxima rodada do Farol, e queremos você nela."
        co_dev "Bora!"
        co_qualidade "Convite registrado. Agora aconteceu."
        hide co_mentora
        hide co_dev
        hide co_qualidade
        with dissolve

    "{i}No caminho para o ônibus, você pensa no chamado 48213. Oito semanas atrás, era só uma linha com a solução vazia.{/i}"
    "{i}Agora ele tem história, trilha e alguém do outro lado que sabe o que foi feito. E o ciclo não termina aqui: ele volta a ouvir quem usa.{/i}"

    scene black
    with fade
    window hide
    pause 1.0
    window show

    "Fim da Semana 8\n\nAprendizado: num sistema legado, a implantação não encerra o ciclo. Ela abre a próxima conversa."

    return
