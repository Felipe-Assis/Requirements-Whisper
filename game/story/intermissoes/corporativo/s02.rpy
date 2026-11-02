# s02.rpy
# Tempo livre da rota Corporativo, semana 2 (sexta, 16h30 às 19h30, logo
# depois do café da co_07). Fonte: docs/design/intermissoes-corporativo.md,
# seções 2.1 e 2.3, e o Aterro aceito em docs/design/mapa-cidade.md §2.3.
# O motor aplica tempo, energia, amizade, pista e registro extra; aqui só há
# fala. A mentoria com o Jorge fica em im_corporativo_mentoria_<k>.

label im_corporativo_abertura_2:
    $ im_mostrar_local({"poi": im_local})
    with dissolve
    "{i}Sexta, quatro e meia. O expresso do café ainda está na boca, e a torre começa a esvaziar andar por andar.{/i}"
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


# -------------------------------
# Baia do Farol
# -------------------------------
label im_corporativo_s2_conversar_co_dev:
    show co_dev neutral at center_zoom
    with dissolve
    "{i}Na tela de [NOME_CO_DEV], o print do comentário \"NAO MEXER - JT 2010\" ganhou uma moldura dourada desenhada à mão no editor de imagem.{/i}"
    co_dev "Opinião sincera: a moldura está exagerada ou está no ponto?"
    "{i}Você lembra que o [NOME_CO_LEGADO] exigiu placa.{/i}"
    co_dev "Verdade! Plaquinha embaixo: \"Patrimônio tombado\". Vou pedir para a [NOME_CO_QUALIDADE] registrar como ativo."
    show co_dev thinking at center_zoom
    co_dev "Sabe por que eu gosto daqui? Todo arquivo do SGC tem um mistério. Você abre achando que é uma consulta e descobre uma greve de 2013."
    co_dev "No Farol tudo faz sentido. No SGC tudo faz sentido para alguém que já saiu da empresa."
    show co_dev neutral at center_zoom
    co_dev "Patrimônio tombado. Hoje à noite eu te mando, pode esperar."
    hide co_dev
    with dissolve
    return

label im_corporativo_s2_conversar_co_qualidade:
    show co_qualidade neutral at center_zoom
    with dissolve
    "{i}[NOME_CO_QUALIDADE] passa a limpo, no tablet, o quadro de quatro colunas de ontem: funcional, não funcional, restrição, desejo.{/i}"
    co_qualidade "Foto de quadro branco some em duas semanas. Ninguém acha, ninguém lê. Por isso eu passo a limpo."
    "{i}Você repara que até o \"tema escuro com mascote\" está lá, na quarta coluna.{/i}"
    show co_qualidade thinking at center_zoom
    co_qualidade "Está. O que fica fora hoje volta na próxima rodada. Se estiver registrado, volta com nome e motivo. Se não, volta como briga."
    co_qualidade "Desejo também é registro. Só não tem data."
    show co_qualidade neutral at center_zoom
    "{i}Ela gira o pulso para ajeitar a caneta, e aparece a tatuagem pequena de um sinal de check.{/i}"
    co_qualidade "Fiz em 2019, depois de uma sexta em que uma mudança pequena zerou o relatório da diretoria. Era para lembrar de conferir tudo."
    co_qualidade "Agora o pulso tem checklist e eu tenho fama de chata. Os dois itens estão marcados."
    hide co_qualidade
    with dissolve
    return


# -------------------------------
# Central de atendimento
# -------------------------------
label im_corporativo_s2_conversar_co_supervisora:
    show co_supervisora thinking at center_zoom
    with dissolve
    "{i}[NOME_CO_SUPERVISORA] está com o relatório de SLA do ano passado aberto em cima da mesa, cheio de marcas de caneta.{/i}"
    co_supervisora "[player_name], aquele número da quarta não saiu da minha cabeça. Fui puxar o ano passado."
    co_supervisora "Dezessete. Dezessete de cada cem ligações eram cobrança de andamento."
    co_supervisora "Dezoito este ano, dezessete no passado. Isso não é acaso, é rotina."
    show co_supervisora serious at center_zoom
    co_supervisora "Agora me diz uma coisa, com sinceridade: quanto tempo essa descrição vai custar por chamado?"
    "{i}Você responde que ainda não sabe, e que vai depender dos modelos prontos que ela pediu.{/i}"
    show co_supervisora neutral at center_zoom
    co_supervisora "Resposta honesta. Gosto mais disso do que de número inventado."
    co_supervisora "Quando tiver o modelo, eu cronometro com a minha equipe. Aí a gente conversa com número de verdade."
    hide co_supervisora
    with dissolve
    return

label im_corporativo_s2_observar_central:
    show co_supervisora neutral at right_zoom
    with dissolve
    co_supervisora "Troca de turno. Pior hora do dia para visita. Melhor hora para aprender."
    co_supervisora "Fica do meu lado. Hoje você observa a fila inteira, não um atendente só."
    "{i}O painel de TV mostra as barras subindo. O turno da tarde se despede, o da noite chega com café na mão, e as ligações não param para ninguém trocar de cadeira.{/i}"
    "{i}Na fileira da frente, uma atendente que está desde as oito atende o último chamado do turno: VPN de um técnico de campo, de novo.{/i}"
    "{i}Ela passa o procedimento de cor. Reinicia, reconecta, testa. O técnico agradece. Funcionou.{/i}"
    "{i}Agora é só fechar. Ela clica em Resolver. O SGC abre o campo Solução.{/i}"
    "{i}Ela olha o relógio. Digita três espaços. Clica em Salvar.{/i}"
    "{i}O SGC aceita sem reclamar e marca: Resolvido.{/i}"
    "{i}Você olha a tela de novo para ter certeza. O campo parece vazio, mas não está: tem três espaços que nenhum olho vê.{/i}"
    show co_supervisora thinking at right_zoom
    "{i}[NOME_CO_SUPERVISORA] também viu. Ela suspira, mas não levanta da cadeira.{/i}"
    co_supervisora "Fim de turno. É disso que eu falava. Ninguém aqui é preguiçoso; a fila é que não acaba."
    co_supervisora "Ela está aqui desde as oito. Se eu dou bronca agora, amanhã ela digita um ponto em vez de três espaços. Não muda nada."
    co_supervisora "O que muda é o tempo que leva para escrever. Se escrever custa um minuto no fim do turno, alguém vai pular."
    "{i}Você anota no caderno: campo obrigatório que aceita espaço é campo opcional com disfarce.{/i}"
    show co_supervisora serious at right_zoom
    co_supervisora "Uma coisa, [player_name]. O nome dela não vai para lugar nenhum. Nem caderno, nem documento, nem conversa na TI."
    co_supervisora "Eu deixei você ver porque confio que você entende a diferença entre o problema e a pessoa."
    "{i}Você mostra a página: só o que aconteceu, sem nome, com a hora aproximada.{/i}"
    show co_supervisora neutral at right_zoom
    co_supervisora "Isso. É assim que a gente trata incidente aqui também."
    if energia_cansaco():
        "{i}O barulho da troca de turno ainda ecoa quando você chega ao elevador. Hoje a central cansou você também.{/i}"
    else:
        "{i}No elevador, você pensa na descrição obrigatória que a [NOME_CO_SUPERVISORA] aceitou na quarta. Obrigatória, sim. Mas e se a descrição for só espaço?{/i}"
    hide co_supervisora
    with dissolve
    return


# -------------------------------
# Café do térreo
# -------------------------------
label im_corporativo_s2_conversar_co_solicitante:
    show co_solicitante neutral at center_zoom
    with dissolve
    "{i}[NOME_CO_SOLICITANTE] está no balcão do café, de colete refletivo, com um notebook embaixo do braço e um pão de queijo na outra mão.{/i}"
    co_solicitante "Fala! Vim deixar o notebook do Wellington na TI. De novo. Aproveitei o café, que o da subestação é um crime."
    show co_solicitante thinking at center_zoom
    co_solicitante "Semana dura. Choveu na Baixada e uma subestação alagou. Passei a terça inteira com água na canela."
    co_solicitante "E o técnico lá, sem conseguir abrir ordem de serviço, porque a VPN caiu de novo. Dessa vez eu não liguei. Vim pessoalmente."
    show co_solicitante neutral at center_zoom
    co_solicitante "E aí, quando eu vejo uma tela de verdade? Desenho no quadro eu entendo pouco."
    "{i}Você conta que o [NOME_CO_DEV] tem um protótipo e que ainda estão escrevendo o que ele precisa fazer.{/i}"
    co_solicitante "Se for para testar, me chama. Se for para imaginar, chama a diretoria."
    "{i}Ele ri, termina o pão de queijo em duas mordidas e vai para o elevador com o notebook do Wellington.{/i}"
    hide co_solicitante
    with dissolve
    return

label im_corporativo_s2_descansar_cafe:
    "{i}O café do térreo está mais calmo no fim da tarde. A máquina de expresso descansa, sem ninguém para dar tapa nela.{/i}"
    "{i}Você pega um café coado e senta perto da porta giratória. Lá fora, a luz do Centro fica laranja e as pessoas andam mais devagar: é sexta.{/i}"
    if energia_cansaco():
        "{i}Você quase cochila na banqueta. O atendente do café deixa um copo d'água do seu lado sem perguntar nada.{/i}"
    else:
        "{i}Ninguém fala de SLA por meia hora. Você nem percebe quando o café acaba.{/i}"
    return


# -------------------------------
# Refeitório
# -------------------------------
label im_corporativo_s2_conversar_co_mentora:
    show co_mentora neutral at center_zoom
    with dissolve
    "{i}[NOME_CO_MENTORA] está no refeitório quase vazio, com um pão de queijo e um chá. Ela empurra o prato para o meio da mesa.{/i}"
    co_mentora "Pega um. Lanche de sexta é sagrado."
    co_mentora "O que mais te surpreendeu esta semana?"
    "{i}Você fala da entrevista: o [NOME_CO_SOLICITANTE] contando a história do Wellington e a [NOME_CO_SUPERVISORA] descobrindo os dezoito por cento no próprio relatório.{/i}"
    show co_mentora thinking at center_zoom
    "{i}Ela escuta até o fim, sem corrigir nada, mexendo o chá.{/i}"
    co_mentora "Eu também me surpreendi. Fazia anos que ela não olhava o relatório por esse lado."
    co_mentora "Na segunda a gente pega aquele episódio e transforma numa frase. Uma frase que a equipe inteira leia igual."
    show co_mentora neutral at center_zoom
    co_mentora "Segunda a gente transforma conversa em especificação. Hoje, só come."
    hide co_mentora
    with dissolve
    return

label im_corporativo_s2_descansar_refeitorio:
    "{i}O refeitório tem o cheiro do último lanche da tarde. Uma funcionária da limpeza empilha cadeiras no fundo, cantarolando baixinho.{/i}"
    "{i}Você senta perto da janela com um chá de máquina. A baía está cor de cobre.{/i}"
    if energia_cansaco():
        "{i}Você deita a cabeça nos braços por dez minutos. Ninguém repara.{/i}"
    else:
        "{i}Você não abre o notebook. Só acompanha os barcos voltando antes de escurecer.{/i}"
    return


# -------------------------------
# Parque do Aterro (descansar, S2+)
# -------------------------------
label im_corporativo_s2_descansar_aterro:
    "{i}Quinze minutos a pé e a torre fica para trás. O Aterro abre em gramado, árvores largas e o calçadão à beira da baía.{/i}"
    "{i}Gente correndo, uma criança aprendendo a andar de bicicleta, um senhor pescando sem pressa nenhuma de pegar peixe.{/i}"
    if energia_cansaco():
        "{i}Você senta num banco à sombra e fecha os olhos. O vento da baía faz o trabalho que o café não fez.{/i}"
    else:
        "{i}Você anda até a água. O Pão de Açúcar está ali, meio enevoado, e por uma hora nenhum chamado parece urgente.{/i}"
    return


# -------------------------------
# Sala do arquivo
# -------------------------------
label im_corporativo_s2_conversar_co_legado:
    show co_legado neutral at center_zoom
    with dissolve
    "{i}[NOME_CO_LEGADO] guarda caixas com a calma de quem já fez isso mil vezes. A caneca de 2008 está em cima de uma pilha de fichários.{/i}"
    co_legado "Ainda pensando na figueira, [player_name]? Eu também. O [NOME_CO_DEV] me deixou com isso na cabeça."
    show co_legado thinking at center_zoom
    co_legado "Eu vi a reescrita de 2016 morrer. Não morreu de tecnologia ruim. Morreu de regra que ninguém escreveu."
    co_legado "Toda semana alguém achava uma. Feriado no código, rotina de madrugada, campo que guardava duas coisas. Cada uma custava um mês."
    co_legado "No fim, a equipe nova tinha medo de apagar qualquer linha. E com razão."
    show co_legado neutral at center_zoom
    co_legado "Por isso hoje eu fico feliz quando alguém pergunta antes de apagar. Como vocês fizeram com a rotina das 72 h."
    co_legado "Regra estranha quase sempre foi um incêndio. Pergunta antes de apagar o fogo velho."
    hide co_legado
    with dissolve
    return

label im_corporativo_s2_estudar_arquivo:
    "{i}Numa pasta de capa dura, entre fichários de 2010, você acha uma folha A3 dobrada em quatro: um mapa do banco do SGC, desenhado à mão.{/i}"
    "{i}A letra é do [NOME_CO_LEGADO]. Caixas para as tabelas, setas a caneta azul, e no canto uma lista com o título \"gatilhos\", cada um com uma data.{/i}"
    "{i}Gatilho é código que roda sozinho dentro do banco quando um dado muda. Ninguém clica, e mesmo assim alguma coisa acontece.{/i}"
    "{i}Você compara com o que vocês acharam no banco na segunda. Metade da lista bate. A outra metade já não existe, ou mudou de nome.{/i}"
    "{i}Embaixo da lista, com outra caneta, a mesma letra acrescentou depois: \"TRG_FECHA_SENHA_72H - job das 2h - 2013\". O mapa continuou crescendo depois de pronto.{/i}"
    "{i}O nome começa com TRG, de gatilho, mas ela roda por horário, numa rotina agendada. Mais uma coisa que o nome não conta.{/i}"
    if energia_cansaco():
        "{i}As letras pequenas começam a dançar. Você para, respira e termina devagar.{/i}"
    "{i}O mapa é de 2010 e já está velho. Mesmo assim, ele diz onde procurar. Você anota no notebook um jeito de ler um banco sem documentação.{/i}"
    return
