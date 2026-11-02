# st_17_testes_seguranca.rpy
# Rota Startup, ato 5, semana 7 (quarta). Fonte: docs/rotas/startup.md, st_17.
# Pirâmide de testes, teste de carga, token do Open Finance e exclusão de conta.

label st_17_testes_seguranca:
    # Lorena e Otávio estão na sala.
    $ set_available("st_mentora", "st_mobile", "st_ceo", "st_estudante")
    $ set_time(9, 0)

    play music music_office_concentrated_2 fadein 1.0
    scene bg startup_coworking_manha
    with fade

    "{i}Semana 7, quarta-feira. Falta uma semana para o começo do semestre. No quadro Kanban, a coluna \"Revisão\" está cheia e a \"Fazendo\" quase vazia.{/i}"
    "{i}Lorena já está na mesa longa, com o tablet apoiado numa pilha de livros e três celulares de teste em fila. Otávio, na ponta, lê alguma coisa com a caneca na mão.{/i}"

    show st_qualidade neutral at left_zoom
    show st_techlead neutral at right_zoom
    with dissolve

    st_qualidade "Bom dia, [player_name]! Senta aqui. Hoje é dia de plano de testes, e eu trouxe desenho."
    if energia_cansaco():
        st_qualidade "Oxe, cansaço dá pra ver de longe. Primeiro: água. Segundo: começamos pelo que é rápido. Terceiro: ninguém fica depois das seis."
    show st_qualidade thinking at left_zoom
    "{i}Ela vira o tablet. Na tela, um triângulo dividido em três faixas.{/i}"
    st_qualidade "Primeiro, a base: muitos testes de unidade. São rápidos e rodam a cada PR. É ali que mora o \"R$ 100 vira R$ 80\" que você escreveu."
    st_qualidade "Segundo, o meio: alguns testes de integração, com o app falando com a API de verdade. É onde aparece o id repetido chegando duas vezes."
    st_qualidade "Terceiro, o topo: poucos testes de ponta a ponta no celular. São lentos e quebram à toa, então ficam só os caminhos que não podem falhar."
    st_qualidade "Fora do triângulo, mas na lista: teste exploratório em modo avião, leitor de tela no botão Excluir e um teste de carga."
    if rast_lacuna_achada("st_rast_exclusao"):
        st_qualidade "E o teste do C4, o total depois da sincronização, que você achou sem teste no quadro. Escrevo à tarde, depois do exploratório."
    st_qualidade "Esse último é seu. Quarta que vem o semestre começa e os calouros chegam. Como a gente testa o pico?"
    call pista_lembrar("st_p_conexoes") from _pl_st17_carga

    menu (tipo="trabalho"):
        "Como testar o pico do início do semestre?"

        "Simular dez vezes os cadastros e lançamentos de um dia normal, concentrados no horário do almoço, medindo se a lista abre em até 2 segundos.":
            $ st_decidir("st_d17_carga", True)
            show st_qualidade neutral at left_zoom
            st_qualidade "Isso. Volume real, horário real e uma meta para comparar. Sem meta, teste vira opinião."
            st_qualidade "O bandejão abre às 11h30. É ali que todo mundo lança o almoço ao mesmo tempo."

        "Pedir para cinco colegas abrirem o app ao mesmo tempo.":
            $ st_decidir("st_d17_carga", False)
            show st_qualidade serious at left_zoom
            st_qualidade "Cinco pessoas não são o pico de mil calouros. O teste passa e não diz nada."
            st_qualidade "Pior: a gente sai daqui achando que está tudo bem."

        "Não precisa: serverless escala sozinho.":
            $ st_decidir("st_d17_carga", False)
            show st_techlead serious at right_zoom
            st_techlead "Escala, sim. As funções. O banco, não."
            st_techlead "Mil funções abrindo conexão ao mesmo tempo derrubam o banco. É como abrir mil torneiras numa casa com um cano só."

    if not st_d17_carga:
        show st_qualidade thinking at left_zoom
        st_qualidade "Vamos montar juntos. Primeiro, quanto: um dia normal tem uns três mil lançamentos, então o pico é dez vezes isso."
        st_qualidade "Segundo, quando: na hora do almoço. Terceiro, contra o quê: os 2 segundos da lista que a gente escreveu lá na classificação."

        menu (tipo="trabalho"):
            "O que você ajusta no teste de carga?"

            "Reproduzo o volume e o horário do pico e meço contra a meta de 2 segundos.":
                show st_qualidade neutral at left_zoom
                st_qualidade "Agora o resultado diz alguma coisa, passe ou falhe. Roda à tarde, depois dos outros testes."

    if st_d17_carga:
        $ advance_minutes(100)
        "{i}O teste roda enquanto vocês seguem com a lista. Às 10h40, no meio do almoço simulado, o gráfico do banco encosta no teto.{/i}"
        show st_techlead thinking at right_zoom
        st_techlead "Limite de conexões. Exatamente o que eu temia. Melhor descobrir hoje do que na quarta que vem."
        st_techlead "Vou pôr um limite nas funções. Elas esperam a vez em vez de afogar o banco."
    else:
        $ advance_minutes(60)

    show st_techlead neutral at right_zoom
    st_techlead "Agora a parte que mais me tira o sono."

    if st_acordo_opcao == "investigar_agora":
        st_techlead "A investigação da parceria terminou. A importação bancária não entra na 1.0, mas o desenho dela fica pronto agora, e ele começa pela segurança."
    else:
        st_techlead "A importação bancária ainda é só protótipo. Não entra na 1.0. Mas, veja bem, onde guardar a chave se decide antes de construir a casa."

    st_techlead "A Bia não digita a senha do banco no nosso app. Nunca. O app manda ela para o próprio banco, e lá ela autoriza: o que compartilhar, para quê e por quanto tempo."
    st_techlead "Isso é o consentimento do Open Finance. Tem finalidade, tem prazo e pode ser revogado quando ela quiser."
    st_techlead "Em troca, a gente recebe um token: uma chave temporária que só abre o extrato, e só pelo tempo combinado. A pergunta é onde guardar essa chave."

    menu (tipo="trabalho"):
        "Onde guardar o token de acesso da importação bancária?"

        "No armazenamento seguro do sistema do celular (Keychain no iPhone, Keystore no Android), com validade curta; o app nunca pede senha do banco.":
            $ st_decidir("st_d17_token", True)
            st_techlead "Isso. O cofre do sistema é feito para guardar chave. Se o celular for perdido, a chave vence logo e a Bia revoga no banco."

        "No armazenamento comum do app, para facilitar.":
            $ st_decidir("st_d17_token", False)
            show st_techlead serious at right_zoom
            st_techlead "Facilita para todo mundo, inclusive para quem não devia."
            st_techlead "Qualquer backup ou celular desbloqueado expõe o token. Com ele, alguém lê o extrato da Bia."

        "Pedir a senha do banco e guardá-la criptografada no servidor.":
            $ st_decidir("st_d17_token", False)
            show st_techlead serious at right_zoom
            st_techlead "Open Finance existe justamente para ninguém precisar da senha."
            st_techlead "Guardar senha de banco é o pior risco que a gente poderia criar. E quebra a confiança que a Bia pediu desde a entrevista."

    if not st_d17_token:
        show st_techlead thinking at right_zoom
        st_techlead "Pensa em quem tem a chave. A senha fica com a Bia e com o banco. O token fica no lugar que o sistema do celular protege. E tudo tem validade."

        menu (tipo="trabalho"):
            "O que você decide?"

            "Uso o cofre do sistema e o consentimento da instituição, sem senha.":
                show st_techlead neutral at right_zoom
                st_techlead "Isso. Dado que você não guarda não vaza. E chave guardada no cofre vaza bem menos."

    $ advance_minutes(25)
    play sound "audio/effects/cell_vibration.ogg"
    "{i}Seu celular vibra. É a Bia.{/i}"

    show st_estudante portrait at center_zoom
    with dissolve
    st_estudante "(mensagem) Oi! Tipo assim: uma amiga da república perguntou e eu fiquei sem saber. Se eu apagar minha conta, meus gastos somem mesmo?"
    hide st_estudante
    with dissolve

    show st_qualidade neutral at left_zoom
    st_qualidade "Pergunta ótima. E não é só resposta: é comportamento do app. O que acontece quando ela apaga a conta?"

    menu (tipo="trabalho"):
        "O que acontece quando a Bia apaga a conta?"

        "Apagar conta e dados financeiros no prazo do RNF02, revogar consentimentos, manter só o que a lei obriga, e explicar isso a ela.":
            $ st_decidir("st_d17_exclusao", True)
            st_techlead "Exato. Até 15 dias, como está no RNF02. Se existir consentimento com banco, ele é revogado junto. Fica só o que a lei manda guardar, como os registros de acesso, e mais nada."
            st_qualidade "E a gente diz isso para ela com as mesmas palavras na tela de exclusão. Promessa escrita tem que ser promessa cumprida."

        "Desativar a conta, mas manter os gastos para métricas.":
            $ st_decidir("st_d17_exclusao", False)
            show st_techlead serious at right_zoom
            st_techlead "Contradiz o RNF02 e a LGPD. Lembra da inspeção? Foi exatamente esse o conflito."
            st_techlead "E as lojas exigem que app com cadastro ofereça exclusão de conta de verdade. Sem isso, a 1.0 nem passa na revisão."

        "Apagar só do celular dela.":
            $ st_decidir("st_d17_exclusao", False)
            show st_qualidade serious at left_zoom
            st_qualidade "No servidor continua tudo. Ela acha que apagou e não apagou."
            st_qualidade "Oxe, isso é pior do que não ter o botão."

    if not st_d17_exclusao:
        show st_techlead thinking at right_zoom
        st_techlead "Vamos por partes. Onde estão os gastos da Bia? No celular e no servidor. O que ela autorizou no banco? O consentimento. O que a lei obriga a guardar? Os registros de acesso que o Marco Civil pede por seis meses, e quase nada além disso."

        menu (tipo="trabalho"):
            "Como fica a exclusão de conta?"

            "Apago nos dois lugares, revogo o consentimento e confirmo para a Bia.":
                show st_techlead neutral at right_zoom
                st_techlead "Isso. E vira uma tela de verdade: Configurações, Minha conta, Excluir conta. Com o prazo escrito."

    "{i}Você responde à Bia: a conta e os gastos são apagados em até 15 dias, qualquer autorização de banco é cancelada junto, e o app vai mostrar isso antes de ela confirmar.{/i}"

    show st_estudante portrait at center_zoom
    with dissolve
    st_estudante "(mensagem) Égua, que bom. Então apaga de verdade. Posso falar pras meninas sem medo."
    hide st_estudante
    with dissolve

    $ registrar("st_reg_lgpd")
    $ st_checar_conquistas()

    st_techlead "Dado financeiro é emprestado. Guarda pouco, protege bem e devolve quando pedirem."

    hide st_qualidade
    hide st_techlead
    with dissolve

    # Tempo livre da semana 7, no almoço (quarta, 11h30-14h30).
    call im_intermissao(7) from _im_startup_s7

    scene bg startup_coworking_tarde
    with dissolve
    $ set_time(14, 30)

    "{i}À tarde, Lorena passa para o teste exploratório. Liga e desliga o modo avião, lança, exclui, cancela.{/i}"
    $ advance_minutes(50)
    "{i}Às 15h20, ela para.{/i}"

    show st_qualidade serious at left_zoom
    with dissolve
    st_qualidade "Achei uma. Lancei o bandejão, R$ 4,50, em modo avião. Liguei a rede. O gasto aparece na lista, mas o total continua o de antes."
    st_qualidade "Só atualiza se eu fechar e abrir o app. Para a Bia, é o \"meu total está errado\" de novo."
    if not rast_lacuna_achada("st_rast_exclusao"):
        st_qualidade "Oxe, espera. Lembra do quadro da semana passada? O C4: total depois da sincronização offline. Nenhum teste cobria. O bug morava nesse elo."

    menu (tipo="conversa"):
        "Como você ataca o bug do modo avião?"

        "Peço à Lorena para reproduzirmos juntos.":
            $ add_friendship_point("st_qualidade", 1)
            show st_qualidade neutral at left_zoom
            st_qualidade "Bora. Primeiro o que eu fiz, segundo o que aconteceu, terceiro o que eu esperava."
            "{i}Na terceira tentativa vocês veem o padrão: a sincronização termina, mas a tela do total não fica sabendo. Ela só calcula quando abre.{/i}"
            "{i}Você faz o total recalcular quando a sincronização termina e escreve um teste para esse caminho. Às 18h, o bandejão aparece e o total sobe na hora.{/i}"
            st_qualidade "Bug com passo a passo é bug pela metade."
            $ set_time(18, 30)

        "Peço ao Otávio para olhar os logs da sincronização comigo.":
            $ add_friendship_point("st_techlead", 1)
            show st_techlead neutral at right_zoom
            with dissolve
            st_techlead "Vamos ver. E repara: graças ao seu review, o log só tem id e status. Dá para ler sem ver a vida de ninguém."
            "{i}Os logs mostram que o gasto chega ao servidor e volta confirmado. O problema está no celular: a tela do total não escuta o fim da sincronização.{/i}"
            "{i}Você faz o total recalcular nesse momento e escreve um teste para esse caminho. Às 18h, o bug está corrigido.{/i}"
            st_techlead "Viu? Log bom conta o que aconteceu sem contar demais."
            $ set_time(18, 30)

        "Tento resolver por conta própria até tarde.":
            "{i}Você mergulha no código. Lorena vai embora às 18h, Otávio logo depois. A luz laranja some das janelas.{/i}"
            scene bg startup_coworking_noite
            with dissolve
            $ set_time(20, 0)
            $ energia_gastar(2, _("ficou até tarde sozinho"))
            $ im_hora_extra_somar(60)
            "{i}Às 20h, o bug continua lá. O celular vibra.{/i}"
            show st_qualidade portrait at center_zoom
            with dissolve
            st_qualidade "(mensagem) Ainda aí? Pedir ajuda cedo é técnica, não fraqueza. Amanhã às 9h a gente reproduz junto."
            hide st_qualidade
            with dissolve
            "{i}Você fecha o notebook e vai para casa. O bug fica para amanhã, agora com companhia.{/i}"

        "Rodar o teste que você pediu na semana passada" (tipo="pista") if rast_lacuna_achada("st_rast_exclusao"):
            $ add_friendship_point("st_qualidade", 0.5)
            "{i}A Lorena tinha acabado de escrever o teste do C4. Ele falha em três segundos, sempre no mesmo passo: a sincronização termina e a tela do total não fica sabendo.{/i}"
            "{i}Às 16h, o total sobe na hora e o teste fica verde. Ele fica no conjunto de testes de vez.{/i}"
            st_qualidade "Critério com teste é bug com endereço. Sobrou a tarde pro leitor de tela."
            $ set_time(18, 30)

        "Peço os logs ao Otávio e conferimos também o relatório de falhas que mandava o e-mail" (tipo="pista") if pista_tem("st_p_logs"):
            $ pista_usar("st_p_logs")
            $ add_friendship_point("st_techlead", 1)
            show st_techlead neutral at right_zoom
            with dissolve
            "{i}Os logs mostram que o gasto chega ao servidor e volta confirmado. O problema está no celular: a tela do total não escuta o fim da sincronização.{/i}"
            "{i}Você faz o total recalcular nesse momento e escreve um teste para esse caminho. Enquanto isso, Otávio abre o relatório de falhas do app.{/i}"
            st_techlead "E o relatório de falhas... olha aí: o e-mail em cada erro, indo para o monitoramento. O log o Davi limpou; esse aqui ficou."
            st_techlead "Corrijo agora, antes da 1.0. Dado que você não manda não vaza."
            "{i}Às 18h, o bug está corrigido e o relatório de falhas passa a mandar só o tipo do erro e a versão do app.{/i}"
            $ set_time(18, 30)

    stop music fadeout 1.0
    play music music_home_reflecting fadein 1.5
    scene bg quarto_noite
    with fade
    $ advance_minutes(30)
    $ set_available("all")

    "{i}Em casa, você pensa na pergunta da Bia. Uma frase curta, de quem só quer ter certeza.{/i}"
    "{i}Na faculdade, LGPD era um capítulo de prova. Hoje foi uma estudante perguntando se os gastos dela somem de verdade.{/i}"
    "{i}Ainda tem gente online. Talvez valha conversar com alguém antes de dormir.{/i}"

    call screen contacts_screen

    stop music fadeout 1.5
    scene black
    with fade

    "{i}Fim da Semana 7\n\nTeste o pico antes que ele chegue. Dado financeiro é emprestado: guarde pouco, proteja bem e devolva quando pedirem.{/i}"

    window hide
    pause 1.0

    return
