# st_16_codificacao.rpy
# Rota Startup, ato 5, semana 6 (terça). Fonte: docs/rotas/startup.md, st_16.
# Testes primeiro, PR pequeno e code review com dados pessoais no log.

label st_16_codificacao:
    # Davi e Otávio estão na sala; Lorena chega no fim da tarde.
    $ set_available("st_mentora", "st_qualidade", "st_ceo", "st_estudante")
    $ set_time(10, 0)

    play music music_office_concentrated_1 fadein 1.0
    scene bg startup_coworking_manha
    with fade

    "{i}Semana 6, terça-feira. O coworking ainda está meio vazio. Alguém deixou a bicicleta encostada no sofá verde, e o cheiro de café vem da copa.{/i}"
    "{i}No quadro Kanban, um cartão tem o seu nome: \"Excluir gasto com confirmação\". Ele acaba de sair de \"Pronto para desenvolver\" e entrar em \"Fazendo\".{/i}"

    show st_mobile neutral at left_zoom
    show st_techlead neutral at right_zoom
    with dissolve

    st_mobile "Bom dia! Pô, chegou o dia. Primeiro cartão seu indo para o código."
    st_techlead "Tem mais empolgação no Davi do que em você, [player_name]. Pode ser bom sinal. Ainda não sei."
    st_mobile "Olha o protótipo de novo, pra gente lembrar do que combinou com a Bia."

    hide st_mobile
    hide st_techlead
    show expression "images/artifacts/st_app_gastos.png" as tela_app at artefato_tela
    with dissolve

    "{i}Na tela da esquerda, a lista do mês: total de R$ 100,00 e o almoço de R$ 20,00 no topo. Na da direita, a caixa que pergunta \"Excluir Almoço, R$ 20,00?\", com os botões Cancelar e Excluir.{/i}"
    st_mobile "Dois caminhos. Confirmou: o almoço sai e o total vai para R$ 80. Cancelou: nada muda e o total fica em R$ 100."

    hide tela_app
    show st_mobile neutral at left_zoom
    show st_techlead thinking at right_zoom
    with dissolve

    st_techlead "Veja bem. Obra começa pela fundação, não pela pintura. Por onde você começa esse cartão?"

    menu:
        "Como você implementa o cartão?"

        "Escrevo primeiro os testes do critério e do caso limite (R$ 100 vira R$ 80; cancelar mantém R$ 100) e abro um PR pequeno.":
            $ st_escolher_abordagem("teste_pr")
            show st_techlead neutral at right_zoom
            st_techlead "Gosto disso. O teste é a planta da casa: diz o que precisa ficar de pé antes do primeiro tijolo."
            st_mobile "E PR pequeno eu reviso hoje mesmo. Fechou."

        "Codifico rápido e testo depois no celular do Davi.":
            $ st_escolher_abordagem("rapida")
            show st_techlead serious at right_zoom
            st_techlead "E se a sincronização chegar depois da exclusão? Isso você só vê testando de propósito, não clicando no celular de alguém."
            st_techlead "A Lorena vai achar que o total não recalcula depois da sincronização. São dois dias de volta, na semana mais apertada."

        "Aproveito para reescrever a tela de gastos com uma biblioteca nova de animações.":
            $ st_escolher_abordagem("reescrever")
            show st_mobile serious at left_zoom
            st_mobile "Mano, eu amo biblioteca nova. Mas olha o tamanho disso."
            st_mobile "Vira um PR de 40 arquivos. Ninguém revisa direito e o cancelamento se perde no meio."

    if st_abordagem != "teste_pr":
        show st_techlead neutral at right_zoom
        st_techlead "Calma. Ninguém escreveu código ainda, então trocar de caminho agora sai barato."
        st_techlead "Começa pelo que a Bia combinou com a gente. Um teste para confirmar, outro para cancelar. Depois, só o código que faz os dois passarem."

        menu:
            "O que você ajusta no plano?"

            "Começo pelos dois testes da Bia e deixo o PR do tamanho do cartão.":
                $ st_escolher_abordagem("teste_pr")
                st_techlead "Perdemos meio dia, não dois."
                st_techlead "E o teste fica lá para sempre. Quando alguém mexer na lista daqui a seis meses, ele avisa se o total quebrar."

    hide st_techlead
    hide st_mobile
    with dissolve

    $ advance_minutes(40)
    "{i}Você abre o editor e escreve o primeiro teste antes de qualquer linha da tela.{/i}"
    "\"Dado um total de R$ 100 com um almoço de R$ 20, quando a estudante confirma a exclusão, o almoço sai da lista e o total passa a R$ 80.\""
    "\"Dado o mesmo total, quando a estudante toca em Excluir e depois em Cancelar, o almoço continua na lista e o total continua em R$ 100.\""
    "{i}Você roda os dois. Vermelho e vermelho. Justo: a função ainda nem existe.{/i}"

    show st_mobile neutral at left_zoom
    with dissolve
    st_mobile "Vermelho é bom nessa hora, viu? Prova que o teste testa alguma coisa."
    hide st_mobile
    with dissolve

    $ advance_minutes(90)
    "{i}Aos poucos, a exclusão toma forma. Primeiro o caminho de confirmar, depois o de cancelar. Pouco depois do meio-dia, os dois testes ficam verdes.{/i}"
    "{i}O valor segue em centavos, como Otávio pediu na semana da arquitetura: 10000 menos 2000 dá 8000. Nenhum centavo some no caminho.{/i}"
    "{i}O PR fecha com quatro arquivos e menos de cem linhas: a função, a caixa de confirmação, os testes e o texto do botão.{/i}"

    scene bg startup_coworking_tarde
    with dissolve
    $ set_time(14, 0)

    "{i}Depois do almoço, a luz entra laranja pelas janelas em arco. Davi gira a cadeira na sua direção.{/i}"

    show st_mobile neutral at left_zoom
    show st_techlead neutral at right_zoom
    with dissolve

    st_mobile "Seu PR tá na minha fila. Mas antes: abri o meu, da fila de sincronização. Cada lançamento sai do celular com um id único, e o servidor ignora repetição."
    st_mobile "É o fim do almoço duplicado da Bia. Revisa pra mim? Quem chegou agora vê coisa que a gente já não enxerga."

    "{i}Você abre o diff. São seis arquivos, e a lógica do id está clara. Até que uma linha chama sua atenção:{/i}"
    "log.info(\"sync\", estudante.email, gasto.descricao, gasto.valor)"
    "{i}Você procura nos testes. Há o caminho feliz: um lançamento enviado uma vez. Não há nenhum teste que envie o mesmo id duas vezes, justamente o caso do túnel.{/i}"

    show st_techlead thinking at right_zoom
    st_techlead "Não olha pra mim. Hoje quem revisa é você."

    menu:
        "Que comentário você deixa no PR do Davi?"

        "O log grava e-mail, descrição e valor do gasto, que são dados pessoais. Sugiro registrar só o id e o status, e incluir um teste enviando o mesmo id duas vezes.":
            $ st_decidir("st_d16_review", True)
            show st_mobile serious at left_zoom
            st_mobile "Pô, nem vi. Botei esse log pra depurar e esqueci lá."
            st_mobile "E o teste do id repetido é literalmente o motivo do PR existir. Corrigindo."
            show st_techlead neutral at right_zoom
            st_techlead "Problema, motivo e sugestão. Dá vontade de imprimir esse comentário e pendurar na parede."

        "Aprovo: o CI passou e o Davi tem mais experiência.":
            $ st_decidir("st_d16_review", False)
            show st_techlead serious at right_zoom
            st_techlead "O CI passou porque ninguém escreveu o teste que falharia. Ele só confere o que a gente pediu."
            st_techlead "E esse log iria para o serviço de monitoramento, fora da nossa base. Dado financeiro de mil estudantes num lugar que ninguém controla."

        "Comento \"isso está estranho, refaz\".":
            $ st_decidir("st_d16_review", False)
            show st_mobile serious at left_zoom
            st_mobile "Estranho onde? Sem dizer o problema e o motivo, eu fico chutando."
            st_mobile "Posso refazer tudo e deixar o log lá do mesmo jeito."

    if not st_d16_review:
        show st_techlead neutral at right_zoom
        st_techlead "Vamos ler juntos. Primeiro, a linha do log: o que ela grava sobre a Bia?"
        st_techlead "Depois, o túnel: qual teste mostraria que o mesmo lançamento chegando duas vezes vira um gasto só?"

        menu:
            "Como você reescreve o comentário?"

            "Aponto a linha, explico o risco e sugiro a correção.":
                "{i}Você escreve: \"Linha 42: o log grava e-mail, descrição e valor do gasto. São dados pessoais e iriam para o monitoramento. Sugestão: registrar só o id e o status. Falta também um teste que envie o mesmo id duas vezes.\"{/i}"
                show st_mobile neutral at left_zoom
                st_mobile "Agora sim. Sei onde, sei por quê e sei o que fazer. Corrigindo."

    show st_techlead neutral at right_zoom
    st_techlead "Log não é diário. Não escreva nele o que você não mostraria para a Bia."

    $ advance_minutes(70)
    "{i}Mais tarde, chega uma notificação: Davi revisou o seu PR.{/i}"

    show st_mobile thinking at left_zoom
    st_mobile "Teu PR tá ótimo, li em dez minutos. Só um comentário: a função se chama tratarExclusao(). Tratar como? Sugiro excluirGasto()."
    st_mobile "Trocadilho do dia: nome bom poupa comentário. Nome ruim custa reunião."

    menu:
        "Como você responde ao review do Davi?"

        "\"Valeu, ajustei o nome.\"":
            $ add_friendship_point("st_mobile", 1)
            show st_mobile neutral at left_zoom
            st_mobile "Fechou! Aprovado."

        "Explico por que escolhi o nome e pergunto o que ele acha.":
            $ add_friendship_point("st_mobile", 1)
            "{i}Você responde que a função decide entre excluir e manter o gasto. Com o nome excluirGasto(), quem lê pensaria que ela sempre exclui.{/i}"
            show st_mobile neutral at left_zoom
            st_mobile "Discussão boa. Fica o seu, com um comentário explicando os dois caminhos."

        "Ajusto sem responder.":
            show st_mobile neutral at left_zoom
            st_mobile "Tudo certo, mas um \"ok\" ajuda a fechar a conversa."

    hide st_mobile
    hide st_techlead
    with dissolve

    $ set_time(17, 10)
    # Lorena chega e sai da lista de quem pode receber mensagem.
    $ set_available("st_mentora", "st_ceo", "st_estudante")

    show st_qualidade neutral at center_zoom
    with dissolve

    st_qualidade "Cheguei! Tava no primeiro teste de usabilidade com os calouros. O segundo é sexta, e tem cadeira para você."
    st_qualidade "Me passa os dois PRs, que eu trouxe o celular perfeito pra isso."
    "{i}Ela tira da bolsa um Android de entrada, com a tela trincada no canto e pouca memória.{/i}"
    show st_qualidade thinking at center_zoom
    st_qualidade "Primeiro: rede lenta. Segundo: modo avião no meio da exclusão. Terceiro: cancelar, porque usuário desiste o tempo todo."

    scene bg startup_coworking_noite
    with dissolve
    $ advance_minutes(50)

    "{i}As luminárias acendem sobre a mesa longa. Lorena testa em silêncio e anota cada passo no tablet.{/i}"

    show st_mobile neutral at left_zoom
    show st_qualidade neutral at center_zoom
    show st_techlead neutral at right_zoom
    with dissolve

    st_qualidade "Excluí o almoço de R$ 20 com a rede lenta: o total foi para R$ 80. Toquei em Excluir e cancelei: o almoço ficou e o total ficou em R$ 100."
    st_qualidade "Lancei um café de R$ 5 e cortei a rede no meio do envio, igual no túnel. Quando a rede voltou, o app reenviou sozinho. Apareceu um café só."
    st_qualidade "Oxe, passou tudo. E o leitor de tela já fala \"Excluir Almoço, R$ 20\", não só \"botão\"."

    if st_abordagem_primeira == "teste_pr":
        st_mobile "Os testes da manhã já tinham pegado o cancelamento antes de chegar na Lorena. Sobrou tempo até pra eu errar o meu log."
    else:
        st_techlead "A gente perdeu meio dia de manhã, mas os testes cobraram de volta: a Lorena não achou nada para devolver."

    st_techlead "Ninguém fez nada heroico hoje. Foi teste, PR pequeno e revisão. É assim que dá certo."

    $ st_checar_conquistas()

    hide st_mobile
    hide st_qualidade
    hide st_techlead
    with dissolve

    stop music fadeout 1.0
    play music music_home_reflecting fadein 1.5
    scene bg quarto_noite
    with fade
    $ set_time(19, 0)
    $ set_available("all")

    "{i}Em casa, você deixa a mochila na cadeira e abre o beta no celular.{/i}"
    "{i}Há quase cinco semanas, um lanche de R$ 7 apareceu duas vezes dentro de um túnel. Hoje você pediu o teste que impede isso de voltar.{/i}"
    "{i}O resto da semana segue no mesmo ritmo: um cartão de cada vez, um PR pequeno de cada vez.{/i}"
    "{i}Ainda tem gente online. Talvez valha mandar uma mensagem para alguém.{/i}"

    call screen contacts_screen

    stop music fadeout 1.5
    scene black
    with fade

    "{i}Fim da Semana 6\n\nTeste primeiro, PR pequeno, revisão com motivo.{/i}"

    window hide
    pause 1.0

    return
