# s06.rpy
# Tempo livre da rota Corporativo, semana 6 (sexta, 15h às 18h), chamado no
# fim da co_16. Na segunda vieram os testes de caracterização, o fuso do
# Norte e a revisão de pull request; na quarta, a consulta em homologação.
# Roteiro: docs/design/intermissoes-corporativo.md, seção 2.7.
# O motor (logic/intermissao.rpy) põe o fundo, cobra tempo e energia e dá a
# recompensa (pistas co_p_senha e co_p_botao dos "ajudar") depois do label.
# As duas ajudas mostram o que foi visto, sem dizer como agir na semana 7.
# Descansar tem label por semana (im_corporativo_s6_descansar_*).

label im_corporativo_abertura_6:
    $ im_mostrar_local({"poi": im_local})
    with dissolve
    "{i}Sexta, três da tarde. No quadro da equipe, a coluna Implementação está quase vazia. A próxima se chama Testes, e já tem cartão com o seu nome.{/i}"
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

label im_corporativo_s6_conversar_co_dev:
    "{i}[NOME_CO_DEV] está de fone, balançando a cabeça no ritmo de alguma coisa. Tira um lado quando vê você.{/i}"
    show co_dev neutral at center_zoom
    with dissolve
    co_dev "Bora, senta! Estou montando o teste de carga. Mil e quinhentos usuários de mentira acessando a consulta ao mesmo tempo."
    co_dev "Roda de madrugada, semana que vem. Se rodar no horário do expediente, a [NOME_CO_SUPERVISORA] me demite antes da [NOME_CO_QUALIDADE]."
    show co_dev thinking at center_zoom
    if co_ok_review:
        co_dev "E valeu de novo pela revisão de segunda. Eu tinha trancado a porta da frente e deixado a dos fundos aberta."
        co_dev "Se você não pega, a integração do SGC ia mandar chamado sem descrição direto para o Farol. Na frente do CAB."
    else:
        co_dev "Sobre segunda: a gente chegou lá junto, e foi isso que importou. Eu também não vi a API na primeira olhada."
        co_dev "Revisão é isso. Dois olhando, um pergunta, o outro descobre."
    show co_dev neutral at center_zoom
    co_dev "Agora toda regra nova eu escrevo duas vezes: na tela e no servidor. Com teste nas duas."
    co_dev "Botão desabilitado é só a porta da frente. Agora eu tranco as duas."
    hide co_dev
    with dissolve
    return

label im_corporativo_s6_ajudar_co_dev:
    "{i}[NOME_CO_DEV] puxa uma segunda cadeira para a mesa dele e vira um dos monitores para você.{/i}"
    show co_dev thinking at center_zoom
    with dissolve
    co_dev "Me ajuda numa coisa chata? A configuração da integração para os testes de segunda. Sozinho eu esqueço metade."
    co_dev "A credencial nova do Farol já está no cofre de segredos da homologação. Ninguém vê a senha. Nem eu."
    co_dev "Falta conferir se o build pega tudo do lugar certo. Você lê, eu explico."
    "{i}Vocês abrem o script de build da integração. Você lê em voz alta, linha por linha: compila, roda os testes, copia os arquivos, carrega a configuração do Farol.{/i}"
    "{i}Mais abaixo, uma linha carrega outro arquivo: config/sgc-integracao.properties. Do lado, um comentário antigo.{/i}"
    "{i}\"senha provisória - 2012\".{/i}"
    co_dev "Peraí. Lê de novo."
    "{i}Você lê de novo. [NOME_CO_DEV] tira os fones do pescoço e coloca na mesa.{/i}"
    co_dev "Esse arquivo é do usuário de serviço do SGC. Sempre esteve aí. Eu nunca abri. Nunca precisei."
    co_dev "Provisória de 2012. Provisória há mais tempo do que eu tenho de carteira assinada."
    "{i}A mão dele vai até o arquivo na árvore de pastas e para no meio do caminho.{/i}"
    "{i}Você sugere não abrir agora e registrar já: o que viram, onde está e quem precisa saber.{/i}"
    show co_dev neutral at center_zoom
    co_dev "É. Se eu abro, vira \"o [NOME_CO_DEV] viu a senha\". Se eu registro, vira trabalho da equipe."
    "{i}Ele abre um registro novo: \"Verificar segredo em arquivo da integração\". Escreve o caminho do arquivo, a linha do script e o comentário, sem copiar mais nada.{/i}"
    "{i}Marca para segunda de manhã, com a [NOME_CO_QUALIDADE]. Você confere o texto e acrescenta a hora em que viram.{/i}"
    co_dev "Não abre, não copia, não manda print. Segunda, com testemunha e com a [NOME_CO_QUALIDADE]."
    if energia_cansaco():
        co_dev "E vai descansar um pouco depois disso. Achado bom com sono vira print no grupo errado. Já vi acontecer."
    else:
        co_dev "Agora volta comigo para o resto do script. Se tinha um, pode ter dois."
    "{i}Vocês leem o resto até o fim. Nenhum outro comentário com senha. O registro fica aberto, com os dois nomes.{/i}"
    hide co_dev
    with dissolve
    return

label im_corporativo_s6_conversar_co_mentora:
    "{i}Na mesa ao lado da do [NOME_CO_DEV], [NOME_CO_MENTORA] cola um post-it novo no quadro: Testes, semana 7.{/i}"
    show co_mentora neutral at center_zoom
    with dissolve
    co_mentora "O [NOME_CO_LEGADO] me contou da revisão de segunda. Dois comentários, um causo e nenhuma nota. Ele revisa assim desde 2008."
    co_mentora "E você? Como foi estar do outro lado, recebendo?"
    "{i}Você conta que o comentário do nome do teste pareceu pequeno, até ouvir o motivo.{/i}"
    show co_mentora thinking at center_zoom
    co_mentora "Nome de teste é carta para alguém que você nunca vai conhecer. Ele sabe disso melhor que ninguém."
    co_mentora "Semana que vem a [NOME_CO_QUALIDADE] traz o plano de testes. Não vou dizer o que tem nele."
    co_mentora "Só uma dica: leva perguntas. Quem chega com pergunta sai com metade do trabalho feito."
    show co_mentora neutral at center_zoom
    co_mentora "Revisão boa é a que você agradece e corrige. Vale para quem recebe e para quem faz."
    hide co_mentora
    with dissolve
    return


# ---------------- Central de atendimento ----------------

label im_corporativo_s6_conversar_co_supervisora:
    "{i}[NOME_CO_SUPERVISORA] está de headset no pescoço, com uma folha impressa na mão. Ela mostra para você de longe.{/i}"
    show co_supervisora neutral at center_zoom
    with dissolve
    co_supervisora "Aprovados. Os três modelos. A equipe votou ontem, e a Neusa ganhou: ficou a versão dela."
    show co_supervisora thinking at center_zoom
    co_supervisora "Agora a minha pergunta. Quanto o Farol vai somar no meu TMA? E não me responde \"pouco\"."
    "{i}Você explica o que sabe: com modelo pronto, a descrição deve levar segundos, não minutos. O número de verdade vem do teste de aceitação.{/i}"
    co_supervisora "Semana passada a Neusa fez em vinte e poucos segundos. Vinte segundos eu aguento. Mas eu quero ver com a fila cheia, não com o andar vazio."
    show co_supervisora neutral at center_zoom
    co_supervisora "Seis e quarenta hoje. Se virar sete, eu quero saber por quê antes da diretoria."
    hide co_supervisora
    with dissolve
    return

label im_corporativo_s6_observar_central:
    "{i}Sexta à tarde. O painel da central está vermelho. Todas as barras com o mesmo assunto: VPN.{/i}"
    "{i}[NOME_CO_SUPERVISORA] passa por você sem parar e aponta uma cadeira atrás do Paulo.{/i}"
    show co_supervisora serious at right_zoom
    with dissolve
    co_supervisora "Senta aí e escuta. Hoje é dia de VPN caindo."
    "{i}O Paulo atende. Técnico de campo, sem VPN. Ele pede para reiniciar o notebook, conferir o cabo, tentar de novo. Conectou. Chamado resolvido.{/i}"
    "{i}Toca de novo. Outro técnico, mesma coisa. Mesmo roteiro. Conectou.{/i}"
    "{i}Na quarta ligação, o Paulo já fala o roteiro antes de a pessoa terminar de explicar.{/i}"
    co_supervisora "Paulo, quantos?"
    "{i}Ele mostra o post-it colado no monitor: onze risquinhos.{/i}"
    co_supervisora "Onze desde o almoço. Todo mundo voltou a funcionar. E ninguém sabe por que caiu."
    "{i}Você lembra da apostila de ITIL do arquivo. Cada ligação é um incidente: algo parou e precisa voltar agora.{/i}"
    "{i}As onze juntas apontam para outra coisa: uma causa só, que ninguém está procurando, porque todo mundo está ocupado fazendo voltar.{/i}"
    show co_supervisora thinking at right_zoom
    co_supervisora "Minha equipe faz voltar. Isso a gente sabe fazer de olho fechado."
    co_supervisora "Descobrir por que cai não é com a central. Eu abro o problema e mando para a infraestrutura, com os onze números."
    "{i}Ela digita rápido. No campo de descrição, cola a lista de chamados e escreve: \"VPN cai às sextas à tarde. Onze casos. Mesmo sintoma.\"{/i}"
    show co_supervisora neutral at right_zoom
    co_supervisora "Hoje é dia de apagar incêndio. Segunda alguém descobre quem acendeu."
    hide co_supervisora
    with dissolve
    "{i}Você anota no caderno: o incidente se resolve na hora; o problema precisa de dono e de dados. Os risquinhos do Paulo viraram os dados.{/i}"
    return


# ---------------- Café do térreo ----------------

label im_corporativo_s6_conversar_co_solicitante:
    "{i}No café do térreo, [NOME_CO_SOLICITANTE] toma um café em pé, com o capacete branco embaixo do braço.{/i}"
    show co_solicitante neutral at center_zoom
    with dissolve
    co_solicitante "Fala! Passei na diretoria e me disseram que o Farol já roda na homologação. Quero testar."
    "{i}Você explica que o teste de aceitação da semana que vem é com a central: são os atendentes que vão escrever as descrições.{/i}"
    show co_solicitante thinking at center_zoom
    if co_negociacao_opcao == "investigar_agora":
        co_solicitante "E o meu pessoal? O piloto entra na janela, né?"
        "{i}Você confirma: a equipe dele entra no piloto na janela da semana 8, junto com a central.{/i}"
        co_solicitante "Então eu separo o Wellington e mais dois. Gente que reclama com educação. É raro."
    else:
        co_solicitante "E o meu pessoal? Também vê a consulta depois da janela, né?"
        "{i}Você confirma: depois da janela, a consulta vale para todo mundo, campo incluído. O aviso por WhatsApp é que fica para a próxima rodada.{/i}"
        co_solicitante "Tá bom. Já aviso o Wellington. Mas sem ficar dando F5 no sábado de madrugada."
    show co_solicitante neutral at center_zoom
    co_solicitante "Sabe o que eu falo para eles? Que agora vai ter que ter descrição. E que isso é bom para nós."
    co_solicitante "Três linhas de solução valem mais que três ligações. Isso eu já ensinei lá no campo."
    hide co_solicitante
    with dissolve
    return


# ---------------- Sala do arquivo ----------------

label im_corporativo_s6_conversar_co_legado:
    "{i}Na sala do arquivo, [NOME_CO_LEGADO] tem o relatório das filiais do Norte aberto na mesa, de 2015. Alguém circulou um número a caneta, há muito tempo: 73 h.{/i}"
    show co_legado neutral at center_zoom
    with dissolve
    co_legado "Achei. A reclamação da supervisora de Manaus. Ela circulou o número e mandou por malote."
    co_legado "Dez anos todo mundo desconfiando. Bastou um teste com nome decente."
    show co_legado thinking at center_zoom
    co_legado "E por falar em nome decente. Trocou o nome do teste_fechamento_2?"
    menu (tipo="conversa"):
        "\"Troquei. Agora o nome diz o comportamento: resolver sem descrição mantém Em atendimento.\"":
            show co_legado neutral at center_zoom
            co_legado "Agora sim. Daqui a cinco anos, alguém vê isso falhar e sabe o que quebrou. Sem me ligar."
        "\"Ainda não. Faço segunda, antes de qualquer outra coisa.\"":
            co_legado "Faz. Teste com nome de número é bilhete sem remetente."
            co_legado "Segunda eu pergunto de novo. Sou velho, mas não esqueço."
    if "co_p_norte" in pistas_usadas:
        co_legado "Registro de problema aberto, teste fotografando o defeito e a reclamação de 2015 junto. Agora o fuso do Norte tem história e tem dono."
    else:
        co_legado "Registro de problema aberto e teste fotografando o defeito. Vou anexar esta folha de 2015 no registro. Aí o fuso do Norte tem história e tem dono."
    hide co_legado
    with dissolve
    return

label im_corporativo_s6_estudar_arquivo:
    "{i}Você leva para o arquivo a lista dos testes de segunda e senta na mesa do canto, longe da janela basculante.{/i}"
    "{i}Relê um por um. O de Reset de senha, que fotografou o defeito mais famoso do prédio. O do fuso, que falhou e virou registro.{/i}"
    "{i}Numa folha em branco, você escreve o roteiro como gostaria de ter recebido na segunda de manhã.{/i}"
    "{i}Um: escolher uma entrada real, de um chamado que existiu. Dois: rodar o código como está, sem mexer.{/i}"
    "{i}Três: copiar a saída para a verificação, mesmo que pareça errada. Quatro: dar ao teste o nome do comportamento, não um número.{/i}"
    "{i}Cinco: se o comportamento for um defeito, o teste continua igual, e um registro de problema guarda a correção para depois.{/i}"
    "{i}Você olha a lista e entende o que o [NOME_CO_LEGADO] quis dizer: primeiro uma rede, depois a mudança. Os testes não julgam o código. Só lembram como ele é.{/i}"
    return


# ---------------- Sala do CAB ----------------

label im_corporativo_s6_conversar_co_qualidade:
    "{i}Na sala do CAB, [NOME_CO_QUALIDADE] tem o plano de testes impresso, seis folhas grampeadas, e uma fileira de canetas coloridas na mesa.{/i}"
    show co_qualidade neutral at center_zoom
    with dissolve
    co_qualidade "Versão final. Seis blocos. Cada um com dono, data e evidência. Segunda eu apresento para a equipe."
    "{i}Enquanto fala, ela alinha as canetas pela cor. Depois desalinha e alinha de novo.{/i}"
    "{i}Você pergunta se ela está nervosa com o CAB da semana que vem.{/i}"
    show co_qualidade thinking at center_zoom
    co_qualidade "Nervosa? Eu devolvo RFC dos outros toda quinta. Sou a chata do CAB, lembra?"
    "{i}Ela alinha as canetas pela terceira vez.{/i}"
    co_qualidade "É que desta vez eu assino a RFC junto. Se eu devolvo a dos outros, tenho que aguentar a pergunta chata na minha."
    show co_qualidade neutral at center_zoom
    co_qualidade "Não estou nervosa. Estou preparada. É diferente. Registrado como ansiedade, prioridade baixa."
    hide co_qualidade
    with dissolve
    return

label im_corporativo_s6_ajudar_co_qualidade:
    "{i}[NOME_CO_QUALIDADE] fecha as persianas até a metade e aponta a cadeira da cabeceira para você.{/i}"
    show co_qualidade neutral at center_zoom
    with dissolve
    co_qualidade "Ensaio. Você é o CAB. Eu apresento a RFC do Farol, você me faz as perguntas que eu não quero ouvir."
    co_qualidade "Sem dó. Se o comitê achar um buraco que você não achou, eu volto aqui e te cobro."
    "{i}Ela apresenta: o que muda, o impacto, a janela de sábado, o ensaio da carga, o plano de volta. Leva doze minutos. Você anota três perguntas.{/i}"
    menu (tipo="conversa"):
        "Qual pergunta você faz primeiro?"
        "\"Quanto tempo leva para voltar, se der errado às 3h?\"":
            co_qualidade "Boa. Tem plano de volta, mas sem tempo medido. Vou cronometrar cada volta antes da janela e mostrar o número na tela."
        "\"Quem decide parar a carga, e até que horas dá para tentar?\"":
            co_qualidade "Boa. O critério está escrito, mas o nome de quem decide estava só na minha cabeça. Vou pôr no slide."
        "\"O que acontece com a central se o Farol travar no pico das nove?\"":
            co_qualidade "Boa. O Farol só lê. Se travar, a central segue no SGC. Mas eu tenho que dizer isso logo no começo, não no fim."
    show co_qualidade thinking at center_zoom
    co_qualidade "Agora a parte de perfis. Pergunta."
    "{i}Você pergunta como ela sabe que um atendente não consegue mexer em chamado de outro setor.{/i}"
    if not pista_tem("co_p_botao"):
        co_qualidade "Pergunta justa. Deixa eu mostrar o risco com o sistema de hoje, que é o exemplo mais honesto que eu tenho."
        "{i}Ela entra na homologação do SGC com um usuário de teste do perfil atendente e abre um chamado da equipe de campo. O botão Reabrir não aparece.{/i}"
        "{i}Depois abre um chamado da central, copia o endereço da ação do botão e troca só o número do chamado. Cola na barra do navegador.{/i}"
        "{i}A tela pisca. O chamado da equipe de campo aparece como Reaberto.{/i}"
        show co_qualidade serious at center_zoom
        co_qualidade "Interessante."
        "{i}Ela devolve o chamado ao estado de antes e anota a hora no tablet.{/i}"
        co_qualidade "Anota o que você viu, não o que você acha. O que achar fica para a semana de testes."
        "{i}Você escreve cinco linhas: perfil, chamado, botão, endereço, resultado. Ela copia para a pasta da RFC.{/i}"
    else:
        co_qualidade "Lembra do que a gente viu semana passada na homologação? Está anotado aqui, na seção de perfis. Palavra por palavra."
        "{i}Vocês leem juntos a seção. Ela mudou desde a semana passada: tem um parágrafo novo, com o que foi visto e a data.{/i}"
        co_qualidade "Por causa daquela tarde, a seção ganhou uma linha: os testes de perfil vão ser planejados com o que vimos no SGC aberto do lado."
        co_qualidade "Como planejar, a gente decide segunda. Hoje eu só não quero esquecer."
    show co_qualidade neutral at center_zoom
    co_qualidade "Mais uma. Pergunta de novo, mais chato. O CAB não vai ser mais gentil que você."
    "{i}Você pergunta o que acontece se o CAB disser não. Ela respira fundo.{/i}"
    co_qualidade "Aí a gente vai para a janela seguinte, com o motivo registrado. Perder a janela é ruim. Subir sem aprovação é pior."
    if energia_cansaco():
        co_qualidade "Chega por hoje. Você está fazendo pergunta de olho fechado. Obrigada, de verdade."
    else:
        co_qualidade "Obrigada. Três perguntas que eu não tinha previsto. Na quinta, quem perguntar vai achar resposta."
    hide co_qualidade
    with dissolve
    return


# ---------------- Descansar ----------------

label im_corporativo_s6_descansar_cafe:
    "{i}O café do térreo está calmo. Na vitrine da lojinha, as canecas de faixa azul acabaram: alguém comprou a última.{/i}"
    "{i}Você pede um coado e senta perto da porta giratória. Lá fora, o Centro começa a desacelerar para o fim de semana.{/i}"
    if energia_cansaco():
        "{i}Você apoia a cabeça na parede e cochila no banco alto. Quando acorda, o café está morno e alguém deixou um guardanapo dobrado do seu lado.{/i}"
    else:
        "{i}Por meia hora você não pensa em teste nem em senha. Só no barulho bom da xícara no pires.{/i}"
    return

label im_corporativo_s6_descansar_refeitorio:
    "{i}O refeitório tem só você e a máquina de chá. Pela janela, a baía e um navio parado no meio dela.{/i}"
    if energia_cansaco():
        "{i}Você deita a cabeça nos braços por dez minutos. Ninguém repara.{/i}"
    else:
        "{i}Você não abre o notebook. Tenta adivinhar para onde o navio vai, e não chega a conclusão nenhuma.{/i}"
    return

label im_corporativo_s6_descansar_aterro:
    "{i}Quinze minutos a pé e você chega ao Aterro. Na sexta à tarde, tem gente saindo do trabalho direto para correr.{/i}"
    if energia_cansaco():
        "{i}Você senta na grama, encosta numa árvore e deixa o vento da baía fazer o trabalho. O celular fica no bolso.{/i}"
    else:
        "{i}Você anda pelo calçadão até a mureta. O Pão de Açúcar está nítido hoje, e o bondinho sobe devagar.{/i}"
    return
