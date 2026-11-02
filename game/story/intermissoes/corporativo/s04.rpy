# s04.rpy
# Tempo livre da rota Corporativo, semana 4 (sexta, 13h às 16h), entre a
# co_13 e a co_14. Ninguém sabe ainda dos 25 anos do Jorge nem da
# aposentadoria: nada aqui cita março.
# Roteiro: docs/design/intermissoes-corporativo.md, seção 2.5.
# O motor (logic/intermissao.rpy) põe o fundo, cobra tempo e energia e dá a
# recompensa depois do label; aqui ficam só as falas. A mentoria com o Jorge
# fica em im_corporativo_mentoria_<k>. Descansar tem label por semana
# (im_corporativo_s4_descansar_*), como nas semanas 1 e 2.

label im_corporativo_abertura_4:
    $ im_mostrar_local({"poi": im_local})
    with dissolve
    "{i}Sexta, uma da tarde. O andar ainda cheira a almoço, e o diagrama de terça continua no quadro, com a figueira desenhada num canto.{/i}"
    if energia_exaustao():
        show co_mentora serious at center_zoom
        with dissolve
        co_mentora "Vamos por partes, e a primeira parte é sentar. Hoje dá para pouca coisa, e tudo bem."
        hide co_mentora
        with dissolve
    elif energia_cansaco():
        show co_mentora neutral at center_zoom
        with dissolve
        co_mentora "Você está com cara de semana longa. Hoje o tempo livre é mais curto. Se eu fosse você, começava pelo café do térreo."
        hide co_mentora
        with dissolve
    return

# ---------------- Baia do Farol ----------------

label im_corporativo_s4_conversar_co_legado:
    "{i}Na baia do Farol, [NOME_CO_LEGADO] tira uma folha da impressora, lê a primeira linha e vira o papel para baixo quando você chega.{/i}"
    show co_legado neutral at center_zoom
    with dissolve
    co_legado "Papelada do RH. Coisa chata, não repara."
    co_legado "Senta aí, [player_name]. A reunião de terça foi boa. A figueira mata-pau ganhou nome técnico."
    co_legado "Em 2016 a gente chamava de reescrita e prometia tudo para um sábado. Deu catorze meses e uma caixa de CDs no arquivo."
    "{i}Você pergunta o que ele achou do desenho de microsserviços do [NOME_CO_DEV].{/i}"
    show co_legado thinking at center_zoom
    co_legado "Bonito. Sério. Ele desenha melhor que eu."
    co_legado "Só que desenho não mostra o que está pendurado no sistema. Quem mostra é quem já foi acordado por ele às 3h da manhã."
    "{i}Ele olha o relógio de pulso e empilha a papelada, ainda virada para baixo.{/i}"
    show co_legado neutral at center_zoom
    co_legado "Às quatro tenho diretoria. Se eu não voltar, a Tia Neide herda a caneca."
    hide co_legado
    with dissolve
    return


# ---------------- Central de atendimento ----------------

label im_corporativo_s4_conversar_co_supervisora:
    "{i}Na central, [NOME_CO_SUPERVISORA] está de pé ao lado do painel de filas, com um fichário grosso debaixo do braço.{/i}"
    show co_supervisora neutral at center_zoom
    with dissolve
    co_supervisora "Fiquei sabendo da terça. Uma tabela que guarda quem mudou o quê, e ninguém apaga. É isso mesmo?"
    "{i}Você confirma: cada mudança vira uma linha nova, com autor, perfil e horário.{/i}"
    co_supervisora "Então olha isso."
    "{i}Ela abre o fichário. É a planilha da auditoria de 2021, impressa. Cada aba tem uma cor e um nome escrito à caneta.{/i}"
    co_supervisora "Uma semana inteira cruzando e-mail, print e memória de atendente para explicar chamado fechado."
    show co_supervisora thinking at center_zoom
    co_supervisora "Só um pedido. Essa trilha tem que ser lida por quem não é da TI. Pela auditoria, por mim, pela Neusa."
    co_supervisora "Se eu precisar de alguém do lado traduzindo código, não me serve."
    show co_supervisora neutral at center_zoom
    co_supervisora "Catorze abas. Se essa trilha funcionar, eu apago essa planilha com prazer."
    hide co_supervisora
    with dissolve
    return

label im_corporativo_s4_observar_central:
    "{i}A central almoça em turnos, do meio-dia às três. Metade das baias está vazia.{/i}"
    "{i}[NOME_CO_SUPERVISORA] deixa você sentar ao lado da Neusa, com um headset sem microfone, só para ouvir.{/i}"
    show co_supervisora thinking at right_zoom
    with dissolve
    co_supervisora "Hoje são sete atendentes para catorze posições. Repara no painel."
    "{i}No painel, duas barras crescem ao mesmo tempo: a fila geral e a fila de senha.{/i}"
    "{i}A Neusa fecha uma ligação da fila geral e já puxa outra da fila de senha. Ela cobre as duas sem tirar o headset.{/i}"
    co_supervisora "Paulo, você almoça agora ou no próximo turno?"
    "{i}Lá do fundo, o Paulo levanta um dedo, pensa e levanta dois. Ela olha o relógio de pulso e anota num papel.{/i}"
    co_supervisora "Então segura até o próximo. A Neusa almoça primeiro, que ela já está na terceira de senha seguida."
    "{i}Em cinco minutos, a barra da fila de senha para de crescer. A da fila geral desce um pouco.{/i}"
    "{i}Você anota no caderno: mudou a escala, mudou a espera. Sem tela nova, sem sistema novo.{/i}"
    show co_supervisora neutral at right_zoom
    co_supervisora "Ninguém trabalhou mais rápido. Eu só mudei quem senta onde, e quando."
    co_supervisora "Quando o Farol entrar, quero ver se ele me ajuda nisso ou se é só mais uma aba para abrir."
    co_supervisora "Hora do almoço é quando o SLA mostra quem planejou e quem torceu."
    hide co_supervisora
    with dissolve
    "{i}Você sai da central com uma linha a mais no caderno: o número do painel depende de gente, não só de código.{/i}"
    return


# ---------------- Café do térreo ----------------

label im_corporativo_s4_conversar_co_mentora:
    "{i}No café do térreo, [NOME_CO_MENTORA] tem o caderno vinho aberto ao lado de um pão de queijo pela metade. Ela puxa uma banqueta para você.{/i}"
    show co_mentora neutral at center_zoom
    with dissolve
    if co_negociacao_opcao == "investigar_agora":
        co_mentora "O [NOME_CO_DEV] já marcou conversa com o jurídico sobre o WhatsApp. Pela primeira vez, ele pediu reunião antes de abrir o editor."
        co_mentora "E o [NOME_CO_SOLICITANTE] avisou a equipe dele que vai ter piloto. Agora é cumprir o que foi combinado."
    else:
        co_mentora "O [NOME_CO_SOLICITANTE] mandou um joinha no acordo de terça. Hoje cedo já perguntou quando começa a próxima rodada."
        co_mentora "Quem pergunta da próxima rodada aceitou esta. É um bom sinal."
    co_mentora "E você? O que achou de conduzir aquela conversa?"
    "{i}Você conta que o mais difícil foi não prometer nada antes de saber o tamanho.{/i}"
    show co_mentora thinking at center_zoom
    co_mentora "Eu aprendi isso do outro lado, quando era atendente na central. A TI dizia \"não dá\" para tudo que a gente pedia, e ninguém explicava o motivo."
    co_mentora "Um dia um analista levou uma folha: para caber o nosso pedido, saía isso e isso. Pela primeira vez, a central aceitou esperar."
    show co_mentora neutral at center_zoom
    co_mentora "Quem diz só \"não cabe\" perde a conversa. Quem mostra o que sai para caber, ganha um acordo."
    hide co_mentora
    with dissolve
    return

label im_corporativo_s4_conversar_co_qualidade:
    "{i}Na mesinha da janela, [NOME_CO_QUALIDADE] tem o tablet apoiado no açucareiro. Na tela, um modelo de RFC quase em branco.{/i}"
    show co_qualidade neutral at center_zoom
    with dissolve
    co_qualidade "Já abri a RFC do Farol. Preenchi o título. É um começo."
    co_qualidade "Semana que vem é semana de calendário: janela, CAB, quem fica de plantão. Eu chamo de semana de agenda cheia e unha roída."
    "{i}Você pergunta por onde ela começaria, se a RFC fosse dela sozinha.{/i}"
    show co_qualidade thinking at center_zoom
    co_qualidade "Pelo fim. O CAB lê primeiro o plano de volta. Se não tem, nem lê o resto."
    co_qualidade "Depois o impacto: quem usa, que tabela mexe, o que para se der errado. O que muda, todo mundo sabe escrever."
    show co_qualidade neutral at center_zoom
    co_qualidade "RFC é como mala de viagem. Você descobre o que esqueceu quando já está longe."
    co_qualidade "Por isso eu faço lista. Registrada, claro."
    hide co_qualidade
    with dissolve
    return


# ---------------- Refeitório ----------------

label im_corporativo_s4_conversar_co_dev:
    "{i}No refeitório quase vazio, [NOME_CO_DEV] almoça atrasado, com os fones no pescoço e o celular apoiado no copo de suco.{/i}"
    show co_dev neutral at center_zoom
    with dissolve
    co_dev "Bora, senta! Almoço atrasado. O melhor horário: ninguém na fila do bufê."
    if co_negociacao_opcao == "investigar_agora":
        "{i}Na tela do celular, a documentação da API oficial do WhatsApp, cheia de trechos marcados em amarelo.{/i}"
        co_dev "Estou lendo as regras do provedor. Tem mais termo de uso do que código. O jurídico vai se divertir."
    show co_dev thinking at center_zoom
    co_dev "Vou ser sincero. Ainda sinto falta da reescrita. Eu tinha desenhado até o nome de cada serviço."
    co_dev "Mas pensei nisso a semana toda. Talvez os serviços sejam o destino, e a figueira do [NOME_CO_LEGADO] seja o caminho. Um não precisa matar o outro."
    "{i}Você pergunta o que ele vai fazer primeiro na camada.{/i}"
    show co_dev neutral at center_zoom
    co_dev "Traduzir estado. O SGC fala código 3, o Farol fala Em atendimento. Parece bobo, mas é ali que mora metade dos bugs."
    co_dev "Perdi a reescrita, ganhei um tradutor. Camada anticorrupção parece nome de série policial."
    hide co_dev
    with dissolve
    return


# ---------------- Sala do arquivo ----------------

label im_corporativo_s4_estudar_arquivo:
    "{i}A sala do arquivo está vazia. Na mesa, alguém esqueceu uma impressão do diagrama de terça, com uma mancha de café no canto do SGC.{/i}"
    "{i}Na estante ao lado, um relatório encadernado de 2014. Na coluna de estado, só números: 1, 2, 3, 5, 7.{/i}"
    "{i}Você abre o caderno e faz duas colunas. À esquerda, o código do SGC. À direita, o que o Farol mostraria para o [NOME_CO_SOLICITANTE].{/i}"
    "{i}O 3 vira Em atendimento. O 5 vira Resolvido. O 7 você não sabe, e escreve isso mesmo: perguntar ao [NOME_CO_LEGADO].{/i}"
    "{i}Fica claro para que serve a camada do meio. O Farol nunca precisa saber que existe um código 7. Se um dia o SGC mudar a tabela, só a tradução muda.{/i}"
    "{i}E é ali que dá para barrar o que chega torto, como uma descrição vazia vinda da integração.{/i}"
    "{i}Você escreve no alto da página: camada anticorrupção. Um tradutor com regras e com teste.{/i}"
    return


# ---------------- Descansar ----------------

label im_corporativo_s4_descansar_cafe:
    "{i}Depois do almoço, o café do térreo vira fila de expresso. Você pega um coado e foge para a banqueta perto da porta giratória.{/i}"
    "{i}Na vitrine da lojinha ao lado, canecas brancas esperam alguém gravar um nome nelas.{/i}"
    if energia_cansaco():
        "{i}Você quase cochila com a xícara na mão. O atendente tira a xícara com cuidado e deixa um copo d'água no lugar.{/i}"
    else:
        "{i}Por meia hora ninguém fala de SLA. Você vê o Centro passando lá fora e deixa a cabeça desligar.{/i}"
    return

label im_corporativo_s4_descansar_refeitorio:
    "{i}O refeitório esvazia depois das duas. Sobram as bandejas empilhadas e a baía inteira na janela.{/i}"
    "{i}Você pega um chá de máquina e escolhe a mesa mais longe do balcão.{/i}"
    if energia_cansaco():
        "{i}Você deita a cabeça nos braços por dez minutos. Ninguém repara.{/i}"
    else:
        "{i}Você não abre o notebook. Conta os barcos atravessando a baía e perde a conta no sétimo.{/i}"
    return

label im_corporativo_s4_descansar_aterro:
    "{i}Quinze minutos a pé e a torre fica para trás. No começo da tarde, o Aterro é quase só sol, gramado e gente correndo de boné.{/i}"
    if energia_cansaco():
        "{i}Você acha uma árvore de copa larga e senta na grama. O vento da baía faz o que o café não conseguiu.{/i}"
    else:
        "{i}Você anda pelo calçadão até a água. Um ambulante vende mate gelado, e você aceita sem pensar duas vezes.{/i}"
    return
