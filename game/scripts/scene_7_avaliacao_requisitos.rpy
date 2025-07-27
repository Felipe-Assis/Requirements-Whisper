label scene_7_avaliacao_requisitos:
    scene bg escritorio_interior_tarde
    with fade

    "Após a entrevista com os stakeholders, você retorna à sala de trabalho e encontra [NOME_DEVELOPER_REQUIREMENTS] revisando anotações na tela do computador."

    show developer_requirements thinking at left_zoom
    show developer_quality positive at right_zoom

    developer_requirements "E aí, [player_name], como foi a conversa? Conseguiu levantar informações importantes?"
    developer_quality "Trouxe café pra todos? (sorri) Porque vamos precisar de energia para revisar esse material!"

    "Você abre seu notebook e compartilha o resumo dos requisitos coletados."
    show developer_requirements neutral at left_zoom
    developer_requirements "Vamos dar uma olhada juntos... (lendo atentamente) Olha, gostei da sua abordagem! Você foi a fundo nas dores do usuário e anotou detalhes relevantes."

    developer_quality "E prestou atenção nas sugestões de melhoria também, ótimo! Mas posso sugerir uma coisa?"

    menu:
        "Como você reage à sugestão de feedback?"
        "Claro, quero sempre melhorar!":
            $ amizade_developer_quality += 1
            developer_quality "É assim que se evolui! Minha dica: sempre pergunte por exemplos reais, isso enriquece o levantamento."
        "Acho que fiz o possível, mas estou aberto(a) a críticas.":
            developer_requirements "Humildade é fundamental nesse processo. Ninguém levanta tudo na primeira rodada, fique tranquilo(a)."
        "Só se for algo rápido, estou cansado(a)...":
            developer_quality "Entendo, foi um dia puxado. Depois podemos revisar com calma, sem estresse!"

    show developer_requirements enthusiastic at left_zoom
    developer_requirements "No geral, mandou bem! Só reforço a importância de separar bem o que é requisito funcional, o que é usabilidade, e o que é só opinião ou desejo do usuário."
    developer_quality "E se pintar dúvida, não hesite em voltar aos stakeholders, mesmo que seja por mensagem."

    "Vocês riem juntos ao perceber que a lista de requisitos só cresce, mas a equipe está animada com o progresso."

    show developer_requirements serious at left_zoom
    developer_requirements "Se quiser minha ajuda para organizar tudo em formato de documento, estou por aqui. E lembre-se: documentação bem feita é amiga do desenvolvedor!"

    show developer_quality thinking at right_zoom
    developer_quality "Amanhã podemos revisar juntos antes da reunião de apresentação. Vai ser bom para todos fixarem os conceitos."

    hide developer_quality
    show developer_requirements enthusiastic at left_zoom
    developer_requirements "Parabéns pelo empenho hoje, [player_name]. Você está evoluindo rápido! Até amanhã!"

    hide developer_requirements

    scene bg escritorio_interior_noite
    with dissolve
    "Fim do expediente. Você sente que está progredindo de verdade, não só no projeto, mas também nas suas habilidades profissionais."

    return
