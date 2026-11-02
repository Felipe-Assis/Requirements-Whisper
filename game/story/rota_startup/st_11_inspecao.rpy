# st_11_inspecao.rpy
# Rota Startup, semana 3, quarta, 14h00 a 19h30. Fonte: docs/rotas/startup.md (st_11).
# Inspeção de requisitos (ambíguo, ausente, inconsistente) e escrita livre com
# autoavaliação. A escrita pendente pode ser retomada na st_12.

label st_11_inspecao:
    $ set_available("st_techlead", "st_mobile", "st_ceo", "st_estudante")
    $ set_time(14, 0)

    play music music_office_focused_2 fadein 1.0
    scene bg startup_coworking_tarde
    with fade

    "{i}Quarta à tarde. A luz entra laranja pelas janelas em arco e deixa os post-its com cor de bala.{/i}"

    show st_mentora neutral at left_zoom
    with dissolve
    st_mentora "Juntei tudo num documento só: \"Especificação Trocado 1.0\". Histórias, regras, os critérios de segunda."
    st_mentora "Antes de passar para o Davi e o Otávio, a Lorena vai conduzir uma inspeção. Me conta o que você achar, sem dó."

    show st_qualidade thinking at right_zoom
    with dissolve
    st_qualidade "Checklist curto, quatro perguntas. Primeiro: falta alguma coisa? Segundo: dá para entender de dois jeitos?"
    st_qualidade "Terceiro: contradiz outra regra? Quarto: dá para testar?"
    st_qualidade "Se um requisito falha numa delas, a gente corrige aqui. Hoje custa uma tarde. Depois do lançamento, custa uma versão nova na loja."
    $ advance_minutes(20)

    "\"RF03: O app deve alertar o estudante quando ele gastar muito.\""

    menu:
        "Qual é o defeito do RF03?"
        "Ambíguo: \"muito\" precisa de referência, por exemplo, ao atingir 80%% do orçamento do mês.":
            $ st_decidir("st_d11_ambiguo", True)
            show st_qualidade neutral at right_zoom
            st_qualidade "Isso. \"Muito\" para quem ganha R$ 600 de bolsa é diferente de \"muito\" para quem ganha R$ 2.000."
        "Inconsistente com outro requisito.":
            $ st_decidir("st_d11_ambiguo", False)
            show st_qualidade serious at right_zoom
            st_qualidade "Não contradiz nada. O problema é que cada um entende \"muito\" de um jeito. A Bia ia receber alerta todo dia ou nunca."
            menu:
                "Releio com a pergunta do checklist que encaixa e corrijo a frase.":
                    pass
            show st_qualidade neutral at right_zoom
            st_qualidade "Segunda pergunta: dá para entender de dois jeitos? Dá. Então é ambíguo."
        "Está bom, o dev escolhe o limite.":
            $ st_decidir("st_d11_ambiguo", False)
            show st_mentora serious at left_zoom
            st_mentora "Aí o limite muda a cada versão, e ninguém consegue testar se o alerta está certo. O Davi escolhe 50, o próximo dev escolhe 90."
            menu:
                "Releio com a pergunta do checklist que encaixa e corrijo a frase.":
                    pass
            show st_qualidade neutral at right_zoom
            st_qualidade "Segunda pergunta: dá para entender de dois jeitos? Dá. Então é ambíguo, e quem decide o número é quem usa, não quem coda."

    "{i}Lorena reescreve: \"RF03: O app deve alertar a pessoa quando os gastos do mês atingirem 80%% do orçamento que ela definiu.\"{/i}"
    $ advance_minutes(25)

    "\"RF05: Ao excluir um gasto, ele é removido da lista.\""
    show st_mentora thinking at left_zoom
    st_mentora "Esse aqui é o nosso cartão de segunda. Olha com carinho."

    menu:
        "Qual é o defeito do RF05?"
        "Ausente: falta a confirmação, o cancelamento e o recálculo do total que combinamos com a Bia.":
            $ st_decidir("st_d11_ausente", True)
            show st_mentora neutral at left_zoom
            st_mentora "Isso. Do jeito que estava, o principal da conversa com a Bia ficou de fora."
        "Redundante com o RF04, que fala de editar gasto.":
            $ st_decidir("st_d11_ausente", False)
            show st_qualidade serious at right_zoom
            st_qualidade "Editar e excluir são ações diferentes, com riscos diferentes. Um errado muda o valor; o outro some com o gasto."
            menu:
                "Releio com a pergunta do checklist que encaixa e corrijo a frase.":
                    pass
            show st_qualidade neutral at right_zoom
            st_qualidade "Primeira pergunta: falta alguma coisa? Falta a confirmação, o cancelamento e o total. Então é ausente."
        "Está completo e dá para testar.":
            $ st_decidir("st_d11_ausente", False)
            show st_qualidade serious at right_zoom
            st_qualidade "Dá para testar e passar com o total errado. É exatamente o problema que a Bia contou."
            menu:
                "Releio com a pergunta do checklist que encaixa e corrijo a frase.":
                    pass
            show st_qualidade neutral at right_zoom
            st_qualidade "Primeira pergunta: falta alguma coisa? Falta a confirmação, o cancelamento e o total. Então é ausente."

    "{i}A nova versão ocupa três linhas: pedir confirmação; se a pessoa confirmar, tirar o gasto e recalcular o total; se cancelar, manter tudo como estava.{/i}"
    $ advance_minutes(25)

    "\"RF08: Gastos excluídos ficam guardados para sempre para métricas.\""
    "\"RNF02: Ao excluir a conta, os dados financeiros do estudante são apagados em até 15 dias.\""

    menu:
        "O que há de errado com o RF08 e o RNF02?"
        "Inconsistentes: o RF08 contradiz o RNF02. Precisamos decidir finalidade e prazo com o Otávio.":
            $ st_decidir("st_d11_inconsistente", True)
            show st_qualidade neutral at right_zoom
            st_qualidade "Oxe, e eu tinha passado batido nesse na primeira leitura. Os dois não podem ser verdade ao mesmo tempo."
        "O RF08 é só ambíguo; falta dizer onde guarda.":
            $ st_decidir("st_d11_inconsistente", False)
            show st_qualidade serious at right_zoom
            st_qualidade "O lugar não resolve. Num banco ou noutro, um diz \"para sempre\" e o outro diz \"apaga em 15 dias\". Os dois não podem ser verdade ao mesmo tempo."
            menu:
                "Releio com a pergunta do checklist que encaixa e corrijo a frase.":
                    pass
            show st_qualidade neutral at right_zoom
            st_qualidade "Terceira pergunta: contradiz outra regra? Contradiz. Então é inconsistente."
        "Não é problema, métrica é importante para o demo day.":
            $ st_decidir("st_d11_inconsistente", False)
            show st_mentora serious at left_zoom
            st_mentora "Guardar dado financeiro sem finalidade e sem prazo vai contra a LGPD. E quebra a promessa feita a quem apaga a conta."
            menu:
                "Releio com a pergunta do checklist que encaixa e corrijo a frase.":
                    pass
            show st_qualidade neutral at right_zoom
            st_qualidade "Terceira pergunta: contradiz outra regra? Contradiz. Então é inconsistente."

    show st_mentora neutral at left_zoom
    st_mentora "Esse não dá para eu corrigir sozinha. Quem decide quanto tempo um dado fica e para quê é o Otávio. Vou mandar para ele."

    play sound "audio/effects/cell_vibration.ogg"
    show st_techlead portrait at center_zoom
    with dissolve
    st_techlead "(mensagem) Veja bem: dado que você não guarda não vaza. Marca o RF08 como bloqueado. Amanhã a gente define finalidade e prazo."
    hide st_techlead
    with dissolve

    $ st_inspecao_acertos = st_contar("st_d11_ambiguo", "st_d11_ausente", "st_d11_inconsistente")
    $ registrar("st_reg_inspecao")

    if st_inspecao_acertos >= 2:
        st_qualidade "Três requisitos, [st_inspecao_acertos] defeitos achados de primeira. Isso é olho de inspeção."
    else:
        st_qualidade "Quem inspeciona pela primeira vez erra o nome do defeito. O que importa é que agora você sabe qual pergunta fazer a cada linha."
    $ advance_minutes(30)

    show st_mentora thinking at left_zoom
    st_mentora "Agora uma coisa diferente. A Bia mandou um pedido novo hoje de manhã."
    st_mentora "Ela lançou o bandejão como R$ 45 em vez de R$ 4,50 e não conseguiu corrigir. Teve que apagar e lançar de novo."
    st_mentora "Quero que você escreva o requisito e o critério de aceitação. Por conta própria, do seu jeito. Depois a gente lê junto."
    st_mentora "Quando terminar, confere quatro pontos. Fica claro quem age? A condição que limita a ação está escrita?"
    st_mentora "O critério tem dados iniciais e um resultado que dá para observar? E tem algo que deve ser recusado, como valor zero ou negativo?"
    st_qualidade "E escreve com número. \"Corrigir o valor\" não testa nada; \"de R$ 45 para R$ 4,50\" testa."
    st_mentora "Sem pressa. Se não fechar hoje, guarda como pendente e retoma depois."

    hide st_mentora
    hide st_qualidade
    with dissolve
    $ advance_minutes(15)

    call exercicio_escrita(ST_ESCRITA_ID, ST_ESCRITA_PEDIDO) from _st_11_exercicio_escrita
    $ st_sincronizar_escrita()

    $ advance_minutes(120)
    show st_mentora neutral at left_zoom
    with dissolve
    if st_escrita_concluida:
        st_mentora "Conferiu os quatro pontos e guardou? Ótimo. Não precisa estar perfeito: precisa estar claro o bastante para a gente discutir."
        st_mentora "Na próxima conversa com a Bia, eu levo o seu texto e a gente vê se ela se reconhece nele."
    else:
        st_mentora "Ficou pendente, tudo bem. Escrever requisito do zero é outra coisa, né?"
        st_mentora "O pedido continua no seu notebook. Quando quiser, retoma de onde parou."

    scene bg startup_coworking_noite
    with fade
    $ set_time(19, 0)

    "{i}Lá fora já escureceu. As luminárias pendentes acendem só sobre a mesa longa, e os outros lugares estão vazios.{/i}"
    "{i}O documento tem dois requisitos corrigidos, um bloqueado esperando o Otávio e o pedido novo da Bia em forma de rascunho.{/i}"

    show st_qualidade neutral at right_zoom
    with dissolve
    st_qualidade "Por hoje é isso. Amanhã o Davi recebe uma especificação que dá para testar linha por linha."

    menu:
        "O que você diz à Lorena antes de ir?"
        "Agradeço à Lorena pelo checklist.":
            $ add_friendship_point("st_qualidade", 1)
            st_qualidade "Que bom que serviu. Eu copiei de uma ficha de correção de redação, sabia? Só troquei \"coesão\" por \"testável\"."
        "Comento que é cansativo, mas útil.":
            show st_qualidade serious at right_zoom
            st_qualidade "Cansa menos do que consertar em produção. Pergunta para o Otávio sobre a sexta-feira de 2009."

    $ st_checar_conquistas()
    $ set_time(19, 30)

    hide st_qualidade
    with dissolve
    "{i}Sete e meia. Você fecha o notebook com a sensação de que leu o mesmo documento de um jeito diferente.{/i}"

    return
