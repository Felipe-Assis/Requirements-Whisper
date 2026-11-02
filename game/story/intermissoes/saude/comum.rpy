# comum.rpy
# -------------------------------
# TEMPO LIVRE DA ROTA SAÚDE: conversas em fios e descansos
# -------------------------------
# docs/design/intermissoes-saude.md §3 (ajuste A7). O motor chama
# im_saude_conversar_<cid> quando a semana não tem conversa própria
# (im_saude_s<N>_conversar_<cid>). Esse label chama a próxima conversa da
# série da pessoa (fio 1 a 3); depois do fio 3, o papo rápido
# (im_saude_papo_<cid>, se existir) ou a fala genérica do motor.
# Os fios não dependem da semana e não citam eventos futuros: podem cair em
# qualquer intermissão, inclusive no primeiro dia.
# Recompensas (amizade) são do motor: nada aqui soma ponto.

init 3 python:

    def saude_conversas(cid):
        """Quantas conversas já terminadas com cid em todas as intermissões."""
        total = 0
        for sem in store.im_feitas.get("saude", {}).values():
            total += sum(1 for p, a, t in sem.get("acoes", []) if a == "conversar" and t == cid)
        return total

    def saude_fio(cid):
        """Label da próxima conversa: fio 1..3, depois o papo rápido."""
        n = saude_conversas(cid) + 1
        fio = "im_saude_fio_%s_%d" % (cid, n)
        if n <= 3 and renpy.has_label(fio):
            return fio
        papo = "im_saude_papo_%s" % cid
        if renpy.has_label(papo):
            return papo
        return "im_generico_conversar"


# -------------------------------
# Despacho (um por pessoa com fio)
# -------------------------------
label im_saude_conversar_developer_requirements:
    call expression saude_fio("developer_requirements") from _im_saude_fio_req
    return

label im_saude_conversar_developer_ai:
    call expression saude_fio("developer_ai") from _im_saude_fio_ai
    return

label im_saude_conversar_developer_coding:
    call expression saude_fio("developer_coding") from _im_saude_fio_coding
    return

label im_saude_conversar_developer_management:
    call expression saude_fio("developer_management") from _im_saude_fio_management
    return

label im_saude_conversar_developer_quality:
    call expression saude_fio("developer_quality") from _im_saude_fio_quality
    return

label im_saude_conversar_developer_project:
    call expression saude_fio("developer_project") from _im_saude_fio_project
    return

label im_saude_conversar_developer_security:
    call expression saude_fio("developer_security") from _im_saude_fio_security
    return

label im_saude_conversar_developer_test:
    call expression saude_fio("developer_test") from _im_saude_fio_test
    return

label im_saude_conversar_doutora_2:
    call expression saude_fio("doutora_2") from _im_saude_fio_doutora_2
    return


# -------------------------------
# Emily (developer_requirements)
# -------------------------------
label im_saude_fio_developer_requirements_1:
    # O caderno de frases
    show developer_requirements neutral at center_zoom
    "{i}[NOME_DEVELOPER_REQUIREMENTS] escreve num caderninho de capa verde. Quase tudo ali está entre aspas.{/i}"
    developer_requirements "Reparou nas aspas? Não é mania. Quer dizer que foi a própria pessoa que falou."
    show developer_requirements thinking
    developer_requirements "Olha esta, de um projeto antigo: 'Perdi tudo de novo e ninguém acredita em mim.' Uma recepcionista me disse isso quase chorando."
    developer_requirements "No relatório da equipe, virou 'usuária relata instabilidade ao salvar'. Está correto. E não dói em ninguém."
    menu (tipo="conversa"):
        "Perguntar por que a dor importa num requisito":
            show developer_requirements serious
            developer_requirements "Porque é a dor que decide a prioridade. 'Instabilidade' vai para o fim da fila. 'Perdi tudo de novo' não espera."
        "Perguntar se copiar tudo não toma tempo demais":
            show developer_requirements positive
            developer_requirements "Cinco minutos na hora. Economiza uma semana quando alguém pergunta: 'mas foi isso mesmo que pediram?'"
    show developer_requirements neutral
    developer_requirements "Eu anoto do jeito que a pessoa falou. Resumo eu faço depois."
    "{i}Ela arranca uma folha em branco do caderno e te entrega. No alto, com a letra dela: 'Frases dos usuários'.{/i}"
    hide developer_requirements
    return

label im_saude_fio_developer_requirements_2:
    # Antes dos requisitos
    show developer_requirements positive at center_zoom
    developer_requirements "Sabe onde eu aprendi a fazer entrevista? Não foi na faculdade. Foi em três anos de suporte por telefone."
    "{i}Ela ri da sua cara de surpresa.{/i}"
    developer_requirements "Oito horas por dia de gente irritada. Ninguém ligava para dizer 'preciso de um campo de data com validação'."
    show developer_requirements thinking
    developer_requirements "Ligavam para dizer 'o sistema comeu meu relatório'. 'Apareceu uma tela vermelha'. 'Ontem funcionava'."
    developer_requirements "Quem liga para o suporte nunca diz o requisito. Diz o que deu errado."
    menu (tipo="conversa"):
        "Perguntar como ela tirava o requisito disso":
            show developer_requirements neutral
            developer_requirements "Com uma pergunta só: 'o que você estava tentando fazer?'. A resposta quase nunca é sobre a tela vermelha."
        "Perguntar se ela sente falta do suporte":
            show developer_requirements neutral
            developer_requirements "Da pressa, não. Das pessoas, um pouco. Lá eu ouvia a reclamação antes de ela virar documento."
    developer_requirements "Quando você estiver diante de um usuário bravo, lembra disso. A raiva é um mapa. Só precisa de alguém que saiba ler."
    hide developer_requirements
    return

label im_saude_fio_developer_requirements_3:
    # Dizer não com cuidado
    show developer_requirements serious at center_zoom
    "{i}[NOME_DEVELOPER_REQUIREMENTS] acaba de desligar uma chamada. Respira fundo antes de olhar para você.{/i}"
    developer_requirements "Pedido novo. Urgente, claro. E não cabe no que a gente combinou."
    developer_requirements "No começo da carreira eu dizia 'não dá' e achava que estava sendo firme. Só estava sendo porta."
    show developer_requirements thinking
    developer_requirements "Hoje eu mostro a troca. 'Se entrar isso agora, aquilo sai da entrega. Qual vale mais para você?'"
    menu (tipo="conversa"):
        "Perguntar se a pessoa não fica chateada mesmo assim":
            show developer_requirements neutral
            developer_requirements "Às vezes fica. Mas fica chateada com a escolha, não comigo. E a escolha é dela, como deve ser."
        "Perguntar o que ela faz quando a pessoa quer tudo":
            show developer_requirements neutral
            developer_requirements "Coloco tudo numa lista, na ordem que ela disser. A linha de corte aparece sozinha. Ninguém discute com uma lista que ela mesma montou."
    show developer_requirements positive
    developer_requirements "'Não dá' fecha a conversa. 'Se entrar isso, sai aquilo' abre."
    hide developer_requirements
    return


# -------------------------------
# Lucas (developer_ai)
# -------------------------------
label im_saude_fio_developer_ai_1:
    # O modelo de recaída
    show developer_ai positive at center_zoom
    developer_ai "Posso te mostrar uma ideia? Promete não rir."
    "{i}No celular dele, um rabisco: setas, caixas e a palavra RECAÍDA bem grande no meio.{/i}"
    developer_ai "Um modelo que avisa a médica antes de o paciente recair. Sono, humor, cigarros por dia. A IA olha tudo e acende um alerta."
    menu (tipo="conversa"):
        "Perguntar de onde viriam esses dados":
            show developer_ai thinking
            developer_ai "Do app, do prontuário... Bom, do prontuário que a gente ainda vai construir. Do app que ainda não manda nada."
        "Perguntar se os pacientes concordariam com isso":
            show developer_ai thinking
            developer_ai "Consentimento. Pois é. Ninguém assinou nada dizendo que o sono dele pode virar alerta."
    show developer_ai concentrated
    developer_ai "Então o primeiro passo nem é o modelo. É ter dado limpo, com permissão, por meses."
    developer_ai "Sem dado bom, IA só erra mais rápido."
    show developer_ai positive
    developer_ai "Vou guardar o rabisco. Daqui a um ano a gente conversa de novo."
    hide developer_ai
    return

label im_saude_fio_developer_ai_2:
    # IA e palavra vaga
    show developer_ai concentrated at center_zoom
    developer_ai "Fiz um teste ontem à noite. Pedi para um assistente de IA revisar uns requisitos de exemplo."
    developer_ai "Coloquei de propósito: 'O sistema deve ser rápido'. Queria ver se ela reclamava."
    show developer_ai thinking
    developer_ai "Ela respondeu: 'Ótimo requisito! Claro e objetivo.'"
    menu (tipo="conversa"):
        "Perguntar o que estava errado na frase":
            show developer_ai concentrated
            developer_ai "Rápido para quem? Fazendo o quê? Em quantos segundos? Ninguém consegue testar 'rápido'."
        "Perguntar se ele desistiu da IA por isso":
            show developer_ai positive
            developer_ai "Não! Só mudei a pergunta. Quando eu pedi 'aponte as palavras que não dá para medir', ela achou na hora."
    show developer_ai positive
    developer_ai "Ela concorda com tudo. Parece eu no primeiro mês."
    developer_ai "A ferramenta ajuda. Mas quem sabe o que perguntar ainda é a gente."
    hide developer_ai
    return

label im_saude_fio_developer_ai_3:
    # O hackathon
    show developer_ai thinking at center_zoom
    developer_ai "Você soube do hackathon? O time da [NOME_DEVELOPER_QUALITY] ganhou. De novo."
    developer_ai "O nosso app funcionava melhor. Sério. Tinha até teste automatizado."
    menu (tipo="conversa"):
        "Perguntar o que o outro time fez de diferente":
            show developer_ai concentrated
            developer_ai "Eles começaram pela dor de uma pessoa de verdade, com nome e história. Em três minutos, o júri entendeu para que servia."
        "Dizer que funcionar melhor devia contar mais":
            show developer_ai concentrated
            developer_ai "Eu também achava. Mas, se ninguém entende para que serve, ninguém chega a ver que funciona."
    show developer_ai positive
    developer_ai "Eles ensaiaram a apresentação. A gente ensaiou o código."
    developer_ai "Próxima vez eu chamo você para ensaiar com a gente. Você faz pergunta de quem não sabe nada, e isso ajuda muito."
    "{i}Você decide levar aquilo como elogio.{/i}"
    hide developer_ai
    return


# -------------------------------
# Joseph (developer_coding)
# -------------------------------
label im_saude_fio_developer_coding_1:
    # Risoto e revisão
    show developer_coding neutral at center_zoom
    developer_coding "Já fez risoto? Não aquele de pacote. O de verdade."
    developer_coding "Você não pode jogar o caldo todo de uma vez. Uma concha, mexe, espera secar. Outra concha. Quarenta minutos de atenção."
    menu (tipo="conversa"):
        "Perguntar o que risoto tem a ver com código":
            show developer_coding thinking
            developer_coding "Tudo. Revisão de código é igual. Se alguém me manda duas mil linhas de uma vez, eu não reviso. Eu passo o olho e aprovo."
        "Dizer que nunca teve paciência para cozinhar":
            show developer_coding thinking
            developer_coding "Então você vai sofrer com revisão. Brincadeira. Mais ou menos. Revisão também é de concha em concha."
    show developer_coding serious
    developer_coding "Ninguém revisa duas mil linhas. Revisa vinte, com atenção."
    developer_coding "Por isso eu peço mudança pequena. Não é chatice. É para eu conseguir ler de verdade."
    show developer_coding neutral
    developer_coding "Um dia eu levo risoto para a equipe. Aí você entende."
    hide developer_coding
    return

label im_saude_fio_developer_coding_2:
    # A sexta-feira
    show developer_coding serious at center_zoom
    developer_coding "Todo mundo aqui já me ouviu dizer 'nada de deploy na sexta à noite'. Sabe de onde veio?"
    developer_coding "Emprego antigo. Sistema de uma rede de farmácias. Sexta, oito da noite, uma mudança 'pequena' no cálculo de desconto."
    show developer_coding thinking
    developer_coding "Às nove, nenhuma farmácia fechava venda. Às dez, o gerente que aprovou estava num casamento, sem celular."
    developer_coding "Passamos o fim de semana inteiro tentando voltar a versão. Ninguém tinha ensaiado a volta."
    menu (tipo="conversa"):
        "Perguntar o que mudou depois disso":
            show developer_coding neutral
            developer_coding "Deploy de manhã, com gente acordada, e um jeito testado de desfazer. Parece óbvio. Só ficou óbvio depois."
        "Perguntar se ele ficou com medo de deploy":
            show developer_coding neutral
            developer_coding "Medo, não. Respeito. Deploy é a hora em que o código encontra gente de verdade."
    developer_coding "Desde então, sexta à noite eu só faço risoto."
    hide developer_coding
    return

label im_saude_fio_developer_coding_3:
    # Por que eu sou chato
    show developer_coding thinking at center_zoom
    developer_coding "Posso te contar uma coisa que não me orgulha?"
    developer_coding "Uns anos atrás eu tinha um estagiário. Bom, esforçado. Eu revisava o código dele com uma palavra: 'refazer'."
    developer_coding "Achava que ele ia descobrir sozinho o porquê. Em dois meses ele pediu para sair. Disse que não sabia o que eu queria."
    menu (tipo="conversa"):
        "Perguntar o que ele faz diferente hoje":
            show developer_coding serious
            developer_coding "Todo comentário meu tem um motivo. 'Troca esse nome, porque ninguém vai saber que x é a idade do paciente.'"
        "Dizer que essa conversa deve ter custado":
            show developer_coding serious
            developer_coding "Custou. Ainda custa. Mas eu prefiro contar a repetir."
    developer_coding "Crítica sem motivo é só barulho. Eu aprendi tarde."
    show developer_coding neutral
    developer_coding "Então, quando eu comentar seu código, pergunta o porquê se eu esquecer de dizer. Pode cobrar."
    hide developer_coding
    return


# -------------------------------
# Robert (developer_management)
# -------------------------------
label im_saude_fio_developer_management_1:
    # Gerente aos 28
    show developer_management thinking at center_zoom
    developer_management "Sabe quantos anos eu tinha quando virei gerente? Vinte e oito. O [NOME_DEVELOPER_CODING] programava havia mais tempo do que eu."
    developer_management "Na primeira reunião, eu quis parecer que sabia tudo. Decidi a arquitetura sozinho, em cinco minutos."
    developer_management "O [NOME_DEVELOPER_PROJECT] ficou quieto. Duas semanas depois, a gente refez tudo do jeito que ele teria sugerido."
    menu (tipo="conversa"):
        "Perguntar como ele decide hoje":
            show developer_management serious
            developer_management "Pergunto antes. Para quem entende do assunto, não para quem fala mais alto. Depois eu decido e assumo."
        "Perguntar se ainda se sente inseguro":
            show developer_management serious
            developer_management "Toda semana. A diferença é que hoje eu não escondo. Insegurança escondida vira decisão ruim."
    developer_management "Eu não sei mais que eles. Eu só sei quem sabe o quê."
    show developer_management thinking
    developer_management "E isso também é uma habilidade. Pode anotar."
    hide developer_management
    return

label im_saude_fio_developer_management_2:
    # O quadro
    show developer_management serious at center_zoom
    "{i}[NOME_DEVELOPER_MANAGEMENT] mostra no celular o quadro da equipe. Cada pessoa tem uma linha. Na coluna 'Fazendo', nunca há mais de dois cartões.{/i}"
    developer_management "Já reparou na regra? Dois cartões em andamento por pessoa. Nem um a mais."
    menu (tipo="conversa"):
        "Perguntar se isso não deixa a equipe mais lenta":
            show developer_management thinking
            developer_management "Parece. Mas faz as coisas terminarem. Quando eu deixava cada um com seis, tinha trinta cartões em andamento e nenhum pronto na sexta."
        "Perguntar o que acontece quando chega algo urgente":
            show developer_management thinking
            developer_management "Alguém para um cartão e escreve por quê. Urgência que não tira nada do lugar não é urgência, é acúmulo."
    developer_management "Se tudo está em andamento, nada está pronto."
    developer_management "E cartão parado tem nome: é bloqueio. Bloqueio a gente fala na hora, não na reunião da semana que vem."
    hide developer_management
    return

label im_saude_fio_developer_management_3:
    # O guarda-chuva
    show developer_management thinking at center_zoom
    "{i}[NOME_DEVELOPER_MANAGEMENT] guarda o celular com um suspiro. A tela ainda mostrava um e-mail com três pontos de exclamação.{/i}"
    developer_management "Diretoria do Instituto. Querem saber por que o sistema não fica pronto 'logo'."
    developer_management "Faz parte do meu trabalho receber essa chuva antes que ela chegue em vocês."
    menu (tipo="conversa"):
        "Perguntar o que ele responde para a diretoria":
            show developer_management serious
            developer_management "Números. O que está pronto, o que falta, quanto a equipe entrega por semana. Contra número, a ansiedade diminui."
        "Perguntar quem protege o próprio gerente":
            show developer_management serious
            developer_management "Boa pergunta. Corrida no domingo, e uma colega de outra empresa que escuta minhas reclamações. Recomendo as duas."
    developer_management "Prazo apertado eu negocio. Gente esgotada eu não consigo consertar."
    developer_management "Então, se a semana pesar demais para você, me fala. Isso também entra no planejamento."
    hide developer_management
    return


# -------------------------------
# Daiana (developer_quality)
# -------------------------------
label im_saude_fio_developer_quality_1:
    # Professora
    show developer_quality positive at center_zoom
    developer_quality "Antes de QA eu dava aula. Matemática, para o ensino médio. Seis turmas."
    developer_quality "Aprendi rápido que aluno com pressa pula etapa. E erra exatamente na etapa que pulou."
    menu (tipo="conversa"):
        "Perguntar por que ela trocou a sala de aula pelo software":
            show developer_quality thinking
            developer_quality "Um sistema de notas da escola fechou a média errada da turma inteira. Fui eu que achei o erro. Gostei de achar."
        "Perguntar se ela ainda pensa como professora":
            show developer_quality thinking
            developer_quality "O tempo todo. Toda vez que alguém diz 'era óbvio', eu penso: óbvio para quem?"
    show developer_quality serious
    developer_quality "Meus checklists são isso. Uma aula curta para quem não tem tempo de assistir à aula inteira."
    show developer_quality positive
    developer_quality "Checklist é aula para quem está com pressa."
    developer_quality "Te mando o meu de revisão de requisitos. Tem doze itens. O décimo segundo é 'releia o primeiro'."
    hide developer_quality
    return

label im_saude_fio_developer_quality_2:
    # O pudim
    show developer_quality positive at center_zoom
    developer_quality "Você já sabe da tradição? Quem conta o melhor bug do mês ganha pudim. Feito por mim."
    developer_quality "E o recorde ainda é meu. Quer ouvir?"
    "{i}Ela não espera resposta.{/i}"
    developer_quality "Um sistema de agendamento aceitou consulta no dia 30 de fevereiro. Por dois anos."
    show developer_quality thinking
    developer_quality "Os pacientes recebiam a confirmação, apareciam no dia 2 de março, e ninguém tinha a consulta marcada."
    menu (tipo="conversa"):
        "Perguntar como ninguém percebeu por dois anos":
            show developer_quality serious
            developer_quality "Porque ninguém testou uma data impossível. Todo mundo testou o que esperava que o usuário digitasse."
        "Perguntar como ela achou o erro":
            show developer_quality serious
            developer_quality "Lendo a regra de data. Ela dizia 'dia entre 1 e 31'. Só isso. Mais nada."
    developer_quality "Ninguém tinha escrito que não podia."
    show developer_quality positive
    developer_quality "Se você achar um melhor, o pudim é seu. Mas eu aviso: a régua está alta."
    hide developer_quality
    return

label im_saude_fio_developer_quality_3:
    # Qualidade não é fase
    show developer_quality serious at center_zoom
    developer_quality "Sabe por que eu vou nas reuniões desde a entrevista com as médicas? Muita gente acha que eu só devia aparecer na semana de testes."
    developer_quality "Num emprego antigo eu só aparecia lá. Recebia o sistema pronto e uma lista de requisitos que ninguém conseguia testar."
    show developer_quality thinking
    developer_quality "Eu encontrava o problema. E ouvia: 'agora não dá mais para mudar'."
    menu (tipo="conversa"):
        "Perguntar o que ela faz nas reuniões do começo":
            show developer_quality serious
            developer_quality "Uma pergunta só, repetida: 'como a gente vai saber que isso está certo?'. Se ninguém sabe responder, o requisito ainda não está pronto."
        "Perguntar se a equipe estranhou no começo":
            show developer_quality positive
            developer_quality "Estranhou. Até o primeiro mês sem bug grave em produção. Depois, começaram a me chamar."
    developer_quality "Qualidade não é a última etapa. É o jeito de fazer todas."
    hide developer_quality
    return


# -------------------------------
# Heitor (developer_project)
# -------------------------------
label im_saude_fio_developer_project_1:
    # O guardanapo
    show developer_project thinking at center_zoom
    "{i}[NOME_DEVELOPER_PROJECT] desenha num guardanapo de papel. Duas caixas, uma linha entre elas, um traço e um tridente na ponta.{/i}"
    "{i}Ele vira o guardanapo para você e espera.{/i}"
    menu (tipo="conversa"):
        "Perguntar o que é o tridente":
            show developer_project confident
            developer_project "'Muitos'. Um paciente, muitos atendimentos."
        "Perguntar por que só duas caixas":
            show developer_project confident
            developer_project "Porque é o que importa primeiro. O resto vem pendurado nelas."
    developer_project "Paciente tem muitos atendimentos. Atendimento tem um paciente. O resto é detalhe."
    "{i}Ele acrescenta uma terceira caixa, 'Escala', ligada a 'Atendimento'. Olha para você de novo.{/i}"
    developer_project "Uma escala por atendimento? Ou várias?"
    "{i}Você pensa um pouco e responde que, numa consulta, a médica pode aplicar mais de uma. Ele desenha outro tridente.{/i}"
    developer_project "Isso. Pode ficar com o guardanapo."
    hide developer_project
    return

label im_saude_fio_developer_project_2:
    # Versionar o histórico
    show developer_project serious at center_zoom
    developer_project "Pergunta. Se a médica corrige o peso do paciente, o que o sistema faz com o peso antigo?"
    menu (tipo="conversa"):
        "Responder que troca pelo valor novo":
            developer_project "É o que quase todo sistema faz. E é o erro."
        "Responder que guarda os dois":
            show developer_project confident
            developer_project "Isso. Guarda os dois, com data e com quem mudou."
    show developer_project serious
    developer_project "Prontuário não se sobrescreve. Cada mudança vira uma versão nova. A antiga continua lá."
    developer_project "Se alguém perguntar daqui a um ano 'o que a médica sabia naquele dia?', a resposta tem que existir."
    developer_project "Em prontuário, apagar é mentir sobre o passado."
    "{i}Ele volta para a tela. Para [NOME_DEVELOPER_PROJECT], foi uma conversa longa.{/i}"
    hide developer_project
    return

label im_saude_fio_developer_project_3:
    # Falar pouco
    show developer_project thinking at center_zoom
    "{i}[NOME_DEVELOPER_PROJECT] tira do bolso um tabuleiro de xadrez dobrável, com uma partida pela metade.{/i}"
    menu (tipo="conversa"):
        "Perguntar se ele joga muito":
            developer_project "Jogava. Campeonato, na adolescência. Hoje é só uma partida por semana, por correspondência."
        "Perguntar de quem é a vez":
            show developer_project confident
            developer_project "Minha. Há três dias."
    developer_project "Xadrez ensina uma coisa. Cada lance muda o tabuleiro inteiro. Então você pensa antes de mexer."
    show developer_project serious
    developer_project "Em reunião é igual. Cada palavra que eu digo numa reunião vira tarefa de alguém."
    developer_project "Por isso eu falo pouco. Não é timidez. É cuidado."
    "{i}Ele move um bispo, anota o lance num papelzinho e, pela primeira vez, sorri.{/i}"
    hide developer_project
    return


# -------------------------------
# Mateus (developer_security)
# -------------------------------
label im_saude_fio_developer_security_1:
    # Devagar
    show developer_security serious at center_zoom
    "{i}[NOME_DEVELOPER_SECURITY] fala devagar, como quem escolhe cada palavra.{/i}"
    developer_security "As pessoas acham que eu sou lento. Não sou. Eu sou devagar de propósito."
    developer_security "No meu primeiro incidente, um servidor foi invadido. Todo mundo correu para 'limpar' a máquina."
    show developer_security thinking
    developer_security "Reiniciaram, apagaram arquivos estranhos, trocaram senhas. Em uma hora, o servidor estava limpo."
    developer_security "E a gente nunca soube por onde a pessoa entrou."
    menu (tipo="conversa"):
        "Perguntar o que devia ter sido feito":
            show developer_security serious
            developer_security "Primeiro isolar e copiar tudo. Depois investigar. Só no fim, limpar. A ordem importa."
        "Perguntar se a invasão se repetiu":
            show developer_security serious
            developer_security "Três semanas depois. Pelo mesmo lugar."
    developer_security "Em incidente, quem corre apaga a prova."
    hide developer_security
    return

label im_saude_fio_developer_security_2:
    # O bonsai
    show developer_security thinking at center_zoom
    "{i}[NOME_DEVELOPER_SECURITY] mostra no celular a foto de um bonsai pequeno, com uma tesoura minúscula ao lado. Fica na mesa dele, lá em cima.{/i}"
    developer_security "Doze anos. Era do meu avô."
    developer_security "Toda semana eu tiro um ou dois galhos. Se eu esqueço um mês, ele cresce torto e não volta mais."
    menu (tipo="conversa"):
        "Perguntar se dá para comparar com o trabalho dele":
            show developer_security serious
            developer_security "Dá. Permissão de acesso cresce igual. Alguém precisa de acesso por uma semana, e ninguém tira depois."
        "Perguntar se ele não fica com pena de cortar":
            show developer_security serious
            developer_security "No começo, sim. Mas o galho que eu não corto rouba força do resto. Com acesso esquecido é a mesma coisa."
    developer_security "Permissão é igual galho: se ninguém poda, cresce para onde não devia."
    developer_security "Cada pessoa com o mínimo que precisa para o trabalho dela. Nem um galho a mais."
    hide developer_security
    return

label im_saude_fio_developer_security_3:
    # A planilha no e-mail
    show developer_security serious at center_zoom
    developer_security "Você deve ter reparado que eu insisto muito em dado de paciente. Vou te contar por quê."
    developer_security "Emprego antigo. Uma colega mandou uma planilha para o e-mail errado. Nome, telefone, diagnóstico. Quatrocentas pessoas."
    show developer_security thinking
    developer_security "Ninguém fez por mal. O nome do destinatário era parecido. O sistema completou sozinho."
    developer_security "Eu ajudei a ligar para cada paciente para avisar. Levamos duas semanas."
    menu (tipo="conversa"):
        "Perguntar o que ele aprendeu com as ligações":
            show developer_security serious
            developer_security "Que dado tem voz. Uma senhora me perguntou se o patrão dela ia ver. Eu não sabia responder."
        "Perguntar o que mudou na empresa depois":
            show developer_security serious
            developer_security "Planilha de paciente parou de sair por e-mail. Devia ter sido sempre assim."
    developer_security "Do outro lado de cada linha tem alguém que confiou na gente."
    hide developer_security
    return


# -------------------------------
# César (developer_test)
# -------------------------------
label im_saude_fio_developer_test_1:
    # Corrida
    show developer_test enthusiastic at center_zoom
    developer_test "Hoje corri dez quilômetros antes das seis da manhã! E achei dois casos de teste no caminho."
    menu (tipo="conversa"):
        "Perguntar como se acha caso de teste correndo":
            show developer_test confident
            developer_test "Correndo a cabeça fica solta. Aí eu imagino alguém usando o sistema e penso no contrário do que essa pessoa devia fazer."
        "Perguntar se ele não prefere dormir mais":
            show developer_test confident
            developer_test "Prefiro! Mas o meu cérebro pensa melhor depois do quinto quilômetro. Antes disso é só sofrimento."
    show developer_test thinking
    developer_test "Hoje foi: e se a médica abrir o mesmo paciente em duas abas e salvar nas duas? Qual vale?"
    developer_test "Ninguém pensou nisso ainda. Agora tem um teste com o nome dela."
    show developer_test enthusiastic
    developer_test "Correndo eu penso: e se o usuário fizer o contrário?"
    hide developer_test
    return

label im_saude_fio_developer_test_2:
    # A base apagada
    show developer_test serious at center_zoom
    developer_test "Já te contei que eu apaguei uma base de dados? Pela metade, na verdade. Mas parece que foi inteira."
    developer_test "Achei que era a base de testes. Era a de produção. Os dois terminais eram idênticos."
    show developer_test thinking
    developer_test "Eu lembro do silêncio. Uns cinco segundos olhando para a tela, sem respirar."
    menu (tipo="conversa"):
        "Perguntar como eles recuperaram":
            show developer_test serious
            developer_test "Backup da noite anterior. Perdemos meio dia de cadastros. Eu liguei para cada pessoa que tinha cadastrado alguma coisa."
        "Perguntar se ele levou bronca":
            show developer_test serious
            developer_test "O chefe só perguntou: 'o que a gente muda para isso não acontecer de novo?'. Foi pior que bronca."
    developer_test "Hoje produção tem fundo vermelho no meu terminal. Aprendi do pior jeito."
    show developer_test confident
    developer_test "Hoje eu conto rindo. Na época, nem um pouco."
    hide developer_test
    return

label im_saude_fio_developer_test_3:
    # Quem quebra
    show developer_test enthusiastic at center_zoom
    developer_test "Quer saber meu teste favorito? Idade: duzentos anos."
    developer_test "CPF com letras. Nome com emoji. Data de nascimento no ano que vem. Colar um texto de três páginas no campo 'telefone'."
    menu (tipo="conversa"):
        "Perguntar se alguém de verdade faria isso":
            show developer_test confident
            developer_test "Faria! Não de propósito. A pessoa cola o que estava na área de transferência. O gato pisa no teclado."
        "Perguntar se ele não está procurando problema":
            show developer_test confident
            developer_test "Estou! É exatamente isso. Melhor eu achar agora do que a médica achar com o paciente na frente dela."
    show developer_test thinking
    developer_test "O caminho feliz todo mundo testa. Eu fico com o caminho bagunçado."
    developer_test "Usuário não lê manual. Usuário aperta tudo."
    hide developer_test
    return


# -------------------------------
# Dra. Nathalia (doutora_2)
# -------------------------------
label im_saude_fio_doutora_2_1:
    # Por que o tabagismo
    show doutora_2 neutral at center_zoom
    doutora_2 "Você quer saber por que eu escolhi tabagismo? Todo mundo pergunta. Não é a área mais charmosa."
    doutora_2 "Meu avô parou de fumar sete vezes. Sete. A família inteira já tinha desistido de acreditar."
    show doutora_2 positive at center_zoom
    doutora_2 "Na sétima, deu certo. Sabe o que mudou? Uma enfermeira do posto ligava para ele toda semana. Só para perguntar como estava."
    menu (tipo="conversa"):
        "Perguntar se ele chegou a saber que ela virou médica por isso":
            doutora_2 "Soube. Foi na minha formatura, sem cigarro no bolso. Chorou mais que eu."
        "Perguntar o que aquela enfermeira fazia de especial":
            doutora_2 "Não esquecia dele. Só isso. Parece pouco. Para quem está tentando parar, é quase tudo."
    show doutora_2 serious at center_zoom
    doutora_2 "Parar de fumar é a coisa mais difícil que eu já vi alguém tentar."
    doutora_2 "Então, quando eu peço um sistema que lembre dos pacientes, não é capricho. É aquela ligação de toda semana."
    hide doutora_2
    return

label im_saude_fio_doutora_2_2:
    # O café do plantão
    show doutora_2 neutral at center_zoom
    "{i}A [NOME_DOUTORA_2] segura uma caneca enorme de café com as duas mãos.{/i}"
    doutora_2 "Plantão de vinte e quatro horas ontem. Esta é a quarta caneca. Não conta para ninguém."
    doutora_2 "Sabe o que acontece no plantão? Eu esqueço de almoçar. Esqueço de beber água. E, às vezes, esqueço um exame pendente."
    menu (tipo="conversa"):
        "Perguntar como ela faz para não esquecer hoje":
            doutora_2 "Post-it no monitor. Lembrete no celular. E sorte. A sorte é a parte que me preocupa."
        "Perguntar se foi por isso que ela pediu notificações":
            doutora_2 "Foi. A [NOME_DOUTORA_1] acha que é pressa minha. É cansaço. Cansaço não lembra de nada."
    show doutora_2 serious at center_zoom
    doutora_2 "No plantão eu esqueço até de almoçar. O sistema não pode depender da minha memória."
    doutora_2 "Agora vou tomar esse café antes que esfrie. Esse eu não esqueço nunca."
    hide doutora_2
    return

label im_saude_fio_doutora_2_3:
    # A tela verdinha
    show doutora_2 neutral at center_zoom
    doutora_2 "Lembra quando eu pedi a tela verdinha, de brincadeira? Tenho um lado sério dessa piada."
    doutora_2 "O Dr. Paulo, aqui do Instituto, é daltônico. Vermelho e verde, para ele, são quase a mesma cor."
    doutora_2 "No sistema antigo, paciente atrasado ficava com o nome em vermelho. Só isso. Nenhum texto."
    menu (tipo="conversa"):
        "Perguntar como ele se virava":
            doutora_2 "Pedia para a recepção ler a lista para ele. Todo dia. Ele nunca reclamou. A gente é que demorou a perceber."
        "Perguntar o que ela gostaria no lugar":
            doutora_2 "Uma palavra do lado do nome. 'Atrasado'. 'Exame pendente'. A cor pode continuar, mas não pode ser a única coisa."
    doutora_2 "Se o aviso for só cor, o Dr. Paulo não vê. Escreve o que é."
    doutora_2 "Pode deixar verdinha a tela inicial, se quiser. Mas o aviso, escreve."
    hide doutora_2
    return


# -------------------------------
# Descansar (§3.4). Valem para qualquer semana.
# -------------------------------
label im_saude_descansar_cafe:
    "{i}Você passa um café na cafeteira de vidro e se senta na banqueta perto da janela.{/i}"
    if im_semana_atual == 4:
        "{i}A copa está cheia de gente voltando do almoço. Você acha um canto e espera o movimento passar.{/i}"
    "{i}O barulho da cafeteira, o cheiro do pó fresco, a luz entrando de lado. Por alguns minutos, ninguém precisa de nada seu.{/i}"
    if energia_cansaco():
        "{i}Você quase cochila na banqueta. Alguém deixa uma xícara do seu lado e não diz nada.{/i}"
    "{i}Quando a xícara esvazia, a cabeça parece mais leve.{/i}"
    return

label im_saude_descansar_praca:
    "{i}Você atravessa a rua e escolhe o banco à sombra de uma palmeira-imperial.{/i}"
    if im_semana_atual == 4:
        "{i}A praça está cheia de gente do campus com marmita no colo. Mesmo assim, o seu banco continua livre.{/i}"
    "{i}O vento vem da baía. Um bem-te-vi canta no galho de cima, insistente, como se cobrasse alguma coisa.{/i}"
    if energia_cansaco():
        "{i}Você fecha os olhos por dez minutos e acorda com o celular vibrando no bolso. Era só o grupo da equipe mandando meme.{/i}"
    "{i}Você volta andando devagar, sem pressa de chegar.{/i}"
    return
