# s04.rpy
# Rota Startup, tempo livre da semana 4: sexta, 14h30 às 18h, antes da festa
# dos mil (st_14). Design: docs/design/intermissoes-startup.md, semana 4.
# O motor (logic/intermissao.rpy) mostra o fundo do local e aplica tempo,
# energia, amizade, pista e registro extra depois de cada label.

label im_startup_abertura_4:
    scene bg startup_coworking_tarde
    with dissolve
    "{i}Sexta, duas e meia da tarde. O contador do beta marca 994 estudantes, e o Vinícius atualiza o painel a cada minuto.{/i}"
    "{i}A pizza já está encomendada, “por precaução”. O terraço fechou para arrumar a festa das seis.{/i}"
    if energia_cansaco():
        "{i}Você boceja antes de abrir o mapa. A semana pesou, e hoje o tempo livre vai ser mais curto.{/i}"
    return


# -------------------------------
# Mesa da equipe
# -------------------------------
label im_startup_s4_conversar_st_mobile:
    show st_mobile neutral at left_zoom
    with dissolve
    st_mobile "Chega aí. Tô montando o id único da fila. Olha que lindo."
    "{i}Na tela, cada gasto ganha um código comprido antes de sair do celular.{/i}"
    st_mobile "É tipo o número do pedido da pizza. Se a pizzaria recebe o pedido 42 duas vezes, ela não faz duas pizzas. Faz uma e fala “já tá saindo”."
    st_mobile "O servidor vai fazer igual. Mesmo id chegou de novo? Ignora e responde que já tem."
    show st_mobile thinking at left_zoom
    st_mobile "Agora, assunto sério: a playlist da festa. Me dá uma sugestão, que a do Vinícius é só podcast de pitch."
    st_mobile "Eu ia abrir com uma música chamada “Duas vezes”. Brincadeira. Talvez."
    "{i}Você sugere uma música. Davi anota no celular de teste, entre dois prints do app.{/i}"
    show st_mobile neutral at left_zoom
    st_mobile "Fechou. Entra logo depois do brinde. E só toca uma vez, prometo."
    hide st_mobile
    with dissolve
    return


# -------------------------------
# Sala de vidro
# -------------------------------
label im_startup_s4_conversar_st_ceo:
    show st_ceo neutral at right_zoom
    with dissolve
    # A notícia dos mil corre às 15h (st_14): antes disso o contador ainda não virou.
    if game_hour < 15:
        st_ceo "Você chegou na hora certa! Faltam seis cadastros para mil. Seis!"
        st_ceo "O post já está pronto, só falta o número virar. Escuta: “Mil estudantes confiam na Trocado para cuidar do dinheiro!” Forte, né?"
    else:
        st_ceo "Você viu? Mil! Bateu às três em ponto, e eu ainda não parei de olhar o contador."
        st_ceo "O post sai daqui a pouco. Escuta: “Mil estudantes confiam na Trocado para cuidar do dinheiro!” Forte, né?"
    menu (tipo="conversa"):
        "Ajudo a deixar o texto mais simples.":
            "{i}Você troca “confiam na Trocado para cuidar do dinheiro” por “mil estudantes já entraram na Trocado”. Entrar é fato; confiar ainda precisa de número.{/i}"
            st_ceo "Mais curto e mais verdadeiro. Detesto quando isso acontece. Fica assim!"
        "Pergunto quantos desses mil voltam a usar.":
            show st_ceo thinking at right_zoom
            st_ceo "Mil! ..."
            st_ceo "Tá, tá. Quantos voltam. Eu sei que a Lorena vai perguntar a mesma coisa daqui a pouco."
            st_ceo "Segunda a gente olha esse número com calma, prometo. Hoje deixa eu sorrir!"
    show st_ceo neutral at right_zoom
    if game_hour < 15:
        "{i}O celular dele vibra. Ele olha a tela e levanta os dois braços.{/i}"
        st_ceo "Mil! Bateu! Posta, posta, posta!"
    else:
        "{i}Ele aperta Publicar e levanta os dois braços, como se o post fosse gol.{/i}"
        st_ceo "Postado! Agora é pizza."
    hide st_ceo
    with dissolve
    return


label im_startup_s4_conversar_st_mentora:
    show st_mentora neutral at left_zoom
    with dissolve
    st_mentora "Senta aqui um minuto, antes que o Vinícius me chame de novo pro post."
    st_mentora "Me conta: como foi negociar com ele na segunda? Por dentro, não o que ficou no documento."
    "{i}Você conta. Tainá escuta e abre o registro do acordo no notebook.{/i}"
    show st_mentora thinking at left_zoom
    if st_acordo_opcao == "investigar_agora":
        st_mentora "Investigar agora. O Otávio já marcou a primeira call com a instituição, terça de manhã."
        st_mentora "E a data nova da 1.0 o Vinícius vai conversar com o fundo. Ele mesmo pediu para ficar com essa parte."
    else:
        st_mentora "Base primeiro. E o protótipo do consentimento já tem dono: uma tarde do Davi, na semana que vem."
        st_mentora "O Vinícius já contou o acordo para o fundo do mesmo jeito que está aqui. Eu conferi."
    show st_mentora neutral at left_zoom
    st_mentora "Acordo bom é aquele que os dois contam do mesmo jeito uma semana depois."
    st_mentora "Agora bora, que eu preciso tirar três exclamações daquele post."
    hide st_mentora
    with dissolve
    return


label im_startup_s4_estudar_sala_vidro:
    "{i}O diagrama da reunião de segunda ainda está no vidro: o celular, a fila, a nuvem, o banco. Ao lado, alguém desenhou uma pizza com o número 42.{/i}"
    "{i}Você pega uma folha e escreve duas frases, uma embaixo da outra.{/i}"
    "{i}“Excluir o gasto X.” Se o pedido chegar duas vezes, o gasto continua excluído. Nada muda.{/i}"
    "{i}“Somar R$ 20 ao total.” Se chegar duas vezes, o total sobe R$ 40. Tudo muda.{/i}"
    if energia_cansaco():
        "{i}Você relê a mesma linha três vezes até ela entrar. A cabeça está lenta hoje, mas a ideia fica.{/i}"
    else:
        "{i}A diferença cabe numa página: uma operação que pode repetir sem estrago, e outra que precisa de uma chave para saber se já aconteceu.{/i}"
    "{i}No fim da folha, você anota a receita: o app manda o id do gasto, e o servidor guarda os ids que já viu.{/i}"
    return


# -------------------------------
# Café da esquina
# -------------------------------
label im_startup_s4_conversar_st_techlead:
    show st_techlead neutral at right_zoom
    with dissolve
    "{i}Otávio está na mesinha mais longe da escada, com um espresso e a caneca esmaltada vazia ao lado, só por companhia.{/i}"
    st_techlead "Vim antes do barulho. Lá em cima já estão testando o som."
    st_techlead "Minha filha diz que eu sou o único pai que sai de festa para descansar. Ela estuda Física em Niterói. Liga toda sexta para saber se o manjericão sobreviveu."
    show st_techlead thinking at right_zoom
    st_techlead "Veja bem: manjericão é igual sistema em produção. Não pode ficar sem água, nem com água demais. E ninguém lembra dele até morrer."
    if energia_cansaco():
        st_techlead "E pela sua cara, você também precisa de um modo econômico hoje. Ninguém aqui ganha medalha por ficar até o fim."
    show st_techlead neutral at right_zoom
    st_techlead "Eu vou à festa, sim. Festa eu frequento como servidor: ligado, mas em modo econômico."
    hide st_techlead
    with dissolve
    return


# -------------------------------
# Bandejão da universidade
# -------------------------------
label im_startup_s4_conversar_st_estudante:
    show st_estudante neutral at left_zoom
    with dissolve
    st_estudante "Égua, olha isso. Metade da república baixou o app hoje. Sete pessoas, numa tarde."
    st_estudante "Eu mostrei o caderno, mostrei o total, contei do almoço duplicado e disse que vocês estão consertando."
    show st_estudante thinking at left_zoom
    st_estudante "Agora eu tô com medo. Tipo assim: se duplicar pra elas, eu mudo de república."
    "{i}Você conta, sem detalhe técnico, que a equipe está montando uma forma de o servidor reconhecer um gasto repetido.{/i}"
    show st_estudante neutral at left_zoom
    st_estudante "Então eu posso falar que tá chegando? Não vou prometer data. Aprendi com vocês."
    hide st_estudante
    with dissolve
    return


label im_startup_s4_observar_bandejao:
    "{i}Na mesa comprida, a Bia e mais cinco estudantes da república, no lanche da tarde: seis copos de suco e seis celulares. Lorena senta duas mesas para trás, sem chamar atenção.{/i}"
    "{i}Você abre o caderno e faz uma coluna para cada pessoa: quando abre o app e o que faz lá dentro. Sem nomes, só letras.{/i}"
    show st_estudante neutral at left_zoom
    with dissolve
    "{i}A Bia lança o suco antes de sentar: R$ 6. Confere o total. Guarda o celular.{/i}"
    st_estudante "Vocês lançaram o lanche? É rapidinho, olha."
    hide st_estudante
    with dissolve
    "{i}A primeira colega abre o app só porque a Bia pediu, olha a tela inicial e fecha. Não lança nada.{/i}"
    "{i}A segunda e a terceira instalaram nesta semana, pelo boca a boca da república. O ícone está lá, na segunda página do celular. Nenhuma das duas lançou um gasto até hoje.{/i}"
    "{i}A quarta é a Rayane. Ela nem abre.{/i}"
    st_npc_rayane "Eu só abro no dia 10, pra ver quanto tenho. Depois dá medo."
    "{i}A primeira colega concorda com a cabeça. A quinta também: abre quando a bolsa cai, olha o número e some até o mês seguinte.{/i}"
    show st_estudante thinking at left_zoom
    with dissolve
    st_estudante "Égua. Eu achava que todo mundo fazia igual a mim."
    hide st_estudante
    with dissolve
    show st_qualidade thinking at right_zoom
    with dissolve
    st_qualidade "Anota exatamente como ela falou: “depois dá medo”. Não traduz."
    st_qualidade "Primeiro: quem instala não é quem usa. Segundo: quem abre uma vez por mês não é quem usa todo dia."
    hide st_qualidade
    with dissolve
    "{i}No caderno, a conta da mesa fica assim: das cinco colegas, três só abrem no dia da bolsa e duas nunca lançaram nada. Só a Bia lança todo dia.{/i}"
    return


label im_startup_s4_conversar_st_qualidade:
    show st_qualidade neutral at right_zoom
    with dissolve
    st_qualidade "Oxe, chegou! Senta, que eu tô fechando uma lista."
    "{i}No tablet, uma lista com os nomes de quem mais mandou feedback no beta. A Bia em primeiro, com trinta e uma mensagens.{/i}"
    st_qualidade "Primeiro: quem mandou mais. Segundo: quem explicou melhor. A Bia ganha nos dois."
    show st_qualidade thinking at right_zoom
    st_qualidade "Vou mandar uma mensagem pra cada um, hoje ainda. Gente que escreve pra gente às onze da noite, irritada, e ainda conta o passo a passo."
    st_qualidade "Quase ninguém agradece a quem reclama direitinho. Hoje eu agradeço."
    show st_qualidade neutral at right_zoom
    st_qualidade "A da Bia eu escrevo por último. Com calma, que ela merece."
    hide st_qualidade
    with dissolve
    return
