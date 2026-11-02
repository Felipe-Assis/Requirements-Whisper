# s07.rpy
# -------------------------------
# TEMPO LIVRE DA SAÚDE · SEMANA 7 (Dia dos testes)
# -------------------------------
# Conteúdos próprios da semana (docs/design/intermissoes-saude.md, S7). As
# conversas de fio e os descansos ficam em comum.rpy. Recompensas (amizade,
# pista, registro extra, energia) são aplicadas pelo motor depois de cada
# label: aqui só há falas. pista_tem() ainda reflete as semanas anteriores.

label im_saude_abertura_7:
    "{i}Os bugs do dia estão anotados e as correções, divididas. Até o fim do expediente, o tempo é seu.{/i}"
    # im_iniciar já zerou im_hora_extra; o desconto fica no registro da semana.
    if any(d[0] == "hora extra" for d in im_registro_semana()["descontos"]):
        "{i}A noite em claro da semana passada ainda cobra: hoje o tempo livre é mais curto.{/i}"
    if energia_cansaco():
        "{i}Seus olhos ardem de tanto ler log. Hoje, uma pausa de verdade pode valer mais do que outra tarefa.{/i}"
    return


# Ajudar César: "O teste das 3h" (pista saude_p_memoria, dada pelo motor).
label im_saude_s7_ajudar_developer_test:
    show developer_test thinking at right_zoom
    with dissolve
    "{i}Na mesa da equipe, [NOME_DEVELOPER_TEST] encara um gráfico que sobe, sobe, sobe e cai a zero sempre no mesmo ponto.{/i}"
    developer_test "Olha isso. Teste de resistência no cadastro: um robô cadastrando paciente sem parar, quarenta e oito horas seguidas."
    developer_test "Só que ele nunca passa da madrugada. Três da manhã, morre. Ontem, anteontem, hoje."
    "{i}Você pergunta o que o log do teste diz às três horas.{/i}"
    developer_test "Nada. Nenhum erro. Parece que alguém puxou a tomada."
    "{i}Vocês trocam de log: em vez do log do teste, o do servidor. Linha por linha, de trás para frente, a partir das 2h59.{/i}"
    show developer_test serious
    developer_test "Ali. 'Rotina de manutenção: reinício agendado.' Toda madrugada. Desde... desde sempre."
    developer_test "Alguém criou isso para o servidor não ficar lento e esqueceu de avisar o resto do mundo."
    "{i}Você pensa alto: se o servidor reinicia toda noite, nenhum teste aqui dura mais de um dia.{/i}"
    developer_test "..."
    developer_test "Então a gente nunca testou o sistema por mais de um dia."
    developer_test "E produção não reinicia de madrugada. Produção fica ligada semanas."
    show developer_test thinking
    developer_test "Se tiver alguma coisa crescendo devagar, memória, conexão aberta, arquivo temporário, o reinício esconde. Todo dia ele limpa a sujeira antes de alguém ver."
    "{i}Desligar a rotina não depende de vocês: o servidor de testes é da infraestrutura do Instituto. [NOME_DEVELOPER_TEST] escreve o pedido ali mesmo, com o trecho do log colado.{/i}"
    developer_test "Pedido feito. Prioridade alta, para a semana do deploy. Se demorar, eu fico de olho na memória na mão mesmo."
    if pista_tem("saude_p_memoria"):
        developer_test "Espera. É a mesma rotina que o [NOME_DEVELOPER_CODING] achou. Ninguém desligou."
        developer_test "Achar o problema não adianta se ninguém fica com ele. Desta vez eu ponho meu nome no pedido."
    else:
        show developer_test confident
        developer_test "Valeu, [player_name]. Sozinho eu ia passar a tarde mexendo na configuração do robô, achando que o problema era ele."
    developer_test "Usuário não lê manual. Pelo visto, servidor também não."
    hide developer_test
    with dissolve
    return


# Ajudar Mateus, variação da semana 7: "O backup verde" (pista saude_p_backup).
# O label sem semana (im_saude_ajudar_developer_security) é o da semana 6.
label im_saude_s7_ajudar_developer_security:
    "{i}No subsolo, o ar-condicionado faz barulho de avião. [NOME_DEVELOPER_SECURITY] etiqueta cabos com uma caneta, devagar, um por um.{/i}"
    show developer_security serious at right_zoom
    with dissolve
    if pista_tem("saude_p_backup"):
        developer_security "Voltou para o subsolo, [player_name]? Senta. Hoje eu aceito ajuda e aceito cobrança."
        "{i}Você pergunta se ele conseguiu testar a restauração do backup.{/i}"
        developer_security "Não. A semana passada virou a semana do código. Esta virou a semana dos testes."
        developer_security "O painel continua verde. E eu continuo sem saber se ele está dizendo a verdade."
    else:
        developer_security "Chegou na hora. O servidor novo vem amanhã e este rack está uma bagunça."
        "{i}Na parede, um monitor mostra o painel do backup: uma fileira de quadradinhos verdes, um por dia, até onde a vista alcança.{/i}"
        developer_security "Dois anos sem falhar. É a única coisa nesta sala que nunca me deu trabalho."
        "{i}Você pergunta quando foi a última vez que alguém restaurou uma dessas cópias.{/i}"
        show developer_security thinking
        developer_security "..."
        "{i}Ele abre o wiki da equipe e procura: 'restauração', 'restore', 'recuperar'. Nada. Só a página que explica como configurar a rotina, escrita dois anos atrás.{/i}"
        developer_security "Verde quer dizer que o arquivo foi gravado. Não quer dizer que ele abre."
        developer_security "Backup que nunca foi restaurado é um arquivo que a gente torce para estar certo."
    "{i}Vocês passam a hora seguinte arrumando o rack para o servidor novo. Ele fala pouco, mas explica o motivo de cada etiqueta.{/i}"
    show developer_security serious
    developer_security "Etiqueta parece bobagem. Às três da manhã, com o sistema fora do ar, é o que separa o cabo certo do errado."
    developer_security "Em incidente ninguém lembra de nada. A gente só segue o que estava escrito antes."
    "{i}No fim, ele cola um post-it amarelo na borda do monitor do backup: 'Testar restauração'.{/i}"
    developer_security "Três noites lendo log de acesso. Eu já não confio nem no meu relógio."
    developer_security "Semana que vem, sem falta."
    hide developer_security
    with dissolve
    return


# Estudar na sala de reuniões: rascunho do plano de rollback (extra saude_extra_rollback).
label im_saude_s7_estudar_sala_reunioes:
    show developer_management thinking at left_zoom
    show developer_project serious at right_zoom
    with dissolve
    "{i}O quadro ainda tem o checklist da manhã. [NOME_DEVELOPER_MANAGEMENT] apaga um canto e escreve uma pergunta só.{/i}"
    developer_management "Se o deploy da semana que vem der errado, quem decide voltar? E em quanto tempo?"
    developer_project "..."
    developer_management "Pois é. Ninguém sabe. Nem eu."
    "{i}Você puxa uma cadeira e começa o rascunho: para qual versão voltar, quem decide, o prazo para decidir e o que fazer com o que for gravado na versão nova.{/i}"
    developer_project "Os dados. Paciente cadastrado no dia do deploy não pode sumir na volta."
    developer_management "Quinze minutos de problema sem solução à vista, e a gente volta. Quem decide sou eu. Se eu não atender, o [NOME_DEVELOPER_PROJECT]."
    "{i}No fim da hora, o rascunho cabe numa página. [NOME_DEVELOPER_MANAGEMENT] tira uma foto do quadro.{/i}"
    developer_management "Antes do deploy, a gente ensaia a volta em homologação. Rollback que nunca foi testado é só uma esperança."
    hide developer_management
    hide developer_project
    with dissolve
    return


# Observar no ambulatório: "A planilha da pesquisa" (só cena; quem é observada
# é a Dra. Michelle).
label im_saude_s7_observar_ambulatorio:
    "{i}Você atravessa a praça até o Instituto. Na sala das médicas, a [NOME_DOUTORA_1] está debruçada sobre o notebook, com uma pilha de fichas de um lado e um café frio do outro.{/i}"
    show doutora_1 neutral at right_zoom
    with dissolve
    doutora_1 "Pode sentar, [player_name]. Só não repara: é planilha de pesquisa. A parte chata da ciência."
    "{i}Ela explica: o Instituto vai mandar os dados do programa para um grupo de pesquisa de outra universidade. Antes, ela precisa tirar a identificação dos pacientes.{/i}"
    doutora_1 "Me pediram 'dados anonimizados'. Então eu apago os nomes."
    "{i}Ela seleciona a coluna de nomes e apaga, conferindo com as fichas de papel. Você observa em silêncio, como combinou.{/i}"
    "{i}Duzentas linhas depois, a coluna está vazia. Ao lado dela, a coluna de telefone continua cheia. Mais adiante, data de nascimento e bairro.{/i}"
    "{i}E, no fim, um campo de observações. Numa das linhas: 'Seu Ivo pediu para remarcar por causa do enterro do irmão'.{/i}"
    doutora_1 "Pronto. Sem nome, sem CPF. Agora posso mandar."
    "{i}Você pergunta, com cuidado, se pode mostrar uma coisa antes.{/i}"
    "{i}Você aponta o telefone, a data de nascimento ao lado do bairro e a linha das observações.{/i}"
    "{i}Com o telefone, qualquer pessoa liga e descobre quem é. Data de nascimento e bairro juntos quase dizem o nome. E o Seu Ivo está ali, escrito por extenso.{/i}"
    doutora_1 "..."
    show doutora_1 serious at right_zoom
    doutora_1 "Nossa. Eu ia mandar isso hoje."
    doutora_1 "Sabe que ninguém nunca me explicou o que 'anonimizar' quer dizer na prática? Todo mundo fala. Ninguém mostra."
    "{i}Vocês fazem juntos uma lista curta na margem de uma ficha: tirar telefone e contato; trocar a data de nascimento por faixa de idade; trocar o bairro pela região; revisar o campo de observações linha por linha, ou nem mandar.{/i}"
    doutora_1 "Faixa de idade serve para a pesquisa. Ninguém precisa saber o dia do aniversário de ninguém."
    show doutora_1 positive at right_zoom
    doutora_1 "Obrigada, [player_name]. E obrigada por falar com jeito. Detesto quando apontam erro como se fosse crime."
    "{i}Você anota no notebook, sem nomes. A pergunta da manhã, exportar com ou sem identificação, agora tem rosto: uma médica cansada, no fim da tarde, apagando nomes à mão.{/i}"
    hide doutora_1
    with dissolve
    return


# Conversar com a Dra. Michelle: a frase para as colegas.
label im_saude_s7_conversar_doutora_1:
    show doutora_1 neutral at right_zoom
    with dissolve
    doutora_1 "[player_name], me ajuda numa coisa. Depois da entrega, eu vou apresentar o sistema para as colegas do Instituto."
    doutora_1 "São doze médicas, meia hora de reunião e nenhuma paciência para slide."
    doutora_1 "Se eu não consigo explicar em uma frase, as minhas colegas não vão usar."
    show doutora_1 thinking at right_zoom
    doutora_1 "Então me diz: em uma frase, o que muda para elas?"
    menu (tipo="conversa"):
        "O formulário se salva sozinho. Ninguém mais perde uma consulta pela metade.":
            doutora_1 "Essa a [NOME_DOUTORA_2] vai contar com lágrimas nos olhos. Todo mundo aqui já perdeu um formulário."
        "Cada mudança num dado fica registrada: quem mudou, quando e o que era antes.":
            doutora_1 "Essa é a minha. Dois dias conferindo ficha de papel por causa de um número. Nunca mais."
        "O sistema foi feito ouvindo vocês, então ele segue a rotina do ambulatório.":
            doutora_1 "Bonito. Mas médica não se convence com 'ouvimos vocês'. Médica se convence com o que economiza tempo."
            doutora_1 "Me dá um exemplo, que a frase vem junto."
    doutora_1 "Vou começar com uma história, não com a tela. Aprendi com vocês na entrevista: caso real rende."
    doutora_1 "Depois eu mostro um botão. Um só."
    hide doutora_1
    with dissolve
    return
