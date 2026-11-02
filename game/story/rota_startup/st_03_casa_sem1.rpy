label st_03_casa_sem1:
    # Fora do coworking: a equipe toda pode receber mensagem.
    $ set_available("all")
    $ set_time(19, 30)

    play music music_streets_focused fadein 1.5
    scene bg transito_noite
    with fade

    "{i}Sexta-feira, sete e meia da noite. O ônibus de volta está cheio, mas você consegue um lugar na janela.{/i}"
    "{i}No colo, um pacote de biscoito comprado na saída do coworking: R$ 7. Hora de cumprir o combinado com a Tainá e lançar tudo no beta.{/i}"
    $ advance_minutes(10)
    "{i}Você abre o Trocado, toca no mais, digita 7,00, escolhe Lanche e toca em Salvar.{/i}"
    play sound "audio/effects/bus.ogg"
    "{i}O ônibus entra no túnel. A tela congela, com a rodinha girando.{/i}"
    "{i}Cinco segundos. Dez. Nada. Você toca em Salvar de novo.{/i}"
    stop sound fadeout 1.0
    "{i}Na saída do túnel, o sinal volta e a lista se atualiza.{/i}"
    "{i}Lanche, R$ 7,00. Logo abaixo, de novo: Lanche, R$ 7,00. O total do mês subiu R$ 14.{/i}"
    "{i}Você tenta apagar o segundo. Arrasta para o lado, segura o dedo em cima, abre o item. Não existe opção de excluir.{/i}"
    "{i}É a avaliação que a Lorena leu na segunda: “lancei o almoço duas vezes e não consigo apagar”. Só que agora o lanche é seu.{/i}"
    $ st_viu_duplicado = True
    "{i}Antes que esqueça, você anota no celular: “Sexta, 19h40, dentro do túnel. Sem sinal, toquei Salvar duas vezes. Lanche duplicado, total R$ 14 a mais.”{/i}"
    $ advance_minutes(30)

    play music music_home_reflecting fadein 2.0
    scene bg quarto_noite
    with fade
    $ advance_minutes(20)

    "{i}Em casa, você larga a mochila na cadeira e abre o notebook para revisar a semana.{/i}"
    show item notebook_fechado as notebook at center_zoom
    with dissolve
    pause 0.5
    "• Ciclo de vida inteiro, em voltas de uma semana: descobrir, especificar, construir, testar, lançar, medir.\n• MVP: pequeno no escopo, não na qualidade."
    "• Quadro Kanban: no máximo duas tarefas em andamento por pessoa.\n• O desafio: versão 1.0 nas lojas em oito semanas, antes do semestre, e o demo day na mesma semana."
    "{i}Embaixo, você cola a anotação do ônibus. Tem horário, lugar e o que você fez. Do jeito que a Tainá pediu.{/i}"
    hide notebook
    with dissolve
    $ advance_minutes(15)

    play sound "audio/effects/cell_vibration.ogg"
    show st_mentora portrait at left_zoom
    with dissolve
    st_mentora "(mensagem) Oi, [player_name]! Primeira semana fechada. Segunda de manhã a gente prepara a entrevista com a Bia, uma estudante que usa o beta desde o começo, e com o Vinícius."
    "{i}Você responde contando o lanche duplicado no túnel, com o horário anotado.{/i}"
    st_mentora "(mensagem) Sério? Então você já sentiu na pele o que a gente leu nas avaliações. Guarda essa anotação, segunda ela vai ser útil. Bom descanso!"
    $ add_friendship_point("st_mentora", 1)
    hide st_mentora
    with dissolve
    $ advance_minutes(5)

    "Tem mais gente da equipe online. Talvez valha mandar uma mensagem para alguém."

    call screen contacts_screen

    scene bg cozinha_noite
    with dissolve
    $ advance_minutes(25)
    "{i}Na cozinha, o colega de república esquenta a janta e olha o celular ao mesmo tempo.{/i}"
    show npc_roommate neutral at right_zoom
    with dissolve
    npc_roommate "E aí, [player_name]! Sobreviveu à primeira semana na startup?"
    "{i}Você conta do app e do lanche que apareceu duas vezes.{/i}"
    npc_roommate "Por isso eu controlo tudo numa planilha. App nenhum acerta. Na planilha, se der errado, pelo menos o erro é meu."
    "{i}Ele mostra a planilha: uma aba por mês, cores para cada categoria e uma fórmula só para dividir o aluguel da república.{/i}"
    "{i}Você pensa nos 800 estudantes do beta. Quantos deles mantêm uma planilha escondida porque não confiam no total?{/i}"
    hide npc_roommate
    with dissolve
    $ advance_minutes(45)

    stop music fadeout 1.5
    scene black
    with fade
    window hide
    pause 1.0
    window show

    "{i}Fim da Semana 1\n\nUm MVP é pequeno no escopo, não na qualidade. E o problema dos estudantes acabou de acontecer com você.{/i}"

    return
