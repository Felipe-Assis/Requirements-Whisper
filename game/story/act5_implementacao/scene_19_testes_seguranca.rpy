# Pontos da autoavaliação de maturidade (0 a 12): testes de segurança feitos
# hoje (até 6) mais as três respostas do questionário (até 6).
default s19_pontos_maturidade = 0

label scene_19_testes_seguranca:
    $ set_available("developer_management", "developer_requirements", "developer_project")

    play music music_office_concentrated_1 fadein 1.0
    scene bg escritorio_interior_manha
    with dissolve

    $ set_time(9, 0)
    $ advance_minutes(10)
    "{i}Novo dia. O clima no escritório é diferente: hoje o foco é testar o sistema, validar requisitos e reforçar a segurança da informação.{/i}"

    show developer_quality serious at left_zoom
    show developer_security serious at right_zoom

    developer_quality "Vamos começar pelo checklist de qualidade. Lembre-se: um sistema pode funcionar, mas só é confiável se passar nos testes."
    developer_security "E qualquer brecha de segurança pode virar dor de cabeça. Atenção máxima aos detalhes!"
    if energia_cansaco():
        developer_quality "Vamos devagar no checklist hoje. Teste feito com sono vira teste pulado."

    # Exibe checklist baseado nos artefatos reais
    "{i}No notebook, você abre o checklist de testes:{/i}"
    window hide
    pause 1.2
    window show

    "\"Checklist:"
    "• Testes de unidade (funções críticas, validação de campos)"
    "• Testes de integração (cadastro, autenticação, notificações, exportação de relatórios)"
    "• Validação de permissões de acesso (papéis de usuário, RBAC, fluxos administrativos)"
    "• Testes de injeção (SQL Injection, XSS, campos editáveis e uploads)"
    "• Cobertura de código (buscando alcançar acima de 80\%)"
    "• Testes de autenticação, redefinição de senha, e multi-fator"
    "• Verificação de logs, backups e anonimização de dados"
    "• Plano de resposta a incidentes"

    $ testes_realizados = []
    $ checklist_opcoes = ["unidade", "integracao", "permissoes", "injeção", "cobertura", "autenticacao", "logs", "backup"]
    $ bugs_encontrados = 0
    $ vulnerabilidades = 0

    $ revisoes = 0
    while revisoes < 4:
        menu (tipo="trabalho"):
            "Por onde começar os testes?"
            "Testes de unidade" if "unidade" in checklist_opcoes:
                $ testes_realizados.append("unidade")
                $ checklist_opcoes.remove("unidade")
                show developer_test enthusiastic at right_zoom2
                developer_test "Excelente! Teste de unidade detecta falhas logo de cara. Já achei um bug na função de cadastro de paciente!"
                $ bugs_encontrados += 1
                hide developer_test
            "Testes de integração" if "integracao" in checklist_opcoes:
                $ testes_realizados.append("integracao")
                $ checklist_opcoes.remove("integracao")
                show developer_quality positive at left_zoom
                developer_quality "Testes de integração pegam erros na comunicação entre módulos, como falhas na exportação de relatórios ou notificações não entregues. Boa escolha!"
                hide developer_quality
            "Validação de permissões" if "permissoes" in checklist_opcoes:
                $ testes_realizados.append("permissoes")
                $ checklist_opcoes.remove("permissoes")
                show developer_security thinking at right_zoom
                if rast_lacuna_achada("saude_rast_acesso"):
                    developer_security "Ótimo! A recepção abrindo o histórico, o teste do quadro já tinha pegado. Sobrou outro: o perfil administrativo vê relatório clínico sem precisar. Corrija isso logo!"
                else:
                    developer_security "Ótimo! Papéis mal definidos são porta de entrada para problemas sérios. Detectou um acesso indevido de usuário comum. Corrija isso logo!"
                $ vulnerabilidades += 1
                hide developer_security
            "Testes de injeção" if "injeção" in checklist_opcoes:
                $ testes_realizados.append("injeção")
                $ checklist_opcoes.remove("injeção")
                show developer_security enthusiastic at right_zoom
                developer_security "Essencial! Encontrou campo vulnerável a SQL Injection. Anote para mitigar imediatamente!"
                $ vulnerabilidades += 1
                hide developer_security
            "Cobertura de código" if "cobertura" in checklist_opcoes:
                $ testes_realizados.append("cobertura")
                $ checklist_opcoes.remove("cobertura")
                show developer_quality serious at left_zoom
                developer_quality "Cobertura acima de 80\% é o ideal. Me chama se precisar gerar relatório."
                hide developer_quality
            "Testes de autenticação" if "autenticacao" in checklist_opcoes:
                $ testes_realizados.append("autenticacao")
                $ checklist_opcoes.remove("autenticacao")
                show developer_security serious at right_zoom
                developer_security "Valide que links de recuperação de senha expiram corretamente e que login inválido bloqueia após tentativas erradas."
                hide developer_security
            "Verificação de logs e backups" if "logs" in checklist_opcoes or "backup" in checklist_opcoes:
                if "logs" in checklist_opcoes:
                    $ testes_realizados.append("logs")
                    $ checklist_opcoes.remove("logs")
                    show developer_ai positive at left_zoom
                    developer_ai "Logs bem feitos facilitam análise de incidentes e rastreamento de bugs. Automatize o envio para SIEM, se puder!"
                    hide developer_ai
                if "backup" in checklist_opcoes:
                    $ testes_realizados.append("backup")
                    $ checklist_opcoes.remove("backup")
                    show developer_test positive at right_zoom2
                    developer_test "Testou o backup? Simular restauração é obrigatório! Melhor prevenir do que remediar."
                    hide developer_test
        $ revisoes += 1

    $ registrar("saude_reg_testes")

    # Inclusão da avaliação de conformidade (questionário de maturidade)
    "{i}Antes da reunião de fechamento, [NOME_DEVELOPER_SECURITY] sugere uma autoavaliação rápida usando o modelo de maturidade de privacidade e segurança.{/i}"

    show developer_security serious at right_zoom
    with dissolve
    developer_security "Funciona assim: cada teste de segurança que fizemos hoje conta ponto. Depois, três perguntas sobre como o time trabalha."
    developer_security "Prática adequada vale 2 pontos, meia solução vale 1, e o resto vale 0. Sem chutar para cima, combinado?"

    # Testes de segurança feitos hoje: 2 pontos cada, até 3 testes.
    $ s19_pontos_maturidade = 2 * min(3, len([t for t in ("permissoes", "injeção", "autenticacao", "logs") if t in testes_realizados]))

    menu (tipo="trabalho"):
        "Os relatórios de pesquisa da [NOME_DOUTORA_1] exportam dados de pacientes. O que o time faz?"
        "Anonimiza os dados antes da exportação: sem nome, CPF ou contato.":
            $ s19_pontos_maturidade += 2
            developer_security "Isso. Pesquisa precisa dos números, não de quem é o paciente. É o que a LGPD pede."
        "Coloca senha no arquivo exportado.":
            $ s19_pontos_maturidade += 1
            developer_security "Ajuda, mas é meia solução. Se a senha vazar, os dados vão junto com nome e CPF."
        "Exporta tudo; quem recebe é médica e sabe o que faz.":
            developer_security "Confiar na pessoa não protege o arquivo. Planilha se perde, vai para e-mail errado, fica em pendrive."

    menu (tipo="trabalho"):
        "Alguém alterou o peso de um paciente no prontuário. Como saber quem foi?"
        "Pelo log de auditoria: usuário, data, campo e valor anterior.":
            $ s19_pontos_maturidade += 2
            developer_security "Exato. Em dado clínico, rastreabilidade é requisito, não luxo."
        "Restaurando o backup da véspera e comparando.":
            $ s19_pontos_maturidade += 1
            developer_security "Mostra o que mudou, mas não quem mudou. E dá um trabalho enorme."
        "Perguntando no grupo da equipe médica.":
            developer_security "Aí depende da memória de cada um. Não dá para auditar assim."

    menu (tipo="trabalho"):
        "E se houver um vazamento de dados amanhã?"
        "Seguir o plano de resposta: conter, avaliar o impacto e avisar o Instituto e os pacientes afetados.":
            $ s19_pontos_maturidade += 2
            developer_security "Isso. Com o plano escrito, ninguém precisa improvisar sob pressão."
        "Corrigir a falha logo e avisar só se alguém perguntar.":
            developer_security "Esconder piora tudo. A LGPD exige comunicar, e o Instituto perde a confiança no sistema."
        "Ainda não temos plano, mas a gente resolve na hora.":
            $ s19_pontos_maturidade += 1
            developer_security "Pelo menos é sincero. Fica como pendência: o plano precisa existir antes do deploy."
    hide developer_security
    with dissolve

    "{i}O notebook soma os pontos dos testes de segurança e das respostas e mostra o nível de maturidade do time, de Inexistente a Excelente.{/i}"

    $ maturidade_percentual = s19_pontos_maturidade * 100 // 12
    if maturidade_percentual >= 91:
        $ nivel_maturidade = "Excelente"
    elif maturidade_percentual >= 71:
        $ nivel_maturidade = "Avançado"
    elif maturidade_percentual >= 41:
        $ nivel_maturidade = "Básico"
    elif maturidade_percentual >= 11:
        $ nivel_maturidade = "Inicial"
    else:
        $ nivel_maturidade = "Inexistente"

    show developer_quality positive at left_zoom
    with dissolve
    developer_quality "Nossa avaliação ficou em [maturidade_percentual]\% — Nível [nivel_maturidade]. Isso mostra como evoluímos desde o início!"
    if maturidade_percentual < 91:
        show developer_quality thinking at left_zoom
        developer_quality "Para chegar ao Excelente, falta cobrir mais testes de segurança ou fechar as práticas que ficaram pela metade."
    hide developer_quality

    show developer_security thinking at right_zoom
    developer_security "Privacidade, segurança e testes: quanto mais investirmos, menos riscos teremos no futuro. Mantenham o checklist sempre atualizado!"
    hide developer_security

    # Padding: Revisão coletiva e resolução colaborativa de bugs/vulns
    scene bg escritorio_interior_tarde
    with dissolve
    play sound "audio/effects/ambiente_reuniao.ogg"
    "{i}À tarde, o time se reúne para debater as vulnerabilidades e bugs encontrados, documentando as correções e discutindo oportunidades de melhoria contínua.{/i}"

    # O critério C3 do quadro de rastreabilidade (scene_17): com o teste
    # escrito, a falha nem chegou; sem ele, aparece agora.
    if rast_lacuna_achada("saude_rast_acesso"):
        show developer_test confident at right_zoom2
        developer_test "Uma boa notícia no meio dos bugs: a recepção abrindo o histórico de saúde nem chegou até hoje. O teste do quadro falhou na pipeline semana passada e o [NOME_DEVELOPER_CODING] corrigiu no mesmo dia."
        hide developer_test
    else:
        show developer_security serious at right_zoom
        show developer_test thinking at right_zoom2
        developer_security "Rodei a revisão de papéis antes do almoço. A falha mais séria: o perfil recepção abre o histórico de saúde inteiro. Diagnóstico, escalas, tudo."
        developer_test "Voltei ao quadro de rastreabilidade que a gente montou duas semanas atrás. O critério estava lá, C3: recepção abre o histórico, acesso negado. Mas nenhum teste cobria. Foi esse o elo que faltou."
        developer_test "Já escrevi o teste que faltava. Agora ele roda em todo commit, e a correção só entra com ele passando."
        hide developer_security
        hide developer_test

    # Pequena ramificação: pedir ajuda
    menu (tipo="trabalho"):
        "Enfrenta dificuldade para corrigir uma falha crítica. O que faz?"
        "Chama [NOME_DEVELOPER_CODING] para revisar código seguro.":
            show developer_coding serious at right_zoom2
            developer_coding "Vamos revisar juntos linha a linha. Segurança se constrói em equipe!"
            hide developer_coding
        "Solicita apoio de [NOME_DEVELOPER_AI] para automatizar testes de segurança.":
            show developer_ai thinking at left_zoom
            developer_ai "Tenho um script de fuzzing que pode acelerar a detecção de falhas. Vou compartilhar contigo."
            hide developer_ai
        "Procura documentação e fóruns especializados.":
            "{i}Você encontra boas práticas, mas percebe que colaboração interna acelera ainda mais a solução.{/i}"
        "Lembrar ao [NOME_DEVELOPER_SECURITY] da senha emprestada: a recepção entra com a senha da médica" (tipo="pista") if pista_tem("saude_p_papeis"):
            $ pista_usar("saude_p_papeis")
            show developer_security thinking at right_zoom
            if rast_lacuna_achada("saude_rast_acesso"):
                developer_security "A senha emprestada. O teste garante que o perfil recepção não abre o histórico. Mas, se a recepção entra com a senha da doutora, o teste passa e o problema continua."
            else:
                developer_security "A senha emprestada. Então corrigir o perfil não basta: se a recepção continuar com a senha da doutora, o histórico abre para a pessoa errada e a trilha registra a médica."
            developer_security "A correção tem duas partes: um login para cada pessoa da recepção, com agenda e cadastro, e uma conversa com a [NOME_DOUTORA_2] sobre senha emprestada."
            "{i}Vocês escrevem juntos a mensagem para a [NOME_DOUTORA_2]: sem culpa, com o motivo. A correção passa a cobrir a causa, não só o sintoma.{/i}"
            $ add_friendship_point("developer_security", 0.5)
            hide developer_security

    $ energia_gastar(1, _("dia inteiro caçando bugs"))

    # Tempo livre da semana 7. A cena seguinte já troca o fundo.
    call im_intermissao(7) from _im_saude_s7
    play music music_office_relaxed fadein 1.0

    # Fechamento: Reflexão e estatísticas
    scene bg escritorio_interior_noite
    with fade
    "{i}Fim do expediente: todos comemoram os bugs corrigidos, e a confiança na segurança do sistema cresce. A equipe aprende que maturidade não é só pontuação: é cultura de melhoria contínua e colaboração.{/i}"

    # Feedback final e conquistas
    if bugs_encontrados + vulnerabilidades >= 3:
        "{i}Você desbloqueou a conquista: 'Caça a Bugs e Vulnerabilidades'!{/i}"
        $ inventario.append("conquista_bug_vuln")
        play sound "audio/effects/recompensa.ogg"
    if maturidade_percentual >= 91:
        "{i}Time em nível 'Excelente': conquista 'Privacidade Levada a Sério' adicionada ao inventário!{/i}"
        $ inventario.append("conquista_guardiao_privacidade")
        play sound "audio/effects/recompensa.ogg"

    scene bg quarto_noite
    with fade
    "{i}Já em casa, você reflete sobre como aplicar práticas de teste, checklist, e governança é indispensável — e sente orgulho do amadurecimento profissional alcançado ao longo do projeto.{/i}"

    window hide
    pause 1.1
    window show

    "{i}Fim da Semana 7\n\nAprendizado: Testes e segurança são processos contínuos, e a maturidade de um time depende tanto de técnica quanto de cultura de colaboração e transparência.{/i}"

    return
