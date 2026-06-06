label scene_16_reuniao_gerenciamento:
    $ disponivel_developer_ai = False
    $ disponivel_developer_coding = False
    $ disponivel_developer_management = False
    $ disponivel_developer_requirements = False
    $ disponivel_developer_project = True
    $ disponivel_developer_quality = False
    $ disponivel_developer_security = True
    $ disponivel_developer_test = False

    play music music_office_focused fadein 1.0
    scene bg escritorio_interior_manha
    with dissolve

    play sound "audio/effects/ambiente_reuniao.ogg"
    $ advance_minutes(8)
    "{i}O novo dia começa com o time reunido em torno do quadro branco. A luz da manhã invade a sala enquanto todos ajeitam seus blocos de anotações e cafés.{/i}"

    show developer_management serious at left_zoom
    show developer_requirements thinking at right_zoom

    developer_management "Vamos revisar nosso cronograma e discutir riscos do projeto. Gerenciar bem o tempo e priorizar as tarefas é tão importante quanto codar."
    developer_requirements "Trouxe aqui a lista de funcionalidades e requisitos priorizados. Lembrem: nem tudo cabe na primeira entrega."

    # Exibição visual do cronograma (placeholder)
    show expression "images/diagrams/placeholder_cronograma.png" as cronograma at center_zoom
    "{i}No projetor, aparece o cronograma inicial do projeto (placeholder). Você nota algumas tarefas críticas destacadas e outras de menor prioridade.{/i}"

    # NOVO BLOCO: Discussão de andamento
    show developer_management thinking at left_zoom
    developer_management "Antes de tudo, queria ouvir vocês: como sentem o andamento do projeto até aqui?"
    menu:
        "Como você avalia o progresso do time?"
        "Acho que estamos no ritmo certo, entregando com qualidade.":
            show developer_requirements positive at right_zoom
            developer_requirements "Bom ouvir isso! Mas lembrem de sempre registrar obstáculos — mesmo pequenos, podem virar bola de neve."
            show developer_management thinking at left_zoom
            developer_management "Ótimo, sigamos atentos às prioridades do sprint."
        "Acredito que estamos ficando um pouco para trás no cronograma.":
            show developer_requirements serious at right_zoom
            developer_requirements "Ótima percepção! Melhor revisar tarefas pendentes e entender os gargalos antes que virem problema maior."
            show developer_management serious at left_zoom
            developer_management "Podemos revisar entregáveis e negociar prazos, se necessário. Transparência é tudo."
        "Sinto que tem muito retrabalho ou dúvida sobre o que priorizar.":
            show developer_requirements thinking at right_zoom
            developer_requirements "Talvez falte clareza nos critérios de pronto. Podemos revisar juntos as definições de done?"
            show developer_management serious at left_zoom
            developer_management "Se a documentação ou a comunicação não estiver clara, vale dedicar um tempo para alinhar tudo."

    # Avaliação sobre o prazo (diretiva do usuário)
    show developer_management serious at left_zoom
    developer_management "E sobre o prazo: alguém acha que o cronograma está ficando apertado?"
    menu:
        "Como você responde sobre o prazo?"
        "Sim, algumas tarefas estão demorando mais do que o previsto.":
            show developer_coding thinking at right_zoom2
            developer_coding "A complexidade aumentou, vale dividir tarefas ou renegociar datas."
            show developer_management thinking at left_zoom
            developer_management "É papel da liderança escutar e ajustar expectativas. Vamos adaptar juntos."
        "Ainda está sob controle, mas precisamos de atenção redobrada.":
            show developer_ai positive at left_zoom_2
            developer_ai "Se quiserem, posso ajudar automatizando alertas de progresso ou pendências."
            show developer_management positive at left_zoom
            developer_management "Bom! Manter vigilância evita surpresas. Qualquer dúvida, tragam antes de virar urgência."
        "Acho que alguns prazos estão folgados demais, dá para desafiar mais o time.":
            show developer_test enthusiastic at right_zoom2
            developer_test "Gosto desse espírito! Se quiserem me passar mais cenários de teste, eu topo."
            show developer_management serious at left_zoom
            developer_management "Cuidado só para não sacrificar a qualidade pelo ritmo. Equilíbrio é o segredo."

    # Limpa gerentes para nova rodada
    hide developer_management
    hide developer_requirements

    # Menu clássico sobre priorização
    show developer_coding neutral at left_zoom
    show developer_ai positive at right_zoom
    developer_coding "Só não esqueçam de reservar tempo para code review! Melhor ajustar agora do que apagar incêndio depois."
    developer_ai "Se quiserem, posso automatizar parte do acompanhamento do progresso com scripts e alertas."
    hide developer_coding
    hide developer_ai

    menu:
        "Como você sugere organizar o trabalho da equipe?"
        "Priorizar tarefas de maior impacto, mesmo que sejam mais complexas.":
            $ flag_prioridade = "impacto"
            show developer_management thinking at right_zoom
            show developer_requirements enthusiastic at left_zoom
            developer_management "Faz sentido. Entregando o que traz mais valor, já mostramos resultado."
            developer_requirements "Mas precisamos garantir que os requisitos estejam bem refinados para evitar retrabalho!"
        "Atacar primeiro as tarefas mais rápidas para mostrar progresso.":
            $ flag_prioridade = "entregaveis_rapidos"
            show developer_management thinking at right_zoom
            show developer_requirements serious at left_zoom
            developer_management "Entregar rápido motiva o time, só não podemos perder de vista as demandas mais críticas."
            developer_requirements "E atenção para não deixar as tarefas grandes acumularem para o fim!"
        "Dividir o time em duplas para que todos avancem juntos, equilibrando desafios.":
            $ flag_prioridade = "colaborativo"
            show developer_management thinking at right_zoom
            show developer_requirements positive at left_zoom
            developer_management "Gosto da ideia! Trabalho em duplas estimula troca de conhecimento."
            developer_requirements "Assim todo mundo aprende e ninguém fica sobrecarregado!"

    hide developer_management
    hide developer_requirements

    # Decisão estratégica (com flag de risco)
    menu:
        "Como lidar com riscos e imprevistos?"
        "Planejar reuniões rápidas diárias para monitorar e ajustar o plano.":
            $ flag_risco = "daily"
            show developer_management serious at left_zoom
            show developer_requirements positive at right_zoom
            developer_management "Ótimo. Comunicação constante evita surpresas desagradáveis."
            developer_requirements "E se surgir dúvida, alinhamos tudo na hora!"
        "Criar um documento de riscos e revisá-lo semanalmente.":
            $ flag_risco = "documento"
            show developer_management thinking at left_zoom
            show developer_requirements thinking at right_zoom
            developer_management "Boa prática! Assim ninguém esquece dos pontos críticos."
            developer_requirements "Vale também pedir que cada membro anote possíveis riscos em suas tarefas."
        "Confiar no time para resolver problemas conforme eles aparecem.":
            $ flag_risco = "ad_hoc"
            show developer_management thinking at left_zoom
            show developer_requirements serious at right_zoom
            developer_management "Temos um time competente, mas recomendo cautela para não sermos reativos demais."
            developer_requirements "A experiência conta, mas planejamento é sempre um diferencial."

    hide cronograma
    hide developer_management
    hide developer_requirements

    scene bg escritorio_interior_tarde
    with dissolve
    play sound "audio/effects/xicara_cafe.ogg"
    $ advance_minutes(25)
    "{i}Horas depois, já à tarde, o time faz uma pausa para um café rápido e revisão das decisões.{/i}"

    show developer_requirements positive at left_zoom
    show developer_management thinking at right_zoom
    developer_requirements "Gostei das ideias de hoje. Cronograma atualizado, riscos mapeados e time motivado."
    developer_management "Agora é garantir o foco e manter o ritmo. Se precisar de apoio, estou sempre por aqui para alinhar ou destravar qualquer pendência."

    hide developer_management
    hide developer_requirements

    show developer_quality positive at center_zoom
    developer_quality "Não esqueçam: registrar tudo no nosso wiki ajuda muito quem entrar depois. Documentação de gestão é qualidade também!"
    hide developer_quality

    "{i}Você percebe como o gerenciamento não é só tarefa do gerente, mas uma responsabilidade compartilhada. Comunicação, registro e colaboração: essas são as ferramentas de times de alta performance.{/i}"

    play music music_office_relaxed fadein 1.5
    scene bg escritorio_interior_noite
    with fade
    "{i}O dia termina com o sentimento de que o projeto está bem encaminhado e que, juntos, a equipe pode encarar qualquer desafio.{/i}"

    return
