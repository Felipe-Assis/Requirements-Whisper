default transfer_complete = False
default transfer_requirement = ""
default transfer_criterion = ""
default transfer_request = ""
default journey_complete = False

label scene_5_sintese:
    $ transfer_complete = False
    hide julio
    show sabrina neutral at colleague_right
    with dissolve
    sabrina "Chegou outro pedido. Agora você vai produzir um registro curto, sem escolher uma resposta pronta."
    if chosen_job == "IDT-UFRJ":
        $ transfer_request = "A pessoa responsável pelo laboratório precisa cancelar uma reserva. Só a pessoa que fez a reserva ou a responsável pode cancelar; após o cancelamento, o horário deve voltar a ficar disponível."
    elif chosen_job == "Startup":
        $ transfer_request = "A estudante precisa corrigir o valor de um gasto. O novo valor deve ser maior que zero; ao confirmar, a lista e o total do mês devem refletir a alteração."
    else:
        $ transfer_request = "A solicitante precisa reabrir um chamado resolvido quando a solução falhar. Ela deve informar o motivo; o chamado volta a Em atendimento e preserva a solução anterior no histórico."
    carlos "[transfer_request]"
    sabrina "Escreva o comportamento esperado e um exemplo que permita verificá-lo. Pode ser breve. Depois você mesmo revisará o registro."

label transfer_write:
    hide screen learning_hud
    $ transfer_requirement = renpy.input("Seu requisito: quem pode fazer o quê e sob quais condições?", default=transfer_requirement, length=300, screen="transfer_input", exclude="").strip()
    $ transfer_criterion = renpy.input("Seu critério: situação inicial, ação e resultado que pode ser conferido.", default=transfer_criterion, length=400, screen="transfer_input", exclude="").strip()
    call screen transfer_review
    show screen learning_hud
    sabrina "O jogo não avalia o significado do texto. Compare seu registro com o pedido de Carlos: [transfer_request]"
    sabrina "Você deixou claro quem age e qual condição restringe a ação? Seu exemplo traz dados iniciais e um resultado observável? Há algo que não pode mudar ou um caso que deve ser recusado?"
    menu:
        "Autoavaliação · O que seu registro precisa agora?"
        "Reescrever para esclarecer uma condição ou o resultado":
            jump transfer_write
        "Conferi os pontos; guardar como rascunho para discutir" if transfer_requirement and transfer_criterion:
            $ transfer_complete = True
        "Continuar sem registrar o exercício":
            $ transfer_complete = False
    if transfer_complete:
        sabrina "Seu rascunho ficou no notebook. O próximo passo seria revisá-lo com Carlos e a equipe, incluindo dúvidas e outros exemplos. Não é uma correção automática."
    else:
        sabrina "O exercício ficou pendente. Você pode retomá-lo no encerramento; concluir a história não equivale a validar um requisito."
    $ journey_complete = True
    return

label journey_review:
    show sabrina enthusiastic at colleague_right
    carlos "Você ouviu o problema, esclareceu a regra e ajudou duas pessoas a assumir um compromisso possível. Obrigado!"
    "Jornada concluída · [mission_context]"
    "Primeira conversa: [mission_score] de 4 decisões adequadas antes do feedback. Esse resultado descreve apenas aquela atividade."
    "Acordo: [negotiation_agreement]"
    if transfer_complete:
        "Aplicação final: rascunho produzido e revisado por você, ainda sem validação da equipe."
    else:
        "Aplicação final: pendente."
    sabrina "Na próxima conversa real, leve uma dúvida e um exemplo para conferir com as pessoas envolvidas. Requisitos continuam sendo discutidos conforme aprendemos."

label journey_actions:
    menu:
        "Fim da jornada · Seu registro continua disponível no notebook."
        "Rever o acordo da entrega":
            "[negotiation_agreement]"
            jump journey_actions
        "Revisar a aplicação final":
            call scene_5_sintese
            jump journey_actions
        "Refazer a missão neste contexto":
            jump scene_2_estagio
        "Experimentar outra vaga":
            $ notebook_available = False
            hide screen learning_hud
            hide screen learning_notebook
            call escolher_vaga(explorar=True)
            jump scene_2_estagio
        "Encerrar e voltar ao menu principal":
            return
screen transfer_input(prompt):
    modal True
    zorder 130
    add Solid("#08151df5")
    frame:
        style "rw_panel"
        align (0.5, 0.5)
        xsize 1600
        ysize 940
        vbox:
            spacing 24
            text "Aplicação final · rascunho" style "rw_heading" size 42
            text prompt style "rw_caption" size 36
            viewport:
                id "transfer_input_scroll"
                ysize 600
                xfill True
                mousewheel True
                draggable False
                pagekeys True
                scrollbars "vertical"
                input:
                    id "input"
                    size (42 if persistent.rw_large_text else 32)
                    color "#ffffff"
                    xmaximum 1400
            text "Digite seu registro. Enter conclui este campo; Page Up / Page Down percorrem o texto." style "rw_caption" size 26

screen transfer_review():
    modal True
    zorder 130
    add Solid("#08151df5")
    frame:
        style "rw_panel"
        align (0.5, 0.5)
        xsize 1600
        ysize 940
        vbox:
            spacing 20
            text "Confira seu rascunho" style "rw_heading" size 42
            viewport:
                id "transfer_review_scroll"
                ysize 660
                xfill True
                mousewheel True
                draggable True
                arrowkeys True
                pagekeys True
                scrollbars "vertical"
                vbox:
                    spacing 24
                    xsize 1400
                    text "Requisito" style "rw_heading" size 36
                    text transfer_requirement.replace("{", "{{") substitute False style "rw_caption" size (42 if persistent.rw_large_text else 32) xmaximum 1360
                    text "Critério de aceitação" style "rw_heading" size 36
                    text transfer_criterion.replace("{", "{{") substitute False style "rw_caption" size (42 if persistent.rw_large_text else 32) xmaximum 1360
            text "Role com a roda do mouse, setas ou Page Up / Page Down." style "rw_caption" size 26
            textbutton "Continuar a autoavaliação":
                style "rw_action"
                action Return()
                default_focus True
