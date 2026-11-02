# st_12_casa_sem3.rpy
# Rota Startup, semana 3, sexta, 20h30 a 22h30. Fonte: docs/rotas/startup.md (st_12).
# Retorno para casa: releitura do rascunho ou retomada da escrita da st_11.

label st_12_casa_sem3:
    $ set_available("all")
    $ set_time(20, 30)

    play music music_streets_focused fadein 1.0
    scene bg transito_noite
    with fade

    "{i}Sexta à noite. O ônibus anda devagar pela praia de Botafogo, e as luzes dos prédios tremem no vidro.{/i}"
    "{i}Uma frase da Lorena não sai da cabeça: \"dá para testar e passar com o total errado\".{/i}"
    "{i}Um requisito pode parecer certo, passar no teste e ainda assim deixar a Bia achando que perdeu dinheiro. Tudo depende do que está escrito.{/i}"
    "{i}Quando o ônibus entra no túnel, você nem tenta lançar a passagem. Melhor esperar o sinal voltar. A Bia faz isso há meses.{/i}"
    $ advance_minutes(40)

    play music music_home_reflecting fadein 1.5
    scene bg quarto_noite
    with fade
    $ advance_minutes(15)

    "{i}Em casa, você larga a mochila na cadeira e abre a especificação no notebook. Dois requisitos corrigidos, um bloqueado esperando o Otávio, dois critérios com valores.{/i}"
    "{i}Na disciplina, inspeção parecia burocracia: uma lista de defeitos para decorar antes da prova.{/i}"
    "{i}Na Trocado, cada defeito tinha um rosto. O \"muito\" do alerta era a bolsa da Bia. O RF05 incompleto era o almoço que sumia sem confirmar.{/i}"

    if st_escrita_concluida:
        "{i}No fim do documento está o seu rascunho, do jeito que ficou na quarta. Você relê devagar.{/i}"
        "Seu requisito:"
        $ narrator(st_escrita_requisito)
        "Seu critério de aceitação:"
        $ narrator(st_escrita_criterio)
        "{i}Uma dúvida aparece: e se a Bia corrigir um gasto de um mês que já fechou? O total daquele mês muda também, ou só o do mês atual?{/i}"
        "{i}Você anota a pergunta para levar à Bia na segunda. Melhor perguntar do que adivinhar.{/i}"
    else:
        "{i}No fim do documento, o pedido da Bia continua esperando: corrigir o valor de um gasto. O exercício ficou pendente.{/i}"
        menu (tipo="trabalho"):
            "Retomar o rascunho agora?"
            "Retomar o rascunho agora":
                call exercicio_escrita(ST_ESCRITA_ID, ST_ESCRITA_PEDIDO) from _st_12_exercicio_escrita
                $ st_sincronizar_escrita()
                if st_escrita_concluida:
                    "{i}Pronto. Com calma e sem ninguém olhando, as frases saíram mais fáceis do que na quarta.{/i}"
                    "{i}Uma dúvida fica: e se a Bia corrigir um gasto de um mês que já fechou? Você anota para perguntar na segunda.{/i}"
                else:
                    "{i}Ainda não fechou, mas o rascunho está mais perto. Segunda você mostra para a Tainá do jeito que está.{/i}"
            "Deixar para depois":
                "{i}Hoje não. O pedido continua guardado no notebook, e a semana foi longa.{/i}"

    $ st_checar_conquistas()
    $ advance_minutes(30)

    play sound "audio/effects/cell_vibration.ogg"
    show st_qualidade portrait at left_zoom
    with dissolve
    st_qualidade "(mensagem no grupo) Colei o checklist no monitor. Primeiro: falta algo? Segundo: dá para entender de dois jeitos? Terceiro: contradiz outra regra? Quarto: dá para testar?"
    st_qualidade "(mensagem no grupo) Segunda ninguém escapa. Bom fim de semana, gente!"
    hide st_qualidade
    with dissolve
    $ add_friendship_point("st_qualidade", 1)

    "{i}Embaixo da foto, Davi responde com um emoji de lupa, e Tainá com um coração coral.{/i}"
    "Semana que vem começa a arquitetura. Talvez valha falar com alguém antes."

    call screen contacts_screen

    play music music_home_dreamy fadein 1.0
    scene black
    with fade
    $ set_time(22, 30)
    window hide
    pause 1.1
    window show

    "{i}Fim da Semana 3\n\nRequisito bom tem quem, condição e resultado. Inspecionar antes de codar custa uma tarde; depois, custa um lançamento.{/i}"

    return
