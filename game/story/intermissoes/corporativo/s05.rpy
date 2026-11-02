# s05.rpy
# Tempo livre da rota Corporativo, semana 5 (sexta, 15h às 18h), chamado no
# fim da co_15. O Jorge já anunciou a aposentadoria (co_14); a RFC está
# pronta e houve o ensaio de quarta (2,7 por cento de acentos quebrados).
# Roteiro: docs/design/intermissoes-corporativo.md, seção 2.6.
# O motor (logic/intermissao.rpy) põe o fundo, cobra tempo e energia e dá a
# recompensa (inclusive a pista co_p_botao do "ajudar") depois do label.
# Não se sabe aqui quem ficou no ensaio de quarta: as falas não supõem.
# Descansar tem label por semana (im_corporativo_s5_descansar_*).

label im_corporativo_abertura_5:
    $ im_mostrar_local({"poi": im_local})
    with dissolve
    "{i}Sexta, três da tarde. A RFC voltou da [NOME_CO_QUALIDADE] com dois comentários pequenos, e a baia inteira respira.{/i}"
    "{i}Tem novidade no mapa: a sala do CAB, no 15º andar. A [NOME_CO_QUALIDADE] passa a tarde lá.{/i}"
    if energia_exaustao():
        show co_mentora serious at center_zoom
        with dissolve
        co_mentora "Vamos por partes, e a primeira parte é sentar. Hoje dá para pouca coisa, e tudo bem."
        hide co_mentora
        with dissolve
    elif energia_cansaco():
        show co_mentora neutral at center_zoom
        with dissolve
        co_mentora "Você está com cara de semana longa. Hoje o tempo livre é mais curto. Se eu fosse você, começava pelo café do térreo."
        hide co_mentora
        with dissolve
    return

# ---------------- Baia do Farol ----------------

label im_corporativo_s5_conversar_co_dev:
    "{i}Na baia, [NOME_CO_DEV] está com o script da carga aberto em uma tela e o relatório do ensaio na outra.{/i}"
    show co_dev thinking at center_zoom
    with dissolve
    if energia_cansaco():
        co_dev "Opa. Cara de quem dormiu pouco. Pega meu café, eu já tomei três."
    co_dev "Dois vírgula sete. Não sai da minha cabeça."
    co_dev "Quarta, quando a validação acusou os acentos quebrados, eu jurei que o erro era meu. Passei uma hora caçando."
    co_dev "Achei que era bug meu. Era bug de 2014. Mesmo assim, o script é meu."
    "{i}Você pergunta o que ele mudou depois do ensaio.{/i}"
    show co_dev neutral at center_zoom
    co_dev "Agora ele confere cada descrição antes de gravar. Se achar um caractere estranho, separa e avisa. Não engole calado."
    co_dev "Lembra da minha primeira RFC, que voltou três vezes? Na primeira, faltava o impacto. Na segunda, o responsável. Na terceira, o plano de volta."
    co_dev "Desta vez a [NOME_CO_QUALIDADE] devolveu com dois comentários pequenos. Para mim, isso é medalha."
    hide co_dev
    with dissolve
    return


# ---------------- Central de atendimento ----------------

label im_corporativo_s5_conversar_co_supervisora:
    "{i}Numa baia vazia da central, [NOME_CO_SUPERVISORA] e a Neusa espalharam folhas impressas. Cada uma tem um título: Senha, VPN, Notebook.{/i}"
    show co_supervisora neutral at center_zoom
    with dissolve
    co_supervisora "Os modelos de descrição. Pedi na entrevista e resolvi escrever eu mesma. Quem atende sabe o que cabe."
    co_supervisora "Faz um favor. Lê esse aqui em voz alta, como se fosse um atendente com cliente na linha."
    "{i}Ela aperta o cronômetro do relógio dourado. Você lê o modelo de VPN: o que foi feito, o que o técnico precisa fazer, quando ligar de novo.{/i}"
    show co_supervisora thinking at center_zoom
    co_supervisora "Vinte e oito segundos. Passou de vinte, tem que reescrever."
    co_supervisora "Neusa, corta o \"prezado colaborador\". Ninguém fala assim com a fila cheia."
    "{i}A Neusa risca a linha. Você lê de novo. Dezenove segundos.{/i}"
    show co_supervisora neutral at center_zoom
    co_supervisora "Agora sim. Modelo bom cabe numa respiração. O resto é romance."
    hide co_supervisora
    with dissolve
    return

label im_corporativo_s5_conversar_co_solicitante:
    "{i}Encostado numa pilastra da central, [NOME_CO_SOLICITANTE] mostra alguma coisa no celular para quem passa. O colete refletivo está dobrado no braço.{/i}"
    show co_solicitante neutral at center_zoom
    with dissolve
    co_solicitante "Fala! Olha aqui. O Wellington pegou aquele print do Farol e mostrou para dois colegas na base."
    co_solicitante "Um perguntou se dava para ver quem atendeu. Dava. O outro perguntou se dava para reclamar. Aí eu disse que era para isso o Reabrir."
    show co_solicitante thinking at center_zoom
    if co_negociacao_opcao == "investigar_agora":
        co_solicitante "E o WhatsApp? O [NOME_CO_DEV] me disse que o jurídico pediu vinte dias."
        "{i}Você explica: o piloto da equipe dele entra na janela da semana 8; a liberação para todos fica para a janela seguinte.{/i}"
        co_solicitante "Piloto já é muito. Meu pessoal vai ser o primeiro a apanhar do sistema novo. Melhor nós do que a central inteira."
    else:
        co_solicitante "E o WhatsApp? Sei que ficou para depois, mas o meu pessoal pergunta toda segunda."
        "{i}Você explica: primeiro a consulta e o bloqueio para todos. O WhatsApp vai ser investigado na próxima rodada, antes de alguém prometer data.{/i}"
        co_solicitante "Tá certo. Sem data inventada. Eu prefiro esperar a ouvir mentira bonita."
    show co_solicitante neutral at center_zoom
    co_solicitante "Se não der agora, me explica o porquê. Eu explico para o meu pessoal."
    hide co_solicitante
    with dissolve
    return

label im_corporativo_s5_observar_central:
    "{i}Meio da tarde. A fila está média, nem pico nem calmaria.{/i}"
    "{i}[NOME_CO_SUPERVISORA] coloca uma cadeira atrás da Neusa e outra para você. Na mesa, ao lado do teclado, a folha do modelo de senha.{/i}"
    show co_supervisora thinking at right_zoom
    with dissolve
    co_supervisora "Hoje é teste de verdade. Fila real, modelo em papel. Eu marco o tempo, ela atende."
    "{i}Toca a primeira ligação. Senha bloqueada. A Neusa resolve o problema rápido, mas trava na hora de escrever. Olha o papel, digita, apaga, olha de novo.{/i}"
    co_supervisora "Quarenta e um segundos só na descrição. Tudo bem. Primeira vez."
    "{i}Segunda ligação, outra senha. A Neusa já não lê o papel inteiro: copia só a primeira linha e troca o nome do sistema.{/i}"
    co_supervisora "Trinta e dois."
    "{i}Entre uma ligação e outra, a Neusa vira a folha para você e aponta com a caneta.{/i}"
    "{i}Ela riscou \"conforme solicitado\" e escreveu por cima, à mão: \"Senha nova enviada por SMS. Trocar no primeiro acesso.\"{/i}"
    "{i}Terceira ligação. Desta vez ela nem olha o papel.{/i}"
    show co_supervisora neutral at right_zoom
    co_supervisora "Vinte e três segundos. Cabe no meu TMA."
    co_supervisora "Viu o que aconteceu? O modelo não ficou bom na minha mesa. Ficou bom na terceira ligação, na mão dela."
    "{i}Você anota no caderno: o primeiro rascunho veio de quem decide; a versão que funciona veio de quem usa, com a fila tocando.{/i}"
    co_supervisora "Segunda eu passo a versão da Neusa para o [NOME_CO_DEV]. A dela, não a minha."
    hide co_supervisora
    with dissolve
    return


# ---------------- Café do térreo ----------------

label im_corporativo_s5_conversar_co_mentora:
    "{i}No café do térreo, [NOME_CO_MENTORA] segura a caneca com as duas mãos e olha a porta giratória girar.{/i}"
    show co_mentora neutral at center_zoom
    with dissolve
    co_mentora "Semana cheia. Calendário, capacidade, RFC, ensaio. Como você está?"
    "{i}Você conta o que ficou na cabeça: a lista de quatro itens que virou dois.{/i}"
    if co_plano_cobertura == 2:
        co_mentora "Você cortou o tema de cores sem dó. Eu vi."
        co_mentora "Muita gente guarda o item bonito porque dá pena. Você olhou para o problema do [NOME_CO_SOLICITANTE] e decidiu por ele."
    else:
        show co_mentora thinking at center_zoom
        co_mentora "O plano de segunda não fechou de primeira, e tudo bem. Me conta: o que você olhou primeiro, os itens ou o problema?"
        "{i}Você admite que olhou os itens.{/i}"
        co_mentora "Vamos por partes, então. Primeiro o problema que a entrevista trouxe. Depois o item que resolve. Nessa ordem, a escolha fica mais fácil."
    show co_mentora neutral at center_zoom
    co_mentora "Sempre sobra pedido e falta gente. O plano é o jeito de dizer isso em voz alta."
    co_mentora "Semana que vem você mexe no fechamento. Pergunta muito ao [NOME_CO_LEGADO]. Ele gosta mais de pergunta do que diz."
    hide co_mentora
    with dissolve
    return


# ---------------- Sala do arquivo ----------------

label im_corporativo_s5_conversar_co_legado:
    "{i}Na sala do arquivo, [NOME_CO_LEGADO] tira caixas da estante e lê as etiquetas uma por uma, sem pressa.{/i}"
    show co_legado neutral at center_zoom
    with dissolve
    co_legado "Março chega rápido. Mais rápido que RFC no CAB, pelo menos."
    if co_homenagem_jorge == "wiki" and co_conq_memoria:
        co_legado "Quarta eu gravei o primeiro causo. A Tia Neide, claro. A [NOME_CO_QUALIDADE] levou o gravador e criou a página no wiki."
        show co_legado thinking at center_zoom
        co_legado "Ouvi de novo ontem. Ficou divertido. E meio inútil: quem ouvir não sabe o que fazer com aquilo."
        co_legado "Tem que ter um jeito melhor de contar. Ainda não sei qual."
    else:
        show co_legado thinking at center_zoom
        co_legado "Desde a festa eu penso em como guardar o que sei. Está tudo aqui, ó. Na cabeça e nessas caixas."
        co_legado "Escrever um documento gigante? Ninguém lê. Gravar vídeo? Ninguém acha depois."
        co_legado "Ainda não sei o jeito certo. Mas sei que não dá para deixar para fevereiro."
    "{i}Ele levanta uma caixa com a etiqueta \"SGC 2010\" e sopra a poeira da tampa.{/i}"
    show co_legado neutral at center_zoom
    co_legado "Isso aí tem história. Tudo aqui tem. O problema é saber qual vale a pena contar primeiro."
    hide co_legado
    with dissolve
    return

label im_corporativo_s5_estudar_arquivo:
    "{i}Numa pasta com a etiqueta \"Mudanças 2019\", você encontra o pedido daquela sexta-feira. O do fechamento que zerou o relatório da diretoria.{/i}"
    "{i}Não chega a ser uma RFC: é um e-mail impresso, de meia página. O que muda: \"ajuste no fechamento\". Motivo: \"melhoria\". Quando: \"sexta, 17h\".{/i}"
    "{i}Ao lado, você abre no celular o modelo atual da [NOME_CO_QUALIDADE] e vai marcando com um lápis o que faltava na velha.{/i}"
    "{i}Impacto: nenhuma linha. Ninguém escreveu que o relatório mensal lia aquela mesma tabela.{/i}"
    "{i}Testes: nenhum. Plano de volta: nenhum. Responsável: um nome, sem plantão.{/i}"
    "{i}Tipo da mudança: nem existia o campo. E não passou pelo CAB.{/i}"
    "{i}Você entende a fama da [NOME_CO_QUALIDADE]. Cada campo do modelo novo é uma pergunta que alguém deixou de fazer em 2019.{/i}"
    "{i}No caderno, você resume numa linha: o CAB não aprova intenção, aprova evidência.{/i}"
    return


# ---------------- Sala do CAB ----------------

label im_corporativo_s5_conversar_co_qualidade:
    "{i}A sala do CAB fica no 15º andar, com persianas pela metade e um calendário enorme na parede. [NOME_CO_QUALIDADE] monta a pauta da próxima reunião.{/i}"
    show co_qualidade neutral at center_zoom
    with dissolve
    co_qualidade "Boas-vindas ao templo. Brincadeira. É só uma sala com mesa comprida e café ruim."
    co_qualidade "A RFC do Farol entra na quinta da semana 7. Hoje eu monto a pauta das outras."
    "{i}Você pergunta como o comitê separa uma mudança da outra.{/i}"
    show co_qualidade thinking at center_zoom
    co_qualidade "Três tipos. Padrão: trocar a senha de um usuário de integração. Risco baixo, passo a passo aprovado uma vez, vale para as próximas."
    co_qualidade "Normal: o Farol. Passa por aqui, com evidência, e espera a janela."
    co_qualidade "Emergencial: o SGC caiu às dez da manhã e a correção precisa subir hoje para a central voltar a atender. Aí não dá para esperar quinta."
    show co_qualidade serious at center_zoom
    co_qualidade "Emergencial é para restaurar serviço. Pressa não é emergência."
    co_qualidade "Toda semana alguém tenta. Toda semana eu devolvo. Registrado como tentativa, prioridade baixa."
    hide co_qualidade
    with dissolve
    return

label im_corporativo_s5_ajudar_co_qualidade:
    "{i}[NOME_CO_QUALIDADE] gira o tablet para você. A seção da RFC chamada Perfis e acessos está em branco.{/i}"
    show co_qualidade thinking at center_zoom
    with dissolve
    co_qualidade "Antes de escrever como o Farol controla acesso, eu quero ver como o SGC faz hoje. De verdade, não pelo manual."
    co_qualidade "Tem um usuário de teste na homologação, perfil atendente. Entra com ele e me mostra o que um atendente vê."
    "{i}Você entra. A tela cinza do SGC, as abas em degradê. A lista mostra chamados de vários setores.{/i}"
    "{i}Você abre um chamado da própria central. Lá embaixo, o botão Reabrir.{/i}"
    co_qualidade "Agora um chamado de outro setor. Manutenção de campo, por exemplo."
    "{i}Você abre um chamado da equipe do [NOME_CO_SOLICITANTE]. O botão Reabrir não aparece.{/i}"
    co_qualidade "Hum. Volta no da central."
    "{i}Ela passa o mouse sobre o botão Reabrir, copia o endereço da ação e cola num bloco de notas.{/i}"
    "{i}Depois troca só o número do chamado pelo da equipe de campo, cola na barra do navegador e aperta Enter.{/i}"
    "{i}A tela pisca. O chamado da manutenção de campo aparece como Reaberto.{/i}"
    show co_qualidade serious at center_zoom
    co_qualidade "Interessante."
    "{i}Ela não diz mais nada por alguns segundos. Depois devolve o chamado ao estado de antes e anota a hora no tablet.{/i}"
    "{i}Você começa a falar o que acha que aconteceu. Ela levanta a mão, sem pressa.{/i}"
    show co_qualidade neutral at center_zoom
    co_qualidade "Calma. Escreve primeiro o que você viu. Perfil, chamado, botão, endereço, resultado. Nessa ordem."
    co_qualidade "Anota o que você viu, não o que você acha. O que achar fica para a semana de testes."
    "{i}Você escreve. Cinco linhas, sem adjetivo. Ela lê, corrige o horário e copia para a pasta da RFC.{/i}"
    if energia_cansaco():
        co_qualidade "E agora para. Você está piscando devagar demais. Tem coisa que eu só aceito de quem dormiu."
    else:
        co_qualidade "Boa. Vou terminar a seção de perfis com isso aberto do lado."
    co_qualidade "Obrigada pela tarde. Se não está registrado, não aconteceu. E agora está."
    hide co_qualidade
    with dissolve
    return


# ---------------- Descansar ----------------

label im_corporativo_s5_descansar_cafe:
    "{i}No café do térreo, o atendente já sabe o seu pedido. Coado, sem açúcar, xícara grande.{/i}"
    "{i}Você senta perto da porta giratória. Cada volta da porta traz um pouco do barulho do Centro e leva de novo.{/i}"
    if energia_cansaco():
        "{i}A semana pesa nos ombros. Você fecha os olhos com a xícara entre as mãos, e o atendente baixa o volume do rádio.{/i}"
    else:
        "{i}Por meia hora, RFC é só uma sigla. Você termina o café devagar, sem olhar o celular.{/i}"
    return

label im_corporativo_s5_descansar_refeitorio:
    "{i}O refeitório está vazio a esta hora. Só a máquina de chá faz barulho.{/i}"
    "{i}Você senta de frente para a janela. A baía está parada, cor de cobre.{/i}"
    if energia_cansaco():
        "{i}Você deita a cabeça nos braços por dez minutos. Ninguém repara, e você acorda com a marca da manga no rosto.{/i}"
    else:
        "{i}Você não abre o notebook. Fica olhando uma barca atravessar até sumir atrás do morro.{/i}"
    return

label im_corporativo_s5_descansar_aterro:
    "{i}Quinze minutos a pé até o Aterro. O fim da tarde de sexta tem cheiro de grama cortada e de mar.{/i}"
    if energia_cansaco():
        "{i}Você deita num banco à sombra e olha as folhas mexendo. Quando percebe, passou meia hora.{/i}"
    else:
        "{i}Você anda até a mureta da baía. Um grupo joga altinha na areia, e a bola não cai nunca.{/i}"
    return
