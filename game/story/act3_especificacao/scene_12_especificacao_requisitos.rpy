label scene_12_especificacao_requisitos:
    $ set_available("developer_ai", "developer_coding", "developer_management", "developer_project", "developer_security", "developer_test")

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

    "Checklist de inspeção:\n• Alguma informação importante está ausente?\n• Existe ambiguidade (dupla interpretação)?\n• Alguma regra está inconsistente ou contraditória?\n• Tem algum detalhe estranho, que foge do contexto ou da linguagem do usuário?\n• O requisito é testável, específico e mensurável?"

    "{i}Vocês abrem juntos o documento de requisitos e começam a analisar linha por linha.{/i}"
    developer_requirements "Vamos revisar juntos alguns exemplos reais? Em cada um, procure o problema que mais pesa."

    window hide
    pause 0.4
    window show

    "\"RF01: O sistema deve permitir o cadastro do paciente conforme a seção de Identificação do formulário de história clínica.\"\n\"Critério de aceitação: Cadastro validado e paciente exibido imediatamente na listagem, com todos os campos obrigatórios destacados e verificados.\""

    "{i}Você percebe que faltava detalhar quais campos são obrigatórios e como validar duplicidade de CPF, como a [NOME_DOUTORA_1] pediu na entrevista. Corrige no documento e sinaliza como melhoria.{/i}"

    show developer_requirements neutral at left_zoom
    developer_requirements "Excelente! Agora veja esse:"

    window hide
    pause 0.4
    window show

    # EXEMPLO 1: informação ausente (resposta parcial)
    "\"RF05A: O sistema deve permitir o cálculo automático de escore da escala HAD, conforme a pontuação das respostas do paciente.\""
    developer_requirements "Está claro? O que pode faltar aqui?"
    call pista_lembrar("saude_p_had") from _pl_s12_had

    menu (tipo="trabalho"):
        "1 de 4 · Qual problema pesa mais neste requisito?"
        "Está bom assim: o cálculo da HAD é conhecido, cada dev sabe fazer.":
            $ decisao("saude_d12_had", False)
            show developer_requirements thinking at left_zoom
            developer_requirements "Se ninguém escrever, cada pessoa implementa de um jeito. E tem uma pergunta que o texto não responde: e se faltar resposta?"
        "Acrescentaria que o resultado deve aparecer de forma bonita e intuitiva.":
            $ decisao("saude_d12_had", False)
            show developer_requirements thinking at left_zoom
            developer_requirements "\"Bonita\" e \"intuitiva\" não dá para testar. E o buraco principal continua: o que acontece quando o paciente não termina?"
        "Faltou dizer o que fazer se o paciente não responder todas as perguntas.":
            if decisao("saude_d12_had", True):
                $ add_friendship_point("developer_requirements", 1)
            show developer_requirements positive at left_zoom
            developer_requirements "Boa! Informação ausente."

    if not aprendizagem.get("saude_d12_had"):
        menu (tipo="trabalho"):
            "Como você revisa a análise?"
            "Registro a dúvida: o que o sistema faz quando o paciente deixa perguntas sem resposta?":
                pass

    developer_requirements "Lembra do UC5? Lá combinamos salvar parcial. O requisito precisa dizer isso também: salva parcial, avisa ou bloqueia o envio."

    # EXEMPLO 2: informação ausente (lista e casos fora dela)
    window hide
    pause 0.3
    window show

    "\"RF06: O sistema deve permitir o cadastro da História de Uso de Outras Substâncias Psicoativas do paciente, conforme o formulário de história clínica.\""
    show developer_requirements neutral at left_zoom
    developer_requirements "Esse parece completo, mas... há algo estranho ou ausente?"

    menu (tipo="trabalho"):
        "2 de 4 · Qual problema você identifica?"
        "Faltam a lista de substâncias e o que fazer com uma que não está na lista.":
            if decisao("saude_d12_substancias", True):
                $ add_friendship_point("developer_requirements", 1)
            show developer_requirements positive at left_zoom
            developer_requirements "Perfeito! Sem a lista, cada pessoa imagina um formulário diferente."
        "Está completo, porque cita o formulário de história clínica.":
            $ decisao("saude_d12_substancias", False)
            show developer_requirements thinking at left_zoom
            developer_requirements "Citar o formulário ajuda, mas quem lê o requisito não sabe quais substâncias entram, nem o que fazer com uma que não aparece lá."
        "Deveria dizer que o cadastro precisa ser rápido.":
            $ decisao("saude_d12_substancias", False)
            show developer_requirements thinking at left_zoom
            developer_requirements "\"Rápido\" é vago, e não é o ponto fraco deste requisito. O que falta é o conteúdo do cadastro."

    if not aprendizagem.get("saude_d12_substancias"):
        menu (tipo="trabalho"):
            "Como você revisa a análise?"
            "Peço a lista de substâncias e um campo \"outra\" para os casos fora dela.":
                pass

    developer_requirements "O requisito passa a listar exemplos, como álcool, maconha e cocaína, e prevê um campo \"outra\" com descrição."

    # EXEMPLO 3: valores de fronteira
    window hide
    pause 0.3
    window show

    "\"RF08A: O sistema deve permitir o cálculo automático da dependência tabágica do paciente com base na escala de Fagerström. Para informar a dependência tabágica, considerar pontuações: entre 0 e 2 == Muito baixa; 3 e 4 Baixa; 5 == Média; 6 e 7 == Elevada; entre 8 e 10 == Muito Elevada.\""
    show developer_requirements neutral at left_zoom
    developer_requirements "Esse é mais detalhado, mas ainda pode ser melhor. Vê algum ponto a aprimorar?"

    menu (tipo="trabalho"):
        "3 de 4 · Qual ponto você sugere?"
        "Trocaria os \"==\" por palavras, para o texto ficar mais elegante.":
            $ decisao("saude_d12_fagerstrom", False)
            show developer_requirements thinking at left_zoom
            developer_requirements "A forma pode melhorar, mas isso não muda o comportamento do sistema. O risco está nos valores que a tabela não cobre."
        "Tiraria a tabela do requisito; a equipe consulta a escala depois.":
            $ decisao("saude_d12_fagerstrom", False)
            show developer_requirements thinking at left_zoom
            developer_requirements "Sem a tabela, cada pessoa pode usar uma versão da escala. É ela que torna o cálculo verificável."
        "Falta dizer o que fazer com pontuação fora de 0 a 10 e testar as fronteiras.":
            if decisao("saude_d12_fagerstrom", True):
                $ add_friendship_point("developer_requirements", 1)
            show developer_requirements positive at left_zoom
            developer_requirements "Importantíssimo! É nas bordas que o cálculo costuma errar."

    if not aprendizagem.get("saude_d12_fagerstrom"):
        menu (tipo="trabalho"):
            "Como você revisa a análise?"
            "Acrescento a regra para valores fora de 0 a 10 e casos de teste nas fronteiras.":
                pass

    developer_requirements "O critério de aceitação ganha os valores de fronteira: 2 e 3, 4 e 5, 7 e 8, e um valor inválido como 11, que deve ser recusado."

    # EXEMPLO 4: não funcional, como medir
    window hide
    pause 0.3
    window show

    "\"DR01: O sistema deve garantir que o tempo de resposta para carregamento completo das interfaces de cadastro de paciente e consulta ao prontuário clínico seja inferior a 2 segundos, em pelo menos 95\% das requisições realizadas sob carga normal (até 100 usuários simultâneos), em ambiente de produção.\""
    show developer_requirements neutral at left_zoom
    developer_requirements "Agora um de desempenho. Vê alguma ambiguidade ou informação que precisa de reforço?"

    menu (tipo="trabalho"):
        "4 de 4 · Qual análise você faz?"
        "Melhor trocar por \"o sistema deve ser rápido\", fica mais simples.":
            $ decisao("saude_d12_desempenho", False)
            show developer_requirements thinking at left_zoom
            developer_requirements "Mais simples, mas impossível de testar. O texto atual já tem números; o que falta é outra coisa."
        "Falta dizer como medir: ferramenta, cenário de carga e quais telas entram.":
            if decisao("saude_d12_desempenho", True):
                $ add_friendship_point("developer_requirements", 1)
            show developer_requirements positive at left_zoom
            developer_requirements "Boa! Sem isso, cada equipe testa de um jeito e chega a um número diferente."
        "Baixaria o limite para 1 segundo, por segurança.":
            $ decisao("saude_d12_desempenho", False)
            show developer_requirements thinking at left_zoom
            developer_requirements "Mudar o número sem falar com as doutoras é decidir por elas. E continuaria sem dizer como medir."

    if not aprendizagem.get("saude_d12_desempenho"):
        menu (tipo="trabalho"):
            "Como você revisa a análise?"
            "Descrevo como medir: a ferramenta, o cenário de carga e as telas incluídas.":
                pass

    developer_requirements "E o cenário de \"carga normal\" a gente alinha com o Instituto, para medir do mesmo jeito que elas vão usar."
    $ advance_minutes(20)

    "{i}Vocês seguem aplicando o checklist nos próximos requisitos, encontrando e corrigindo detalhes ausentes ou ambíguos, e ajustando a linguagem técnica para a do usuário final.{/i}"
    $ registrar("saude_reg_inspecao")

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

    menu (tipo="conversa"):
        "Como você reage ao processo de inspeção?"
        "Agradece e valoriza o olhar crítico do time.":
            $ add_friendship_point("developer_quality", 1)
            show developer_quality positive at right_zoom
            developer_quality "É assim que se aprende! Inspeção rigorosa agora evita dor de cabeça depois."
        "Fica com receio de nunca acertar tudo.":
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
    $ advance_minutes(10)

    # Pedido novo: escrita livre de requisito e critério, com autoavaliação.
    play sound "audio/effects/cell_vibration.ogg"
    show doutora_2 portrait at right_zoom
    doutora_2 "(mensagem pelo app) Oi, [player_name]! Lembrei de uma coisa. Quando um paciente falta ao retorno, a gente só percebe semanas depois. Queria ser avisada no mesmo dia, para tentar remarcar antes que ele desista do tratamento."
    hide doutora_2
    show developer_requirements thinking at left_zoom
    developer_requirements "Pedido novo, e chegou na hora certa. Que tal você escrever esse? Um requisito e um critério de aceitação, usando o checklist."
    if amb_resultados.get("saude_amb_historico", {}).get("concluido"):
        developer_requirements "É o alerta que a gente destrinchou na caça à ambiguidade. Agora ela contou o motivo. Escreve inteiro, com critério."
    developer_requirements "Não precisa ficar perfeito. Depois a gente revisa junto e confirma com ela."
    hide developer_requirements

    call exercicio_escrita("saude_escrita", _("Pedido da equipe clínica: quando um paciente faltar à consulta de retorno, a profissional que acompanha o caso quer ser avisada no mesmo dia, para tentar remarcar antes que ele abandone o tratamento."))

    show developer_requirements positive at left_zoom
    if escritas.get("saude_escrita", {}).get("status") == "confirmado":
        developer_requirements "Ficou guardado. Vou mostrar para a [NOME_DOUTORA_2] e ver se o critério bate com o que ela imagina."
    else:
        developer_requirements "Sem problema deixar pendente. Rascunho guardado já é meio caminho; depois a gente fecha junto."
    hide developer_requirements

    play music music_office_relaxed fadein 1.5
    scene bg escritorio_interior_noite
    with fade
    $ advance_minutes(18)
    $ energia_gastar(1, _("especificação até a noite"))
    "{i}Fim de tarde, sensação de dever cumprido. Com o checklist completo e o documento revisado, você sente que o projeto está cada vez mais sólido.{/i}"
    "{i}Colaborar e inspecionar juntos mostrou como cada detalhe faz diferença na Engenharia de Software real.{/i}"

    return
