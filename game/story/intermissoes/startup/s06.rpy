# s06.rpy
# Rota Startup, tempo livre da semana 6: terça, 18h às 21h, dentro da st_16
# (depois dos testes da Lorena). Design: docs/design/intermissoes-startup.md,
# semana 6. O motor aplica tempo, energia, amizade, pistas e registro extra
# depois de cada label; aqui só as falas.

label im_startup_abertura_6:
    "{i}Terça, seis da tarde. Os dois PRs passaram no celular da Lorena. O coworking esvazia, mas quase ninguém foi para casa.{/i}"
    "{i}No mapa, um lugar novo: a Aceleradora Maré, no Centro, onde o Vinícius ensaia o pitch hoje.{/i}"
    if energia_cansaco():
        "{i}Você boceja olhando a tela escura da janela. O dia foi longo, e a noite livre vai ser mais curta.{/i}"
    return


# -------------------------------
# Mesa da equipe (noite)
# -------------------------------
label im_startup_s6_ajudar_st_mobile:
    show st_mobile neutral at left_zoom
    with dissolve
    st_mobile "Bora montar o pacote das lojas? Prints, descrição, lista de envio. A parte chata do lançamento."
    st_mobile "Regra número um: nada de gasto de verdade nos prints. Nada da Bia, nada de ninguém."
    "{i}Vocês criam uma conta de teste e lançam gastos inventados: bandejão R$ 4,50, xerox R$ 2,40, passagem R$ 4,70. Um estudante que não existe, com um mês bem comportado.{/i}"
    "{i}Você tira os prints no Tijolo e no Foguete. Davi confere um por um, procurando qualquer nome real escondido.{/i}"
    show st_mobile thinking at left_zoom
    st_mobile "Agora a lista de envio. Abre o histórico das versões do beta, que eu quero ver quanto tempo a loja levou."
    "{i}O histórico é uma tabela comprida. Você procura a última versão enviada para o Google.{/i}"
    "{i}Enviada numa quarta. Liberada na sexta. Dois dias inteiros parada em revisão.{/i}"
    "{i}Duas linhas acima, uma versão anterior tem uma marca vermelha: rejeitada. O motivo, em inglês curto: faltava o link da política de privacidade.{/i}"
    show st_mobile serious at left_zoom
    st_mobile "Ah, essa. Lembro. Perdi três dias por causa de um link. Um link!"
    st_mobile "Dois dias de fila e uma rejeição por causa de um link. Loja não tem pressa nenhuma."
    "{i}Você anota as duas datas e o motivo da rejeição no caderno, ao lado da lista de envio.{/i}"
    show st_mobile neutral at left_zoom
    st_mobile "Política de privacidade com link: confere. Prints sem dado real: confere. Pô, a gente tá ficando profissional."
    st_mobile "Trocadilho do dia: loja boa é loja que revisa. Loja rápida é lenda."
    hide st_mobile
    with dissolve
    return


label im_startup_s6_conversar_st_mobile:
    show st_mobile neutral at left_zoom
    with dissolve
    "{i}Davi come uma fatia de pizza fria que sobrou do almoço, direto da caixa, com o celular de teste apoiado na lata de guaraná.{/i}"
    st_mobile "Quer? Tá fria, mas é honesta."
    st_mobile "Hoje foi o dia mais calmo de PR desde que eu entrei aqui. Sério. Ninguém gritou, ninguém reverteu nada."
    show st_mobile thinking at left_zoom
    st_mobile "Teu PR eu li em dez minutos. O meu a Lorena testou em meia hora. Pequeno é outra vida."
    if energia_cansaco():
        st_mobile "E, mano, vai pra casa daqui a pouco. A gente não precisa de herói, precisa de você amanhã."
    show st_mobile neutral at left_zoom
    st_mobile "PR pequeno, noite tranquila. Quem diria."
    hide st_mobile
    with dissolve
    return


label im_startup_s6_ajudar_st_techlead:
    show st_techlead neutral at right_zoom
    with dissolve
    st_techlead "Chegou na hora do ensaio. Vou montar a ferramenta do teste de carga, e eu quero alguém olhando junto."
    st_techlead "Primeira regra: nada de dado real. A gente gera usuários de mentira, com gastos de mentira."
    "{i}Ele abre um script que cria cinquenta estudantes inventados. Cada um abre o app, lança um gasto e pede a lista.{/i}"
    if pista_tem("st_p_conexoes"):
        st_techlead "Você lembra da noite da festa. Duzentas pessoas e as conexões em 80%%. Hoje eu quero ver isso acontecer de propósito, em pequeno."
    else:
        st_techlead "Na noite da festa dos mil, o banco reclamou de uma coisa. Hoje eu quero ver se ele reclama de novo, de propósito e em pequeno."
    show st_techlead thinking at right_zoom
    st_techlead "Fica de olho nas conexões abertas do banco. Eu cuido do resto."
    "{i}Otávio aperta Enter. No painel, o tempo de resposta mal se mexe.{/i}"
    "{i}A linha das conexões, não. Ela estava em dez e sobe de uma vez: trinta, quarenta, sessenta.{/i}"
    "{i}Você lê o número em voz alta. Otávio para o teste.{/i}"
    st_techlead "Sessenta. Com cinquenta pessoas de mentira, lançando um gasto cada uma."
    st_techlead "Veja bem: é como provar o molho de colher em colher. A panela ainda não queimou, mas já deu para sentir o gosto."
    show st_techlead serious at right_zoom
    st_techlead "Cinquenta pessoas de mentira e o banco já sentiu. Imagina o bandejão no primeiro dia de aula."
    show st_techlead neutral at right_zoom
    st_techlead "Hoje foi só para afinar a ferramenta. O cenário de verdade quem define é você, semana que vem: quantas pessoas, fazendo o quê, em que horário."
    "{i}Você anota no caderno: dez conexões paradas, sessenta com cinquenta usuários de mentira.{/i}"
    hide st_techlead
    with dissolve
    return


label im_startup_s6_conversar_st_techlead:
    show st_techlead neutral at right_zoom
    with dissolve
    st_techlead "Às nove eu fecho o notebook. Aconteça o que acontecer. Já avisei o Davi."
    "{i}Ele aponta para um post-it amarelo colado na tampa do notebook: “21h”.{/i}"
    show st_techlead thinking at right_zoom
    st_techlead "Não publico na sexta e não fico depois das nove. As duas regras nasceram na mesma noite."
    st_techlead "Aquela sexta de 2009. Publiquei às seis da tarde, caiu às sete, e eu fiquei até de madrugada consertando sozinho. Errei mais consertando do que no erro original."
    show st_techlead neutral at right_zoom
    st_techlead "Cabeça cansada não conserta nada. Só cria trabalho para a cabeça descansada do dia seguinte."
    hide st_techlead
    with dissolve
    return


# -------------------------------
# Sala de vidro (luz apagada)
# -------------------------------
label im_startup_s6_estudar_sala_vidro:
    "{i}A sala de vidro está escura. Você acende só a luminária do canto, e os post-its da parede viram sombras coloridas.{/i}"
    "{i}Você lê sobre teste de carga devagar. A primeira frase que fica: teste sem meta vira opinião.{/i}"
    "{i}Numa folha, você desenha um painel imaginário. No meio, o tempo da lista. Em volta, o que também precisa de olho: erros, conexões abertas no banco, a fila de envios e o custo da nuvem no fim do mês.{/i}"
    "{i}Embaixo, três perguntas para o cenário: quantas pessoas, fazendo o quê, em que horário.{/i}"
    if energia_cansaco():
        "{i}A luminária é a única luz acesa no andar. Você percebe que leu o mesmo parágrafo duas vezes e decide parar na próxima página.{/i}"
    "{i}E uma regra sublinhada no fim: usuários de mentira, dados de mentira. Nunca dados reais de pessoas.{/i}"
    return


# -------------------------------
# Café da esquina
# -------------------------------
label im_startup_s6_conversar_st_estudante:
    show st_estudante neutral at left_zoom
    with dissolve
    if mentoria_feitos() >= 1:
        st_estudante "Olha quem chegou! Você já conhece a Joana e a Rayane. Hoje a gente veio testar a versão nova antes de todo mundo."
    else:
        st_estudante "Deixa eu te apresentar. Essa é a Joana, de Letras. Essa é a Rayane, de Educação Física. Minhas colegas de república."
        st_npc_joana "E testers oficiais da Trocado. Sem crachá, mas com opinião."
    st_estudante "A gente começou ajudando a Lorena e agora não para mais."
    show st_estudante thinking at left_zoom
    st_estudante "Égua, a gente virou equipe de qualidade sem salário."
    st_npc_rayane "Salário não. Mas o pão de queijo daqui conta como benefício."
    show st_estudante neutral at left_zoom
    st_estudante "Sexta tem teste do clube, com os calouros. Tipo assim: tem cadeira pra você, se quiser vir."
    hide st_estudante
    with dissolve
    return


label im_startup_s6_observar_cafe:
    "{i}No café da esquina, três celulares em cima da mesinha, ao lado de uma cesta de pão de queijo. A Bia, a Joana e a Rayane testam a versão que vai para as lojas.{/i}"
    "{i}Você senta na mesa ao lado, abre o caderno e fica em silêncio: sem ajudar, só olhando.{/i}"
    show st_estudante neutral at left_zoom
    with dissolve
    if mentoria_feitos() < 1:
        st_estudante "Ah, oi! Essas são a Joana e a Rayane, da minha república. Elas testam tudo comigo."
        st_estudante "Pode olhar à vontade. A gente finge que você é a parede."
    "{i}A Joana usa o celular com a fonte enorme e o leitor de tela ligado. Ela passa o dedo pela lista, e uma voz rápida lê cada linha.{/i}"
    "{i}Ela para na lixeira ao lado de um gasto. A voz diz: “Excluir Xerox, R$ 2,40”.{/i}"
    st_npc_joana "Olha só. Agora ele diz o nome. Antes era só “botão”, e eu tinha que adivinhar."
    st_npc_joana "O leitor de tela não tem paciência. Nem eu. Mas esse aqui eu aprovo."
    "{i}A Rayane está na janela, onde o 4G dela pega pela metade. Ela toca em Excluir num café de R$ 3,50.{/i}"
    "{i}A confirmação aparece. Ela toca em Cancelar. Depois desce a lista inteira, devagar, e confere o total duas vezes.{/i}"
    st_npc_rayane "Ficou. O café ficou, o total ficou. Nada mudou."
    st_npc_rayane "Com internet ruim e tudo. Antes eu não confiava nem com internet boa."
    show st_estudante thinking at left_zoom
    "{i}A Bia lança o bandejão do dia, R$ 4,50, e fica olhando o total por um tempo, sem dizer nada.{/i}"
    st_estudante "Tipo assim: R$ 312,40 até a bolsa cair. E eu acredito nesse número."
    show st_estudante neutral at left_zoom
    "{i}Ela sorri para a tela. Não para vocês: para o total.{/i}"
    hide st_estudante
    with dissolve
    "{i}No seu caderno, três linhas: o rótulo da lixeira funcionou com o leitor de tela; cancelar no 4G fraco não mudou nada; a Bia confia no total.{/i}"
    return


# -------------------------------
# Terraço
# -------------------------------
label im_startup_s6_conversar_st_mentora:
    show st_mentora neutral at left_zoom
    with dissolve
    "{i}Tainá está encostada no guarda-corpo, de casaco, olhando as luzes da enseada.{/i}"
    st_mentora "Acabei de voltar da aceleradora. Reunião de uma hora que podia ser um e-mail."
    show st_mentora thinking at left_zoom
    st_mentora "Posso confessar uma coisa? Tô nervosa com a 1.0. Desde o banco eu não lançava nada tão grande."
    st_mentora "Mas aí eu olho o quadro e vejo cartão pequeno, teste escrito e risco com dono. E o nervoso diminui um pouco."
    show st_mentora neutral at left_zoom
    st_mentora "Sabe o que a gente faz sexta? Revisão da semana com bolo. Cada um traz uma coisa que deu certo e uma que deu errado."
    st_mentora "Ninguém aqui precisa virar a noite. Bolo na sexta, sim."
    hide st_mentora
    with dissolve
    return


label im_startup_s6_conversar_st_qualidade:
    show st_qualidade neutral at right_zoom
    with dissolve
    st_qualidade "Oxe, senta aqui, que eu tô organizando o teste de hoje à tarde com os calouros."
    "{i}No tablet, cinco colunas, uma por calouro, e uma anotação repetida em quatro delas.{/i}"
    show st_qualidade thinking at right_zoom
    st_qualidade "Primeiro, a tarefa: “lance o almoço de hoje”. Segundo, o que aconteceu: quatro de cinco foram no “+” e procuraram onde botar o dinheiro que entrou."
    st_qualidade "Eles acharam que o “+” era para adicionar dinheiro. Não gasto. Dinheiro."
    st_qualidade "Oxe, nunca tinha pensado: pra quem chega, “+” é dinheiro entrando."
    show st_qualidade neutral at right_zoom
    st_qualidade "A gente que fez o app lê “+” como “novo gasto” há meses. Nem enxerga mais. Por isso teste com quem chega agora vale ouro."
    st_qualidade "Cadê a evidência? Tá aqui: quatro de cinco. Amanhã eu levo pro Davi."
    hide st_qualidade
    with dissolve
    return


# -------------------------------
# Aceleradora Maré
# -------------------------------
label im_startup_s6_ajudar_st_ceo:
    show st_ceo neutral at right_zoom
    with dissolve
    st_ceo "Você veio! Preciso de alguém com cronômetro e coragem. O pitch tem que caber em três minutos."
    st_ceo "A mentora da aceleradora vai assistir. Ela foi investidora por dez anos. Ninguém sai igual de um ensaio com ela."
    "{i}O auditório do galpão está quase vazio. Na terceira fila, uma mulher de cabelo grisalho e caderno fechado no colo. Você senta duas cadeiras ao lado e prepara o cronômetro.{/i}"
    "{i}Vinícius sobe ao palco. Mil estudantes, festa, curva de cadastros, mercado, concorrentes, a história da mãe e uma lista de tudo o que a Trocado ainda vai fazer.{/i}"
    "{i}O cronômetro passa de três minutos. Você levanta a mão, como combinaram. Ele não vê.{/i}"
    "{i}Quatro minutos e quarenta segundos.{/i}"
    show st_ceo thinking at right_zoom
    st_ceo "E então? Pode falar. Eu aguento!"
    "{i}A mentora abre o caderno pela primeira vez. Não anota nada. Faz uma pergunta só:{/i}"
    "{i}“Dos estudantes que entraram há um mês, quantos ainda usam?”{/i}"
    "{i}Silêncio no auditório. Vinícius olha para os slides, depois para você.{/i}"
    st_ceo "Ela ouviu quatro minutos de mim e perguntou uma coisa só."
    "{i}Vocês descem para a última fila com o notebook. Você lê o tempo de cada parte em voz alta, e ele decide o que sai.{/i}"
    "{i}Sai o mercado. Saem os concorrentes. Sai a lista do futuro. Sai a curva de cadastros.{/i}"
    show st_ceo neutral at right_zoom
    st_ceo "Quatro slides a menos. Dói, mas dói menos que aquele silêncio."
    st_ceo "Se a pergunta é essa, a resposta tem que estar no centro do pitch. Não no apêndice!"
    "{i}No caderno, você anota a pergunta da mentora, palavra por palavra.{/i}"
    hide st_ceo
    with dissolve
    return


label im_startup_s6_conversar_st_ceo:
    show st_ceo neutral at right_zoom
    with dissolve
    st_ceo "Olha esse palco. Primeira vez que eu subo aqui. No demo day, todas essas cadeiras vão estar ocupadas."
    show st_ceo thinking at right_zoom
    st_ceo "Posso te contar um segredo? Eu tenho medo de palco. Muito."
    st_ceo "Em reunião eu falo sem parar. Num palco, a mão sua e eu esqueço o nome da empresa. Da minha empresa!"
    show st_ceo neutral at right_zoom
    st_ceo "Pitch eu faço dormindo. Acordado é que é difícil!"
    st_ceo "Hoje eu ensaio até a voz cansar. No demo day, quero estar entediado de tanto saber o texto."
    hide st_ceo
    with dissolve
    return
