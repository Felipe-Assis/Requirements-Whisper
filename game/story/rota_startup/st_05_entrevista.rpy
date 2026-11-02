# st_05_entrevista.rpy
# Rota Startup, semana 2, segunda, 14h00 a 15h30. Bíblia: docs/rotas/startup.md (st_05).

label st_05_entrevista:
    $ set_available("st_techlead", "st_mobile", "st_qualidade")
    $ set_time(14, 0)

    play music music_office_relaxed fadein 1.0
    scene bg sala_reunioes_tarde
    with fade

    "{i}O aquário do coworking pega o sol da tarde. Na mesa, um copo de água para cada um, o roteiro impresso e o caderno laranja de [NOME_ST_MENTORA].{/i}"

    show st_mentora neutral at left_zoom
    with dissolve
    st_mentora "Lembra: a gente pergunta mais e fala menos. Se der silêncio, deixa o silêncio trabalhar."

    $ advance_minutes(5)
    play sound "audio/effects/abrindo_porta.ogg"
    show st_estudante thinking at right_zoom
    with dissolve
    "{i}Uma estudante entra ainda de mochila, com uma garrafa d'água presa na lateral e um chaveiro de boto-cor-de-rosa balançando.{/i}"
    st_estudante "Oi, gente. Desculpa a correria, saí agora da aula de Cálculo. Tenho até umas três e meia."
    st_mentora "Imagina, [NOME_ST_ESTUDANTE]! Obrigada por vir. [player_name] chegou na equipe semana passada e vai conduzir a conversa comigo."
    st_estudante "Prazer. Já aviso: eu sou chata com esse app. Uso todo dia."
    st_mentora "Melhor ainda. É de gente assim que a gente precisa."

    show st_ceo neutral at center_zoom
    with dissolve
    "{i}[NOME_ST_CEO] entra logo atrás, terminando uma ligação no fone sem fio.{/i}"
    st_ceo "Fechado, falamos quinta! ... Pronto, desculpa. Fundo de investimento não dorme."
    st_ceo "Olha, vou direto: precisamos de um jeito fácil de controlar os gastos. E que impressione no demo day!"

    $ advance_minutes(5)
    "{i}[NOME_ST_MENTORA] olha para você e faz um sinal discreto com a cabeça. A primeira pergunta é sua.{/i}"

    menu:
        "Como você começa?"

        "[NOME_ST_ESTUDANTE], você pode contar a última vez em que o app te atrapalhou?":
            $ st_decidir("st_d05_episodio", True)
            $ add_friendship_point("st_estudante", 1)
            st_estudante "Posso. Foi semana passada, inclusive."

        "Qual funcionalidade você mais quer: modo escuro ou medalhas?":
            $ st_decidir("st_d05_episodio", False)
            st_estudante "Hum... modo escuro, acho?"
            show st_mentora serious at left_zoom
            st_mentora "(baixinho) Essa pergunta oferece duas soluções prontas. A [NOME_ST_ESTUDANTE] escolhe uma e a gente não descobre o que dói."
            menu:
                "Como você reformula?"
                "[NOME_ST_ESTUDANTE], me conta a última vez em que isso aconteceu?":
                    st_estudante "Ah, isso eu conto. Foi semana passada."

        "Você usaria mais se a tela tivesse menos botões?":
            $ st_decidir("st_d05_episodio", False)
            st_estudante "Acho que sim, né?"
            show st_mentora serious at left_zoom
            st_mentora "(baixinho) Ela pode dizer sim por educação. Menos botões é uma hipótese nossa, não um relato dela."
            menu:
                "Como você reformula?"
                "[NOME_ST_ESTUDANTE], me conta a última vez em que isso aconteceu?":
                    st_estudante "Tá. Então deixa eu contar o que aconteceu semana passada."

    $ advance_minutes(10)
    show st_estudante neutral at right_zoom
    st_estudante "Tipo assim: eu estava no ônibus, voltando do campus. Lancei o almoço, R$ 20, que foi o prato feito do restaurante perto do bloco."
    st_estudante "A internet caiu. Ficou aquela rodinha girando. Eu toquei em Salvar de novo."
    st_estudante "Quando o sinal voltou, o almoço estava lá duas vezes. O total ficou R$ 20 acima."
    show st_estudante thinking at right_zoom
    st_estudante "Égua, eu achei que tinha perdido dinheiro. Fui procurar como apagar e não achei. Desinstalei e fiquei três dias sem usar."

    show st_mentora neutral at left_zoom
    st_mentora "(baixinho) Agora a gente sabe quem, o quê e qual consequência."
    "{i}O ônibus, o sinal caindo, o toque repetido. É a mesma história do seu lanche de sexta.{/i}"

    st_estudante "Se fosse fácil, isso não acontecia."

    menu:
        "O que fazer com \"fácil\"?"

        "Pergunto o que ela precisa conseguir fazer naquela situação.":
            $ st_decidir("st_d05_ambiguidade", True)
            st_estudante "Naquela hora? Apagar o almoço repetido, sem medo de apagar o certo. E ver o total voltar ao normal."
            show st_mentora neutral at left_zoom
            st_mentora "Isso já dá para escrever e para testar. \"Fácil\" sozinho, não."

        "Anoto \"o app deve ser fácil\" e deixo o time decidir.":
            $ st_decidir("st_d05_ambiguidade", False)
            show st_mentora serious at left_zoom
            st_mentora "(baixinho) [NOME_ST_MOBILE] vai entender uma coisa, [NOME_ST_QUALIDADE] outra e a [NOME_ST_ESTUDANTE] uma terceira. Ninguém consegue testar \"fácil\"."
            menu:
                "Como você pergunta de novo?"
                "O que precisa acontecer para o problema que você contou não se repetir?":
                    st_estudante "Eu preciso conseguir apagar o gasto que lancei errado. Com uma pergunta antes, para não apagar o certo sem querer. E o total tem que mudar na hora."
                    show st_mentora thinking at left_zoom
                    st_mentora "Boa. Essa regra resolve uma parte. Se o botão vai ser fácil de achar, a gente só confirma vendo gente de verdade usando."

        "Troco por \"moderno e intuitivo\", que soa mais profissional.":
            $ st_decidir("st_d05_ambiguidade", False)
            show st_mentora serious at left_zoom
            st_mentora "(baixinho) Trocou um adjetivo por dois. O resultado esperado continua sem nome."
            menu:
                "Como você pergunta de novo?"
                "O que precisa acontecer para o problema que você contou não se repetir?":
                    st_estudante "Eu preciso conseguir apagar o gasto que lancei errado. Com uma pergunta antes, para não apagar o certo sem querer. E o total tem que mudar na hora."
                    show st_mentora thinking at left_zoom
                    st_mentora "Boa. Essa regra resolve uma parte. Se o botão vai ser fácil de achar, a gente só confirma vendo gente de verdade usando."

    $ advance_minutes(15)
    "{i}Você escreve a regra no roteiro e lê em voz alta para conferir:{/i}"
    "\"A pessoa pode excluir um gasto lançado por engano, com uma confirmação antes, e vê o total do mês atualizado.\""
    show st_estudante neutral at right_zoom
    st_estudante "É isso. Simples assim."

    show st_ceo thinking at center_zoom
    st_ceo "Concordo que tem que funcionar. Mas, pra mim, fácil de verdade é nem precisar lançar nada!"
    st_ceo "A gente importa os gastos direto do banco, via Open Finance. E coloca medalhas para engajar. Investidor ama engajamento."
    show st_estudante thinking at right_zoom
    st_estudante "Com todo respeito, eu não dou acesso ao meu banco para um app que erra o total."
    st_estudante "E medalha não paga almoço."
    st_ceo "Mas pensa na praticidade..."

    "{i}Os dois olham para você. [NOME_ST_MENTORA] não diz nada, mas o caderno dela está aberto numa página com uma palavra circulada: \"objetivo\".{/i}"

    menu:
        "Como você conduz a discordância?"

        "Pergunto a cada um que resultado espera e proponho decidir pelo objetivo comum: estudantes que confiam no total e voltam a usar.":
            $ st_decidir("st_d05_conflito", True)
            $ add_friendship_point("st_ceo", 1)
            $ add_friendship_point("st_estudante", 1)

        "Fico com o [NOME_ST_CEO]: ele decide o que vai para o demo day.":
            $ st_decidir("st_d05_conflito", False)
            $ add_friendship_point("st_ceo", 1)
            st_estudante "..."
            show st_mentora serious at left_zoom
            st_mentora "Espera. Se a [NOME_ST_ESTUDANTE] sai daqui sem ser ouvida, os 800 do beta continuam desinstalando. E a métrica do [NOME_ST_CEO] cai junto."
            menu:
                "Como você recomeça?"
                "Peço que cada um diga o que quer ver acontecer e procuro o que os dois têm em comum.":
                    $ add_friendship_point("st_estudante", 1)

        "Fico com a [NOME_ST_ESTUDANTE] e descarto o Open Finance.":
            $ st_decidir("st_d05_conflito", False)
            $ add_friendship_point("st_estudante", 1)
            st_ceo "Descartar? Assim, sem conversar?"
            show st_mentora serious at left_zoom
            st_mentora "A vontade de não lançar tudo à mão é real, e o [NOME_ST_CEO] vai trazer o pedido de volta mais forte. Descartar não resolve."
            menu:
                "Como você recomeça?"
                "Peço que cada um diga o que quer ver acontecer e procuro o que os dois têm em comum.":
                    $ add_friendship_point("st_ceo", 1)

    $ advance_minutes(20)
    st_estudante "Eu quero abrir o app e confiar no número. Saber quanto sobra até a bolsa cair."
    st_ceo "Eu quero que os estudantes voltem. Que usem no segundo mês, no terceiro..."
    show st_mentora neutral at left_zoom
    st_mentora "Então os dois querem a mesma coisa: estudante que confia no total e volta a usar."
    show st_ceo neutral at center_zoom
    st_ceo "Retenção. É exatamente o que o fundo vai perguntar."
    show st_ceo thinking at center_zoom
    st_ceo "Vou abrir o jogo: a retenção de 30 dias está em 22%%. Era 40. É isso que me tira o sono."
    st_estudante "Égua. Então não sou só eu."

    "{i}Você registra as duas coisas no roteiro, uma embaixo da outra:{/i}"
    "Prioridade: total confiável, com exclusão segura do gasto lançado por engano.\nHipótese a investigar: importar gastos do banco, que depende do consentimento da pessoa."
    st_mentora "Ninguém perdeu nada aqui. Um pedido virou prioridade e o outro virou pergunta que a gente vai responder com calma."

    $ advance_minutes(25)
    show st_estudante neutral at right_zoom
    st_estudante "Preciso ir, que a monitoria começa às quatro. Mas olha, foi a primeira vez que alguém do app me perguntou o que aconteceu, e não o que eu queria."
    st_estudante "Anota meu número. Se precisar conferir alguma coisa, me chama."
    $ add_contact("st_estudante")
    show st_ceo neutral at center_zoom
    st_ceo "O meu também, [player_name]! Se eu estiver pedindo coisa demais, me fala com o impacto. Eu escuto."
    $ add_contact("st_ceo")

    hide st_estudante
    hide st_ceo
    with dissolve

    $ advance_minutes(10)
    st_mentora "Viu? Duas vozes, um app. Bora passar isso a limpo enquanto está fresco."
    hide st_mentora
    with dissolve

    "{i}Você relê o roteiro. Na margem, três anotações: pedir o episódio, trocar o adjetivo por tarefa e resultado, e procurar o objetivo comum quando as pessoas discordam.{/i}"
    $ registrar("st_reg_elicitacao")
    $ st_checar_conquistas()

    return
