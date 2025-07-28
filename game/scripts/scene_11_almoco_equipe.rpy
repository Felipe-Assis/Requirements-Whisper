label scene_11_almoco_equipe:
    play music music_coffee_break_friendly fadein 1.0

    $ game_hour = 13
    $ game_minute = 12

    scene bg refeitorio_tarde
    with fade

    $ advance_minutes(12)
    "{i}O relógio marca o início da tarde. A equipe se reúne no refeitório para o almoço. As mesas estão cheias de bandejas, risadas e conversas paralelas.{/i}"
    "{i}Você percebe [NOME_DEVELOPER_TEST] e [NOME_DEVELOPER_AI] discutindo animados sobre scripts; [NOME_DEVELOPER_CODING] trocando ideias com [NOME_DEVELOPER_PROJECT]; [NOME_DEVELOPER_QUALITY] ouvindo uma história engraçada de [NOME_DEVELOPER_SECURITY]; enquanto [NOME_DEVELOPER_REQUIREMENTS] revisa algo no notebook, de olho nas conversas.{/i}"
    "{i}Você pega sua comida e pode escolher onde sentar.{/i}"

    menu:
        "Você pode escolher com quem iniciar a conversa:"
        "Sentar com [NOME_DEVELOPER_CODING] e [NOME_DEVELOPER_PROJECT].":
            hide developer_test
            hide developer_ai
            hide developer_quality
            hide developer_security
            hide developer_requirements

            show developer_coding serious at left_zoom
            show developer_project thinking at right_zoom

            $ add_friendship_point("developer_coding", 1)
            $ add_friendship_point("developer_project", 1)

            # Extra: reação especial para alta amizade com coding
            if get_friendship_point("developer_coding") >= 4:
                developer_coding "Sabia que você ia vir pra cá! Bom ter alguém que gosta de arquitetura no time."
            else:
                developer_coding "E aí, [player_name]! Gostando do projeto até agora? Estávamos debatendo padrões de arquitetura. Tem algum que você prefira usar?"

            menu:
                "Como você responde?"
                "Gosto de padrões clássicos, como MVC.":
                    $ add_friendship_point("developer_coding", 1)
                    show developer_coding thinking at left_zoom
                    developer_coding "Ótima escolha! Simplicidade e previsibilidade nunca decepcionam."
                    # Extra: developer_project reage se amizade alta
                    if get_friendship_point("developer_project") >= 4:
                        show developer_project positive at right_zoom
                        developer_project "MVC resolve muito! Mas gosto que você analisa as opções antes de decidir."
                    else:
                        show developer_project serious at right_zoom
                        developer_project "MVC é seguro, mas se precisar escalar, pense em algo mais modular também."
                    # Interrupção de developer_quality
                    show developer_quality positive at right_zoom2
                    developer_quality "Desculpa me intrometer, mas se precisarem de checklist de revisão de arquitetura, só avisar!"
                    hide developer_quality
                "Tenho curiosidade sobre microsserviços e coisas novas.":
                    $ add_friendship_point("developer_project", 1)
                    if get_friendship_point("developer_project") >= 4:
                        show developer_project positive at right_zoom
                        developer_project "Só de querer inovar já mostra sua evolução no projeto. Posso compartilhar uns artigos depois!"
                    else:
                        show developer_project positive at right_zoom
                        developer_project "Gosto desse espírito inovador! Podemos estudar juntos como adaptar isso ao nosso contexto."
                    show developer_ai positive at left_zoom
                    developer_ai "Se quiser simular alguns fluxos com IA, topo ajudar. Pode render ideias legais!"
                    hide developer_ai
                "Na verdade, ainda estou aprendendo sobre o assunto.":
                    if get_friendship_point("developer_coding") >= 4:
                        show developer_coding neutral at left_zoom
                        developer_coding "Relaxa, você aprende rápido! Posso te passar uns materiais que usei no início da carreira."
                    else:
                        show developer_coding neutral at left_zoom
                        developer_coding "Sem pressa, o projeto é ótimo para experimentar e crescer."
                    show developer_requirements positive at right_zoom2
                    developer_requirements "Se quiser um material básico, posso te passar depois!"
                    hide developer_requirements
            hide developer_coding
            hide developer_project

        "Sentar com [NOME_DEVELOPER_TEST] e [NOME_DEVELOPER_AI].":
            hide developer_coding
            hide developer_project
            hide developer_quality
            hide developer_security
            hide developer_requirements

            show developer_test enthusiastic at left_zoom
            show developer_ai positive at right_zoom

            $ add_friendship_point("developer_test", 1)
            $ add_friendship_point("developer_ai", 1)

            if get_friendship_point("developer_test") >= 4:
                developer_test "Ei, [player_name]! Estava te esperando pra animar o papo aqui!"
            else:
                developer_test "E aí, [player_name]! Sabia que eu já automatizei o teste de uma cafeteria inteira? Imagina isso aqui no sistema..."

            developer_ai "Eu estava explicando sobre como IA pode ajudar a prever demandas e otimizar os fluxos do hospital. Já pensou?"
            menu:
                "Sobre o que quer conversar?"
                "Quero aprender mais sobre testes automatizados.":
                    $ add_friendship_point("developer_test", 1)
                    if get_friendship_point("developer_test") >= 5:
                        show developer_test confident at left_zoom
                        developer_test "Sabia que ia perguntar! Já deixei uns exemplos prontos pra te mostrar depois do almoço!"
                    else:
                        show developer_test confident at left_zoom
                        developer_test "Depois do almoço, se quiser, te mostro uns scripts e ferramentas!"
                    # Interrupção de developer_coding
                    show developer_coding neutral at right_zoom2
                    developer_coding "Não esqueçam de manter o padrão no código dos testes, hein! Qualquer dúvida me chama."
                    hide developer_coding
                "Fico curioso(a) sobre IA aplicada à saúde.":
                    $ add_friendship_point("developer_ai", 1)
                    if get_friendship_point("developer_ai") >= 4:
                        show developer_ai positive at right_zoom
                        developer_ai "Legal te ver engajado(a) nisso! Tenho um artigo salvo só pra você, depois te mando no chat."
                    else:
                        show developer_ai positive at right_zoom
                        developer_ai "Tem muita coisa inovadora surgindo! Se quiser, te passo uns artigos legais."
                    # Interrupção de developer_project
                    show developer_project serious at left_zoom
                    developer_project "Só lembrem de validar os dados! IA é poderosa, mas depende da qualidade das informações."
                    hide developer_project
                "Prefiro só ouvir e aproveitar o clima descontraído.":
                    show developer_ai thinking at right_zoom
                    developer_ai "Justo! Às vezes é bom só relaxar."
                    show developer_test positive at left_zoom
                    developer_test "Café e risadas também ajudam no rendimento!"
            hide developer_test
            hide developer_ai

        "Sentar com [NOME_DEVELOPER_QUALITY] e [NOME_DEVELOPER_SECURITY].":
            hide developer_coding
            hide developer_project
            hide developer_test
            hide developer_ai
            hide developer_requirements

            show developer_quality positive at left_zoom
            show developer_security serious at right_zoom

            $ add_friendship_point("developer_quality", 1)
            $ add_friendship_point("developer_security", 1)

            if get_friendship_point("developer_quality") >= 4:
                developer_quality "Senta aqui, [player_name]! Depois quero ver suas anotações de bugs, sei que são detalhadas!"
            else:
                developer_quality "Estávamos falando sobre os maiores bugs que já pegamos em produção... e olha, foram uns casos cabeludos."
            show developer_security thinking at right_zoom
            developer_security "E a maioria deles era falha boba de permissão ou de senha fraca. Segurança nunca é demais."
            menu:
                "O que você comenta?"
                "Pergunto como evitar esses bugs no futuro.":
                    $ add_friendship_point("developer_quality", 1)
                    if get_friendship_point("developer_quality") >= 5:
                        show developer_quality enthusiastic at left_zoom
                        developer_quality "Você sempre atento(a) aos detalhes! Vou te passar meu checklist exclusivo depois."
                    else:
                        show developer_quality enthusiastic at left_zoom
                        developer_quality "Processo de revisão, testes e checklist bem definidos. Depois te mostro nossa rotina."
                    # Interrupção de developer_test
                    show developer_test enthusiastic at right_zoom2
                    developer_test "É verdade! E sempre documente os casos de erro, fica muito mais fácil de corrigir depois."
                    hide developer_test
                "Quero saber sobre ataques de segurança mais comuns.":
                    $ add_friendship_point("developer_security", 1)
                    if get_friendship_point("developer_security") >= 4:
                        show developer_security serious at right_zoom
                        developer_security "Te ensino os principais tipos — e posso simular um ataque só para treino se quiser! Mas só depois do almoço, prometo."
                    else:
                        show developer_security serious at right_zoom
                        developer_security "Phishing, senhas fracas, SQL injection... Posso te mostrar exemplos e como se proteger."
                    # Interrupção de developer_ai
                    show developer_ai positive at left_zoom
                    developer_ai "Curto bastante desafios de segurança! Um dia desses tentei hackear meu próprio sistema só para treinar."
                    hide developer_ai
                "Comento sobre bugs que já presenciei em outros projetos.":
                    if get_friendship_point("developer_quality") >= 4:
                        show developer_quality positive at left_zoom
                        developer_quality "Esses exemplos de campo são os melhores! Se topar, depois pode mostrar pro time inteiro."
                    else:
                        show developer_quality thinking at left_zoom
                        developer_quality "Todo mundo já viu algum perrengue. Aprendizado de campo é valioso demais!"
                    # Interrupção de developer_requirements
                    show developer_requirements positive at right_zoom2
                    developer_requirements "Compartilhe esses exemplos no grupo depois, assim todos aprendem juntos."
                    hide developer_requirements
            hide developer_quality
            hide developer_security

    $ advance_minutes(10)
    with dissolve

    # Após a conversa principal, todos fazem pequenas interações cruzadas para dar mais vida ao almoço:
    show developer_requirements positive at left_zoom
    if get_friendship_point("developer_requirements") >= 4:
        developer_requirements "Lembrem de passar na sala depois! Se alguém tiver ideias que queira testar, a porta está aberta. Equipe colaborativa é tudo."
    else:
        developer_requirements "Não esqueçam da reunião às 15h, hein! Depois quero ouvir as ideias que surgiram no almoço."
    show developer_ai thinking at right_zoom
    developer_ai "Almoço é onde surgem as melhores soluções para bugs, pode apostar!"
    hide developer_requirements
    hide developer_ai

    show developer_security serious at left_zoom
    if get_friendship_point("developer_security") >= 4:
        developer_security "[player_name], obrigado(a) por sempre pensar em segurança! Se quiser se aprofundar, me chama depois."
    else:
        developer_security "E, [player_name], se quiser conversar sobre proteção de dados, só procurar!"
    hide developer_security

    show developer_quality positive at right_zoom
    if get_friendship_point("developer_quality") >= 4:
        developer_quality "Pudim só pra quem compartilha bugs engraçados, hein! Quem vai contar o melhor hoje?"
    else:
        developer_quality "Estou de olho nas sobremesas também, alguém quer dividir um pudim?"
    hide developer_quality

    $ advance_minutes(6)
    with dissolve

    "{i}O almoço termina em clima leve, com risos e provocações saudáveis entre os colegas.{/i}"
    "{i}Você sente que as conexões vão além do profissional — a amizade e a troca de experiências fazem toda diferença no ambiente.{/i}"

    play music music_office_focused fadein 1.5
    scene bg escritorio_interior_tarde
    with dissolve
    $ advance_minutes(12)
    "{i}Hora de voltar ao trabalho, agora com mais confiança para encarar as próximas etapas do projeto.{/i}"

    return
