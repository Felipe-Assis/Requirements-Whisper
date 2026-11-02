# s02.rpy
# Tempo livre da rota Startup, semana 2 (sexta à tarde; o bandejão abre).
# Fonte: docs/design/intermissoes-startup.md (seção 3, Semana 2). A pista
# st_p_cancelar e a amizade com a Bia do "observar" são dadas pelo motor
# depois do return. A mentoria fica em mentoria.rpy.

label im_startup_abertura_2:
    scene bg startup_coworking_tarde
    with dissolve
    "{i}Sexta, três da tarde. A semana teve roteiro, entrevista e post-its.{/i}"
    "{i}Um lugar novo aparece no mapa: o bandejão da universidade, onde a [NOME_ST_ESTUDANTE] almoça e estuda.{/i}"
    if energia_cansaco():
        "{i}Você boceja antes de abrir o mapa. Hoje o tempo livre vai ser mais curto.{/i}"
    return

label im_startup_s2_ajudar_st_techlead:
    show st_techlead neutral at right_zoom
    with dissolve
    st_techlead "Chegou numa boa hora. Veja bem: estou começando uma coisa que devia ter começado há um ano."
    "{i}Ele vira o notebook. Um documento novo, com um título só: \"Registro de decisões\".{/i}"
    show st_techlead thinking at right_zoom
    st_techlead "Uma página por decisão. Quatro partes: o contexto, as opções, a escolhida e o que a gente perde com ela."
    st_techlead "Essa última ninguém escreve. E é a mais importante."
    st_techlead "Tenho três decisões antigas para passar a limpo. Eu conto, você pergunta, você escreve. Topa?"
    "{i}Primeira: funções na nuvem em vez de um servidor ligado o tempo todo.{/i}"
    st_techlead "Contexto: equipe pequena, dinheiro curto, uso concentrado no almoço. Servidor ligado de madrugada é luz acesa em casa vazia."
    st_techlead "O que a gente perde: depois de um tempo parada, a função precisa acordar. A primeira chamada demora mais."
    "{i}Você escreve. Ele lê por cima do seu ombro e troca uma palavra só.{/i}"
    "{i}Segunda: o app funciona sem internet e sincroniza depois.{/i}"
    st_techlead "Contexto: estudante anda de ônibus, entra em túnel, almoça em subsolo. Sem isso, metade dos gastos nem seria lançada."
    st_techlead "O que a gente perde: dois lugares guardando o mesmo dado. Cada vez que eles discordam, alguém precisa decidir quem tem razão."
    "{i}Você lembra do lanche duplicado no túnel. Não diz nada, mas anota ao lado, a lápis.{/i}"
    "{i}Terceira: React Native, um código só para Android e iPhone.{/i}"
    show st_techlead serious at right_zoom
    st_techlead "Contexto... hum."
    "{i}Ele bebe um gole de café. Depois outro. Então vira a cadeira para a outra ponta da mesa.{/i}"
    st_techlead "[NOME_ST_MOBILE], por que a gente escolheu React Native?"
    show st_mobile neutral at left_zoom
    with dissolve
    st_mobile "Pô, achei que tinha sido ideia sua."
    hide st_mobile
    with dissolve
    show st_techlead neutral at right_zoom
    st_techlead "Viu? Decisão sem registro vira lenda."
    st_techlead "Provavelmente foi uma boa escolha. Mas hoje ninguém sabe dizer por quê. Então ninguém sabe dizer quando ela deixa de ser boa."
    "{i}Vocês escrevem a terceira página assim mesmo, com o contexto marcado: \"a reconstruir\".{/i}"
    st_techlead "Obrigado. Isso aqui não é burocracia, é obra com planta. Quem vier reformar sabe onde passa o cano."
    st_techlead "Registro de decisão é carta pro você de daqui a seis meses."
    hide st_techlead
    with dissolve
    return

label im_startup_s2_conversar_st_techlead:
    show st_techlead neutral at right_zoom
    with dissolve
    st_techlead "Então. Como foi a entrevista com a [NOME_ST_ESTUDANTE]?"
    "{i}Você conta: o almoço de R$ 20, o ônibus, a rodinha girando, o toque repetido em Salvar, os três dias sem usar o app.{/i}"
    "{i}Ele escuta calado, os dedos em volta da caneca. Não interrompe nenhuma vez.{/i}"
    show st_techlead thinking at right_zoom
    st_techlead "Uma pergunta só. Ela disse a hora?"
    "{i}Você procura nas anotações. Semana passada, voltando do campus. Hora, nenhuma.{/i}"
    st_techlead "Hum. Não tem problema. Ela contou o que importava para ela."
    st_techlead "Mas repara: história boa tem hora e lugar. Bug também."
    show st_techlead neutral at right_zoom
    st_techlead "Na cozinha é igual. \"O molho azedou\" não ajuda ninguém. \"Azedou na quarta, depois que trocaram o fornecedor\" já é meio caminho."
    "{i}Ele volta para a tela, mas deixa uma última frase no ar.{/i}"
    st_techlead "Se um bug desses já aconteceu com você, guarda a hora. Eu vou querer saber."
    hide st_techlead
    with dissolve
    return

label im_startup_s2_conversar_st_mobile:
    show st_mobile neutral at left_zoom
    with dissolve
    "{i}[NOME_ST_MOBILE] lança gastos de teste no Tijolo, um atrás do outro, e confere a lista a cada três.{/i}"
    st_mobile "Quer ouvir uma história de terror? Meu primeiro bug em produção."
    show st_mobile thinking at left_zoom
    st_mobile "Primeiro app que eu publiquei, um controle de mesada. Gasto lançado às 23h50 aparecia no dia seguinte."
    st_mobile "Passei dois dias procurando. Era o fuso. O servidor estava em outro horário, e dez minutos viravam um dia inteiro."
    st_mobile "Até hoje eu confiro horário três vezes. Fuso horário? Pra mim é confuso horário."
    show st_mobile neutral at left_zoom
    st_mobile "Mano, o tempo é o pior inimigo do programador. Fuso, relógio e prazo."
    st_mobile "Mudando de assunto: sábado tem partida online de novo. A vaga continua aberta, hein?"
    "{i}Você diz que vai pensar. Ele finge que acredita.{/i}"
    st_mobile "Fechou. Se não aparecer, eu digo pro time que você estava descansando. É a única desculpa que a [NOME_ST_QUALIDADE] aceita."
    hide st_mobile
    with dissolve
    return

label im_startup_s2_conversar_st_ceo:
    show st_ceo neutral at center_zoom
    with dissolve
    "{i}[NOME_ST_CEO] fecha o notebook com cuidado, como quem acabou de sair de uma prova.{/i}"
    st_ceo "Call com o fundo. Quarenta minutos! Falei \"tração\" umas dez vezes. Acho que é recorde."
    show st_ceo thinking at center_zoom
    st_ceo "Posso te perguntar uma coisa? Sem filtro."
    st_ceo "O que a [NOME_ST_ESTUDANTE] achou de mim? Na entrevista. Eu falei de Open Finance e ela fez uma cara..."
    "{i}Você lembra da frase dela: medalha não paga almoço. E escolhe um jeito gentil de contar.{/i}"
    st_ceo "É. Eu imaginei."
    st_ceo "Sabe por que eu falo desse jeito? \"Tração\", \"engajamento\", \"escala\". É a língua do fundo. Se eu não falo, eles não escutam."
    show st_ceo neutral at center_zoom
    st_ceo "Mas quando fecho o olho, penso na minha mãe contando moeda na mesa da cozinha, no fim do mês."
    st_ceo "Talvez eu devesse contar isso pra [NOME_ST_ESTUDANTE]. Dez segundos de mãe valem mais que cem slides!"
    "{i}Ele abre o notebook de novo e apaga um slide inteiro. Depois sorri, meio sem graça.{/i}"
    hide st_ceo
    with dissolve
    return

label im_startup_s2_estudar_sala_vidro:
    "{i}No canto da sala de vidro, longe da call do [NOME_ST_CEO], você abre o roteiro de segunda e as anotações da entrevista.{/i}"
    "{i}Você pega duas canetas e passa por todas as perguntas que estavam na mesa, as que você fez e as que poderia ter feito: verde para as que abrem a conversa, vermelha para as que fecham.{/i}"
    "{i}\"Qual funcionalidade você mais quer: modo escuro ou medalhas?\" Vermelho. A resposta seria um palpite entre duas soluções prontas, e ninguém descobriria o que dói.{/i}"
    "{i}\"Me conta a última vez em que isso aconteceu?\" Verde. Daí saíram o ônibus, o almoço de R$ 20 e os três dias sem usar.{/i}"
    "{i}\"Você usaria mais se a tela tivesse menos botões?\" Vermelho. Sim ou não confirma uma ideia nossa. Não descobre nada dela.{/i}"
    "{i}No fim, o padrão aparece sozinho: quem pergunta \"como\" e \"me conta\" ouve um episódio. Quem pergunta \"você gostaria\" ouve uma opinião.{/i}"
    "{i}Você copia o padrão para o caderno, com um exemplo de cada lado.{/i}"
    return

label im_startup_s2_conversar_st_mentora:
    show st_mentora neutral at left_zoom
    with dissolve
    "{i}No café, [NOME_ST_MENTORA] relê as anotações da entrevista, com uma caneta coral atrás da orelha.{/i}"
    st_mentora "Senta aqui. Estou relendo a parte da discussão. Você lembra de algo que eu não anotei?"
    "{i}Você lembra: a [NOME_ST_ESTUDANTE] dizendo que não dá acesso ao banco, e o [NOME_ST_CEO] insistindo na praticidade.{/i}"
    show st_mentora thinking at left_zoom
    st_mentora "Isso. Repara que os dois brigavam por solução. Um queria importar do banco. A outra queria apagar o gasto repetido."
    st_mentora "Quando duas pessoas brigam por solução, eu volto pro problema. Ninguém briga pelo problema."
    st_mentora "E repito com as palavras da pessoa, não com as minhas. \"Você quer abrir o app e confiar no número.\" Pronto: os dois concordam."
    show st_mentora neutral at left_zoom
    st_mentora "Aprendi isso no banco, atendendo cliente bravo. Me conta: o que você teria feito?"
    "{i}Você confessa que teria tentado convencer um dos dois. Ela ri.{/i}"
    st_mentora "Todo mundo tenta, na primeira vez. A gente não convence ninguém. A gente acha o que os dois já querem."
    hide st_mentora
    with dissolve
    return

label im_startup_s2_conversar_st_estudante:
    show st_estudante neutral at right_zoom
    with dissolve
    "{i}No bandejão, [NOME_ST_ESTUDANTE] estuda Cálculo com um copo de suco já vazio do lado e o caderno de capa de flores embaixo da apostila.{/i}"
    st_estudante "Oi! Senta. Já almocei: bandejão, R$ 4,50, lançado e conferido."
    "{i}Você pergunta do caderno. Ela passa a mão na capa.{/i}"
    show st_estudante thinking at right_zoom
    st_estudante "Minha avó mora na beira do Rio Negro. Lá, sinal de celular é luxo. Pega num canto do quintal, se não chover."
    st_estudante "Ela anota tudo no papel: o que vendeu, o que comprou, quem ficou devendo. Eu cresci vendo."
    st_estudante "Quando vim estudar no Rio, trouxe o costume. Tipo assim: o caderno nunca ficou sem sinal."
    show st_estudante neutral at right_zoom
    "{i}Ela balança o chaveiro de boto-cor-de-rosa preso no zíper da mochila.{/i}"
    st_estudante "Presente dela. Disse que boto encanta gente. Eu disse que ia encantar o professor de Cálculo."
    st_estudante "Égua, não funcionou ainda. Mas faltam duas provas."
    hide st_estudante
    with dissolve
    return

label im_startup_s2_observar_bandejao:
    show st_qualidade neutral at left_zoom
    with dissolve
    st_qualidade "Chegou na hora. A [NOME_ST_ESTUDANTE] topou que a gente observe a tarde dela por aqui. Eu pedi antes, ela sabe de tudo."
    st_qualidade "Primeiro: a gente olha a tela, não o rosto, e não filma nada. Segundo: ela pode mandar a gente embora quando quiser."
    show st_qualidade thinking at left_zoom
    st_qualidade "Terceiro, o mais difícil: a gente não ajuda. Nem um dedinho apontando."
    hide st_qualidade
    with dissolve
    "{i}Vocês sentam duas mesas atrás. O almoço já passou. A [NOME_ST_ESTUDANTE] está numa mesa com duas amigas da república, entre apostilas e celulares.{/i}"
    show st_estudante neutral at right_zoom
    with dissolve
    "{i}Ela vai até o balcão da lanchonete e volta com um suco. Na mesa, começa a lançar: R$ 6. Antes de salvar, a amiga empurra uma nota para ela: \"Esse é por minha conta.\"{/i}"
    "{i}Ela toca em Cancelar. E, logo em seguida, abre a lista. Desce, sobe, confere. Depois tira o caderno da mochila e confere de novo.{/i}"
    "{i}Você anota: cancelou, conferiu a lista, conferiu o caderno. Doze segundos.{/i}"
    "{i}Nos vinte minutos seguintes, ela abre o total três vezes. Não lança nada novo. Só olha o número e fecha.{/i}"
    "{i}Sua mão quer levantar para perguntar por quê. A [NOME_ST_QUALIDADE] percebe e balança a cabeça, devagar.{/i}"
    "{i}Quarenta minutos depois, as amigas vão para a aula. A [NOME_ST_ESTUDANTE] acena para vocês e puxa duas cadeiras.{/i}"
    show st_qualidade neutral at left_zoom
    with dissolve
    st_estudante "E aí? Fui uma boa cobaia?"
    st_qualidade "Cobaia não. Especialista no próprio uso. É diferente."
    "{i}Você pergunta, com cuidado, por que ela conferiu tudo depois de cancelar o suco.{/i}"
    show st_estudante thinking at right_zoom
    st_estudante "Ah. Nem percebi que fiz isso."
    st_estudante "Depois do almoço duplicado, toda vez que eu desisto eu confiro se nada mudou."
    st_estudante "Tipo assim: eu cancelei. Mas será que o app fez o que eu mandei? Prefiro olhar."
    show st_qualidade thinking at left_zoom
    "{i}[NOME_ST_QUALIDADE] se inclina para você e fala baixinho.{/i}"
    st_qualidade "Ninguém conta isso numa entrevista."
    "{i}No seu caderno, a frase da [NOME_ST_ESTUDANTE] ganha um círculo.{/i}"
    hide st_estudante
    hide st_qualidade
    with dissolve
    return

label im_startup_s2_conversar_st_qualidade:
    show st_qualidade neutral at left_zoom
    with dissolve
    st_qualidade "Já provou o bandejão? R$ 4,50 com suco. Oxe, melhor negócio do Rio."
    st_qualidade "Arroz, feijão, farofa e uma carne que muda de nome todo dia. Eu venho até sem motivo."
    "{i}Você pergunta como é observar alguém usando o app. Ela pensa antes de responder.{/i}"
    show st_qualidade thinking at left_zoom
    st_qualidade "A parte difícil não é ver. É ficar quieta quando a pessoa erra."
    st_qualidade "Ela toca no botão errado, você sabe onde está o certo, e a mão coça."
    st_qualidade "Se eu ajudo, eu aprendo como eu uso o app. Não como ela usa."
    show st_qualidade neutral at left_zoom
    st_qualidade "Primeiro: sentar longe o bastante. Segundo: ter um caderno, para a mão ficar ocupada. Terceiro: comer devagar, que aí a boca também fica."
    "{i}Ela aponta para o prato pela metade, com a seriedade de quem ensina um método.{/i}"
    hide st_qualidade
    with dissolve
    return
