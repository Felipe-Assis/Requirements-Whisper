# st_06_classificacao.rpy
# Rota Startup, semana 2, terça, 10h00 a 16h00. Bíblia: docs/rotas/startup.md (st_06).

label st_06_classificacao:
    $ set_available("st_techlead", "st_mobile", "st_ceo", "st_estudante")
    $ set_time(10, 0)

    play music music_office_focused fadein 1.0
    scene bg startup_coworking_manha
    with fade

    "{i}Terça de manhã. As anotações da entrevista viraram uma pilha de post-its amarelos, cada um com uma frase curta. A parede de vidro está limpa, esperando.{/i}"

    show st_mentora thinking at left_zoom
    with dissolve
    st_mentora "Bora organizar isso. Quatro colunas."
    "{i}[NOME_ST_MENTORA] escreve com caneta para vidro, em letra grande:{/i}"
    "Funcional · Não funcional · Restrição (lei, lojas, parceiros) · Ideia a validar"
    st_mentora "Funcional é o que o app faz. Não funcional é como ele faz: rapidez, segurança, acessibilidade. Restrição é regra que vem de fora e a gente não escolhe. E ideia a validar é aposta, ainda sem evidência."

    show st_qualidade neutral at right_zoom
    with dissolve
    st_qualidade "E tem um motivo prático para separar, [player_name]. Cada tipo vira um teste diferente."
    st_qualidade "Primeiro: funcional se testa executando. Segundo: não funcional se mede. Terceiro: restrição se confere com a regra externa. Quarto: ideia se valida com usuários."
    st_qualidade "Se o post-it vai para a coluna errada, a gente testa do jeito errado. E passa achando que está tudo certo."

    $ advance_minutes(20)
    "{i}[NOME_ST_MENTORA] te entrega o primeiro post-it.{/i}"
    "\"Excluir um gasto lançado por engano, com confirmação, e ver o total atualizado.\""

    menu:
        "Em qual coluna vai este post-it?"

        "Funcional: é um comportamento que o app executa.":
            $ st_decidir("st_d06_funcional", True)
            show st_qualidade neutral at right_zoom
            st_qualidade "Isso. Eu testo tocando em Excluir, confirmando e olhando a lista e o total."

        "Não funcional, porque é sobre a qualidade do total.":
            $ st_decidir("st_d06_funcional", False)
            show st_qualidade serious at right_zoom
            st_qualidade "Ele descreve uma ação e um resultado. Se fosse não funcional, eu mediria tempo ou carga, e não teria como testar a exclusão."
            menu:
                "O que você faz com o post-it?"
                "Coloco o post-it na coluna que permite testar do jeito certo.":
                    st_qualidade "Funcional, então. Aí o teste é executar: excluir, confirmar e conferir se o gasto saiu e o total mudou."

        "Ideia a validar.":
            $ st_decidir("st_d06_funcional", False)
            show st_mentora serious at left_zoom
            st_mentora "Já temos um episódio e nove avaliações. Isso é necessidade confirmada."
            menu:
                "O que você faz com o post-it?"
                "Coloco o post-it na coluna que permite testar do jeito certo.":
                    show st_qualidade neutral at right_zoom
                    st_qualidade "Funcional. Ideia a validar é para o que ninguém contou ainda. Esse a [NOME_ST_ESTUDANTE] contou com valor e tudo."

    $ advance_minutes(25)
    "{i}Segundo post-it, com a letra apressada de quem anotou durante a entrevista:{/i}"
    "\"A lista de gastos deve abrir rápido no 4G.\""

    menu:
        "Como você classifica?"

        "Não funcional, e precisa de número: abrir em até 2 segundos em 95%% das vezes, num celular de entrada com 4G.":
            $ st_decidir("st_d06_nao_funcional", True)
            show st_qualidade neutral at right_zoom
            st_qualidade "Oxe, já veio com a medida! Com isso eu monto o teste amanhã."

        "Funcional, porque fala da lista.":
            $ st_decidir("st_d06_nao_funcional", False)
            show st_qualidade serious at right_zoom
            st_qualidade "A lista existir é funcional. A velocidade é uma qualidade, e qualidade se mede."
            menu:
                "O que você faz com o post-it?"
                "Coloco o post-it na coluna que permite testar do jeito certo.":
                    st_qualidade "Não funcional. E escreve o número junto: até 2 segundos em 95%% das vezes, num celular de entrada com 4G. Sem número, não tem como medir."

        "Não funcional, e \"rápido\" já é suficiente.":
            $ st_decidir("st_d06_nao_funcional", False)
            show st_qualidade serious at right_zoom
            st_qualidade "[NOME_ST_MOBILE] vai achar rápido no celular dele, de topo de linha. A [NOME_ST_ESTUDANTE], com o celular de 2019, não."
            menu:
                "O que você faz com o post-it?"
                "Coloco o post-it na coluna que permite testar do jeito certo.":
                    st_qualidade "A coluna estava certa; faltava a medida. Até 2 segundos em 95%% das vezes, num celular de entrada com 4G. Agora dá para medir."

    $ advance_minutes(25)
    "{i}O terceiro post-it é o mais disputado da entrevista.{/i}"
    "\"Importar gastos do banco automaticamente.\""

    menu:
        "Onde ele entra?"

        "Ideia a validar, que depende de restrições: consentimento do Open Finance, parceiro autorizado e LGPD.":
            $ st_decidir("st_d06_ideia", True)
            show st_mentora neutral at left_zoom
            st_mentora "Exato. E a gente cola três post-its de restrição do lado, ligados por uma seta. Assim ninguém esquece do que essa ideia depende."

        "Funcional obrigatório da 1.0, porque o CEO pediu.":
            $ st_decidir("st_d06_ideia", False)
            show st_mentora serious at left_zoom
            st_mentora "Ninguém contou um episódio sobre isso ainda, e depende de um parceiro autorizado. Se virar obrigatório agora, ocupa o espaço da exclusão segura."
            menu:
                "O que você faz com o post-it?"
                "Coloco o post-it na coluna que permite testar do jeito certo.":
                    show st_qualidade neutral at right_zoom
                    st_qualidade "Ideia a validar, com as restrições do lado: consentimento do Open Finance, parceiro autorizado e LGPD. Ideia se testa conversando com estudante, não com código."

        "Descartar, porque a [NOME_ST_ESTUDANTE] não quer.":
            $ st_decidir("st_d06_ideia", False)
            show st_mentora serious at left_zoom
            st_mentora "A [NOME_ST_ESTUDANTE] não quer agora, com o total errado. A vontade de digitar menos aparece em seis avaliações. Fica como hipótese."
            menu:
                "O que você faz com o post-it?"
                "Coloco o post-it na coluna que permite testar do jeito certo.":
                    show st_qualidade neutral at right_zoom
                    st_qualidade "Ideia a validar, com as restrições do lado: consentimento do Open Finance, parceiro autorizado e LGPD. Fica na parede até a gente ter evidência para um lado ou para o outro."

    $ st_classif_acertos = st_contar("st_d06_funcional", "st_d06_nao_funcional", "st_d06_ideia")

    "{i}Os outros post-its vão mais rápido. O modo escuro vai para ideia a validar. \"Apagar a conta e os dados\" vai para funcional, com um post-it de restrição ao lado: LGPD e regras das lojas.{/i}"
    hide st_mentora
    hide st_qualidade
    with dissolve

    $ advance_minutes(150)
    play music music_office_focused fadein 1.0
    scene bg startup_coworking_tarde
    with fade

    "{i}Depois do almoço, a luz laranja entra pelas janelas em arco e deixa os post-its mais vivos. [NOME_ST_QUALIDADE] puxa uma cadeira ao seu lado com o tablet.{/i}"

    show st_qualidade thinking at right_zoom
    with dissolve
    st_qualidade "Estou lendo suas anotações da entrevista. Estão boas. Só uma coisa aqui me pegou."
    st_qualidade "\"[NOME_ST_ESTUDANTE] achou confuso.\""
    show st_qualidade serious at right_zoom
    st_qualidade "Confuso onde? Em qual passo? \"Confuso\" não é defeito, é uma sensação. Eu não consigo testar uma sensação."

    menu:
        "Como você reage ao comentário?"

        "Me mostra como você anotaria?":
            $ add_friendship_point("st_qualidade", 1)
            show st_qualidade neutral at right_zoom
            st_qualidade "Claro. Eu volto ao que ela contou e escrevo só o que dá para ver acontecendo."
            "{i}[NOME_ST_QUALIDADE] apaga a frase e escreve outra:{/i}"
            "\"[NOME_ST_ESTUDANTE] procurou o botão de apagar na lista e não achou.\""
            st_qualidade "Viu? Agora tem um lugar, uma ação e o que deu errado."

        "Posso mandar mensagem para a [NOME_ST_ESTUDANTE] confirmar onde foi?":
            $ add_friendship_point("st_mentora", 1)
            show st_mentora neutral at left_zoom
            with dissolve
            st_mentora "(da mesa ao lado) Pode e deve. Voltar ao stakeholder é parte do trabalho."
            play sound "audio/effects/cell_vibration.ogg"
            "{i}A resposta chega em poucos minutos.{/i}"
            show st_estudante portrait at center_zoom
            with dissolve
            st_estudante "(mensagem) Foi na lista. Eu arrastei o gasto pro lado, segurei o dedo em cima, e nada. Não achei onde apagar."
            hide st_estudante
            with dissolve
            "{i}Você reescreve a anotação:{/i}"
            "\"[NOME_ST_ESTUDANTE] procurou o botão de apagar na lista e não achou.\""
            hide st_mentora
            with dissolve

        "É só uma anotação, depois eu lembro.":
            show st_qualidade serious at right_zoom
            st_qualidade "Daqui a três semanas ninguém lembra. Anotação é memória da equipe."
            show st_qualidade neutral at right_zoom
            st_qualidade "Pelo que você contou da entrevista, dá para escrever assim:"
            "\"[NOME_ST_ESTUDANTE] procurou o botão de apagar na lista e não achou.\""

    $ advance_minutes(115)
    show st_mentora neutral at left_zoom
    with dissolve
    "{i}No fim da tarde, vocês três param na frente da parede.{/i}"
    st_mentora "Olha que bonito. De um lado, o que é necessidade confirmada. Do outro, o que ainda é aposta."
    st_qualidade "E cada coluna já diz como a gente vai testar. É isso que eu queria ver."
    st_mentora "Amanhã o [NOME_ST_TECHLEAD] passa aqui para olhar as restrições. LGPD é com ele."

    $ advance_minutes(25)
    hide st_mentora
    hide st_qualidade
    with dissolve
    "{i}Você tira uma foto da parede para o notebook. Os post-its de exclusão e de total confiável estão na coluna mais cheia.{/i}"
    $ registrar("st_reg_tipos")

    return
