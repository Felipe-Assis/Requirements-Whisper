label scene_17_tarde_estudos_tecnicos:
    play music music_office_relaxed fadein 1.0
    scene bg escritorio_interior_tarde
    with dissolve

    $ advance_minutes(11)
    "{i}Após a reunião de gerenciamento, a equipe retorna ao trabalho. Você decide aproveitar a tarde para revisar algumas teorias essenciais no notebook.{/i}"

    play sound "audio/notebook_open.ogg"
    show expression "images/items/notebook.png" as notebook at center_zoom
    "{i}Você abre seu material digital e encontra uma lista de tópicos para revisar:{/i}"

    window hide
    pause 0.7
    window show

    "• Testes automatizados\n• Métricas de qualidade de software\n• Algoritmos de Machine Learning\n• Práticas de documentação\n• Revisão de código colaborativa"

    # Minijogo didático: quiz de revisão rápida
    "{i}Você resolve testar seus conhecimentos com um quiz rápido no notebook:{/i}"
    $ acertos_quiz = 0

    menu:
        "O que é um critério de aceitação eficaz para um requisito?"
        "Deve ser objetivo, mensurável e validável.":
            $ acertos_quiz += 1
            "Correto! Critérios claros facilitam os testes."
        "Deve ser bonito e agradar a equipe.":
            "Errado! O importante é ser testável e objetivo."
        "Serve só para a documentação ficar mais completa.":
            "Errado! O objetivo é garantir que o requisito seja atendido."

    menu:
        "O que significa 'code review'?"
        "Revisão do código por um colega para identificar melhorias e evitar bugs.":
            $ acertos_quiz += 1
            "Exato! Revisão colaborativa aumenta a qualidade."
        "Adicionar comentários bonitos no código.":
            "Nem sempre... O foco é melhorar o entendimento e a segurança."
        "Testar a performance do sistema.":
            "Não exatamente! Isso é importante, mas não é code review."

    "Você acerta [acertos_quiz] de 2 perguntas no quiz."

    menu:
        "Deseja estudar mais e fazer mais questões, ou avançar?"
        "Sim, quero responder mais perguntas!":
            $ acertos_extra = 0
            menu:
                "O que é TDD (Test Driven Development)?"
                "Desenvolver testes antes do código de produção.":
                    $ acertos_extra += 1
                    "Correto! TDD orienta o desenvolvimento pela validação constante."
                "Testar apenas depois de tudo pronto.":
                    "Errado! O ideal é testar o tempo todo."
                "É um relatório de bugs.":
                    "Não, TDD é uma prática de programação orientada a testes."

            menu:
                "Qual métrica mede a facilidade de manter o software ao longo do tempo?"
                "Manutenibilidade.":
                    $ acertos_extra += 1
                    "Correto! Manutenibilidade está entre os fatores de qualidade ISO."
                "Eficiência.":
                    "Eficiência é sobre performance, não manutenção."
                "Portabilidade.":
                    "Portabilidade está relacionada à capacidade de rodar em outros ambientes."

            "Você acerta [acertos_extra] de 2 perguntas no quiz extra."
            "O tempo voa enquanto você revisa conceitos e testa seus conhecimentos."

            # Padding de estudo — transição para noite
            play sound "audio/music_focus.ogg"
            scene bg escritorio_interior_noite
            with fade
            $ advance_minutes(32)
        "Prefiro avançar para as próximas tarefas.":
            "Você decide que já revisou o suficiente por hoje e fecha o notebook para descansar um pouco."

    # Estatísticas/resumo de desempenho do estudo
    $ total_acertos = acertos_quiz
    if "acertos_extra" in globals():
        $ total_acertos += acertos_extra
        $ total_perguntas = 4
    else:
        $ total_perguntas = 2

    "Resumo dos estudos:"
    "Você respondeu corretamente [total_acertos] de [total_perguntas] perguntas."

    if total_acertos == total_perguntas:
        "Excelente desempenho! Você desbloqueia o item especial: 'Medalha de Estudioso'."
        $ inventario.append("medalha_estudioso")
        play sound "audio/recompensa.ogg"
    elif total_acertos >= (total_perguntas // 2):
        "Bom desempenho! Continue praticando para ficar ainda mais afiado(a)."
    else:
        "Valeu o esforço! O importante é nunca parar de aprender."

    menu:
        "Gostaria de aprofundar algum tema?"
        "Sim, quero falar com [NOME_DEVELOPER_QUALITY] sobre qualidade de software.":
            show developer_quality positive at right_zoom
            developer_quality "Ótimo! Sempre recomendo ler sobre as métricas ISO/IEC 25010: manutenibilidade, funcionalidade, usabilidade, eficiência, confiabilidade, portabilidade e segurança."
            developer_quality "Se quiser, tenho um template de checklist para revisar requisitos e código. Vou te enviar por e-mail!"
            $ amizade_developer_quality += 1
            $ inventario.append("checklist_qualidade")
            hide developer_quality
        "Prefiro consultar [NOME_DEVELOPER_AI] para discutir machine learning.":
            show developer_ai positive at right_zoom
            developer_ai "Topa uma call? Posso te mostrar notebooks práticos de classificação, clusterização e até uns exemplos reais de predição de exames médicos."
            developer_ai "Ah, e tem vários datasets públicos para você experimentar algoritmos sem medo!"
            $ amizade_developer_ai += 1
            $ inventario.append("notebook_ml_exemplo")
            hide developer_ai
        "Vou pesquisar sozinho(a) por enquanto.":
            "Você decide seguir pelos seus próprios caminhos, mas anota dúvidas para discutir depois com a equipe."

    show developer_test enthusiastic at left_zoom
    developer_test "Se quiser revisar algum teste, me chama! Nada como aprender praticando."
    hide developer_test

    $ inventario.append("anotacoes_tecnicas")
    "Você salva suas anotações, fecha o notebook e sente-se pronto(a) para os desafios dos próximos dias."

    play music music_home_reflecting fadein 1.3
    scene bg quarto_noite
    with fade
    $ advance_minutes(18)

    "{i}Mais tarde, em casa, você compara suas anotações com o material das aulas. Agora entende, na prática, como o gerenciamento de riscos e o acompanhamento do cronograma são vitais para o sucesso de um projeto — bem além da teoria.{/i}"

    window hide
    pause 1.1
    window show

    "Fim da Semana 5\n\nAprendizado: Gestão de riscos e cronogramas não são só burocracia. Quando bem aplicados, garantem organização, transparência e qualidade no desenvolvimento de software."

    return
