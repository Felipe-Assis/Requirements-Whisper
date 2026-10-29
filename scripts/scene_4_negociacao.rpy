define julio = Character("Júlio · desenvolvimento", color="#c2d5aa")

default negotiation_complete = False
default negotiation_agreement = ""
default negotiation_change = ""
default negotiation_impact = ""
default negotiation_option = ""

label scene_4_negociacao:
    hide sabrina
    show carlos serious at colleague_left
    show julio thinking at colleague_right
    with dissolve
    if chosen_job == "IDT-UFRJ":
        $ negotiation_change = "avisar por e-mail quando alguém cancelar uma reserva"
        $ negotiation_impact = "A integração de e-mail ainda precisa ser preparada; incluí-la agora adia a proteção contra reservas conflitantes."
    elif chosen_job == "Startup":
        $ negotiation_change = "importar automaticamente os gastos do banco"
        $ negotiation_impact = "A conexão com o banco exige autorização e tratamento de falhas; incluí-la agora adia a exclusão segura dos gastos."
    else:
        $ negotiation_change = "avisar pelo WhatsApp quando um chamado for resolvido"
        $ negotiation_impact = "A integração de mensagens ainda precisa de autorização e testes; incluí-la agora adia a consulta confiável da solução."
    carlos "Antes de fechar a entrega, surgiu outro pedido: [negotiation_change]. Assim eu não preciso conferir tudo manualmente."
    julio "Quero entregar algo confiável nesta rodada. [negotiation_impact]"
    carlos "Eu quero reduzir o trabalho de consulta. Mas o problema que contei continua acontecendo hoje."

label negotiation_decision:
    menu:
        "Como você conduz essa mudança?"
        "Incluir o novo pedido e manter o prazo sem conversar sobre capacidade.":
            julio "Para cumprir isso eu teria de cortar a verificação do caso limite. Não consigo prometer as duas coisas com segurança."
            carlos "Então eu receberia uma novidade, mas ainda poderia enfrentar o problema original. Precisamos rever esse compromisso."
            jump negotiation_decision
        "Recusar a mudança porque o requisito já foi escrito.":
            carlos "A necessidade de reduzir consultas não desapareceu. Podemos ao menos decidir quando investigá-la?"
            julio "O registro pode mudar. Precisamos deixar claro o efeito na entrega e combinar a prioridade."
            jump negotiation_decision
        "Entregar a regra e o caso limite primeiro; investigar a integração na próxima rodada.":
            $ negotiation_option = "base_primeiro"
            $ negotiation_agreement = "Entregar primeiro a regra confirmada e o caso limite. Carlos e Júlio vão investigar como " + negotiation_change + " na próxima rodada, antes de estimar e assumir uma data."
            carlos "Ainda vou consultar o sistema nesta primeira entrega, mas quero resolver o problema atual antes. Eu participo da próxima conversa."
            julio "Mantenho a verificação da regra e do caso limite. A integração fica registrada para investigação, sem promessa de data."
        "Investigar a integração agora e renegociar a data da primeira entrega.":
            $ negotiation_option = "investigar_agora"
            $ negotiation_agreement = "Investigar agora como " + negotiation_change + ". Carlos aceita adiar a primeira entrega; Júlio avaliará dependências e esforço antes de combinar uma nova data, preservando a regra e o caso limite."
            carlos "Aceito esperar pela primeira entrega para entender essa integração. Vou manter o processo atual enquanto investigamos."
            julio "Vou verificar dependências e esforço. Depois combinamos uma nova data; investigar agora não garante que a integração será viável."
    "Acordo proposto: [negotiation_agreement]"
    menu:
        "Carlos e Júlio conferem o registro."
        "Rever o acordo antes de confirmar":
            $ negotiation_agreement = ""
            jump negotiation_decision
        "Confirmar o acordo com os dois":
            $ negotiation_complete = True
    julio "Com o efeito e a prioridade registrados, a equipe sabe qual compromisso está assumindo."
    carlos "E eu sei o que ainda vou precisar fazer enquanto a solução não chega."
    return
