# st_13_arquitetura.rpy
# Rota Startup, semana 4, segunda. Causa do duplicado (idempotência),
# modelagem de dados e negociação da importação bancária.
# Fonte: docs/rotas/startup.md, seção st_13_arquitetura.

label st_13_arquitetura:
    $ set_available("st_qualidade", "st_estudante")
    $ set_time(10, 0)

    play music music_office_concentrated_2 fadein 1.0
    scene bg startup_coworking_manha
    with fade

    "{i}Segunda-feira, semana 4. A luz da manhã entra pelas janelas em arco e bate num desenho novo na parede de vidro, feito com caneta azul.{/i}"
    "{i}Otávio está ao lado dele, caneca na mão, com a calma de quem espera a água do café ferver.{/i}"

    show st_techlead neutral at center_zoom
    with dissolve
    st_techlead "Bom dia, [player_name]. Puxa uma cadeira. Hoje a gente descobre por que o almoço da Bia aparece duas vezes."

    show st_mobile neutral at right_zoom
    with dissolve
    st_mobile "Trouxe três celulares de teste e um carregador. Se é pra quebrar o app, que seja aqui e não no ônibus."

    show st_mentora neutral at left_zoom
    with dissolve
    st_mentora "Eu vim de ouvinte. Quero entender a causa antes de prometer qualquer coisa pra Bia."

    hide st_mentora
    hide st_mobile
    hide st_techlead
    with dissolve

    show expression "images/artifacts/st_diagrama_arquitetura.png" as st_diagrama at artefato_tela
    with dissolve

    st_techlead "Veja bem. Começa no celular. O app guarda cada lançamento num banco local, dentro do aparelho. Por isso a Bia consegue lançar o bandejão mesmo sem sinal."
    st_techlead "Quando a internet volta, uma fila de sincronização manda os lançamentos para a nuvem, um por um."
    st_techlead "Na nuvem não tem servidor ligado o dia inteiro. São funções que acordam quando chega um pedido, fazem o trabalho e voltam a dormir. A gente paga só pelo que roda."
    st_techlead "No fim do caminho fica o banco relacional, cuidado pelo provedor. É ali que mora o total do mês."
    "{i}Você acompanha as setas: celular, fila, funções, banco. Num canto, uma caixa tracejada diz “Instituição parceira (Open Finance)”, ligada por uma linha pontilhada.{/i}"
    st_techlead "Essa caixa pontilhada ainda é só uma possibilidade. Daqui a pouco ela volta."

    hide st_diagrama
    with dissolve

    $ advance_minutes(25)

    show st_techlead serious at center_zoom
    show st_mobile thinking at right_zoom
    with dissolve

    st_techlead "Agora, o bug. Lembra do horário que você me mandou na semana 2?"
    if st_viu_duplicado:
        "{i}Você lembra do túnel, do lanche de R$ 7 e do total que subiu R$ 14 de uma vez.{/i}"
    else:
        "{i}Você lembra das anotações sobre o ônibus e o sinal que some no túnel.{/i}"
    st_techlead "Fui no registro daquele minuto. Dois pedidos iguais, com poucos segundos de diferença. Mesmo valor, mesma descrição, mesmo celular."
    st_mobile "Deixa eu reproduzir. Lancei um café de R$ 5... toquei em Salvar..."
    st_mobile "Agora corto a rede bem no meio do envio, igual no túnel. O pedido chega no servidor, mas a resposta não volta."
    "{i}No notebook de Otávio, o banco recebe o café. Davi religa a rede, o app tenta de novo, e o banco recebe o café outra vez. O total no celular de teste salta de R$ 5 para R$ 10.{/i}"
    st_techlead "Aí está. O app enviou, a resposta se perdeu no caminho e ele não sabe se o servidor recebeu. Na dúvida, reenvia."
    st_techlead "E o servidor acha que cada envio é um gasto novo. É como pedir uma pizza, a ligação cair e você ligar de novo. Se a pizzaria não perguntar o número do pedido, chegam duas."
    st_mobile "E a Bia paga as duas, pelo menos na tela."
    st_techlead "Então, [player_name]. Como você evitaria o gasto duplicado?"
    call pista_lembrar("st_p_tunel") from _pl_st13_idempotencia

    menu (tipo="trabalho"):
        "Como evitar o gasto duplicado?"

        "Bloquear lançamentos quando o celular estiver sem internet.":
            $ st_decidir("st_d13_idempotencia", False)
            show st_mobile serious at right_zoom
            st_mobile "A Bia lança no ônibus e no bandejão, justamente onde o sinal some. Sem poder salvar, ela esquece o gasto e o total fica errado para menos."
            st_techlead "Trocamos um total alto demais por um total baixo demais. Pensa no número do pedido da pizza."
            menu (tipo="trabalho"):
                "Faço cada lançamento ter uma identidade própria desde o celular.":
                    st_techlead "Isso. Agora o servidor consegue reconhecer um pedido repetido."

        "O celular gera um identificador único no momento do lançamento; o servidor ignora repetições com o mesmo id.":
            $ st_decidir("st_d13_idempotencia", True)
            show st_techlead neutral at center_zoom
            st_techlead "Isso tem nome: idempotência. Pode repetir à vontade que o resultado é o mesmo."

        "O servidor apaga gastos com o mesmo valor e a mesma data.":
            $ st_decidir("st_d13_idempotencia", False)
            show st_techlead thinking at center_zoom
            st_techlead "E os dois cafés de R$ 5 que a Bia toma no mesmo dia? Viram um só. Trocamos um erro por outro."
            st_mobile "Valor e data não dizem quem é quem. Precisa de algo que seja só daquele lançamento."
            menu (tipo="trabalho"):
                "Faço cada lançamento ter uma identidade própria desde o celular.":
                    st_techlead "Isso. Agora o servidor consegue reconhecer um pedido repetido."

    show st_techlead neutral at center_zoom
    show st_mobile neutral at right_zoom
    st_techlead "O id nasce no celular, antes do primeiro envio. Se o mesmo pedido chegar três vezes, o servidor vê que já conhece aquele id e devolve a mesma resposta, sem criar gasto novo."
    if not st_d13_idempotencia:
        st_techlead "Isso tem nome: idempotência. Pode repetir o pedido quantas vezes for, o resultado é o mesmo."
    st_mobile "Tipo o número do pedido da pizza. Fechou, eu monto isso na fila."

    $ advance_minutes(40)

    "{i}Otávio apaga metade do quadro e desenha quatro caixas. Em cima de cada uma, um nome: Estudante, Gasto, Categoria, Consentimento.{/i}"
    show st_techlead thinking at center_zoom
    st_techlead "Agora os dados. O Gasto tem o id que nasce no celular, o valor, a data, a categoria, a origem, que pode ser manual ou banco, quando foi criado e quando foi excluído."
    st_techlead "Antes de seguir, uma pergunta que parece boba. Como a gente guarda o valor?"

    menu (tipo="trabalho"):
        "Como guardar o valor do gasto?"

        "Texto, do jeito que aparece na tela: “R$ 20,00”.":
            $ st_decidir("st_d13_valor", False)
            show st_mobile serious at right_zoom
            st_mobile "Aí pra somar o total eu converto tudo de volta. E na hora de ordenar, R$ 100 aparece antes de R$ 20, porque o texto compara letra por letra."
            menu (tipo="trabalho"):
                "Guardo em centavos inteiros e formato só na tela.":
                    st_techlead "Isso. O banco guarda número; a tela mostra o “R$”."

        "Número decimal de ponto flutuante, que já aceita os centavos.":
            $ st_decidir("st_d13_valor", False)
            st_techlead "Some 0,10 com 0,20 no computador e veja o que dá. Dá 0,30000000000000004."
            st_techlead "Num lançamento, ninguém percebe. Em mil, o centavo some ou aparece do nada. E é justamente de total errado que a Bia reclama."
            menu (tipo="trabalho"):
                "Guardo em centavos inteiros e formato só na tela.":
                    st_techlead "Isso. Conta com inteiro não tem sobra."

        "Número inteiro em centavos: R$ 20,00 vira 2000.":
            $ st_decidir("st_d13_valor", True)
            show st_techlead neutral at center_zoom
            st_techlead "Exato. Dinheiro em float é como medir farinha com régua. Centavo é inteiro."
            st_mobile "E a vírgula só aparece na tela. Fechou."

    show st_techlead serious at center_zoom
    st_techlead "Mais dois detalhes. “Excluído em” guarda a data em que a Bia apagou o gasto. Assim, se um envio atrasado chegar depois, o servidor não ressuscita o almoço."
    st_techlead "Depois de um prazo combinado, apagamos de vez. Foi o que a Tainá e eu decidimos para o RF08 depois da inspeção: nada de guardar para sempre."
    st_techlead "E o Consentimento guarda a instituição, o que a pessoa autorizou, a validade e quando ela revogou. Só existe se um dia houver importação."
    st_mobile "Precisa de tanto cuidado assim? A lei nem coloca dado financeiro na lista de dados sensíveis."
    st_techlead "Não coloca. Mas um vazamento mostra quanto a pessoa ganha, onde come e quando atrasa o aluguel. É dado pessoal e é sério. Guarda só o necessário."
    st_techlead "Dado que você não guarda não vaza."

    hide st_techlead
    hide st_mobile
    with dissolve

    "{i}A manhã termina com o quadro cheio de setas e uma pilha de post-its sobre a mesa. Davi já abriu o projeto da fila de sincronização.{/i}"

    # Tarde: o pedido do Vinícius e a negociação.
    $ set_time(14, 30)
    scene bg startup_coworking_tarde
    with fade

    "{i}Depois do almoço, a porta da escada bate. Vinícius entra com o celular ainda na orelha, encerra a ligação e abre os braços.{/i}"

    show st_ceo neutral at right_zoom
    with dissolve
    st_ceo "Time! Acabei de sair da reunião com o fundo. Eles amaram a história da Bia!"
    st_ceo "Mas perguntaram uma coisa: e a importação bancária? Todo mundo tá falando de Open Finance. Quero isso na 1.0. Imagina a Bia sem precisar lançar nada!"

    show st_mentora thinking at left_zoom
    show st_mobile thinking at center_zoom
    with dissolve

    st_mobile "Pô, Vinícius, deixa eu mostrar o que tem dentro desse pedido."
    st_mobile "Primeiro, precisa de parceria com uma instituição autorizada. Segundo, uma tela de consentimento com prazo e com jeito de revogar. Terceiro, tratar falha: banco fora do ar, consentimento vencido, gasto que chega repetido do banco."
    st_mobile "Se entra agora, a exclusão segura e a correção do duplicado vão pra depois do semestre. Não cabe tudo em quatro semanas com o mesmo time."
    st_ceo "Mas sem novidade eu chego no demo day com o quê?"
    st_mentora "[player_name], você estava na entrevista com os dois. Como a gente conduz isso?"

    jump st_13_negociacao

label st_13_negociacao:
    menu (tipo="negociacao"):
        "Como você conduz o pedido do Vinícius?"

        "Incluir a importação e manter o prazo, sem falar de capacidade.":
            $ st_acordo_ruins += 1
            show st_mobile serious at center_zoom
            st_mobile "Pra caber, eu corto o teste do cancelamento e a correção do duplicado. A Bia continua vendo o almoço duas vezes."
            show st_ceo thinking at right_zoom
            st_ceo "Então eu mostraria uma novidade em cima de um total errado. Não é isso que eu quero."
            show st_mentora serious at left_zoom
            st_mentora "Tenta de novo. Impacto dito em voz alta, e um caminho que proteja o que a Bia pediu."
            jump st_13_negociacao

        "Recusar o pedido, porque a especificação já está fechada.":
            $ st_acordo_ruins += 1
            show st_ceo thinking at right_zoom
            st_ceo "O documento não é contrato com o universo. O fundo vai perguntar de novo."
            show st_mentora serious at left_zoom
            st_mentora "A necessidade continua lá: seis avaliações pedem pra digitar menos. Precisamos decidir quando investigar, não se ela existe."
            jump st_13_negociacao

        "Propor “base primeiro”: exclusão segura e duplicado na 1.0; a importação vira investigação.":
            "{i}Acordo proposto: entregar na 1.0 a exclusão segura e a correção do duplicado. A importação vira investigação: no demo day, mostramos o protótipo do consentimento como próximo passo, sem dados reais e sem data prometida.{/i}"
            show st_ceo thinking at right_zoom
            st_ceo "Um protótipo do consentimento... Investidor gosta de ver que a gente sabe o próximo passo. E eu não prometo data que não posso cumprir."
            show st_mobile neutral at center_zoom
            st_mobile "E eu entrego a base sem cortar teste."
            menu (tipo="negociacao"):
                "Rever o acordo antes de confirmar.":
                    jump st_13_negociacao
                "Confirmar o acordo com Vinícius, Davi e Tainá.":
                    $ st_confirmar_acordo("base_primeiro")

        "Propor “investigar agora”: Otávio estuda a parceria por uma semana e a data da 1.0 é renegociada.":
            "{i}Acordo proposto: Otávio investiga a parceria por uma semana agora; a data da 1.0 é renegociada, preservando a exclusão segura, o caso limite e a correção do duplicado. Se não couber antes do semestre, a importação fica para depois.{/i}"
            show st_mobile neutral at center_zoom
            st_mobile "Uma semana dá pra saber se o parceiro existe e quanto custa. Construir, não dá. Mas a base fica protegida."
            show st_ceo thinking at right_zoom
            st_ceo "Data nova eu converso com o fundo, desde que a gente chegue no semestre com o total certo."
            menu (tipo="negociacao"):
                "Rever o acordo antes de confirmar.":
                    jump st_13_negociacao
                "Confirmar o acordo com Vinícius, Davi e Tainá.":
                    $ st_confirmar_acordo("investigar_agora")

    $ advance_minutes(35)

    show st_mentora neutral at left_zoom
    show st_mobile neutral at center_zoom
    show st_ceo neutral at right_zoom
    with dissolve

    st_mentora "Fechado. Vou escrever no documento quem pediu, o que foi combinado e por quê. Daqui a um mês ninguém vai lembrar da conversa, mas vai lembrar do registro."
    if st_acordo_opcao == "base_primeiro":
        st_ceo "Então no demo day eu mostro a Bia confiando no total e o consentimento como próximo passo. Gostei. Dá pra contar essa história."
    else:
        st_ceo "Então o Otávio me traz uma resposta em uma semana e eu ajusto a conversa com o fundo. Combinado."
    st_ceo "E, [player_name]: se eu estiver pedindo coisa demais, me fala com o impacto, como hoje. Eu escuto."

    $ registrar("st_reg_mudanca")

    hide st_ceo
    with dissolve
    "{i}Vinícius já sai atendendo outra ligação. Tainá cola um post-it com o acordo no quadro, ao lado do cartão “Importação bancária (investigar)”.{/i}"

    hide st_mentora
    hide st_mobile
    with dissolve

    $ set_time(16, 50)
    "{i}O fim da tarde chega devagar. Otávio volta de uma call e se senta na ponta da mesa, ao lado de Davi.{/i}"

    show st_techlead neutral at center_zoom
    show st_mobile neutral at right_zoom
    with dissolve

    menu (tipo="conversa"):
        "Antes de ir embora, você..."

        "Agradeço ao Otávio pela paciência em reproduzir o bug.":
            $ add_friendship_point("st_techlead", 1)
            st_techlead "Obrigado você, que anotou o horário. Sem isso eu ainda estaria procurando."
            st_techlead "Já te contaram do internet banking por SMS que eu ajudei a fazer em 2004? A mensagem chegava duas vezes, e o saldo também."
            st_techlead "A versão certa da história é esta: depois de três meses apanhando, cada SMS ganhou um número. Se chegasse de novo, o sistema respondia “já feito”. Foi o que a gente desenhou hoje de manhã."

        "Pergunto ao Davi como ele vai montar a fila de sincronização.":
            $ add_friendship_point("st_mobile", 1)
            show st_mobile thinking at right_zoom
            st_mobile "Cada lançamento entra na fila com o id dele. O app tenta enviar; se falhar, espera um pouco mais a cada tentativa."
            st_mobile "E só tira da fila quando o servidor confirma. Amanhã a gente pareia nisso, bora?"

        "Vou direto registrar a decisão no documento.":
            show st_mentora neutral at left_zoom
            with dissolve
            st_mentora "Registro de decisão é ouro daqui a seis meses."
            hide st_mentora

    $ st_checar_conquistas()
    $ set_time(17, 0)

    hide st_techlead
    hide st_mobile
    with dissolve

    "{i}Você guarda o notebook na mochila. No quadro, o desenho de Otávio continua lá: celular, fila, funções, banco. E, agora, um número para cada pedido.{/i}"

    return
