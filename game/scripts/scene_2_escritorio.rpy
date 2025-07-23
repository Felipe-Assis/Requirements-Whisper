label scene_2_escritorio:
    if chosen_job == "IDT-UFRJ":
        scene bg escritorio_interior_tarde
        with fade

        "Após um trajeto de ônibus, você chega ao prédio do Instituto de Doenças do Tórax (IDT-UFRJ)."
        "Na recepção, uma jovem de sorriso simpático te espera."

        show sabrina enthusiastic at left_zoom
        sabrina "Olá, você deve ser o [player_name], certo? Seja bem-vindo ao time do projeto IDT!"
        sabrina "Eu sou a Sabrina, engenheira de software responsável pelos requisitos desse projeto."
        sabrina "Vou te apresentar ao restante da equipe, vem comigo!"

        "Sabrina te conduz por um corredor até uma sala de trabalho ampla e iluminada, com computadores e quadros brancos."

        show carlos confident at right_zoom
        carlos "Opa! Chegou o reforço! Eu sou o Carlos, gosto de deixar o clima leve, mas sou fissurado por desafios de código. Sempre pode contar comigo!"

        show julio serious at center_zoom
        julio "Prazer, [player_name]. Eu sou o Julio, gosto das coisas bem feitas, organizadas e funcionais. Você vai me ver bastante por aqui, focado no backend."

        hide carlos
        show rodrigo serious at right_zoom
        rodrigo "Rodrigo. Analista de Qualidade. Não se assuste se eu aparecer cobrando testes, viu? (Brincadeira... ou não!)"
        "Rodrigo sorri de leve."

        hide sabrina
        show sabrina neutral at left_zoom
        sabrina "A equipe está animada com o projeto! Vamos desenvolver um sistema web inovador para o gerenciamento de exames médicos. Ele vai facilitar muito a vida de pacientes e médicos do IDT."
        sabrina "Logo você vai poder participar das reuniões e também dar suas ideias! O importante aqui é colaboração e curiosidade."

        "Você sente um misto de ansiedade e empolgação ao olhar para aquela equipe diversa e acolhedora."
        "O dia passa rápido enquanto você conhece os processos, o ambiente do escritório e aprende sobre a rotina do projeto."

        jump proxima_cena3

    else:
        # Se não escolheu a vaga correta, faz voltar para procurar vaga
        "Você passa a tarde esperando por respostas das empresas..."
        if chosen_job == "Startup":
            "A startup de educação financeira não respondeu seu e-mail."
        elif chosen_job == "Empresa legada":
            "A grande empresa enviou uma resposta automática, dizendo que o processo seletivo já foi encerrado."
        "Talvez seja melhor tentar se candidatar para outra vaga."
        jump scene_1_quarto
