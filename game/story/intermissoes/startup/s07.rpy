# s07.rpy
# Tempo livre da rota Startup, semana 7 (quarta, almoço, depois da manhã da
# st_17). Fonte: docs/design/intermissoes-startup.md, seção 3 (Semana 7).
# Labels por convenção do motor (logic/intermissao.rpy, im_label_conteudo).
# As recompensas (amizade, pista, registro extra, energia) são aplicadas pelo
# motor depois de cada label; aqui ficam só as falas.

label im_startup_abertura_7:
    "{i}Quarta, onze e meia. De manhã vocês decidiram o teste de carga, o cofre do token e a exclusão de conta.{/i}"
    "{i}Hoje à tarde a 1.0 vai para as lojas. Até lá, o almoço é seu.{/i}"
    if energia_cansaco():
        "{i}Você boceja antes de abrir o mapa. Hoje o tempo livre vai ser mais curto.{/i}"
    return


# ---------------- mesa ----------------

label im_startup_s7_conversar_st_techlead:
    "{i}Otávio almoça na própria mesa: marmita de vidro de um lado, o gráfico do teste de carga do outro.{/i}"
    show st_techlead neutral at center_zoom
    with dissolve
    st_techlead "Senta. Arroz, feijão e um gráfico. O almoço dos campeões."
    st_techlead "Você já me ouviu falar de 2009 como quem fala de um terremoto. Hoje eu conto inteiro."
    show st_techlead thinking
    st_techlead "Sexta-feira, seis da tarde. A gente publicou tudo junto: banco de dados novo, tela nova e cobrança nova. Era para comemorar."
    st_techlead "Às sete, caiu. A cobrança passou duas vezes para metade dos clientes. E ninguém sabia qual das três mudanças era a culpada."
    st_techlead "Às onze da noite eu ainda estava lá, sozinho, desfazendo uma coisa de cada vez. O resto da equipe estava num aniversário."
    "{i}Você pergunta o que ficou daquela noite.{/i}"
    show st_techlead neutral
    st_techlead "Três regras saíram daquela noite. Nada na sexta. Nada tudo junto."
    st_techlead "Veja bem: é como estrear três pratos no dia da festa. Se alguém passa mal, você não sabe qual foi."
    st_techlead "E a terceira: depois das nove, ninguém conserta nada. Gente cansada não enxerga erro."
    if energia_cansaco():
        st_techlead "Por isso: come direito hoje e vai cedo pra casa."
    "{i}Ele fecha a marmita e volta o olho para o gráfico. As conexões do banco estão calmas, por enquanto.{/i}"
    hide st_techlead
    with dissolve
    return


# ---------------- sala de vidro ----------------

label im_startup_s7_ajudar_st_mobile:
    "{i}Na sala de vidro, Davi tem duas abas abertas: o formulário de segurança de dados do Google e o da Apple. Ao lado, um pacote de biscoito pela metade.{/i}"
    show st_mobile neutral at center_zoom
    with dissolve
    st_mobile "Chegou na hora! A loja quer saber tudo que o app coleta. Tudo. E pra quê. E como apaga."
    st_mobile "Se a gente responder errado, volta rejeitado. Se responder certo e o app fizer diferente, é pior."
    "{i}Vocês vão campo por campo. E-mail: para entrar na conta. Gastos e categorias: para mostrar o total. Localização e contatos: nada.{/i}"
    show st_mobile thinking
    st_mobile "Pô, e os logs? Eles mandam alguma coisa pessoal?"
    "{i}Você lembra do review da semana passada: o log da sincronização guarda só o id e o status. Vocês marcam \"diagnóstico\" e seguem.{/i}"
    st_mobile "E o \"como apaga\"?"
    "{i}Você escreve: \"Pelo app, em Configurações, Minha conta, Excluir conta. Os dados são apagados em até 15 dias.\" É a mesma resposta que a Bia recebeu de manhã.{/i}"
    show st_mobile neutral
    st_mobile "Fechou. Agora o link da política de privacidade. Esse eu confiro três vezes."
    if pista_tem("st_p_loja"):
        "{i}No histórico de envios, o mesmo que vocês olharam na semana passada: dois dias de fila na última versão e a rejeição por causa do link.{/i}"
        st_mobile "Você já viu esse histórico comigo. Pô, não quero repetir aquela rejeição."
    else:
        "{i}Ele abre o histórico de envios. A última versão do beta ficou dois dias em revisão no Google. Uma anterior voltou rejeitada: faltava o link da política de privacidade.{/i}"
        st_mobile "Dois dias de fila e uma rejeição por causa de um link. Loja não tem pressa nenhuma."
    "{i}Você abre o link no celular de teste. Carrega. O texto fala dos mesmos 15 dias do formulário.{/i}"
    st_mobile "Então: link funcionando, formulário batendo com o app, e a gente envia hoje. Não amanhã."
    st_mobile "Só espero o exploratório da Lorena, à tarde. Se ela achar alguma coisa, a correção entra antes do envio."
    "{i}Ele salva o formulário pronto e cola um post-it no monitor: \"enviar hoje\".{/i}"
    st_mobile "Envia hoje e reza. Brincadeira: envia hoje e acompanha."
    st_mobile "Valeu. Sozinho eu ia marcar \"não coleta nada\" só pra acabar logo. E ia estar mentindo pra loja."
    if energia_cansaco():
        "{i}Você esfrega os olhos. Formulário cansa mais do que parece.{/i}"
        st_mobile "Toma, o último biscoito. Hoje você precisa mais que eu."
    hide st_mobile
    with dissolve
    return

label im_startup_s7_conversar_st_mobile:
    show st_mobile thinking at center_zoom
    with dissolve
    st_mobile "Fala! Vou ser sincero: tô nervoso. É a primeira versão grande que eu mando pra loja aqui na Trocado."
    st_mobile "Site você conserta e dá F5. App, não. Quem instalou fica com o que a gente mandou até a próxima passar na revisão."
    "{i}Ele gira o Tijolo na mão, o celular de teste mais antigo da mesa.{/i}"
    st_mobile "E se a loja rejeitar?"
    show st_mobile neutral
    st_mobile "Se a loja rejeitar, a gente não se loja."
    st_mobile "...Desculpa. Saiu."
    "{i}Você ri mesmo assim. Ele também, e os ombros dele descem um pouco.{/i}"
    st_mobile "Fechou. Se rejeitar, a gente lê o motivo, corrige e manda de novo. Nervoso, mas com plano."
    st_mobile "E sábado tem partida online. Se a loja aprovar, eu jogo pra comemorar. Se rejeitar, jogo pra esquecer."
    hide st_mobile
    with dissolve
    return

label im_startup_s7_estudar_sala_vidro:
    "{i}Na outra ponta da mesa de vidro, Davi preenche formulários. Você abre a documentação das duas lojas, lado a lado.{/i}"
    "{i}No Google, quem envia escolhe a porcentagem: dez, cinquenta, cem. Na Apple, a liberação em fases segue um calendário de sete dias.{/i}"
    "{i}Nas duas, cada versão passa por revisão antes de chegar a alguém. E uma versão instalada não volta atrás.{/i}"
    show st_mobile neutral at right_zoom
    with dissolve
    st_mobile "Tá lendo sobre liberação em etapas? Pô, melhor coisa já inventada. Deu problema com dez por cento, você para e respira."
    st_mobile "E o que é novo fica atrás de uma flag. Eu desligo de longe, sem mandar versão nova."
    hide st_mobile
    with dissolve
    "{i}Você desenha no caderno três degraus e um interruptor ao lado. Embaixo, escreve: \"enviar com folga\".{/i}"
    return


# ---------------- café ----------------

label im_startup_s7_conversar_st_mentora:
    "{i}No café da esquina, Tainá tem um pão de queijo esquecido no prato e o notebook aberto no texto da tela de exclusão de conta.{/i}"
    show st_mentora thinking at center_zoom
    with dissolve
    st_mentora "Oi, [player_name]! Senta aí. Preciso da sua voz."
    st_mentora "Lê isso em voz alta pra mim. Do jeito que está."
    "{i}Você lê: \"A exclusão da conta implica a eliminação irreversível dos dados vinculados, ressalvadas as hipóteses legais de retenção.\" Na palavra \"ressalvadas\", a língua tropeça.{/i}"
    show st_mentora neutral
    st_mentora "Viu? Tropeçou. Se você lê em voz alta e tropeça, a Bia também tropeça."
    st_mentora "Agora a minha versão."
    "{i}\"Quando você apaga a conta, a gente apaga seus gastos em até 15 dias. Se você ligou um banco, essa autorização é cancelada junto. Só fica o que a lei manda guardar.\"{/i}"
    st_mentora "Melhor? Frase curta, palavra de todo dia e o prazo com número."
    st_mentora "Passei cinco anos no atendimento do banco. Metade das ligações era gente com medo de um texto que ninguém entendia."
    if energia_cansaco():
        st_mentora "E me promete uma coisa: hoje você não fica até tarde. Lançamento não é maratona."
    hide st_mentora
    with dissolve
    return


# ---------------- bandejão ----------------

label im_startup_s7_conversar_st_estudante:
    "{i}No bandejão, Bia está na fila com a bandeja numa mão e o celular na outra.{/i}"
    show st_estudante neutral at center_zoom
    with dissolve
    st_estudante "Oi! Chegou na hora do feijão. Vem pra fila comigo."
    st_estudante "Tipo assim: obrigada pela resposta de hoje de manhã. Sobre apagar a conta."
    st_estudante "Mostrei pras meninas da república. A Rayane quase chorou de alívio. Ela achava que o app ia guardar tudo pra sempre."
    show st_estudante thinking
    st_estudante "Uma vez um site de sorteio vazou o CPF dela. Desde então ela desconfia de qualquer cadastro."
    st_estudante "Égua, e quando eu falei \"em até 15 dias\", ela anotou no caderno. Com a data."
    show st_estudante neutral
    "{i}Ela chega ao caixa, paga e lança na hora.{/i}"
    st_estudante "Bandejão, R$ 4,50. Lançado. Uma vez só."
    st_estudante "Semana que vem chegam os calouros. Tô até ensaiando o que dizer quando me perguntarem que app usar."
    hide st_estudante
    with dissolve
    return

label im_startup_s7_observar_bandejao:
    "{i}Hora do almoço no bandejão. A fila sai pela porta e vai até a escada do subsolo.{/i}"
    show st_estudante neutral at right_zoom
    with dissolve
    st_estudante "Senta aqui, dá pra ver a fila inteira daqui. É o melhor camarote do campus."
    "{i}Você observa sem atrapalhar. Quase todo mundo segura o celular enquanto anda com a bandeja.{/i}"
    "{i}Na saída do caixa, um grupo de cinco paga e, um atrás do outro, lança o almoço no Trocado. Quarenta pessoas fazem o mesmo nos dez minutos seguintes.{/i}"
    if st_d17_carga:
        "{i}É o horário que você simulou de manhã. Agora ele tem rosto, bandeja e pressa.{/i}"
    else:
        "{i}É o horário que a Lorena te ajudou a escolher de manhã. Agora ele tem rosto, bandeja e pressa.{/i}"
    show st_estudante thinking
    st_estudante "Isso é uma quarta qualquer, sem aula. Semana que vem é o primeiro dia do semestre."
    st_estudante "No primeiro dia a fila dobra. Vai até lá fora, no ipê. E todo calouro baixa um app de finanças na fila, porque o veterano mandou."
    "{i}Na mesa ao lado, um rapaz lança o almoço, espera, olha a tela e lança de novo.{/i}"
    st_estudante "Viu? Ele não esperou o app responder. Na hora do almoço, ninguém espera dois segundos."
    "{i}Você anota: o horário, quantas pessoas por minuto e o gesto de tocar de novo quando a tela demora. Sem nomes.{/i}"
    show st_estudante neutral
    st_estudante "Tipo assim: se o app aguentar essa fila em dobro, ele aguenta qualquer coisa."
    "{i}Ela volta para o próprio prato. O feijão já esfriou, e ela nem reclama.{/i}"
    hide st_estudante
    with dissolve
    return

label im_startup_s7_conversar_st_qualidade:
    "{i}Lorena almoça devagar, com o caderninho de frases aberto ao lado do prato.{/i}"
    show st_qualidade neutral at center_zoom
    with dissolve
    st_qualidade "Oi! Senta. Quero te mostrar uma coisa antes que eu fique emocionada sozinha."
    st_qualidade "Lembra do caderninho? Frase estranha de avaliação, queixa de total errado..."
    show st_qualidade thinking
    st_qualidade "Hoje entrou a primeira avaliação de cinco estrelas de uma tester do beta. Escuta: \"Agora eu confio no total.\""
    st_qualidade "Cinco palavras. Nenhuma fala de botão nem de cor. Fala de confiança."
    "{i}Ela copia a frase no caderno com a letra mais caprichada da página. Na folha anterior, ainda da primeira semana: \"o app me julgou pelo café\".{/i}"
    st_qualidade "Dá pra contar a história do app só pelas frases. Do \"meu total tem personalidade própria\" até \"agora eu confio no total\"."
    show st_qualidade neutral
    st_qualidade "Primeiro: guardei. Segundo: vou reler no dia ruim."
    st_qualidade "Porque ele vem, viu? Toda versão tem um dia ruim. Oxe, não é pessimismo. É plano de testes."
    hide st_qualidade
    with dissolve
    return


# ---------------- aceleradora ----------------

label im_startup_s7_ajudar_st_ceo:
    "{i}No auditório da Aceleradora Maré, o palco está aceso e a plateia, vazia. Na primeira fila, a mentora da aceleradora espera com as pernas cruzadas.{/i}"
    show st_ceo neutral at center_zoom
    with dissolve
    st_ceo "Você veio! Hoje é o segundo ensaio, e é só perguntas e respostas. Nada de slide."
    st_ceo "Você anota o que eu respondo, palavra por palavra. Eu sempre acho que respondi melhor do que respondi."
    if pista_tem("st_p_retencao"):
        st_ceo "E torce pra ela não fazer aquela mesma pergunta do primeiro ensaio. Spoiler: ela vai fazer."
    else:
        st_ceo "No primeiro ensaio ela ouviu tudo e perguntou uma coisa só. Uma! Tô curioso pra saber se muda."
    hide st_ceo
    with dissolve
    "{i}A mentora levanta a mão. A voz é calma, sem pressa nenhuma.{/i}"
    "{i}\"Dos estudantes que entraram há um mês, quantos ainda usam?\"{/i}"
    "{i}E abaixa a mão. Não pergunta mais nada.{/i}"
    show st_ceo thinking at center_zoom
    with dissolve
    st_ceo "Então! Olha, a gente cresceu muito, a festa dos mil foi um marco, o boca a boca nas repúblicas é incrível, e..."
    "{i}Você anota. Um minuto e vinte segundos de resposta. O número só aparece no fim: dos estudantes do beta, 57 por cento voltam a lançar gastos toda semana. Antes da correção do lançamento duplicado, eram 41.{/i}"
    "{i}A mentora agradece e sai para atender o telefone.{/i}"
    st_ceo "E aí? Fui bem?"
    "{i}Você mostra o caderno. A resposta tem o número certo, mas ele está enterrado embaixo de três frases de festa.{/i}"
    show st_ceo serious
    st_ceo "Pô. Eu comecei pelos cadastros de novo. Ela perguntou de quem fica, e eu respondi de quem chega."
    show st_ceo neutral
    st_ceo "Tá. Número primeiro, festa nunca. Amanhã eu treino com o cronômetro."
    st_ceo "Valeu de verdade. Investidor nenhum me diz onde eu enrolo. Você disse em um minuto!"
    if energia_cansaco():
        "{i}Você sente o peso da manhã nos ombros. Vinícius repara.{/i}"
        st_ceo "Vai comer alguma coisa. Pitch eu ensaio no espelho; cansaço não se ensaia."
    hide st_ceo
    with dissolve
    return

label im_startup_s7_conversar_st_ceo:
    show st_ceo neutral at center_zoom
    with dissolve
    st_ceo "Ei! Pausa no ensaio. Me diz uma coisa: você fica pro demo day, né?"
    st_ceo "Quinta que vem. Quarto da fila. Eu já decorei a ordem de todas as startups."
    show st_ceo thinking
    st_ceo "Vou levar minha mãe. Ela pegou dois ônibus pra me ver formar, então ela vem pra isso também."
    st_ceo "Ela vai sentar na primeira fila e filmar na vertical. Já aceitei."
    st_ceo "E já avisou o grupo da família inteira. Tem tia que vai assistir pela transmissão e comentar em tempo real!"
    show st_ceo neutral
    st_ceo "Quando eu quase larguei a faculdade, foi ela que fez a conta do que faltava no mês. Num caderno, à mão."
    st_ceo "No fundo, o Trocado é aquele caderno. Só que não perde a página!"
    hide st_ceo
    with dissolve
    return
