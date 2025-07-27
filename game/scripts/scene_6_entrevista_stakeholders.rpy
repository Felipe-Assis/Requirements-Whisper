label scene_6_entrevista_stakeholders:
    scene bg sala_reuniao_manha
    with fade

    "Você e [NOME_DEVELOPER_REQUIREMENTS] se acomodam na sala de reuniões. O ambiente é iluminado, com uma mesa oval, quadro branco e algumas xícaras de café espalhadas."
    "Pouco depois, os stakeholders chegam."

    show developer_requirements neutral at left_zoom
    show dr_almeida neutral at center_zoom
    show enf_marta neutral at right_zoom

    developer_requirements "Dr. Almeida, Enfermeira Marta, este é nosso novo integrante da equipe de desenvolvimento. Hoje vamos conversar sobre as necessidades do sistema."

    dr_almeida "Prazer, [player_name]. Espero que estejam prontos para ouvir, porque já passamos por muitos sistemas problemáticos..."
    enf_marta "Se servir café eu fico mais calma, viu? (risos) Mas falando sério, a rotina aqui é puxada, precisamos de algo que nos ajude de verdade."

    hide developer_requirements

    "Você abre o notebook e inicia a entrevista. O clima é de expectativa. É sua chance de mostrar atenção e coletar os requisitos certos."

    # PRIMEIRA PERGUNTA
    menu:
        "Como você começa a entrevista?"
        "Peço para descreverem um dia típico de trabalho usando o sistema atual.":
            $ amizade_enf_marta += 1
            enf_marta "Ótimo ponto! Olha, no começo do dia já preciso lançar os atendimentos, checar exames e preencher fichas digitais. Tudo tem que ser rápido, não posso perder tempo com telas lentas."
            dr_almeida "É, e do meu lado, preciso acessar relatórios para reuniões. Várias vezes encontro erros nos dados ou demora no carregamento."
        "Pergunto quais funções sentem mais falta no sistema.":
            $ amizade_dr_almeida += 1
            dr_almeida "Eu sinto falta de filtros avançados em relatórios e exportação fácil de dados. Hoje é tudo travado, depende da TI."
            enf_marta "No meu caso, queria notificações automáticas e que os avisos fossem mais visíveis. Às vezes esqueço exames, aí já viu, né?"
        "Quero saber qual foi o maior problema enfrentado nos últimos meses.":
            enf_marta "Uma vez o sistema travou no meio de um plantão... Quase perdi um exame de um paciente grave."
            dr_almeida "Já tive que explicar para a diretoria porque relatórios estavam incompletos. Perdi a confiança nos relatórios automáticos."

    # INTERVENÇÃO ENTRE OS STAKEHOLDERS
    "Enquanto vocês conversam, Dr. Almeida e Marta trocam opiniões sobre as prioridades do sistema."
    dr_almeida "Marta, você acha mesmo que notificações são prioridade? Pra mim, relatórios vêm primeiro."
    enf_marta "Relatórios são importantes, doutor, mas sem avisos eu deixo passar coisa urgente no plantão!"
    developer_requirements "Parece que precisamos atender bem ambos os lados. O que você acha, [player_name]?"

    menu:
        "Sua opinião pode influenciar o foco dos requisitos."
        "Priorizar notificações, mas sem esquecer relatórios.":
            $ amizade_enf_marta += 1
            $ amizade_dr_almeida += 1
            developer_requirements "Boa solução! Vamos equilibrar essas demandas no levantamento."
        "Concordo com o doutor, relatórios bem feitos são essenciais.":
            $ amizade_dr_almeida += 1
            dr_almeida "Finalmente alguém me entende!"
            enf_marta "Só não me deixe de fora, hein?"
        "Concordo com Marta, notificações são urgentes para o dia a dia.":
            $ amizade_enf_marta += 1
            enf_marta "Obrigada! Se não tiver aviso, tudo desanda."
            dr_almeida "Mas preciso dos relatórios, hein?"

    # SEGUNDA RODADA DE PERGUNTAS
    "Você aproveita para aprofundar as perguntas enquanto anota tudo no notebook."

    menu:
        "Pergunta adicional:"
        "Quais telas mais usam e o que mudariam nelas?":
            enf_marta "Uso muito a tela de cadastro e consulta de pacientes. Queria que fosse mais simples, menos cliques."
            dr_almeida "No meu caso, uso gráficos de desempenho. Se pudesse personalizar os indicadores seria ótimo."
        "Gostaria de saber sobre integrações: precisam que o sistema converse com outros softwares?":
            dr_almeida "Sim! Precisamos integrar com o sistema de exames laboratoriais e exportar dados para planilhas externas."
            enf_marta "Se puder receber notificações no celular seria um sonho, viu?"
        "Pergunto sobre problemas de acesso e segurança de informações.":
            enf_marta "Já esqueci senha e precisei pedir reset várias vezes. Tem que ser mais fácil."
            dr_almeida "Sou a favor de controle rígido de acesso. Segurança é prioridade, mas sem travar o trabalho."

    # CONCLUSÃO E PADDING DE SAÍDA
    "A entrevista chega ao fim, todos agradecem sua atenção e disposição para ouvir cada detalhe."
    show developer_requirements enthusiastic at left_zoom
    developer_requirements "Muito bom, [player_name]. Suas perguntas foram ótimas! Agora vamos organizar esses pontos e preparar a próxima etapa do projeto."
    hide developer_requirements

    scene transito_tarde
    with dissolve
    "Você retorna para sua mesa, sentindo que a entrevista foi produtiva e que já aprendeu muito sobre a importância de ouvir todos os envolvidos."
    "Anota rapidamente os pontos principais no notebook antes de seguir para a próxima atividade."

    return
