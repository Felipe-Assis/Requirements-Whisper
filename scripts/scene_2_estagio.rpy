define sabrina = Character("Sabrina · mentora", color="#b9dbe9")
define carlos = Character("Carlos · usuário", color="#e8cba4")

default mission_score = 0
default mission_elicitation = False
default mission_ambiguity = False
default mission_acceptance = False
default mission_edge_case = False
default mission_edge_criterion = ""
default mission_complete = False
default mission_context = ""
default mission_request = ""
default mission_problem = ""
default mission_rule = ""
default mission_criterion = ""

label scene_2_estagio:
    $ mission_score = 0
    $ mission_elicitation = False
    $ mission_ambiguity = False
    $ mission_acceptance = False
    $ mission_edge_case = False
    $ mission_edge_criterion = ""
    $ mission_complete = False
    scene bg escritorio
    with dissolve
    show sabrina neutral at colleague_left
    show carlos thinking at colleague_right
    with dissolve

    if chosen_job == "IDT-UFRJ":
        $ mission_context = "reservas de equipamentos do laboratório"
        $ mission_request = "Precisamos de um jeito fácil de reservar os equipamentos."
        $ mission_problem = "Ontem duas pessoas chegaram para usar o mesmo microscópio às 14h. As duas tinham anotado a reserva em planilhas diferentes."
        $ mission_rule = "Não pode haver duas reservas confirmadas para o mesmo equipamento em horários que se sobrepõem."
        $ mission_criterion = "Dada uma reserva confirmada das 14h às 15h, quando outra pessoa solicitar o mesmo equipamento das 14h30 às 15h30, o sistema deve recusar a segunda reserva e informar o conflito."
    elif chosen_job == "Startup":
        $ mission_context = "registro de gastos de estudantes"
        $ mission_request = "Precisamos de um jeito fácil de controlar os gastos."
        $ mission_problem = "Anotei duas vezes o mesmo almoço sem perceber. Quando o total ficou alto, não consegui descobrir de onde ele veio."
        $ mission_rule = "A pessoa deve poder excluir um gasto lançado por engano, com uma confirmação antes da exclusão, e ver o total atualizado."
        $ mission_criterion = "Dado um total mensal de R$ 100 com um gasto de R$ 20, quando a pessoa confirmar a exclusão desse gasto, ele deve sair da lista e o total deve passar a R$ 80."
    else:
        $ mission_context = "acompanhamento de chamados de suporte"
        $ mission_request = "Precisamos de um jeito fácil de acompanhar os chamados."
        $ mission_problem = "Telefonei três vezes para saber se meu chamado tinha sido resolvido. A equipe respondeu cada vez uma coisa, porque ninguém registrou a mudança."
        $ mission_rule = "Quando o suporte resolver um chamado, a pessoa solicitante deve poder consultar o estado Resolvido e a descrição da solução."
        $ mission_criterion = "Dado um chamado Em atendimento, quando o suporte registrar uma solução e mudar seu estado para Resolvido, a consulta da pessoa solicitante deve mostrar Resolvido e o texto registrado."

    sabrina "Bom dia, [player_name]! Sou Sabrina. Vou acompanhar seu estágio por aqui."
    sabrina "Sua primeira tarefa é investigar um pedido sobre [mission_context]. Carlos usa esse processo no dia a dia."
    "Você abre o notebook. O cursor pisca sobre uma página em branco."
    sabrina "Não precisa chegar com a solução pronta. Hoje queremos descobrir qual problema vale resolver."
    carlos "[mission_request]"
    sabrina "Vamos tomar quatro decisões: investigar o problema, esclarecer uma ambiguidade, combinar como verificar a entrega e explorar um caso limite."
    sabrina "Cada escolha recebe um comentário. Se precisar de ajuda, você poderá revisar antes de continuar."

label mission_elicitation_choice:
    menu:
        "1 de 4 · Como você começa a conversa?"
        "Pergunto qual tecnologia a equipe prefere usar.":
            sabrina "A tecnologia importa para construir a solução, mas ainda não sabemos o que precisa mudar para Carlos."
            sabrina "Sem entender o trabalho atual, podemos entregar uma tela nova que mantém o mesmo problema."
        "Peço que Carlos conte uma situação recente em que isso deu errado.":
            $ mission_elicitation = True
            $ mission_score += 1
            sabrina "Um episódio concreto ajuda a descobrir quem enfrenta o problema, o que acontece e qual é a consequência."
        "Confirmo se Carlos gostaria de uma tela com menos botões.":
            sabrina "Talvez menos botões ajudem, mas essa pergunta já sugere uma solução. Carlos pode concordar sem revelar a dificuldade real."
            sabrina "Uma pergunta aberta deixa espaço para descobrir algo que ainda não imaginamos."

    if not mission_elicitation:
        menu:
            "Como você reformula a pergunta?"
            "Carlos, você pode contar a última vez em que isso atrapalhou sua rotina?":
                sabrina "Agora temos uma pergunta sobre a experiência dele. Vamos ouvir antes de propor."

    show carlos serious at colleague_right
    carlos "[mission_problem]"
    "Você registra o episódio, as pessoas envolvidas e o efeito do problema."
    sabrina "Isso é elicitação de requisitos: buscar e compreender as necessidades das pessoas envolvidas. Esta conversa é uma das formas de fazer isso."

label mission_ambiguity_choice:
    show sabrina thinking at colleague_left
    carlos "Se o sistema fosse fácil, isso não aconteceria."
    menu:
        "2 de 4 · O que fazer com a palavra 'fácil'?"
        "Registro 'o sistema deve ser fácil' e deixo a equipe decidir o significado.":
            sabrina "A equipe pode interpretar 'fácil' de um jeito e Carlos de outro. Precisamos tornar essa expectativa mais clara."
        "Troco 'fácil' por 'moderno', para orientar o desenho das telas.":
            sabrina "'Moderno' também permite interpretações diferentes. Trocar o adjetivo não esclarece o resultado esperado."
        "Pergunto o que Carlos precisa conseguir fazer nessa situação.":
            $ mission_ambiguity = True
            $ mission_score += 1
            sabrina "Você ligou o pedido a uma tarefa e a um resultado. Agora podemos negociar um comportamento observável."

    if not mission_ambiguity:
        menu:
            "Como você esclarece a necessidade?"
            "O que precisa acontecer para evitar o problema que você contou?":
                sabrina "Vamos registrar a resposta e confirmar se entendemos."

    carlos "[mission_rule]"
    sabrina "Essa regra resolve uma parte concreta do problema. Ainda não prova que o sistema inteiro será fácil de usar."
    sabrina "Para avaliar facilidade de uso, depois precisaremos observar pessoas realizando tarefas e combinar critérios com elas."
    "Você lê a regra de volta para Carlos."
    carlos "É isso. Começar por essa situação já ajudaria bastante."

label mission_acceptance_choice:
    sabrina "Antes de passar o pedido para desenvolvimento, precisamos combinar como verificar esse comportamento."
    if chosen_job == "IDT-UFRJ":
        menu:
            "3 de 4 · Qual critério verifica a regra combinada?"
            "O calendário deve ter cores agradáveis e aparência profissional.":
                sabrina "Isso fala de aparência, mas não verifica se duas reservas conflitantes serão aceitas."
            "Uma reserva das 14h às 15h deve impedir outra do mesmo equipamento das 14h30 às 15h30.":
                $ mission_acceptance = True
                $ mission_score += 1
                sabrina "Há um estado inicial, uma ação e um resultado verificável. É um exemplo de critério de aceitação."
            "A pessoa responsável deve gostar da tela de reservas.":
                sabrina "A opinião da pessoa responsável importa, mas esse critério não mostra como verificar a regra de conflito."
    elif chosen_job == "Startup":
        menu:
            "3 de 4 · Qual critério verifica a regra combinada?"
            "Ao confirmar a exclusão de um gasto de R$ 20 de um total de R$ 100, a lista e o total devem refletir R$ 80.":
                $ mission_acceptance = True
                $ mission_score += 1
                sabrina "Há dados iniciais, uma ação e um resultado verificável. É um exemplo de critério de aceitação."
            "O aplicativo deve ter um painel moderno de educação financeira.":
                sabrina "Esse painel pode ser útil, mas não verifica a exclusão nem o cálculo do total que combinamos."
            "O botão Excluir deve ficar visível na lista de gastos.":
                sabrina "Isso verifica que existe um botão, mas não o que acontece com o gasto e o total após a confirmação."
    else:
        menu:
            "3 de 4 · Qual critério verifica a regra combinada?"
            "A pessoa solicitante deve receber atendimento de qualidade.":
                sabrina "É um objetivo importante, mas ainda precisamos definir o que observar no sistema para verificar a entrega."
            "O suporte deve conseguir clicar no botão Resolver.":
                sabrina "Conseguir clicar não garante que a pessoa solicitante verá o estado e a solução registrados."
            "Após o suporte resolver o chamado com uma descrição, a consulta deve mostrar Resolvido e essa descrição.":
                $ mission_acceptance = True
                $ mission_score += 1
                sabrina "Há uma ação do suporte e um resultado que a pessoa solicitante pode conferir. É um exemplo de critério de aceitação."

    if not mission_acceptance:
        menu:
            "O que falta para verificar o comportamento?"
            "Registrar a situação inicial, a ação e o resultado esperado.":
                sabrina "Vamos aplicar essa estrutura ao exemplo de Carlos."

    sabrina "Nossa primeira condição de aceitação fica assim:"
    "[mission_criterion]"
    show carlos confident at colleague_right
    carlos "Com esse exemplo, consigo conferir se vocês entenderam o que preciso."
    sabrina "Um exemplo não cobre tudo. Vamos investigar uma situação que ainda pode mudar o comportamento esperado."

label mission_edge_case_choice:
    if chosen_job == "IDT-UFRJ":
        carlos "E se uma reserva terminar às 15h e a outra começar exatamente às 15h?"
        menu:
            "4 de 4 · Como tratar reservas consecutivas?"
            "Permito sempre, porque os horários não se sobrepõem.":
                sabrina "Isso segue a primeira regra, mas pode ignorar a preparação do equipamento. Vamos confirmar essa necessidade antes."
            "Pergunto se é necessário um intervalo de preparação.":
                $ mission_edge_case = True
                $ mission_score += 1
                sabrina "Você identificou uma dúvida de domínio. A resposta pode mudar a regra, então precisamos conversar com quem conhece o processo."
            "Bloqueio o equipamento pelo resto do dia para garantir.":
                sabrina "Esse bloqueio reduziria a disponibilidade sem uma necessidade confirmada. Vamos descobrir qual intervalo é realmente necessário."
        carlos "Para esse microscópio, o laboratório exige dez minutos de preparação entre reservas. Ainda não tínhamos falado disso."
        $ mission_edge_criterion = "Para esse microscópio, uma reserva que termina às 15h só permite a próxima a partir das 15h10; uma solicitação às 15h deve ser recusada."
        sabrina "A regra inicial de não sobrepor horários precisa desse complemento. Vamos confirmar também se outros equipamentos exigem intervalos diferentes."
    elif chosen_job == "Startup":
        carlos "E se eu tocar em Excluir e depois cancelar na confirmação?"
        menu:
            "4 de 4 · O que verificar no cancelamento?"
            "O gasto some, mas o total só muda quando eu abrir a tela novamente.":
                sabrina "Cancelar deve desistir da operação. Remover o gasto mesmo assim contrariaria a confirmação que combinamos."
            "A janela fecha; não é preciso conferir a lista nem o total.":
                sabrina "Fechar a janela não garante que os dados ficaram intactos. Precisamos conferir o estado do gasto e do total."
            "O gasto permanece e o total não muda; confirmo isso com Carlos.":
                $ mission_edge_case = True
                $ mission_score += 1
                sabrina "Você verificou o efeito de desistir da ação, além do caminho de confirmação."
        carlos "Isso. Se eu cancelar, quero manter o gasto e o total como estavam."
        $ mission_edge_criterion = "Com total de R$ 100 e um gasto de R$ 20, cancelar a exclusão deve manter o gasto na lista e o total em R$ 100."
    else:
        carlos "E se o suporte tentar resolver o chamado sem explicar a solução?"
        menu:
            "4 de 4 · Como tratar a descrição vazia?"
            "Confirmo se devemos impedir a mudança e pedir uma descrição.":
                $ mission_edge_case = True
                $ mission_score += 1
                sabrina "Você propôs uma validação e a levou para confirmação. Assim, a regra não fica a cargo de quem implementar."
            "Preencho automaticamente com 'Resolvido', para não atrasar o suporte.":
                sabrina "Repetir o estado não explica a solução. Vamos confirmar o que é necessário para encerrar um chamado."
            "Mudo o estado e deixo a descrição para uma ligação posterior.":
                sabrina "Isso manteria a dependência das ligações que Carlos quer evitar. Vamos esclarecer a regra para esse caso."
        carlos "Precisamos da descrição antes de resolver. Se estiver vazia, mantenha Em atendimento e avise o suporte para preenchê-la."
        $ mission_edge_criterion = "Se a descrição estiver vazia, a tentativa de resolver deve manter o chamado Em atendimento e mostrar uma orientação para preencher a solução."

    if not mission_edge_case:
        menu:
            "Como você incorpora a revisão?"
            "Registro o caso limite e confirmo o resultado esperado com Carlos.":
                sabrina "Agora essa situação também faz parte do acordo."
    "Caso limite confirmado: [mission_edge_criterion]"
    sabrina "Buscar exceções cedo evita que uma regra pareça completa só porque funciona no exemplo mais simples."

label mission_review:
    $ mission_complete = True
    show sabrina enthusiastic at colleague_left
    show carlos enthusiastic at colleague_right
    sabrina "Você concluiu a primeira conversa de requisitos. Vamos revisar o que aconteceu."
    "Escolhas adequadas antes do feedback: [mission_score] de 4. As revisões orientadas não acrescentam pontos."
    if mission_elicitation:
        "Elicitação · Você começou por um episódio concreto, antes de sugerir uma solução."
    else:
        "Elicitação · Com apoio, você reformulou a pergunta para investigar um episódio concreto. Na próxima conversa, comece pela experiência da pessoa."
    if mission_ambiguity:
        "Ambiguidade · Você transformou 'fácil' em uma conversa sobre tarefa e resultado."
    else:
        "Ambiguidade · Com apoio, você esclareceu o que 'fácil' deveria permitir. Evite encerrar requisitos com adjetivos sem um significado combinado."
    if mission_acceptance:
        "Aceitação · Você escolheu uma condição com um resultado que pode ser conferido."
    else:
        "Aceitação · Com apoio, você relacionou situação inicial, ação e resultado esperado. Verifique o comportamento completo, não apenas a presença de um botão."
    if mission_edge_case:
        "Caso limite · Você considerou uma situação além do caminho principal e confirmou o comportamento esperado."
    else:
        "Caso limite · Com apoio, você incluiu uma situação que o primeiro exemplo não cobria. Pergunte também o que acontece nas exceções."
    sabrina "Guarde esta sequência: investigar a necessidade, esclarecer o significado e combinar como verificar, incluindo as exceções."
    carlos "Obrigado por ouvir antes de começar a construir. É um bom começo."
    "A página já não está em branco. Há um problema, uma regra confirmada, exemplos de verificação e um caso limite confirmado."

    menu:
        "Fim da primeira missão · O que você quer fazer?"
        "Planejar a primeira entrega (atividade opcional)":
            call scene_3_planejamento
            jump mission_review_actions
        "Rever o requisito e o critério combinados":
            "Problema relatado: [mission_problem]"
            "Regra confirmada: [mission_rule]"
            "Critério de aceitação: [mission_criterion]"
            "Caso limite: [mission_edge_criterion]"
            jump mission_review_actions
        "Refazer a missão neste contexto":
            jump scene_2_estagio
        "Experimentar outra vaga":
            call escolher_vaga(explorar=True)
            jump scene_2_estagio
        "Encerrar e voltar ao menu principal":
            return

label mission_review_actions:
    menu:
        "O registro está pronto para a próxima conversa."
        "Rever o requisito e o critério combinados":
            "Problema relatado: [mission_problem]"
            "Regra confirmada: [mission_rule]"
            "Critério de aceitação: [mission_criterion]"
            "Caso limite: [mission_edge_criterion]"
            jump mission_review_actions
        "Planejar a primeira entrega (atividade opcional)":
            call scene_3_planejamento
            jump mission_review_actions
        "Refazer a missão neste contexto":
            jump scene_2_estagio
        "Experimentar outra vaga":
            call escolher_vaga(explorar=True)
            jump scene_2_estagio
        "Encerrar e voltar ao menu principal":
            return
