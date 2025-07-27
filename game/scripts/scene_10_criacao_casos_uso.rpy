label scene_10_criacao_casos_uso:
    scene bg escritorio_interior_manha
    with fade

    "{i}Novo dia, novas tarefas. Você chega cedo ao escritório, determinado(a) a estruturar os primeiros casos de uso do sistema.{/i}"
    "{i}O ambiente está silencioso, exceto pelo som de teclados e o aroma do café recém-passado.{/i}"

    show developer_requirements thinking at left_zoom
    developer_requirements "Bom dia, [player_name]! Que tal começarmos pelos fluxos mais comuns do usuário? Pense nos cenários mais críticos do sistema."

    "{i}Você senta ao lado de [NOME_DEVELOPER_REQUIREMENTS] e abre o notebook. Juntos, começam a mapear os passos do atendimento e do lançamento de exames.{/i}"

    "{i}Depois de algumas ideias anotadas, surge uma dúvida técnica sobre a estrutura de dados ideal para um dos fluxos.{/i}"

    # Interação via notebook com developer_project
    "{i}Você decide enviar uma mensagem rápida para [NOME_DEVELOPER_PROJECT], conhecido por ser direto e eficiente, pedindo uma revisão rápida do diagrama.{/i}"

    show developer_project serious at right_zoom
    developer_project "(mensagem pelo chat) Olhei seu fluxograma. Só cuidado com dependência circular entre módulos. O ideal é separar persistência de dados da lógica de negócios."
    show developer_requirements neutral at left_zoom
    developer_requirements "Ótima observação, [NOME_DEVELOPER_PROJECT]! Essa distinção evita muita dor de cabeça depois."

    hide developer_project

    # Entrada de developer_ai (presencial, curioso)
    show developer_ai positive at right_zoom
    developer_ai "Vocês já pensaram em automatizar parte desse fluxo? Se a gente coletar dados de uso, podemos propor melhorias baseadas em machine learning no futuro!"
    show developer_requirements enthusiastic at left_zoom
    developer_requirements "Olha, seria inovador... Mas vamos primeiro garantir que o básico está sólido."
    hide developer_ai

    # Entrada de developer_test, animando o clima
    show developer_test enthusiastic at right_zoom
    developer_test "Já quero ver esses casos de uso rodando com testes automatizados! Se precisar de ajuda para escrever cenários de teste, me chama!"
    show developer_requirements thinking at left_zoom
    developer_requirements "Essa colaboração vai ser importante na próxima etapa. Obrigada, [NOME_DEVELOPER_TEST]."
    hide developer_test

    # Pausa, interação leve e respiro narrativo
    "{i}Após algumas horas intensas, vocês decidem fazer uma pausa para alongar e conversar.{/i}"
    show developer_requirements neutral at left_zoom
    menu:
        "Durante a pausa, sobre o que você quer conversar com [NOME_DEVELOPER_REQUIREMENTS]?"
        "Pergunto sobre desafios enfrentados em projetos antigos.":
            show developer_requirements serious at left_zoom
            developer_requirements "Já lidei com projetos em que não mapearam cenários críticos. O resultado? Sistema travava sempre que o volume de usuários aumentava. Desde então, sempre reviso casos de uso com calma."
        "Pergunto como manter o time motivado em tarefas repetitivas.":
            show developer_requirements thinking at left_zoom
            developer_requirements "Transparência e celebração das pequenas vitórias ajudam muito. E variar as tarefas sempre que possível."
        "Falo sobre como a universidade está ajudando no trabalho.":
            show developer_requirements positive at left_zoom
            developer_requirements "Legal ouvir isso! Muita gente esquece que a base teórica da faculdade faz diferença no dia a dia."

    # Recebe uma mensagem de developer_quality sugerindo revisão futura
    play sound "audio/cell_vibration.ogg"
    show developer_quality positive at right_zoom
    developer_quality "(mensagem pelo chat) Assim que terminar, me manda esses casos de uso! Vou revisar antes de documentarmos tudo oficialmente :)"
    show developer_requirements enthusiastic at left_zoom
    developer_requirements "Essa revisão em dupla vai garantir um material de qualidade. Equipe colaborativa faz toda a diferença!"

    hide developer_requirements
    hide developer_quality

    scene bg escritorio_interior_tarde
    with dissolve
    "{i}Com os principais fluxos definidos e revisados, você sente que está ganhando ritmo no projeto. As colaborações estão fluindo cada vez melhor.{/i}"

    return
