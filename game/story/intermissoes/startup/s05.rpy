# s05.rpy
# Rota Startup, tempo livre da semana 5: segunda, 16h às 19h30, dentro da
# st_15 (depois do planejamento). Design: docs/design/intermissoes-startup.md,
# semana 5. O motor aplica tempo, energia, amizade, pistas e registro extra
# depois de cada label; aqui só as falas.

label im_startup_abertura_5:
    "{i}Segunda, quatro da tarde. O plano das três últimas semanas está no quadro: dois itens e três riscos, cada um com dono.{/i}"
    "{i}O resto da tarde é seu.{/i}"
    if energia_cansaco():
        "{i}Você esfrega os olhos antes de abrir o mapa. O planejamento cansou mais do que parecia, e o tempo livre de hoje vai ser mais curto.{/i}"
    return


# -------------------------------
# Mesa da equipe
# -------------------------------
label im_startup_s5_ajudar_st_techlead:
    show st_techlead neutral at right_zoom
    with dissolve
    st_techlead "Puxa uma cadeira. O risco do pico ficou comigo de manhã, então eu vou fazer o que dono de risco faz: olhar antes de doer."
    st_techlead "Vou abrir o painel do banco da noite da festa dos mil. Muita gente entrou de uma vez. Quero saber o que o banco achou disso."
    "{i}A tela se enche de gráficos: uso de memória, tempo de resposta, consultas por segundo. Otávio empurra o notebook na sua direção.{/i}"
    show st_techlead thinking at right_zoom
    st_techlead "Não vou te dizer onde olhar. Procura o gráfico que subiu junto com a festa."
    "{i}Você passa pelos gráficos devagar. O tempo de resposta sobe um pouco perto das sete da noite e volta. A memória quase não mexe.{/i}"
    "{i}Um gráfico pequeno, no canto, faz uma montanha na mesma hora: conexões abertas. No pico, a linha chega a 80%% do limite.{/i}"
    "{i}Você aponta. Otávio confere o horário com o registro de acessos: umas duzentas pessoas ao mesmo tempo.{/i}"
    st_techlead "Isso. Duzentas pessoas. Não duas mil. Duzentas."
    st_techlead "Veja bem: cada função que acorda na nuvem abre a própria conexão com o banco. Duzentas funções acordadas, duzentas conexões. É uma cozinha onde cada garçom traz o próprio fogão."
    show st_techlead serious at right_zoom
    st_techlead "Agora pensa no primeiro dia de aula. O bandejão abre, todo mundo lança o almoço no mesmo minuto."
    "{i}Você faz a conta de cabeça e não gosta do resultado.{/i}"
    show st_techlead neutral at right_zoom
    st_techlead "Pois é. A festa quase achou o limite com duzentas pessoas. Anota aí, que esse risco é meu."
    st_techlead "Eu ainda não sei a solução. Mas agora sei a pergunta. Isso já é metade da obra."
    "{i}Você anota o número e o horário no caderno, com a palavra “conexões” sublinhada duas vezes.{/i}"
    hide st_techlead
    with dissolve
    return


label im_startup_s5_conversar_st_techlead:
    show st_techlead neutral at right_zoom
    with dissolve
    st_techlead "E aí, sobreviveu ao planejamento?"
    st_techlead "O Davi saiu da sala com cara de quem perdeu um cachorro. As medalhas eram filhas dele."
    show st_techlead thinking at right_zoom
    st_techlead "Veja bem: dizer sim é fácil. Todo mundo sai feliz da reunião e infeliz três semanas depois."
    st_techlead "Dizer não para medalha é o trabalho mais difícil desta empresa. E o mais barato."
    show st_techlead neutral at right_zoom
    st_techlead "Você fez a conta com o que cabe, não com o que a gente queria que coubesse. Isso eu levo para o meu registro de decisões."
    hide st_techlead
    with dissolve
    return


label im_startup_s5_ajudar_st_mobile:
    show st_mobile serious at left_zoom
    with dissolve
    st_mobile "Mano, chegou na hora. Tem uma falha na fila de sincronização que tá me tirando do sério."
    st_mobile "Se o app fecha no meio do envio, a fila trava. O gasto fica preso no celular e não sobe nunca mais."
    "{i}Ele te passa o Tijolo, o celular de teste mais lento da mesa. Você lança um café de R$ 5, e no meio do envio fecha o app à força.{/i}"
    "{i}Abre de novo. O café está na lista do celular, mas não sobe. Nenhum aviso.{/i}"
    show st_mobile thinking at left_zoom
    st_mobile "Reproduziu de primeira! Pô, você tem dedo pra bug."
    st_mobile "Abre o relatório de falhas, que eu quero ver o erro que o app mandou."
    "{i}O relatório lista cada falha que o app enviou para o serviço de monitoramento. A sua está no topo, de dois minutos atrás.{/i}"
    "{i}Ao lado do erro, junto com o modelo do celular e a versão do app, aparece um campo a mais: o e-mail da pessoa.{/i}"
    "{i}Você rola a lista. Todas as falhas da semana levam um e-mail junto, para um serviço de fora da equipe.{/i}"
    show st_mobile serious at left_zoom
    st_mobile "É, eu sei. Botei isso pra saber quem tava com problema, lá no começo do beta."
    st_mobile "Pô, depois eu tiro isso. Anota pra me cobrar."
    "{i}Você anota. Com nome, data e o que precisa sair.{/i}"
    show st_mobile neutral at left_zoom
    st_mobile "Agora a fila. Olha só: o app marca o gasto como “enviando” e, se fecha no meio, nunca desmarca."
    "{i}Vocês escrevem juntos a correção: ao abrir, o app procura o que ficou preso e tenta de novo. Você fecha o app à força mais três vezes. O café sobe nas três.{/i}"
    st_mobile "Fechou! Fila destravada. Trocadilho do dia: quem trava a fila é a fila."
    hide st_mobile
    with dissolve
    return


label im_startup_s5_conversar_st_mobile:
    show st_mobile serious at left_zoom
    with dissolve
    st_mobile "Não fala comigo. Tô de luto."
    "{i}Na tela dele, uma pasta chamada “medalhas”. Dentro, doze ícones desenhados à mão: um cofrinho, um foguete, um pão de queijo dourado.{/i}"
    st_mobile "Fiz doze medalhas. Doze! Tem até uma pra quem lança o bandejão cinco dias seguidos."
    menu (tipo="conversa"):
        "Rio junto: o pão de queijo dourado é bom demais.":
            show st_mobile neutral at left_zoom
            st_mobile "Né? Levei uma tarde nesse pão de queijo. Tem até brilho."
        "Lembro que as medalhas não morreram, só foram para depois.":
            show st_mobile thinking at left_zoom
            st_mobile "Depois da 1.0. Eu sei, eu sei. Eu tava na sala."
    show st_mobile neutral at left_zoom
    st_mobile "Tá, tá. Depois da 1.0. A Bia não precisa de medalha, precisa do total certo."
    st_mobile "Mas quando chegar a hora, o pão de queijo dourado é o primeiro."
    hide st_mobile
    with dissolve
    return


# -------------------------------
# Sala de vidro
# -------------------------------
label im_startup_s5_conversar_st_mentora:
    show st_mentora neutral at left_zoom
    with dissolve
    "{i}Tainá está riscando e reescrevendo a lista de riscos no vidro. Os três de hoje de manhã já ganharam datas.{/i}"
    st_mentora "Oi! Senta. Quero te contar por que eu fiz aquela pergunta mais cedo, sobre a pressão."
    show st_mentora thinking at left_zoom
    st_mentora "É que eu já fui a pessoa que respondia “tudo bem” com febre."
    st_mentora "No banco, eu trabalhava doente pra bater meta. Achava bonito. Chegava antes de todo mundo, saía depois."
    st_mentora "No banco eu achava que cansaço era prova de dedicação. Era só cansaço."
    show st_mentora neutral at left_zoom
    st_mentora "As próximas três semanas vão apertar. Lançamento, loja, demo day. E a gente vai precisar de gente descansada, não de gente heroica."
    if energia_cansaco():
        st_mentora "E, olhando pra você agora, eu diria: hoje, depois daqui, casa. Sério."
    st_mentora "Se pesar, fala comigo antes de virar a noite. Combinado?"
    hide st_mentora
    with dissolve
    return


label im_startup_s5_estudar_sala_vidro:
    "{i}O gráfico de retenção da manhã ainda está aberto no telão: uma linha só, de todo mundo, parada em 22%%.{/i}"
    "{i}Você exporta os dados e separa as pessoas pela semana em que entraram. Quem chegou com a festa dos mil ganha uma linha só dela.{/i}"
    "{i}As turmas antigas caem nas primeiras semanas e depois se firmam, baixas mas estáveis. A turma da festa só tem três dias e já caiu rápido: muita gente instalou na sexta e não lançou mais nada.{/i}"
    "{i}No gráfico de cadastros, essa turma era só um pico bonito. Separada, ela mostra quem já foi embora.{/i}"
    if energia_cansaco():
        "{i}Os números começam a dançar na tela. Você para, bebe água e confere a conta de novo, devagar. Ela fecha.{/i}"
    "{i}No canto da folha, você escreve a regra antes de esquecer: primeiro defina a ação que importa e a janela. Depois, separe por quando a pessoa chegou.{/i}"
    return


# -------------------------------
# Café da esquina
# -------------------------------
label im_startup_s5_conversar_st_ceo:
    show st_ceo neutral at right_zoom
    with dissolve
    st_ceo "Olha o slide novo! Antes era a curva de cadastros, subindo até o céu. Agora é este aqui."
    "{i}No notebook, um slide com uma frase grande e um número: quantos voltam a usar.{/i}"
    st_ceo "Menos bonito. Mais verdadeiro. O fundo vai gostar. Eu acho. Espero!"
    play sound "audio/effects/cell_vibration.ogg"
    "{i}O celular dele vibra em cima da mesa. Na tela: “Mãe”.{/i}"
    show st_ceo thinking at right_zoom
    st_ceo "Oi, mãe. Tô, tô trabalhando. É, aquele app. Não, não é banco."
    st_ceo "Ela quer saber o que é “retenção”. Me ajuda: uma frase."
    "{i}Você sussurra uma frase curta. Ele repete no telefone.{/i}"
    st_ceo "Mãe, é quantos voltam. Isso. Não, não é empréstimo!"
    show st_ceo neutral at right_zoom
    st_ceo "Ela entendeu. Se a minha mãe entende, o investidor entende. Esse é o teste agora."
    hide st_ceo
    with dissolve
    return


# -------------------------------
# Bandejão da universidade
# -------------------------------
label im_startup_s5_conversar_st_estudante:
    show st_estudante thinking at left_zoom
    with dissolve
    st_estudante "Égua, saiu a lista da monitoria. Sessenta calouros. Sessenta! Ano passado eram vinte e dois."
    st_estudante "E eu tenho que explicar limite e derivada pra quem acabou de sair do ensino médio."
    "{i}Ela roda o chaveiro de boto no dedo, sem perceber.{/i}"
    st_estudante "Tipo assim: eu ainda lembro de quando eu era a perdida. Primeira semana, eu não achava nem a sala."
    show st_estudante neutral at left_zoom
    st_estudante "Talvez seja por isso que eles vão me entender. Eu sei onde a gente se perde."
    st_estudante "Vou começar pelo dinheiro. Derivada é quanto o saldo muda por dia. Todo mundo entende saldo."
    hide st_estudante
    with dissolve
    return


label im_startup_s5_observar_bandejao:
    "{i}Fim de tarde no bandejão. A fila do jantar ainda não começou, e as mesas estão cheias de gente estudando.{/i}"
    "{i}A Bia está numa mesa perto da janela, ajudando a Rayane com o app. Você senta perto, abre o caderno e não interrompe.{/i}"
    show st_estudante neutral at left_zoom
    with dissolve
    st_estudante "Lança o café que você tomou agora. Três reais, né?"
    st_npc_rayane "Três e cinquenta. Mas meu 4G acabou. Acaba todo dia 20, é pré-pago."
    "{i}Rayane lança mesmo assim. Toca em Salvar. Uma rodinha começa a girar no topo da tela.{/i}"
    "{i}A rodinha gira. Gira mais. Nenhuma mensagem.{/i}"
    st_npc_rayane "Salvou ou não salvou? A rodinha não me diz nada."
    show st_estudante thinking at left_zoom
    st_estudante "Salvou no celular. Eu acho. Quando a internet volta, ele manda."
    st_npc_rayane "Você acha?"
    st_estudante "...Eu acho."
    "{i}As duas olham para a tela. O café aparece na lista, mas sem nenhum sinal diferente dos outros gastos.{/i}"
    st_npc_rayane "Então eu vou anotar no papel também. Por garantia."
    hide st_estudante
    with dissolve
    "{i}Ela tira uma caneta da mochila e escreve “café 3,50” no canto do caderno. Exatamente o que a Bia faz com o caderno de capa de flores.{/i}"
    "{i}Você anota no seu caderno, com as palavras dela: “salvou ou não salvou?”. E embaixo, a sua leitura: falta um aviso de “salvo no celular, enviando”.{/i}"
    "{i}Não é um bug. O app fez a coisa certa. Ele só não contou para ninguém.{/i}"
    return


label im_startup_s5_conversar_st_qualidade:
    show st_qualidade neutral at right_zoom
    with dissolve
    st_qualidade "Oxe, o planejamento foi bom, né? Dois itens. Eu quase chorei de alegria."
    show st_qualidade thinking at right_zoom
    st_qualidade "Você viu que eu botei o leitor de tela na definição de pronto. Teve gente torcendo o nariz."
    st_qualidade "Primeiro: se o botão não diz o nome, a pessoa não sabe o que vai apagar. Segundo: isso não é detalhe, é o botão inteiro."
    if mentoria_feitos() >= 3:
        show st_qualidade neutral at right_zoom
        st_qualidade "Foi a Joana que me convenceu, no clube. Depois daquela tarde eu não consigo mais olhar uma lixeira sem nome."
    else:
        st_qualidade "Leitor de tela não é extra. Tem gente que só usa assim, e usa muito bem."
    show st_qualidade neutral at right_zoom
    st_qualidade "Cadê a evidência? Na definição de pronto. Agora ninguém esquece."
    hide st_qualidade
    with dissolve
    return
