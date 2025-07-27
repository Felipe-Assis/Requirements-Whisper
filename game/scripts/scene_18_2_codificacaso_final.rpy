label scene_18_2_codificacao_final:
    scene bg escritorio_interior_manha
    with dissolve

    play sound "audio/teclado.ogg"
    "Você chega cedo ao escritório, determinado(a) a finalizar o módulo de cadastro de pacientes com máxima qualidade."
    show developer_coding serious at left_zoom
    show developer_test enthusiastic at right_zoom

    developer_coding "Foco total agora, [player_name]. Lembre-se: pequenas revisões fazem grande diferença!"
    developer_test confident "Se quiser revisar juntos, estou por aqui. Vários olhos enxergam mais bugs!"

    # Mini-game visual: revisão/correção final
    "Você abre o PR (Pull Request) no sistema de versionamento, pronto para a revisão final."
    show expression "images/ui/pr_placeholder.png" as pr at center_zoom
    "No diff, identifica:"
    "1. Função pouco legível"
    "2. Campo sem validação"
    "3. Documentação técnica desatualizada"
    hide pr

    # Escolhas: o que priorizar primeiro (pode repetir até 2 vezes, tipo 'to-do')
    $ revisoes_realizadas = []
    $ revisoes_restantes = ["função", "validação", "documentação"]

    $ opcoes = [("função", "Refatora a função para código limpo."),
                ("validação", "Adiciona validação ao campo do formulário."),
                ("documentação", "Chama [NOME_DEVELOPER_QUALITY] para revisar documentação técnica."),
                ("automacao", "Pede dica para [NOME_DEVELOPER_AI] sobre automação de testes.")]
    $ revisoes = 0
    while revisoes < 2:
        menu:
            "Qual revisão deseja fazer agora?"
            "Refatora a função para código limpo." if "função" in revisoes_restantes:
                $ revisoes_realizadas.append("função")
                $ revisoes_restantes.remove("função")
                developer_coding positive "Excelente! Código limpo facilita a vida de todo mundo, inclusive a sua no futuro."
                $ amizade_developer_coding += 1
            "Adiciona validação ao campo." if "validação" in revisoes_restantes:
                $ revisoes_realizadas.append("validação")
                $ revisoes_restantes.remove("validação")
                developer_test thinking "Boa! Validação previne bugs e problemas para o usuário final."
                $ amizade_developer_test += 1
            "Chama [NOME_DEVELOPER_QUALITY] para revisar documentação." if "documentação" in revisoes_restantes:
                $ revisoes_realizadas.append("documentação")
                $ revisoes_restantes.remove("documentação")
                show developer_quality positive at center_zoom
                developer_quality "Ótima iniciativa! Documentação clara agiliza suporte e facilita onboarding de novos devs."
                $ amizade_developer_quality += 1
                hide developer_quality
            "Pede dica para [NOME_DEVELOPER_AI] sobre automação de testes.":
                developer_ai positive "Se quiser, te passo um script para rodar cenários de teste automaticamente!"
                $ amizade_developer_ai += 1
        $ revisoes += 1

    # Visual do checklist de revisão
    show expression "images/ui/checklist_placeholder.png" as checklist at right_zoom2
    "Checklist de revisão preenchido:"
    if "função" in revisoes_realizadas:
        "✔ Função refatorada"
    else:
        "✖ Função refatorada"
    if "validação" in revisoes_realizadas:
        "✔ Validação implementada"
    else:
        "✖ Validação implementada"
    if "documentação" in revisoes_realizadas:
        "✔ Documentação revisada"
    else:
        "✖ Documentação revisada"
    hide checklist

    # Breve comentário de outro NPC para dinâmica
    show developer_requirements positive at right_zoom2
    developer_requirements "Lembrem sempre de alinhar as implementações aos requisitos! Qualquer dúvida, me chama."
    hide developer_requirements

    # Padding: escolha de entrega
    menu:
        "Tudo pronto! Como deseja entregar o módulo?"
        "Faz uma demo para a equipe antes de dar merge.":
            developer_coding enthusiastic "Ótima prática! Demonstração facilita feedback imediato e fortalece o trabalho em equipe."
            developer_test positive "Assim todo mundo aprende com a solução!"
            $ amizade_developer_coding += 1
            $ amizade_developer_test += 1
            $ entrega_pr = "demo"
        "Comenta no pull request e detalha as decisões tomadas.":
            developer_coding positive "Transparência na revisão é fundamental. Isso é maturidade técnica!"
            $ amizade_developer_coding += 1
            $ entrega_pr = "pr"
        "Entrega direto, mas deixa um recado avisando no grupo.":
            developer_test neutral "Importante avisar, mas tente sempre garantir uma revisão coletiva antes. Previne sustos!"
            $ amizade_developer_test += 1
            $ entrega_pr = "direto"

    # Estatísticas finais e feedback
    "Resumo da revisão:"
    if len(revisoes_realizadas) == 2:
        "Você concluiu 2 revisões essenciais!"
        if "função" in revisoes_realizadas and "validação" in revisoes_realizadas:
            "Seu código ficou robusto, limpo e seguro!"
            $ inventario.append("badge_codigo_limpo")
    else:
        "Uma revisão só já faz diferença, mas sempre tente revisar mais."

    if entrega_pr == "demo":
        "Sua demonstração foi elogiada por todos!"
        $ inventario.append("badge_demo_colaborativa")
    elif entrega_pr == "pr":
        "Documentação detalhada do PR facilita a vida da equipe!"
        $ inventario.append("badge_pr_transparente")

    # Reflexão e recompensa extra para quem não se exauriu
    "Descansar antes de programar fez diferença. Sua mente está mais clara, e os colegas elogiam sua responsabilidade."
    "Você ganha o item 'Mindfulness Dev' no inventário."
    $ inventario.append("mindfulness_dev")

    # Feedback dos membros
    show developer_quality positive at right_zoom
    developer_quality "Parabéns, [player_name]! Seu compromisso com qualidade inspira o time."
    hide developer_quality
    show developer_ai positive at left_zoom
    developer_ai "Bora pensar juntos em automatizar ainda mais o fluxo na próxima sprint!"
    hide developer_ai

    scene bg escritorio_interior_tarde
    with fade

    scene bg escritorio_interior_tarde
    with fade

    # Resumo do progresso do dia
    "Módulo entregue, bugs corrigidos e feedbacks recebidos: sensação de evolução profissional e de equipe."
    "Você percebe como pequenas melhorias cotidianas levam a grandes resultados no longo prazo."

    # Fechamento da semana
    scene bg quarto_noite
    with fade
    "Em casa, você reflete sobre como descansar, planejar e revisar cada parte do código mudou a forma de encarar o projeto."
    "A teoria de boas práticas faz ainda mais sentido após superar um ciclo intenso de codificação."

    window hide
    pause 1.1
    window show

    "Fim da Semana 6\n\nAprendizado: Aplicar o que aprendeu na universidade traz confiança para inovar, resolver problemas e crescer na carreira de verdade."

    return