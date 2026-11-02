# st_09_historias.rpy
# Rota Startup, semana 3, segunda, 9h00 a 12h00. Fonte: docs/rotas/startup.md (st_09).
# História de usuário, critério Dado/Quando/Então, caso limite e Definition of Ready.

label st_09_historias:
    $ set_available("st_techlead", "st_qualidade", "st_ceo", "st_estudante")
    $ set_time(9, 0)

    play music music_office_concentrated_1 fadein 1.0
    scene bg startup_coworking_manha
    with fade

    "{i}Segunda-feira da semana 3. O coworking ainda está meio vazio, e o cheiro de café passado vem da copa.{/i}"
    "{i}Na parede de vidro, os post-its da semana passada continuam no lugar. No topo da coluna \"funcional\", um papel coral: excluir um gasto lançado por engano.{/i}"

    show st_mentora neutral at left_zoom
    with dissolve
    st_mentora "Bom dia, [player_name]! Bora transformar aquele post-it em trabalho de verdade?"
    st_mentora "Aqui cada cartão do Kanban é uma história de usuário. Uma frase curta: quem precisa, o que quer fazer e para quê."
    st_mentora "Embaixo vão os critérios de aceitação. É com eles que a Lorena vai dizer se o cartão ficou pronto."

    show st_mobile neutral at right_zoom
    with dissolve
    st_mobile "E é com eles que eu não invento moda. Bom dia, gente!"
    st_mentora "Caso de uso completo, com fluxo principal e todos os desvios, a gente só escreve quando o fluxo tem muitos caminhos. Para excluir um gasto, história e critério dão conta."
    $ advance_minutes(20)

    # Caça à ambiguidade (docs/design/intermissoes-startup.md, seção 7).
    show st_mentora thinking at left_zoom
    st_mentora "Antes do cartão, um aquecimento. Na sexta, o Vinícius colou isso no quadro de ideias."
    "\"O app deve mostrar o total do mês atualizado rapidamente e deixar a pessoa excluir gastos facilmente, sem perder dados.\""
    st_mobile "Pô, parece ótimo."
    st_mentora "Parece. Agora tenta escrever o teste. Marca as palavras que cada um aqui leria de um jeito."
    call amb_atividade("st_amb_total") from _amb_st09
    show st_mentora neutral at left_zoom
    st_mentora "Agora o Vinícius lê e reconhece o pedido dele. E a Lorena consegue testar cada pedaço."
    st_mobile "\"Rapidamente\" era minha palavra favorita. Era."
    $ advance_minutes(15)

    show st_mentora thinking at left_zoom
    st_mentora "Rabisquei três versões do cartão no fim de semana. Me diz qual vai para o quadro."

    menu (tipo="trabalho"):
        "Qual história vai para o cartão?"
        "\"Como estudante que lançou um gasto por engano, quero excluí-lo com uma confirmação, para que o total do mês volte a ser confiável.\"":
            $ st_decidir("st_d09_historia", True)
            show st_mentora neutral at left_zoom
            st_mentora "Essa. Tem a pessoa, a ação e o motivo. Se amanhã aparecer outro cartão disputando a vaga, a gente compara pelo \"para quê\"."
        "\"Como sistema, quero um botão Excluir na lista de gastos.\"":
            $ st_decidir("st_d09_historia", False)
            show st_mentora serious at left_zoom
            st_mentora "Essa descreve uma tela, não uma pessoa. E sem o \"para quê\", ninguém sabe dizer se ela vale mais que outro cartão."
            menu (tipo="trabalho"):
                "Reescrevo dizendo quem é a pessoa, a ação e o benefício.":
                    pass
            show st_mentora neutral at left_zoom
            st_mentora "Isso. \"Como estudante que lançou um gasto por engano, quero excluí-lo com uma confirmação, para que o total do mês volte a ser confiável.\" Agora dá para priorizar."
        "\"Como usuário, quero um app fácil de usar.\"":
            $ st_decidir("st_d09_historia", False)
            show st_mentora serious at left_zoom
            st_mentora "Isso é um épico do tamanho do app inteiro. Não cabe numa semana e não tem como testar. Lembra o que a Bia ensinou sobre \"fácil\"?"
            menu (tipo="trabalho"):
                "Reescrevo dizendo quem é a pessoa, a ação e o benefício.":
                    pass
            show st_mentora neutral at left_zoom
            st_mentora "Isso. \"Como estudante que lançou um gasto por engano, quero excluí-lo com uma confirmação, para que o total do mês volte a ser confiável.\" Cabe numa semana e dá para conferir."

    $ advance_minutes(25)
    "{i}Tainá escreve a história num cartão novo. Embaixo, deixa um espaço em branco com o título \"Critérios\".{/i}"

    show st_mobile thinking at right_zoom
    st_mobile "Agora a parte que me interessa. Como eu sei que terminei?"

    menu (tipo="trabalho"):
        "Qual critério verifica a regra combinada com a Bia?"
        "\"Dado um total mensal de R$ 100 com um gasto de R$ 20, quando a estudante confirmar a exclusão, o gasto sai da lista e o total passa a R$ 80.\"":
            $ st_decidir("st_d09_criterio", True)
            show st_mobile neutral at right_zoom
            st_mobile "Pô, esse eu consigo transformar em teste quase do jeito que está. Cem, exclui vinte, sobra oitenta."
            st_mentora "Dado, quando, então. Situação inicial com número, a ação e um resultado que qualquer pessoa confere."
        "\"O app deve ter um painel moderno de educação financeira.\"":
            $ st_decidir("st_d09_criterio", False)
            show st_mobile serious at right_zoom
            st_mobile "Mano, eu entrego um painel lindo e o total continua errado. E esse critério passa."
            menu (tipo="trabalho"):
                "Escrevo situação inicial, ação e resultado com valores.":
                    pass
            show st_mobile neutral at right_zoom
            st_mentora "Então fica: \"Dado um total de R$ 100 com um gasto de R$ 20, quando a estudante confirmar a exclusão, o gasto sai da lista e o total passa a R$ 80.\""
            st_mobile "Agora sim. Isso vira teste."
        "\"O botão Excluir deve ficar visível na lista.\"":
            $ st_decidir("st_d09_criterio", False)
            show st_mobile serious at right_zoom
            st_mobile "Esse confere que o botão existe. Não diz nada do que acontece com o gasto e com o total depois do toque."
            menu (tipo="trabalho"):
                "Escrevo situação inicial, ação e resultado com valores.":
                    pass
            show st_mobile neutral at right_zoom
            st_mentora "Então fica: \"Dado um total de R$ 100 com um gasto de R$ 20, quando a estudante confirmar a exclusão, o gasto sai da lista e o total passa a R$ 80.\""
            st_mobile "Agora sim. Isso vira teste."

    $ advance_minutes(30)
    show st_mobile neutral at right_zoom
    st_mobile "Aproveitei o domingo e fiz um protótipo rapidinho da confirmação. Olha só."

    show expression "images/artifacts/st_app_gastos.png" as st_prototipo at artefato_tela
    with dissolve
    "{i}Na tela da esquerda, a lista de outubro: total de R$ 100, o almoço de R$ 20, o bandejão, o ônibus, o café.{/i}"
    "{i}Na da direita, a mesma lista escurecida e uma caixa no meio: \"Excluir Almoço, R$ 20,00?\". Dois botões: Cancelar e Excluir.{/i}"
    hide st_prototipo
    with dissolve

    st_mentora "Ficou ótimo, Davi. Vou mandar um print para a Bia junto com o critério. Quem usa é quem confirma."
    $ advance_minutes(25)

    play sound "audio/effects/cell_vibration.ogg"
    show st_estudante portrait at center_zoom
    with dissolve
    st_estudante "(mensagem) Égua, ficou bonito! Mas tipo assim: e se eu tocar em Excluir e depois cancelar? Às vezes eu toco errado no ônibus."
    hide st_estudante
    with dissolve

    show st_mentora thinking at left_zoom
    st_mentora "Ela achou o caso limite antes da gente. O que a gente responde e escreve no cartão?"
    call pista_lembrar("st_p_cancelar") from _pl_st09_limite

    menu (tipo="trabalho"):
        "Bia pergunta: e se eu tocar em Excluir e depois cancelar?"
        "O gasto permanece e o total continua R$ 100; confirmo isso com a Bia.":
            $ st_decidir("st_d09_limite", True)
            show st_mentora neutral at left_zoom
            st_mentora "Perfeito. Cancelar é desistir, então nada muda. Vira um segundo critério, ao lado do primeiro."
        "O gasto some, mas o total só atualiza quando ela reabrir a tela.":
            $ st_decidir("st_d09_limite", False)
            show st_mentora serious at left_zoom
            st_mentora "Cancelar é desistir. Se o gasto some mesmo assim, a confirmação vira enfeite. E o total desatualizado é a queixa número um das avaliações."
            menu (tipo="trabalho"):
                "Registro o caso do cancelamento e o resultado esperado, e confirmo com a Bia.":
                    pass
            show st_mentora neutral at left_zoom
            st_mentora "Isso: ao cancelar, o gasto continua na lista e o total fica em R$ 100. Vira um segundo critério."
        "A janela fecha; não precisa conferir lista nem total.":
            $ st_decidir("st_d09_limite", False)
            show st_mobile serious at right_zoom
            st_mobile "Fechar a janela não prova nada. Já vi app que apagava no fundo e só mostrava depois. O teste tem que olhar a lista e o total."
            menu (tipo="trabalho"):
                "Registro o caso do cancelamento e o resultado esperado, e confirmo com a Bia.":
                    pass
            show st_mentora neutral at left_zoom
            st_mentora "Isso: ao cancelar, o gasto continua na lista e o total fica em R$ 100. Vira um segundo critério."

    "{i}No cartão, embaixo do primeiro critério, entra o segundo: \"Dado um total de R$ 100 com um gasto de R$ 20, quando a estudante cancelar a exclusão, o gasto continua na lista e o total continua R$ 100.\"{/i}"
    $ registrar("st_reg_criterio")

    show st_mobile thinking at right_zoom
    st_mobile "Pergunta chata, mas alguém tem que fazer: e se ela excluir sem internet? No ônibus, no túnel?"
    show st_mentora thinking at left_zoom
    st_mentora "Boa. Não sei responder agora, e não quero chutar."
    st_mentora "Vou anotar como pergunta aberta para a arquitetura. O Otávio vai querer olhar isso junto com o duplicado."
    $ advance_minutes(30)

    st_mentora "Agora a regra da casa: cartão só vai para \"Pronto para desenvolver\" quando tem história, critério com valores e a confirmação de quem pediu."
    st_mentora "Antes disso, o Davi começaria a codar em cima de suposição."
    "{i}Tainá manda os dois critérios para a Bia. A resposta chega em poucos minutos.{/i}"

    play sound "audio/effects/cell_vibration.ogg"
    show st_estudante portrait at center_zoom
    with dissolve
    st_estudante "(mensagem) É isso. Cem, tira vinte, fica oitenta. E se eu desistir, fica tudo como estava. Pode fazer!"
    hide st_estudante
    with dissolve

    "{i}Tainá arrasta o cartão para a coluna \"Pronto para desenvolver\". Davi faz um barulho de vitória baixinho.{/i}"
    $ advance_minutes(10)

    show st_mobile neutral at right_zoom
    st_mobile "[player_name], bora parear no protótipo à tarde? Quero ligar a confirmação na lista de verdade."

    menu (tipo="conversa"):
        "O que você responde ao Davi?"
        "Bora!":
            $ add_friendship_point("st_mobile", 1)
            st_mobile "Fechou! Duas da tarde. Eu levo o café, você leva os critérios."
        "Hoje prefiro revisar os critérios por conta própria, mas amanhã topo.":
            st_mobile "Fechou, amanhã. Revisa mesmo, que eu vou te cobrar."

    show st_mentora neutral at left_zoom
    st_mentora "Bom trabalho, [player_name]. Do post-it ao cartão pronto numa manhã."

    $ st_checar_conquistas()
    $ set_time(12, 0)

    hide st_mentora
    hide st_mobile
    with dissolve
    "{i}Meio-dia. O cartão coral está sozinho na coluna nova, com dois critérios e uma pergunta aberta embaixo.{/i}"

    return
