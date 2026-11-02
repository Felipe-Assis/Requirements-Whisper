# s08.rpy
# Tempo livre da rota Startup, semana 8 (quarta, primeiro dia do semestre,
# depois do pico da st_18; véspera do demo day). Fonte:
# docs/design/intermissoes-startup.md, seção 3 (Semana 8). Sem estudar nesta
# semana. Labels por convenção do motor (logic/intermissao.rpy); as
# recompensas são aplicadas pelo motor depois de cada label.

label im_startup_abertura_8:
    if st_d17_carga:
        "{i}Quarta, uma e meia. O pico do primeiro dia passou sem ninguém notar. Amanhã é o demo day.{/i}"
    else:
        "{i}Quarta, uma e meia. O pico passou depois de vinte minutos de aperto. Amanhã é o demo day.{/i}"
    "{i}É o último tempo livre antes do palco. A cidade está cheia de calouros com mochila nova.{/i}"
    if energia_cansaco():
        "{i}Você boceja antes de abrir o mapa. Hoje o tempo livre vai ser mais curto.{/i}"
    return


# ---------------- mesa ----------------

label im_startup_s8_conversar_st_mobile:
    "{i}Davi não tira o olho do painel. A perna balança embaixo da mesa sem parar.{/i}"
    show st_mobile neutral at center_zoom
    with dissolve
    st_mobile "Viu o número? Viu?"
    st_mobile "Hoje três mil pessoas usaram um botão que eu fiz. Três mil, mano."
    if not st_d17_carga:
        show st_mobile thinking
        st_mobile "Tá, teve os vinte minutos de lista lenta. Ainda tô digerindo. Mas ninguém perdeu gasto, e isso eu não troco."
        show st_mobile neutral
    st_mobile "Quando eu entrei aqui, o app tinha duzentas pessoas. Eu conhecia metade pelo nome da avaliação."
    "{i}Ele mostra o celular: uma mensagem da mãe, com três pontos de exclamação, perguntando se o app dele é o do jornal da faculdade.{/i}"
    st_mobile "Não é do jornal. É do grupo da república da Bia. Mas deixa ela achar que é do jornal."
    st_mobile "Trocadilho de comemoração: hoje o app não travou, ele trabalhou. Tá, esse foi fraco. Tô sem sono pra fazer melhor."
    hide st_mobile
    with dissolve
    return

label im_startup_s8_conversar_st_techlead:
    "{i}Otávio está com o painel aberto e a caneca esmaltada na mão, como sempre. Só que hoje ele sorri para o gráfico.{/i}"
    show st_techlead neutral at center_zoom
    with dissolve
    if st_d17_carga:
        st_techlead "Sabe qual é o melhor pico? O que ninguém nota."
        st_techlead "Ninguém escreveu no grupo da república, ninguém ligou, ninguém lembrou que o banco existe. Para mim, isso é aplauso."
        st_techlead "O teste da semana passada achou o limite de conexões antes dos calouros. A correção entrou antes. A ordem certa."
    else:
        show st_techlead thinking
        st_techlead "Vinte minutos de gente esperando a lista, com a bandeja na mão."
        st_techlead "O teste achou o problema. A correção ficou na fila. Teste que acha problema só ajuda se a correção entra antes."
        st_techlead "Aprendi de novo hoje, aos cinquenta. A gente nunca termina de aprender essa."
        show st_techlead neutral
    st_techlead "Veja bem: obra boa é a que ninguém comenta. Quando o vizinho reclama, é porque alguma coisa caiu."
    "{i}Ele bebe um gole e aponta para o horário no canto do painel.{/i}"
    st_techlead "Hoje eu saio às seis. Amanhã tem palco, e palco eu deixo para o Vinícius."
    hide st_techlead
    with dissolve
    return


# ---------------- sala de vidro ----------------

label im_startup_s8_conversar_st_mentora:
    "{i}Na sala de vidro, Tainá cobriu uma parede inteira com post-its: coral, amarelo e verde. São as oito semanas, da primeira entrevista ao pico de hoje.{/i}"
    show st_mentora neutral at center_zoom
    with dissolve
    st_mentora "Chegou bem na hora. Tô rascunhando a retrospectiva das oito semanas."
    st_mentora "Me conta: se a gente começasse tudo de novo amanhã, o que você faria diferente?"
    menu (tipo="conversa"):
        "Pediria ajuda mais cedo, em vez de tentar tudo por conta própria primeiro.":
            show st_mentora thinking
            st_mentora "Boa. Pedir cedo custa cinco minutos de vergonha. Pedir tarde custa uma noite."
            st_mentora "Vou escrever isso num post-it verde. Verde é \"já sei\", mas a gente esquece."
        "Ia mais vezes ao bandejão ver a Bia usando o app.":
            show st_mentora thinking
            st_mentora "Também acho. Toda vez que alguém foi lá, voltou com alguma coisa que a entrevista não pegou."
            st_mentora "Observar ensina coisa que pergunta nenhuma ensina."
        "Testaria o pico com mais folga, antes de tudo ficar apertado.":
            show st_mentora thinking
            st_mentora "Isso. O teste veio, mas veio colado no lançamento. Folga também é requisito."
            st_mentora "Na próxima volta, o teste de carga entra no plano junto com a tela, não no fim."
    show st_mentora neutral
    st_mentora "E sabe o que eu não mudaria? A gente ouviu antes de construir."
    st_mentora "Retrospectiva não é tribunal. É pra próxima volta ser mais leve."
    if energia_cansaco():
        st_mentora "E pra próxima volta não deixar ninguém com essa cara de semana longa. Hoje você sai cedo, combinado?"
    hide st_mentora
    with dissolve
    return


# ---------------- bandejão ----------------

label im_startup_s8_conversar_st_estudante:
    "{i}Bia está numa mesa do canto, cercada de calouros com as listas da monitoria de Cálculo. Quando você chega, ela respira fundo.{/i}"
    show st_estudante thinking at center_zoom
    with dissolve
    st_estudante "Oi! Pode sentar. Eu tô ensaiando a fala de amanhã de cabeça e esquecendo a cada cinco minutos."
    st_estudante "Égua, eu nunca subi num palco. Na escola eu fugia até da apresentação de grupo."
    show st_estudante neutral
    st_estudante "Mas olha o que aconteceu agora há pouco. Uma caloura me perguntou: \"Esse app aí, o total dele mente?\""
    st_estudante "Tipo assim: dois meses atrás eu ia dizer que sim. Com o almoço de R$ 20 duplicado no ônibus."
    st_estudante "Eu disse: agora não. E é verdade."
    "{i}Ela sorri, meio sem graça.{/i}"
    st_estudante "Acho que amanhã eu só conto isso. Do jeito que aconteceu, com o valor."
    hide st_estudante
    with dissolve
    return

label im_startup_s8_observar_bandejao:
    "{i}Primeiro dia do semestre. O bandejão está barulhento, e a fila ainda chega perto da escada, mesmo depois do almoço.{/i}"
    show st_qualidade neutral at left_zoom
    show st_estudante neutral at right_zoom
    with dissolve
    st_qualidade "Senta do meu lado. Primeiro: olha. Segundo: não ajuda. Terceiro: anota."
    st_estudante "Três calouros da minha monitoria. Eles tão comparando app de finanças desde a fila."
    hide st_qualidade
    hide st_estudante
    with dissolve
    "{i}Na mesa da frente, três calouros com mochila nova põem os celulares lado a lado. Três apps diferentes, três telas de cadastro.{/i}"
    "{i}Um deles desiste do primeiro app na terceira tela: pediu o CPF antes de mostrar qualquer coisa.{/i}"
    "{i}O segundo app fica aberto mais tempo. Tem gráfico colorido, mas o calouro não acha onde lançar o almoço.{/i}"
    show st_estudante thinking at right_zoom
    with dissolve
    st_estudante "Ele vai perguntar pra mim. Eu sei que vai."
    "{i}E pergunta. Bia só responde: \"Usa o que você quiser. Eu uso o Trocado porque o total não mente.\"{/i}"
    hide st_estudante
    with dissolve
    "{i}O calouro abre o Trocado. Você acompanha cada toque, do cadastro ao primeiro gasto.{/i}"
    "{i}E-mail e senha. Uma tela explicando o que o app guarda e como apagar. Ele lê a frase curta da Tainá até o fim.{/i}"
    "{i}Na tela principal, ele procura alguma coisa com o dedo no ar. Você anota: parou quatro segundos no total do mês, como quem procura um saldo.{/i}"
    "{i}Depois toca no botão de novo gasto. Digita 4,50. Escolhe \"Alimentação\". Salvar.{/i}"
    "{i}O almoço aparece uma vez só, e o total muda na hora. Ele mostra a tela para o amigo, sem dizer nada.{/i}"
    show st_qualidade thinking at left_zoom
    with dissolve
    if mentoria_feitos() >= 4:
        st_qualidade "Cadê a evidência? Tá aí: primeiro uso, sem ajuda, um minuto e meio. E ele travou no mesmo lugar onde o Ítalo travou."
    else:
        st_qualidade "Cadê a evidência? Tá aí: primeiro uso, sem ajuda, um minuto e meio. E ele travou procurando um saldo."
    st_qualidade "Oxe, \"total do mês\" ainda não é a palavra de quem chega. Isso vai pra retrospectiva."
    hide st_qualidade
    with dissolve
    "{i}No caderno, você escreve: \"veterana recomendou\", \"CPF cedo afasta\", \"procurou saldo\". Sem nomes.{/i}"
    return

label im_startup_s8_conversar_st_qualidade:
    "{i}Lorena tem o tablet apoiado no copo de suco e lê avaliações em voz baixa, como quem corrige redação.{/i}"
    show st_qualidade neutral at center_zoom
    with dissolve
    st_qualidade "Oi! Chegou a hora boa: as primeiras avaliações da 1.0."
    st_qualidade "Nota 4,6 nas últimas cinquenta. Cinquenta! Na semana passada eu comemorava quando chegavam três."
    show st_qualidade thinking
    st_qualidade "Cadê a evidência? Tá aqui. E ninguém falou de total errado. Nenhuma."
    if not st_d17_carga:
        st_qualidade "Três falam de lista lenta na hora do almoço. Justo. Foram vinte minutos, e eu estaria brava também."
    else:
        st_qualidade "A mais crítica reclama da cor do botão. Oxe, eu aceito essa com um sorriso."
    show st_qualidade neutral
    st_qualidade "Teve uma que eu já copiei pro caderninho: \"o app que não me faz sentir burra com dinheiro\"."
    st_qualidade "Primeiro: é a frase do ano. Segundo: ela fala de vergonha, não de função. Terceiro: é por isso que a gente testa com gente."
    hide st_qualidade
    with dissolve
    return


# ---------------- aceleradora ----------------

label im_startup_s8_ajudar_st_ceo:
    "{i}Ensaio geral na Aceleradora Maré. Hoje o telão está ligado de verdade, e a logo da Trocado ocupa a parede inteira.{/i}"
    show st_ceo neutral at center_zoom
    with dissolve
    st_ceo "Que bom que você veio! Preciso de alguém que não tenha medo de me corrigir."
    st_ceo "Duas tarefas. Primeiro, você confere os números do slide contra o painel. Segundo, você me faz as perguntas mais chatas que conseguir."
    hide st_ceo
    with dissolve
    "{i}Você abre o painel no celular e vai slide por slide.{/i}"
    "{i}Cadastros: mais de três mil, depois de hoje. Bate. Estudantes que fecharam o mês com o total conferido: 312. Bate.{/i}"
    "{i}Retenção semanal: no slide, 75 por cento. No painel, 57.{/i}"
    show st_ceo serious at center_zoom
    with dissolve
    st_ceo "Não. Não, não, não. Eu inverti os dígitos?"
    st_ceo "Imagina eu falando 75 no palco e alguém da primeira fila abrindo o nosso painel. Fim de carreira!"
    show st_ceo neutral
    "{i}Ele corrige o slide na hora. Depois, você faz as perguntas chatas: de onde vem o número, quantas pessoas são, o que acontece se a internet cair na demo.{/i}"
    "{i}No fim do ensaio, a mentora da aceleradora levanta a mão de novo.{/i}"
    "{i}\"Dos estudantes que entraram há um mês, quantos ainda usam?\"{/i}"
    if pista_tem("st_p_retencao"):
        st_ceo "Cinquenta e sete por cento voltam toda semana. A coorte dos calouros de hoje eu mostro em trinta dias."
        "{i}Uma frase, sem festa. A mentora acena e não pergunta mais nada.{/i}"
        st_ceo "Viu? Número primeiro. Treinei com o cronômetro, como a gente combinou."
    else:
        show st_ceo thinking
        st_ceo "Então, a gente teve a festa dos mil, depois os cadastros subiram muito, e hoje..."
        "{i}Você mostra o caderno com uma palavra escrita: \"número\". Ele para no meio da frase.{/i}"
        st_ceo "Cinquenta e sete por cento voltam toda semana."
        "{i}A mentora acena. Vinícius solta o ar devagar.{/i}"
        show st_ceo neutral
        st_ceo "Ela só pergunta isso, né? Sempre a mesma coisa. Então a resposta tem que estar pronta antes da pergunta."
    st_ceo "Valeu. Sem você, eu subia amanhã com um 75 no telão e um sorriso no rosto."
    if energia_cansaco():
        "{i}Você boceja no meio do aplauso de mentira. Vinícius ri.{/i}"
        st_ceo "Vai pra casa dormir! Amanhã eu preciso de você na plateia com a cabeça descansada, não de heroísmo."
    hide st_ceo
    with dissolve
    return

label im_startup_s8_conversar_st_ceo:
    "{i}Vinícius anda de um lado para o outro do palco vazio, falando sozinho.{/i}"
    show st_ceo thinking at center_zoom
    with dissolve
    st_ceo "Me ajuda com a frase de abertura? Eu mudo ela a cada dez minutos."
    st_ceo "Escuta essa."
    show st_ceo neutral
    st_ceo "\"Eu quase larguei a faculdade por falta de dinheiro.\""
    "{i}Ele faz uma pausa longa, olhando para a plateia vazia.{/i}"
    show st_ceo thinking
    st_ceo "...Muito dramático?"
    "{i}Você balança a cabeça.{/i}"
    show st_ceo neutral
    st_ceo "Não? Fica."
    st_ceo "Ontem eu tinha doze slides. Hoje tenho oito. Cada slide cortado me deixou mais calmo."
    st_ceo "É verdade, então não precisa enfeitar. A Tainá vive dizendo isso da Bia. Acho que vale pra mim também."
    st_ceo "Amanhã, quarto da fila. Minha mãe na primeira fila, filmando na vertical. Tô pronto. Tô pronto, né?"
    hide st_ceo
    with dissolve
    return
