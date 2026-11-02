# mentoria_encontros.rpy
# -------------------------------
# TEMPO LIVRE DA SAÚDE · MENTORIA "Um dia de ambulatório" (Dra. Nathalia)
# -------------------------------
# Os 5 encontros (docs/design/intermissoes-saude.md §5). O motor chama
# im_saude_mentoria_<k> em qualquer semana a partir de semana_min, e depois
# aplica a amizade, a pista do passo e, no 5º, a conquista. Aqui só há falas.
# Pacientes e recepcionista não têm sprite.

define saude_npc_recepcao = Character(_("Sônia"), color="#8FA3B8")
define saude_npc_ivo = Character(_("Seu Ivo"), color="#C49A6C")
define saude_npc_celia = Character(_("Dona Célia"), color="#C58DBF")


# 1 · Triagem e escala no papel (pista saude_p_had, só até a semana 2).
label im_saude_mentoria_1:
    "{i}Você atravessa a praça das palmeiras até o Instituto. A [NOME_DOUTORA_2] espera na porta do ambulatório, já de jaleco, com uma prancheta embaixo do braço.{/i}"
    show doutora_2 neutral at right_zoom
    with dissolve
    doutora_2 "Veio mesmo! Achei que o pessoal da computação tinha alergia a ambulatório. (risos)"
    doutora_2 "O combinado é este: você fica no canto, não anota nome de ninguém e, se o paciente não quiser você na sala, sai sem drama."
    doutora_2 "Na entrevista eu te contei como deveria ser. Aqui você vê como é."
    "{i}O paciente é novo no programa: um homem de uns quarenta anos, com um maço amassado no bolso da camisa. Ele olha para você, dá de ombros e diz que pode ficar.{/i}"
    "{i}A triagem é no papel. Primeiro, o teste de Fagerström: quanto tempo depois de acordar vem o primeiro cigarro, se ele fuma mesmo doente, quantos por dia.{/i}"
    doutora_2 "Cinco minutos depois de acordar? Antes do café, então."
    "{i}Ele ri, sem graça. Ela anota sem comentar e passa para a escala HAD: catorze perguntas sobre ansiedade e depressão, cada uma com quatro respostas.{/i}"
    "{i}As primeiras vão rápido. Na oitava, 'Estou lento para pensar e fazer as coisas', ele para, olha para a janela e diz que prefere pular.{/i}"
    "{i}Na décima, 'Perdi o interesse em cuidar da minha aparência', ele nem lê até o fim. Só balança a cabeça.{/i}"
    "{i}A [NOME_DOUTORA_2] não insiste. Escreve 'incompleta' na margem da folha, com uma setinha, e segue a consulta como se nada tivesse acontecido.{/i}"
    "{i}Vinte minutos depois, o paciente sai com um folheto e o retorno marcado. A sala fica quieta.{/i}"
    doutora_2 "Viu as duas que ele pulou?"
    "{i}Você diz que viu, e que achou que ela fosse insistir.{/i}"
    doutora_2 "Se eu insisto, ele mente. Ou não volta. Prefiro escala pela metade e paciente no retorno."
    show doutora_2 serious at right_zoom
    doutora_2 "O problema é depois. Com duas em branco, o escore não fecha. Eu não sei se ele está no limite ou longe dele."
    doutora_2 "E o papel não me avisa de nada. Daqui a três meses, alguém pega essa folha e acha que o escore é baixo, quando na verdade está faltando resposta."
    "{i}Você anota no notebook, sem nome: 'paciente novo pulou 2 perguntas da HAD por vergonha; escore incompleto não é escore baixo'.{/i}"
    doutora_2 "Isso. Anota o que aconteceu, não quem. Ele confiou em deixar você na sala."
    "{i}E percebe uma coisa que a entrevista não contou: o usuário pula, hesita, contorna. Ninguém descreve isso quando fala do próprio trabalho, porque nem nota que faz.{/i}"
    doutora_2 "Volta outro dia? Tem muita coisa que eu nunca ia lembrar de te contar numa sala de reunião."
    hide doutora_2
    with dissolve
    return


# 2 · O retorno de um paciente.
label im_saude_mentoria_2:
    show doutora_2 neutral at right_zoom
    with dissolve
    doutora_2 "Hoje é dia de retorno. Vou te apresentar o paciente mais teimoso e mais querido do programa."
    "{i}Seu Ivo tem setenta e poucos anos, um boné de time na mão e o jeito de quem conhece todo mundo no corredor. Ele aperta sua mão antes que você se apresente.{/i}"
    saude_npc_ivo "Da turma do computador? Então senta aí e aprende comigo o que não fazer. (risos)"
    "{i}É o terceiro retorno dele. A [NOME_DOUTORA_2] abre a pasta e espalha três fichas na mesa: a do primeiro atendimento, a do primeiro retorno e a do segundo.{/i}"
    "{i}Ela passa o dedo pela linha de cigarros por dia em cada uma. Vinte. Oito. Três. Depois, levanta os olhos.{/i}"
    doutora_2 "E agora, Seu Ivo?"
    saude_npc_ivo "Voltei pros vinte, doutora. Meu irmão faleceu mês passado. No velório todo mundo fumando lá fora... eu fui junto."
    "{i}Silêncio. Você espera um sermão, mas ele não vem.{/i}"
    doutora_2 "Sinto muito pelo seu irmão. E obrigada por me contar. Muita gente some quando recai."
    doutora_2 "Vamos ver onde o senhor está agora, então. Não onde estava."
    "{i}Ela pergunta sobre a vontade de parar hoje, não sobre a culpa. Anota o estágio de motivação numa ficha nova e compara com as outras três, folheando para frente e para trás.{/i}"
    saude_npc_ivo "Da outra vez a senhora disse que eu tava quase lá."
    doutora_2 "E o senhor estava. Quem chegou a três por dia uma vez conhece o caminho."
    "{i}Seu Ivo sai com o retorno marcado para dali a duas semanas e uma piada sobre o time dele.{/i}"
    doutora_2 "Viu o que eu fiz com as fichas?"
    "{i}Você diz que ela passou quase tanto tempo procurando números quanto conversando com ele.{/i}"
    doutora_2 "Exato. E olha que ele é organizado e veio em todos os retornos."
    doutora_2 "Recaída não é fracasso, é dado. O sistema precisa me mostrar a história, não só a última foto."
    "{i}Você pergunta se um gráfico da evolução do consumo resolveria.{/i}"
    doutora_2 "Gráfico fica bonito em relatório. Aqui eu preciso de outra coisa: abrir a ficha e ver, numa linha, o que mudou desde a última consulta."
    doutora_2 "Cigarro, estágio, remédio, o que aconteceu na vida. O resto eu converso."
    "{i}Você anota a diferença entre o que se pede e o que se precisa: não 'um gráfico', mas 'ver o que mudou desde o último retorno'.{/i}"
    show doutora_2 serious at right_zoom
    doutora_2 "E sabe qual é o meu maior medo? Não é o Seu Ivo recair. É o paciente que recai e não volta mais."
    doutora_2 "Esse eu só descubro semanas depois, quando alguém estranha a pasta parada."
    "{i}Você lembra do aviso de falta ao retorno que ela pediu pelo app. Agora o pedido tem um rosto, e um boné de time.{/i}"
    hide doutora_2
    with dissolve
    return


# 3 · Quem vê o quê (pista saude_p_papeis, até a semana 6).
label im_saude_mentoria_3:
    show doutora_2 neutral at right_zoom
    with dissolve
    doutora_2 "Hoje eu quero te mostrar o caminho de um prontuário, da porta até a pesquisa. Vem comigo."
    hide doutora_2
    with dissolve
    "{i}Vocês começam pela recepção. Atrás do balcão, Sônia atende o telefone, confere uma carteirinha e cadastra um paciente novo, tudo ao mesmo tempo.{/i}"
    "{i}A [NOME_DOUTORA_2] fala baixo, para não atrapalhar: a recepção precisa da agenda e do cadastro. Nome, contato, horário. Do histórico, nada.{/i}"
    "{i}Depois, a sala da enfermagem: balança, aparelho de pressão e uma folha onde a técnica anota peso, pressão e o monóxido de carbono medido no sopro.{/i}"
    "{i}A enfermagem precisa dos sinais vitais e de saber quem é o paciente. O que ele conta na consulta não passa por ali.{/i}"
    show doutora_2 neutral at right_zoom
    with dissolve
    "{i}Na sala das médicas, as pastas com o histórico completo: tabagismo, outras substâncias, escalas, remédios, o que o paciente contou de porta fechada.{/i}"
    doutora_2 "Isso aqui, só a médica que acompanha. E a pesquisa da [NOME_DOUTORA_1] recebe os números, sem saber de quem são."
    "{i}Você desenha no notebook quatro colunas: recepção, enfermagem, médica, pesquisa. Embaixo de cada uma, o que precisa ver para trabalhar. Nada além.{/i}"
    doutora_2 "Mínimo necessário. A LGPD fala bonito, mas na prática é isso: cada um vê o que precisa para fazer o próprio trabalho."
    hide doutora_2
    with dissolve
    "{i}Na volta, vocês passam de novo pela recepção. Sônia está no computador do balcão, com a agenda da semana aberta.{/i}"
    "{i}No canto de cima da tela, o nome de quem está logado: [NOME_DOUTORA_2].{/i}"
    "{i}Você pergunta, com cuidado, por que o sistema está aberto com o login da doutora.{/i}"
    saude_npc_recepcao "Ah, é que o meu perfil não abre a agenda."
    saude_npc_recepcao "Sem agenda eu não marco retorno. Aí a doutora me passou a senha dela. Faz tempo já."
    show doutora_2 serious at right_zoom
    doutora_2 "Eu sei, eu sei."
    "{i}Ela fica vermelha e puxa você de volta para o corredor.{/i}"
    doutora_2 "Ninguém aqui quer burlar nada. A senha emprestada é o jeito que a gente achou de trabalhar."
    doutora_2 "Pedi três vezes para o perfil da recepção abrir a agenda. Nunca veio."
    "{i}Você pensa no que isso quer dizer. Tudo o que a recepção faz fica registrado como se fosse a médica. E, com a senha da médica, o balcão abre o histórico inteiro.{/i}"
    "{i}Você anota, sem culpa e sem nome: um contorno é sinal de requisito mal atendido. A recepção precisava da agenda; como não tinha, ganhou acesso a tudo.{/i}"
    doutora_2 "Você vai contar para o pessoal de segurança, né?"
    "{i}Você diz que sim, e que a ideia é dar à recepção o que ela precisa, para ninguém mais depender de senha emprestada.{/i}"
    doutora_2 "Então pode contar. Se for para a Sônia ter a agenda dela, eu mesma levo o café na reunião."
    hide doutora_2
    with dissolve
    return


# 4 · A consulta de 15 minutos.
label im_saude_mentoria_4:
    show doutora_2 neutral at right_zoom
    with dissolve
    if energia_cansaco():
        doutora_2 "Você está com cara de fim de plantão. Senta aí; hoje você só cronometra."
    doutora_2 "Hoje eu quero um favor esquisito. Cronometra a minha consulta. Inteira."
    doutora_2 "Todo mundo me pergunta quanto tempo eu perco no sistema. Eu nunca sei responder."
    "{i}O paciente da vez concorda que você fique, desde que o nome dele não apareça em lugar nenhum. Você abre o cronômetro do celular e faz duas colunas no notebook: olhando o paciente, olhando a tela.{/i}"
    "{i}Minuto um: ela cumprimenta, pergunta da semana, ri de alguma coisa. Coluna do paciente.{/i}"
    "{i}Minuto três: ela se vira para o computador para abrir a ficha. Três cliques, uma tela que demora, uma senha que expirou. Coluna da tela.{/i}"
    "{i}Minuto seis: o paciente conta que tem dormido mal. Ela escuta, mas digita ao mesmo tempo, de costas para ele.{/i}"
    "{i}Minuto nove: o sistema pede um campo obrigatório que não tem nada a ver com a conversa. Ela volta duas telas para achar onde fica.{/i}"
    "{i}Minuto treze: receita, orientação, retorno marcado. Ela se vira de novo para ele, e a conversa fica boa justamente agora, no fim.{/i}"
    "{i}Minuto quinze: porta fechada. Você soma as colunas.{/i}"
    doutora_2 "E aí? Dá o veredito."
    "{i}Você mostra: dos quinze minutos, seis foram olhando a tela e digitando. Quase metade da consulta, de costas para o paciente.{/i}"
    show doutora_2 thinking at right_zoom
    doutora_2 "Seis..."
    doutora_2 "Eu chutaria dois. Juro que chutaria dois."
    "{i}Você mostra também o minuto nove: o campo obrigatório que não tinha nada a ver com a conversa. Ela ri, sem humor.{/i}"
    doutora_2 "Esse campo é da época de outro programa. Ninguém usa. Mas, se ficar em branco, o sistema não deixa salvar."
    doutora_2 "Quando eu digito, eu paro de perguntar. Quando eu paro de perguntar, ele para de contar."
    doutora_2 "Cada minuto que eu olho a tela é um minuto que eu não olho para ele. E é olhando que eu percebo quando alguém está para desistir."
    "{i}Você percebe o que tem nas mãos: não uma opinião sobre o sistema, mas um número. 'O cadastro é lento' qualquer um diz. 'Seis de quinze minutos na tela' dá para medir de novo depois.{/i}"
    "{i}E lembra de uma das reescritas da semana dos casos de uso: registrar um retorno sem mudanças em até três minutos. Agora dá para conferir se o número faz sentido.{/i}"
    doutora_2 "Faz isso de novo quando o sistema novo estiver no ar? Quero ver esse seis virar três."
    "{i}Você anota: tempo de tarefa medido antes. Medir depois do mesmo jeito, com a mesma médica e o mesmo tipo de consulta.{/i}"
    show doutora_2 positive at right_zoom
    doutora_2 "Olha só, engenharia de software com cronômetro. Vou contar para a [NOME_DOUTORA_1]. Ela adora um número."
    hide doutora_2
    with dissolve
    return


# 5 · A paciente testa o protótipo (na semana 8, a versão já está no ar).
label im_saude_mentoria_5:
    show doutora_2 neutral at right_zoom
    with dissolve
    if im_semana_atual >= 8:
        doutora_2 "Último encontro, e com o sistema no ar. Hoje quem trabalha não sou eu: é uma paciente."
        "{i}Na sala de espera, um tablet com a versão nova da escala HAD, a mesma que entrou em produção. O [NOME_DEVELOPER_TEST] deixou tudo pronto de manhã.{/i}"
    else:
        doutora_2 "Último encontro. Hoje quem trabalha não sou eu: é uma paciente."
        "{i}Na sala de espera, um tablet com o protótipo clicável da escala HAD que o [NOME_DEVELOPER_TEST] montou. Ele deixou tudo pronto de manhã, com um bilhete: 'Pode quebrar'.{/i}"
    doutora_2 "A Dona Célia aceitou responder a escala sozinha no tablet. Sessenta e dois anos, primeira vez num tablet."
    doutora_2 "Regras: ela pensa em voz alta, você anota onde ela trava, e ninguém ajuda. Nem eu, nem você. Combinado?"
    "{i}Você concorda. É mais difícil do que parece.{/i}"
    hide doutora_2
    with dissolve
    "{i}Dona Célia senta, ajeita os óculos e segura o tablet com as duas mãos, longe do rosto.{/i}"
    saude_npc_celia "Bom. Vamos ver. Pergunta um... 'Eu me sinto tensa ou contraída.' Às vezes, né? Esse aqui."
    "{i}Ela toca na resposta. Nada parece acontecer. Procura um botão para seguir, aproxima o tablet do rosto, afasta de novo.{/i}"
    saude_npc_celia "Cadê o próximo? A letra é tão pequenininha..."
    "{i}Você morde a língua. O botão 'Próximo' está no rodapé e só aparece se ela rolar a tela. Você anota: 'não achou o Próximo; letra pequena'.{/i}"
    "{i}Quase um minuto depois, ela arrasta a tela sem querer, e o botão aparece.{/i}"
    saude_npc_celia "Ah! Estava escondido. Por que esconderam?"
    "{i}Daí em diante ela vai mais rápido. Na pergunta sobre o interesse pela aparência, para.{/i}"
    saude_npc_celia "Essa eu não vou responder, não. Pula."
    "{i}Ela toca em 'Próximo' sem escolher nada. No fim, a tela não dá erro nem fica vermelha. Mostra uma frase só: 'Faltam 2 respostas. Você pode voltar ou salvar e continuar depois.'{/i}"
    saude_npc_celia "Olha que educado. Nem brigou comigo."
    "{i}Ela sorri, volta numa pergunta que tinha pulado sem perceber, responde e salva o resto para a consulta.{/i}"
    saude_npc_celia "Se até eu consegui, qualquer um consegue."
    "{i}Quando ela entra para a consulta, você mostra as anotações para a [NOME_DOUTORA_2]: onde travou, quanto tempo levou, o que disse em voz alta.{/i}"
    show doutora_2 neutral at right_zoom
    with dissolve
    doutora_2 "Duas coisas, então. Letra maior. E o botão Próximo sempre embaixo, parado, sem precisar rolar."
    doutora_2 "Eu nunca ia descobrir isso. Eu sei usar o tablet. Ela não sabe, e é para ela que a gente fez."
    "{i}Você anota as duas sugestões para o [NOME_DEVELOPER_TEST], com o tempo que ela levou para achar o botão. Tarefa clara, pensar em voz alta, não ajudar, anotar onde trava. Simples de dizer; difícil de não ajudar.{/i}"
    show doutora_2 positive at right_zoom
    doutora_2 "Cinco encontros, hein? Triagem, retorno, recepção, cronômetro e agora a Dona Célia."
    doutora_2 "Agora você sabe olhar um ambulatório."
    hide doutora_2
    with dissolve
    return
