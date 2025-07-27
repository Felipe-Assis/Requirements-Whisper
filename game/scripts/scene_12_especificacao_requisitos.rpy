label scene_12_especificacao_requisitos:
    scene bg escritorio_interior_tarde
    with dissolve

    "{i}De volta à sala de trabalho, você e [NOME_DEVELOPER_REQUIREMENTS] se preparam para transformar todos os requisitos levantados em uma especificação formal.{/i}"

    show developer_requirements thinking at left_zoom
    developer_requirements "Esse é o momento de organizar tudo: separar requisitos funcionais, regras de negócio, critérios de aceitação..."
    developer_requirements "Te mostro um modelo de especificação — mas sinta-se livre para propor melhorias!"

    "{i}No quadro branco, [NOME_DEVELOPER_REQUIREMENTS] escreve:{/i}"
    window hide
    pause 0.4
    window show

    "\"Exemplo:\nRequisito funcional: O sistema deve permitir o cadastro de novos pacientes.\nCritério de aceitação: O cadastro deve ser validado e exibido imediatamente na lista de pacientes.\""

    "{i}Você abre seu notebook e começa a preencher o documento. Algumas dúvidas técnicas aparecem durante o processo.{/i}"

    menu:
        "Quem você prefere pedir ajuda nesse momento?"
        "Chamar [NOME_DEVELOPER_CODING] para dúvidas de implementação.":
            $ amizade_developer_coding += 1
            show developer_coding thinking at right_zoom
            developer_coding "Sempre que possível, deixe as regras bem explícitas. Nada de ambiguidade, isso complica na hora de codar."
            developer_coding "Por exemplo, ao invés de 'sistema deve ser rápido', escreva 'resposta em até 2 segundos para consulta de pacientes'."
            developer_coding "Se precisar, posso revisar alguns exemplos de requisito contigo."
            hide developer_coding
        "Perguntar a [NOME_DEVELOPER_TEST] sobre critérios de aceitação.":
            $ amizade_developer_test += 1
            show developer_test confident at right_zoom
            developer_test "Critério de aceitação bom é objetivo e testável! Sempre pergunte: consigo criar um teste automatizado para isso?"
            developer_test "Exemplo: 'O usuário deve receber mensagem de confirmação após salvar um exame.'"
            hide developer_test
        "Tentar sozinho(a), só pedir ajuda se travar.":
            show developer_requirements neutral at left_zoom
            developer_requirements "Gosto de ver autonomia! Mas lembre: ninguém espera que você acerte tudo sozinho(a)."
            developer_requirements "Dica: sempre use frases curtas e pense como o usuário vai validar aquele requisito."

    "{i}Vocês revisam juntos linha por linha, ajustando detalhes para deixar a especificação clara e objetiva.{/i}"

    show developer_requirements enthusiastic at left_zoom
    developer_requirements "Ótimo, agora leia tudo em voz alta comigo. Às vezes, só de ouvir, já encontramos pontos para melhorar!"
    "{i}Você se surpreende ao perceber pequenas ambiguidades ao ler, e rapidamente corrige no documento.{/i}"

    show developer_quality serious at right_zoom
    developer_quality "Deixa eu dar uma olhada também? Foco na padronização e clareza, ok? Requisito bem escrito evita retrabalho e facilita os testes depois."

    # Dica didática embutida
    show developer_quality thinking at right_zoom
    developer_quality "Aliás, vocês já ouviram falar do padrão SMART? Requisito bom é:\nS – Específico\nM – Mensurável\nA – Atingível\nR – Relevante\nT – Temporal (tem prazo)"
    "{i}Vocês comparam seus requisitos com os critérios do SMART, ajustando o que for necessário para tornar o documento mais robusto.{/i}"

    menu:
        "Como você reage à inspeção?"
        "Agradece pela revisão, valoriza o cuidado.":
            $ amizade_developer_quality += 1
            show developer_quality positive at right_zoom
            developer_quality "Trabalho em equipe é assim mesmo. Se precisar de exemplos de documento, me chama!"
        "Fica um pouco inseguro(a), mas aceita o feedback.":
            show developer_quality enthusiastic at right_zoom
            developer_quality "Relaxa! Todo mundo erra, e é melhor revisar agora do que na hora do deploy."
        "Prefere não mexer muito, acha que já está bom.":
            show developer_quality thinking at right_zoom
            developer_quality "Tudo bem, só recomendo uma última leitura amanhã com a cabeça fresca!"

    show developer_requirements positive at left_zoom
    developer_requirements "Mandou bem, [player_name]! Com uma especificação dessas, a próxima etapa vai fluir muito melhor."
    hide developer_requirements

    show developer_quality positive at right_zoom
    developer_quality "Documento pronto, time feliz. Agora bora celebrar as pequenas vitórias!"
    hide developer_quality

    # Padding extra: mensagem motivadora de outro NPC
    play sound "audio/cell_vibration.ogg"
    show developer_ai positive at left_zoom
    developer_ai "(mensagem no grupo) Parabéns pelo avanço, pessoal! Depois quero ver como posso automatizar parte desse processo para próximos projetos 😁"
    hide developer_ai

    scene bg escritorio_interior_noite
    with fade
    "{i}Fim de tarde, sensação de dever cumprido. Você percebe que, com apoio do time, o desafio de documentar ficou bem mais leve.{/i}"
    "{i}Guardar as versões do documento e compartilhar no grupo reforça a importância da colaboração em equipe.{/i}"

    return
