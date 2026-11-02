# s03.rpy
# -------------------------------
# TEMPO LIVRE DA ROTA SAÚDE · SEMANA 3 (sexta, 15h às 18h30)
# -------------------------------
# docs/design/intermissoes-saude.md §2 (S3). Conversas: fios em comum.rpy.
# Mentoria: mentoria.rpy. Descansar: comum.rpy.
# A pista saude_p_autosave (observar), a amizade e o registro extra são dados
# pelo motor depois de cada label.

label im_saude_abertura_3:
    "{i}Sexta. A especificação foi revisada ontem à noite, e a tarde de hoje está mais leve.{/i}"
    if energia_cansaco():
        "{i}Ontem você saiu tarde. O corpo lembra.{/i}"
    return


label im_saude_s3_ajudar_developer_management:
    # Do caso de uso ao cartão (sem pista)
    show developer_management serious at center_zoom
    "{i}[NOME_DEVELOPER_MANAGEMENT] projeta o quadro do Trello na parede. A coluna 'A fazer' tem um cartão só, enorme: 'Fazer o cadastro'.{/i}"
    developer_management "A especificação ficou boa. Agora preciso transformar isso em trabalho que caiba numa semana. Me ajuda?"
    developer_management "Vamos começar pelo UC1, o cadastro de paciente, e pelo UC5, a escala HAD."
    show developer_management thinking
    developer_management "Esse cartão aqui, 'Fazer o cadastro'. Quanto tempo você acha que leva?"
    menu:
        "Arriscar: uma semana":
            developer_management "Talvez. Ou três. Ninguém sabe, porque ninguém sabe o que tem dentro dele."
        "Dizer que não dá para saber do jeito que está":
            developer_management "Exato. Quando ninguém consegue estimar, o cartão está grande demais."
    developer_management "Como você dividiria?"
    "{i}Você abre o caso de uso ao lado e percebe que ele já vem dividido. Só falta passar para o quadro.{/i}"
    if "saude_p_cpf" in pistas_usadas:
        "{i}Você propõe um cartão por fluxo: o principal, do paciente com documento; o alternativo, do paciente que chega sem CPF; e a exceção, quando a conexão cai no meio do preenchimento.{/i}"
    else:
        "{i}Você propõe um cartão por fluxo: o principal, do paciente novo; o alternativo, do paciente que já veio antes e tem os dados reaproveitados; e a exceção, quando a conexão cai no meio do preenchimento.{/i}"
    show developer_management serious
    developer_management "Gostei. Cada cartão tem começo e fim. E cada um dá para testar separado."
    if "saude_p_cpf" in pistas_usadas:
        developer_management "E esse do paciente sem CPF veio daquela tarde na recepção, não foi? Dá para ver. Está escrito do jeito que acontece."
    developer_management "E o UC5?"
    "{i}Você separa a HAD em três cartões: aplicar as perguntas, calcular os escores de ansiedade e de depressão, e salvar uma escala incompleta para terminar depois.{/i}"
    developer_management "O cálculo separado da tela. O [NOME_DEVELOPER_PROJECT] vai gostar disso."
    "{i}Em cada cartão, você cola o critério de aceitação que já está na especificação. [NOME_DEVELOPER_MANAGEMENT] lê um por um, em voz baixa.{/i}"
    show developer_management thinking
    developer_management "Sabe o que era aquele cartão gigante? Uma preocupação. Isto aqui é trabalho."
    developer_management "Cartão que ninguém consegue terminar numa semana é só uma preocupação com nome bonito."
    developer_management "Na semana que vem a gente estima esses cartões juntos, com a equipe toda. Você vai ver como os números brigam."
    hide developer_management
    return


label im_saude_s3_estudar_sala_reunioes:
    # Coesão e acoplamento (saude_extra_acoplamento)
    show developer_requirements thinking at center_zoom
    "{i}[NOME_DEVELOPER_REQUIREMENTS] pede para ver a mensagem que [NOME_DEVELOPER_PROJECT] te mandou no dia dos casos de uso. Você mostra no celular.{/i}"
    developer_requirements "'Melhor separar a persistência de dados da lógica de negócios.' Concordo. Mas, sinceramente? Só sei explicar o porquê pela metade."
    developer_requirements "Você estuda e me explica? Uma hora. Eu pago o café."
    hide developer_requirements
    "{i}Você lê sobre coesão e acoplamento. Um módulo coeso faz uma coisa só. Acoplamento baixo quer dizer que mudar um módulo não obriga a mexer nos outros.{/i}"
    "{i}A teoria só faz sentido de verdade quando você pensa nas escalas.{/i}"
    show developer_requirements neutral at center_zoom
    "{i}Você explica: o cálculo da HAD soma pontos e devolve dois escores. Ele não precisa saber em que tabela a resposta está guardada.{/i}"
    "{i}Se um dia o banco mudar, o cálculo continua igual. E dá para testar o cálculo sem banco nenhum, só com as respostas.{/i}"
    show developer_requirements enthusiastic
    developer_requirements "Ah. Então era isso a 'dependência circular'. Se o cálculo conhece a tabela e a tabela chama o cálculo, ninguém mexe em um sem quebrar o outro."
    developer_requirements "Escreve do jeito que você me explicou, com as escalas. Ficou melhor que o livro."
    hide developer_requirements
    "{i}Você resume tudo no notebook, com o exemplo da HAD no meio.{/i}"
    return


label im_saude_s3_observar_ambulatorio:
    # O formulário que sumiu (pista saude_p_autosave, dada pelo motor)
    show doutora_2 neutral at center_zoom
    "{i}A [NOME_DOUTORA_2] te recebe na porta do consultório, na ala antiga do Instituto.{/i}"
    doutora_2 "O próximo paciente deixou você assistir. Perguntei antes. Fica naquele canto e, por favor, não fala nada durante a consulta."
    hide doutora_2
    "{i}Você se senta numa cadeira perto da estante. Dali dá para ver a tela de lado.{/i}"
    "{i}A consulta começa. A médica pergunta, ouve e digita rápido. Cigarros por dia, há quanto tempo, quantas tentativas de parar.{/i}"
    "{i}Ela preenche o formulário inteiro sem salvar. Você conta: quinze minutos, mais de vinte campos.{/i}"
    "{i}No teto do corredor, o roteador da ala antiga pisca. Pisca de novo. Apaga.{/i}"
    "{i}A tela recarrega sozinha. O formulário volta em branco.{/i}"
    show doutora_2 serious at center_zoom
    "{i}A [NOME_DOUTORA_2] fica parada por um segundo, com as mãos ainda sobre o teclado. Respira fundo.{/i}"
    doutora_2 "O senhor me desculpa. O sistema perdeu o que a gente fez. Vou precisar perguntar tudo de novo."
    "Paciente" "De novo, doutora? Desde o começo?"
    doutora_2 "Desde o começo. Mas agora eu vou mais rápido, prometo."
    "{i}Ela refaz as perguntas. O paciente responde mais curto, olhando o relógio. Algumas respostas mudam da primeira vez para a segunda.{/i}"
    menu (tipo="conversa"):
        "Anotar as respostas que mudaram":
            "{i}Você anota: na segunda vez, os cigarros por dia caíram de vinte para quinze. Pressa? Vergonha? O dado que fica no sistema é o da segunda vez.{/i}"
        "Anotar quanto tempo levou para refazer":
            "{i}Você cronometra: onze minutos para refazer o que tinha levado quinze. Com a sala de espera cheia.{/i}"
    "{i}Quando o paciente sai, ela fecha a porta e se encosta nela.{/i}"
    doutora_2 "Viu? É disso que eu falava."
    doutora_2 "Não é a internet que cai. Internet cai em qualquer lugar. É o sistema que não guarda nada até eu clicar em salvar, lá no fim."
    "{i}No caderno, você escreve: 'Paciente A, consulta de retorno. A conexão caiu aos 15 minutos, o formulário se perdeu e foi refeito com o paciente esperando.'{/i}"
    "{i}Ela se inclina para ler.{/i}"
    doutora_2 "Boa. Nome de paciente não sai daqui."
    hide doutora_2
    return
