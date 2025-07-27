label scene_2_escritorio:

    if chosen_job == "saude":
        # Redefinir relógio para tarde (ex: 13h30)
        $ game_hour = 13
        $ game_minute = 30

        scene bg empresa_exterior_manha
        with fade
        play music music_office_motivated fadein 1.5

        "{i}Após um trajeto de ônibus e muita expectativa, você chega ao prédio onde será desenvolvido o novo sistema web para a área da saúde.{/i}"
        $ advance_minutes(15)

        scene bg escritorio_interior_tarde
        with fade

        "{i}Na recepção, uma jovem de sorriso simpático te espera, já segurando uma prancheta digital com anotações do projeto.{/i}"

        show developer_requirements enthusiastic at left_zoom
        developer_requirements "Olá, você deve ser o [player_name], certo? Seja bem-vindo ao nosso time!"
        $ add_contact("developer_requirements")
        $ add_friendship_point("developer_requirements")
        $ advance_minutes(2)

        developer_requirements "Eu sou a [NOME_DEVELOPER_REQUIREMENTS], engenheira de software responsável pela parte de requisitos desse projeto."
        developer_requirements "Hoje vou te apresentar à equipe. Preparado(a) para conhecer quem vai te acompanhar nessa jornada?"
        $ advance_minutes(1)

        "{i}Ela te conduz por um corredor até uma sala de trabalho ampla e iluminada, com computadores, quadros brancos e post-its por toda parte.{/i}"
        $ advance_minutes(2)

        # developer_test - animado/eficiente
        show developer_test enthusiastic at right_zoom
        developer_requirements "Esse é o [NOME_DEVELOPER_TEST], nosso expert em testes!"
        developer_test "Oi! Bem-vindo! Sou apaixonado por desafios de teste e validação. Não se assuste se me ver codando e automatizando até o café!"
        $ add_contact("developer_test")
        $ add_friendship_point("developer_test")
        pause 0.4
        hide developer_test with dissolve

        # developer_coding - experiente/sério
        show developer_coding serious at center_zoom
        developer_requirements "Aqui temos o [NOME_DEVELOPER_CODING], referência em desenvolvimento backend."
        developer_coding "Prazer, sou criterioso com código limpo e funcionalidade bem feita. Você vai me ver bastante atento aos detalhes, principalmente nas integrações do sistema ByeByeFumo com o app móvel."
        $ add_contact("developer_coding")
        $ add_friendship_point("developer_coding")
        pause 0.4
        hide developer_coding with dissolve

        # developer_management - gerente, querido/organizado
        show developer_management thinking at right_zoom2
        developer_requirements "Esse é o [NOME_DEVELOPER_MANAGEMENT], nosso gerente de projeto."
        developer_management "Olá! Pode contar comigo para alinhar prazos, organizar documentação e garantir que ninguém perca a daily!"
        $ add_contact("developer_management")
        $ add_friendship_point("developer_management")
        pause 0.4
        hide developer_management with dissolve

        # developer_project - arquitetura, fala pouco, pontual
        hide developer_requirements
        show developer_project serious at left_zoom
        developer_requirements "Aqui, [NOME_DEVELOPER_PROJECT], responsável pela arquitetura do sistema e banco de dados."
        developer_project "Sou direto: se precisar de algo sobre modelagem ou banco, é só chamar. Estamos desenhando uma arquitetura robusta pro ByeByeFumo."
        $ add_contact("developer_project")
        $ add_friendship_point("developer_project")
        pause 0.3
        hide developer_project with dissolve
        show developer_requirements neutral at left_zoom

        # developer_quality - comunicativa, ensina, ajuda em requisitos
        show developer_quality positive at right_zoom
        developer_requirements "A [NOME_DEVELOPER_QUALITY] cuida da qualidade do software e adora compartilhar conhecimento!"
        developer_quality "Oi! Testes, documentação, requisitos... Se quiser conversar sobre qualidade ou aprender algo novo, pode me procurar!"
        $ add_contact("developer_quality")
        $ add_friendship_point("developer_quality")
        pause 0.3
        hide developer_quality with dissolve

        # developer_ai - entusiasmado, rápido, ideias novas
        show developer_ai positive at center_zoom
        developer_requirements "Já [NOME_DEVELOPER_AI] é nosso entusiasta de IA e inovação."
        developer_ai "E aí! Sou fissurado em IA, machine learning e inovação. Se tiver uma ideia maluca, me chama. Bora revolucionar esse sistema juntos, do requisito ao deploy!"
        $ add_contact("developer_ai")
        $ add_friendship_point("developer_ai")
        pause 0.3
        hide developer_ai with dissolve

        # developer_security - sério, fala devagar
        show developer_security serious at right_zoom
        developer_requirements "E fechando o time, [NOME_DEVELOPER_SECURITY], segurança total!"
        developer_security "Oi, sou o responsável por garantir que tudo esteja seguro. Checklist, logs, criptografia... Pode confiar, seus dados (e os dos pacientes) estarão protegidos."
        $ add_contact("developer_security")
        $ add_friendship_point("developer_security")
        pause 0.3
        hide developer_security with dissolve

        # Sabrina retorna para integração
        show developer_requirements neutral at left_zoom
        developer_requirements "O time todo está animado com o projeto! Vamos desenvolver um sistema inovador para acompanhamento de pacientes, baseado nos formulários do NETT e focado em saúde pulmonar."
        developer_requirements "Logo você vai participar de reuniões e poderá dar sugestões. O segredo aqui é colaboração, curiosidade e organização!"
        $ advance_minutes(4)
        hide developer_requirements

        "{i}Você sente um misto de ansiedade e empolgação ao olhar para aquela equipe diversa e acolhedora.{/i}"
        "{i}O dia passa rápido enquanto você conhece os processos, explora o escritório e aprende sobre as primeiras tarefas do projeto ByeByeFumo, desde o levantamento de requisitos até o planejamento de sprints no Trello.{/i}"
        $ advance_minutes(30)

        stop music fadeout 2.0

    else:
        "{i}Você passa a tarde esperando por respostas das empresas...{/i}"
        if chosen_job == "startup":
            "{i}A startup de tecnologia não respondeu seu e-mail.{/i}"
        elif chosen_job == "corporativo":
            "{i}A grande empresa enviou uma resposta automática, dizendo que o processo seletivo já foi encerrado.{/i}"
        "{i}Talvez seja melhor tentar se candidatar para outra vaga.{/i}"
        jump scene_1_quarto

    return