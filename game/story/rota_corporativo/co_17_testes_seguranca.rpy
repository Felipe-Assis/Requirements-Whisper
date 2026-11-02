# co_17_testes_seguranca.rpy
# Semana 7 da rota Corporativo: perfis, regressão, senha no repositório,
# aceitação na central e CAB. Bíblia: docs/rotas/corporativo.md, co_17.
# Decisões 19 (co_ok_rbac) e 20 (co_ok_regressao); registro co_reg_verificacao;
# conquistas co_conq_rede e co_conq_trilha.

label co_17_testes_seguranca:
    $ set_available("co_mentora", "co_legado", "co_supervisora", "co_solicitante")
    $ set_time(9, 15)

    play music music_office_focused_2 fadein 1.0
    scene bg escritorio_interior_manha
    with fade

    "{i}Semana 7, segunda-feira. Na quinta, a RFC do Farol vai ao CAB. Até lá, tudo precisa estar testado e registrado.{/i}"

    show co_qualidade neutral at left_zoom
    show co_dev neutral at right_zoom
    with dissolve

    co_qualidade "Bom dia. Plano de testes, versão final. Seis blocos."
    co_qualidade "Um: unidade. Dois: integração com o SGC em homologação. Três: perfis. Quatro: trilha de auditoria."
    co_qualidade "Cinco: carga do pico das nove, com 1.500 usuários. Seis: regressão."
    co_qualidade "Cada bloco tem dono, data e evidência. Se não está registrado, não aconteceu."
    co_dev "Unidade e integração são comigo. A carga eu rodo à noite, para não assustar a central."
    co_qualidade "[player_name], perfis e regressão ficam com você e comigo. Começa pelos perfis."

    show expression "images/artifacts/co_farol_auditoria.png" as tela_auditoria at artefato_tela
    with dissolve
    "{i}[NOME_CO_QUALIDADE] abre a tela da trilha de auditoria. Na aba lateral, a matriz de permissões: solicitante, atendente, supervisor e admin, cada um com o que pode e o que não pode.{/i}"
    hide tela_auditoria
    with dissolve

    show co_qualidade thinking at left_zoom
    with dissolve
    co_qualidade "Quatro perfis. Como você prova que essa matriz vale de verdade?"

    menu:
        "Como verificar os perfis?"

        "Testes negativos por perfil: o atendente tenta abrir a trilha, o solicitante tenta ver chamado de outra pessoa; os dois recebem acesso negado e a tentativa fica registrada.":
            $ co_acerto("co_ok_rbac")
            show co_qualidade neutral at left_zoom
            with dissolve
            co_qualidade "Isso. Perfil se testa pelo lado do não."
            co_qualidade "E a tentativa negada também vai para a trilha: quem tentou, com qual perfil, quando."

        "Testar com o usuário administrador, que acessa tudo.":
            $ co_erro("co_ok_rbac")
            show co_qualidade serious at left_zoom
            with dissolve
            co_qualidade "Prova que funciona para quem pode tudo. Não prova que alguém é impedido."
            co_qualidade "Se um atendente conseguir abrir a trilha, a auditoria da [NOME_CO_SUPERVISORA] perde o valor."

        "Esconder os botões de quem não tem permissão.":
            $ co_erro("co_ok_rbac")
            show co_qualidade serious at left_zoom
            with dissolve
            co_qualidade "Botão escondido não é controle de acesso. Quem souber o endereço da API chama direto."
            co_dev "É o meu erro da semana passada, só que com permissão no lugar de descrição."

    if not co_ok_rbac:
        show co_qualidade thinking at left_zoom
        with dissolve
        co_qualidade "Vamos pelo outro lado. Como provar que alguém não consegue fazer uma coisa?"
        menu:
            "Como você reformula?"

            "Entrar com cada perfil e tentar o que ele não pode. O esperado é acesso negado, registrado na trilha.":
                show co_qualidade neutral at left_zoom
                with dissolve
                co_qualidade "Isso. Teste de permissão pergunta: e se tentar? Anotado no plano."

    $ advance_minutes(80)
    "{i}Você escreve doze casos negativos. O solicitante tenta abrir um chamado de outra pessoa: acesso negado. O atendente tenta abrir a trilha: acesso negado.{/i}"
    "{i}Um caso falha: o perfil supervisor consegue editar perfis, função que é só do admin. [NOME_CO_DEV] corrige antes do almoço, e o caso entra na suíte.{/i}"
    co_dev "Esse teria virado manchete na auditoria. Bem achado."

    co_qualidade "Agora a regressão. A RFC pede a lista do que roda antes da janela. O que entra?"

    menu:
        "O que entra na suíte de regressão antes do CAB?"

        "Só os testes do Farol; o SGC não foi alterado.":
            $ co_erro("co_ok_regressao")
            show co_dev serious at right_zoom
            with dissolve
            co_dev "O Farol grava histórico e lê as mesmas tabelas, e a rotina das 72 h agora grava descrição. Se o relatório mensal quebrar, foi a gente."

        "Os fluxos do SGC que o Farol toca: abrir, resolver, a rotina das 72 h e o relatório mensal da diretoria, além dos testes novos.":
            $ co_acerto("co_ok_regressao")
            show co_qualidade neutral at left_zoom
            with dissolve
            co_qualidade "Isso. Regressão olha para o que já funcionava, inclusive o que o Farol só toca de leve."
            co_qualidade "E os testes de caracterização da semana passada entram direto. Já estão prontos."

        "Testar manualmente em produção depois da janela.":
            $ co_erro("co_ok_regressao")
            show co_qualidade serious at left_zoom
            with dissolve
            co_qualidade "Depois da janela, defeito vira incidente com a central aberta. Regressão serve para descobrir antes."

    if not co_ok_regressao:
        show co_qualidade thinking at left_zoom
        with dissolve
        co_qualidade "Pensa no que já funcionava e pode ser afetado."
        menu:
            "Como você reformula?"

            "Tudo que usa as mesmas tabelas ou a rotina das 72 h: abrir, resolver, a rotina e o relatório mensal, mais os testes novos.":
                show co_qualidade neutral at left_zoom
                with dissolve
                co_qualidade "Fechado. Lista registrada na RFC."

    $ advance_minutes(45)
    show co_dev serious at right_zoom
    with dissolve
    co_dev "Gente. Olha isso aqui."
    "{i}Procurando a configuração da integração, [NOME_CO_DEV] abre um arquivo antigo do repositório. Numa linha marcada como \"provisório\" está a senha do usuário de integração do SGC.{/i}"
    "{i}O histórico do arquivo mostra a data: 2012.{/i}"
    co_dev "Provisório desde 2012. É mais velho que meu primeiro celular."
    show co_qualidade serious at left_zoom
    with dissolve
    co_qualidade "Respira. Ninguém copia, ninguém posta print. A gente decide como relatar."

    menu:
        "Como você relata a senha no repositório?"

        "Registro como vulnerabilidade e levo para [NOME_CO_QUALIDADE] e [NOME_CO_LEGADO], sem procurar culpados.":
            $ co_senha_relato = "registro"
            $ add_friendship_point("co_qualidade", 1)
            show co_qualidade neutral at left_zoom
            with dissolve
            co_qualidade "Era exatamente o que eu ia pedir. Registro primeiro, conversa depois."

        "Pergunto ao [NOME_CO_LEGADO] como a senha foi parar ali antes de registrar.":
            $ co_senha_relato = "historia"
            $ add_friendship_point("co_legado", 1)
            play sound "audio/effects/cell_vibration.ogg"
            show co_legado portrait at center_zoom
            with dissolve
            co_legado "(mensagem) Essa é minha. 2012, integração com o RH para entregar numa sexta. Pus a senha ali \"só até segunda\"."
            co_legado "(mensagem) Ninguém voltou para corrigir. Nem eu. Me põe no registro como quem ajuda a resolver."
            hide co_legado
            with dissolve

        "Posto no grupo geral da TI para todo mundo ver.":
            $ co_senha_relato = "grupo"
            co_qualidade "Espera. Expor um segredo para 300 pessoas aumenta o problema. Vamos trocar a senha agora."

    co_qualidade "Passo a passo. Um: a senha vai para o cofre de segredos, e a integração passa a ler de lá."
    co_qualidade "Apagar a linha do arquivo não basta. A senha antiga continua no histórico do repositório, para quem quiser procurar."
    co_qualidade "Dois: por isso trocamos a senha do usuário de integração. É mudança padrão, pré-aprovada. Não espera o CAB."
    co_qualidade "Três: registramos o caso. O que aconteceu, desde quando, o que fizemos. Sem nome de culpado."
    co_dev "Sem caça às bruxas. Gostei."
    co_qualidade "Caça às bruxas só ensina as pessoas a esconder. Eu quero que me contem."

    $ co_registrar("co_reg_verificacao")

    hide co_qualidade
    hide co_dev
    with dissolve

    # Quarta à tarde, na central: Rosângela presente; Kauã ficou no andar.
    $ set_available("co_mentora", "co_legado", "co_dev", "co_solicitante")
    $ set_time(14, 30)
    scene bg central_atendimento_tarde
    with fade

    "{i}Quarta-feira à tarde, na central. Luz laranja nas persianas e menos fila do que de manhã.{/i}"
    "{i}[NOME_CO_SUPERVISORA] separou dois atendentes para o teste de aceitação: Neusa e Paulo.{/i}"

    show co_supervisora neutral at left_zoom
    show co_qualidade neutral at right_zoom
    with dissolve

    co_supervisora "Tenho quarenta minutos. Depois disso, minha equipe volta para a fila. Vamos ver esse Farol."
    co_qualidade "Três roteiros: bloqueio da descrição vazia, modelos de descrição e trilha."

    "{i}Paulo tenta resolver um chamado de VPN sem escrever nada. O Farol mantém Em atendimento e mostra: \"Descreva o que foi feito. Se quiser, use um modelo.\"{/i}"
    "{i}Neusa escolhe o modelo de Reset de senha, ajusta duas palavras e resolve em menos de vinte segundos.{/i}"

    show co_supervisora thinking at left_zoom
    with dissolve
    co_supervisora "Vinte segundos. Isso cabe no meu TMA. Paulo, de novo, agora com o modelo de VPN."

    show expression "images/artifacts/co_farol_auditoria.png" as tela_auditoria at artefato_tela
    with dissolve
    "{i}Na trilha, uma linha chama a atenção: usuário \"sistema\", ação \"Encerrado automaticamente após 72 h sem retorno do solicitante\". Ao lado, um cadeado.{/i}"
    hide tela_auditoria
    with dissolve

    co_supervisora "Isso aqui. Na auditoria interna de 2021, passei uma semana montando planilha para explicar quem fechou o quê."
    co_supervisora "Com essa tela, eu teria economizado a semana inteira."
    show co_supervisora neutral at left_zoom
    with dissolve
    co_supervisora "Aprovado pela central. Mas o treinamento da minha equipe é antes da janela, não depois."
    co_qualidade "Registrado. Treinamento na sexta, quinze minutos por turno."

    hide co_supervisora
    hide co_qualidade
    with dissolve

    $ set_available("co_mentora", "co_legado", "co_supervisora", "co_solicitante")
    $ set_time(11, 40)
    scene bg escritorio_interior_manha
    with fade

    "{i}Quinta-feira, fim da manhã. [NOME_CO_QUALIDADE] volta da reunião do CAB com o tablet debaixo do braço.{/i}"

    show co_qualidade neutral at left_zoom
    show co_dev neutral at right_zoom
    with dissolve

    if co_ok_cab:
        co_qualidade "Aprovada. Janela de sábado, da meia-noite às quatro."
        co_qualidade "E a RFC passou sem nenhuma pergunta. Isso quase nunca acontece. Tirei print."
    else:
        co_qualidade "Aprovada. Janela de sábado, da meia-noite às quatro."
        co_qualidade "Teve duas perguntas sobre o plano de volta. Respondi com o roteiro que a gente revisou. Passou."

    co_dev "Bora! Agora é a semana 8."
    co_qualidade "Agora é descansar antes de sexta à noite. Janela de madrugada com sono é incidente esperando acontecer."

    $ co_conceder("co_conq_rede")
    $ co_conceder("co_conq_trilha")

    hide co_qualidade
    hide co_dev
    with dissolve

    scene black
    with fade
    window hide
    pause 1.0
    window show

    "Fim da Semana 7\n\nAprendizado: teste de permissão se faz pelo lado do não."

    return
