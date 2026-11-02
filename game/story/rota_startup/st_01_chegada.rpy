label st_01_chegada:
    # Contatos da equipe ainda não existem: ninguém disponível no celular.
    $ set_available()
    $ set_time(9, 0)

    play music music_office_motivated fadein 1.5
    scene bg transito_manha
    with fade

    "{i}Segunda-feira, nove da manhã. O ônibus avança devagar pelas ruas de Botafogo, parando em cada ponto.{/i}"
    "{i}No celular, o e-mail da Trocado: “Segundo andar do casarão amarelo. Pode subir direto, a gente te espera.”{/i}"
    "{i}Você desce perto do metrô e encontra o casarão: fachada antiga, janelas em arco e uma plaquinha de coworking no portão.{/i}"
    play sound "audio/effects/steps.ogg"
    $ advance_minutes(5)

    scene bg startup_coworking_manha
    with fade

    "{i}A escada de madeira range a cada degrau. No segundo andar, pé-direito alto, uma mesa comprida cheia de notebooks e uma parede de vidro coberta de post-its.{/i}"
    "{i}Na porta, uma mulher de cabelo cacheado preso no alto e caderno laranja na mão já sorri antes de você dizer o nome.{/i}"

    show st_mentora neutral at center_zoom
    with dissolve
    st_mentora "Oi! [player_name], né? Eu sou a Tainá, head de produto. Boas-vindas à Trocado!"
    $ add_contact("st_mentora")
    $ add_friendship_point("st_mentora", 1)
    st_mentora "A gente é sete pessoas. Aqui todo mundo faz um pouco de tudo."
    st_mentora "Eu cuido do produto e dos requisitos, mas já respondi suporte, já escrevi texto de botão e já carreguei caixa na mudança."
    st_mentora "Bora conhecer o time? Começando por quem tem menos tempo."
    $ advance_minutes(10)

    # Otávio, entre duas reuniões
    show st_mentora neutral at left_zoom
    show st_techlead neutral at right_zoom
    with dissolve
    "{i}Perto da janela, um homem alto, de cardigã cinza e óculos redondos, segura uma caneca esmaltada.{/i}"
    st_mentora "Esse é o Otávio, nosso CTO e cofundador. Aproveita agora, que daqui a dez minutos ele some em outra reunião."
    st_techlead "Prazer, [player_name]. Cuido da API, da infraestrutura e de tudo que guarda dado de alguém."
    $ add_contact("st_techlead")
    $ add_friendship_point("st_techlead", 1)
    st_techlead "Veja bem: aqui você vai ouvir muita ideia boa. Antes de construir qualquer uma, pergunta que caminho o dado faz. Isso já evita metade dos problemas."
    st_techlead "Agora me dão licença. Investidor não espera, e o café esfria."
    hide st_techlead
    with dissolve

    # Davi e os celulares de teste
    "{i}Na ponta da mesa, três celulares de teste estão em pé num suporte, cada um de um tamanho. Atrás deles, um rapaz de moletom acena com um quarto celular na mão.{/i}"
    show st_mobile neutral at right_zoom
    with dissolve
    st_mentora "O Davi faz o app. Na prática, é com ele que você vai parear mais."
    st_mobile "Fala, [player_name]! Chegou na hora certa, o build acabou de passar."
    $ add_contact("st_mobile")
    $ add_friendship_point("st_mobile", 1)
    st_mobile "Esses três são meus celulares de teste: um top de linha, um médio e um que trava se você olhar torto."
    st_mobile "Se roda no mais barato, roda em qualquer um. É o que a maioria dos estudantes tem no bolso."
    hide st_mobile
    with dissolve

    # Lorena e as avaliações
    "{i}Do outro lado da mesa, uma mulher de óculos verde-água lê alguma coisa no tablet com a testa franzida.{/i}"
    show st_qualidade thinking at right_zoom
    with dissolve
    st_mentora "E a Lorena cuida da qualidade e da pesquisa com usuários. Ela lê todas as avaliações das lojas. Todas mesmo."
    st_qualidade "Oi, [player_name], prazer. Desculpa a cara, tô no meio de uma avaliação de uma estrela."
    $ add_contact("st_qualidade")
    $ add_friendship_point("st_qualidade", 1)
    st_qualidade "Primeiro eu leio, segundo eu agrupo, terceiro eu trago para a equipe. E já aviso: minha pergunta favorita é “cadê a evidência?”."
    hide st_qualidade
    with dissolve
    $ advance_minutes(15)

    # O app no celular
    show st_mobile thinking at right_zoom
    with dissolve
    st_mentora "Davi, mostra o app? Melhor que qualquer apresentação."
    st_mobile "Bora. O Trocado é simples: você lança um gasto, ele entra na lista do mês e o total sobe."

    show expression "images/artifacts/st_app_gastos.png" as st_tela_app at artefato_tela
    with dissolve
    "{i}Na tela da esquerda, a lista de outubro: almoço, bandejão, ônibus, café. Cada item com um ícone de categoria. No topo, o total do mês em destaque.{/i}"
    st_mobile "Toca no mais, digita o valor, escolhe a categoria e salva. Uns cinco segundos."
    st_mobile "A tela da direita é um rascunho da Tainá. Ainda não existe no app. Hoje, se você lança errado, não tem como apagar."
    st_mentora "Ainda. Guarda essa palavra."
    hide st_tela_app
    with dissolve
    $ advance_minutes(20)

    show st_mobile neutral at right_zoom
    show st_qualidade serious at center_zoom
    with dissolve
    st_qualidade "Agora a parte menos bonita. Separei duas avaliações reais do beta, de ontem."
    st_qualidade "Primeira, uma estrela: “Meu total está errado. Não sei mais quanto gastei.”"
    st_qualidade "Segunda, duas estrelas: “Lancei o almoço duas vezes e não consigo apagar.”"
    st_qualidade "Não são casos isolados. Essas duas queixas voltam toda semana, com outras palavras."
    "{i}Você imagina a cena: alguém abre o app no fim do mês, vê um número que não bate e já não sabe se o erro é do app ou da própria conta.{/i}"
    hide st_qualidade
    hide st_mobile
    with dissolve
    $ advance_minutes(15)

    # O painel de métricas
    show st_mentora thinking at left_zoom
    st_mentora "Me conta: você confiaria num app que erra a sua conta? Pois é. Os números dizem a mesma coisa."
    show expression "images/artifacts/st_painel_metricas.png" as st_painel at artefato_tela
    with dissolve
    st_mentora "Hoje são 800 estudantes no beta. A nota nas lojas está em 3,4."
    st_mentora "E esse é o número que me tira o sono: retenção de 30 dias. De cada cem estudantes que começam, quantos ainda lançam gasto um mês depois."
    st_mentora "Era 40%%. Agora está em 22%%."
    "{i}A linha do gráfico desce sem pressa, mês após mês.{/i}"
    st_mentora "Download a gente consegue com anúncio. Gente voltando a usar, só se o app ajudar de verdade."
    hide st_painel
    with dissolve
    $ advance_minutes(25)

    # O desafio das oito semanas
    show st_mentora serious at left_zoom
    st_mentora "Agora o desafio. Daqui a oito semanas começa o semestre. Os calouros chegam, procuram um jeito de controlar a bolsa, e quem estiver nas lojas ganha essa turma."
    st_mentora "A gente precisa publicar a versão 1.0 antes disso. E, na mesma semana, o Vinícius, nosso CEO, apresenta a Trocado no demo day da Aceleradora Maré, para investidores."
    show st_mobile neutral at right_zoom
    with dissolve
    st_mobile "Oito semanas, sete pessoas e um celular que trava. Tranquilo."
    st_mobile "Relaxa, o app chama Trocado, mas o prazo a gente não troca. Desculpa, saiu."
    show st_mentora neutral at left_zoom
    st_mentora "Ignora o Davi. Ou não, às vezes ele acerta."
    $ advance_minutes(20)

    menu (tipo="conversa"):
        st_mentora "E você, [player_name]? O que mais chamou sua atenção até agora?"
        "As avaliações dos estudantes. Quero entender o que está dando errado.":
            $ add_friendship_point("st_mentora", 1)
            st_mentora "Começou pelo lugar certo."
            st_mentora "Cada avaliação daquelas é uma pessoa que tentou fazer alguma coisa e não conseguiu. Nosso trabalho é descobrir o quê."
        "O app em si. Quero ver como ele é construído.":
            $ add_friendship_point("st_mobile", 1)
            show st_mobile thinking at right_zoom
            st_mobile "Pô, falou minha língua!"
            "{i}Davi já puxa o notebook e abre o projeto: pastas de telas, uma de sincronização, outra de testes com bem menos arquivos do que deveria.{/i}"
            st_mobile "Essa pasta de testes aqui tá pedindo ajuda. Depois a gente olha junto."
        "Como vocês aguentam o ritmo com tão pouca gente?":
            $ add_friendship_point("st_techlead", 1)
            show st_techlead neutral at center_zoom
            with dissolve
            "{i}Otávio, que voltava para encher a caneca entre uma reunião e outra, responde antes da Tainá.{/i}"
            st_techlead "Fazendo menos coisas, mas direito."
            st_techlead "Em 2009 eu tentei fazer tudo ao mesmo tempo e derrubei um banco de dados numa sexta. Desde então, escolho."
            hide st_techlead
            with dissolve
    $ advance_minutes(15)

    # Repositório e beta no celular
    show st_mobile neutral at right_zoom
    st_mobile "Já te mandei o convite do repositório. E instala o beta no seu celular. Melhor teste que existe é usar no dia a dia."
    "{i}Você aceita o convite, baixa o beta e lança seu primeiro gasto no Trocado: o café da padaria, R$ 5.{/i}"
    "{i}Aparece na lista. O total marca R$ 5,00. Por enquanto, tudo certo.{/i}"
    st_mentora "Lança tudo que gastar essa semana. E se algo estranho acontecer, anota: hora, lugar e o que você fez. Isso vale ouro."
    st_mentora "Quarta tem reunião com o time inteiro. Até lá, explora o app e lê as avaliações com a Lorena."
    $ advance_minutes(25)

    hide st_mentora
    hide st_mobile
    with dissolve
    "{i}Onze e meia. A mesa comprida volta ao barulho de teclado e conversa baixa. Você ocupa um lugar perto da janela, com o beta aberto no celular e uma lista de perguntas crescendo no caderno.{/i}"

    return
