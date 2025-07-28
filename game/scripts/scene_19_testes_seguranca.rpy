label scene_19_testes_seguranca:
    $ disponivel_developer_ai = False
    $ disponivel_developer_coding = False
    $ disponivel_developer_management = True
    $ disponivel_developer_requirements = True
    $ disponivel_developer_project = True
    $ disponivel_developer_quality = False
    $ disponivel_developer_security = False
    $ disponivel_developer_test = False

    play music music_office_concentrated_1 fadein 1.0
    scene bg escritorio_interior_manha
    with dissolve

    $ advance_minutes(10)
    "{i}Novo dia. O clima no escritório é diferente: hoje o foco é testar o sistema, validar requisitos e reforçar a segurança da informação.{/i}"

    show developer_quality serious at left_zoom
    show developer_security serious at right_zoom

    developer_quality "Vamos começar pelo checklist de qualidade. Lembre-se: um sistema pode funcionar, mas só é confiável se passar nos testes."
    developer_security "E qualquer brecha de segurança pode virar dor de cabeça. Atenção máxima aos detalhes!"

    # Exibe checklist baseado nos artefatos reais
    "{i}No notebook, você abre o checklist de testes:{/i}"
    show expression "images/ui/checklist_teste_seguranca.png" as checklist at center_zoom
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
        menu:
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

    hide checklist

    # Inclusão da avaliação de conformidade (questionário de maturidade)
    "{i}Antes da reunião de fechamento, [NOME_DEVELOPER_SECURITY] sugere uma autoavaliação rápida usando o modelo de maturidade de privacidade e segurança.{/i}"

    show developer_security serious at right_zoom
    developer_security "Preencha o checklist: cada resposta 'Sim' vale 2 pontos, 'Parcialmente' vale 1, 'Não' ou 'Não sei' valem 0. Use só 'Não se aplica' se realmente não couber ao projeto."
    hide developer_security

    "{i}Você e a equipe respondem perguntas sobre: privacidade de dados,{/i}"
    "{i}práticas de segurança (OWASP, RBAC, backups, criptografia), conformidade legal (LGPD), e governança do projeto.{/i}"
    "{i}O sistema gera automaticamente a pontuação e mostra o nível de maturidade do time, de Inexistente a Excelente.{/i}"

    # Feedback dinâmico do resultado (simulação)
    $ maturidade_percentual = 85   # Exemplo de cálculo fictício, pode ser ramificado depois
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
    developer_quality "Nossa avaliação ficou em [maturidade_percentual]\% — Nível [nivel_maturidade]. Isso mostra como evoluímos desde o início!"
    hide developer_quality

    show developer_security thinking at right_zoom
    developer_security "Privacidade, segurança e testes: quanto mais investirmos, menos riscos teremos no futuro. Mantenham o checklist sempre atualizado!"
    hide developer_security

    # Padding: Revisão coletiva e resolução colaborativa de bugs/vulns
    scene bg escritorio_interior_tarde
    with dissolve
    play sound "audio/effects/ambiente_reuniao.ogg"
    "{i}À tarde, o time se reúne para debater as vulnerabilidades e bugs encontrados, documentando as correções e discutindo oportunidades de melhoria contínua.{/i}"

    # Pequena ramificação: pedir ajuda
    menu:
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

    # Fechamento: Reflexão e estatísticas
    scene bg escritorio_interior_noite
    with fade
    "{i}Fim do expediente: todos comemoram os bugs corrigidos, e a confiança na segurança do sistema cresce. A equipe aprende que maturidade não é só pontuação: é cultura de melhoria contínua e colaboração.{/i}"

    # Feedback final e conquistas
    if bugs_encontrados + vulnerabilidades >= 3:
        "{i}Você desbloqueou a conquista: 'Caçador de Bugs & Vulns'!{/i}"
        $ inventario.append("conquista_bug_vuln")
        play sound "audio/effects/recompensa.ogg"
    elif maturidade_percentual >= 91:
        "{i}Time em nível 'Excelente': conquista 'Guardião da Privacidade e Segurança' adicionada ao inventário!{/i}"
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
