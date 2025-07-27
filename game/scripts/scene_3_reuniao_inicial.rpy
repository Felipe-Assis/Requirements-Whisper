label scene_3_reuniao_inicial:
    scene bg escritorio_interior_tarde
    with dissolve

    "Mais tarde, a equipe se reúne em volta de uma mesa para a reunião inicial do projeto."
    "O clima é leve, todos estão curiosos sobre como será trabalhar juntos."

    # 1º bloco: developer_requirements + developer_ai
    show developer_requirements enthusiastic at left_zoom
    show developer_ai positive at right_zoom
    developer_requirements "Agora que estamos completos, gostaria de explicar o ciclo de desenvolvimento que vamos seguir neste projeto."
    developer_requirements "Já ouviram falar do ciclo de vida do desenvolvimento de software? É fundamental para mantermos tudo organizado e eficiente."
    developer_ai "Eu sempre digo: entender o ciclo faz toda diferença para inovar sem perder o controle!"

    hide developer_ai
    show developer_quality positive at right_zoom
    developer_requirements "Vou detalhar as principais etapas para vocês:"
    developer_requirements "1. **Elicitação de requisitos**: entender as necessidades reais dos usuários e stakeholders."
    developer_requirements "2. **Especificação e documentação**: transformar tudo isso em algo claro para todos."
    developer_requirements "3. **Design e arquitetura**: planejar como o sistema será construído."
    developer_requirements "4. **Codificação**: escrever o código em si, colocando tudo em prática."
    developer_requirements "5. **Testes e validação**: garantir que tudo funciona e é seguro."
    developer_requirements "6. **Implantação**: colocar o sistema para rodar e monitorar o uso."
    developer_quality "Isso mesmo! Qualidade nasce com bons requisitos e especificações. Sem isso, fica impossível testar direito."

    # --- Pergunta interativa do jogador ---
    hide developer_quality
    show developer_management thinking at right_zoom
    menu:
        "Você deseja perguntar algo?"
        "Qual a importância de cada fase para o sucesso do projeto?":
            $ amizade_developer_requirements += 1
            developer_requirements "Ótima pergunta! Cada fase tem seu papel para evitar erros e retrabalhos. Quanto mais clareza no início, menos dor de cabeça depois."
            show developer_quality positive at right_zoom2
            developer_quality "Exatamente. E sempre envolva a equipe em todas etapas!"
            hide developer_quality
        "E se uma etapa não for bem feita, o que pode acontecer?":
            $ amizade_developer_quality += 1
            show developer_quality serious at right_zoom2
            developer_quality "Já vi projetos em que ignoraram testes ou documentação... Foi só problema! O segredo é não pular etapas."
            developer_requirements "Perfeito, [NOME_DEVELOPER_QUALITY]! Tudo no ciclo tem um motivo."
            hide developer_quality
        "Vocês usam métodos ágeis ou tradicionais?":
            $ amizade_developer_management += 1
            developer_management "Costumamos adaptar. Seguimos princípios ágeis, mas documentamos bem para facilitar revisões e auditorias."
            developer_requirements "Exatamente. A ideia é ser flexível, mas organizado."

    # --- Troca para developer_project ---
    hide developer_management
    show developer_project thinking at right_zoom
    developer_project "Posso dar um toque? Banco de dados bem planejado faz diferença desde o começo. Design ruim agora gera retrabalho depois."
    developer_requirements "Boa, [NOME_DEVELOPER_PROJECT]! Todo mundo vai poder contribuir nas decisões técnicas."
    hide developer_project

    # --- Coloca developer_test + developer_coding na tela ---
    show developer_test enthusiastic at right_zoom
    show developer_coding serious at center_zoom
    developer_test "E não se esqueçam dos testes automatizados! Quanto antes a gente rodar testes, melhor."
    developer_coding "Quero só reforçar: código limpo e padronizado facilita tudo, inclusive para quem for revisar ou manter depois."

    hide developer_test
    hide developer_coding

    # --- developer_quality + developer_security na tela ---
    show developer_quality thinking at right_zoom
    show developer_security serious at right_zoom2
    developer_quality "Às vezes, a maior dificuldade nem é técnica... É alinhar o entendimento entre todo mundo!"
    developer_security "E lembrar que segurança não é só um detalhe no final, tem que ser pensada desde o início."
    hide developer_quality
    hide developer_security

    # --- developer_ai + developer_coding para conversa cruzada ---
    show developer_ai concentrated at left_zoom
    show developer_coding thinking at center_zoom
    developer_ai "Falando nisso, alguém já trabalhou com deploy automatizado? Queria testar umas integrações."
    developer_coding "Se for seguro e bem testado, estou dentro! Mas quero revisar cada linha do pipeline, hein."
    hide developer_ai
    hide developer_coding

    # Pergunta do jogador sobre o que será esperado dele(a)
    show developer_requirements enthusiastic at left_zoom
    developer_requirements "E você, [player_name], como prefere aprender? Mais mão na massa ou acompanhando os colegas nas reuniões?"
    menu:
        "Como você responde?"
        "Prefiro aprender fazendo, mas gosto de pedir dicas.":
            $ amizade_developer_coding += 1
            show developer_coding serious at right_zoom
            developer_coding "Ótimo, sempre que quiser, pode me chamar para revisar o código juntos."
            hide developer_coding
        "Gosto de observar e anotar tudo antes de tentar sozinho(a).":
            $ amizade_developer_requirements += 1
            developer_requirements "Adoro pessoas organizadas! No início, anotar tudo faz diferença."
        "Posso ajudar no que for preciso!":
            $ amizade_developer_test += 1
            show developer_test confident at right_zoom
            developer_test "Gostei da atitude! Aqui a gente aprende junto, errando e acertando."
            hide developer_test

    # Mini-evento social: developer_quality sugere um café rápido para relaxar
    show developer_quality positive at right_zoom
    developer_quality "Antes de continuarmos, que tal um café? Troca de ideia descontraída faz bem para o time."
    "O grupo ri e concorda, criando clima acolhedor. Você se sente mais integrado à equipe."
    hide developer_quality

    # developer_security faz pergunta sobre segurança
    show developer_security serious at right_zoom
    developer_security "Alguém lembra o motivo de envolver segurança desde o início do ciclo?"
    menu:
        "Como você responde?"
        "Para evitar vulnerabilidades desde o começo.":
            $ amizade_developer_security += 1
            developer_security "Perfeito. Prevenção é sempre melhor que remediar depois."
        "Porque consertar bug de segurança no fim sai caro.":
            $ amizade_developer_security += 1
            developer_security "Exatamente, [player_name]! Custa tempo, dinheiro e reputação."
        "Nunca pensei nisso, mas quero aprender.":
            developer_security "Ótimo! Já começamos bem, então. Vamos falar bastante sobre segurança durante o projeto."
    hide developer_security

    hide developer_requirements

    "Com isso, a reunião inicial chega ao fim. Você já começa a se sentir parte do time e percebe o quanto pode aprender neste ambiente colaborativo."

    return
