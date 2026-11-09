# A campanha tem seu próprio estado; as três atividades guiadas continuam em start.
label lab_campaign:
    hide screen learning_hud
    hide screen learning_notebook
    hide screen inv_quick
    hide screen inventory_screen
    $ lab_reset()
    $ lab_return_milestone = "reunião de sexta-feira da semana seguinte"
    show screen lab_hud
    scene bg laboratorio
    show carlos serious at colleague_right
    with dissolve
    "Segunda-feira, 14h. Laboratório da universidade."
    carlos "Tem duas equipes esperando pelo mesmo microscópio. As duas receberam confirmação."
    carlos "Uma pessoa já preparou a amostra. A outra cancelou uma reunião para vir."
    player "Antes de trocar a agenda, quero entender onde essas confirmações se separaram."
    show sabrina thinking at colleague_left
    sabrina "Eu achei que bastava juntar as planilhas. Agora não tenho tanta certeza."
    sabrina "Vou conversar com a coordenação. Você consegue trazer as fontes para a mesa da equipe?"
    hide sabrina
    hide carlos

label lab_investigation:
    call screen lab_map
    if _return == "continue":
        jump lab_definition
    $ lab_location = _return

label lab_visit_location:
    call screen lab_location_screen(lab_location)
    if _return == "back":
        jump lab_investigation
    call lab_inspect_source
    jump lab_visit_location

label lab_inspect_source:
    if _return == "sheets":
        $ lab_collect("sheets")
        scene bg laboratorio
        show carlos thinking at colleague_right
        "Na primeira planilha: microscópio, 14h–15h. Na segunda: microscópio, 14h30–15h30."
        carlos "Eu confirmei a primeira. A outra veio da bancada. Não vejo o que eles alteram lá."
        player "As duas reservas existem. Ainda não sabemos qual consulta cada pessoa fez."
        carlos "Pois é. Escolher uma planilha vencedora agora não devolve a preparação de ninguém."
    elif _return == "preparation":
        $ lab_collect("preparation")
        scene bg laboratorio
        "A ficha ao lado do microscópio pede dez minutos de preparação entre usos. Você chama a técnica."
        "Técnica" "É deste microscópio. Eu limpo, ajusto e confiro a imagem antes da próxima amostra."
        player "Se uma reserva acaba às 15h, outra às 15h05 ainda atrapalha?"
        "Técnica" "Aqui, sim. Às 15h10 consigo entregar pronto. Não use essa ficha para a centrífuga."
        player "Vou registrar o equipamento e o intervalo juntos."
    elif _return == "interview":
        $ lab_collect("interview")
        scene bg escritorio
        show carlos thinking at colleague_right
        carlos "Eu olho a agenda antes de chamar o pessoal. Preciso saber se posso confiar naquele horário."
        player "O que você confere primeiro?"
        carlos "Equipamento, dia, início e fim. Se preciso abrir outra planilha para confirmar, fico inseguro."
        player "Você quer uma consulta clara. E a confirmação precisa impedir que duas equipes ocupem o mesmo horário."
        carlos "Isso. Um aviso bonito depois que eu trouxe a amostra chega tarde."
    elif _return == "offline":
        $ lab_collect("offline")
        scene bg escritorio
        show julio neutral at colleague_right
        "Na mesa da equipe há uma cópia local da agenda. A coluna de alterações está cheia."
        julio "Eu ia pedir para apagarem isso. A técnica disse que a conexão cai perto da bancada."
        player "Então não é só apego à planilha. Ela cobre uma falta de acesso."
        julio "Se tirarmos a cópia hoje, ela anota no papel. Precisamos combinar como uma anotação vira reserva confirmada."
        player "A cópia pode servir de consulta. Mudança de reserva precisa voltar para quem confirma a agenda."
        julio "Vou levar esse procedimento para a bancada, junto com a tela."
    hide carlos
    hide julio
    return

label lab_definition:
    $ lab_phase = "definition"
    scene bg escritorio
    show julio thinking at colleague_right
    julio "Trouxe as fontes? Vamos deixar claro qual delas sustenta cada regra."
    player "Uma fala ajuda a entender a necessidade. A ficha do equipamento limita onde a regra vale."
    hide julio
    call screen lab_board
    $ lab_phase = "planning"
    show julio neutral at colleague_right
    julio "Nesta rodada cabem três pontos do nosso quadro. São uma estimativa desta equipe, não horas de relógio."
    julio "Impedir sobreposição custa dois. O preparo custa mais um e depende dessa conferência."
    julio "Pesquisar o acesso exige uma rodada dedicada. Podemos antecipar essa pesquisa, mas a execução deste pacote fica para depois."
    player "O que ficar fora precisa aparecer na conversa da entrega."
    hide julio
    call screen lab_planning

label lab_negotiation:
    $ lab_phase = "negotiation"
    scene bg escritorio
    show carlos thinking at colleague_left
    show julio thinking at colleague_right
    carlos "Se as planilhas conversassem entre si, eu não precisaria comparar cópias. Dá para fazer agora?"
    julio "Ainda preciso de autorização e de um ambiente de teste. Não cabe prometer isso junto com o pacote escolhido."
    carlos "Quero parar de perder horários. Mas também não quero trocar de tela e continuar copiando tudo."

label lab_negotiate_choice:
    menu:
        "Qual compromisso você propõe?"
        "Entregar o plano primeiro; investigar a integração na próxima rodada.":
            player "Entregamos só o que está no plano. Júlio e Carlos trazem a pesquisa na sexta-feira da semana que vem."
            carlos "Enquanto isso, eu continuo consultando a agenda. Quero esse retorno mesmo se a entrega parecer boa."
            menu:
                "O pacote e a promessa estão separados no registro."
                "Confirmar com Carlos e Júlio":
                    $ lab_confirm_commitment("base_primeiro")
                "Rever o plano antes de confirmar":
                    hide carlos
                    hide julio
                    $ lab_phase = "planning"
                    call screen lab_planning
                    jump lab_negotiation
        "Investigar a integração agora e adiar a primeira entrega.":
            player "Vamos conferir o acesso antes de marcar a entrega. O processo atual continua, com confirmação centralizada pelo Carlos."
            julio "Eu verifico a autorização. Carlos confere as solicitações. Trazemos a resposta na sexta-feira da semana que vem."
            carlos "Aceito esperar. Preciso que todo mundo saiba a quem pedir confirmação nesse intervalo."
            menu:
                "O adiamento e o responsável temporário estão no registro."
                "Confirmar com Carlos e Júlio":
                    $ lab_confirm_commitment("investigar_agora")
                "Rever o plano antes de confirmar":
                    hide carlos
                    hide julio
                    $ lab_phase = "planning"
                    call screen lab_planning
                    jump lab_negotiation

label lab_delivery:
    $ lab_phase = "delivery"
    "Quarta-feira. Mesa da equipe."
    if lab_commitment == "investigar_agora":
        julio "A rodada ficou com a pesquisa. Este protótipo simula o plano futuro; a execução do pacote está adiada."
        player "Vamos conferir o comportamento proposto sem tratar esse ensaio como entrega."
    else:
        julio "Separei o pacote em uma versão para revisão. Vamos conferir o que mudou antes de mostrar."
    if "conflict" in lab_plan:
        player "A confirmação agora compara equipamento e intervalo com as reservas já registradas."
        julio "E só grava se a conferência permitir. Recusar a tentativa não apaga a reserva anterior."
    else:
        player "A proteção contra sobreposição ficou fora deste pacote. Ele ainda pode aceitar dois horários incompatíveis."
        julio "Vou manter essa limitação na demonstração. A interface sozinha não resolve isso."
    if "preparation" in lab_plan:
        player "Depois vem a conferência dos dez minutos, apenas para o microscópio."
        julio "Revisei o alcance com a ficha. Equipamentos diferentes continuam independentes."
    else:
        julio "O intervalo do microscópio ainda não está protegido. Essa ausência continua no registro."
    if "clarity" in lab_plan:
        player "Também deixamos equipamento e horários visíveis na mesma consulta."
    hide carlos
    if lab_commitment == "investigar_agora":
        julio "Este calendário é um protótipo. Ninguém deve tratar o teste como reserva no laboratório."
        hide julio
        menu:
            "Antes do protótipo, confira a alternativa temporária."
            "Experimentar a confirmação centralizada":
                player "Carlos, duas equipes pediram o microscópio: 14h–15h e 14h30–15h30."
                carlos "Confiro na agenda central antes de confirmar. A segunda fica em espera; vou falar com a equipe."
                player "E a anotação na bancada?"
                carlos "É uma solicitação até eu devolver a confirmação. Vou responder às duas pessoas."
                $ lab_record_event("temporary_confirmation")
        "O procedimento depende de Carlos disponível. O sistema anterior continua em uso."
    else:
        julio "Os testes vão usar exatamente as regras do pacote confirmado. Uma regra ausente continua ausente."
        hide julio
    call screen lab_demo
    if lab_commitment == "base_primeiro":
        $ lab_mark_delivery()
        "Sexta-feira. O pacote escolhido chega à bancada com suas limitações registradas."
    else:
        "Sexta-feira da primeira semana. A entrega continua adiada. O retorno da investigação está marcado para a próxima sexta-feira."

label lab_followup:
    $ lab_phase = "followup"
    scene bg laboratorio
    show carlos thinking at colleague_left
    show sabrina retorno at colleague_right
    "Sexta-feira da semana seguinte. Uma semana depois da entrega prevista, chega a reunião combinada."
    if lab_commitment == "base_primeiro":
        carlos "Você combinou que eu consultaria a agenda e que teríamos um retorno nesta reunião. E a integração?"
    else:
        carlos "Eu fiquei com as confirmações enquanto vocês investigavam. Você prometeu trazer a resposta, não a integração pronta."
    menu:
        "Carlos abre o registro do acordo."
        "Trazer o retorno da investigação e combinar o próximo passo":
            player "Júlio verificou o acesso. A coordenação precisa autorizar uma conta de teste antes de conectarmos as planilhas."
            player "Nós dois vamos levar o pedido à coordenação na próxima reunião. Ainda não temos uma data de integração."
            carlos "Essa resposta eu consigo levar para a bancada. Vou participar do pedido."
            $ lab_commitment_status = "fulfilled"
            $ lab_record_event("dependency_found")
            $ lab_record_event("investigation_returned")
        "Renegociar o retorno e registrar a investigação pendente":
            player "Não trouxe a verificação completa. Preciso mudar o marco de retorno com você e Júlio."
            carlos "Então escreva: próxima reunião com a coordenação. Eu vou precisar manter a consulta manual até lá."
            $ lab_return_milestone = "próxima reunião com a coordenação"
            $ lab_commitment_status = "renegotiated"
            $ lab_record_event("return_renegotiated")
    hide sabrina
    show julio thinking at colleague_right
    if lab_delivery == "not_delivered":
        carlos "O procedimento evitou confirmar o segundo pedido no nosso ensaio. No dia a dia, continuo fazendo essa conferência à mão."
        julio "A dependência de autorização continua. O calendário que você testou ainda não foi entregue."
        jump lab_adoption
    if "conflict" not in lab_plan or "preparation" not in lab_plan:
        $ lab_record_event("incident_observed")
        if "conflict" not in lab_plan:
            carlos "Ontem duas equipes conseguiram confirmar o mesmo horário de novo. Eu precisei pedir que uma esperasse."
            player "A proteção ficou fora do nosso pacote. Não foi a falta de um clique no teste que criou isso."
        else:
            carlos "Não houve sobreposição. Mas uma reserva começou cinco minutos depois da outra, e o microscópio ainda estava em preparo."
            player "Entregamos a conferência de horários sem o intervalo da ficha. A técnica ficou com o problema."
        menu:
            "O incidente pode entrar numa revisão pequena."
            "Reproduzir e reparar o incidente com Júlio":
                if "conflict" not in lab_plan:
                    $ lab_run_test("overlap")
                    "O ensaio reproduz duas reservas sobrepostas aceitas pela versão atual."
                else:
                    $ lab_run_test("preparation")
                    "O ensaio reproduz uma reserva aceita com apenas cinco minutos de preparo."
                player "Na revisão, entram a conferência de sobreposição e o preparo específico do microscópio."
                julio "Eu altero a confirmação. Você confere o exemplo da ficha comigo e repete os dois testes."
                $ lab_repair()
                hide carlos
                hide julio
                jump lab_regression
            "Registrar o impacto e deixar a revisão pendente":
                player "Vou registrar quem precisou esperar e a revisão necessária. Ela ainda não tem responsável confirmado."
                julio "Sem alguém assumir, não vou apresentar essa correção como entregue."
    else:
        carlos "Na terça apareceu outro pedido sobreposto. A agenda recusou antes de a pessoa trazer a amostra."
        carlos "E os dez minutos ficaram livres. A técnica não precisou negociar o preparo na porta."
    jump lab_adoption

label lab_regression:
    call screen lab_demo
    if lab_test_results.get("overlap") != "conflict" or lab_test_results.get("preparation") != "preparation_required":
        julio "Precisamos repetir a sobreposição e os cinco minutos de preparação na revisão. Um caso não cobre o outro."
        jump lab_regression
    show julio neutral at colleague_right
    julio "A sobreposição foi recusada. Cinco minutos também; a reserva anterior ficou intacta."
    $ lab_mark_delivery()
    "A revisão 2 chega à bancada. Carlos repete os horários com a técnica antes de usá-la."
    show carlos thinking at colleague_left
    carlos "Eu esperei pela correção, mas agora consigo mostrar exatamente o que mudou."

label lab_adoption:
    if lab_sidequest:
        player "E a cópia local, quando a conexão cai?"
        carlos "Marcamos como consulta. Uma alteração só vira reserva depois da confirmação central. A técnica ajudou a combinar isso."
        if lab_delivery == "not_delivered":
            carlos "Por enquanto, eu sou essa confirmação. A nova tela ainda não chegou."
        else:
            carlos "Quando a conexão volta, eu confiro a agenda antes de confirmar a solicitação. Já não temos duas confirmações independentes."
    else:
        carlos "Ainda há uma cópia local na bancada. Precisamos ouvir quem usa antes de pedir que parem."
    $ lab_record_event("adoption_reviewed")
    hide julio
    show sabrina retorno at colleague_right
    if lab_sidequest:
        sabrina "Eu comecei achando que era só juntar planilhas. A conversa da bancada mudou meu plano."
    else:
        sabrina "Eu comecei achando que era só juntar planilhas. As reservas e a ficha do microscópio mostraram outra coisa."
    if lab_delivery == "not_delivered":
        player "O sistema ainda não chegou. A bancada sabe quem confirma as reservas enquanto a investigação continua."
    elif lab_ending() == "unowned":
        player "A tela mudou, mas a conferência ainda sobra para as pessoas. Falta alguém assumir a revisão."
    else:
        player "A entrega só virou mudança quando combinamos como confirmar e como voltar às pendências."
    sabrina "O que continua pendente está no registro. Vou chamar as pessoas envolvidas na próxima conversa."
    $ lab_phase = "ending"
    hide carlos
    hide sabrina
    if lab_ending() == "reliable":
        "Na bancada, o próximo grupo consulta o horário antes de preparar a amostra. O conflito é barrado antes de virar uma espera."
        "A integração continua como próximo passo. A rotina já tem uma proteção concreta."
    elif lab_ending() == "waiting":
        "Carlos fecha a agenda central e leva o pedido de autorização. A equipe sabe por que espera e quem confirma as reservas nesse intervalo."
        "O protótipo ainda não substitui o processo atual. O próximo passo tem destinatário."
    elif lab_ending() == "repaired":
        "A ficha do microscópio fica ao lado do registro da revisão 2. A falha tem uma causa, uma mudança e exemplos que a equipe consegue repetir."
        "O tempo perdido não volta. A próxima equipe encontra uma confirmação diferente."
    else:
        "Carlos deixa o incidente aberto no quadro. A agenda mudou, mas parte do trabalho de conciliar horários continua com as pessoas."
        "A equipe ainda pode assumir a revisão. Hoje, essa responsabilidade permanece pendente."
    call screen lab_final(lab_ending())
    if _return == "replay":
        jump lab_campaign
    elif _return == "legacy":
        $ lab_active = False
        hide screen lab_hud
        hide screen lab_journal
        jump start
    jump lab_campaign_end

label lab_campaign_end:
    $ lab_active = False
    hide screen lab_hud
    hide screen lab_journal
    $ renpy.full_restart()
