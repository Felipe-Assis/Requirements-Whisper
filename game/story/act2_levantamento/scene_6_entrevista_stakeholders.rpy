label scene_6_entrevista_stakeholders:
    # Emily está na sala com as doutoras; o resto da equipe pode receber mensagem.
    # As doutoras só viram contato no fim da cena.
    $ set_available("developer_ai", "developer_coding", "developer_management", "developer_project", "developer_quality", "developer_security", "developer_test")

    play music music_office_relaxed fadein 1.0
    scene bg escritorio_medica
    with fade

    $ advance_minutes(5)
    "{i}No Instituto, uma secretária leva você e [NOME_DEVELOPER_REQUIREMENTS] até a sala das médicas: estantes cheias de pastas, duas mesas cobertas de papéis e uma janela que dá para o jardim.{/i}"
    "{i}Pouco depois, as médicas — suas stakeholders — chegam, com uma pilha de fichas e aquele olhar de quem já viveu muitos plantões.{/i}"
    $ advance_minutes(3)

    show developer_requirements neutral at left_zoom
    show doutora_1 neutral at center_zoom
    show doutora_2 neutral at right_zoom
    with dissolve

    developer_requirements "Doutoras, quero apresentar [player_name], que acabou de entrar na nossa equipe de desenvolvimento. Hoje a ideia é ouvir vocês."
    $ advance_minutes(2)

    doutora_1 "Prazer, [player_name]. Espero que estejam prontos para ouvir, porque já passamos por muitos sistemas problemáticos..."
    doutora_2 "Se servir café eu fico mais calma, viu? (risos) Mas falando sério, a rotina aqui é puxada. Precisamos de algo que ajude de verdade."
    $ advance_minutes(2)

    "{i}Você abre o notebook com o roteiro da entrevista e o formulário de história clínica. É sua chance de ouvir com atenção e entender o que elas precisam.{/i}"

    # PRIMEIRA PERGUNTA: abrir pedindo um episódio concreto.
    menu:
        "Como você começa a entrevista?"
        "Pergunto quais funções elas gostariam de ter no sistema novo.":
            $ decisao("saude_d6_abertura", False)
            show developer_requirements thinking at left_zoom
            developer_requirements "(baixinho) Uma lista de funções ajuda, mas cada pedido chega sem o motivo. Sem saber o problema por trás, a gente pode construir a função errada."
        "Peço que contem uma situação recente em que o sistema atual atrapalhou o atendimento.":
            if decisao("saude_d6_abertura", True):
                $ add_friendship_point("doutora_2", 1)
        "Pergunto se preferem um sistema com uma tela só ou com várias abas.":
            $ decisao("saude_d6_abertura", False)
            show developer_requirements thinking at left_zoom
            developer_requirements "(baixinho) Essa pergunta já traz a solução pronta. Elas podem escolher uma das opções sem contar o que realmente atrapalha."

    if not aprendizagem.get("saude_d6_abertura"):
        menu:
            "Como você reformula a pergunta?"
            "Doutoras, podem me contar a última vez em que o sistema atrapalhou um atendimento?":
                pass

    doutora_2 "Tenho uma bem fresca. Semana passada, no meio do plantão, o sistema travou enquanto eu preenchia o histórico de saúde de um paciente."
    doutora_2 "Perdi tudo. Tive que refazer a entrevista com ele, com a sala de espera cheia. E nem dava para saber quais campos eram obrigatórios antes de salvar."
    doutora_1 "O meu caso é outro. Um dado de consumo saiu errado no relatório da diretoria, e ninguém conseguiu descobrir quem tinha mudado o registro, nem quando."
    doutora_1 "Passei dois dias conferindo fichas de papel para corrigir os números."
    $ advance_minutes(4)

    show developer_requirements positive at left_zoom
    if aprendizagem.get("saude_d6_abertura"):
        developer_requirements "Viu como um caso real rende? Já sabemos quem sofre, o que acontece e o que se perde."
    else:
        developer_requirements "Agora sim. Com um caso real, sabemos quem sofre, o que acontece e o que se perde."
    "{i}Você anota: salvar automaticamente durante o preenchimento, mostrar os campos obrigatórios antes de salvar, registrar quem alterou cada dado e quando.{/i}"

    "{i}Você aproveita e pede que contem também como é um dia comum.{/i}"
    doutora_2 "Começo cadastrando pacientes novos. São muitos dados de identificação, e o sistema podia puxar o que já existe das visitas anteriores."
    doutora_2 "Depois registro evoluções, incluo exames, confiro pendências e acompanho as tentativas de parar de fumar."
    doutora_1 "Eu uso os relatórios clínicos nas reuniões com a diretoria e nas pesquisas. Preciso de filtros por estágio motivacional e por carga tabágica, e de exportar em PDF ou Excel. Hoje, exportar é um sofrimento."
    $ advance_minutes(5)

    "{i}Enquanto vocês conversam, as doutoras trocam opiniões sobre o que é mais urgente no sistema.{/i}"
    doutora_1 "[NOME_DOUTORA_2], você acha mesmo que notificações são prioridade? Para mim, relatórios e painéis vêm primeiro, por causa dos indicadores e da prestação de contas."
    doutora_2 "Relatórios são importantes, doutora, mas sem avisos eu deixo passar coisa urgente no plantão! Preciso saber rápido de exames, retornos e situações de risco."
    show developer_requirements thinking at left_zoom
    developer_requirements "Parece que precisamos atender bem os dois lados. O que você acha, [player_name]?"

    menu:
        "Sua opinião pode influenciar o foco dos requisitos."
        "Priorizar notificações, mas sem esquecer relatórios.":
            $ add_friendship_point("doutora_2", 1)
            $ add_friendship_point("doutora_1", 1)
            show developer_requirements enthusiastic at left_zoom
            developer_requirements "Boa solução! Vamos equilibrar essas demandas no levantamento, pensando em fluxos práticos para cada perfil de usuário."
        "Concordo com a [NOME_DOUTORA_1], relatórios bem feitos são essenciais.":
            $ add_friendship_point("doutora_1", 1)
            doutora_1 "Finalmente alguém me entende! Um sistema sem indicadores clínicos e relatórios personalizáveis perde o sentido, inclusive para prestação de contas e publicações científicas."
            doutora_2 "Só não me deixe de fora, hein? Preciso dos avisos de rotina!"
        "Concordo com a [NOME_DOUTORA_2], notificações são urgentes para o dia a dia.":
            $ add_friendship_point("doutora_2", 1)
            doutora_2 "Obrigada! Sem avisos a rotina não funciona — esqueço retornos e exames pendentes."
            doutora_1 "Mas preciso dos relatórios para validar dados, principalmente nas pesquisas."

    $ advance_minutes(4)

    # SEGUNDA RODADA: esclarecer uma palavra ambígua.
    "{i}Você volta ao cadastro, que apareceu na fala das duas.{/i}"
    doutora_2 "No fim das contas, o que eu queria mesmo é um cadastro mais prático."

    menu:
        "O que fazer com a palavra \"prático\"?"
        "Anoto \"o cadastro deve ser prático\" e deixo a equipe decidir o que isso quer dizer.":
            $ decisao("saude_d6_ambiguidade", False)
            show developer_requirements thinking at left_zoom
            developer_requirements "(baixinho) Cada pessoa da equipe vai entender \"prático\" de um jeito, e a doutora de outro. Melhor descobrir agora o que ela espera."
        "Sugiro um cadastro mais moderno, com menos campos na tela.":
            $ decisao("saude_d6_ambiguidade", False)
            show developer_requirements thinking at left_zoom
            developer_requirements "(baixinho) Isso já é uma solução, e pode cortar campos que o atendimento exige. E \"moderno\" é tão vago quanto \"prático\"."
        "Pergunto o que ela precisa conseguir fazer no cadastro que hoje não consegue.":
            $ decisao("saude_d6_ambiguidade", True)

    if not aprendizagem.get("saude_d6_ambiguidade"):
        menu:
            "Como você esclarece o pedido?"
            "Doutora, o que mais toma seu tempo no cadastro hoje? O que precisaria mudar?":
                pass

    doutora_2 "Digitar de novo o que o sistema já tem das visitas anteriores. O endereço podia completar pelo CEP. E quero ver os campos obrigatórios marcados antes de clicar em salvar, não depois."
    doutora_1 "E o sistema avisar quando o CPF já estiver cadastrado. Hoje temos paciente duplicado, com o histórico dividido em duas fichas."
    show developer_requirements positive at left_zoom
    developer_requirements "Agora \"prático\" virou coisas que dá para conferir: dados reaproveitados, endereço pelo CEP, obrigatórios visíveis e aviso de CPF duplicado."
    $ advance_minutes(4)

    "{i}Você consulta o questionário clínico para aproveitar o tempo que resta.{/i}"

    menu:
        "O que mais você quer entender?"
        "Como lidam com histórico de saúde, comorbidades e psiquiatria?":
            doutora_1 "É difícil manter tudo atualizado. O sistema podia sugerir o preenchimento com base nas consultas passadas e aceitar exames digitalizados. A parte de comorbidades psiquiátricas e das escalas HAD e AUDIT ainda é muito manual."
            doutora_2 "Muita coisa ainda é anotada no papel e depois preciso digitar. Seria ótimo anexar arquivos e ver a data da última atualização do histórico."
        "Sobre uso de outras substâncias, álcool e tabagismo: algum ponto crítico?":
            doutora_2 "Preciso de alertas para pacientes em risco por uso de álcool ou outras drogas, com campos para frequência, quantidade e tentativas de parar."
            doutora_1 "Seria útil um gráfico da evolução do consumo, para ver quem está conseguindo reduzir ou parou de fumar."

    $ advance_minutes(8)

    "{i}Você faz perguntas finais sobre escalas automáticas (HAD, AUDIT, Fagerström), integração com o app, backups e acompanhamento dos pacientes ao longo do tempo.{/i}"
    doutora_2 "A escala HAD é essencial para o acompanhamento. Se puder ser aplicada e calculada direto no sistema, economiza muito tempo!"
    doutora_1 "O cálculo automático da carga tabágica também é prioridade. E queria integração com o app móvel do ByeByeFumo, para puxar dados de recaídas e consumo em tempo real."
    doutora_2 "E backup frequente, porque ninguém merece perder tudo no meio do plantão de novo!"
    doutora_1 "No acompanhamento, um painel mostrando a evolução dos principais indicadores de cada paciente facilitaria muito."

    show developer_requirements enthusiastic at left_zoom
    developer_requirements "Muito bom, [player_name]. Saímos daqui com casos reais, não só com uma lista de desejos. Agora é organizar tudo para a próxima etapa."
    $ advance_minutes(5)

    "{i}Ao final, as doutoras se levantam e pegam o celular.{/i}"
    doutora_1 "Se surgir qualquer dúvida, pode me chamar pelo app, viu? Prefiro resolver as coisas direto com quem está na linha de frente do sistema."
    doutora_2 "Exatamente! Pode contar comigo também, [player_name]. Ah, e se der, deixa a tela inicial verdinha? Combina com saúde. (risos)"
    $ add_contact("doutora_1")
    $ add_contact("doutora_2")
    hide developer_requirements
    hide doutora_1
    hide doutora_2
    with dissolve

    play music music_streets_focused fadein 0.8
    scene bg transito_tarde
    with fade
    $ advance_minutes(20)
    "{i}No ônibus de volta para o escritório, você relê as anotações. A entrevista rendeu mais do que o roteiro previa, e quase tudo de importante veio das histórias que elas contaram.{/i}"
    $ registrar("saude_reg_entrevista")
    "{i}Você marca os pontos principais no notebook antes de chegar.{/i}"

    return
