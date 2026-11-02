# s05.rpy
# -------------------------------
# TEMPO LIVRE DA SAÚDE · SEMANA 5 (sexta, depois da tarde de estudos)
# -------------------------------
# Conteúdos próprios da semana (docs/design/intermissoes-saude.md, S5). As
# conversas de fio, os descansos e a mentoria ficam em comum.rpy e
# mentoria.rpy. Recompensas (amizade, pista, registro extra, energia) são
# aplicadas pelo motor depois de cada label: aqui só há falas. pista_tem()
# ainda reflete as semanas anteriores.

label im_saude_abertura_5:
    "{i}A tarde de estudos rendeu. Ainda falta um pedaço do expediente, e ninguém está cobrando nada.{/i}"
    if energia_cansaco():
        "{i}Foi uma semana de cronograma, riscos e prazos. Se o corpo pedir pausa, o café e a praça estão logo ali.{/i}"
    return


# Ajudar Joseph: "O servidor que melhora de manhã" (pista saude_p_memoria).
# Sem semana no nome: vale para a S5 e a S6. Na S6, quem já ganhou a pista na
# S5 vê outra ajuda (.revisao), para não repetir a mesma descoberta.
label im_saude_ajudar_developer_coding:
    "{i}Na mesa da equipe, [NOME_DEVELOPER_CODING] encara o terminal com os braços cruzados, como quem espera um pedido de desculpas.{/i}"
    show developer_coding serious at right_zoom
    with dissolve
    if im_semana_atual >= 6 and pista_tem("saude_p_memoria"):
        jump .revisao
    developer_coding "[player_name], chega aqui. Quero uma segunda opinião antes de culpar o código errado."
    if im_semana_atual >= 6:
        developer_coding "O servidor de testes é rápido de manhã e lento à tarde. Hoje, com todo mundo subindo código, está pior ainda."
    else:
        developer_coding "O servidor de testes é rápido de manhã e lento à tarde. Todo dia. Mesmo código, mesma carga."
    developer_coding "Opinião eu tenho várias. Quero número."
    "{i}Vocês abrem o painel de monitoramento. O gráfico de memória sobe devagar o dia inteiro e despenca de uma vez durante a madrugada.{/i}"
    "{i}Sempre no mesmo horário: 3h.{/i}"
    show developer_coding thinking
    developer_coding "Às três da manhã ninguém está mexendo em nada. Por que cai?"
    "{i}Você sugere olhar as tarefas agendadas do servidor. Ele abre a lista sem muita fé.{/i}"
    "{i}Na quarta linha, uma rotina que reinicia o servidor todo dia às 3h. Criada há quatro anos. O único comentário: 'para limpar'.{/i}"
    developer_coding "Para limpar o quê?"
    "{i}Ninguém sabe. Quem criou a rotina já saiu da empresa, e o wiki não fala dela.{/i}"
    developer_coding "Então o servidor fica lento à tarde, reinicia de madrugada e amanhece novinho. E todo mundo acha normal."
    show developer_coding serious
    developer_coding "Espera. Então qualquer coisa que cresce devagar nunca passa de um dia."
    developer_coding "Se tem alguma coisa enchendo a memória aos poucos, a gente nunca vê. O reinício limpa antes."
    menu (tipo="conversa"):
        "Perguntar se não é melhor desligar a rotina agora":
            developer_coding "Com a entrega chegando, sem saber o que ela segura em pé? Nada de mexer no escuro."
            developer_coding "Se eu desligo hoje e o servidor cai amanhã no meio dos testes do [NOME_DEVELOPER_TEST], ninguém vai agradecer a descoberta."
        "Perguntar o que ele vai fazer com isso":
            developer_coding "Anotar. Com o gráfico, a rotina e o horário. Do jeito que a gente achou, não do jeito que eu vou lembrar daqui a um mês."
    "{i}Ele cria um cartão no quadro: 'Reinício das 3h: o que cresce durante o dia?'. Põe na coluna de depois do deploy.{/i}"
    developer_coding "Agora o módulo de cadastro é a prioridade. Mas isso aqui não sai do quadro."
    show developer_coding neutral
    developer_coding "Valeu, [player_name]. Eu ia passar a tarde otimizando consulta que não tinha culpa nenhuma."
    hide developer_coding
    with dissolve
    return

label .revisao:
    developer_coding "A rotina das três continua lá, antes que você pergunte. Está no quadro, para depois do deploy. Não esqueci."
    developer_coding "Hoje eu preciso de outra coisa: revisão. Pouco código, mas é do cadastro."
    "{i}São trinta linhas: a validação do CPF. Você começa pelo comportamento, não pelo estilo.{/i}"
    "{i}Os dígitos verificadores estão certos. Mas você testa de cabeça um CPF com os onze números iguais, e a conta fecha.{/i}"
    show developer_coding thinking
    developer_coding "Passa na conta e não existe. Bem lembrado."
    "{i}Mais abaixo, quando o CPF é inválido, a mensagem de erro vai para o log com o CPF inteiro.{/i}"
    developer_coding "Dado de paciente no log. Se o [NOME_DEVELOPER_SECURITY] vê isso, me olha daquele jeito dele, devagar."
    "{i}Ele corrige as duas coisas e escreve um teste para cada uma antes de subir de novo.{/i}"
    show developer_coding neutral
    developer_coding "Revisão boa é essa: a pergunta que eu não tinha feito."
    hide developer_coding
    with dissolve
    return


# Estudar na sala de reuniões: revisar o PR de outra equipe (extra saude_extra_revisao).
label im_saude_s5_estudar_sala_reunioes:
    show developer_requirements enthusiastic at left_zoom
    with dissolve
    developer_requirements "[player_name], topa um desafio? A equipe da agenda pediu alguém de fora para revisar um PR pequeno. Eu indiquei você."
    developer_requirements "É o lembrete por SMS na véspera da consulta. Tem um roteiro de revisão no wiki. Começa por ele."
    "{i}O roteiro tem quatro linhas. Primeiro o comportamento: o código faz o que o requisito pede, inclusive nas exceções? Depois nomes, entradas validadas, dado sensível fora do log e testes junto da mudança.{/i}"
    "{i}Você resiste à vontade de comentar a indentação e lê o requisito: avisar o paciente um dia antes, a não ser que a consulta tenha sido cancelada.{/i}"
    "{i}O código manda o lembrete. Mas não confere se a consulta foi cancelada. E, quando o telefone está vazio, tenta enviar mesmo assim e grava no log o nome e o telefone do paciente.{/i}"
    show developer_requirements thinking
    developer_requirements "E aí? Achou o quê?"
    "{i}Você mostra os três pontos, nessa ordem.{/i}"
    developer_requirements "Paciente que cancelou recebendo lembrete... É assim que a pessoa passa a achar que o Instituto não sabe o que faz."
    "{i}Você escreve os comentários: o que acontece, em qual caso e uma sugestão. Nenhum começa com 'você esqueceu'.{/i}"
    show developer_requirements enthusiastic
    developer_requirements "Comentou o código, não a pessoa. E começou pelo que o paciente ia sentir. É isso."
    developer_requirements "O espaço sobrando depois do parêntese fica para o lint reclamar. Ele não se ofende."
    hide developer_requirements
    with dissolve
    return


# Ajudar Mateus na praça: "A médica em dois lugares" (pista saude_p_papeis).
label im_saude_s5_ajudar_developer_security:
    "{i}Na praça, [NOME_DEVELOPER_SECURITY] anda devagar entre as palmeiras, com as mãos nos bolsos. Quando vê você, para.{/i}"
    show developer_security thinking at right_zoom
    with dissolve
    developer_security "Eu ando para pensar. Lá em cima, com o monitor na frente, eu tiro conclusão rápido demais."
    developer_security "Me ajuda com uma coisa que eu vi no log de acesso do sistema antigo? Eu conto de memória. Sem nome de paciente."
    "{i}Vocês sentam num banco à sombra. Ele desenha uma linha do tempo com o dedo na palma da mão.{/i}"
    developer_security "Terça. 7h02: a [NOME_DOUTORA_2] entra no sistema pelo computador da recepção e abre a agenda do dia."
    developer_security "7h05: ela registra a evolução de um paciente. Pelo computador do plantão. No outro prédio."
    "{i}Três minutos. Não dá para atravessar a praça, subir dois andares e ligar outro computador em três minutos.{/i}"
    developer_security "Pois é. Ou a doutora tem uma irmã gêmea, ou não era ela na recepção."
    "{i}Você pergunta se o perfil da recepção consegue abrir a agenda.{/i}"
    developer_security "Boa pergunta. Deixa eu ver."
    "{i}Ele confere no celular a tabela de permissões do sistema antigo. O perfil da recepção cadastra paciente. A agenda, não abre.{/i}"
    show developer_security serious
    developer_security "Então a recepção usa a senha dela para trabalhar. E tudo o que a recepção faz fica registrado como se fosse a médica."
    developer_security "Inclusive abrir histórico. Com senha de médica, abre qualquer um."
    developer_security "Senha emprestada não é maldade. É sinal de que o perfil de alguém não deixa trabalhar."
    menu (tipo="conversa"):
        "Perguntar se isso não é caso de advertência":
            developer_security "Se eu brigo com a recepção, amanhã ela pega outra senha. Se eu conserto o perfil, ela não precisa mais de senha nenhuma."
        "Perguntar o que ele vai fazer agora":
            developer_security "Nada com pressa. Log a gente lê duas vezes antes de apontar para alguém."
            developer_security "Primeiro eu anoto o que vi, do jeito que estava. Depois isso entra na revisão dos papéis de acesso."
    if pista_tem("saude_p_papeis"):
        "{i}Você conta, com cuidado, que já tinha visto a cena na recepção do ambulatório, ao lado da [NOME_DOUTORA_2].{/i}"
        developer_security "Você já tinha visto isso de perto, então. Agora tem o log também."
        developer_security "Duas fontes dizendo a mesma coisa. Deixou de ser palpite."
    else:
        developer_security "Se um dia você passar pela recepção do ambulatório, repara. Sem julgar ninguém. Só repara."
    "{i}Ele escreve uma linha no caderno de capa preta e fecha. Fica um tempo olhando um bem-te-vi na palmeira.{/i}"
    developer_security "Obrigado. Sozinho, eu ia passar a tarde achando que o relógio do servidor estava errado."
    hide developer_security
    with dissolve
    return


# Observar no ambulatório: "A fila da tarde" (só cena, sem pista).
label im_saude_s5_observar_ambulatorio:
    "{i}Quatro da tarde no ambulatório. A sala de espera está cheia: cadeiras azuis ocupadas, gente em pé perto do bebedouro, uma criança desenhando no verso de uma senha.{/i}"
    "{i}Você se senta num canto, perto do balcão, de caderno aberto.{/i}"
    "{i}Colado no balcão, virado para dentro, há um cartão plastificado com quatro linhas escritas à mão: gestantes; recaída na última semana; primeira consulta; retorno.{/i}"
    "{i}Um senhor se levanta e vai até o balcão.{/i}"
    "Paciente" "Eu cheguei antes daquela moça. Por que ela vai entrar primeiro?"
    saude_npc_recepcao "Ela está grávida, senhor. Gestante entra antes. Está escrito aqui, ó."
    "{i}Sônia, a recepcionista, vira o cartão para ele ler. Ele resmunga, mas volta para a cadeira.{/i}"
    show doutora_2 neutral at right_zoom
    with dissolve
    doutora_2 "Esse cartão já evitou muita briga. E muita injustiça também."
    "{i}Você pergunta por que a recaída vem antes da primeira consulta.{/i}"
    show doutora_2 serious at right_zoom
    doutora_2 "Quem recaiu esta semana está por um fio. Se esperar duas horas na cadeira, vai embora e não volta."
    doutora_2 "Quem veio pela primeira vez ainda tem a coragem do primeiro dia. Aguenta esperar um pouco."
    "{i}Na meia hora seguinte, você conta seis pacientes chamados, todos na ordem do cartão.{/i}"
    "{i}Quando Sônia sai para tomar um café, quem fica no balcão é um rapaz novo. Ele chama por ordem de chegada. Duas pessoas reclamam. Sônia volta, olha a fila e reorganiza sem dizer nada.{/i}"
    doutora_2 "Antes do cartão, dependia de quem estava no balcão e de quem reclamava mais alto."
    doutora_2 "Critério escrito é para ninguém decidir no humor do dia."
    "{i}Você anota as quatro linhas do cartão, na ordem, e uma observação: se um dia o sistema mostrar a fila só por hora de chegada, ele desfaz o cartão.{/i}"
    doutora_2 "Isso. Se o sistema ignorar o cartão, a Sônia imprime outra lista e ignora o sistema."
    "{i}Você lembra do plano da manhã: duas vagas na primeira entrega, e o critério veio antes da vontade de cada um. Aqui é igual, só que com gente esperando na cadeira.{/i}"
    hide doutora_2
    with dissolve
    return
