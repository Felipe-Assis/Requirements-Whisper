# mentoria.rpy
# Arco de mentoria da rota Startup: Clube das Testers, com a Lorena, a Bia e
# duas colegas de república dela. Fonte: docs/design/intermissoes-startup.md,
# seção 6. Labels im_startup_mentoria_<k> (k = 1..5), chamados pelo motor em
# qualquer semana a partir de semana_min; o encontro acontece onde a Lorena
# estiver (terraço na semana 6, bandejão nas outras). O motor aplica a
# amizade, a pista do encontro 3 (até a semana 5) e a conquista do encontro 5.

# NPCs do arco: sem sprite, sem contato.
define st_npc_joana = Character(_("Joana"), color="#C9A0FF")
define st_npc_rayane = Character(_("Rayane"), color="#FFB870")
define st_npc_italo = Character(_("Ítalo"), color="#9FD3C7")


# ---------------- 1. Apresentar o beta ao clube ----------------

label im_startup_mentoria_1:
    if im_op["poi"] == "terraco":
        "{i}No terraço, Lorena espera com o caderno aberto. Bia sobe do café com duas amigas e o notebook debaixo do braço.{/i}"
    else:
        "{i}No bandejão, Lorena juntou duas mesas perto da janela. Bia chega com duas amigas da república e três copos de suco.{/i}"
    show st_qualidade neutral at left_zoom
    show st_estudante neutral at right_zoom
    with dissolve
    st_estudante "Gente, essa é a Lorena, da Trocado. E [player_name], que trabalha com ela. Lorena, essas são a Joana e a Rayane."
    st_npc_joana "Oi. Joana, Letras. Tenho baixa visão, então uso leitor de tela e fonte gigante."
    st_npc_joana "Já aviso: o leitor de tela não tem paciência. Nem eu."
    st_npc_rayane "Rayane, Educação Física. Faço entrega de bicicleta no sábado. Celular de 2018, tela trincada, e o plano acaba todo dia 20."
    st_qualidade "Oxe, perfeito. Vocês usam o celular de jeitos que ninguém na mesa da Trocado usa."
    st_qualidade "Primeiro, o combinado: um teste curto toda semana, uns vinte minutos. Vocês usam o app, a gente observa."
    st_qualidade "Segundo: antes de cada teste, um termo simples. Diz o que a gente observa, que só a tela é gravada, nunca o rosto, e que os gastos são de mentira."
    st_qualidade "Terceiro: dá pra parar quando quiser, sem explicar por quê."
    st_npc_rayane "Tem camisa?"
    st_qualidade "...Não tem camisa."
    st_npc_rayane "Ainda."
    "{i}Cada uma conta como usa o celular. Joana faz tudo pelo ouvido, com a tela quase apagada para poupar bateria. Rayane só usa internet no Wi-Fi depois do dia 20. Bia lança tudo, até o cafezinho.{/i}"
    show st_qualidade thinking
    st_qualidade "Viu, [player_name]? Três aparelhos, três jeitos de ter internet, um leitor de tela. Gente diferente acha problema diferente."
    st_qualidade "Agora a regra de ouro. Essa é pra você."
    st_qualidade "Durante o teste, a gente não ajuda. Se alguém travar, você anota onde travou. Não aponta o botão."
    st_npc_joana "Nem se eu xingar o app?"
    st_qualidade "Principalmente se você xingar o app. Xingamento é dado."
    show st_estudante thinking
    st_estudante "Égua, isso precisa de um nome. Tipo assim: Clube das Testers."
    st_npc_rayane "Clube precisa de camisa."
    st_estudante "E a Joana acha erro até em placa de ônibus. Imagina em app."
    show st_qualidade neutral
    show st_estudante neutral
    st_qualidade "Clube das Testers, então. Sem camisa. O primeiro teste é no próximo encontro."
    if energia_cansaco():
        st_qualidade "E você, [player_name], toma um suco antes de ir. Observar cansa mais do que parece."
    "{i}Rayane já está desenhando uma camisa no guardanapo.{/i}"
    hide st_qualidade
    hide st_estudante
    with dissolve
    return


# ---------------- 2. Cinco tarefas cronometradas ----------------

label im_startup_mentoria_2:
    if im_op["poi"] == "terraco":
        "{i}As três sobem do café para o terraço com o notebook da Bia debaixo do braço. Lorena já arrumou três cadeiras em fila.{/i}"
    else:
        "{i}No bandejão, o clube ocupa a mesa da janela de novo. Joana, Rayane e Bia, cada uma com o próprio celular.{/i}"
    show st_qualidade neutral at left_zoom
    with dissolve
    st_qualidade "Hoje o cronômetro é seu, [player_name]. Cinco tarefas, uma pessoa de cada vez. Eu leio, você marca o tempo e anota onde travou."
    st_qualidade "E elas pensam em voz alta. Tudo que passar pela cabeça, falado."
    "{i}Tarefa 1: lançar o bandejão de R$ 4,50. As três conseguem. Rayane é a mais rápida: doze segundos.{/i}"
    "{i}Tarefa 2: dizer o total do mês. As três conseguem.{/i}"
    "{i}Tarefa 3: achar o gasto de ontem. As três conseguem. Joana ouve a lista inteira pelo leitor de tela e acha antes da Bia.{/i}"
    if im_semana_atual <= 5:
        "{i}Tarefa 4: apagar um gasto lançado errado. Ninguém consegue: no beta ainda não existe. E as três fazem a mesma coisa: tentam arrastar o gasto para o lado.{/i}"
    else:
        "{i}Tarefa 4: apagar um gasto lançado errado, na versão nova. As três conseguem, mas todas tentam primeiro arrastar o gasto para o lado. A lixeira fica dentro do gasto.{/i}"
    "{i}No meio da tarefa, Rayane para, aponta a tela e olha para você.{/i}"
    st_npc_rayane "É aqui?"
    menu (tipo="conversa"):
        "\"O que você acha?\"":
            st_npc_rayane "Acho que é arrastando. Tô arrastando... não vai."
            st_qualidade "(baixinho) Isso. Devolver a pergunta. A tarefa é dela."
        "Apontar o lugar certo na tela":
            st_npc_rayane "Ah, tá. Pronto."
            show st_qualidade serious
            st_qualidade "(baixinho) Oxe. Agora a gente nunca vai saber se ela acharia sem ajuda."
            st_qualidade "Tudo bem, acontece com todo mundo. Anota \"precisou de ajuda\". Da próxima vez, devolve: \"o que você acha?\""
            show st_qualidade neutral
    "{i}Tarefa 5: ligar o modo avião, lançar um gasto e dizer se salvou. As três lançam. Nenhuma sabe dizer se salvou.{/i}"
    st_npc_joana "O leitor disse \"salvo\". Salvo onde? No celular? No servidor? No além?"
    show st_qualidade thinking
    st_qualidade "Agora o relato. Nada de \"foi confuso\". Com número."
    if im_semana_atual <= 5:
        "{i}Você escreve: \"Tarefa 4: 0 de 3 conseguiram apagar; 3 de 3 tentaram arrastar. Tarefa 5: 0 de 3 souberam dizer se salvou.\"{/i}"
    else:
        "{i}Você escreve: \"Tarefa 4: 3 de 3 conseguiram apagar; 3 de 3 tentaram arrastar antes. Tarefa 5: 0 de 3 souberam dizer se salvou.\"{/i}"
    show st_qualidade neutral
    st_qualidade "Cadê a evidência? Tá aqui: três de três."
    st_qualidade "Repara que ninguém disse que o app é ruim. Elas mostraram onde ele não fala a língua delas."
    st_npc_rayane "Isso conta como camisa?"
    st_qualidade "Conta como relatório. É melhor que camisa."
    hide st_qualidade
    with dissolve
    return


# ---------------- 3. O leitor de tela da Joana ----------------

label im_startup_mentoria_3:
    if im_op["poi"] == "terraco":
        "{i}As três sobem do café para o terraço com o notebook da Bia debaixo do braço. Joana senta no lugar mais perto da tomada.{/i}"
    else:
        "{i}No bandejão, Joana escolhe a mesa mais longe da caixa de som. Hoje o teste é dela.{/i}"
    show st_qualidade neutral at left_zoom
    with dissolve
    st_npc_joana "Hoje eu mostro como eu uso. Vocês só escutam. Aviso logo: eu ouço no dobro da velocidade."
    "{i}Ela liga o leitor de tela. A voz sai tão rápida que você entende uma palavra em cada três.{/i}"
    st_npc_joana "Se for na velocidade normal, eu durmo."
    "{i}Ela abre o Trocado. O leitor fala o total do mês certinho, com reais e centavos. Depois passa pelo ícone de categoria do primeiro gasto e diz só: \"imagem\".{/i}"
    st_npc_joana "Imagem de quê? Se é a categoria, diz a categoria. Alimentação. Transporte. Não é segredo."
    if im_semana_atual <= 5:
        "{i}Depois ela abre o protótipo da confirmação do Davi, instalado como versão de teste. Passa o dedo até a lixeira.{/i}"
        "{i}O leitor diz: \"botão\".{/i}"
        st_npc_joana "Botão. Botão do quê? Eu vou apagar qual gasto? O almoço? A conta inteira?"
        st_npc_joana "Eu não preciso de app especial. Preciso que o botão diga o nome."
        show st_qualidade thinking
        if im_semana_atual <= 4:
            st_qualidade "Anotado. Isso vai pra definição de pronto: nenhum botão sai sem nome que o leitor fale. Na semana que vem eu levo pra equipe."
        else:
            st_qualidade "Anotado. Hoje cedo eu levei isso pra definição de pronto. Agora tenho a prova, com a sua voz."
    else:
        "{i}Depois ela abre a versão nova. Passa o dedo até a lixeira.{/i}"
        "{i}O leitor diz: \"Excluir Almoço, R$ 20, botão\".{/i}"
        st_npc_joana "Viu? Quando o botão diz o nome, eu nem lembro que existe leitor de tela."
        st_npc_joana "Eu não preciso de app especial. Preciso que o botão diga o nome. Esse aprendeu. O ícone da categoria, ainda não."
        show st_qualidade thinking
        st_qualidade "Anotado pra próxima versão: a categoria com nome, igual à lixeira."
    st_qualidade "Primeiro: o rótulo diz a ação e o objeto. \"Excluir Almoço, R$ 20\", não \"lixeira\"."
    st_qualidade "Segundo: nada só por ícone, nada só por cor. Terceiro: botão grande, que dá pra acertar com o polegar no ônibus."
    st_qualidade "Quarto: a ordem de leitura segue a ordem da tela. Se o leitor pula do topo para o rodapé, a pessoa se perde."
    st_npc_joana "E quinto: testa com quem usa. Simulador não pega ônibus lotado."
    show st_qualidade neutral
    st_qualidade "Oxe, o quinto é o melhor. Vou roubar."
    if energia_cansaco():
        "{i}Você fecha os olhos por um segundo e só escuta o leitor. Dá para entender mais do que parecia.{/i}"
    hide st_qualidade
    with dissolve
    return


# ---------------- 4. Calouros e o pico ----------------

label im_startup_mentoria_4:
    if im_op["poi"] == "terraco":
        "{i}O clube sobe do café para o terraço com uma pessoa a mais: um rapaz de camisa de time do interior, olhando a vista como se fosse um mapa.{/i}"
    else:
        "{i}No bandejão, o clube chega com uma pessoa a mais: um rapaz de camisa de time do interior, segurando a bandeja com as duas mãos.{/i}"
    show st_qualidade neutral at left_zoom
    show st_estudante neutral at right_zoom
    with dissolve
    st_npc_rayane "Gente, esse é o Ítalo, meu primo. Veio do interior pra matrícula de Engenharia. Nunca usou app de finanças."
    st_npc_italo "Eu anoto num caderno. Quando lembro."
    st_qualidade "Perfeito. As mesmas cinco tarefas. Primeiro uso é outro teste."
    "{i}Tarefa 1: lançar o bandejão. Ítalo encara o botão de mais por vinte segundos antes de tocar.{/i}"
    st_npc_italo "Achei que o mais era pra pôr dinheiro. Tipo depósito."
    "{i}Tarefa 2: dizer o total do mês. Ítalo passa o dedo pela tela inteira, duas vezes.{/i}"
    st_npc_italo "Total do mês? Total de quê? Cadê o saldo?"
    "{i}Rayane abre a boca para ajudar. Lorena levanta um dedo, e ela fecha.{/i}"
    show st_qualidade thinking
    st_qualidade "A gente reescreve a tarefa com as palavras dele. Ítalo: quanto você já gastou neste mês?"
    "{i}Ele acha em cinco segundos.{/i}"
    st_qualidade "A gente escreveu a tarefa com as nossas palavras. Quem chega não conhece as nossas palavras."
    st_npc_rayane "E ele achou três problemas que a gente nem vê mais."
    st_qualidade "Com cinco pessoas você já vê a maioria dos problemas. Não precisa de cem. Precisa de gente diferente."
    show st_estudante thinking
    if im_semana_atual >= 8:
        st_estudante "E hoje foi o primeiro dia de aula. Vocês viram? O bandejão abriu às 11h30 e a fila foi até a escada."
        st_npc_rayane "Todo mundo lançou o almoço no mesmo minuto. Eu vi três celulares do meu lado com o Trocado aberto."
    else:
        st_estudante "Agora imagina o primeiro dia de aula. O bandejão abre às 11h30 e a fila vai até a escada."
        st_npc_rayane "E todo mundo lança o almoço no mesmo minuto, na saída do caixa. Eu faço isso. Todo mundo faz."
    st_npc_italo "Eu vou fazer também, então. Agora que eu sei onde fica o \"quanto gastei\"."
    show st_qualidade neutral
    st_qualidade "Anota, [player_name]: comportamento coletivo. Mil pessoas fazendo a mesma coisa ao mesmo tempo."
    st_qualidade "Uso de verdade tem horário. Teste que ignora o horário testa um app que ninguém usa."
    show st_estudante neutral
    st_npc_italo "Posso voltar no próximo? Gostei de errar de propósito."
    st_npc_rayane "Ele quer a camisa."
    hide st_qualidade
    hide st_estudante
    with dissolve
    return


# ---------------- 5. O primeiro relato de bug do clube ----------------

label im_startup_mentoria_5:
    if im_op["poi"] == "terraco":
        "{i}As três sobem do café para o terraço com o notebook da Bia debaixo do braço. Rayane vem na frente, com o celular trincado na mão.{/i}"
    else:
        "{i}No bandejão, Rayane chega antes de todo mundo, com o celular trincado na mão e cara de quem tem uma denúncia.{/i}"
    show st_qualidade neutral at left_zoom
    show st_estudante neutral at right_zoom
    with dissolve
    st_npc_rayane "Mandei no grupo do clube agora há pouco: \"o app bugou\"."
    st_qualidade "Oxe. Bugou como?"
    st_npc_rayane "Bugou, ué. Bugou bugado."
    show st_qualidade thinking
    st_qualidade "[player_name], mostra pra ela a receita."
    "{i}Você escreve no guardanapo, uma linha por item: o que fez, o que aconteceu, o que esperava, os passos, o aparelho, a versão do app, se acontece sempre, e um print sem dado real.{/i}"
    st_qualidade "Primeiro, o que você fez. Segundo, o que aconteceu. Terceiro, o que esperava. O resto ajuda o Davi a chegar no mesmo lugar."
    "{i}Rayane reescreve, devagar, apagando duas vezes.{/i}"
    st_npc_rayane "\"Celular de 2018, teclado sem vírgula. Digitei 4.50 no bandejão. Salvou R$ 450,00. Esperava R$ 4,50. Acontece sempre que uso ponto.\""
    st_estudante "Égua. Tá melhor que os relatórios da minha monitoria."
    show st_qualidade neutral
    st_qualidade "Agora o Davi consegue repetir sem te ligar. É isso que faz um relato servir: quem não estava lá chega no mesmo lugar."
    "{i}Rayane manda no grupo. Cinco minutos depois, o celular da Lorena vibra.{/i}"
    hide st_estudante
    show st_mobile portrait at center_zoom
    with dissolve
    st_mobile "(mensagem) Pô, reproduzi de primeira! Teclado sem vírgula, o ponto vira separador de milhar. 4.50 vira 450,00."
    st_mobile "(mensagem) Vai pra fila com prioridade. E se a Bia digitou 4.5, virou 45: acho que isso explica aquele R$ 45 dela na inspeção. Valeu, clube!"
    hide st_mobile
    show st_estudante neutral at right_zoom
    with dissolve
    show st_qualidade neutral
    st_qualidade "Viu? Bug com passo a passo é bug pela metade."
    st_npc_rayane "Eu achei um bug. Eu. Com um celular de 2018."
    st_npc_joana "Achou porque seu celular é de 2018. É uma qualidade, não um defeito."
    "{i}Lorena tira da bolsa o caderninho de frases das avaliações, gasto nas pontas, e põe na frente da Bia.{/i}"
    st_qualidade "Bia, a partir de hoje quem coordena o clube é você."
    show st_estudante thinking
    st_estudante "Eu? Tipo assim... eu?"
    st_qualidade "Primeiro: vocês acham o que eu não acho. Segundo: vocês sabem relatar. Terceiro: eu vou continuar aparecendo, que eu gosto do suco."
    show st_estudante neutral
    st_estudante "Então eu cuido do caderno. E a Rayane cuida da camisa."
    st_npc_rayane "FINALMENTE."
    "{i}Você olha para a mesa: um guardanapo com uma receita de relato, um caderno passando de mão e três pessoas que agora testam sem precisar de ninguém da Trocado do lado.{/i}"
    hide st_qualidade
    hide st_estudante
    with dissolve
    return
