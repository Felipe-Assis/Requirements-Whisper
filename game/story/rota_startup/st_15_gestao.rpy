# st_15_gestao.rpy
# Rota Startup, semana 5, segunda. Planejamento com capacidade (2 de 4),
# riscos, métrica do demo day e definição de pronto.
# Fonte: docs/rotas/startup.md, seção st_15_gestao.

label st_15_gestao:
    $ set_available("st_estudante")
    $ set_time(9, 30)

    play music music_office_focused fadein 1.0
    scene bg sala_reunioes_manha
    with fade

    "{i}Segunda-feira, semana 5. O aquário do coworking cheira a café recém-passado. É o planejamento do último ciclo antes do lançamento: faltam três semanas.{/i}"

    show st_mentora neutral at left_zoom
    show st_techlead neutral at center_zoom
    show st_mobile neutral at right_zoom
    with dissolve

    st_mentora "Bom dia, gente. Bora começar pelo que dói: quanto cabe nessas três semanas."

    hide st_mentora
    hide st_techlead
    hide st_mobile
    with dissolve

    show expression "images/artifacts/st_quadro_kanban.png" as st_kanban at artefato_tela
    with dissolve

    st_mentora "Esse é o quadro de hoje. A correção do duplicado já está em “Fazendo”, com o id único que o Davi montou na fila."
    st_mentora "Agora a capacidade real. O Davi está sozinho no app. O Otávio divide a semana entre a API e os investidores."
    if st_acordo_opcao == "investigar_agora":
        st_mentora "E, pelo acordo da semana passada, uma dessas semanas do Otávio vai inteira para a investigação da parceria do Open Finance."
    else:
        st_mentora "A importação ficou como investigação, como combinamos. Ela não ocupa vaga neste ciclo. O protótipo do consentimento para o demo day são umas telas sem dados reais, coisa de uma tarde."
    st_mentora "Fazendo a conta com honestidade: além do duplicado, cabem dois itens. Dois. E tem quatro pedidos em cima da mesa."

    hide st_kanban
    with dissolve

    show st_mentora thinking at left_zoom
    show st_qualidade neutral at right_zoom
    with dissolve
    st_qualidade "Primeiro, os quatro pedidos. Segundo, de onde veio cada um. Tem coisa que veio da Bia e das avaliações, e tem coisa que veio de reunião."
    st_mentora "[player_name], monta o plano. Duas vagas. Depois a gente confere junto."

    hide st_qualidade
    with dissolve

    call atividade_planejamento("st_plano", ST_PLANO_ITENS, ST_PLANO_NECESSARIOS, 2) from _st_15_plano_primeiro
    # A atividade tem revisão interna; a conquista olha a primeira conferência,
    # guardada em planejamentos["st_plano"]["primeira_cobertura"].
    $ st_registrar_plano(planejamentos["st_plano"]["primeira_cobertura"])
    $ st_registrar_plano(_return)

label .feedback_plano:
    $ st_plano_selecionados = list(planejamentos["st_plano"]["selecionados"])

    if st_plano_cobertura == len(ST_PLANO_NECESSARIOS):
        show st_mentora neutral at left_zoom
        st_mentora "Confirmar a exclusão, manter o gasto se a pessoa cancelar, e recalcular o total depois de excluir ou sincronizar. É exatamente o que a Bia contou na entrevista."
        st_mentora "Vou mandar o plano pra ela."
        $ advance_minutes(10)
        play sound "audio/effects/cell_vibration.ogg"
        show st_estudante portrait at right_zoom2
        st_estudante "(mensagem) Isso! Se eu desistir de excluir, o gasto fica. Se eu excluir, o total muda na hora. É só isso que eu quero, tipo assim, de verdade."
        hide st_estudante
        st_mentora "Medalhas e compartilhar nas redes podem ter valor um dia. Hoje, não resolvem o problema de ninguém."
    else:
        st_mentora "Antes de fechar, deixa eu mostrar pra quem vai usar."
        $ advance_minutes(10)
        play sound "audio/effects/cell_vibration.ogg"
        show st_estudante portrait at right_zoom2
        if st_plano_cobertura == 0:
            st_estudante "(mensagem) Medalha e post nas redes? Égua. Com esse plano eu ainda veria o almoço duas vezes no total, sem conseguir apagar. Medalha não paga almoço."
        elif 0 not in st_plano_selecionados:
            st_estudante "(mensagem) E se eu tocar em Excluir sem querer? Sem a confirmação, o almoço some sem perguntar, e se eu desistir não tem volta. Aí eu volto pro caderno."
        else:
            st_estudante "(mensagem) Consigo apagar, mas o total não muda? Eu apago o almoço de R$ 20 e continuo vendo R$ 100. Aí não adianta nada."
        hide st_estudante
        show st_mentora serious at left_zoom
        st_mentora "Viu? Cada vaga que foi para um extra tirou uma parte do que a Bia confirmou como necessidade. O extra não é ruim; só não é para agora."
        menu:
            "Refaço o plano com os dois itens que a Bia confirmou como necessidade.":
                pass
        call atividade_planejamento("st_plano", ST_PLANO_ITENS, ST_PLANO_NECESSARIOS, 2) from _st_15_plano_revisao
        $ st_registrar_plano(_return)
        jump .feedback_plano

    hide st_estudante
    $ advance_minutes(25)

    show st_mentora neutral at left_zoom
    show st_mobile thinking at right_zoom
    with dissolve
    st_mentora "Plano fechado. Agora a parte que ninguém gosta: o que pode dar errado nessas três semanas."
    st_mobile "Pô, dá pra fazer uma lista de cem coisas."
    st_mentora "Por isso mesmo. [player_name], como a gente trata os riscos?"

    menu:
        "Como tratar os riscos destas três semanas?"

        "Registrar cada risco com dono, gatilho e plano: pico de cadastros no semestre, revisão das lojas e textos de privacidade.":
            $ st_decidir("st_d15_riscos", True)
            st_mentora "Isso. Poucos riscos, cada um com alguém cuidando."

        "Resolver os riscos quando aparecerem; somos rápidos.":
            $ st_decidir("st_d15_riscos", False)
            show st_mobile serious at right_zoom
            st_mobile "A revisão da loja pode levar dias. Se rejeitarem na véspera, a gente lança depois que os calouros já escolheram outro app."
            st_mobile "Rapidez não resolve o que depende dos outros."
            menu:
                "Escolho os riscos que podem atrasar o lançamento e dou um dono e um gatilho para cada um.":
                    st_mentora "Isso. Poucos riscos, cada um com alguém cuidando."

        "Fazer uma planilha com todos os riscos possíveis, sem dono.":
            $ st_decidir("st_d15_riscos", False)
            show st_qualidade serious at center_zoom
            with dissolve
            st_qualidade "Sessenta linhas que ninguém abre. Risco sem dono é decoração."
            hide st_qualidade
            with dissolve
            menu:
                "Escolho os riscos que podem atrasar o lançamento e dou um dono e um gatilho para cada um.":
                    st_mentora "Isso. Poucos riscos, cada um com alguém cuidando."

    show st_mobile neutral at right_zoom
    "{i}Tainá escreve três linhas no quadro:{/i}"
    "Pico de cadastros no início do semestre. Dono: Otávio. Gatilho: a lista passar de 2 segundos no teste de carga da semana 7. Plano: ajustar a API e o banco antes da semana 8."
    "Revisão das lojas. Dono: Davi. Gatilho: qualquer rejeição. Plano: enviar a versão com uma semana de folga."
    "Textos de consentimento e privacidade. Dono: Otávio. Gatilho: qualquer texto novo sobre dados. Plano: revisão dele antes de ir para a loja."
    st_mobile "Três linhas. Essas eu leio."

    hide st_mentora
    hide st_mobile
    with dissolve

    $ set_time(11, 20)
    "{i}A porta de vidro se abre. Vinícius entra com o notebook debaixo do braço.{/i}"

    show st_ceo neutral at right_zoom
    with dissolve
    st_ceo "Bom dia! Preciso fechar o slide principal do demo day. Qual número eu mostro?"

    hide st_ceo
    with dissolve
    show expression "images/artifacts/st_painel_metricas.png" as st_painel at artefato_tela
    with dissolve
    "{i}O painel aparece no telão: cadastros subindo depois da festa dos mil. Ao lado, a retenção de 30 dias, parada em 22%%.{/i}"
    hide st_painel
    with dissolve

    show st_ceo thinking at right_zoom
    show st_qualidade thinking at left_zoom
    with dissolve
    st_ceo "O gráfico de cadastros é lindo, né? Mas a Lorena me lembrou da retenção na sexta. [player_name], qual número a gente leva?"

    menu:
        "Que métrica Vinícius deve mostrar no demo day?"

        "Total de downloads.":
            $ st_decidir("st_d15_metrica", False)
            show st_qualidade serious at left_zoom
            st_qualidade "Download sobe com anúncio e com festa de mil cadastros. Não mostra se o app ajudou alguém."
            st_qualidade "Cadê a evidência de que a pessoa voltou?"
            menu:
                "Escolho um número que mostre se o estudante voltou e confiou no total.":
                    show st_ceo neutral at right_zoom
                    st_ceo "Gente voltando e confiando. Isso responde a pergunta que todo fundo faz."

        "Retenção semanal (estudantes que voltam a lançar gastos) e quantos fecharam o mês com o total conferido.":
            $ st_decidir("st_d15_metrica", True)
            show st_ceo neutral at right_zoom
            st_ceo "Isso responde a pergunta que todo fundo faz: as pessoas voltam?"

        "Número de funcionalidades entregues.":
            $ st_decidir("st_d15_metrica", False)
            show st_techlead serious at center_zoom
            with dissolve
            st_techlead "Mede nosso esforço, não o resultado de quem usa. Podemos entregar vinte coisas e a Bia continuar no caderno."
            hide st_techlead
            with dissolve
            menu:
                "Escolho um número que mostre se o estudante voltou e confiou no total.":
                    show st_ceo neutral at right_zoom
                    st_ceo "Gente voltando e confiando. Isso responde a pergunta que todo fundo faz."

    show st_qualidade neutral at left_zoom
    st_qualidade "Pra medir o total conferido, no fim do mês o app pergunta: “Seu total bate com o que você gastou?”. Um toque, sim ou não. Dá pra contar."
    st_ceo "Downloads eu mostro num slide pequeno. O grande fica pra retenção. Fechado!"

    hide st_ceo
    with dissolve

    show st_mentora neutral at center_zoom
    with dissolve
    st_qualidade "Mais uma coisa, antes de todo mundo levantar. Quero mudar a nossa definição de pronto."
    st_qualidade "Primeiro: um cartão só está pronto se o teste do caso limite passou. Cancelar a exclusão e o total continuar em R$ 100."
    st_qualidade "Segundo: o botão Excluir precisa ter um nome que o leitor de tela fale. Hoje ele é só um ícone de lixeira."
    st_mentora "Aprovado. Escreve no quadro, Lorena."

    $ registrar("st_reg_metricas")

    hide st_mentora
    hide st_qualidade
    with dissolve

    # Tarde: quadro atualizado e conversa com a Tainá.
    $ set_time(15, 40)
    scene bg startup_coworking_tarde
    with fade

    "{i}À tarde, o quadro está diferente. Os dois cartões escolhidos estão em “Pronto para desenvolver”. Medalhas e redes sociais foram para uma coluna nova, “Depois da 1.0”.{/i}"
    "{i}Você confere a lista de riscos colada ao lado. Davi já marcou na agenda a data de envio às lojas, com uma semana de folga.{/i}"

    show st_mentora thinking at center_zoom
    with dissolve
    st_mentora "Ei, [player_name]. Antes de você ir: como você tá com essa pressão toda? Três semanas, lojas, demo day..."

    menu:
        "Como você responde à Tainá?"

        "“Com honestidade: a ansiedade aparece, mas o plano ajudou.”":
            $ add_friendship_point("st_mentora", 1)
            show st_mentora neutral at center_zoom
            st_mentora "Obrigada por falar. Ansiedade dita em voz alta vira ajuste."
            st_mentora "E se apertar, me chama. Prefiro tirar um item do plano a perder alguém do time."

        "“Tudo tranquilo!”":
            show st_mentora neutral at center_zoom
            st_mentora "Que bom. Se mudar, me fala."

    $ st_checar_conquistas()
    $ set_time(16, 0)

    hide st_mentora
    with dissolve

    # Volta para casa.
    $ set_available("all")
    $ set_time(19, 30)
    play music music_home_reflecting fadein 1.5
    scene bg quarto_noite
    with fade

    "{i}Em casa, você abre o notebook e relê o plano do dia. Dois itens. Parecia pouco de manhã; agora parece a escolha certa.{/i}"
    "{i}Na disciplina, gerência de projeto era um capítulo de cronogramas. Na Trocado, foi dizer não para medalhas, com motivo, e escolher um número que mostre se a vida da Bia melhorou.{/i}"
    "{i}O celular está ao lado do teclado. Talvez valha conversar com alguém antes de dormir.{/i}"

    call screen contacts_screen

    play music music_home_dreamy fadein 1.0
    scene black
    with fade
    window hide
    pause 1.1
    window show

    "{i}Fim da Semana 5\n\nCapacidade é finita: escolher é dizer não com motivo. E métrica boa mostra se a vida de alguém melhorou.{/i}"

    return
