# Acordo da negociação de escopo (integração com o app Adeus Cigarro):
# "base_primeiro" ou "investigar_agora". Lido em scene_16 e scene_21.
default s14_acordo_escopo = ""

label scene_14_discussao_arquitetura:
    $ set_available("developer_management", "developer_requirements", "developer_quality", "developer_security")

    play music music_office_concentrated_2 fadein 1.0
    scene bg escritorio_interior_manha
    with fade

    $ set_time(9, 0)
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
    if energia_cansaco():
        developer_test "(baixinho) Tá com cara de sono, [player_name]. Pega um café; essa discussão vai longe."

    $ advance_minutes(4)
    "{i}A conversa esquenta. No quadro, caixas e setas ligam cadastro, prontuário, escalas e relatórios, enquanto os argumentos se multiplicam.{/i}"

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
    menu (tipo="trabalho"):
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

    $ registrar("saude_reg_arquitetura")
    "{i}Você faz um esboço no notebook e projeta para o grupo: os módulos, o banco e por onde passam os dados do paciente. O diagrama vira o centro da discussão.{/i}"

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
    $ set_time(14, 0)
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

    # Pedido de mudança no meio da entrega: integração com o app Adeus Cigarro
    # (citado pela doutora na entrevista e anotado como desejável nos casos de uso).
    $ advance_minutes(25)
    play sound "audio/effects/cell_vibration.ogg"
    "{i}No meio da tarde, chega uma chamada de vídeo do Instituto. [NOME_DEVELOPER_PROJECT] passa a chamada para o telão da sala.{/i}"
    show doutora_1 neutral at right_zoom
    show developer_coding serious at left_zoom
    with dissolve
    doutora_1 "Boa tarde, pessoal. Vou ser rápida, que tenho ambulatório daqui a pouco."
    doutora_1 "Lembram do app Adeus Cigarro? Muitos pacientes já usam. Quero que o sistema puxe de lá as recaídas e o consumo de cada um, já nesta primeira entrega."
    developer_coding "Doutora, a ideia é boa. Mas o app é de outra empresa: precisamos de autorização, de acesso aos dados, e ninguém aqui conhece essa API ainda."
    developer_coding "Se a integração entrar agora, o tempo sai do autosave do histórico e do cálculo das escalas. Justamente o que vocês pediram primeiro."
    doutora_1 "Eu entendo. Mas hoje eu passo horas copiando esses números à mão para as planilhas da pesquisa."
    "{i}Os olhares se voltam para você. Como o pedido vai ser conduzido?{/i}"

    $ s14_acordo_escopo = ""
    while not s14_acordo_escopo:
        menu (tipo="negociacao"):
            "Como você conduz o pedido da [NOME_DOUTORA_1]?"
            "Aceitar a integração e manter o prazo, sem falar da capacidade da equipe.":
                $ decisao("saude_negociacao_escopo", False)
                show developer_coding serious at left_zoom
                developer_coding "Para caber no prazo, eu teria que cortar os testes do autosave. Não dá para prometer as duas coisas com segurança."
                show doutora_1 serious at right_zoom
                doutora_1 "Então eu ganharia um recurso novo e continuaria perdendo histórico no meio do plantão? Assim não serve."
                "{i}Prometer tudo sem olhar a capacidade só empurra o problema para a véspera da entrega. Vale pensar de novo.{/i}"
            "Recusar, porque a integração não estava na especificação.":
                $ decisao("saude_negociacao_escopo", False)
                doutora_1 "A especificação foi escrita semana passada. A necessidade não some só porque ninguém anotou."
                show developer_coding thinking at left_zoom
                developer_coding "Ela tem razão. Requisito pode mudar. O que a gente precisa é deixar claro o efeito da mudança e combinar a prioridade."
                "{i}Recusar sem conversa fecha a porta para uma necessidade real. Vale pensar de novo.{/i}"
            "Entregar primeiro o autosave e as escalas; investigar a integração na próxima rodada.":
                $ decisao("saude_negociacao_escopo", True)
                doutora_1 "Tudo bem. Sigo com as planilhas por enquanto, mas quero participar dessa investigação."
                show developer_coding positive at left_zoom
                developer_coding "Combinado. Mantemos o que já foi especificado e testado. A integração fica registrada para investigar, sem data prometida."
                "Acordo proposto: a primeira entrega mantém o autosave do histórico e o cálculo das escalas. Na rodada seguinte, a equipe e a [NOME_DOUTORA_1] investigam a integração com o Adeus Cigarro antes de estimar uma data."
                menu (tipo="negociacao"):
                    "[NOME_DOUTORA_1] e [NOME_DEVELOPER_CODING] conferem o registro."
                    "Confirmar o acordo com os dois.":
                        $ s14_acordo_escopo = "base_primeiro"
                    "Rever o acordo antes de confirmar.":
                        pass
            "Investigar a integração agora e renegociar a data da primeira entrega.":
                $ decisao("saude_negociacao_escopo", True)
                doutora_1 "Prefiro esperar alguns dias a receber o sistema sem isso. Enquanto vocês investigam, sigo com as planilhas."
                show developer_coding thinking at left_zoom
                developer_coding "Vou ver o que a API oferece, que autorizações precisamos e quanto esforço dá. Investigar não garante que a integração seja viável, viu?"
                "Acordo proposto: a equipe investiga agora a integração com o Adeus Cigarro. A [NOME_DOUTORA_1] aceita adiar a primeira entrega; a nova data só será combinada depois da investigação, sem cortar o autosave nem as escalas."
                menu (tipo="negociacao"):
                    "[NOME_DOUTORA_1] e [NOME_DEVELOPER_CODING] conferem o registro."
                    "Confirmar o acordo com os dois.":
                        $ s14_acordo_escopo = "investigar_agora"
                    "Rever o acordo antes de confirmar.":
                        pass

    show developer_coding neutral at left_zoom
    developer_coding "Com o efeito e a prioridade anotados, a equipe sabe o que está assumindo."
    doutora_1 "E eu sei o que ainda vou ter que fazer à mão enquanto isso. Obrigada pela franqueza."
    hide doutora_1
    hide developer_coding
    with dissolve

    show developer_test positive at center_zoom
    with dissolve
    developer_test "Ótima discussão! Agora, mãos à obra para transformar o que foi decidido em código de verdade."
    hide developer_test
    with dissolve

    $ advance_minutes(40)
    "{i}A equipe termina a reunião animada, cada um com novas ideias e tarefas. Você percebe como a discussão técnica aberta e colaborativa faz diferença para o sucesso do projeto.{/i}"

    play music music_office_relaxed fadein 1.5
    scene bg escritorio_interior_noite
    with fade
    $ set_time(19, 10)
    "{i}Já é noite quando você finalmente fecha o notebook, com a sensação de que o dia rendeu.{/i}"

    return
