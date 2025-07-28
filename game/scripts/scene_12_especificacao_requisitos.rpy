label scene_12_especificacao_requisitos:
    play music music_office_focused_2 fadein 1.0
    scene bg escritorio_interior_tarde
    with dissolve

    $ advance_minutes(8)
    "{i}De volta à sala de trabalho, você e [NOME_DEVELOPER_REQUIREMENTS] se preparam para transformar todos os requisitos levantados em uma especificação formal.{/i}"

    show developer_requirements thinking at left_zoom
    developer_requirements "Agora é hora de revisar cada requisito com rigor. Antes de documentar, vamos aplicar uma inspeção: identificar informação ausente, ambígua ou estranha. É isso que separa um requisito robusto de um retrabalho futuro!"

    "{i}No quadro branco, [NOME_DEVELOPER_REQUIREMENTS] escreve os principais pontos do checklist de inspeção:{/i}"
    window hide
    pause 0.4
    window show

    "\"Checklist de Inspeção:\n• Alguma informação importante está ausente?\n• Existe ambiguidade (dupla interpretação)?"
    "• Alguma regra está inconsistente ou contraditória?"
    "\n• Tem algum detalhe estranho, que foge do contexto ou da linguagem do usuário?"
    "\n• O requisito é testável, específico e mensurável?\""

    "{i}Vocês abrem juntos o documento de requisitos e começam a analisar linha por linha. [NOME_DEVELOPER_REQUIREMENTS] propõe: {/i}"
    developer_requirements "Vamos revisar juntos alguns exemplos reais?"

    window hide
    pause 0.4
    window show

    "\"RF01: O sistema deve permitir o cadastro do paciente conforme a seção de Identificação do formulário de história clínica.\"\n"
    "\"Critério de aceitação: Cadastro validado e paciente exibido imediatamente na listagem, com todos os campos obrigatórios destacados e verificados.\""

    "{i}Você percebe que faltava detalhar quais campos são obrigatórios e como validar duplicidade de CPF. Corrige no documento e sinaliza como melhoria.{/i}"

    show developer_requirements neutral at left_zoom
    developer_requirements "Excelente! Agora veja esse:"

    window hide
    pause 0.4
    window show

    "\"RF05A: O sistema deve permitir o cálculo automático de escore da escala HAD, conforme a pontuação das respostas do paciente.\""
    "\"Está claro? O que pode faltar aqui?\""

    menu:
        "Como você responde?"
        "Faltou dizer o que fazer se o paciente não responder todas as perguntas.":
            $ add_friendship_point("developer_requirements", 1)
            show developer_requirements positive at left_zoom
            developer_requirements "Boa! Informação ausente. Devemos definir se o sistema salva parcial, exibe aviso ou bloqueia o envio."
        "A fórmula do cálculo não está descrita no requisito.":
            $ add_friendship_point("developer_requirements", 1)
            show developer_requirements positive at left_zoom
            developer_requirements "Ótima percepção! Se não detalhar, cada dev pode implementar de um jeito."
        "Está um pouco ambíguo: 'pontuação das respostas' pode gerar interpretações diferentes.":
            $ add_friendship_point("developer_requirements", 1)
            show developer_requirements thinking at left_zoom
            developer_requirements "Exatamente! Precisa ser específico. Melhor já linkar o método de cálculo no anexo da especificação."

    # EXEMPLO 2
    window hide
    pause 0.3
    window show

    "\"RF06: O sistema deve permitir o cadastro da História de Uso de Outras Substâncias Psicoativas do paciente, conforme o formulário de história clínica.\""
    developer_requirements "Esse parece completo, mas... há algo estranho ou ausente?"

    menu:
        "Qual problema você identifica?"
        "Faltam exemplos de substâncias para não deixar dúvidas.":
            $ add_friendship_point("developer_requirements", 1)
            show developer_requirements positive at left_zoom
            developer_requirements "Perfeito! Informação ausente ou ambígua. O formulário deve listar exemplos: álcool, maconha, cocaína, etc., ou permitir cadastrar outras substâncias."
        "Como o sistema deve lidar com substâncias não listadas?":
            $ add_friendship_point("developer_requirements", 1)
            show developer_requirements positive at left_zoom
            developer_requirements "Ótima observação. Sempre prever campo 'outros' ou permitir customização."
        "Não há indicação se é campo obrigatório ou opcional.":
            $ add_friendship_point("developer_requirements", 1)
            show developer_requirements positive at left_zoom
            developer_requirements "Bem visto! A obrigatoriedade tem que estar clara e visível no requisito."

    # EXEMPLO 3
    window hide
    pause 0.3
    window show

    "\"RF08A: O sistema deve permitir o cálculo automático da dependência tabágica do paciente com base na escala de Fagerström."
    " Para informar a dependência tabágica, considerar pontuações:"
    " entre 0 e 2 == Muito baixa; 3 e 4 Baixa; 5 == Média; 6 e 7 == Elevada; entre 8 e 10 == Muito Elevada.\""
    developer_requirements "Esse é mais detalhado, mas ainda pode ser melhor. Vê algum ponto a aprimorar?"

    menu:
        "Qual ponto você sugere?"
        "Faltou explicar como o sistema informa o resultado ao usuário.":
            $ add_friendship_point("developer_requirements", 1)
            show developer_requirements positive at left_zoom
            developer_requirements "Exatamente! O requisito deve descrever se a classificação aparece em tela, em relatório ou ambos."
        "A tabela de classificação devia estar como anexo para fácil consulta.":
            $ add_friendship_point("developer_requirements", 1)
            show developer_requirements thinking at left_zoom
            developer_requirements "Boa ideia! Ajuda muito para manutenção e revisão futura."
        "É preciso garantir que o cálculo não aceita valores fora do esperado.":
            $ add_friendship_point("developer_requirements", 1)
            show developer_requirements positive at left_zoom
            developer_requirements "Importantíssimo! Testes de fronteira devem estar especificados nos critérios de aceitação."

    # EXEMPLO 4 (não funcional, colaborativo)
    window hide
    pause 0.3
    window show

    "\"DR01: O sistema deve garantir que o tempo de resposta para carregamento completo das interfaces de cadastro de paciente e consulta ao prontuário clínico seja inferior a 2 segundos,"
    " em pelo menos 95\% das requisições realizadas sob carga normal (até 100 usuários simultâneos), em ambiente de produção.\""
    show developer_requirements neutral at left_zoom
    developer_requirements "Agora um de desempenho. Vê alguma ambiguidade ou informação que precisa reforço?"

    menu:
        "Qual análise você faz?"
        "É preciso definir como será feita a medição (ferramenta, cenário de teste)." :
            $ add_friendship_point("developer_requirements", 1)
            show developer_requirements positive at left_zoom
            developer_requirements "Boa! O critério de validação precisa ser bem descrito, senão cada equipe pode testar de forma diferente."
        "Faltou detalhar quais interfaces exatamente entram na regra.":
            $ add_friendship_point("developer_requirements", 1)
            show developer_requirements positive at left_zoom
            developer_requirements "Ótima percepção! O requisito deve listar explicitamente as telas envolvidas."
        "A definição de 'carga normal' pode ser diferente para cada clínica.":
            $ add_friendship_point("developer_requirements", 1)
            show developer_requirements thinking at left_zoom
            developer_requirements "Justo! O cenário e parâmetros de teste devem ser alinhados com o cliente."

    "{i}Vocês seguem aplicando o checklist nos próximos requisitos, encontrando e corrigindo detalhes ausentes ou ambíguos, e ajustando linguagem técnica para a do usuário final.{/i}"

    show developer_quality serious at right_zoom
    developer_quality "Deixa eu inspecionar também? Requisito estranho ou fora do padrão a gente corta antes de complicar pro time!"
    show developer_requirements enthusiastic at left_zoom
    developer_requirements "Combinado! Cada olhar extra diminui o risco de erro."

    show developer_quality thinking at right_zoom
    developer_quality "Aliás, já ouviu falar nas categorias clássicas? Informação ausente, ambígua, inconsistente, redundante, estranha... Tente identificar pelo menos uma delas em cada revisão!"
    "{i}Vocês debatem exemplos, e [NOME_DEVELOPER_QUALITY] destaca um erro clássico:{/i}"

    window hide
    pause 0.3
    window show

    "\"Requisito estranho: 'O sistema deve exibir gráficos 3D animados.' — Será mesmo necessário? Está alinhado ao contexto da clínica?\""

    menu:
        "Como você reage ao processo de inspeção?"
        "Agradece e valoriza o olhar crítico do time.":
            $ add_friendship_point("developer_quality", 1)
            show developer_quality positive at right_zoom
            developer_quality "É assim que se aprende! Inspeção rigorosa agora evita dor de cabeça depois."
        "Fica inseguro(a), acha que nunca vai acertar tudo.":
            show developer_quality enthusiastic at right_zoom
            developer_quality "Todo mundo já esqueceu detalhe uma vez. Ninguém revisa sozinho, confie no processo!"
        "Acha cansativo, mas entende o valor.":
            show developer_quality thinking at right_zoom
            developer_quality "Revisar é chato, mas um requisito mal especificado causa problemas por meses!"

    show developer_requirements positive at left_zoom
    developer_requirements "Ótimo trabalho, [player_name]! Revisar, inspecionar e documentar faz toda a diferença para o sucesso do projeto."

    hide developer_requirements
    hide developer_quality

    play sound "audio/effects/cell_vibration.ogg"
    show developer_ai portrait at left_zoom
    developer_ai "(mensagem no grupo) Fiquei animado com a revisão! Um dia quero automatizar parte desse checklist com IA, viu? (risos)"
    hide developer_ai

    play music music_office_relaxed fadein 1.5
    scene bg escritorio_interior_noite
    with fade
    $ advance_minutes(28)
    "{i}Fim de tarde, sensação de dever cumprido. Com o checklist completo e o documento revisado, você sente que o projeto está cada vez mais sólido.{/i}"
    "{i}Colaborar e inspecionar juntos mostrou como cada detalhe faz diferença na Engenharia de Software real.{/i}"

    return
