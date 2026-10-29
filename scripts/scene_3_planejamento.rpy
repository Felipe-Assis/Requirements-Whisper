default planning_selected = []
default planning_complete = False
default planning_coverage = 0
default planning_used = 0
default planning_items = []
default planning_missing = []

label scene_3_planejamento:
    $ planning_selected = []
    $ planning_complete = False
    $ planning_coverage = 0
    $ planning_missing = []
    if chosen_job == "IDT-UFRJ":
        $ planning_items = ["Impedir reservas com horários sobrepostos", "Aplicar os dez minutos de preparação do microscópio", "Oferecer temas de cores para o calendário", "Exportar um relatório mensal de utilização"]
    elif chosen_job == "Startup":
        $ planning_items = ["Confirmar a exclusão e manter o gasto se houver cancelamento", "Atualizar a lista e recalcular o total após excluir", "Criar medalhas por frequência de uso", "Compartilhar um resumo de gastos nas redes sociais"]
    else:
        $ planning_items = ["Mostrar o estado e a solução na consulta do solicitante", "Impedir resolução sem descrição da solução", "Oferecer temas de cores para o painel", "Exportar um relatório mensal de chamados"]

    show sabrina thinking at colleague_left
    sabrina "Agora vamos planejar uma primeira entrega com o que você descobriu."
    sabrina "Neste exercício, temos capacidade para dois itens. Cada item custa um ponto fictício; isso não é uma estimativa de esforço de um projeto real."
    sabrina "Na prática, a equipe precisaria discutir tamanho, dependências, riscos e capacidade antes de assumir um compromisso."
    carlos "Para esta rodada, quero resolver primeiro o problema que relatei, incluindo o caso limite que confirmamos."
    sabrina "Escolha dois dos quatro itens. Você pode retirar escolhas e revisar o plano sem perder pontos. Não há nota nesta atividade."
    "Necessidade confirmada: [mission_rule]"
    "Caso limite: [mission_edge_criterion]"

label planning_select:
    $ planning_used = len(planning_selected)
    menu:
        "Plano da entrega · [planning_used]/2 pontos usados · Cada item custa 1"
        "Adicionar: [planning_items[0]]" if 0 not in planning_selected and planning_used < 2:
            $ planning_selected.append(0)
            jump planning_select
        "Adicionar: [planning_items[1]]" if 1 not in planning_selected and planning_used < 2:
            $ planning_selected.append(1)
            jump planning_select
        "Adicionar: [planning_items[2]]" if 2 not in planning_selected and planning_used < 2:
            $ planning_selected.append(2)
            jump planning_select
        "Adicionar: [planning_items[3]]" if 3 not in planning_selected and planning_used < 2:
            $ planning_selected.append(3)
            jump planning_select
        "Retirar: [planning_items[0]]" if 0 in planning_selected:
            $ planning_selected.remove(0)
            jump planning_select
        "Retirar: [planning_items[1]]" if 1 in planning_selected:
            $ planning_selected.remove(1)
            jump planning_select
        "Retirar: [planning_items[2]]" if 2 in planning_selected:
            $ planning_selected.remove(2)
            jump planning_select
        "Retirar: [planning_items[3]]" if 3 in planning_selected:
            $ planning_selected.remove(3)
            jump planning_select
        "Conferir este plano" if planning_used == 2:
            jump planning_feedback
        "Voltar ao resumo da missão":
            return

label planning_feedback:
    $ planning_complete = True
    $ planning_coverage = sum(1 for item in planning_selected if item in (0, 1))
    $ planning_missing = [planning_items[item] for item in (0, 1) if item not in planning_selected]
    "Seu plano inclui: [planning_items[planning_selected[0]]] e [planning_items[planning_selected[1]]]."
    if planning_coverage == 2:
        show sabrina enthusiastic at colleague_left
        sabrina "Esse recorte cobre as duas partes necessárias para a entrega que Carlos pediu: o comportamento principal e a proteção que combinamos."
        carlos "Consigo relacionar os dois itens ao problema que contei. Vamos usar nossos critérios para verificar a entrega."
    elif planning_coverage == 1:
        show sabrina thinking at colleague_left
        sabrina "Seu plano cobre uma parte do acordo, mas usa o outro ponto em algo que não resolve a necessidade que priorizamos nesta rodada."
        "Parte que ficou de fora: [planning_missing[0]]."
        if chosen_job == "IDT-UFRJ":
            if 0 not in planning_selected:
                carlos "O intervalo de preparação não substitui a verificação de reservas sobrepostas. Duas pessoas ainda poderiam disputar o mesmo horário."
            else:
                carlos "Evitar sobreposição ajuda, mas ainda preciso dos dez minutos de preparação antes da próxima reserva do microscópio."
        elif chosen_job == "Startup":
            if 0 not in planning_selected:
                carlos "Recalcular o total ajuda, mas ainda preciso confirmar a exclusão e poder desistir sem perder o gasto."
            else:
                carlos "A confirmação ajuda, mas a lista e o total também precisam refletir a exclusão. Senão continuo sem confiar nos números."
        else:
            if 0 not in planning_selected:
                carlos "Exigir uma descrição ajuda o suporte, mas eu ainda preciso conseguir consultar a solução e o estado do chamado."
            else:
                carlos "A consulta ajuda, mas precisamos impedir que o chamado seja resolvido sem uma explicação para mostrar."
    else:
        show sabrina thinking at colleague_left
        sabrina "Os dois pontos foram para extras. Eles podem ter valor, mas nenhuma das duas partes da necessidade confirmada entrou nesta entrega."
        "Ficaram de fora: [planning_missing[0]] e [planning_missing[1]]."
        carlos "Eu ainda enfrentaria o problema que trouxe. Podemos rever o recorte antes de desenvolver?"

    sabrina "Isso não torna os extras inúteis. Outra meta ou novas evidências poderiam mudar a prioridade. Aqui avaliamos o plano pelo objetivo que Carlos confirmou."
    sabrina "Antes de assumir esse plano num projeto real, também precisamos conferir dependências e estimativas com a equipe."
    menu:
        "O que você quer fazer com este plano?"
        "Revisar os itens escolhidos":
            $ planning_complete = False
            jump planning_select
        "Concluir a atividade e voltar ao resumo":
            return
