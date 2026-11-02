label scene_10_criacao_casos_uso:
    # Emily, Lucas e César passam pela mesa; Heitor e Daiana falam pelo chat.
    $ set_available("developer_coding", "developer_management", "developer_project", "developer_quality", "developer_security")

    $ game_hour = 9
    $ game_minute = 10
    play music music_office_concentrated_1 fadein 1.0
    scene bg escritorio_interior_manha
    with fade

    $ advance_minutes(8)
    "{i}Novo dia, novas tarefas. Você chega cedo ao escritório, com vontade de estruturar os primeiros casos de uso do sistema.{/i}"
    "{i}O ambiente está silencioso, exceto pelo som de teclados e o aroma do café recém-passado.{/i}"
    with dissolve

    show developer_requirements thinking at left_zoom
    developer_requirements "Bom dia, [player_name]! Que tal começarmos pelos fluxos mais comuns do usuário? Pense em como o profissional de saúde interage com o sistema logo ao chegar para o atendimento."
    $ advance_minutes(3)

    # Caça à ambiguidade: o rascunho de requisito que saiu da entrevista.
    developer_requirements "Antes, olha esse rascunho que saiu das anotações da entrevista. Se o caso de uso nascer de palavra vaga, ele herda o problema."
    call amb_atividade("saude_amb_historico") from _amb_s10
    show developer_requirements positive at left_zoom
    developer_requirements "Agora dá para testar cada pedaço. E os 3 minutos são uma proposta nossa: a gente confirma com a [NOME_DOUTORA_2] antes de fechar."
    $ advance_minutes(7)

    "{i}Você senta ao lado de [NOME_DEVELOPER_REQUIREMENTS] e abre o notebook. Juntos, começam a mapear os passos do cadastro de pacientes, histórico de saúde e registro de atendimentos.{/i}"

    show item notebook_fechado as notebook at center_zoom
    developer_requirements "Por exemplo, UC1: Cadastro de Paciente. O profissional deve preencher todos os dados de identificação: nome, idade, endereço, profissão, escolaridade, telefone, e por aí vai."
    developer_requirements "O sistema precisa garantir que campos obrigatórios estejam destacados e facilitar o preenchimento — puxando informações anteriores, quando houver."
    hide notebook
    $ advance_minutes(7)

    "{i}Vocês discutem o fluxo principal: profissional logado, acessa 'Novo Paciente', preenche formulário, salva, sistema armazena e confirma. Também anotam exceções: e se faltar conexão? E se faltar campo obrigatório?{/i}"

    show developer_requirements neutral at left_zoom
    developer_requirements "Agora vamos para o UC2, registro do histórico de saúde. O profissional entra no prontuário e preenche detalhes como tratamentos em andamento, uso de medicamentos, gravidez, etc. Campos precisam ser atualizáveis a cada consulta."
    $ advance_minutes(6)

    "{i}Vocês já visualizam os próximos casos de uso essenciais: registro de comorbidades clínicas (UC3), psiquiátricas (UC4), uso de substâncias (UC6, UC7), escalas HAD, AUDIT e Fagerström.{/i}"

    show developer_requirements enthusiastic at left_zoom
    developer_requirements "Detalhe importante: a aplicação da escala HAD (UC5) deve calcular o resultado automaticamente, tanto para ansiedade quanto depressão. E precisa permitir salvar parcialmente, caso o paciente não conclua de primeira."

    # Interação via notebook com developer_project
    $ advance_minutes(3)
    "{i}Durante o mapeamento do fluxo de registro de exames, surge uma dúvida técnica sobre dependências entre módulos.{/i}"
    "{i}Você decide enviar uma mensagem rápida para [NOME_DEVELOPER_PROJECT], conhecido por ser direto e eficiente, pedindo uma revisão do diagrama de entidades.{/i}"

    show developer_project portrait at right_zoom
    developer_project "(mensagem pelo chat) Vi seu fluxograma. Só cuidado para não criar dependência circular entre módulos de pacientes, exames e acompanhamento. Melhor separar a persistência de dados da lógica de negócios."
    show developer_requirements neutral at left_zoom
    developer_requirements "Ótima observação, [NOME_DEVELOPER_PROJECT]! Essa separação é fundamental para facilitar manutenções e evitar bugs futuros."
    hide developer_project
    $ advance_minutes(2)

    # Entrada de developer_ai (presencial, curioso)
    show developer_ai positive at right_zoom
    developer_ai "Vocês já pensaram em usar esses dados para automatizar alertas? Se a gente coletar padrões de evolução clínica, podemos sugerir intervenções com IA ou gerar relatórios inteligentes no futuro!"
    show developer_requirements enthusiastic at left_zoom
    developer_requirements "Seria incrível! Por enquanto, o foco é garantir que o fluxo básico funcione, mas vamos deixar isso anotado como caso de uso desejável, como a integração com o app móvel do ByeByeFumo e a geração automática de indicadores."
    hide developer_ai
    $ advance_minutes(2)

    # Entrada de developer_test, animando o clima
    show developer_test enthusiastic at right_zoom
    developer_test "Já quero ver esses casos de uso rodando com testes automatizados! Quando for mapear os fluxos alternativos e exceções, lembra de detalhar o que acontece em cada cenário — isso ajuda muito na hora de escrever os testes."
    show developer_requirements thinking at left_zoom
    developer_requirements "Colaboração fundamental, [NOME_DEVELOPER_TEST]. Documentar fluxos alternativos e exceções evita falhas depois. Já vou separar para você revisar!"
    hide developer_test

    $ advance_minutes(110)
    "{i}Após algumas horas intensas, vocês decidem fazer uma pausa para alongar e conversar.{/i}"
    show developer_requirements neutral at left_zoom
    menu (tipo="conversa"):
        "Durante a pausa, sobre o que você quer conversar com [NOME_DEVELOPER_REQUIREMENTS]?"
        "Pergunto sobre desafios enfrentados em projetos antigos.":
            show developer_requirements serious at left_zoom
            developer_requirements "Já vi sistemas em que ignoraram fluxos alternativos — resultado: quando o paciente esquecia o CPF, travava todo cadastro! Aprendi a revisar sempre com usuários reais antes de finalizar os casos de uso."
        "Pergunto como manter o time motivado em tarefas repetitivas.":
            show developer_requirements thinking at left_zoom
            developer_requirements "Transparência e celebrar pequenas entregas ajudam muito. E variar tarefas quando possível, pra ninguém ficar sobrecarregado."
        "Falo sobre como a universidade está ajudando no trabalho.":
            show developer_requirements positive at left_zoom
            developer_requirements "Legal ouvir isso! Saber teoria de Engenharia de Software e análise de requisitos faz diferença todo dia, ainda mais quando temos que justificar uma decisão para os stakeholders."
        "Contar o que vi na recepção do ambulatório: um paciente sem CPF, anotado num papel" (tipo="pista") if pista_tem("saude_p_cpf"):
            $ pista_usar("saude_p_cpf")
            show developer_requirements serious at left_zoom
            developer_requirements "Num papel? Então o paciente existe para a recepção e não existe para o sistema. Foi esse buraco que eu já vi travar um cadastro inteiro."
            developer_requirements "Vamos escrever agora: fluxo alternativo do UC1, paciente sem documento. Cadastro provisório com nome, data de nascimento e nome da mãe; o CPF fica pendente e o sistema lembra na próxima visita."
            "{i}O UC1 ganha o fluxo alternativo FA1, com o passo onde começa e como termina. Ao lado, você anota a origem: observação na recepção.{/i}"
            $ add_friendship_point("developer_requirements", 0.5)
    $ advance_minutes(4)

    # Recebe uma mensagem de developer_quality sugerindo revisão futura
    play sound "audio/effects/cell_vibration.ogg"
    show developer_quality positive at right_zoom
    developer_quality "(mensagem pelo chat) Assim que terminar, me manda esses casos de uso! Vou revisar antes de documentarmos tudo oficialmente. Ah, capriche nos fluxos alternativos e exceções!"
    show developer_requirements enthusiastic at left_zoom
    developer_requirements "Equipe colaborativa faz toda a diferença. Essa revisão em dupla vai garantir um material de qualidade!"

    hide developer_requirements
    hide developer_quality

    play music music_office_relaxed fadein 1.5
    scene bg escritorio_interior_tarde
    with dissolve
    $ advance_minutes(15)
    "{i}Com os principais fluxos definidos, revisados e anotados (Cadastro de Paciente, Registro de Histórico, Comorbidades, Escalas, Acompanhamento e Integração), você sente que está ganhando ritmo no projeto.{/i}"
    "{i}As colaborações estão fluindo cada vez melhor e, a cada etapa, o sistema vai ganhando forma nos detalhes.{/i}"
    $ registrar("saude_reg_casos_uso")

    return
