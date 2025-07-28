label scene_20_deploy_final:
    play music music_office_motivated fadein 1.0
    scene bg escritorio_interior_manha
    with fade

    $ advance_minutes(9)
    play sound "audio/ambiente_reuniao.ogg"
    "{i}O clima no escritório é de expectativa: hoje é dia de deploy! Todos estão presentes — a energia contagia.{/i}"

    show developer_management serious at left_zoom
    developer_management "Atenção, equipe! Chegou o grande momento. Vamos garantir que tudo esteja em ordem antes de ir para produção."

    show developer_quality positive at right_zoom
    developer_quality "Vamos passar pelo checklist final juntos! Documentar cada etapa é tão importante quanto programar."
    hide developer_quality

    window hide
    pause 1.1
    window show

    show expression "images/ui/checklist_deploy.png" as checklist at center_zoom
    "{i}Checklist final:\n• Código revisado\n• Testes automatizados rodando\n"
    "• Documentação atualizada\n• Backup realizado\n"
    "• Ambiente de produção pronto\n• Script de rollback disponível{/i}"
    hide checklist

    $ checklist_deploy = []
    $ acertos_deploy = 0

    menu:
        "Documentação está atualizada e fácil de acessar?"
        "Sim, revisamos e está no Wiki da equipe.":
            show developer_quality positive at right_zoom
            developer_quality "Ótimo! Isso ajuda até quem chegar na equipe depois. Pense em versionamento de documentação, se puder."
            hide developer_quality
        "Tem coisa solta no drive ainda...":
            show developer_quality thinking at right_zoom
            developer_quality "Cuidado! Documentação espalhada é receita para confusão no futuro — padronize e use um único repositório sempre."
            hide developer_quality

    "{i}Checklist parcial aprovado. Agora, sobre os testes...{/i}"

    menu:
        "Todos os testes passaram nos últimos commits?"
        "Sim, cobertura acima de 85\% e sem falhas.":
            show developer_test confident at right_zoom
            developer_test "Maravilha! Deploy seguro começa em teste bem feito. Não esqueça de olhar a pipeline do CI/CD."
            hide developer_test
        "Ficaram alguns testes quebrando, mas nada grave.":
            show developer_test thinking at right_zoom
            developer_test "Fique atento! Pequenos erros podem crescer lá na frente. Invista sempre em cobertura e em testes end-to-end!"
            hide developer_test

    "{i}Por fim, segurança dos dados:{/i}"

    menu:
        "Backup do banco e dos arquivos realizado?"
        "Sim, já salvei o backup em nuvem e local.":
            show developer_project positive at right_zoom
            developer_project "Responsabilidade é tudo! Melhor prevenir do que perder dados. Tenha rotina de restore testado."
            hide developer_project
        "Ainda não, mas vou fazer agora.":
            show developer_project serious at right_zoom
            developer_project "Nunca deixe para depois! Backup salva projetos e empregos. Documente sempre o hash do backup."
            hide developer_project

    "{i}Checklist concluído! Última pausa para café e integração do time.{/i}"

    play sound "audio/xicara_cafe.ogg"
    scene bg empresa_cafe_tarde
    with dissolve

    show developer_ai positive at left_zoom
    developer_ai "E aí, alguém afim de café antes do grande momento? Prometo só falar de IA se for na pausa!"
    show developer_quality positive at right_zoom2
    developer_quality "Café de deploy é tradição! E sempre junto de checklist!"
    show developer_test enthusiastic at center_zoom
    developer_test "Só não derruba no notebook, hein! (risos)"
    hide developer_ai
    hide developer_quality
    hide developer_test

    "{i}Entre goles e risadas, o time revisita aprendizados: boas práticas, comunicação, bugs superados, amizade e memes dos erros.{/i}"

    # Decisão de deploy
    scene bg escritorio_interior_tarde
    with dissolve
    $ advance_minutes(13)

    "{i}De volta à sala, é hora de decidir onde será feito o deploy. [NOME_DEVELOPER_CODING] e [NOME_DEVELOPER_PROJECT] trazem opções para debate.{/i}"

    show developer_coding serious at left_zoom
    show developer_project thinking at right_zoom
    developer_coding "Podemos ir pelo tradicional: servidor próprio, a gente controla tudo, mas depende da nossa manutenção e configuração de segurança."
    developer_project "Ou alugar uma instância em nuvem. É mais flexível, mas exige cuidado com escalabilidade, custos e configurações automáticas."
    show developer_ai positive at center_zoom
    developer_ai "E que tal usar Docker? Garante portabilidade, facilita rollback, e a infra vira código! Posso configurar o pipeline CI/CD se quiserem."
    hide developer_ai

    menu:
        "Qual estratégia de deploy você sugere para a equipe?"
        "Servidor próprio, controle total sobre tudo.":
            show developer_coding positive at left_zoom
            developer_coding "Gosto! Se bem configurado, é seguro. Só lembre de atualizar tudo sempre, manter firewall e logs ativos."
            hide developer_coding
        "Nuvem, mais flexibilidade para crescer e menos dor de cabeça com hardware.":
            show developer_project positive at right_zoom
            developer_project "Ótima escolha para um sistema escalável. Só fique de olho no billing! E prefira regiões brasileiras para dados de saúde."
            hide developer_project
        "Docker, CI/CD e tudo automatizado, mirando o futuro!":
            show developer_ai enthusiastic at center_zoom
            developer_ai "Amo! Menos dependência, mais agilidade — e menos 'funciona só na minha máquina'! Automatize os secrets e tokens, hein."
            hide developer_ai

    # Intervenção divertida: ligação do stakeholder (mensagem no celular)
    play sound "audio/cell_vibration.ogg"
    show expression "images/ui/phone_placeholder.png" at right_zoom2
    "{i}Seu celular vibra: é o stakeholder ansioso, querendo saber do deploy.{/i}"
    show developer_requirements thinking at left_zoom
    developer_requirements "(no viva-voz) Pode ficar tranquilo, Dr. Almeida! A equipe está conferindo tudo, logo estará no ar!"
    hide developer_requirements

    "{i}O time troca olhares e sorri, sentindo a pressão e a responsabilidade do momento. Hora de unir forças para o grande push final!{/i}"

    # Mini-game: Resolver último bug crítico antes do deploy (simulado)
    scene bg escritorio_interior_tarde
    with dissolve
    $ advance_minutes(8)

    "{i}Tudo pronto... mas um bug crítico aparece no teste final: sistema trava quando cadastra mais de 1000 pacientes.{/i}"
    show developer_test thinking at left_zoom
    developer_test "Bora debugar rapidinho? Time unido resolve tudo!"
    hide developer_test

    menu:
        "Como você resolve o bug crítico?"
        "Identifico vazamento de memória e otimizo a função.":
            show developer_coding positive at left_zoom
            developer_coding "Mandou bem! Resolver esse tipo de problema rápido é sinal de desenvolvedor experiente. Já documenta a solução para evitar recorrência."
            hide developer_coding
        "Divido a tarefa com [NOME_DEVELOPER_AI] e [NOME_DEVELOPER_PROJECT] para achar o gargalo.":
            show developer_ai positive at center_zoom
            show developer_project positive at right_zoom
            developer_ai "Em equipe vai mais rápido! Já rodando scripts de profiling e análise de heap."
            developer_project "Localizei uma query lenta, otimizando agora. Valeu pela parceria!"
            hide developer_ai
            hide developer_project
        "Rodo um script de rollback para evitar downtime e aviso a todos.":
            show developer_quality positive at right_zoom
            developer_quality "Ótima decisão! Mais vale um sistema seguro do que um deploy apressado. Avise os stakeholders da nova previsão de entrega."
            hide developer_quality

    # Exibe placeholder de tela de sucesso do deploy
    show expression "images/ui/placeholder_sucesso_deploy.png" as sucesso at center_zoom
    "{i}A equipe vê a mensagem: 'Deploy realizado com sucesso! Parabéns!' — O sistema está oficialmente no ar, com monitoramento ativo e checklist final arquivado.{/i}"
    hide sucesso

    # Feedback coletivo — clima de vitória
    play sound "audio/aplausos.ogg"
    show developer_management enthusiastic at left_zoom
    show developer_quality positive at right_zoom
    show developer_test positive at center_zoom
    show developer_ai enthusiastic at right_zoom2
    developer_management "Parabéns, equipe! Deploy concluído. Cliente feliz, usuários protegidos, e aprendizados para a vida toda."
    developer_quality "Qualidade até o fim! Vocês mostraram o que é Engenharia de Software na prática."
    developer_test "Bugs não tiveram vez! Orgulho do time."
    developer_ai "Vamos comemorar! Pizza hoje é por minha conta — mas só depois de um último backup!"
    hide developer_management
    hide developer_quality
    hide developer_test
    hide developer_ai

    # Clima de celebração, padding, reflexões finais (mas sem conquistas)
    scene bg escritorio_interior_noite
    with fade
    $ advance_minutes(29)
    "{i}Ao cair da noite, a equipe celebra. Você sente orgulho do caminho, das amizades e da carreira que começa a construir.{/i}"
    "{i}Relembra cada desafio, cada sprint, cada conceito, cada apoio dos colegas e até os bugs superados com bom humor.{/i}"
    "{i}O projeto está online, mas a avaliação final ainda está por vir...{/i}"

    window hide
    pause 1.2
    window show

    "{i}Fim da Semana 8 – O projeto foi entregue com excelência!\n\nAprendizado: Deploy é muito mais do que apertar um botão — é o resultado de planejamento, testes, comunicação, domínio técnico e espírito de equipe.{/i}"

    return
