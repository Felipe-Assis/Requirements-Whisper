# s01.rpy
# Tempo livre da rota Corporativo, semana 1 (sexta, 15h às 17h, tutorial).
# Fonte: docs/design/intermissoes-corporativo.md, seções 2.1 e 2.2.
# O motor (logic/intermissao.rpy) chama estes labels por convenção de nome e
# aplica sozinho tempo, energia, amizade, pista e registro extra: aqui só há
# fala. Descansar tem label por semana (im_corporativo_s1_descansar_*) para
# não colidir com o label geral im_corporativo_descansar_<local>.

label im_corporativo_abertura_1:
    # Tutorial (guia: Valéria). Mostra o fundo do local de partida.
    $ im_mostrar_local({"poi": im_local})
    with dissolve
    show co_mentora neutral at center_zoom
    with dissolve
    co_mentora "Sexta à tarde a torre fica mais calma. Até as cinco, o tempo é seu."
    co_mentora "Vamos por partes. No mapa, cada lugar mostra quem está lá e o que dá para fazer. Cada ação diz quanto tempo custa."
    show co_mentora thinking at center_zoom
    co_mentora "Não cabe tudo. Escolher o que fica de fora também é planejamento. Você vai ver isso de novo no projeto."
    co_mentora "A energia aparece embaixo do relógio. Ajudar e estudar cansam. Descansar recupera."
    show co_mentora neutral at center_zoom
    co_mentora "Se você observar alguém usando o sistema de verdade, pode sair com uma pista. Ela volta numa conversa mais adiante."
    co_mentora "E nada aqui é obrigatório para aprender. O que o projeto precisa acontece no trabalho. Aqui é o seu tempo."
    co_mentora "Eu vou descer para o café do térreo. Se quiser companhia, já sabe onde me achar."
    hide co_mentora
    with dissolve
    return


# -------------------------------
# Baia do Farol
# -------------------------------
label im_corporativo_s1_conversar_co_dev:
    show co_dev neutral at center_zoom
    with dissolve
    "{i}[NOME_CO_DEV] está de fone, com três abas abertas sobre inteligência artificial para prever pico de chamados. O notebook prateado tem mais adesivo do que tampa.{/i}"
    co_dev "Bora! Senta aí. Se o [NOME_CO_LEGADO] perguntar, eu estava lendo documentação do Oracle."
    co_dev "Olha esse aqui: um modelo que tenta adivinhar a fila da central de manhã. Ia ser lindo. Ia ser inútil, provavelmente, mas lindo."
    "{i}Ele mostra os adesivos um por um: um foguete, um pato de borracha e um \"funciona na minha máquina\" meio descascado.{/i}"
    co_dev "O pato é para explicar o código em voz alta. Às vezes ele acha o bug antes de mim."
    show co_dev thinking at center_zoom
    co_dev "Sinceridade? Num fim de semana bem dormido, eu reescrevia o SGC inteiro."
    co_dev "Tá, talvez dois. E o [NOME_CO_LEGADO] ia me olhar daquele jeito."
    show co_dev neutral at center_zoom
    co_dev "E aí, o que você achou da Tia Neide? Pode falar a verdade."
    "\"Barulhenta\", você responde. \"E gelada.\""
    co_dev "Barulhenta, gelada e segurando dezesseis anos de chamado. Respeito. Um pouco de medo, mas respeito."
    hide co_dev
    with dissolve
    return

label im_corporativo_s1_ajudar_co_dev:
    show co_dev neutral at center_zoom
    with dissolve
    co_dev "Sua máquina nova chegou? Então hoje a gente monta o ambiente. Em pair: eu digito, você pergunta."
    "{i}Vocês puxam duas cadeiras para a mesa dele. A caixa do notebook ainda tem cheiro de plástico.{/i}"
    co_dev "Primeiro o acesso ao repositório. Depois o banco de teste. Depois a parte divertida."
    "{i}Ele abre duas pastas lado a lado. Uma se chama farol: arquivos novos, nomes claros e uma pasta de testes cheia.{/i}"
    co_dev "Esse é o Farol. Tudo com teste. Se alguém quebrar alguma coisa, a tela fica vermelha antes do café esfriar."
    show co_dev thinking at center_zoom
    "{i}A outra pasta se chama sgc-ponte. Tem arquivos com nomes como ajuste_final_2.sql e ajuste_final_2_agora_vai.sql.{/i}"
    co_dev "E aqui mora o mistério. É o código que conversa com o SGC. Quem escreveu metade disso já saiu da empresa."
    "{i}Você lê os passos da instalação em voz alta, um por um, e pergunta o que cada um faz.{/i}"
    co_dev "Esse configura o acesso ao banco de teste. Esse baixa as dependências. Esse..."
    "{i}No quinto passo, a instalação para com um erro vermelho. Falta uma variável de ambiente que não aparece em lugar nenhum da lista.{/i}"
    "{i}Você pergunta de onde ela vem.{/i}"
    co_dev "Peraí. Ela vem... de um arquivo que eu criei na minha máquina em março. E nunca anotei no wiki."
    show co_dev serious at center_zoom
    co_dev "Ou seja: todo mundo que chegou depois de mim passou uma tarde travado nisso. E ninguém reclamou."
    co_dev "Ou reclamaram baixinho. Pior ainda."
    show co_dev neutral at center_zoom
    "{i}Ele abre o wiki da equipe e acrescenta o passo que faltava, com um exemplo e o nome do arquivo.{/i}"
    co_dev "Pronto. Agora existe. Se não está registrado, não aconteceu, como diz a [NOME_CO_QUALIDADE]."
    "{i}No fim da tarde, o Farol roda na sua máquina pela primeira vez. A tela de consulta abre, ainda sem dados, com um chamado de exemplo.{/i}"
    co_dev "Pair é isso: um digita, o outro pergunta. Quem pergunta acha os bugs."
    co_dev "Valeu, sério. Você me poupou de explicar esse erro para a próxima pessoa que chegar."
    hide co_dev
    with dissolve
    return


# -------------------------------
# Central de atendimento
# -------------------------------
label im_corporativo_s1_conversar_co_supervisora:
    show co_supervisora neutral at center_zoom
    with dissolve
    "{i}Ao lado do painel de filas, uma mulher de headset no pescoço confere as barras na TV e anota alguma coisa num relatório impresso.{/i}"
    co_supervisora "Você é da equipe do Farol? Sou a [NOME_CO_SUPERVISORA], supervisora da central. Fala rápido, que a fila não espera."
    co_supervisora "Me avisaram que vem gente da TI conversar comigo na quarta."
    show co_supervisora thinking at center_zoom
    co_supervisora "Meu tempo médio de atendimento está em seis minutos e quarenta. Cada minuto a mais vira fila às nove da manhã."
    co_supervisora "Então um pedido: traz pergunta boa. Já veio muita gente aqui com tela pronta perguntando se a gente gostou."
    show co_supervisora neutral at center_zoom
    co_supervisora "Quarta a gente conversa direito. Traz pergunta, não traz solução pronta."
    "{i}Um atendente levanta a mão do outro lado da fileira. Ela já está andando antes de terminar a frase.{/i}"
    hide co_supervisora
    with dissolve
    return

label im_corporativo_s1_observar_central:
    show co_supervisora neutral at right_zoom
    with dissolve
    "{i}Você pede para ver como é o atendimento de perto. A supervisora da central olha o crachá provisório e pensa um segundo.{/i}"
    co_supervisora "Pode. Senta do lado do Paulo e não toca em nada. Ele está na fila de cobrança hoje."
    co_supervisora "E nada de nome de ninguém no seu caderno. Nem dele, nem de quem liga."
    hide co_supervisora
    with dissolve
    "{i}Paulo é jovem, fala rápido e tem um post-it amarelo colado na borda do monitor. Ele aponta uma cadeira com o queixo e já atende.{/i}"
    "{i}Primeira ligação: \"E o meu chamado da impressora? Abri na segunda.\"{/i}"
    "{i}Paulo abre o chamado. Depois o histórico. Depois a fila técnica. Depois o e-mail do grupo de suporte. Quatro abas para uma resposta.{/i}"
    "{i}\"Está com o grupo de infraestrutura, senhora. Assim que tiver novidade, eles avisam.\"{/i}"
    "{i}Ele desliga e faz um risquinho no post-it.{/i}"
    "{i}Segunda ligação, sete minutos depois. Um gerente: \"E o meu chamado do notebook novo?\"{/i}"
    "{i}As mesmas quatro abas. Desta vez, o chamado diz Resolvido, e o campo Solução está vazio.{/i}"
    "{i}Paulo hesita. \"Consta como resolvido, senhor. O senhor recebeu o equipamento?\" Não recebeu.{/i}"
    "{i}Ele abre outro chamado para descobrir o que aconteceu com o primeiro. Outro risquinho.{/i}"
    "{i}Terceira ligação: \"E o meu chamado?\". Desta vez Paulo não acha resposta em aba nenhuma.{/i}"
    "{i}\"Vou verificar com a equipe e retorno para a senhora ainda hoje.\" Ele anota o número num papel separado. Terceiro risquinho.{/i}"
    "{i}Você pergunta, baixinho, para que servem os risquinhos.{/i}"
    "{i}\"Só para eu saber quantas são\", ele responde, sem tirar os olhos da tela. \"Ninguém conta isso. Eu conto.\"{/i}"
    "{i}Vinte minutos. Três ligações. Nenhuma delas era um problema novo: as três só queriam saber o que já tinha acontecido.{/i}"
    "{i}Paulo olha o post-it e solta o ar.{/i}"
    "{i}\"Três. E ainda nem deu quatro horas.\"{/i}"
    show co_supervisora thinking at center_zoom
    with dissolve
    "{i}Na saída, a supervisora passa por você com uma prancheta.{/i}"
    co_supervisora "Viu o post-it? Ele faz isso há meses. Eu nunca perguntei o total."
    if energia_cansaco():
        "{i}Você sai com o caderno cheio e os ouvidos zumbindo de tanto telefone. Observar também cansa.{/i}"
    else:
        "{i}Você sai com o caderno cheio, sem nenhum nome escrito, e com a cabeça nos três risquinhos.{/i}"
    hide co_supervisora
    with dissolve
    return


# -------------------------------
# Café do térreo
# -------------------------------
label im_corporativo_s1_conversar_co_mentora:
    show co_mentora neutral at center_zoom
    with dissolve
    "{i}[NOME_CO_MENTORA] está numa mesinha perto da porta giratória, com um café coado e o caderno vinho fechado ao lado.{/i}"
    co_mentora "Senta. Primeira semana inteira. O que ficou de dúvida?"
    "{i}Você fala do chamado 48213, resolvido sem uma linha escrita.{/i}"
    show co_mentora thinking at center_zoom
    co_mentora "E por que você acha que ninguém escreveu?"
    "{i}Você arrisca: preguiça? Pressa?{/i}"
    co_mentora "Pode ser. Pode ser outra coisa. Vamos por partes. Primeiro, o que você viu. Depois, o que você acha."
    show co_mentora neutral at center_zoom
    co_mentora "Estou separando uns chamados reais para a gente ler junto na segunda. Sem dados pessoais, claro."
    co_mentora "Se quiser adiantar alguma coisa, tem uma apostila velha de ITIL lá no arquivo. As anotações a lápis na margem valem mais do que o texto."
    co_mentora "Mas é sexta. Não precisa adiantar nada."
    hide co_mentora
    with dissolve
    return

label im_corporativo_s1_descansar_cafe:
    "{i}Você pega um café coado no balcão e senta perto da porta giratória.{/i}"
    "{i}Por quinze minutos ninguém fala de SLA. Lá fora, o Centro passa apressado: pastas, crachás, um ambulante vendendo guarda-chuva antes da chuva.{/i}"
    if energia_cansaco():
        "{i}Você quase cochila na banqueta. O atendente do café deixa um copo d'água do seu lado sem perguntar nada.{/i}"
    else:
        "{i}O café esfria devagar. Você deixa o celular virado para baixo e só olha a rua.{/i}"
    return


# -------------------------------
# Refeitório
# -------------------------------
label im_corporativo_s1_descansar_refeitorio:
    "{i}O refeitório está quase vazio a esta hora. Bandejas empilhadas, o barulho baixo da máquina de lavar e a baía inteira na janela.{/i}"
    "{i}Você pega um chá de máquina e não abre o notebook.{/i}"
    if energia_cansaco():
        "{i}Você deita a cabeça nos braços por dez minutos. Ninguém repara.{/i}"
    else:
        "{i}Um barco atravessa a baía bem devagar. Você acompanha até ele sumir atrás de um prédio.{/i}"
    return


# -------------------------------
# Sala do arquivo
# -------------------------------
label im_corporativo_s1_conversar_co_legado:
    show co_legado thinking at center_zoom
    with dissolve
    "{i}No subsolo, [NOME_CO_LEGADO] está de joelhos diante de uma estante, tirando e devolvendo caixas-arquivo.{/i}"
    co_legado "[player_name]! Me ajuda com os olhos. Uma caixa de CDs com a etiqueta \"Renova 2016\"."
    co_legado "É o que sobrou da reescrita cancelada. Código, atas, apresentação bonita. Tudo em CD, que em 2016 já era coisa de museu."
    "{i}Vocês procuram por uns dez minutos. Nada.{/i}"
    show co_legado neutral at center_zoom
    co_legado "Talvez seja melhor assim. Tem coisa que a gente procura mais por saudade do que por necessidade."
    "{i}Você aproveita e pergunta por que o servidor se chama Tia Neide.{/i}"
    co_legado "Essa história só com crachá definitivo. Regra é regra."
    co_legado "Isso aí tem história. E caixa perdida também é história."
    hide co_legado
    with dissolve
    return

label im_corporativo_s1_estudar_arquivo:
    "{i}Numa estante do arquivo, entre fichários de lombada colorida, uma apostila encadernada em espiral: \"Treinamento interno ITIL, 2012\".{/i}"
    "{i}Alguém leu com lápis na mão. Na margem, ao lado de um parágrafo: \"isso aqui vale\". Ao lado de outro: \"isso aqui ninguém faz\".{/i}"
    "{i}Você vai direto ao capítulo de incidente, problema e mudança e senta na mesa dos documentos, sob a luz da janela basculante.{/i}"
    "{i}Incidente é o que parou agora. Problema é a causa por trás. Mudança é o que se altera em produção, com pedido, janela e plano de volta.{/i}"
    "{i}Na margem do capítulo de problema, a mesma letra a lápis: \"todo mundo apaga o fogo, ninguém procura o fósforo\".{/i}"
    if energia_cansaco():
        "{i}Você relê o mesmo parágrafo três vezes antes de ele entrar. Mas entra.{/i}"
    "{i}Você pensa no chamado 48213. Resolver sem escrever o que foi feito apaga o fogo e esconde o fósforo.{/i}"
    "{i}Você copia no notebook as três definições com um exemplo de cada, nas suas palavras.{/i}"
    return
