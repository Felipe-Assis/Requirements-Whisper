label scene_6_entrevista_stakeholders:

    play music music_office_relaxed fadein 1.0
    scene bg sala_reuniao_manha
    with fade

    $ advance_minutes(5)
    "{i}Você e [NOME_DEVELOPER_REQUIREMENTS] se acomodam na sala de reuniões. O ambiente é iluminado, com uma mesa oval, quadro branco e algumas xícaras de café espalhadas.{/i}"
    with dissolve
    "{i}Pouco depois, as médicas — suas stakeholders — chegam, trazendo consigo uma pilha de papéis e aquele olhar de quem já viveu muitos plantões.{/i}"
    $ advance_minutes(3)
    with dissolve

    show developer_requirements neutral at left_zoom
    show doutora_1 neutral at center_zoom
    show doutora_2 neutral at right_zoom

    developer_requirements "Doutoras, este é nosso novo integrante da equipe de desenvolvimento. Hoje vamos conversar sobre as necessidades do sistema."
    $ advance_minutes(2)
    with dissolve

    doutora_1 "Prazer, [player_name]. Espero que estejam prontos para ouvir, porque já passamos por muitos sistemas problemáticos..."
    doutora_2 "Se servir café eu fico mais calma, viu? (risos) Mas falando sério, a rotina aqui é puxada, precisamos de algo que nos ajude de verdade."
    hide developer_requirements
    $ advance_minutes(2)
    with dissolve

    "{i}Você abre o notebook, o roteiro da entrevista e o formulário de história clínica à mão. O clima é de expectativa. É sua chance de mostrar atenção e coletar os requisitos certos.{/i}"
    with dissolve

    # PRIMEIRA PERGUNTA
    menu:
        "Como você começa a entrevista?"
        "Peço para descreverem um dia típico de trabalho usando o sistema atual.":
            $ add_friendship_point("doutora_2", 1)
            doutora_2 "Ótimo ponto! Olha, já começo o dia cadastrando novos pacientes: preciso preencher todos os dados de identificação — é muita coisa, e o sistema deveria facilitar, puxando info de visitas anteriores, por exemplo."
            doutora_2 "Depois, preciso registrar evoluções, incluir exames recebidos, checar as notificações de pendências e acompanhar as tentativas de parada dos pacientes."
            doutora_1 "No meu caso, uso os relatórios clínicos para reuniões com a diretoria e pesquisas. Preciso de acesso fácil aos gráficos, filtros por estágio motivacional e carga tabágica, e exportação em PDF ou Excel."
            doutora_2 "E no meio disso tudo ainda tenho que lidar com sistema travando, perda de conexão ou campos obrigatórios mal sinalizados!"
        "Pergunto quais funções sentem mais falta no sistema.":
            $ add_friendship_point("doutora_1", 1)
            doutora_1 "Falta integração real com o laboratório, para os resultados aparecerem automaticamente no prontuário. E seria ótimo se o sistema calculasse sozinho a carga tabágica e os escores de escalas como HAD e AUDIT."
            doutora_2 "Sinto muita falta de alertas — avisos de acompanhamento, exames pendentes, retornos dos pacientes. Também seria bom um campo para registrar tentativas de parada e recaídas, e um lugar para anexar documentos."
        "Quero saber qual foi o maior problema enfrentado nos últimos meses.":
            doutora_2 "Uma vez o sistema travou e perdi todo o preenchimento do histórico atual de saúde. Precisa ter autosave e indicar claramente quais campos são obrigatórios."
            doutora_1 "O maior problema foi quando, na pressa, alguém preencheu dados errados e depois não conseguimos rastrear quem fez a alteração. Logs e auditoria são essenciais!"

    $ advance_minutes(5)
    with dissolve

    "{i}Enquanto vocês conversam, as doutoras trocam opiniões sobre prioridades do sistema, mostrando diferentes pontos de vista sobre o que é mais crítico.{/i}"
    doutora_1 "Dra. [NOME_DOUTORA_2], você acha mesmo que notificações são prioridade? Para mim, relatórios e dashboards vêm primeiro, especialmente para acompanhamento dos indicadores e prestação de contas."
    doutora_2 "Relatórios são importantes, doutora, mas sem avisos eu deixo passar coisa urgente no plantão! Preciso saber rapidamente sobre exames, consultas de retorno e situações de risco."
    show developer_requirements neutral at left_zoom
    developer_requirements "Parece que precisamos atender bem ambos os lados. O que você acha, [player_name]?"
    hide developer_requirements
    with dissolve

    menu:
        "Sua opinião pode influenciar o foco dos requisitos."
        "Priorizar notificações, mas sem esquecer relatórios.":
            $ add_friendship_point("doutora_2", 1)
            $ add_friendship_point("doutora_1", 1)
            show developer_requirements enthusiastic at left_zoom
            developer_requirements "Boa solução! Vamos equilibrar essas demandas no levantamento, pensando em fluxos práticos para cada perfil de usuário."
            hide developer_requirements
        "Concordo com a [NOME_DOUTORA_1], relatórios bem feitos são essenciais.":
            $ add_friendship_point("doutora_1", 1)
            doutora_1 "Finalmente alguém me entende! Um sistema sem indicadores clínicos e relatórios personalizáveis perde o sentido, inclusive para prestação de contas e publicações científicas."
            doutora_2 "Só não me deixe de fora, hein? Preciso dos avisos de rotina!"
        "Concordo com a [NOME_DOUTORA_2], notificações são urgentes para o dia a dia.":
            $ add_friendship_point("doutora_2", 1)
            doutora_2 "Obrigada! Sem avisos a rotina não funciona — esqueço retornos e exames pendentes."
            doutora_1 "Mas preciso dos relatórios para validar dados, principalmente nas pesquisas."

    $ advance_minutes(4)
    with dissolve

    "{i}Você aproveita para aprofundar as perguntas, consultando o questionário clínico e os documentos de requisitos, anotando tudo no notebook.{/i}"

    # SEGUNDA RODADA — MAIS ADERENTE AOS ARTEFATOS
    menu:
        "Pergunta adicional:"
        "Sobre o cadastro do paciente: há campos que julgam desnecessários, difíceis ou que faltam?" :
            doutora_2 "Alguns campos de endereço poderiam ser automáticos. Falta também um lugar para registrar profissão e escolaridade direito. E os campos obrigatórios deviam estar mais destacados."
            doutora_1 "Eu gostaria que tivesse checagem automática para CPF ou número de registro, pra evitar duplicidade. Também facilitar exportar só alguns campos quando preciso montar relatórios para pesquisa."
        "Como lidam com histórico de saúde, comorbidades e psiquiatria?":
            doutora_1 "É difícil manter tudo atualizado. Precisamos que o sistema sugira preenchimento com base em consultas passadas e permita anexar exames digitalizados. A parte de comorbidades psiquiátricas e aplicação de escalas como HAD e AUDIT ainda é muito manual."
            doutora_2 "Muita coisa ainda é anotada no papel e depois preciso digitalizar. Seria ótimo anexar arquivos diretamente e marcar a última atualização do histórico."
        "Sobre uso de outras substâncias, álcool e tabagismo: algum ponto crítico?":
            doutora_2 "Preciso de alertas para pacientes em risco por uso de álcool ou outras drogas, com campos específicos para frequência, quantidade e tentativas de parar."
            doutora_1 "Seria útil um gráfico de evolução do consumo e registro automático da carga tabágica, para monitorar quem está conseguindo reduzir ou parou de fumar."
        "Querem logs e auditoria detalhada?":
            doutora_1 "Com certeza. Precisamos saber quem editou cada campo e quando. Auditoria detalhada evita confusão, principalmente em casos de inconsistências nos dados."
            doutora_2 "Facilita muito em plantões: cada vez que acesso ou altero um registro, quero ver o histórico ali na tela."

    $ advance_minutes(8)
    with dissolve

    "{i}Você faz perguntas finais sobre escalas automáticas (HAD, AUDIT, Fagerström), integração com app, backups, e acompanhamento longitudinal dos pacientes.{/i}"
    doutora_2 "A escala HAD é essencial para acompanhamento. Se puder ser aplicada e calculada direto no sistema, economiza muito tempo!"
    doutora_1 "Cálculo automático da carga tabágica também é prioridade. E queria integração com o app Adeus Cigarro para puxar dados de recaídas e consumo em tempo real."
    doutora_2 "Se possível, implementar autosave e backup frequente, porque ninguém merece perder tudo no meio do plantão!"
    doutora_1 "E no acompanhamento, um painel longitudinal mostrando evolução dos principais indicadores por paciente facilitaria o monitoramento clínico."

    show developer_requirements enthusiastic at left_zoom
    developer_requirements "Muito bom, [player_name]. Suas perguntas foram ótimas! Agora vamos organizar esses pontos e preparar a próxima etapa do projeto."
    hide developer_requirements

    $ advance_minutes(5)
    with dissolve

    "{i}Ao final, as doutoras se levantam e, sorrindo, pegam o celular.{/i}"
    show doutora_1 neutral at center_zoom
    show doutora_2 neutral at right_zoom
    doutora_1 "Se surgir qualquer dúvida, pode me chamar pelo app, viu? Prefiro resolver as coisas direto com quem está na linha de frente do sistema."
    doutora_2 "Exatamente! Pode contar comigo também, [player_name]. Quanto mais alinhados estivermos, melhor será o resultado final para todo mundo."
    $ add_contact("doutora_1")
    $ add_contact("doutora_2")
    hide doutora_1
    hide doutora_2
    with dissolve

    play music music_streets_focused fadein 0.8
    scene transito_tarde
    with fade
    "{i}Você retorna para sua mesa, sentindo que a entrevista foi produtiva e que já aprendeu muito sobre a importância de ouvir todos os envolvidos.{/i}"
    "Anota rapidamente os pontos principais no notebook antes de seguir para a próxima atividade."

    return
