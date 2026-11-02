# mentoria.rpy
# Arco de mentoria da rota Corporativo: "Causos do SGC", cinco encontros com
# o Jorge (co_legado). Roteiro: docs/design/intermissoes-corporativo.md,
# seção 5. O motor chama im_corporativo_mentoria_<k> antes de avançar o
# arco; depois do label, ele dá a amizade, a pista do passo (co_p_acentos no
# 2, co_p_norte no 3, se a semana ainda permitir) e, no 5, a conquista
# extra. Aqui ficam só as falas.
# Regras de texto: na semana 4 o Jorge está na baia, nas outras no arquivo.
# Antes da co_14 (co_homenagem_jorge == "") nada cita a aposentadoria.
# O ano da história é 2024 (SGC com 16 anos, desde 2008).

label im_corporativo_mentoria_1:
    if im_semana_atual == 4:
        "{i}Na baia do Farol, [NOME_CO_LEGADO] ocupa a cadeira de visita, com a caneca de 2008 numa mão e um fichário no colo.{/i}"
    else:
        "{i}Na sala do arquivo, [NOME_CO_LEGADO] tira a poeira de uma caixa com a manga da camisa. A caneca de 2008 está na mesa, longe dos papéis.{/i}"
    show co_legado neutral at center_zoom
    with dissolve
    co_legado "[player_name]. Pergunta importante: o crachá definitivo chegou?"
    "{i}Você mostra o crachá novo, com foto e tudo.{/i}"
    co_legado "Então posso contar uma história. Por aqui, a Tia Neide só se conta para quem tem crachá definitivo."
    co_legado "A Tia Neide. Talvez alguém já tenha contado a parte do ar-condicionado. Hoje é a outra metade: quem batizou."
    co_legado "Em 2008 a equipe tinha dois DBAs. Andavam de camiseta preta, inverno e verão."
    co_legado "Um deles chamava todo mundo da limpeza de tia. A dona Neide era a tia favorita dele."
    co_legado "Quando a gente descobriu que era ela que desligava o ar às três, ele não ficou bravo. Fez um cartaz e deu o nome dela para o servidor."
    co_legado "A justificativa oficial: as duas esquentavam, faziam barulho e nunca iam dormir antes da gente. A dona Neide adorou. Pediu foto."
    show co_legado thinking at center_zoom
    co_legado "Agora a caneca."
    "{i}Ele gira a caneca devagar. Branca, faixa azul, lascada na borda.{/i}"
    co_legado "Ela viu o lançamento, com pão de queijo e o servidor caindo às onze da noite."
    co_legado "Viu a greve de 2013, quando a fila de senha passou de três mil. Viu a reescrita de 2016 nascer e ser cancelada catorze meses depois."
    co_legado "Nada disso está no manual. Está aqui."
    "{i}Ele bate de leve com o dedo na própria testa.{/i}"
    co_legado "Metade do SGC é código. A outra metade é causo."
    "{i}Você pergunta como alguém de fora tira essa outra metade de dentro de uma pessoa.{/i}"
    show co_legado neutral at center_zoom
    co_legado "Do mesmo jeito que você fez com o [NOME_CO_SOLICITANTE] na entrevista. Pergunta pelo episódio."
    co_legado "'Quando foi a última vez que isso aconteceu?' Com essa pergunta eu lembro a data, o nome, até o cheiro da sala."
    co_legado "Se você perguntar 'como funciona a rotina', eu te dou o manual. E o manual mente, você já viu."
    co_legado "Me pergunta 'por que', não 'o quê'. O 'o quê' está no banco."
    "{i}Você propõe uma regra simples: toda vez que ele disser \"isso aí tem história\", você anota a data e pede o causo.{/i}"
    co_legado "Fechado. Vou ter que dizer menos, senão não tem caderno que chegue."
    "{i}No alto de uma página em branco, você escreve: Causos do SGC. Na primeira linha: 2008, Tia Neide, quem batizou e por quê.{/i}"
    if co_homenagem_jorge == "":
        co_legado "Da próxima vez tem mais. Traz o caderno e uma pergunta boa."
    else:
        co_legado "Até março tem mais. Traz o caderno e uma pergunta boa."
    hide co_legado
    with dissolve
    return


label im_corporativo_mentoria_2:
    if im_semana_atual == 4:
        "{i}Na baia do Farol, [NOME_CO_LEGADO] chega com uma pasta de plástico amarelada debaixo do braço e a abre em cima do teclado de ninguém.{/i}"
    else:
        "{i}Na sala do arquivo, [NOME_CO_LEGADO] está numa escadinha, puxando uma caixa da prateleira mais alta.{/i}"
    show co_legado neutral at center_zoom
    with dissolve
    co_legado "Achei. Sabia que estava aqui. Isso aí tem história."
    "{i}Você anota a data no caderno antes que ele continue. Ele percebe e sorri.{/i}"
    co_legado "Boa. A regra está valendo."
    "{i}Ele mostra um relatório impresso de 2014: chamados de manutenção de rede por filial. Na primeira linha, em vez de \"manutenção\", está escrito \"manutenÃ§Ã£o\".{/i}"
    co_legado "Lê a primeira linha. Parece palavrão em outra língua, né?"
    co_legado "2014. O SGC saiu da Tia Neide e foi para o Oracle novo. Servidor grande, sala refrigerada, ninguém desligava o ar."
    co_legado "Na migração, o DBA trocou a codificação do banco. É o jeito de guardar cada letra, principalmente as com acento."
    co_legado "Tudo o que foi escrito depois ficou certo. O que veio de antes, em alguns campos, passou pela conversão duas vezes."
    co_legado "Aí o 'ç' vira 'Ã§', o 'ã' vira 'Ã£', e o relatório parece escrito por um robô nervoso."
    "{i}Você pergunta por que ninguém consertou.{/i}"
    show co_legado thinking at center_zoom
    co_legado "Porque ninguém lê chamado velho. Era a frase da época."
    co_legado "Ninguém lê chamado velho. Até a auditoria ler."
    co_legado "Em 2017 a auditoria pediu os chamados de uma filial de 2010. Metade dos textos veio assim. Passei um fim de semana explicando acento para auditor."
    co_legado "Todo dado tem sotaque. O de 2008 fala outra língua."
    "{i}No caderno, você escreve a pergunta que fica: antes de mover um dado, por quais mudanças ele já passou?{/i}"
    show co_legado neutral at center_zoom
    co_legado "Isso. E não é só codificação. Tem formato de data, que aqui dentro já foi dia-mês e mês-dia."
    co_legado "Tem campo reaproveitado: o 'observação' que virou 'número de patrimônio' em 2012, porque ninguém quis pedir campo novo."
    co_legado "E tem valor mágico. Chamado com abertura em primeiro de janeiro de 1900 não é viagem no tempo. É 'não sei'."
    if im_semana_atual >= 5:
        co_legado "Lembra da carga do histórico? Duzentas mil descrições. Todas com sotaque, algumas com três."
        co_legado "Por isso eu disse que nem toda história ali é bonita."
    else:
        co_legado "Guarda isso. Um dia alguém vai querer levar essas descrições para um lugar novo. Vai ser bom ter perguntado antes."
    "{i}Ele entrega o relatório para você.{/i}"
    co_legado "Fica com ele. Um exemplo na mão vale mais que um parágrafo no wiki."
    hide co_legado
    with dissolve
    return


label im_corporativo_mentoria_3:
    if im_semana_atual == 4:
        "{i}Na baia do Farol, [NOME_CO_LEGADO] puxa uma cadeira para perto do monitor e abre um fichário de capa verde, escrito à mão: \"Relatórios Norte\".{/i}"
    else:
        "{i}Na sala do arquivo, [NOME_CO_LEGADO] abre na mesa um fichário de capa verde, escrito à mão: \"Relatórios Norte\".{/i}"
    show co_legado neutral at center_zoom
    with dissolve
    co_legado "Hoje é causo com número. A [NOME_CO_QUALIDADE] disse que você gosta de número."
    co_legado "Lembra da rotina das 72 h? A que fecha sozinha chamado de senha sem resposta."
    co_legado "Em 2014, na mesma migração dos acentos, o servidor novo veio no horário de Brasília. E a rotina passou a gravar o fechamento nesse horário."
    co_legado "Em Manaus, o relógio está uma hora atrás. O chamado abre às dez, no horário de lá. A rotina fecha 72 horas depois e grava onze, no horário daqui."
    co_legado "No relatório das filiais do Norte, chamado de senha leva 73 horas. Uma a mais que a regra. Sempre."
    "{i}Ele mostra uma folha com a coluna de tempo médio. Manaus: 73. Porto Velho: 73. Belém, que usa o horário de Brasília: 72.{/i}"
    show co_legado thinking at center_zoom
    co_legado "Em 2015 a supervisora de Manaus ligou reclamando. Disse que a equipe dela parecia mais lenta, e não era."
    co_legado "A gente olhou, entendeu e riu. Apelidou de 'hora do Norte'. Virou piada de corredor."
    co_legado "E ninguém registrou. Nem um e-mail. Nem eu."
    co_legado "Bug que vira apelido nunca mais é consertado."
    "{i}Você pergunta o que teria mudado se alguém tivesse registrado naquele dia.{/i}"
    show co_legado neutral at center_zoom
    co_legado "Não precisava consertar naquele dia. Ninguém morre de uma hora a mais num relatório."
    co_legado "Precisava escrever: o que acontece, desde quando, quem sofre com isso. E quem decide."
    co_legado "Aí alguém, um dia, com tempo e teste, decide. Sem registro, a decisão some junto com quem lembra."
    "{i}No caderno, você abre três colunas: causa, impacto, dono. Na primeira linha: hora do Norte. Fuso gravado errado desde 2014. Relatório das filiais do Norte. Dono: a definir.{/i}"
    co_legado "'A definir' já é melhor do que piada. Pelo menos alguém vai perguntar quem."
    if im_semana_atual == 4:
        show co_legado thinking at center_zoom
        "{i}Ele olha o relógio da parede. Depois o celular. Depois o relógio de novo.{/i}"
        co_legado "Ainda tenho uma papelada do RH para assinar hoje. Coisa chata, nada de mais."
        co_legado "Tem coisa que eu preciso contar para alguém antes de... bom. Antes de esquecer."
        co_legado "Enfim. Me pergunta outra coisa, vai. Qualquer coisa que não seja o RH."
    elif im_semana_atual >= 6:
        co_legado "E agora a hora do Norte tem prova. O teste de caracterização de vocês pegou a hora a mais."
        co_legado "Nove anos de piada, e foi um teste que finalmente levou a sério."
        co_legado "Até março eu quero ver isso registrado direito. Depois, quem decide é quem fica."
    else:
        co_legado "Até março eu quero contar todos esses. Depois, quem lembra é o caderno."
    hide co_legado
    with dissolve
    return


label im_corporativo_mentoria_4:
    if im_semana_atual == 4:
        "{i}Na baia do Farol, [NOME_CO_LEGADO] já arrumou a mesa: dois cafés, o notebook aberto numa página em branco do wiki e um bloco de papel.{/i}"
    else:
        "{i}Na sala do arquivo, [NOME_CO_LEGADO] já arrumou a mesa: dois cafés, o notebook aberto numa página em branco do wiki e um bloco de papel.{/i}"
    show co_legado neutral at center_zoom
    with dissolve
    co_legado "Março está aí. Quero começar pelo causo que mais me preocupa: a rotina das 72 h."
    if co_conq_memoria:
        co_legado "Na quarta depois da festa eu gravei o da Tia Neide com a [NOME_CO_QUALIDADE]. Ficou ótimo. Rimos muito."
        co_legado "Ficou divertido e inútil. Ninguém sabe o que fazer com aquilo."
        co_legado "Se a Tia Neide parar amanhã, o causo não diz onde fica o rack, o que roda nela nem para quem ligar."
    else:
        co_legado "Desde a festa eu fico pensando. Vinte e cinco anos de casa, e quase nada escrito."
        co_legado "Não quero mais adiar. Quero começar hoje, e pelo que dá mais medo."
    show co_legado thinking at center_zoom
    co_legado "Causo bom diverte. Página boa tem que responder outra pergunta: o que eu faço com isso?"
    "{i}Você propõe um modelo de seis campos. Ele lê a lista devagar, como quem confere um roteiro.{/i}"
    "{i}Um: o que faz.{/i}"
    co_legado "Fecha sozinha o chamado de senha sem resposta do solicitante depois de 72 horas. Uns trezentos por semana."
    "{i}Dois: quando e por que nasceu.{/i}"
    co_legado "Março de 2013. Greve, central pela metade, fila de senha com mais de três mil chamados. Escrevi numa quinta, subi na sexta."
    "{i}Três: onde está.{/i}"
    co_legado "TRG_FECHA_SENHA_72H, no banco. Roda num job às duas da manhã. Quem procurar na tela não acha."
    "{i}Quatro: o que mudou depois.{/i}"
    co_legado "Há poucas semanas, vocês decidiram: a rotina grava uma descrição padrão, e o autor aparece como 'sistema'. Escreve com a data."
    "{i}Cinco: o que quebra se mexer.{/i}"
    co_legado "A fila de senha, que volta a crescer. O relatório mensal da diretoria, que conta esses fechamentos."
    co_legado "E a hora do Norte. Mexeu no horário da rotina, mexeu no relatório de Manaus."
    "{i}Seis: quem sabe mais.{/i}"
    show co_legado neutral at center_zoom
    co_legado "No campo 'quem sabe mais' eu escrevi meu nome. Agora risca e põe mais um."
    "{i}Você escreve o seu nome embaixo do dele, com a data de hoje.{/i}"
    co_legado "História boa diverte. Registro bom avisa."
    co_legado "Daqui a cinco anos, alguém vai querer desligar essa rotina numa sexta à tarde. Essa página vai dizer: espera, lê isto antes."
    co_legado "E vai dizer por quê. Regra sem porquê é a que todo mundo tem medo de tocar. Ou toca sem medo nenhum, que é pior."
    "{i}Ele salva a página. O primeiro causo do wiki com os seis campos preenchidos.{/i}"
    co_legado "Da próxima vez a gente olha o resto. Tudo o que ainda só existe aqui dentro."
    hide co_legado
    with dissolve
    return


label im_corporativo_mentoria_5:
    if im_semana_atual == 4:
        "{i}Na baia do Farol, [NOME_CO_LEGADO] abre uma folha de papel grande sobre duas mesas juntas.{/i}"
    else:
        "{i}Na sala do arquivo, [NOME_CO_LEGADO] abriu uma folha de papel grande na mesa, presa nas pontas por quatro fichários.{/i}"
    show co_legado neutral at center_zoom
    with dissolve
    co_legado "Hoje é o último da série. Quero fazer uma lista que me assusta: tudo o que, hoje, só eu sei."
    co_legado "Eu vou falando, você escreve. Depois a gente organiza."
    "{i}Ele começa a contar nos dedos.{/i}"
    co_legado "A rotina das 72 h. Essa já tem página, graças a nós dois."
    co_legado "O cálculo do SLA com os feriados escritos à mão. Sexta à noite, 2010, Carnaval contado como dia útil."
    co_legado "A integração com o RH, que bloqueia o acesso de quem sai da empresa. Ninguém lembra dela até o dia em que ela para."
    co_legado "A réplica na Tia Neide. Pelo menos três relatórios leem dela, e eu não juro que são só três."
    co_legado "E os 14 relatórios. Um deles vai para a diretoria todo dia primeiro."
    "{i}Você desenha uma tabela com três colunas: o que quebra, quem percebe, com que frequência acontece.{/i}"
    show co_legado thinking at center_zoom
    co_legado "Integração com o RH: quebra o bloqueio de acesso. Quem percebe é a auditoria, tarde demais. Acontece a cada desligamento."
    co_legado "Feriados: quebra o prazo do SLA. Quem percebe é a [NOME_CO_SUPERVISORA], no relatório. Uma vez por ano, na virada."
    co_legado "Relatórios: quebra a reunião da diretoria. Quem percebe é todo mundo, no dia primeiro. Todo mês."
    co_legado "Tia Neide: quebra um relatório ou outro. Quem percebe? Ninguém sabe. Esse é o problema."
    "{i}Vocês marcam os cinco assuntos mais arriscados. Para cada um, falta a mesma coisa: uma segunda pessoa.{/i}"
    show co_legado neutral at center_zoom
    co_legado "Integração com o RH: o [NOME_CO_DEV]. Ele já leu o código e não fugiu."
    co_legado "Relatórios e a réplica, que andam juntos: a [NOME_CO_QUALIDADE]. Ela vai documentar até a cor da fonte."
    co_legado "Regras da central, com os feriados do SLA: a [NOME_CO_MENTORA]. Ela começou na central. Sabe onde dói."
    co_legado "A página das 72 h fica com você, [player_name], enquanto durar o estágio. Metade você já escreveu."
    co_legado "E eu reviso tudo até março. Um assunto por semana. Sem pressa e sem desculpa."
    "{i}Você lê o mapa inteiro em voz alta. Cinco assuntos, quatro duplas, uma data para cada um.{/i}"
    co_legado "Fator ônibus não se resolve com um documento de quinhentas páginas. Ninguém lê."
    co_legado "Se resolve assim: o mais arriscado primeiro, e ninguém sozinho em nada."
    "{i}Ele imprime o mapa na impressora do subsolo, que range mas funciona. Pega a caneta e assina embaixo, com a data.{/i}"
    co_legado "Em 2008 eu era o SGC. Agora sou só um dos autores. Melhor assim."
    co_legado "Março ficou menos assustador."
    if im_semana_atual == 8:
        co_legado "E hoje à noite tem janela. Vamos ver se o meu mapa aguenta a primeira prova."
    hide co_legado
    with dissolve
    return
