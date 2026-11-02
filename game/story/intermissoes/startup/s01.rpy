# s01.rpy
# Tempo livre da rota Startup: semana 1 (sexta, 15h-17h, tutorial) e os três
# "descansar", que valem para todas as semanas.
# Fonte: docs/design/intermissoes-startup.md (seção 3). O motor
# (scripts/mechanics/intermissao_fluxo.rpy) mostra o fundo do local, chama
# estes labels pelo nome e aplica a recompensa depois do return.

# A abertura roda antes do mapa, sem fundo de local: mostra a mesa da equipe,
# que é o ponto de partida.
label im_startup_abertura_1:
    scene bg startup_coworking_tarde
    with dissolve
    show st_mentora neutral at center_zoom
    with dissolve
    st_mentora "Sexta, três da tarde, e a semana já rendeu. Aqui a tarde de sexta é livre: cada um escolhe onde pôr o tempo."
    show st_mentora thinking at center_zoom
    st_mentora "Esse é o mapa. Cada lugar mostra quem está lá e o que dá para fazer. Toda ação custa minutos, e o relógio não volta."
    st_mentora "Ajudar alguém e observar gente usando o app cansam mais. Sua energia fica embaixo do relógio. Descansar também é escolha, viu?"
    st_mentora "Às vezes você vai ver alguma coisa que vira pista. Ela pode ajudar numa conversa mais para frente."
    show st_mentora neutral at center_zoom
    st_mentora "E o mais importante: nada aqui é obrigatório para aprender. O que precisa, a gente faz junto durante a semana. Isso aqui é o seu tempo."
    st_mentora "Hoje são duas horas. Não dá para fazer tudo. Escolher já é metade do trabalho."
    hide st_mentora
    with dissolve
    return


# -------------------------------
# Descansar (todas as semanas)
# -------------------------------
# energia_cansaco() é lido antes do +2 do descanso, que o motor soma depois.

label im_startup_descansar_cafe:
    play sound "audio/effects/xicara_cafe.ogg"
    "{i}Na esquina, a fornada de pão de queijo acabou de sair. A máquina de espresso chia atrás do balcão.{/i}"
    if energia_cansaco():
        "{i}Você senta perto da janela e fica um tempo olhando para a xícara, sem beber.{/i}"
        "{i}A atendente passa, olha duas vezes e deixa um segundo café na mesa.{/i}"
        "Atendente" "Esse é por conta da casa. Tá com cara de quem precisa."
        "{i}Você aceita. A cabeça desacelera aos poucos, um gole de cada vez.{/i}"
    else:
        "{i}Você pega uma mesinha na calçada e olha a rua: bicicleta de entrega, gente voltando da praia, um cachorro dormindo na sombra da amendoeira.{/i}"
        "{i}No caderno, uma linha só: uma coisa boa da semana. Você pensa um pouco e escreve.{/i}"
        "{i}Quando o café acaba, a cabeça está mais leve que a xícara.{/i}"
    return

label im_startup_descansar_terraco:
    "{i}A escada estreita termina no deck de madeira do terraço. Entre dois prédios, aparece um pedaço do Pão de Açúcar.{/i}"
    if im_semana_atual == 6:
        if game_hour < 19:
            "{i}Às sete em ponto, o varal de lâmpadas acende sozinho, uma de cada vez, como se alguém tivesse lembrado de você.{/i}"
        else:
            "{i}O varal de lâmpadas já está aceso. Lá embaixo, Botafogo troca o barulho de trabalho pelo barulho de bar.{/i}"
    if energia_cansaco():
        "{i}Tem um puff no canto. Você deita só para descansar os olhos.{/i}"
        "{i}Dez minutos depois, acorda com um bem-te-vi gritando na grade. Ninguém viu. O corpo agradece.{/i}"
    else:
        "{i}Os vasos de manjericão do [NOME_ST_TECHLEAD] estão com a terra seca. Num deles, um cartãozinho: \"Não arrancar. Assinado: O.\"{/i}"
        "{i}Você rega um por um, sem arrancar nada. O cheiro sobe com o vento da baía.{/i}"
        "{i}Por alguns minutos, ninguém precisa de nada de você.{/i}"
    return

label im_startup_descansar_ponto:
    "{i}Você desce até o calçadão de ondas pretas e brancas e caminha até o ponto, sem fone. Só o barulho do mar e dos ônibus.{/i}"
    if energia_cansaco():
        "{i}No ponto, você senta no banco e não levanta mais.{/i}"
        "{i}Passa um ônibus. Passa outro. Passa o terceiro. Nenhum era o seu, e tudo bem.{/i}"
        "{i}Na volta, as pernas estão pesadas, mas a cabeça parou de girar.{/i}"
    elif im_semana_atual == 1:
        "{i}Do banco do ponto dá para ver a boca do túnel no morro. Um ônibus entra nele e some no escuro.{/i}"
        "{i}Por curiosidade, você caminha até perto da entrada. O sinal do celular cai de quatro barrinhas para uma.{/i}"
        "{i}Você guarda o celular no bolso e volta pela orla, sem pressa.{/i}"
    else:
        "{i}Um vendedor de mate passa com os dois galões nas costas: \"Olha o mate, olha o limão!\" Você compra um copo.{/i}"
        "{i}Na mureta da praia, gente de todo tipo olhando o mar. Você fica ali até o copo esvaziar.{/i}"
        "{i}A volta é mais leve que a ida.{/i}"
    return


# -------------------------------
# Semana 1
# -------------------------------

label im_startup_s1_conversar_st_mobile:
    show st_mobile neutral at left_zoom
    with dissolve
    "{i}[NOME_ST_MOBILE] olha a barra de progresso do build no celular menor do suporte. Ela não anda.{/i}"
    st_mobile "Pô, chegou na hora certa. Deixa eu te apresentar a equipe de verdade."
    st_mobile "Esse grandão é o Foguete. Abre tudo em meio segundo. O do meio é o Tartaruga. Chega lá, mas sem pressa."
    show st_mobile thinking at left_zoom
    st_mobile "E esse aqui é o Tijolo. Pesado, lento, pouca memória. É o modelo que mais aparece nas avaliações do beta."
    st_mobile "Quem conferiu foi a [NOME_ST_QUALIDADE]. Ela leu as avaliações uma por uma e anotou o aparelho de cada pessoa."
    show st_mobile neutral at left_zoom
    st_mobile "Então, mano: o Tijolo é meu chefe. Se ele aprova, ninguém reclama."
    "{i}O build termina. O app abre no Tijolo depois de uma pausa longa o bastante para você contar até cinco.{/i}"
    st_mobile "Viu? Cinco segundos. No Foguete, eu nem teria percebido."
    st_mobile "E antes que você pergunte: não, eles não descansam no fim de semana."
    st_mobile "Celular de teste não tira férias. No máximo, tira print."
    "{i}Ele ri da própria piada. Você ri também, mais da risada dele do que da piada.{/i}"
    hide st_mobile
    with dissolve
    return

label im_startup_s1_ajudar_st_mobile:
    show st_mobile neutral at left_zoom
    with dissolve
    st_mobile "Quer ajudar de verdade? Fechou. Primeiro passo: rodar o projeto no seu notebook. Todo mundo sofre nessa parte."
    play sound "audio/effects/teclado.ogg"
    "{i}Você baixa o código, instala as dependências e espera. Uma barra, outra barra, um aviso amarelo que [NOME_ST_MOBILE] manda ignorar.{/i}"
    "{i}Depois, o cabo no Tijolo. O build leva seis minutos inteiros. [NOME_ST_MOBILE] aproveita para buscar água.{/i}"
    show st_mobile thinking at left_zoom
    st_mobile "Rodou? Agora o passeio. Lança um gasto de teste e toca em Salvar. A gente segue o caminho dele."
    st_mobile "Você toca em Salvar, o app grava no celular, manda para a nuvem, a lista lê de novo e o total soma tudo."
    st_mobile "Cinco paradas. Todo gasto passa por todas. Quando o total erra, alguma delas falhou."
    "{i}Você pergunta onde ficam os testes. Ele abre uma pasta. Dentro, três arquivos.{/i}"
    st_mobile "Pois é. Três. Um testa se o app abre. Outro, se o login aparece."
    st_mobile "O terceiro eu nem lembro. Tá na lista de coisas que dão vergonha."
    show st_mobile neutral at left_zoom
    st_mobile "Bora para o seu primeiro commit? Achei uma coisa do seu tamanho."
    "{i}Na tela de lançamento, o botão diz \"Salva\". [NOME_ST_MOBILE] aponta e espera.{/i}"
    "{i}Você troca para \"Salvar\", escreve a mensagem do commit e envia. Uma letra.{/i}"
    st_mobile "Pronto, você já está no histórico do Trocado. Agora roda de novo para conferir."
    "{i}Mais seis minutos. O botão aparece certo no Tijolo, e vocês comemoram como se fosse gol.{/i}"
    show st_mobile thinking at left_zoom
    st_mobile "Repara no que aconteceu: seis minutos para ver uma letra mudar."
    st_mobile "Agora imagina isso a cada ajuste. Seis minutos pra ver uma vírgula mudar."
    st_mobile "Por isso a gente testa antes, e não no olho. Teste roda em segundos. O olho cansa."
    show st_mobile neutral at left_zoom
    st_mobile "Valeu pela tarde. Quando aquela pasta tiver mais de três arquivos, o primeiro brinde é seu."
    hide st_mobile
    with dissolve
    return

label im_startup_s1_conversar_st_techlead:
    show st_techlead neutral at right_zoom
    with dissolve
    "{i}[NOME_ST_TECHLEAD] revisa um PR com a caneca esmaltada na mão. O esmalte está lascado na borda.{/i}"
    "{i}Você pergunta da caneca. Ele olha para ela como quem olha um cachorro velho.{/i}"
    show st_techlead thinking at right_zoom
    st_techlead "Presente da minha primeira equipe, em 1998. Sistema de folha de pagamento, servidor numa sala sem janela."
    st_techlead "É a única coisa daquela época que nunca deu bug."
    show st_techlead neutral at right_zoom
    st_techlead "E você? Já entendeu como o Trocado funciona por dentro? Me explica."
    "{i}Você tenta. Fala de tela, de banco, de nuvem, de sincronizar. A explicação dá voltas.{/i}"
    "{i}Ele puxa um guardanapo do pote e desenha três caixas: celular, nuvem, banco. Duas setas entre elas.{/i}"
    st_techlead "O gasto nasce aqui, no celular. Vai para a nuvem quando tem sinal. Mora no banco."
    st_techlead "Quando alguma coisa dá errado, a pergunta é sempre a mesma: em qual seta ele se perdeu?"
    st_techlead "Veja bem: se não cabe num guardanapo, você ainda não entendeu o sistema."
    "{i}Ele empurra o guardanapo para o seu lado. Você guarda no caderno.{/i}"
    hide st_techlead
    with dissolve
    return

label im_startup_s1_conversar_st_mentora:
    show st_mentora neutral at left_zoom
    with dissolve
    "{i}Na sala de vidro, [NOME_ST_MENTORA] reorganiza a coluna de descoberta, com o caderno laranja aberto em cima da mesa.{/i}"
    st_mentora "Senta aí. Quer ver meu sistema? É bem sofisticado, viu?"
    "{i}Ela mostra três blocos de post-it, um de cada cor.{/i}"
    show st_mentora thinking at left_zoom
    st_mentora "Coral é dúvida de usuário. Amarelo é dúvida técnica. Verde é \"já sei\". Quanto mais verde na parede, melhor a semana."
    menu (tipo="conversa"):
        st_mentora "Me conta: qual foi a sua dúvida da semana? Aquela que ficou martelando."
        "Por que tanta gente desinstala o app.":
            st_mentora "Essa é das boas. Ninguém aqui sabe responder ainda, só tem palpite."
        "Se o total errado acontece sempre ou só às vezes.":
            st_mentora "Ótima. A gente só tem as reclamações. Ninguém viu acontecer ainda."
        "Como saber o que o estudante precisa, e não o que a gente acha.":
            st_mentora "Essa é a pergunta do meu trabalho inteiro. Bom começo."
    show st_mentora neutral at left_zoom
    "{i}Ela escreve a sua dúvida num post-it coral, do jeito que você falou, e cola no seu caderno.{/i}"
    st_mentora "Segunda tem entrevista com uma estudante do beta. Leva esse post-it."
    st_mentora "Dúvida anotada vira pergunta de entrevista. Dúvida só lembrada some na sexta."
    hide st_mentora
    with dissolve
    return

label im_startup_s1_estudar_sala_vidro:
    "{i}Na parede da sala de vidro, o quadro da equipe: descoberta, pronto para desenvolver, fazendo, revisão, pronto.{/i}"
    "{i}Você conta os cartões em \"Fazendo\": seis. Em \"Revisão\", quatro, dois deles com a data de segunda.{/i}"
    "{i}No notebook, você abre um texto sobre limite de trabalho em andamento. A ideia é simples: um teto de cartões na coluna, e ninguém puxa um novo enquanto ela estiver cheia.{/i}"
    show st_mentora neutral at left_zoom
    with dissolve
    st_mentora "Estudando o quadro? Só uma dica, sem dar a resposta."
    st_mentora "Repara quantos cartões estão parados esperando alguém."
    hide st_mentora
    with dissolve
    "{i}Você volta à parede. Dos seis em \"Fazendo\", três esperam uma resposta. Ninguém está trabalhando neles agora.{/i}"
    "{i}Cartão parado não aparece como problema. Aparece como demora.{/i}"
    return

label im_startup_s1_conversar_st_qualidade:
    show st_qualidade neutral at right_zoom
    with dissolve
    "{i}[NOME_ST_QUALIDADE] lê avaliações no celular, com um café pela metade e um caderninho de capa azul aberto ao lado.{/i}"
    st_qualidade "Senta, senta. Olha essa: \"o app me julgou pelo café\". Cinco palavras, e eu dei risada sozinha aqui na mesa."
    st_qualidade "Eu guardo as mais estranhas nesse caderninho. Já são vinte e três."
    show st_qualidade thinking at right_zoom
    st_qualidade "Mas não é só coleção, viu? Tem um jogo. Toda queixa esconde um verbo: uma coisa que a pessoa queria fazer e não conseguiu."
    st_qualidade "Primeiro, ache o verbo. \"Meu total está errado\" esconde \"conferir\". Ela queria conferir o mês e não conseguiu."
    st_qualidade "Segundo, pergunte quando foi. Queixa sem dia é nuvem. Queixa com dia vira caso."
    "{i}Ela passa o celular para você. A próxima avaliação: \"lancei e sumiu, app inútil\".{/i}"
    "{i}Você pensa um pouco e arrisca: o verbo escondido é \"guardar\".{/i}"
    show st_qualidade neutral at right_zoom
    st_qualidade "Oxe, rápido. E o \"quando\"? Não diz. Então essa vai para a pilha das que a gente precisa perguntar."
    st_qualidade "Agora me diz: qual é o verbo de \"o app me julgou pelo café\"?"
    "{i}Você não faz ideia. Ela também não. As duas risadas saem juntas.{/i}"
    hide st_qualidade
    with dissolve
    return

label im_startup_s1_conversar_st_ceo:
    show st_ceo neutral at center_zoom
    with dissolve
    "{i}No terraço, [NOME_ST_CEO] fala para os vasos de manjericão, com o celular na mão marcando o tempo.{/i}"
    st_ceo "...e por isso o Trocado vai ser o app de dinheiro de um milhão de estudantes! Obrigado!"
    st_ceo "Ah! [player_name]! Plateia de verdade, finalmente. Os vasos não reagem muito."
    menu (tipo="conversa"):
        st_ceo "Três minutos de pitch. Diz com sinceridade: o que ficou na cabeça?"
        "\"Um milhão de estudantes.\"":
            st_ceo "Ótimo! Número redondo gruda. Era essa a ideia!"
            "{i}Ele anota alguma coisa no celular. Depois apaga.{/i}"
        "\"Que é um app de dinheiro. Não sei bem para quê.\"":
            show st_ceo thinking at center_zoom
            st_ceo "Ai. Justo. Muito justo. Eu falo de mercado antes de falar de quem usa."
        "\"A parte em que você contava moeda no fim do mês.\"":
            st_ceo "Sério? Essa parte dura quinze segundos! Talvez devesse durar mais."
    show st_ceo thinking at center_zoom
    st_ceo "Sabe meu primeiro investidor? Disse não em quatro minutos. Cronometrados."
    st_ceo "Ele fez uma pergunta só: quem voltava a usar o app. Eu fiquei olhando para ele, sorrindo, sem número nenhum."
    show st_ceo neutral at center_zoom
    st_ceo "Ele perguntou quem voltava a usar. Eu não sabia. Nunca mais vou não saber!"
    "{i}Ele volta para os vasos e recomeça do início. Desta vez, a parte da moeda dura um pouco mais.{/i}"
    hide st_ceo
    with dissolve
    return
