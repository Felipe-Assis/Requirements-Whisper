label scene_7_avaliacao_requisitos:
#     $ disponivel_developer_ai = True
#     $ disponivel_developer_coding = True
#     $ disponivel_developer_management = True
    $ disponivel_developer_requirements = False
#     $ disponivel_developer_project = True
    $ disponivel_developer_quality = False
#     $ disponivel_developer_security = True
#     $ disponivel_developer_test = True
    play music music_office_focused fadein 1.0
    scene bg escritorio_interior_tarde
    with fade

    $ advance_minutes(15)
    "{i}De volta ao escritório, você encontra [NOME_DEVELOPER_REQUIREMENTS] revisando anotações na tela do computador.{/i}"

    show developer_requirements thinking at left_zoom
    show developer_quality positive at right_zoom

    developer_requirements "Pronto, [player_name]. Vamos olhar com calma o que saiu da entrevista?"
    developer_quality "Trouxe café pra todos? (sorri) Porque vamos precisar de energia para revisar esse material!"
    $ advance_minutes(2)

    "Você abre seu notebook e compartilha o resumo dos requisitos coletados."
    show developer_requirements neutral at left_zoom
    # A avaliação lê as duas decisões da scene_6 (primeira tentativa).
    if aprendizagem.get("saude_d6_abertura") and aprendizagem.get("saude_d6_ambiguidade"):
        developer_requirements "Você começou pedindo um caso concreto e não aceitou \"prático\" sem perguntar o que isso queria dizer. Foi daí que vieram os melhores detalhes."
    elif aprendizagem.get("saude_d6_abertura"):
        developer_requirements "Começar pedindo um caso concreto foi o ponto alto. No \"prático\", você precisou de um empurrão, mas chegou a tarefas que dá para conferir."
    elif aprendizagem.get("saude_d6_ambiguidade"):
        developer_requirements "Você destrinchou o \"prático\" muito bem. Na abertura, precisou de ajuda, mas o caso do plantão acabou aparecendo e rendeu muito."
    elif "saude_d6_abertura" in aprendizagem:
        developer_requirements "Você precisou de ajuda nas duas perguntas-chave, e tudo bem: as respostas vieram. Na próxima entrevista, tente abrir pedindo um caso real."
    else:
        developer_requirements "Olha, gostei da sua abordagem! Você foi a fundo nas dores do usuário e anotou detalhes relevantes."
    $ advance_minutes(3)

    developer_quality "E anotou as sugestões de melhoria também, ótimo! Mas posso sugerir uma coisa?"

    menu (tipo="conversa"):
        "Como você reage à sugestão de feedback?"
        "Claro, quero sempre melhorar!":
            $ add_friendship_point("developer_quality", 1)
            developer_quality "É assim que se evolui! Minha dica: quando ouvir um adjetivo como \"rápido\" ou \"fácil\", pergunte o que a pessoa quer conseguir fazer."
        "Acho que fiz o possível, mas aceito críticas.":
            developer_requirements "Humildade é fundamental nesse processo. Ninguém levanta tudo na primeira rodada, pode ficar em paz."
        "Só se for algo rápido, o dia foi longo...":
            developer_quality "Entendo, foi um dia puxado. Depois podemos revisar com calma, sem estresse!"
    $ advance_minutes(2)

    show developer_requirements enthusiastic at left_zoom
    developer_requirements "Antes de documentar, falta separar bem o que é requisito funcional, o que é não funcional, e o que é só opinião ou desejo."
    developer_requirements "Vamos treinar com três itens que saíram da entrevista. Para cada um, diga o que ele é."
    developer_quality "Funcional é o que o sistema faz. Não funcional é como ele precisa se comportar: rapidez, segurança, facilidade de uso. Desejo é preferência sem uma necessidade clara por trás."
    $ advance_minutes(2)

    # ITEM 1: funcional
    "Item 1: \"Calcular a carga tabágica a partir dos cigarros por dia e dos anos de fumo.\""
    menu (tipo="trabalho"):
        "1 de 3 · Como você classifica esse item?"
        "Requisito não funcional.":
            $ decisao("saude_d7_carga_tabagica", False)
            show developer_requirements thinking at left_zoom
            developer_requirements "Não funcional fala de como o sistema se comporta, como rapidez ou segurança. Aqui temos uma função: entra o consumo, sai a carga tabágica."
        "Requisito funcional.":
            $ decisao("saude_d7_carga_tabagica", True)
            show developer_requirements positive at left_zoom
            developer_requirements "Isso. É algo que o sistema faz: recebe dados e devolve um resultado. Dá até para escrever um teste com números."
        "Desejo da médica.":
            $ decisao("saude_d7_carga_tabagica", False)
            show developer_requirements thinking at left_zoom
            developer_requirements "A [NOME_DOUTORA_1] pediu isso por um motivo concreto: hoje o cálculo é feito à mão. Quando há uma necessidade clara por trás, não é só desejo."

    if not aprendizagem.get("saude_d7_carga_tabagica"):
        menu (tipo="trabalho"):
            "Reveja a classificação:"
            "É funcional: descreve uma ação do sistema, com entrada e resultado.":
                developer_requirements "Exato. Vamos ao próximo."

    # ITEM 2: não funcional
    "Item 2: \"Abrir o prontuário em menos de 2 segundos, mesmo com 100 pessoas usando o sistema.\""
    menu (tipo="trabalho"):
        "2 de 3 · Como você classifica esse item?"
        "Desejo da equipe clínica.":
            $ decisao("saude_d7_desempenho", False)
            show developer_quality thinking at right_zoom
            developer_quality "Tem número e condição de uso. Dá para medir, então é mais que preferência."
        "Requisito funcional.":
            $ decisao("saude_d7_desempenho", False)
            show developer_quality thinking at right_zoom
            developer_quality "Abrir o prontuário é a função. O que este item acrescenta é o tempo e a carga, e isso é qualidade de desempenho."
        "Requisito não funcional.":
            $ decisao("saude_d7_desempenho", True)
            show developer_quality positive at right_zoom
            developer_quality "Certo! Fala de desempenho e já vem com número e condição de carga. Dá para medir."

    if not aprendizagem.get("saude_d7_desempenho"):
        menu (tipo="trabalho"):
            "Reveja a classificação:"
            "É não funcional: diz como o sistema precisa se comportar, com uma medida.":
                developer_quality "Isso. E repare que ele já nasce testável."

    # ITEM 3: desejo
    "Item 3, o comentário da [NOME_DOUTORA_2] na saída: \"Deixar a tela inicial verdinha, porque combina com saúde.\""
    menu (tipo="trabalho"):
        "3 de 3 · Como você classifica esse item?"
        "Requisito não funcional de aparência.":
            $ decisao("saude_d7_tela_verde", False)
            show developer_requirements thinking at left_zoom
            developer_requirements "Aparência pode virar requisito quando há uma necessidade, como contraste para quem lê no plantão. Aqui é gosto pessoal."
        "Requisito funcional.":
            $ decisao("saude_d7_tela_verde", False)
            show developer_requirements thinking at left_zoom
            developer_requirements "A cor não muda o que o sistema faz. É preferência, sem um problema por trás."
        "Desejo, para confirmar depois.":
            $ decisao("saude_d7_tela_verde", True)
            show developer_requirements positive at left_zoom
            developer_requirements "Isso. Não há necessidade por trás, só preferência. A gente anota e confirma com as duas antes de decidir."

    if not aprendizagem.get("saude_d7_tela_verde"):
        menu (tipo="trabalho"):
            "Reveja a classificação:"
            "É desejo: anoto e confirmo com as médicas antes de virar requisito.":
                developer_requirements "Combinado. Desejo não se joga fora, só não entra na frente do que é necessário."

    $ advance_minutes(6)
    show developer_requirements enthusiastic at left_zoom
    developer_requirements "Separar assim ajuda a decidir o que entra primeiro e como cada item vai ser testado."
    $ registrar("saude_reg_classificacao")
    developer_quality "E se pintar dúvida, não hesite em voltar aos stakeholders, mesmo que seja por mensagem. Um bom documento de requisitos acompanha a realidade do projeto!"
    $ advance_minutes(2)

    "{i}Vocês riem juntos ao perceber que a lista de requisitos só cresce, mas a equipe está animada com o progresso.{/i}"

    show developer_requirements serious at left_zoom
    developer_requirements "Se quiser minha ajuda para organizar tudo em formato de documento, estou por aqui. E lembre-se: documentação bem feita é amiga do desenvolvedor!"

    show developer_quality thinking at right_zoom
    developer_quality "Mais tarde podemos revisar a lista inteira juntos. Vai ser bom para todos fixarem os conceitos."
    $ advance_minutes(2)

    hide developer_quality
    show developer_requirements enthusiastic at left_zoom
    developer_requirements "Bom trabalho, [player_name]. Agora vai tomar um café, que parte do pessoal está lá na copa."

    hide developer_requirements
    with dissolve
    $ advance_minutes(5)
    "{i}Você salva o arquivo e se levanta para esticar as pernas. Ainda é meio da tarde, e o cheiro de café chega até a sua mesa.{/i}"

    return
