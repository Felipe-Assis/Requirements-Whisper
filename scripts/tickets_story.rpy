define ticket_rodrigo = Character("Rodrigo · suporte", color="#e1b66b")
image rodrigo serious = "images/characters/rodrigo/serious.png"
image rodrigo thinking = "images/characters/rodrigo/thinking.png"

label tickets_campaign:
    $ campaign_mark_started("tickets")
    hide screen learning_hud
    hide screen learning_notebook
    hide screen inv_quick
    hide screen inventory_screen
    $ ticket_reset()
    $ campaign_set_clock("support", "Segunda-feira", "14h30", "day")
    scene expression Transform(campaign_clock["image"], xysize=(1920, 1080), fit="cover")
    show rodrigo serious at colleague_right
    with dissolve
    "Segunda-feira, 14h30. A ligação volta à mesa do suporte."
    ticket_rodrigo "Eu já encerrei o atendimento da Ana. Mesmo assim, ela está perguntando se alguém resolveu."
    player "O que ela vê quando abre o chamado?"
    show rodrigo thinking at colleague_right
    ticket_rodrigo "Não sei. Eu só conferi o nosso painel. A nota técnica está aqui."
    show sabrina thinking at colleague_left
    sabrina "Vamos comparar os dois lados antes de pedir que ela tente de novo. E olhar o registro que liga uma tela à outra."
    hide rodrigo
    hide sabrina

label tickets_investigation:
    $ ticket_phase = "investigation"
    call screen ticket_investigation
    show rodrigo thinking at colleague_right
    ticket_rodrigo "Então eu encerrei para o suporte. Para a Ana, não chegou estado nem orientação."
    "Ana · solicitante" "Eu não preciso dos detalhes de acesso. Preciso saber o que mudou e o que fazer se continuar bloqueado."
    player "Estado e solução precisam chegar juntos à pessoa. A nota interna tem outro público."
    hide rodrigo
    show sabrina neutral at colleague_left
    sabrina "A fila tem mais dois pedidos. Só conseguimos acompanhar uma validação nesta rodada. Quem ficar esperando precisa aparecer no acordo."
    hide sabrina

label tickets_triage:
    $ ticket_phase = "triage"
    call screen ticket_triage
    "Você registra o impacto de atender primeiro o chamado #[ticket_selected]. Os outros dois continuam abertos."
    show julio thinking at colleague_right
    julio "Preparei a correção de serviço deste atendimento. Falta corrigir como o encerramento chega à pessoa."
    julio "Vamos começar pela versão anterior. Depois você escolhe o patch e compara as duas telas."
    julio "Uma solução vazia deve recusar a operação inteira. Resolver um chamado também não pode alterar os outros."
    hide julio

label tickets_development:
    $ ticket_phase = "development"
    call screen ticket_workbench
    show julio neutral at colleague_right
    julio "A nova versão publicou estado e solução juntos. O caso vazio foi recusado e os outros chamados ficaram intactos."
    player "Agora precisamos decidir quando publicar, o texto que a pessoa recebe e quem faz o próximo passo."
    hide julio
    show rodrigo thinking at colleague_right
    ticket_rodrigo "Minha nota tem detalhes técnicos. Podemos preparar outra orientação para a pessoa, sem copiar tudo."
    if "shift" in ticket_evidence:
        player "Eu conferi sua escala. Você não estará amanhã; vou combinar a continuidade com alguém disponível."
        ticket_rodrigo "Isso evita deixar a revisão parada na minha caixa depois do turno."
    else:
        ticket_rodrigo "Confira quem estará aqui amanhã antes de repassar o atendimento."
    hide rodrigo

label tickets_delivery:
    $ ticket_phase = "delivery"
    call screen ticket_delivery
    $ ticket_submit()
    show sabrina neutral at colleague_left
    if ticket_delivery == "review_pending":
        sabrina "A solução está preparada, mas a pessoa ainda vê Em atendimento. Eu reviso na terça-feira às 09h antes de publicar."
    elif ticket_delivery == "published":
        sabrina "Estado e solução já chegaram à pessoa. Na terça-feira às 09h eu confiro o uso e acompanho eventuais reaberturas."
    else:
        sabrina "O repasse ficou sem responsável confirmado. O chamado continua aberto; amanhã podemos recuperar essa combinação."
    hide sabrina
    $ campaign_set_clock("support", "Terça-feira", "09h", "morning")
    scene expression Transform(campaign_clock["image"], xysize=(1920, 1080), fit="cover")
    with dissolve
    "Terça-feira, 09h. O próximo turno abre o histórico do atendimento."
    show sabrina neutral at colleague_left
    sabrina "Vamos retomar a ação registrada ontem e o próximo passo. O histórico precisa contar também o que ainda não aconteceu."
    if ticket_delivery == "published":
        "Solicitante" "Agora consigo ver o estado e uma orientação. Se o problema continuar em outro turno, consigo reabrir este mesmo chamado com um motivo?"
        player "Sim. A reabertura preserva a solução anterior, para a equipe entender o que já foi tentado."
    hide sabrina

label tickets_followup:
    $ ticket_phase = "followup"
    call screen ticket_return

label tickets_adoption:
    $ campaign_set_clock("support", "Terça-feira · semana seguinte", "10h10", "rain")
    scene expression Transform(campaign_clock["image"], xysize=(1920, 1080), fit="cover")
    show sabrina chuva at colleague_left
    show rodrigo chuva at colleague_right
    with dissolve
    "Uma semana depois, terça-feira às 10h10. A chuva acompanha o retorno à sala do suporte."
    sabrina "A chuva apertou no caminho. Trouxe o registro daquela rodada para conferir o que chegou às pessoas."
    ticket_rodrigo "Separei este caso dos outros dois. Quero conferir o que aconteceu antes de passá-lo ao próximo turno."
    if ticket_ending() == "review_pending":
        sabrina "A revisão das 09h não foi realizada. A publicação continua pendente; precisamos assumir esse atraso e combinar um novo retorno."
    elif ticket_ending() == "unowned":
        sabrina "O repasse continuou sem responsável. O atendimento ainda está aberto. Dar o trabalho como entregue esconderia essa espera."
    elif ticket_ending() == "reopened":
        sabrina "A pessoa reabriu com um motivo. O histórico preservou o que já tentamos; falta conferir o caso com Júlio."
    elif ticket_ending() == "followup_pending":
        sabrina "A solução foi publicada, mas o acompanhamento das 09h não foi realizado. Ainda precisamos ouvir a pessoa."
    else:
        sabrina "A ação combinada foi realizada e ficou no histórico. Os outros dois chamados continuam abertos; esta validação não atendeu a fila inteira."
    player "O registro mostra a entrega e a próxima conversa, sem transformar pendência em conclusão."
    hide sabrina
    $ ticket_phase = "ending"
    hide rodrigo
    $ campaign_record("tickets", ticket_summary())
    call screen ticket_final
    $ ticket_active = False
    jump campaign_hub
