# s03.rpy
# Tempo livre da rota Startup, semana 3 (sexta à tarde, depois da inspeção).
# Fonte: docs/design/intermissoes-startup.md (seção 3, Semana 3). A pista
# st_p_tunel e a amizade com a Bia do "observar" são dadas pelo motor depois
# do return. A mentoria fica em mentoria.rpy.

label im_startup_abertura_3:
    scene bg startup_coworking_tarde
    with dissolve
    "{i}Sexta, três da tarde. A especificação passou pela lupa da [NOME_ST_QUALIDADE] na quarta.{/i}"
    "{i}Na parede de vidro, um post-it sozinho na coluna de perguntas abertas: \"e se ela excluir sem internet?\".{/i}"
    if energia_cansaco():
        "{i}Você boceja antes de abrir o mapa. Hoje o tempo livre vai ser mais curto.{/i}"
    return

label im_startup_s3_conversar_st_mobile:
    show st_mobile neutral at left_zoom
    with dissolve
    "{i}[NOME_ST_MOBILE] liga o protótipo da confirmação no Tijolo. A pergunta \"Excluir este gasto?\" aparece com um atraso que ele mede no relógio.{/i}"
    st_mobile "O pareamento dessa semana foi bom, hein? Rendeu mais do que eu sozinho numa semana inteira."
    show st_mobile thinking at left_zoom
    st_mobile "Quando você navega, eu erro menos. Quando eu navego, você pergunta mais. Todo mundo ganha."
    st_mobile "Você fez umas três perguntas que eu fingi que sabia responder. Fui pesquisar. Agora eu sei de verdade."
    show st_mobile neutral at left_zoom
    st_mobile "Posso te contar um segredo? Meu sonho é fazer um jogo. De ritmo. Sobre pegar ônibus."
    st_mobile "Você corre no compasso da música, e o motorista fecha a porta no contratempo. Errou a batida, perdeu o ônibus: vinte minutos de tela preta."
    st_mobile "Realismo, mano. A fase \"Botafogo às seis da tarde\" é o chefão."
    "{i}Você sugere um nome para o jogo. Ele anota num post-it amarelo e cola no monitor, ao lado de outros seis nomes.{/i}"
    st_mobile "Fechou, entrou na lista. O jogo ainda não tem uma linha de código. Mas já tem sete nomes. Prioridades!"
    hide st_mobile
    with dissolve
    return

label im_startup_s3_conversar_st_mentora:
    show st_mentora neutral at left_zoom
    with dissolve
    "{i}[NOME_ST_MENTORA] escreve critérios de aceitação no notebook, um por linha, todos com valores.{/i}"
    st_mentora "Viu o post-it sozinho no quadro? \"E se ela excluir sem internet?\" Foi o [NOME_ST_MOBILE] que perguntou."
    show st_mentora thinking at left_zoom
    st_mentora "Eu tenho um palpite. Mas não vou chutar a resposta dele."
    st_mentora "Quem sabe como o gasto anda entre o celular e a nuvem é o [NOME_ST_TECHLEAD]. Ele está olhando os registros. A gente espera."
    "{i}Você pergunta se a pergunta parada não atrasa o cartão.{/i}"
    st_mentora "Atrasa um pouco. Mas pergunta aberta não é falha."
    st_mentora "Falha é chutar a resposta e esquecer que chutou. Aí a gente constrói em cima de palpite e descobre no lançamento."
    show st_mentora neutral at left_zoom
    st_mentora "Por isso a coluna existe: a dúvida fica à vista até alguém responder de verdade."
    st_mentora "Bora? Me ajuda a reler esse critério. Tem um \"rápido\" escondido aqui que a [NOME_ST_QUALIDADE] vai pegar."
    hide st_mentora
    with dissolve
    return

label im_startup_s3_conversar_st_techlead:
    show st_techlead thinking at right_zoom
    with dissolve
    "{i}Na sala de vidro, [NOME_ST_TECHLEAD] tem duas janelas lado a lado: a sua mensagem da semana passada e uma lista longa de registros do servidor.{/i}"
    "{i}Sexta, 19h40, entrando no túnel, lanche de R$ 7. Ele desce a lista até aquele minuto e para.{/i}"
    st_techlead "Achei uma coisa no registro daquele minuto."
    "{i}Você espera o resto. Ele bebe um gole de café, sem pressa.{/i}"
    st_techlead "Não vou contar. Veja bem: não é mistério de propósito."
    st_techlead "Se eu contar, você imagina. Se eu mostrar, você vê. Segunda, com o [NOME_ST_MOBILE] e três celulares, eu te mostro."
    show st_techlead neutral at right_zoom
    st_techlead "Bug se mostra reproduzindo, não contando."
    st_techlead "É como provar o molho antes de servir. Ninguém confia no cozinheiro que diz \"tá bom, eu acho\"."
    st_techlead "A colher vai na panela, e todo mundo prova junto."
    "{i}Ele fecha a lista de registros. Na tela, fica só a sua mensagem, com o horário marcado em amarelo.{/i}"
    st_techlead "E obrigado pelo horário. Sem ele, eu estaria procurando agulha num palheiro de três semanas."
    hide st_techlead
    with dissolve
    return

label im_startup_s3_estudar_sala_vidro:
    "{i}Do outro lado da sala de vidro, [NOME_ST_TECHLEAD] está mergulhado nos registros. Você pega o canto livre e abre as três versões da história de segunda.{/i}"
    "{i}Na tela, a lista INVEST: Independente, Negociável, Valiosa, Estimável, Pequena, Testável. Seis perguntas para cada cartão.{/i}"
    "{i}\"Como usuário, quero um app fácil de usar.\" Valiosa, talvez. Estimável, não: ninguém sabe o tamanho de \"fácil\". Pequena, não. Testável, nunca.{/i}"
    "{i}\"Como sistema, quero um botão Excluir na lista de gastos.\" Pequena e estimável, sim. Mas valiosa para quem? Sistema não perde dinheiro. Falha no V.{/i}"
    "{i}\"Como estudante que lançou um gasto por engano, quero excluí-lo com uma confirmação, para que o total do mês volte a ser confiável.\" Passa nas seis. Dá até para imaginar o teste.{/i}"
    "{i}Você anota ao lado: a primeira falha em quase tudo, a segunda falha no motivo, a terceira cabe num ciclo e tem critério.{/i}"
    "{i}Lista de checagem não escreve história. Mas mostra rápido onde ela manca.{/i}"
    return

label im_startup_s3_conversar_st_ceo:
    show st_ceo neutral at center_zoom
    with dissolve
    "{i}No café, [NOME_ST_CEO] lê um livro de métricas de capa laranja. As páginas estão cheias de sublinhado.{/i}"
    st_ceo "Lição de casa! Segunda reunião com o fundo chegando. Dessa vez eu vou entrar sabendo os números."
    show st_ceo thinking at center_zoom
    st_ceo "Olha esse capítulo: métricas de vaidade. Número que sobe, fica lindo no slide e não diz nada sobre o negócio."
    st_ceo "Downloads. Cadastros. Seguidores. Eu tinha os três no meu pitch. Em destaque!"
    st_ceo "Sublinhei a palavra \"vaidade\" três vezes. Acho que o livro tava falando comigo!"
    "{i}Você pergunta qual número ele vai levar, então.{/i}"
    st_ceo "Pois é. Ainda não sei. Tô no capítulo quatro de doze."
    show st_ceo neutral at center_zoom
    st_ceo "Mas uma coisa eu já aprendi: número bonito no slide não paga o almoço de ninguém. A Bia ia gostar dessa frase!"
    st_ceo "Próximo capítulo: \"Como não se apaixonar pelo próprio gráfico\". Esse vai doer!"
    hide st_ceo
    with dissolve
    return

label im_startup_s3_conversar_st_estudante:
    show st_estudante neutral at right_zoom
    with dissolve
    "{i}No subsolo do bandejão, [NOME_ST_ESTUDANTE] divide a mesa com uma pilha de listas de exercício. Prova na terça.{/i}"
    st_estudante "Oi! Fala baixo, que aqui é minha sala de estudo. Ninguém desce pro subsolo, só eu e o ar-condicionado barulhento."
    st_estudante "Eu sou monitora de Cálculo, sabia? Explico derivada pra calouro duas vezes por semana."
    "{i}Você confessa que derivada nunca entrou direito na sua cabeça. Ela fecha a apostila.{/i}"
    show st_estudante thinking at right_zoom
    st_estudante "Tipo assim: a bolsa caiu faz vinte dias. Eram R$ 600. Hoje eu tenho R$ 120."
    st_estudante "Égua, derivada é só quanto o saldo muda por dia. No meu caso, muda pra baixo. Isso eu entendo bem."
    st_estudante "Caiu R$ 480 em vinte dias: menos R$ 24 por dia, em média. Se começa a cair mais rápido, a derivada fica mais negativa. E eu me preocupo."
    show st_estudante neutral at right_zoom
    st_estudante "Os calouros entendem na hora. Dinheiro ensina Cálculo melhor que muito livro."
    "{i}Ela anota a sua dúvida no canto da lista, do jeito que faz com os calouros.{/i}"
    hide st_estudante
    with dissolve
    return

label im_startup_s3_observar_bandejao:
    show st_qualidade neutral at left_zoom
    with dissolve
    st_qualidade "Hoje ela estuda no subsolo e chamou a gente para descer junto. Mesma regra da outra vez: olhar, anotar, não ajudar."
    hide st_qualidade
    with dissolve
    "{i}A escada desce para uma sala de luz fria, com mesas compridas e um ar-condicionado barulhento. No meio da escada, o 4G do seu celular some.{/i}"
    show st_estudante neutral at right_zoom
    with dissolve
    "{i}[NOME_ST_ESTUDANTE] divide a mesa com a Rayane, colega de república, e com dois sucos da lanchonete.{/i}"
    st_estudante "Rayane, vou lançar os dois sucos agora, o meu e o seu. Depois a gente acerta."
    "{i}Ela lança dois sucos de R$ 6, um depois do outro. De propósito: um dela, um da Rayane. A rodinha gira um tempo em cada um, mas salva.{/i}"
    "{i}Você anota: dois sucos de R$ 6, iguais, os dois verdadeiros.{/i}"
    "{i}Quando a fila do jantar abre lá em cima, ela sobe, volta com a bandeja e lança o bandejão: R$ 4,50.{/i}"
    "{i}Desta vez a tela trava. A rodinha gira, gira, e não sai do lugar. Ela espera cinco segundos e toca em Salvar de novo.{/i}"
    "{i}A tela destrava. Na lista, dois bandejões de R$ 4,50.{/i}"
    show st_estudante thinking at right_zoom
    st_estudante "Égua, de novo."
    "{i}Ela não reclama mais do que isso. Puxa o caderno de capa de flores e escreve, com letra firme: \"duplicou no subsolo\".{/i}"
    "{i}A [NOME_ST_QUALIDADE] te cutuca e aponta a tela. Você olha a lista de cima a baixo.{/i}"
    "{i}Dois sucos de R$ 6. Dois bandejões de R$ 4,50. As duas duplas parecem iguais.{/i}"
    show st_qualidade thinking at left_zoom
    with dissolve
    st_qualidade "Oxe. Se eu olhasse só a lista, ia achar que os sucos também estavam errados."
    st_estudante "Os sucos tão certos. Um é meu, outro da Rayane. Só sei disso porque eu lembro."
    st_estudante "Tipo assim: na lista, um suco é igual ao outro. Quem lembra a diferença é o caderno."
    "{i}Você anota o horário, o lugar, o que ela fez e o que apareceu na tela. Do jeito que o [NOME_ST_TECHLEAD] gosta.{/i}"
    hide st_estudante
    hide st_qualidade
    with dissolve
    return

label im_startup_s3_conversar_st_qualidade:
    show st_qualidade neutral at left_zoom
    with dissolve
    "{i}[NOME_ST_QUALIDADE] espera a fila do suco diminuir, batendo o pé num ritmo que não é de samba.{/i}"
    st_qualidade "Percebeu? É forró. O pé não esquece."
    show st_qualidade thinking at left_zoom
    st_qualidade "Em Campina Grande, o São João é o maior do mundo. A gente fala isso sem modéstia nenhuma."
    st_qualidade "Com quinze anos, eu organizei a quadrilha da escola. Trinta pares, um sanfoneiro e uma professora de Geografia gritando \"anarriê\"."
    st_qualidade "Foi ali que eu aprendi a observar gente. Lá da frente, você vê tudo: quem sabe o passo, quem copia o vizinho, quem finge."
    show st_qualidade neutral at left_zoom
    st_qualidade "Oxe, quem organiza quadrilha sabe testar fluxo: sempre tem um par que entra na hora errada."
    st_qualidade "E não adianta brigar com o par. Você muda a marcação para ele entrar certo da próxima vez."
    "{i}Você pergunta se ela ainda dança.{/i}"
    st_qualidade "Todo ano. Primeiro: tiro férias em junho. Segundo: ninguém marca reunião comigo. Terceiro: volto com dois quilos de queijo coalho."
    hide st_qualidade
    with dissolve
    return
