# s01.rpy
# -------------------------------
# TEMPO LIVRE DA ROTA SAÚDE · SEMANA 1 (primeiro dia, 16h às 18h, tutorial)
# -------------------------------
# docs/design/intermissoes-saude.md §2 (S1). Conversas: fios em comum.rpy.
# Descansar: comum.rpy. Sem ajudar, sem observar, sem pistas nesta semana.
# Recompensas (registro extra, energia, amizade) são aplicadas pelo motor.

label im_saude_abertura_1:
    show developer_requirements positive at center_zoom
    developer_requirements "Hoje ninguém vai te passar tarefa até as seis. Primeiro dia é para conhecer a casa."
    developer_requirements "Esse é o mapa da cidade. Por enquanto, o que interessa é o nosso canto do campus. Em cada lugar aparece quem está lá e o que dá para fazer."
    show developer_requirements thinking
    developer_requirements "Cada coisa custa tempo: conversar, meia hora; estudar, uma hora. Andar até a praça também conta. Não cabe tudo, e tudo bem. Escolher é deixar algo para outro dia."
    developer_requirements "Fica de olho na sua energia, embaixo do relógio. Ajudar alguém cansa; descansar recupera."
    show developer_requirements neutral
    developer_requirements "Às vezes você vai ver um detalhe que vira pista e ajuda numa decisão lá na frente."
    show developer_requirements positive
    developer_requirements "E o mais importante: nada aqui é obrigatório para aprender. O que o projeto precisa, a gente faz junto no expediente. Esse tempo é seu."
    hide developer_requirements
    return


label im_saude_s1_estudar_sala_reunioes:
    # Glossário do projeto (saude_extra_glossario)
    show developer_management thinking at center_zoom
    "{i}Na sala de reuniões, [NOME_DEVELOPER_MANAGEMENT] abre o wiki da equipe no projetor.{/i}"
    developer_management "Quer começar por algum lugar? Começa por aqui. A página 'Glossário'."
    "{i}A página tem três termos: 'sprint', 'deploy' e 'homologação'. A última edição foi há dois anos.{/i}"
    show developer_management serious
    developer_management "Pois é. Ninguém mexe nela. E toda semana alguém usa a mesma palavra com sentido diferente."
    "{i}Você abre o plano do projeto ao lado e marca as palavras que ainda não sabe explicar: carga tabágica, escala HAD, retorno, histórico de saúde.{/i}"
    developer_management "Carga tabágica é a conta que as médicas fazem: maços por dia vezes anos fumando. Vinte cigarros por dia durante dez anos dá dez maços-ano."
    developer_management "E 'retorno', para elas, é a consulta de acompanhamento. Para o [NOME_DEVELOPER_CODING], já foi o valor que uma função devolve. Imagina a confusão numa reunião."
    "{i}Você escreve cada termo com uma frase curta e um exemplo. Onde não tem certeza, deixa a pergunta anotada para a entrevista.{/i}"
    show developer_management thinking
    developer_management "Gostei das perguntas abertas. Glossário bom também mostra o que a gente ainda não sabe."
    developer_management "Se você mantiver isso vivo, vira a página mais lida do wiki."
    hide developer_management
    "{i}Você copia o glossário para o seu notebook, para levar na semana que vem.{/i}"
    return
