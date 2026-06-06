label scene_14_discussao_arquitetura:
    $ set_available("developer_management", "developer_requirements", "developer_quality", "developer_security")

    play music music_office_concentrated_2 fadein 1.0
    scene bg escritorio_interior_manha
    with fade

    $ advance_minutes(10)
    "{i}Logo cedo, você encontra parte da equipe reunida na sala de reuniões. No quadro branco, rabiscos de fluxos e caixas já começam a aparecer.{/i}"
    play sound "audio/effects/ambiente_reuniao.ogg"

    show developer_project serious at left_zoom
    show developer_coding serious at right_zoom

    developer_project "Hoje vamos definir a arquitetura base do sistema. Toda escolha agora impacta o futuro do projeto — então nada de pressa."
    $ advance_minutes(2)

    show developer_coding neutral at right_zoom
    developer_coding "Sempre digo: o melhor sistema é aquele que a equipe consegue manter. Antes de embarcar em modismos, precisamos garantir estabilidade e clareza."

    show developer_test enthusiastic at center_zoom
    developer_test "E do ponto de vista de testes, quanto mais modular e desacoplado, mais fácil automatizar cenários e detectar bugs!"
    play sound "audio/effects/feedback_positive.ogg"

    $ advance_minutes(4)
    "{i}A conversa esquenta, desenhos de diagramas aparecem no quadro (placeholder: [[Imagem de Diagrama de Componentes]]) enquanto os argumentos se multiplicam.{/i}"

    window hide
    pause 1.0
    window show

    # Discussão sobre modelagem de banco de dados
    show developer_project thinking at left_zoom
    developer_project "Falando em base de dados: para esse projeto, começaria modelando paciente, atendimento, exame, histórico clínico, tentativas de parada, e escala tabágica como tabelas principais."
    show developer_coding serious at right_zoom
    developer_coding "Concordo. Relação um-para-muitos entre paciente e atendimentos; exames referenciam o atendimento e paciente; tabelas de escala podem ficar normalizadas pra facilitar agregações futuras."

    show developer_test confident at center_zoom
    developer_test "E não esqueçam dos relacionamentos: cada registro de evolução clínica pode referenciar um exame ou uma tentativa de parada. E logs de alteração precisam de tabela própria pra rastreabilidade!"
    show developer_ai concentrated at right_zoom2
    developer_ai "Se depois formos fazer análise preditiva, é bom já pensar em timestamp nas tabelas principais. Ajuda na mineração de dados!"
    hide developer_ai

    $ advance_minutes(5)
    show developer_project thinking at left_zoom
    show developer_coding serious at right_zoom
    developer_project "Vocês preferem arquitetura monolítica, mais simples e fácil de entender, ou já querem partir para microsserviços, pensando em escalabilidade futura?"

    developer_coding "Monolito é mais fácil de implantar e debugar. Menos dependências, menos dor de cabeça no início."
    show developer_test thinking at center_zoom
    developer_test "Mas microsserviços facilitam testes independentes, e permitem escalar partes críticas sem mexer no sistema todo!"

    # developer_ai entra, disruptivo
    play sound "audio/effects/abrindo_porta.ogg"
    show developer_ai positive at right_zoom2
    developer_ai "Posso jogar uma ideia? Já pensaram em usar funções serverless para alguns módulos? Baixo custo e atualização super rápida!"

    show developer_coding serious at right_zoom
    developer_coding "Só não vamos reinventar a roda... Cada escolha dessas exige monitoramento e integrações a mais."

    # Player input: decisão arquitetural (flag para próximas cenas)
    menu:
        "Qual abordagem você sugere?"
        "Defendo o monolito, priorizando simplicidade e entrega rápida.":
            $ flag_arquitetura = "monolito"
            show developer_project serious at left_zoom
            developer_project "Vai facilitar o onboarding de quem entrar no projeto. Documentação clara vai ser fundamental!"
            show developer_coding thinking at right_zoom
            developer_coding "Menos armadilhas, menos microgerenciamento. Gosto da sua linha."
            play sound "audio/effects/feedback_positive.ogg"
        "Sugiro microsserviços, pensando na escalabilidade futura.":
            $ flag_arquitetura = "microsservicos"
            show developer_test enthusiastic at center_zoom
            developer_test "Adoro! Vai dar pra brincar com testes automatizados em cada serviço. Vamos caprichar na integração."
            show developer_ai positive at right_zoom2
            developer_ai "Com cloud bem configurada, escalamos cada módulo conforme o uso. Só precisamos de uma boa estratégia de monitoramento."
            play sound "audio/effects/feedback_positive.ogg"
        "Proponho uma abordagem híbrida, com base em modularização progressiva.":
            $ flag_arquitetura = "hibrido"
            show developer_project thinking at left_zoom
            developer_project "Interessante! Podemos começar simples e ir separando módulos críticos aos poucos."
            show developer_coding neutral at right_zoom
            developer_coding "Vai exigir mais revisão, mas pode equilibrar entrega rápida e escalabilidade."
            show developer_ai thinking at right_zoom2
            developer_ai "Gostei. Se precisar automatizar migração, posso ajudar com scripts e pipelines."
            play sound "audio/effects/feedback_positive.ogg"

    "{i}Você faz um esboço no notebook e projeta para o grupo. O diagrama (placeholder) vira o centro da discussão.{/i}"

    # Debate extra: prós e contras (pode exibir dicas)
    show developer_coding serious at right_zoom
    developer_coding "Qualquer escolha tem pontos fortes e fracos. O importante é prever as dificuldades futuras e documentar as decisões."

    show developer_test confident at center_zoom
    developer_test "Lembre de definir critérios de aceitação para arquitetura: integração fácil, cobertura de testes, monitoramento e rollback automatizado."

    show developer_project thinking at left_zoom
    developer_project "E vamos detalhar no banco: índices para CPF, datas de exame e campo ativo para facilitar buscas rápidas. Versionamento de registros é essencial para histórico clínico!"

    $ advance_minutes(8)
    # Passagem do tempo para tarde: mudança de cenário
    hide developer_project
    hide developer_coding
    hide developer_test
    hide developer_ai

    scene bg escritorio_interior_tarde
    with dissolve
    "{i}Horas se passam, a luz do escritório muda. O grupo faz pausas para café e logo todos voltam animados para finalizar os detalhes.{/i}"

    # Pequena interrupção casual
    play sound "audio/effects/cell_vibration.ogg"
    show developer_quality positive at right_zoom2
    developer_quality "(mensagem no chat) Se precisarem de revisão de documentação técnica, me avisem! Quero ver esses diagramas bem feitos!"
    hide developer_quality

    # Feedback de acordo com flag escolhida
    if flag_arquitetura == "monolito":
        show developer_coding positive at right_zoom
        developer_coding "Simples, direto e fácil de evoluir. Só não esqueçam de pensar em boas práticas de versionamento."
        hide developer_coding
    elif flag_arquitetura == "microsservicos":
        show developer_ai enthusiastic at right_zoom2
        developer_ai "Vamos testar integrações automatizadas desde já! Se precisar, já tenho um template pronto para deploy."
        hide developer_ai
    elif flag_arquitetura == "hibrido":
        show developer_project confident at left_zoom
        developer_project "O melhor dos dois mundos, se a equipe estiver alinhada. Bora documentar o plano de migração!"
        hide developer_project

    show developer_test positive at center_zoom
    developer_test "Ótima discussão! Agora, mãos à obra para transformar o que foi decidido em código de verdade."
    hide developer_test

    $ advance_minutes(10)
    "{i}A equipe termina a reunião animada, cada um com novas ideias e tarefas. Você percebe como a discussão técnica aberta e colaborativa faz diferença para o sucesso do projeto.{/i}"

    play music music_office_relaxed fadein 1.5
    scene bg escritorio_interior_noite
    with fade
    "{i}Já é noite quando você finalmente fecha o notebook, satisfeito(a) com o resultado do dia.{/i}"

    return
