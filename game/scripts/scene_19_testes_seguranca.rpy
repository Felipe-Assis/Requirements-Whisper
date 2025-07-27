label scene_19_testes_seguranca:
    # Manhã: início dos testes
    scene bg escritorio_interior_manha
    with dissolve

    play sound "audio/teclado.ogg"
    "{i}Novo dia. O clima no escritório é diferente: hoje o foco é testar e garantir segurança do sistema.{/i}"
    show developer_quality serious at left_zoom
    show developer_security serious at right_zoom

    developer_quality "Vamos começar com o checklist de qualidade. Lembre-se: um sistema pode funcionar, mas só é confiável se passar nos testes."
    developer_security "E qualquer brecha de segurança que passar, pode virar uma dor de cabeça enorme depois. O segredo está nos detalhes."

    "{i}Você recebe um checklist no notebook:{/i}"
    show expression "images/ui/checklist_teste_seguranca.png" as checklist at center_zoom
    window hide
    pause 1.2
    window show

    "{i}Checklist:\n• Testes de unidade\n• Testes de integração\n• Validação de permissões de acesso\n• Testes de injeção (SQL, XSS)\n• Cobertura de código\n• Testes de autenticação/recuperação de senha{/i}"

    # Minigame: seleção de prioridades do checklist
    $ testes_realizados = []
    $ checklist_opcoes = ["unidade", "integracao", "permissoes", "injeção", "cobertura", "autenticacao"]
    $ bugs_encontrados = 0
    $ vulnerabilidades = 0

    $ revisoes = 0
    while revisoes < 3:
        menu:
            "Por onde começar os testes?"
            "Testes de unidade" if "unidade" in checklist_opcoes:
                $ testes_realizados.append("unidade")
                $ checklist_opcoes.remove("unidade")
                show developer_test enthusiastic at right_zoom2
                developer_test "Excelente! Teste de unidade detecta falhas logo de cara. Já achei um bug na função de cadastro!"
                $ bugs_encontrados += 1
                hide developer_test
            "Testes de integração" if "integracao" in checklist_opcoes:
                $ testes_realizados.append("integracao")
                $ checklist_opcoes.remove("integracao")
                hide developer_quality
                show developer_quality positive at left_zoom
                developer_quality "Testes de integração pegam erros de comunicação entre módulos. Boa escolha!"
                hide developer_quality
            "Validação de permissões" if "permissoes" in checklist_opcoes:
                $ testes_realizados.append("permissoes")
                $ checklist_opcoes.remove("permissoes")
                show developer_security thinking at right_zoom
                developer_security "Ótimo! A maioria dos ataques começa por permissão fraca. Detectou que um usuário comum consegue acessar dados do admin. Corrija isso rápido!"
                $ vulnerabilidades += 1
                hide developer_security
            "Testes de injeção" if "injeção" in checklist_opcoes:
                $ testes_realizados.append("injeção")
                $ checklist_opcoes.remove("injeção")
                show developer_security enthusiastic at right_zoom
                developer_security "Essenciais! Ataques de SQL Injection são clássicos. Achou um campo vulnerável, já anotei pra corrigirmos juntos."
                $ vulnerabilidades += 1
                hide developer_security
            "Cobertura de código" if "cobertura" in checklist_opcoes:
                $ testes_realizados.append("cobertura")
                $ checklist_opcoes.remove("cobertura")
                hide developer_quality
                show developer_quality serious at left_zoom
                developer_quality "Cobertura acima de 80\% é o ideal. Se precisar, te ensino a usar a ferramenta do time."
                hide developer_quality
            "Testes de autenticação" if "autenticacao" in checklist_opcoes:
                $ testes_realizados.append("autenticacao")
                $ checklist_opcoes.remove("autenticacao")
                show developer_security neutral at right_zoom
                developer_security "Importante revisar recuperação de senha. Não deixe o link expirar em menos de 10 min, hein!"
                hide developer_security
        $ revisoes += 1

    hide checklist
    hide developer_quality
    hide developer_security

    # Padding: Transição para tarde com revisão coletiva
    scene bg escritorio_interior_tarde
    with fade
    play sound "audio/ambiente_reuniao.ogg"
    "{i}À tarde, o time se reúne para discutir bugs e vulnerabilidades encontradas.{/i}"
    show developer_test thinking at left_zoom
    show developer_quality thinking at right_zoom
    show developer_security serious at center_zoom

    developer_test "Vi que encontrou [bugs_encontrados] bug(s) importante(s). Excelente trabalho investigativo!"
    developer_quality "E o checklist foi bem usado. Reforço: documentar cada falha para evitar regressão!"
    developer_security "Ficaram [vulnerabilidades] vulnerabilidade(s) críticas. Segurança é constante. Recomendo revisar a autenticação com multifator."

    # Opção de pedir ajuda/remoto — ligação para developer_ai ou developer_coding
    menu:
        "Enfrenta dificuldade para corrigir um bug/vulnerabilidade crítica. O que faz?"
        "Liga para [NOME_DEVELOPER_CODING] pedir ajuda em código seguro.":
            show developer_coding serious at right_zoom2
            developer_coding "Se precisar, reviso linha a linha contigo. Prevenção é sempre melhor que remediar."
            hide developer_coding
        "Envia mensagem para [NOME_DEVELOPER_AI] para sugerir automação de testes de segurança.":
            show developer_ai thinking at left_zoom
            developer_ai "Tenho script pra rodar fuzzing automático. Quer que envie por e-mail?"
            hide developer_ai
        "Procura soluções em fóruns técnicos e documentação oficial.":
            "{i}Você encontra boas práticas, mas percebe que compartilhar dúvidas com a equipe acelera o processo.{/i}"

    # Dinâmica de tempo: se encontrou muitos bugs/vuln, pode avançar para noite
    if bugs_encontrados + vulnerabilidades > 2:
        scene bg escritorio_interior_noite
        with fade
        "{i}O tempo passou voando... Você ficou até tarde corrigindo as falhas encontradas. Mas o sistema está mais robusto e seguro!{/i}"
    else:
        "{i}Ainda resta tempo para revisar outros pontos e planejar próximos testes.{/i}"

    # Fechamento e reflexão didática
    show developer_quality positive at left_zoom
    developer_quality "Orgulho do progresso do time! Cada bug encontrado é um problema a menos para o usuário."
    hide developer_quality
    show developer_security positive at right_zoom
    developer_security "Segurança nunca é demais. O segredo é sempre pensar como um atacante — e documentar tudo!"
    hide developer_security

    # Feedback e estatísticas da rodada
    "{i}Resumo dos testes e segurança:{/i}"
    "{i}• Bugs críticos detectados: [bugs_encontrados]{/i}"
    "{i}• Vulnerabilidades encontradas: [vulnerabilidades]{/i}"
    if bugs_encontrados + vulnerabilidades >= 3:
        "{i}Você desbloqueou a conquista: 'Caçador de Bugs & Vulns'!{/i}"
        $ inventario.append("conquista_bug_vuln")
        play sound "audio/recompensa.ogg"

    # Reflexão e fechamento do ciclo
    scene bg quarto_noite
    with fade

    "{i}Em casa, você revisa anotações de aulas sobre testes, segurança e lembra que, na prática, nem sempre os livros mostram o tamanho dos desafios.{/i}"
    "{i}Mas agora está claro: testar, documentar e proteger o sistema são atitudes indispensáveis para qualquer dev.{/i}"

    window hide
    pause 1.1
    window show

    "{i}Fim da Semana 7\n\nAprendizado: Encontrar e corrigir bugs e vulnerabilidades é tão importante quanto escrever código novo. A segurança de um sistema começa nos detalhes e no olhar atento do time.{/i}"

    return
