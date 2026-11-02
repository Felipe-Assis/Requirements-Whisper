# s03.rpy
# Tempo livre da rota Corporativo, semana 3 (sexta, 15h às 18h, depois da
# inspeção da co_11). Fonte: docs/design/intermissoes-corporativo.md, seções
# 2.1 e 2.4, e o Aterro aceito em docs/design/mapa-cidade.md §2.3.
# O motor aplica tempo, energia, amizade e registro extra; aqui só há fala.
# Observar na central não dá pista nesta semana (só cena).

label im_corporativo_abertura_3:
    $ im_mostrar_local({"poi": im_local})
    with dissolve
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
    else:
        "{i}Sexta, três da tarde. Na mesa do canto ainda tem farelo do biscoito da inspeção e três cópias do documento cheias de marcas.{/i}"
    return


# -------------------------------
# Baia do Farol
# -------------------------------
label im_corporativo_s3_conversar_co_mentora:
    show co_mentora neutral at center_zoom
    with dissolve
    "{i}[NOME_CO_MENTORA] está relendo o documento da inspeção, com o caderno vinho aberto ao lado.{/i}"
    co_mentora "Senta aí. Ontem foram quatro horas de inspeção. Como você saiu dela?"
    if co_escrita_status == "rascunho":
        co_mentora "Li seu texto sobre reabrir chamado. Tem coisa boa ali."
        show co_mentora thinking at center_zoom
        co_mentora "Mas quem vai dizer se está claro não sou eu. É o [NOME_CO_SOLICITANTE]. Na semana que vem ele lê e conta o que entendeu."
        co_mentora "Se ele entender o mesmo que você, ótimo. Se entender outra coisa, melhor ainda: a gente descobre agora, e não na tela pronta."
    else:
        show co_mentora thinking at center_zoom
        co_mentora "Seu texto sobre reabrir chamado ficou pendente. Tudo bem."
        co_mentora "Pendência registrada não se perde. Pendência esquecida, sim. A sua está anotada, com dono e assunto."
    show co_mentora neutral at center_zoom
    co_mentora "Ninguém escreve requisito bom sozinho. A gente escreve, o outro lê, a gente reescreve."
    co_mentora "Terça tem reunião de arquitetura. Vamos decidir como o Farol conversa com o SGC."
    co_mentora "E o [NOME_CO_DEV] vai chegar com slide. Já estou avisando."
    hide co_mentora
    with dissolve
    return


# -------------------------------
# Central de atendimento
# -------------------------------
label im_corporativo_s3_conversar_co_supervisora:
    show co_supervisora neutral at center_zoom
    with dissolve
    "{i}[NOME_CO_SUPERVISORA] está de pé ao lado do painel de filas, com o celular na mão e a conversa de ontem aberta.{/i}"
    co_supervisora "[player_name]. Sobre a rotina das 72 h."
    co_supervisora "Respondi rápido, pelo chat, no meio da tarde. Depois passei a noite inteira pensando se tinha decidido certo."
    show co_supervisora thinking at center_zoom
    co_supervisora "Decidi que sim. Sem a rotina, minha fila de senha explode. Com a frase padrão e o \"sistema\" na trilha, a auditoria entende."
    co_supervisora "Mas minha equipe vai precisar de um treinamento curto. Quinze minutos, na troca de turno, com exemplo na tela."
    co_supervisora "Senão alguém acha que foi colega que fechou e vem me perguntar quem foi."
    show co_supervisora neutral at center_zoom
    co_supervisora "Decidi rápido, mas não decidi sozinha. Perguntaram para mim. Isso é raro."
    "{i}O painel apita. Ela guarda o celular no bolso e volta para a fila.{/i}"
    hide co_supervisora
    with dissolve
    return

label im_corporativo_s3_conversar_co_solicitante:
    show co_solicitante neutral at center_zoom
    with dissolve
    "{i}[NOME_CO_SOLICITANTE] está sentado numa cadeira emprestada perto da mesa da supervisora, com o capacete no colo.{/i}"
    co_solicitante "Fala! O [NOME_CO_DEV] me mandou um print da tela nova. Mandei na hora para o Wellington."
    show co_solicitante thinking at center_zoom
    co_solicitante "O Wellington olhou dois segundos e perguntou: e se não resolver de novo?"
    co_solicitante "Nem perguntou da cor, do tamanho da letra. Foi direto no botão de reabrir. Quer saber o que acontece depois que aperta: a solução velha some? Precisa explicar por quê?"
    "{i}Você conta que a inspeção de ontem fez essas mesmas perguntas sobre a reabertura.{/i}"
    show co_solicitante neutral at center_zoom
    co_solicitante "Olha só. Então vocês já estavam pensando nisso antes de ele perguntar."
    co_solicitante "É por isso que eu gosto de ver tela. No quadro eu concordo com tudo. Na tela eu vejo o que falta."
    co_solicitante "Quando tiver o botão, manda outro print. O Wellington vira testador oficial."
    hide co_solicitante
    with dissolve
    return

label im_corporativo_s3_observar_central:
    show co_supervisora neutral at left_zoom
    show co_solicitante neutral at right_zoom
    with dissolve
    "{i}Hoje o observador não é só você. [NOME_CO_SOLICITANTE] pediu para sentar do lado de dentro da central, ao lado da [NOME_CO_SUPERVISORA].{/i}"
    co_supervisora "Primeira vez que alguém de campo pede para ver isso aqui. Senta. Headset no ouvido, boca fechada."
    co_solicitante "Fechada. Prometo."
    "{i}Vocês três ouvem um atendente na fileira da frente. Um técnico do interior está sem VPN.{/i}"
    "{i}O atendente explica a correção passo a passo: desconectar, apagar o perfil, reconectar, testar. Com paciência.{/i}"
    "{i}Desliga. Faz uma anotação. Atende a próxima.{/i}"
    "{i}Outro técnico. Outra VPN. A mesma explicação, palavra por palavra.{/i}"
    show co_supervisora thinking at left_zoom
    co_supervisora "É a terceira vez hoje. E a tarde nem acabou."
    show co_solicitante thinking at right_zoom
    "{i}[NOME_CO_SOLICITANTE] não diz nada. Fica olhando o atendente, depois o painel, depois o próprio celular.{/i}"
    "{i}Um bom tempo passa assim. Na tela do painel, a fila da tarde sobe e desce.{/i}"
    co_solicitante "Então é isso que acontece quando eu ligo."
    co_solicitante "Eu só via o meu lado. Eu ligo, alguém atende, alguém demora. Eu nunca pensei que do outro lado tinha essa fila."
    co_supervisora "E eu nunca pensei que do seu lado tinha um técnico parado na base o dia inteiro."
    "{i}Os dois ficam em silêncio por um instante. Parece a primeira vez que concordam sem precisar de mediação.{/i}"
    show co_solicitante neutral at right_zoom
    co_solicitante "Faz o seguinte: quando a VPN cair, meu técnico escreve no chamado o que já tentou. Antes de ligar."
    show co_supervisora neutral at left_zoom
    co_supervisora "E quando a gente resolver, escreve o que fez. Aí ninguém precisa ligar de novo para perguntar."
    co_solicitante "Ligar menos, escrever mais."
    co_supervisora "Ligar menos, escrever mais. Vou colar isso no painel."
    if energia_cansaco():
        "{i}Você sai da central com a cabeça pesada, mas com uma frase anotada que vale a semana.{/i}"
    else:
        "{i}Você anota a frase no caderno. Parece pouco. É exatamente o que o Farol tenta fazer.{/i}"
    hide co_supervisora
    hide co_solicitante
    with dissolve
    return


# -------------------------------
# Café do térreo
# -------------------------------
label im_corporativo_s3_conversar_co_dev:
    show co_dev neutral at center_zoom
    with dissolve
    "{i}[NOME_CO_DEV] ocupa uma mesinha do café com o notebook aberto. Na tela, um slide com fundo escuro e letras enormes: \"A Grande Virada\".{/i}"
    co_dev "Ensaio da apresentação de terça. Microsserviços. Olha esse primeiro slide. Fala que não arrepiou."
    "{i}Ele passa os próximos: caixinhas coloridas, setas para todo lado, um foguete no último.{/i}"
    show co_dev thinking at center_zoom
    co_dev "Agora, sinceridade: o [NOME_CO_LEGADO] vai acabar comigo?"
    co_dev "Porque eu já sei a primeira pergunta dele. \"E a rotina das 72 h, vai para qual caixinha?\""
    co_dev "Slide bonito eu tenho. Resposta para o [NOME_CO_LEGADO] eu não tenho."
    "{i}Você não opina sobre a arquitetura. Isso é para terça, com todo mundo na sala.{/i}"
    show co_dev neutral at center_zoom
    co_dev "Tudo bem, tudo bem. Pelo menos o foguete fica. O foguete é inegociável."
    hide co_dev
    with dissolve
    return

label im_corporativo_s3_descansar_cafe:
    "{i}Você pega um café coado no balcão e senta perto da porta giratória. Na vitrine da lojinha ao lado, uma fileira de canecas brancas espera alguém com motivo para comprar.{/i}"
    "{i}Depois da inspeção de ontem, o barulho da rua parece música. Ninguém pergunta se o requisito dá para testar.{/i}"
    if energia_cansaco():
        "{i}Você quase cochila na banqueta. O atendente do café deixa um copo d'água do seu lado sem perguntar nada.{/i}"
    else:
        "{i}Você toma o café inteiro ainda quente, coisa rara nesta semana.{/i}"
    return


# -------------------------------
# Refeitório
# -------------------------------
label im_corporativo_s3_conversar_co_qualidade:
    show co_qualidade neutral at center_zoom
    with dissolve
    "{i}[NOME_CO_QUALIDADE] está numa mesa comprida do refeitório, tablet de lado, comendo uma salada com uma mão.{/i}"
    co_qualidade "O [NOME_CO_DEV] passou aqui faz dez minutos. Reclamou do avatar 3D. Registrei a reclamação. Prioridade baixa, como prometido."
    "{i}Ela ri sozinha.{/i}"
    co_qualidade "Sabe que eu gosto dele? Ele testa os limites do documento. Alguém tem que testar."
    show co_qualidade thinking at center_zoom
    "{i}Você pergunta da fama de \"chata do CAB\".{/i}"
    co_qualidade "Desde 2019. Teve uma sexta em que uma mudança pequena zerou o relatório da diretoria. Dali em diante, eu decidi que prefiro incomodar na quinta a ver alguém trabalhando no sábado."
    co_qualidade "Mudança mal planejada não cai na minha mesa. Cai na madrugada de alguém. Geralmente de quem não opinou."
    show co_qualidade neutral at center_zoom
    co_qualidade "Chata na quinta, para ninguém chorar no sábado. É o meu acordo comigo mesma."
    hide co_qualidade
    with dissolve
    return

label im_corporativo_s3_descansar_refeitorio:
    "{i}O refeitório da tarde de sexta tem três pessoas e um rádio baixo tocando samba antigo.{/i}"
    "{i}Você pega um chá de máquina e senta de frente para a janela. A baía está cheia de veleiros.{/i}"
    if energia_cansaco():
        "{i}Você deita a cabeça nos braços por dez minutos. Ninguém repara.{/i}"
    else:
        "{i}Você não abre o notebook. O documento da inspeção pode esperar até segunda.{/i}"
    return


# -------------------------------
# Parque do Aterro (descansar, S2+)
# -------------------------------
label im_corporativo_s3_descansar_aterro:
    "{i}Você atravessa a avenida e caminha quinze minutos até o Aterro. A torre do Grupo Vértice vai diminuindo atrás de você.{/i}"
    "{i}No gramado, um grupo joga futevôlei. Mais perto da água, alguém lê deitado na sombra de uma árvore enorme.{/i}"
    if energia_cansaco():
        "{i}Você deita na grama e fica olhando a copa da árvore. Quando percebe, passou meia hora.{/i}"
    else:
        "{i}Você senta no muro do calçadão. O vento da baía leva embora o resto da semana.{/i}"
    return


# -------------------------------
# Sala do arquivo
# -------------------------------
label im_corporativo_s3_conversar_co_legado:
    if get_friendship_point("co_legado") >= 4:
        show co_legado neutral at center_zoom
        with dissolve
        "{i}[NOME_CO_LEGADO] puxou um monitor para a mesa do arquivo. Do lado, a caneca de 2008.{/i}"
        co_legado "Meia hora de PL/SQL? Senta aí. A rotina das 72 h merece."
        "{i}Na tela, o PL/SQL da TRG_FECHA_SENHA_72H. Quarenta linhas. No topo, um comentário: \"greve - JT 03/2013\".{/i}"
        show co_legado thinking at center_zoom
        co_legado "Março de 2013. A central em greve, a fila de senha passando de três mil. Eu escrevi isso numa quinta à noite."
        co_legado "Olha a linha doze. Setenta e duas horas. O código diz o que ela faz. Não diz quem pediu, o que a gente discutiu nem o que ficou de fora."
        co_legado "Isso não está em tabela nenhuma. Está aqui."
        "{i}Ele bate de leve com o dedo na própria têmpora.{/i}"
        show co_legado neutral at center_zoom
        co_legado "O código conta metade. A outra metade eu conto, enquanto lembro."
    else:
        show co_legado neutral at center_zoom
        with dissolve
        "{i}[NOME_CO_LEGADO] está no scanner do arquivo, alinhando uma foto antiga com cuidado de restaurador.{/i}"
        co_legado "Lançamento do SGC, 2008. Achei no armário. Repara no cabelo. Eu também tinha."
        "{i}Você tenta ver a foto, mas ele cobre com a mão, rindo.{/i}"
        co_legado "Depois te mando. Tem gente nessa foto que vai ficar brava se eu mostrar sem aviso."
        show co_legado thinking at center_zoom
        co_legado "Cada pessoa aí sabia uma parte do sistema. Hoje, algumas dessas partes só existem na minha cabeça."
        co_legado "O código conta metade. A outra metade eu conto, enquanto lembro."
    hide co_legado
    with dissolve
    return

label im_corporativo_s3_estudar_arquivo:
    "{i}Numa caixa-arquivo com a etiqueta \"SGC - casos de uso - 2008\", você acha uma pasta grossa, cheia de diagramas e passos numerados.{/i}"
    "{i}Você coloca do lado o UC01 que a equipe escreveu na segunda: consultar chamado pelo número.{/i}"
    "{i}Os casos de 2008 têm fluxo principal, fluxos alternativos, exceções. Alguns têm vinte e cinco passos.{/i}"
    "{i}Metade descreve telas que nunca foram feitas. Um deles termina com \"o sistema envia um fax ao solicitante\".{/i}"
    if energia_cansaco():
        "{i}Você para no décimo passo de um caso de uso e esfrega os olhos. Pula para o fim e volta depois.{/i}"
    "{i}O UC01 de segunda é curto e tem as exceções que importam: SGC fora do ar, chamado de outra pessoa.{/i}"
    "{i}A história do [NOME_CO_SOLICITANTE] cabe num cartão. O caso de uso mostra o caminho passo a passo, com os desvios.{/i}"
    "{i}Você anota no notebook quando usar cada um, e que os dois podem conviver.{/i}"
    return
