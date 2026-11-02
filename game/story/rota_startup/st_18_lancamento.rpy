# st_18_lancamento.rpy
# Rota Startup, ato 5, semana 8. Fonte: docs/rotas/startup.md, st_18 e seção 6.
# Lojas e rollout (segunda), pico do semestre (quarta), demo day e final (quinta).

label st_18_lancamento:
    # Segunda: equipe completa na sala; os stakeholders estão fora.
    $ set_available("st_ceo", "st_estudante")
    $ set_time(9, 0)

    play music music_office_motivated fadein 1.0
    scene bg startup_coworking_manha
    with fade

    "{i}Semana 8, segunda-feira. A última.{/i}"
    "{i}Alguém pendurou uma folha no quadro Kanban, escrita à mão com caneta coral: \"1.0\". Embaixo, a palavra \"quarta\", sublinhada duas vezes.{/i}"

    show st_mentora neutral at left_zoom
    show st_mobile neutral at center_zoom
    show st_techlead neutral at right_zoom
    with dissolve

    st_mentora "Bom dia, gente! Bora, que hoje a 1.0 sai de casa."
    st_mentora "A versão foi para a revisão das lojas na quarta passada, como a gente combinou nos riscos. Falta decidir como liberar."
    st_mobile "Quarta o semestre começa. Os calouros chegam, baixam três apps de finanças e ficam com um. Tem que ser o nosso."
    st_techlead "E na quinta tem demo day. Muita coisa numa semana só. Veja bem, [player_name]: como você soltaria essa versão?"

    menu:
        "Como liberar a 1.0?"

        "Enviar às lojas com antecedência, liberar aos poucos (10%%, depois 50%%, depois 100%%), deixar o que é novo atrás de feature flag e acompanhar falhas e o tempo de abertura da lista.":
            $ st_decidir("st_d18_rollout", True)
            show st_techlead neutral at right_zoom
            st_techlead "Isso. Se der problema com 10%%, atinge poucos, a gente desliga a novidade e respira."
            st_mobile "E a flag deixa eu desligar a exclusão nova sem mandar outra versão pra loja. Fechou."

        "Liberar para 100%% hoje à noite, de uma vez, para os números subirem antes do demo day.":
            $ st_decidir("st_d18_rollout", False)
            show st_techlead serious at right_zoom
            st_techlead "De uma vez e à noite, não. Lembra do meu causo de 2009? Foi assim: tudo junto, fora de hora."
            st_techlead "Se der problema, atinge todo mundo de madrugada, sem ninguém de plantão, na véspera do semestre. E não dá para desfazer uma versão instalada: quem atualizou fica com o bug até a próxima passar na loja."

        "Esperar o demo day passar para lançar com calma.":
            $ st_decidir("st_d18_rollout", False)
            show st_mentora serious at left_zoom
            st_mentora "O semestre começa na quarta. É quando o estudante decide como vai controlar o dinheiro."
            st_mentora "Se a gente lança depois, perde a janela. E o Vinícius sobe no palco sem nada novo nas mãos."

    if not st_d18_rollout:
        show st_mobile thinking at center_zoom
        st_mobile "Pensa no celular de mil pessoas. Não dá pra dar F5. O que você quer é poder ver o problema cedo e desligar rápido."
        st_mentora "E sem perder a quarta-feira."

        menu:
            "O que você ajusta no lançamento?"

            "Libero em etapas, com a novidade desligável e o painel aberto.":
                show st_mentora neutral at left_zoom
                st_mentora "Isso. Dez por cento hoje, metade amanhã, todo mundo na quarta cedo, se o painel deixar."

    show st_mobile neutral at center_zoom
    st_mobile "Só um detalhe de loja: no Google eu escolho a porcentagem. Na Apple, a liberação em fases segue um calendário de sete dias."
    st_mobile "Então quem manda no ritmo é a flag. A exclusão nova liga para 10%%, depois 50%%, depois todo mundo, sem mandar versão nova."

    $ advance_minutes(120)
    "{i}Às 11h, chega o primeiro e-mail: a loja da Apple aprovou a 1.0.{/i}"
    $ advance_minutes(20)
    "{i}Às 11h20, o segundo. A loja do Google pede uma coisa antes de aprovar: o caminho para excluir a conta precisa estar dentro do app.{/i}"

    hide st_mentora
    show st_qualidade neutral at left_zoom
    with dissolve

    if st_d17_exclusao:
        st_qualidade "Oxe, mas já está lá! Configurações, Minha conta, Excluir conta. A gente fez semana passada por causa da pergunta da Bia."
        st_techlead "Mando o passo a passo com as telas. Às vezes o revisor só não achou."
        "{i}Às 16h, a loja do Google aprova. Às 17h, a 1.0 chega a 10%% dos estudantes.{/i}"
    else:
        st_techlead "Está quase. A tela existe desde que a gente revisou o que acontece quando a Bia apaga a conta. Falta o atalho no menu e o texto com o prazo."
        st_mobile "Meio dia de ajuste. Dá tempo."
        "{i}Davi termina o ajuste no fim da tarde. A loja do Google aprova na terça cedo, e a 1.0 chega a 10%% dos estudantes logo depois.{/i}"

    "{i}Na terça, o painel fica limpo: nenhuma falha nova, a lista abrindo em menos de 2 segundos. Metade dos estudantes recebe a 1.0 à tarde, e o restante na quarta às 8h.{/i}"

    hide st_mentora
    hide st_mobile
    hide st_techlead
    hide st_qualidade
    with dissolve

    play music music_office_concentrated_2 fadein 1.0
    scene bg startup_coworking_tarde
    with fade
    $ set_time(12, 0)

    "{i}Quarta-feira, meio-dia. Primeiro dia do semestre.{/i}"

    show expression "images/artifacts/st_painel_metricas.png" as tela_painel at center_zoom
    with dissolve
    "{i}No painel, a linha de cadastros faz uma curva para cima perto do almoço. Em uma hora, chegam oito vezes mais cadastros do que num dia comum.{/i}"
    hide tela_painel
    with dissolve

    show st_qualidade thinking at left_zoom
    show st_techlead thinking at right_zoom
    with dissolve

    if st_d17_carga:
        st_techlead "Veja bem: igualzinho ao teste da semana passada. O banco está usando metade das conexões. O limite que a gente pôs segura o resto."
        st_qualidade "Lista abrindo em 1,4 segundo no celular de entrada. Nenhuma reclamação nova na loja."
        $ advance_minutes(40)
        "{i}Às 12h40 o pico passa, e ninguém precisou fazer nada. É a melhor coisa que pode acontecer num pico.{/i}"
    else:
        $ advance_minutes(15)
        "{i}Às 12h15, o tempo de abertura da lista sobe de 2 para 6 segundos.{/i}"
        show st_mobile serious at center_zoom
        with dissolve
        st_mobile "Mano, tá lento. Tô vendo gente reclamando no grupo da república da Bia."
        st_techlead "O banco está no limite de conexões. O teste que a gente refez semana passada mostrou isso, mas o ajuste ficou na fila. Faltou aplicar antes do pico."
        "{i}Otávio aplica o limite de conexões nas funções. Vinte minutos depois, a lista volta a abrir em 1,6 segundo.{/i}"
        $ advance_minutes(20)
        st_qualidade "Ninguém perdeu dado. Mas foram vinte minutos de gente esperando no bandejão."
        st_techlead "Anota para a retrospectiva: teste que acha problema só ajuda se a correção entrar antes do pico."
        hide st_mobile

    hide st_qualidade
    hide st_techlead
    with dissolve

    # Quinta: todos estão juntos no demo day.
    $ set_available()
    scene bg transito_tarde
    with fade
    $ set_time(14, 20)

    "{i}Quinta-feira. A equipe vai de ônibus até a Aceleradora Maré. Davi segura o celular da demo com as duas mãos, como quem carrega um bolo.{/i}"
    "{i}Na altura do túnel, todo mundo fica quieto. O sinal some e volta. Lorena lança um café de R$ 5 de propósito. Aparece uma vez só.{/i}"

    scene bg demo_day_auditorio
    with fade
    $ set_time(15, 0)

    "{i}O auditório é pequeno e está cheio. No telão, a logo da aceleradora. Na primeira fila, gente de fundo de investimento com caderno no colo.{/i}"

    show st_ceo neutral at left_zoom
    show st_estudante neutral at right_zoom
    with dissolve

    st_ceo "Time! Faltam vinte minutos. Somos a quarta startup. Eu tô ótimo. Tô ótimo, né?"
    st_estudante "Eu é que vou subir num palco pela primeira vez, e você que tá nervoso?"

    hide st_ceo
    hide st_estudante
    with dissolve

    menu:
        "Antes do pitch, quem você ajuda?"

        "Ensaio a fala da Bia com a Tainá.":
            $ add_friendship_point("st_mentora", 1)
            show st_mentora neutral at left_zoom
            show st_estudante neutral at right_zoom
            with dissolve
            st_mentora "Conta como contou pra gente na entrevista, Bia. Com o valor e com o ônibus. Não precisa enfeitar."
            st_estudante "R$ 20 do almoço. Isso eu não esqueço nunca."

        "Confiro o painel de métricas com o Otávio.":
            $ add_friendship_point("st_techlead", 1)
            show st_techlead neutral at right_zoom
            with dissolve
            st_techlead "Número no telão tem que bater com o número no banco. Investidor pergunta, e a gente responde com a mesma consulta."
            "{i}Vocês conferem os números um por um. Batem.{/i}"

        "Testo o celular da demo com o Davi.":
            $ add_friendship_point("st_mobile", 1)
            show st_mobile neutral at center_zoom
            with dissolve
            st_mobile "Bateria cheia, modo não perturbe, Wi-Fi do auditório desligado. Se a rede cair, melhor: é a nossa demo."
            st_mobile "Trocadilho de palco: esse app não dá branco, dá saldo."

        "Reviso com a Lorena se os slides têm contraste e legenda.":
            $ add_friendship_point("st_qualidade", 1)
            show st_qualidade thinking at left_zoom
            with dissolve
            st_qualidade "Primeiro, o gráfico verde em fundo verde: troca. Segundo, o vídeo da demo: legenda. Terceiro, tem gente no fundo da sala: fonte maior."
            st_qualidade "Pronto. Agora todo mundo consegue ler, não só quem sentou na frente."

    hide st_mentora
    hide st_techlead
    hide st_mobile
    hide st_qualidade
    hide st_estudante
    with dissolve

    $ advance_minutes(25)
    "{i}As luzes baixam. Vinícius sobe ao palco.{/i}"

    show st_ceo neutral at center_zoom
    with dissolve

    st_ceo "Boa tarde! Eu quase larguei a faculdade por falta de dinheiro. A Trocado é o app que eu queria ter tido."
    st_ceo "Poderia mostrar cadastros. Hoje são mais de três mil, depois de ontem. Mas número de cadastro sobe com festa e com anúncio."
    st_ceo "O que importa é quem volta. Desde que a correção do lançamento duplicado chegou ao beta, a retenção semanal subiu de 41%% para 57%%. E 312 estudantes fecharam o último mês com o total conferido."

    "{i}É a métrica que vocês combinaram na semana 5, no aquário. Na plateia, alguém anota.{/i}"

    if st_acordo_opcao == "investigar_agora":
        st_ceo "Próximo passo: importação bancária via Open Finance. Passamos uma semana investigando a parceria. O parceiro autorizado existe. Ela entra depois do semestre, começando pelo consentimento."
    else:
        st_ceo "Próximo passo: importação bancária via Open Finance. Hoje mostro só o protótipo do consentimento, sem dados reais. Data? Quando estiver redondo."

    st_ceo "Mas quem melhor explica a Trocado não sou eu."

    hide st_ceo
    show st_estudante neutral at center_zoom
    with dissolve

    st_estudante "Oi. Eu sou a Bia, faço Engenharia Ambiental e sou bolsista."
    st_estudante "Uns dois meses atrás, lancei o almoço de R$ 20 no ônibus. A internet caiu, toquei de novo, e o almoço apareceu duas vezes. Achei que tinha perdido dinheiro. Desinstalei por três dias."
    st_estudante "Semana passada lancei o bandejão, R$ 4,50, dentro do túnel. Apareceu uma vez só. E quando lancei errado, consegui apagar."
    st_estudante "Tipo assim: eu só quero saber quanto sobra até a bolsa cair. Agora eu sei."

    "{i}O auditório aplaude. Davi bate palma mais alto que todo mundo.{/i}"

    hide st_estudante
    with dissolve

    $ st_checar_conquistas(final=True)

    $ advance_minutes(60)
    "{i}Depois das apresentações, a equipe se junta no corredor, entre copos de café e crachás pendurados.{/i}"

    if st_final_grade() == "excelente":
        show st_estudante neutral at left_zoom
        show st_ceo neutral at right_zoom
        with dissolve
        st_estudante "Voltei a confiar no total. Já indiquei o app pra república inteira. Até a menina que jurava pela planilha."
        st_ceo "Um fundo acabou de pedir uma segunda reunião. Por causa da retenção, não dos cadastros! Nunca achei que ia comemorar uma porcentagem assim."
        hide st_estudante
        hide st_ceo
        show st_mentora neutral at center_zoom
        with dissolve
        st_mentora "Sabe o que mais me orgulha, [player_name]? Você ouviu antes de construir. Do primeiro dia até hoje."
        hide st_mentora
    elif st_final_grade() == "bom":
        show st_estudante thinking at left_zoom
        show st_ceo neutral at right_zoom
        with dissolve
        st_estudante "O total está certo, isso eu garanto. Só queria entender melhor quando estou sem internet. Às vezes não sei se já salvou."
        st_ceo "Saí satisfeito! E no próximo ciclo eu quero você nessa conversa do modo offline, [player_name]."
        hide st_estudante
        hide st_ceo
        show st_qualidade thinking at center_zoom
        with dissolve
        st_qualidade "Anotei duas melhorias. Primeiro: um aviso claro de \"salvo no celular, enviando\". Segundo: retenção por curso, para saber quem a gente ainda não ajudou."
        hide st_qualidade
        with dissolve
    else:
        show st_estudante thinking at left_zoom
        show st_ceo thinking at right_zoom
        with dissolve
        st_estudante "Obrigada pelo trabalho, de verdade. Mas, por enquanto, vou continuar conferindo no caderno."
        st_ceo "O pitch foi bom. Mas poucas semanas de retenção subindo ainda não convenceram ninguém na primeira fila."
        hide st_estudante
        hide st_ceo
        show st_mentora neutral at center_zoom
        with dissolve
        st_mentora "Ei. O próximo ciclo começa segunda, e dá para fazer melhor. A gente faz junto."
        hide st_mentora
        with dissolve

    if get_friendship_point("st_mentora") >= 6:
        show st_mentora neutral at left_zoom
        with dissolve
        st_mentora "Lembra do primeiro dia, quando você começou pelas avaliações? Eu soube ali que ia dar certo."
        hide st_mentora
        with dissolve

    if get_friendship_point("st_techlead") >= 6:
        show st_techlead neutral at right_zoom
        with dissolve
        st_techlead "Faz tempo que eu não ensinava alguém que pergunta \"e se o 4G cair?\" antes de mim. Obrigado por isso."
        hide st_techlead
        with dissolve

    if get_friendship_point("st_mobile") >= 6:
        show st_mobile neutral at left_zoom
        with dissolve
        st_mobile "Melhor dupla de pair programming que eu tive. E você riu dos meus trocadilhos. Quase todos."
        hide st_mobile
        with dissolve

    if get_friendship_point("st_qualidade") >= 6:
        show st_qualidade neutral at right_zoom
        with dissolve
        st_qualidade "Você sempre trouxe evidência. Na minha régua, é o maior elogio que eu sei dar."
        hide st_qualidade
        with dissolve

    if st_conq_equipe:
        show st_mentora neutral at left_zoom
        show st_mobile neutral at center_zoom
        show st_techlead neutral at right_zoom
        with dissolve
        st_mentora "A gente conversou e decidiu uma coisa. Nas férias, tem vaga aqui. Se você quiser voltar."
        st_mobile "E a partida de sábado continua de pé, com ou sem férias."
        st_techlead "Só não publique nada na sexta."
        hide st_mentora
        hide st_mobile
        hide st_techlead
        with dissolve

    stop music fadeout 1.0
    play music music_home_reflecting fadein 1.5
    scene bg quarto_noite
    with fade
    $ set_time(22, 0)
    $ set_available("all")

    "{i}Em casa, você abre o app e olha a lista do mês. Cada gasto aparece uma vez.{/i}"
    "{i}Sete semanas atrás, um lanche de R$ 7 apareceu duas vezes num túnel. Hoje, a estudante que mais sofreu com isso subiu num palco para contar que agora confia no total.{/i}"
    "{i}Você pensa no caminho: a queixa virou requisito, o requisito virou teste, o teste virou uma versão nas lojas. Ninguém pulou etapa. Só fez cada uma menor.{/i}"
    "{i}O celular não para de vibrar no grupo da equipe. Talvez valha responder alguém.{/i}"

    call screen contacts_screen

    stop music fadeout 1.5
    scene black
    with fade

    "{i}Fim da Semana 8.{/i}"

    window hide
    pause 1.0

    return
