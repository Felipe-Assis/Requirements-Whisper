# s07.rpy
# Tempo livre da rota Corporativo, semana 7 (quinta, 14h às 17h), chamado no
# fim da co_17, depois do CAB aprovado. Amanhã à noite é a janela.
# Roteiro: docs/design/intermissoes-corporativo.md, seção 2.8.
# O motor (logic/intermissao.rpy) põe o fundo, cobra tempo e energia e dá a
# recompensa (inclusive a pista co_p_parada do "ajudar" e o extra
# co_extra_parada do "estudar") depois do label; aqui ficam só as falas.
# As falas não respondem à decisão da janela (co_18): só mostram os tempos.
# A mentoria com o Jorge fica em mentoria.rpy. Descansar tem label por semana.

label im_corporativo_abertura_7:
    $ im_mostrar_local({"poi": im_local})
    with dissolve
    "{i}Quinta, duas da tarde. A RFC aprovada está presa no quadro da baia, com um visto vermelho no canto.{/i}"
    "{i}Tem novidade no mapa: a sala de servidores, no subsolo, abriu para os ensaios. A [NOME_CO_QUALIDADE] desceu para lá depois do almoço.{/i}"
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

label im_corporativo_s7_conversar_co_dev:
    show co_dev neutral at center_zoom
    with dissolve
    "{i}[NOME_CO_DEV] tem dois gráficos abertos e o fone no pescoço. Numa das telas, uma curva sobe e fica reta.{/i}"
    co_dev "Teste de carga de madrugada. Mil e quinhentos usuários, igual ao pico das nove."
    co_dev "2,4 segundos no percentil 95. Passou com folga."
    "{i}Ele não parece aliviado. Rola a tela até o script da carga do histórico e fica olhando.{/i}"
    show co_dev serious at center_zoom
    co_dev "Esse aqui é meu. Duzentas mil descrições. Se der ruim no sábado, é o meu nome no histórico do arquivo."
    co_dev "Passou no teste e mesmo assim eu sonhei com acento quebrado."
    show co_dev neutral at center_zoom
    if co_senha_relato == "historia":
        co_dev "Pelo menos a senha de 2012 virou história com começo, meio e fim. O [NOME_CO_LEGADO] contando foi melhor que qualquer log."
    elif co_senha_relato == "grupo":
        co_dev "E depois da senha de 2012 eu leio cada linha do repositório com lupa. Ainda bem que a [NOME_CO_QUALIDADE] segurou aquele post a tempo."
    else:
        co_dev "Pelo menos a senha de 2012 já está no cofre. Um pesadelo a menos."
    if energia_cansaco():
        co_dev "Você também está com cara de quem sonhou com script. Bora os dois dormir cedo hoje?"
    else:
        co_dev "Vou rodar mais uma vez à noite. Não porque precise. Porque eu durmo melhor."
    hide co_dev
    with dissolve
    return

# ---------------- Central de atendimento ----------------

label im_corporativo_s7_conversar_co_supervisora:
    show co_supervisora neutral at center_zoom
    with dissolve
    "{i}[NOME_CO_SUPERVISORA] está de pé ao lado do painel de filas, com uma planilha impressa cheia de setas.{/i}"
    co_supervisora "Treinamento amanhã. Quinze minutos por turno, como a [NOME_CO_QUALIDADE] registrou."
    co_supervisora "Manhã eu faço às oito, antes do pico. Tarde, às duas, quando a fila respira."
    co_supervisora "Manhã e tarde eu garanto. A noite é a minha dor de cabeça."
    "{i}Ela aponta a última linha da planilha. Turno da noite: em branco.{/i}"
    show co_supervisora thinking at center_zoom
    co_supervisora "São doze atendentes. Entram às seis, e às seis eu estou presa no trânsito da Presidente Vargas."
    co_supervisora "Se eles pegarem o Farol sem ter visto, quem atende é a confusão. E quem leva a culpa é a ferramenta."
    co_supervisora "Vou tentar uma sessão por vídeo amanhã, às seis e meia. Se a VPN deixar."
    co_supervisora "Anota aí, [player_name]: se a noite ficar sem treino, eu vou falar disso na reunião de segunda."
    if energia_cansaco():
        co_supervisora "E vai para casa cedo hoje. Gente com sono erra tecla. Na central e na TI."
    hide co_supervisora
    with dissolve
    return

label im_corporativo_s7_observar_central:
    "{i}Meio da tarde na central. A fila está baixa, e metade das cadeiras gira para o lado da janela na pausa.{/i}"
    "{i}Neusa não gira. Ela abriu a homologação do Farol numa aba e treina sozinha, chamado por chamado.{/i}"
    "{i}Você puxa uma cadeira ao lado, como da primeira vez, e observa sem interromper.{/i}"
    "Neusa" "Não é para o treinamento de amanhã. É para eu não passar vergonha na frente do Paulo."
    "{i}Ela escolhe o modelo de Reset de senha, troca duas palavras e resolve. Depois o de VPN. Depois o de notebook.{/i}"
    "Neusa" "Esses três estão lindos. Vinte segundos cada, no máximo."
    "{i}Ela abre a fila real em outra aba e conta os chamados de hoje com a ponta da caneta.{/i}"
    "Neusa" "Senha, VPN, notebook. E a impressora, que é metade da minha fila de sexta?"
    "{i}Você olha a lista de modelos do Farol. Não tem impressora.{/i}"
    "Neusa" "Sexta à tarde todo mundo quer imprimir relatório. A do quarto andar trava, a do sexto come papel."
    "Neusa" "Eu escrevo 'impressora reiniciada' umas vinte vezes. Com modelo, era um clique e duas palavras."
    "{i}Você anota no caderno, sem nome: \"Modelo de descrição para impressora. Pedido da central. Pico na sexta à tarde.\"{/i}"
    "Neusa" "E acesso a sistema de campo. Esse o pessoal do [NOME_CO_SOLICITANTE] pede toda segunda de manhã."
    "{i}Mais uma linha no caderno. Ela espia e aprova com a cabeça.{/i}"
    show co_supervisora neutral at right_zoom
    with dissolve
    co_supervisora "Neusa, você está na pausa."
    "Neusa" "Estou na pausa treinando, chefe. É diferente."
    co_supervisora "[player_name], leva essa lista para a reunião de segunda. Do jeito que ela falou, sem enfeite."
    hide co_supervisora
    with dissolve
    "{i}A pausa acaba. Neusa fecha a homologação, ajusta o headset e atende a próxima ligação antes do segundo toque.{/i}"
    return

# ---------------- Café do térreo ----------------

label im_corporativo_s7_conversar_co_mentora:
    show co_mentora neutral at center_zoom
    with dissolve
    "{i}[NOME_CO_MENTORA] está no balcão do café com um pão de queijo e o tablet fechado. É a primeira vez na semana que ela não está digitando.{/i}"
    co_mentora "CAB aprovado. Senta. Hoje eu me dou dez minutos de comemoração."
    co_mentora "Sabe a minha primeira janela? 2011. Troca de versão do banco do SGC."
    co_mentora "Começamos à meia-noite. Às três, deu erro. Ninguém tinha combinado quando parar."
    co_mentora "Então ninguém parou. Fomos tentando. Às sete da manhã a central chegou, e a gente ainda estava lá."
    show co_mentora thinking at center_zoom
    co_mentora "Em 2011 a gente não tinha plano de volta. Tinha café e fé. Não recomendo."
    co_mentora "Deu certo no fim. Mas ninguém lembra direito como. Isso me incomoda até hoje."
    co_mentora "Por isso eu sou chata com roteiro e a [NOME_CO_QUALIDADE] é chata com registro. Juntas, a equipe dorme."
    show co_mentora neutral at center_zoom
    if energia_cansaco():
        co_mentora "E você está com cara de quem não dormiu a semana inteira. Hoje, casa cedo. Amanhã eu quero você aqui com sono em dia."
    else:
        co_mentora "Um pedido: amanhã, chega com sono em dia. Janela pede cabeça descansada, não coragem."
    hide co_mentora
    with dissolve
    return

label im_corporativo_s7_descansar_cafe:
    "{i}Quinta à tarde, o café do térreo está quase vazio. Você pega um coado e senta na banqueta perto da porta giratória.{/i}"
    "{i}Lá fora, o Centro passa apressado. Aqui dentro, ninguém fala de RFC.{/i}"
    if energia_cansaco():
        "{i}Você fecha os olhos por um instante e quase escorrega da banqueta. O atendente deixa um copo d'água ao lado da xícara, sem perguntar nada.{/i}"
    else:
        "{i}Você termina o café devagar e, pela primeira vez na semana, não pensa no sábado.{/i}"
    return

# ---------------- Refeitório ----------------

label im_corporativo_s7_conversar_co_solicitante:
    show co_solicitante neutral at center_zoom
    with dissolve
    if co_negociacao_opcao == "investigar_agora":
        "{i}[NOME_CO_SOLICITANTE] está no refeitório com a botina ainda suja de barro e um café de máquina. Veio para a conversa do piloto da equipe dele.{/i}"
        co_solicitante "Fala! Acabei de sair da reunião do piloto. Meus técnicos vão ser os primeiros a usar o Farol no sábado."
        co_solicitante "Já avisei o pessoal: achou problema, abre chamado. Nada de me ligar. Quero ver o sistema funcionando."
    else:
        "{i}[NOME_CO_SOLICITANTE] está no refeitório de camisa social e botina, uma combinação que só ele usa. Veio a uma reunião na diretoria.{/i}"
        co_solicitante "Fala! Reunião na diretoria. Me chamaram para contar o caso do Wellington de novo."
        co_solicitante "Contei. Agora todo diretor sabe o nome do Wellington. Ele vai ficar famoso."
    co_solicitante "Por falar nele: o notebook ainda falha de vez em quando. Ontem perdeu a VPN duas vezes."
    co_solicitante "O chamado está Resolvido, com a solução escrita. Mas o notebook não leu a solução."
    show co_solicitante thinking at center_zoom
    co_solicitante "O notebook do Wellington tem personalidade. Se voltar a dar problema, eu vou querer reabrir."
    co_solicitante "Com o Farol dá, né? Reabrir com motivo, sem ligar para ninguém."
    "{i}Você confirma: dá para reabrir com o motivo escrito, e a solução anterior fica guardada no histórico.{/i}"
    show co_solicitante neutral at center_zoom
    co_solicitante "Então pode deixar. Se ele aprontar, eu testo isso na rua. Valeu."
    hide co_solicitante
    with dissolve
    return

label im_corporativo_s7_descansar_refeitorio:
    "{i}Depois das duas, o refeitório esvazia. Sobram as bandejas empilhadas e a baía inteira na janela.{/i}"
    "{i}Você pega um chá de máquina e escolhe a mesa mais longe do balcão.{/i}"
    if energia_cansaco():
        "{i}Você deita a cabeça nos braços por dez minutos. Ninguém repara, e o chá esfria sem pressa.{/i}"
    else:
        "{i}Você não abre o notebook. Um barco atravessa a baía devagar, e você acompanha até ele sumir atrás do morro.{/i}"
    return

# ---------------- Sala do arquivo ----------------

label im_corporativo_s7_conversar_co_legado:
    show co_legado neutral at center_zoom
    with dissolve
    "{i}[NOME_CO_LEGADO] está na mesa do arquivo, cercado de fichários, com a caneca de 2008 longe dos papéis.{/i}"
    if co_senha_relato == "historia":
        co_legado "Senta, [player_name]. Antes de tudo: obrigado por me perguntar antes de registrar."
        co_legado "Era minha. 'Só até segunda.' A segunda durou doze anos."
        co_legado "Como você perguntou, eu pude contar o porquê. Integração com o RH, entrega numa sexta, pressa."
        co_legado "Registro sem porquê vira caça ao culpado. Com o porquê, vira lição."
    else:
        co_legado "Senta, [player_name]. Tenho uma confissão sobre a senha de 2012."
        co_legado "Era minha. 'Só até segunda.' A segunda durou doze anos."
        co_legado "Integração com o RH, entrega numa sexta, pressa. A desculpa de sempre."
        co_legado "Li o registro da [NOME_CO_QUALIDADE]. O que aconteceu, desde quando, o que foi feito. Nenhum nome."
        co_legado "Gostei. Se tivesse meu nome, eu ia me defender. Sem nome, eu fui ajudar."
    show co_legado thinking at center_zoom
    co_legado "Provisório, aqui no Grupo Vértice, é uma unidade de tempo. Vai de três dias a dezesseis anos."
    co_legado "Agora a senha mora no cofre. A Tia Neide nunca teve cofre. Ela tinha um post-it."
    hide co_legado
    with dissolve
    return

label im_corporativo_s7_estudar_arquivo:
    "{i}Na sala do arquivo, você abre o roteiro aprovado no CAB. Seis passos, cada um com dono e horário.{/i}"
    "{i}Ao lado de cada passo, você escreve duas perguntas: o que faria voltar? E quem decide?{/i}"
    "{i}Passo um, backup verificado. Volta se a restauração de teste não bater. Quem decide: [NOME_CO_LEGADO].{/i}"
    "{i}Passos dois e três, Farol desligado, camada e regra. Volta se a leitura em produção falhar. Quem decide: [NOME_CO_DEV], com a [NOME_CO_QUALIDADE].{/i}"
    "{i}Passo quatro, carga do histórico. A RFC já diz: zero registro corrompido. Quem decide: a [NOME_CO_QUALIDADE], dona do roteiro.{/i}"
    "{i}Passos cinco e seis, testes de fumaça e liberação. Volta se um teste de fumaça falhar. Quem decide: a [NOME_CO_MENTORA].{/i}"
    "{i}Duas coisas o roteiro ainda não diz em minutos: até que horas dá para tentar e quanto tempo leva cada volta.{/i}"
    "{i}Você marca as duas com um ponto de interrogação. Um critério sem hora limite e sem custo de volta fica pela metade.{/i}"
    return

# ---------------- Sala de servidores ----------------

label im_corporativo_s7_conversar_co_qualidade:
    show co_qualidade neutral at center_zoom
    with dissolve
    "{i}Na sala de servidores, o ar é frio e o zumbido não para. [NOME_CO_QUALIDADE] está numa mesa dobrável, com o notebook aberto no agendamento do backup.{/i}"
    co_qualidade "Oi. Estou só conferindo."
    "{i}Na tela, o agendamento tem três marcas de visto. As três de hoje.{/i}"
    co_qualidade "Tá bom. Terceira vez. Mas a terceira é a que conta."
    co_qualidade "Backup às dez da noite de sexta. À meia-noite, a gente confere a cópia antes de qualquer outra coisa."
    show co_qualidade thinking at center_zoom
    co_qualidade "Eu disse para descansar. Eu disse para vocês, não para mim."
    co_qualidade "Daqui a pouco eu subo. Prometo. Está registrado, e você é testemunha."
    "{i}No canto, o rack bege da Tia Neide pisca devagar, como se também estivesse conferindo.{/i}"
    if energia_cansaco():
        show co_qualidade neutral at center_zoom
        co_qualidade "E você nem pensa em ficar aqui comigo. Com essa cara, quem precisa de backup é você."
    hide co_qualidade
    with dissolve
    return

label im_corporativo_s7_ajudar_co_qualidade:
    show co_qualidade neutral at center_zoom
    with dissolve
    "{i}[NOME_CO_QUALIDADE] puxa uma segunda cadeira para a mesa dobrável e vira o notebook para você.{/i}"
    co_qualidade "Quer ajudar no último ensaio? É o ensaio da volta."
    co_qualidade "Duas semanas atrás, a gente ensaiou a ida da carga. Ninguém ensaiou voltar. E eu não confio em plano que só foi lido."
    co_qualidade "Cópia de produção, aqui no subsolo. Já está como estaria às duas da manhã de sábado, com os quatro primeiros passos aplicados."
    co_qualidade "Duas voltas possíveis. Você cronometra, eu executo."
    "{i}Ela entrega o celular com o cronômetro aberto. No notebook, o roteiro da janela, passo a passo.{/i}"
    co_qualidade "Primeira volta: desfazer a janela inteira. Restaurar tudo pelo backup, como se nada tivesse acontecido. Pode soltar."
    "{i}A barra de restauração anda devagar. O ar-condicionado zumbe. [NOME_CO_QUALIDADE] lê cada mensagem do log e marca um visto no papel.{/i}"
    "{i}Vinte minutos. Ela levanta para pegar água. Trinta. Você confere se o cronômetro não travou.{/i}"
    "{i}Quarenta minutos. O banco volta inteiro, e a consulta de teste responde.{/i}"
    show co_qualidade thinking at center_zoom
    co_qualidade "Quarenta. Numa janela de quatro horas, isso é um sexto da noite."
    co_qualidade "Segunda volta: só a carga do histórico. O script de reversão do passo quatro, que o [NOME_CO_DEV] escreveu junto com a carga."
    co_qualidade "Antes, eu rodo a carga de novo na cópia, para ter o que desfazer."
    "{i}A carga roda. Depois, o script de reversão. Você aperta o cronômetro.{/i}"
    "{i}A tabela de histórico volta ao estado de antes. O resto continua no lugar: a camada, a regra, a tela de consulta.{/i}"
    "{i}Seis minutos.{/i}"
    co_qualidade "Seis. Sem tocar em mais nada."
    show co_qualidade neutral at center_zoom
    co_qualidade "Quarenta para voltar tudo, seis para voltar um passo. Agora a gente sabe quanto custa cada volta."
    "{i}Ela escreve os dois tempos à caneta, na margem do roteiro impresso: um ao lado do passo um, outro ao lado do passo quatro.{/i}"
    co_qualidade "[player_name], confere minha anotação. Número errado em roteiro é pior que número nenhum."
    "{i}Você compara com o cronômetro: quarenta minutos para a restauração completa, seis para a reversão da carga. Bate.{/i}"
    co_qualidade "Bateu. Registrado. Agora existe."
    if energia_cansaco():
        co_qualidade "E agora você sobe e vai para casa. Eu prometi que ia descansar, mas hoje quem cumpre primeiro é você."
    else:
        co_qualidade "Obrigada. Sozinha, eu ia cronometrar e executar ao mesmo tempo. E ia errar um dos dois."
    hide co_qualidade
    with dissolve
    return

# ---------------- Parque do Aterro ----------------

label im_corporativo_s7_descansar_aterro:
    "{i}Quinze minutos a pé e a torre fica para trás. Quinta à tarde, o Aterro tem pouca gente: um grupo de idosos na ginástica, um cachorro correndo atrás de pombo.{/i}"
    if energia_cansaco():
        "{i}Você senta na grama, na sombra de uma árvore de copa larga, e fecha os olhos. O vento da baía faz o que o café não conseguiu.{/i}"
    else:
        "{i}Você anda pelo calçadão até a água e fica olhando o Pão de Açúcar. Por uma hora, a janela de sábado é só uma palavra.{/i}"
    return
