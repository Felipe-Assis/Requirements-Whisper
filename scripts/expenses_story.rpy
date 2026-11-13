define exp_lia = Character("Lia · estudante", color="#e8cba4")
image julio gastos_pensando = ConditionSwitch("exp_renegotiated", "images/characters/julio/return.png", "True", "images/characters/julio/thinking.png")
image julio gastos_neutro = ConditionSwitch("exp_renegotiated", "images/characters/julio/return.png", "True", "images/characters/julio/neutral.png")
image lia gastos = ConditionSwitch("exp_renegotiated", "images/characters/lia/return.png", "True", "images/characters/lia/neutral.png")

label expenses_campaign:
    $ campaign_mark_started("expenses")
    hide screen learning_hud
    hide screen learning_notebook
    hide screen inv_quick
    hide screen inventory_screen
    hide screen lab_hud
    $ exp_reset()
    $ campaign_set_clock("startup", "Terça-feira", "14h", "afternoon")
    scene expression Transform(campaign_clock["image"], xysize=(1920, 1080), fit="cover")
    with dissolve
    show lia gastos at colleague_right
    "Terça-feira, 14h. Lia abre o controle de gastos que a equipe está construindo."
    exp_lia "Eu só almocei uma vez. O aplicativo diz que gastei cem reais hoje. Agora nem sei quanto posso usar no ônibus."
    show sabrina thinking at colleague_left
    sabrina "Trouxe o comprovante? Vamos comparar com os lançamentos antes de mexer no saldo."
    exp_lia "Sim. Só cuidado: transporte e almoço custaram o mesmo valor. Os dois aconteceram."
    if campaign_memory("lab").get("repaired"):
        sabrina "Na agenda, reconhecer a lacuna e repetir o exemplo ajudou a recuperar a confiança. Vamos fazer isso antes da entrega aqui."
    elif campaign_memory("lab").get("outcome") == "reliable":
        sabrina "A agenda melhorou quando você levou uma situação real para a bancada. Faça o mesmo com o recibo da Lia."
    hide sabrina
    hide lia
    call screen exp_investigation
    call screen campaign_app_builder("expenses")
    $ exp_phase = "before"
    show julio gastos_pensando at colleague_right
    julio "Tenho uma versão de teste com botão Remover e uma pergunta de confirmação. Ainda não passou pela revisão."
    player "Vamos abrir a pergunta e cancelar. Se os dados mudarem antes da resposta, o botão já está fazendo coisa demais."
    hide julio
    call screen exp_ledger
    show julio gastos_pensando at colleague_right
    exp_lia "Eu cancelei, mas a linha sumiu. Se fosse o transporte, eu teria perdido uma compra de verdade."
    julio "Achei o ponto: a remoção roda ao abrir a pergunta. Vou movê-la para a resposta Confirmar."
    player "E lista e total precisam mudar juntos. Vamos guardar uma cópia para desfazer também."
    $ exp_phase = "planning"
    hide julio
    call screen exp_planning
    $ exp_set_plan(_return)
    if exp_plan == "bank":
        jump exp_bank_priority
    jump exp_development

label exp_bank_priority:
    show julio gastos_pensando at colleague_right
    exp_lia "Se o banco trouxesse minhas compras, eu não digitava tudo. Só não quero entregar minha senha para isso."
    julio "Não precisamos dela neste ensaio. Vou descobrir o que o banco oferece, quais dados viriam e qual consentimento seria necessário. Ainda não tenho acesso de testes."
    player "Nesta rodada, então, pesquisamos. A correção de Cancelar fica pendente. Lia, até o retorno, você consegue conferir o caderno?"
    exp_lia "Consigo por alguns dias. Se continuar dando trabalho, prefiro corrigir a lista primeiro."
    $ campaign_set_clock("startup", "Terça-feira · semana seguinte", "09h", "morning")
    scene expression Transform(campaign_clock["image"], xysize=(1920, 1080), fit="cover")
    with dissolve
    show lia retorno at colleague_right
    show julio retorno at colleague_left
    "Uma semana depois, terça-feira às 09h. Lia e Júlio voltam à sala. A resposta do banco não chegou; o pedido de acesso está registrado, sem integração pronta."
    julio "O próximo passo depende do acesso. A pesquisa reduziu uma dúvida, mas a lista continua com a falha."
    menu:
        "A prioridade pode ser renegociada com quem usa o produto."
        "Retomar a correção com Lia e Júlio":
            $ exp_set_plan("core")
            player "Vamos combinar outra rodada para a correção e manter o pedido bancário separado."
            exp_lia "Combinado. Vou validar o exemplo do almoço com vocês."
            hide julio
            hide lia
            jump exp_development
        "Manter a pesquisa e registrar a correção pendente":
            player "Júlio acompanha o acesso. Na próxima sexta, voltamos com uma resposta ou revemos a prioridade."
            exp_lia "Até lá vou continuar conferindo o caderno. Registrem isso como trabalho que ainda falta."
            hide julio
            hide lia
            jump exp_finish

label exp_development:
    $ exp_phase = "development"
    show julio gastos_neutro at colleague_right
    julio "A mudança é pequena, mas atravessa três comportamentos. Aplique os três no quadro para eu revisar o conjunto."
    player "A duplicata é AL-18 porque Lia confirmou o mesmo pagamento C-071. A implementação remove só o ID escolhido; não procura valores iguais."
    hide julio
    call screen exp_implementation
    show julio gastos_pensando at colleague_right
    menu:
        "Como vamos conferir a versão de teste antes de chamar Lia?"
        "Parear com Júlio e explicar cada mudança":
            $ exp_build("pair")
            player "A pergunta guarda o ID. Confirmar copia a lista e remove a linha. O total soma o estado atual."
            julio "Conferi os três pontos com você. Agora quero ver Cancelar e Desfazer funcionando."
        "Pedir revisão de Júlio e preparar os casos de teste":
            $ exp_build("review")
            julio "Revisei: nenhum dado muda ao abrir a pergunta; o total vem da lista; a cópia não aponta para os mesmos registros."
            player "Eu preparo cancelar, confirmar e desfazer com o recibo de Lia ao lado."
    hide julio
    $ exp_phase = "demo"

label exp_demo:
    call screen exp_ledger
    if _return == "pending":
        show julio gastos_pensando at colleague_right
        menu:
            "A revisão pode ficar aberta sem receber o nome de entregue."
            "Continuar o ensaio e recuperar os dados":
                hide julio
                jump exp_demo
            "Combinar outra rodada e registrar a pendência":
                player "Eu e Júlio retomamos estes casos com Lia na próxima sexta. A revisão não será publicada antes disso."
                hide julio
                jump exp_finish
    if not exp_deliver():
        jump exp_demo
    $ exp_phase = "followup"
    show lia gastos at colleague_right
    show sabrina enthusiastic at colleague_left
    exp_lia "Agora Cancelar deixa tudo como estava. Confirmar AL-18 traz o total para oitenta. E eu consigo desfazer uma escolha errada."
    sabrina "Vocês mudaram o ponto em que a ação acontece e conferiram o resultado. A pergunta sozinha não era uma proteção."
    hide sabrina
    $ campaign_set_clock("startup", "Terça-feira · duas semanas depois" if exp_renegotiated else "Terça-feira · semana seguinte", "09h", "morning")
    scene expression Transform(campaign_clock["image"], xysize=(1920, 1080), fit="cover")
    with dissolve
    show lia retorno at colleague_right
    "Uma semana depois da entrega, terça-feira às 09h. Lia volta com os gastos da semana e o mesmo caderno, agora usado só para conferir os primeiros dias."
    if campaign_layout("expenses")[0] == "balance":
        exp_lia "Você deixou o total primeiro. Quando abro o controle, vejo logo quanto registrei."
    elif campaign_layout("expenses")[0] == "records":
        exp_lia "Você deixou os lançamentos primeiro. Ficou fácil conferir o recibo antes de olhar o total."
    else:
        exp_lia "Você deixou as ações primeiro. O Desfazer fica à mão; rolo a lista para conferir os recibos."
    exp_lia "Eu deixei um almoço parecido no dia seguinte. Ele ficou na lista, como deveria. Valor igual não virou motivo para apagar."
    if exp_recovered:
        exp_lia "No ensaio, vocês recuperaram um gasto legítimo. Saber que dá para voltar me ajudou a testar sem medo."
    if exp_sidequest:
        exp_lia "Também vimos que editar um valor positivo muda o total, e que dá para desfazer a edição."
    if exp_zero_rejected:
        exp_lia "Zero foi recusado sem destruir o que já estava salvo."
    show julio retorno at colleague_left
    julio "A correção está entregue. Para o banco, eu ainda preciso confirmar consentimento e ambiente de testes antes de estimar a integração."
    player "Você acompanha esse acesso; eu volto com Lia na próxima sexta para conferir o uso e decidir o próximo pacote."
    exp_lia "Isso me atende. Prefiro essa combinação a uma data inventada para o banco."
    hide julio
    hide lia

label exp_finish:
    $ exp_phase = "ending"
    $ campaign_record("expenses", exp_result())
    call screen exp_final
    jump campaign_hub
