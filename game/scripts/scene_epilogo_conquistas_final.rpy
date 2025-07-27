label scene_epilogo_conquistas_final:
    scene bg tela_conquistas
    with fade

    "Parabéns, [player_name]! Você concluiu o ciclo do projeto e deixou sua marca como engenheiro(a) de software."

    # Tela de conquistas/troféus
    "Veja algumas das conquistas desbloqueadas ao longo do jogo:"

    if "badge_devops" in inventario:
        "🏅 DevOps Visionário — Você liderou a adoção de automação, Docker e pipelines modernos!"
    if "badge_bug_buster" in inventario:
        "🔎 Caçador(a) de Bugs — Detectou e solucionou bugs críticos sob pressão."
    if "badge_team_work" in inventario:
        "🤝 Trabalho em Equipe — Você buscou colaboração nas horas decisivas."
    if "badge_resiliencia" in inventario:
        "🛡️ Resiliência — Priorizou segurança, preferindo rollback seguro a deploy apressado."
    if "selo_codigo_sem_bugs" in inventario:
        "✅ Código sem Bugs — Seu código passou nos testes sem falhas críticas."
    if "conquista_bug_vuln" in inventario:
        "🔐 Segurança de Verdade — Identificou vulnerabilidades e fortaleceu o sistema."
    if "mindfulness_dev" in inventario:
        "🧘 Mindfulness Dev — Soube equilibrar saúde, descanso e produtividade."
    if "badge_pr_transparente" in inventario:
        "📝 PR Transparente — Explicou suas decisões técnicas de modo claro para toda a equipe."
    if "badge_demo_colaborativa" in inventario:
        "🎤 Demo Colaborativa — Apresentou suas soluções e envolveu toda a equipe nas decisões."
    if "checklist_qualidade" in inventario:
        "📋 Mestre dos Checklists — Garantiu qualidade do início ao fim."

    "Se não desbloqueou todos os troféus, que tal jogar novamente e buscar caminhos diferentes?"

    window hide
    pause 1.2
    window show

    # Depoimentos dos NPCs (personalizados, educativos, curtos)
    show developer_coding positive at left_zoom
    developer_coding "Orgulho do seu código, [player_name]! Continue buscando padrões sólidos e clareza."
    hide developer_coding

    show developer_requirements positive at right_zoom
    developer_requirements "Ver você evoluir em requisitos e colaboração me inspira. Que venham mais projetos juntos!"
    hide developer_requirements

    show developer_ai enthusiastic at center_zoom
    developer_ai "Adorei suas ideias inovadoras! Lembre: criatividade com responsabilidade transforma equipes e sistemas."
    hide developer_ai

    show developer_quality positive at left_zoom
    developer_quality "Você mostrou que qualidade é hábito, não exceção. Mantenha esse espírito na sua carreira!"
    hide developer_quality

    show developer_test enthusiastic at right_zoom
    developer_test "Aprender testando é o caminho! Espero encontrar seus códigos bem testados por aí."
    hide developer_test

    show developer_management positive at left_zoom
    developer_management "Gestão é sobre pessoas e processos — e você mostrou maturidade em ambos. Sucesso!"
    hide developer_management

    show developer_project thinking at right_zoom
    developer_project "Documentação, arquitetura, deploy... Você venceu cada etapa. Torcendo pelo seu próximo desafio."
    hide developer_project

    show developer_security positive at center_zoom
    developer_security "Você nunca esqueceu da segurança. O mundo precisa de devs assim. Parabéns!"
    hide developer_security

    # Reflexão final do protagonista e sugestão de replay
    scene bg quarto_noite
    with fade
    "Você sente orgulho de sua jornada, das amizades e de tudo que construiu — mas sabe que sempre há espaço para crescer."

    "Cada escolha levou a um final diferente. Que tal experimentar outros caminhos, focar em outras competências ou explorar alternativas técnicas na próxima vez?"

    "Obrigado por jogar! Continue aprendendo, colaborando e desenvolvendo — dentro e fora dos projetos."

    menu:
        "O que deseja fazer agora?"
        "Jogar novamente (novo ciclo, novos desafios)":
            jump start
        "Ver créditos finais":
            jump creditos_finais
        "Encerrar":
            return

label creditos_finais:
    scene bg creditos
    with fade
    "Projeto desenvolvido como Visual Novel Educacional em Engenharia de Software."
    "Roteiro: [Seu Nome] | Arte: [Equipe/IA/Créditos] | Programação: [Seu Nome] | Personagens e história inspirados em vivências reais."
    "Agradecimentos especiais aos colegas, professores e todos que colaboraram direta ou indiretamente."
    "Obrigado por jogar!"
    return
