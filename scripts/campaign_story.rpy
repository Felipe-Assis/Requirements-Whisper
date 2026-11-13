label campaign_start:
    $ campaign_reset()
    $ campaign_set_clock("startup", "Início da jornada", "09h", "morning")
    show screen campaign_time_hud
    hide screen learning_hud
    hide screen inv_quick
    scene bg escritorio
    show sabrina neutral at colleague_right
    with dissolve
    sabrina "Tem três pedidos na mesa. Todos parecem pequenos até alguém mostrar o que acontece de verdade."
    player "Posso escolher por onde começar?"
    sabrina "Pode. Traga o que encontrou, o que mudou e o que ainda não consegue prometer. Eu guardo os retornos aqui."
    hide sabrina
    jump campaign_hub

label campaign_hub:
    $ campaign_active = True
    $ campaign_clock = {}
    show screen campaign_time_hud
    $ lab_active = False
    hide screen lab_hud
    hide screen lab_journal
    hide screen campaign_journal
    scene bg escritorio
    call screen campaign_hub_screen
    if _return == "lab":
        jump lab_campaign
    elif _return == "expenses":
        jump expenses_campaign
    elif _return == "tickets":
        jump tickets_campaign
    elif _return == "city":
        jump student_city
    scene bg escritorio
    show sabrina retorno at colleague_right
    with dissolve
    sabrina "Vamos olhar o que ficou com as pessoas depois que fechamos os protótipos."
    if campaign_memory("lab").get("repaired"):
        sabrina "No laboratório vocês voltaram ao incidente. O registro conserva a primeira decisão e a revisão; isso ajuda a próxima pessoa a entender a mudança."
    elif campaign_memory("lab").get("outcome") == "waiting":
        sabrina "A pesquisa do laboratório ainda não virou entrega. O próximo passo precisa continuar visível, mesmo com os outros projetos andando."
    if campaign_memory("lab").get("sidequest"):
        sabrina "A cópia da bancada tinha uma razão de existir. Foi a conversa que revelou isso."
    if campaign_memory("lab").get("delivery", "not_delivered") != "not_delivered" or campaign_memory("expenses").get("delivered") or campaign_memory("tickets").get("outcome") in ("reviewed", "followed_up", "repaired", "followup_pending"):
        player "As entregas mudaram mais que as telas. Também tivemos que combinar como testar e passar a responsabilidade adiante."
    else:
        player "Agora sabemos o que precisa mudar. As propostas ainda têm pendências; não vou apresentá-las como entregas."
    sabrina "E nem tudo terminou. Vamos deixar cada pendência ao lado do resultado, para ninguém precisar adivinhar."
    hide sabrina
    call screen campaign_closing
    jump campaign_hub
