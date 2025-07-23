label scene_1_quarto:
    $ player_gender = ""
    $ player_name = ""
    $ player_age = ""
    $ inventory = []

    scene bg quarto_manha

    "BIP BIP BIP... O som do alarme ecoa pelo quarto iluminado pela manhã."
    "Ainda sonolento, você se senta na cama e logo se lembra: hoje é dia de buscar um estágio!"
    "Você olha ao redor do quarto, respira fundo e decide começar o dia."

    # 1. Pergunta o nome
    $ player_name = renpy.input("Antes de começarmos, qual é o seu nome?")
    $ player_name = player_name.strip()
    while player_name == "":
        $ player_name = renpy.input("Por favor, digite um nome válido:")
        $ player_name = player_name.strip()

    # 2. Pergunta o sexo
    "E qual seu gênero?"
    menu:
        "Escolha seu gênero:"
        "Feminino":
            $ player_gender = "Feminino"
        "Masculino":
            $ player_gender = "Masculino"
        "Outro":
            $ player_gender = "Outro"

    # 3. Pergunta a idade
    $ player_age = renpy.input("Qual sua idade?")
    $ player_age = player_age.strip()
    while not player_age.isdigit() or int(player_age) < 12 or int(player_age) > 99:
        $ player_age = renpy.input("Por favor, digite uma idade válida (12-99):")
        $ player_age = player_age.strip()
    $ player_age = int(player_age)

    # Continua normalmente:
    "Ótimo, [player_name]! Tudo pronto para sua busca por estágio."

    "Você se levanta, pega seu notebook em cima da escrivaninha e senta para procurar vagas disponíveis."
    $ inventory.append("notebook")

    "Após alguns minutos de busca, você encontra três oportunidades interessantes:"

    menu:
        "Qual vaga deseja se candidatar?"
        "1. Projeto de software para o Instituto de Doenças do Tórax (IDT-UFRJ)":
            $ chosen_job = "IDT-UFRJ"
            "Você sente um frio na barriga, mas a ideia de participar de um projeto de impacto na área da saúde te anima."
        "2. Desenvolvimento mobile para startup de educação financeira":
            $ chosen_job = "Startup"
            "Startups costumam ser ambientes dinâmicos... Quem sabe seja a chance de crescer rápido?"
        "3. Estágio em manutenção de sistemas legados numa grande empresa":
            $ chosen_job = "Empresa legada"
            "Estabilidade, benefícios, um ambiente mais tradicional. Pode ser interessante para aprender com uma grande equipe."

    "Você anota todos os detalhes da vaga e envia sua candidatura pelo notebook."
    "Depois de terminar, sente que merece um pouco de organização. Você pega sua mochila e começa a guardar os itens que vai precisar."
    $ inventory.append("mochila")
    "Em seguida, confere no espelho se está apresentável para o dia. Troca de roupa e se sente pronto para essa nova fase!"
    "Agora é esperar a resposta das empresas..."