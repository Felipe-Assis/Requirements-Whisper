label scene_9_retorno_casa_sem2:
    scene bg transito_noite
    with dissolve

    "O segundo dia de entrevistas chega ao fim. Você embarca em um ônibus lotado, o cansaço pesando nas costas, mas a mente cheia de ideias."
    play sound "audio/bus.ogg"
    pause 1.0

    "Enquanto olha pela janela e observa as luzes da cidade, você relembra os principais pontos levantados nas conversas com os stakeholders."
    "Aos poucos, o trajeto para casa se torna um momento de reflexão silenciosa."

    scene bg quarto_noite
    with fade

    "Já no seu quarto, você coloca a mochila sobre a cama, abre o notebook e revisa cada anotação feita ao longo do dia."
    show expression "images/items/notebook.png" as notebook at center_zoom
    pause 0.7

    "Você lê atentamente:\n• Problemas enfrentados no sistema atual\n• Demandas prioritárias do diretor médico e da enfermeira\n• Dilemas entre relatórios e notificações\n• Sugestões de melhoria e integrações necessárias"

    "Faz pequenas correções nos requisitos, anotando exemplos reais que ouviu — como a vez em que o sistema travou no plantão, ou as dificuldades para exportar dados."

    "Para não esquecer, decide criar um checklist rápido para as próximas entrevistas: sempre perguntar por situações concretas, explorar não só o que o usuário deseja, mas também o que realmente precisa no dia a dia."

    "Antes de dormir, abre o celular e lê algumas anotações antigas da disciplina de Engenharia de Software."

    window hide
    pause 0.8
    window show

    "Você compara o que viu hoje com o que aprendeu na universidade:\n\n*“Na teoria, elicitar requisitos parece simples: basta fazer perguntas certas. Mas na prática, cada resposta traz novos desafios e pontos de vista. Entender o contexto do usuário faz toda diferença!”*"

    "Satisfeito(a) com o progresso, você fecha o notebook, prepara tudo para o dia seguinte e se permite finalmente descansar."

    scene black
    with fade

    window hide
    pause 1.0
    window show

    "Fim da Semana 2\n\nAprendizado: Técnicas de entrevista são essenciais, mas a empatia e a escuta ativa são o que realmente tornam um bom analista de requisitos."

    return
