label scene_2_escritorio:
    if chosen_job == "saude":
        scene bg escritorio_interior_tarde
        with fade

        "Após um trajeto de ônibus, você chega ao prédio onde será desenvolvido o novo sistema web para a área da saúde."
        "Na recepção, uma jovem de sorriso simpático te espera."

        show developer_requirements enthusiastic at left_zoom
        developer_requirements "Olá, você deve ser o [player_name], certo? Seja bem-vindo ao nosso time!"
        developer_requirements "Eu sou a [NOME_DEVELOPER_REQUIREMENTS], engenheira de software responsável pela parte de requisitos desse projeto."
        developer_requirements "Vou te apresentar à equipe, vem comigo!"

        "Ela te conduz por um corredor até uma sala de trabalho ampla e iluminada, com computadores e quadros brancos."

        # Apresentação da equipe (um a um, com personalidade e transição)
        # developer_test - animado/eficiente
        show developer_test enthusiastic at right_zoom
        developer_test "Oi! Bem-vindo! Eu sou o [NOME_DEVELOPER_TEST], apaixonado por desafios de teste e validação. Não se assuste se eu aparecer por aqui codando ou automatizando tudo!"
        pause 0.4

        hide developer_test with dissolve

        # developer_coding - experiente/sério
        show developer_coding serious at center_zoom
        developer_coding "Prazer, sou [NOME_DEVELOPER_CODING]. Prezo por código limpo e funcionalidade bem feita. Você vai me ver bastante, sempre atento aos detalhes do backend."
        pause 0.4

        hide developer_coding with dissolve

        # developer_management - gerente, querido/organizado
        show developer_management thinking at right_zoom2
        developer_management "Olá! Eu sou o [NOME_DEVELOPER_MANAGEMENT], responsável por garantir que tudo esteja bem organizado e documentado. Pode contar comigo para alinhar o projeto!"
        pause 0.4

        hide developer_management with dissolve

        # developer_project - arquitetura, fala pouco, pontual
        hide developer_requirements with dissolve
        show developer_project serious at left_zoom
        developer_project "Sou [NOME_DEVELOPER_PROJECT]. Gosto de arquitetura de software e banco de dados. Prefiro ser direto: se precisar de algo nessa área, é só chamar."
        pause 0.3

        hide developer_project with dissolve

        # developer_quality - comunicativa, ensina, ajuda em requisitos
        show developer_quality positive at right_zoom
        developer_quality "Oi! Eu sou a [NOME_DEVELOPER_QUALITY], trabalho com qualidade de software e adoro compartilhar conhecimento. Se precisar de dicas ou quiser conversar sobre testes, me procure!"
        pause 0.3

        hide developer_quality with dissolve

        # developer_ai - entusiasmado, rápido, ideias novas
        show developer_ai positive at center_zoom
        developer_ai "E aí! [NOME_DEVELOPER_AI] na área! Sou fissurado em IA, Machine Learning e inovação. Se tiver uma ideia maluca, me chama. Bora revolucionar esse sistema juntos!"
        pause 0.3

        hide developer_ai with dissolve

        # developer_security - sério, fala devagar
        show developer_security serious at right_zoom
        developer_security "Oi, sou o [NOME_DEVELOPER_SECURITY], foco em segurança do sistema. Se quiser saber como proteger seus dados ou precisa de checklists, só perguntar."
        pause 0.3

        hide developer_security with dissolve

        # Sabrina (developer_requirements) retorna para reforçar integração
        show developer_requirements neutral at left_zoom
        developer_requirements "A equipe está animada com o projeto! Vamos desenvolver um sistema inovador para o gerenciamento de exames médicos, facilitando a vida de pacientes e médicos."
        developer_requirements "Logo você vai participar das reuniões e trazer suas ideias! O importante aqui é colaboração e curiosidade."
        hide developer_requirements

        "Você sente um misto de ansiedade e empolgação ao olhar para aquela equipe diversa e acolhedora."
        "O dia passa rápido enquanto você conhece os processos, o ambiente do escritório e aprende sobre a rotina do projeto."

    else:
        # Se não escolheu a vaga correta, faz voltar para procurar vaga
        "Você passa a tarde esperando por respostas das empresas..."
        if chosen_job == "startup":
            "A startup de tecnologia não respondeu seu e-mail."
        elif chosen_job == "corporativo":
            "A grande empresa enviou uma resposta automática, dizendo que o processo seletivo já foi encerrado."
        "Talvez seja melhor tentar se candidatar para outra vaga."
        jump scene_1_quarto
