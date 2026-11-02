# s08.rpy
# Tempo livre da rota Corporativo, semana 8 (sexta, 18h às 21h), entre o
# ponto de parada da semana 7 e a co_18. A janela começa às 23h30.
# Roteiro: docs/design/intermissoes-corporativo.md, seção 2.9.
# Sem registro extra nesta semana. Refeitório e sala de servidores fechados.
# O motor (logic/intermissao.rpy) põe o fundo (a baia à noite), cobra tempo
# e energia e aplica a recompensa depois do label; aqui ficam só as falas.
# Ninguém discute o que fazer se o critério de parada estourar: isso é a
# decisão da co_18.

label im_corporativo_abertura_8:
    $ im_mostrar_local({"poi": im_local})
    with dissolve
    "{i}Sexta, seis da tarde. O andar esvazia, as luzes do corredor vão apagando, e a baia do Farol continua acesa.{/i}"
    "{i}Até as nove, o tempo é seu. Às onze e meia, a janela.{/i}"
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

label im_corporativo_s8_conversar_co_dev:
    show co_dev neutral at center_zoom
    with dissolve
    "{i}[NOME_CO_DEV] tem o celular numa mão e o script da carga aberto na outra tela.{/i}"
    co_dev "Duas grandes. Meia calabresa, meia marguerita. E uma de frango com catupiry para o [NOME_CO_LEGADO], que finge que não gosta."
    co_dev "Chega às onze. Fria à meia-noite. Tradição de sala de guerra, segundo a [NOME_CO_QUALIDADE]."
    "{i}Ele desliga e volta para o script. Você reconhece a tela: é a mesma de ontem, e a de anteontem.{/i}"
    show co_dev thinking at center_zoom
    co_dev "Quinta vez. Eu sei. Cada vez eu acho uma vírgula que podia estar em outro lugar, e não mudo nada."
    co_dev "O ensaio passou. A reversão está testada. O roteiro está impresso."
    co_dev "Bora... Bora. Falei duas vezes para ver se acredito."
    show co_dev neutral at center_zoom
    if energia_cansaco():
        co_dev "Você tá com cara de quem precisa de um cochilo antes. Tem um sofá na sala ao lado. Eu acordo você quando a pizza chegar."
    else:
        co_dev "Fica aí um pouco? Ler o script com alguém do lado é diferente. Parece menos script e mais plano."
    hide co_dev
    with dissolve
    return

label im_corporativo_s8_conversar_co_qualidade:
    show co_qualidade neutral at center_zoom
    with dissolve
    "{i}A impressora do andar trabalha sem parar. [NOME_CO_QUALIDADE] tira as folhas ainda quentes e grampeia cada cópia com um estalo.{/i}"
    co_qualidade "Seis passos. Uma cópia para cada pessoa. A sua está aqui, com seu nome em cima."
    co_qualidade "Lê comigo o critério de parada da carga. Em voz alta, do jeito que está na RFC."
    "{i}Você lê em voz alta: \"Critério de parada do passo quatro: zero registro corrompido.\"{/i}"
    co_qualidade "Isso. Nem uma palavra a mais, nem uma a menos."
    "{i}Você começa a perguntar o que acontece se não der zero. Ela levanta a mão, sem pressa.{/i}"
    co_qualidade "Hoje à noite ninguém inventa nada. A gente lê, executa e registra."
    co_qualidade "Guarda a pergunta para a hora em que ela for necessária. Se ninguém precisar dela, melhor ainda."
    show co_qualidade thinking at center_zoom
    co_qualidade "Agora me ajuda a grampear o resto. Cinco cópias. Seis, com a da [NOME_CO_SUPERVISORA], que vai acompanhar por telefone."
    "{i}Vocês grampeiam em silêncio. Cada estalo parece um visto.{/i}"
    if energia_cansaco():
        show co_qualidade neutral at center_zoom
        co_qualidade "E hoje você lê o roteiro, não digita. Quem está com sono confere. Quem dormiu executa."
    hide co_qualidade
    with dissolve
    return

# ---------------- Central de atendimento ----------------

label im_corporativo_s8_observar_central:
    "{i}Noite no terceiro andar. Metade das luzes está apagada. O turno da noite tem doze pessoas e um painel de fila que quase ninguém olha.{/i}"
    "{i}Você senta numa baia vazia e observa uma hora de atendimento: VPN de quem trabalha de casa, uma impressora, duas senhas.{/i}"
    "{i}Na baia da janela, um atendente pergunta baixinho para a colega: \"Esse Farol começa hoje mesmo?\"{/i}"
    "{i}Ninguém aqui viu os modelos de descrição. O treinamento da noite seria por vídeo, no começo do turno. A VPN caiu duas vezes no fim da tarde, e a [NOME_CO_SUPERVISORA] desmarcou a sessão.{/i}"
    "{i}Um supervisor da noite, de colete e caneca térmica, para do seu lado. Ele não sabe seu nome, mas reconhece o crachá.{/i}"
    "Supervisor da noite" "Você é da equipe do Farol, né?"
    "Supervisor da noite" "Esse Farol muda o quê para a gente?"
    "{i}Você pensa em tudo que poderia dizer: camada, trilha, CAB. Escolhe duas frases.{/i}"
    "{i}\"Para resolver um chamado, o Farol pede uma descrição do que foi feito, e tem modelo pronto para os casos comuns. E quem abriu o chamado consegue ver isso sozinho, sem ligar para cá.\"{/i}"
    "Supervisor da noite" "Então é menos gente ligando para perguntar do chamado."
    "Supervisor da noite" "E uns segundos a mais para mim na hora de fechar. Justo."
    "Supervisor da noite" "Só que ninguém aqui viu esses modelos. Às quatro da manhã, quem cai na tela nova é a gente."
    "{i}Ele não está bravo. Está cansado de ser o último a saber.{/i}"
    "Supervisor da noite" "Na segunda, quando vocês sentarem com a [NOME_CO_SUPERVISORA], fala da noite. A gente também atende."
    "{i}Você anota, sem nome: \"Turno da noite sem treinamento: sessão cancelada pela VPN. Pedem um treino curto, no horário deles.\"{/i}"
    "{i}Quando você levanta, ele já está mostrando a uma atendente onde fica o botão de modelo, na tela de homologação.{/i}"
    return

# ---------------- Café do térreo ----------------

label im_corporativo_s8_conversar_co_mentora:
    show co_mentora neutral at center_zoom
    with dissolve
    "{i}O café do térreo está quase fechando. [NOME_CO_MENTORA] pede dois sanduíches e empurra um para você antes de qualquer pergunta.{/i}"
    co_mentora "Come agora. Às duas da manhã, ninguém pensa direito com fome."
    co_mentora "E se der, cochila. Sofá da sala de reunião, uma hora. Alarme no celular, não na boa vontade."
    co_mentora "Vamos por partes, inclusive o jantar."
    show co_mentora thinking at center_zoom
    co_mentora "Uma coisa que eu levei anos para entender."
    co_mentora "Em janela, a pessoa mais útil não é a que digita mais rápido. É a que lê o roteiro com calma."
    co_mentora "Quem digita olha para o terminal. Quem lê olha para o plano. As duas precisam estar na sala."
    co_mentora "Se alguém pular uma linha hoje, quero que você seja quem diz: espera, o passo é este."
    show co_mentora neutral at center_zoom
    if energia_cansaco():
        co_mentora "Principalmente hoje. Com a semana que você teve, ler com calma é o melhor que dá para fazer. E é muito."
    else:
        co_mentora "Agora termina o sanduíche. O resto, às onze e meia."
    hide co_mentora
    with dissolve
    return

label im_corporativo_s8_descansar_cafe:
    "{i}O café do térreo está fechando. O atendente vira as banquetas, mas deixa a sua no chão.{/i}"
    "{i}Pela porta giratória, o Centro troca o paletó pelo bar da esquina. Ninguém aqui sabe que hoje tem janela.{/i}"
    if energia_cansaco():
        "{i}Você encosta a cabeça na parede e cochila de verdade. Quando abre os olhos, tem um pão de queijo embrulhado ao lado da xícara.{/i}"
    else:
        "{i}Você toma um descafeinado, porque a noite vai ser longa, e deixa a cabeça vazia até o fim da xícara.{/i}"
    return

# ---------------- Sala do arquivo ----------------

label im_corporativo_s8_conversar_co_legado:
    show co_legado neutral at center_zoom
    with dissolve
    "{i}[NOME_CO_LEGADO] está no arquivo com um casaco no encosto da cadeira. Trouxe de casa: diz que a sala de servidores à noite é o lugar mais frio do Rio.{/i}"
    co_legado "A última janela antes de março. Já fiz mais de cem. Essa eu quero lembrar direito."
    if mentoria_conq_corporativo:
        "{i}Ele aponta a estante. Preso com fita crepe entre dois fichários de 2009, está o mapa dos causos que vocês imprimiram. Embaixo, a assinatura dele.{/i}"
        co_legado "Pus aqui, onde o próximo curioso vai procurar primeiro. O wiki é para quem já sabe o que procura. A estante é para quem chega."
        co_legado "Cada causo tem uma segunda pessoa. Se eu sumir amanhã, o SGC ainda tem com quem conversar."
    elif mentoria_feitos() > 0:
        co_legado "Nossos causos ainda estão pela metade. Não tem problema. Até março dá tempo."
        co_legado "Eu trago o café, você traz o caderno."
    else:
        co_legado "Tenho uma pilha de causo que ninguém pediu ainda. Até março dá tempo, se você quiser ouvir."
        co_legado "Isso aí tem história. Muita. E quase nada está em papel."
    show co_legado thinking at center_zoom
    co_legado "Hoje a Tia Neide fica de plantão comigo. Ela não sabe que é a última vez."
    co_legado "Última janela com crachá. A próxima eu acompanho de casa, de pijama."
    hide co_legado
    with dissolve
    return

# ---------------- Parque do Aterro ----------------

label im_corporativo_s8_descansar_aterro:
    "{i}Quinze minutos a pé até o Aterro. À noite, os postes acendem o caminho de pedras, e a baía vira um espelho escuro com as luzes de Niterói do outro lado.{/i}"
    if energia_cansaco():
        "{i}Você senta num banco perto da água e fecha os olhos. O barulho das ondas pequenas faz o que o café não conseguiu.{/i}"
    else:
        "{i}Você anda até o fim do calçadão e volta, sem pressa. A torre de vidro aparece acesa lá atrás, um andar só: o seu.{/i}"
    return
