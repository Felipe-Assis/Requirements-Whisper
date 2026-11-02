# co_04_preparacao.rpy
# Semana 2, segunda, 9h às 17h30. Arqueologia do SGC: chamados reais, central e
# sala de arquivo. Decisão 2 (co_ok_fontes), registro co_reg_legado e conquista
# co_conq_arqueologia. Fonte: docs/rotas/corporativo.md, co_04.

label co_04_preparacao:
    $ set_available("co_dev", "co_qualidade")
    $ set_time(9, 0)

    play music music_office_concentrated_2 fadein 1.0
    scene bg escritorio_interior_manha
    with fade

    "{i}Segunda-feira, semana 2. Na mesa de [NOME_CO_MENTORA], uma pilha de folhas impressas espera por você: os 30 chamados do mês passado, sem dados pessoais.{/i}"

    show co_mentora neutral at left_zoom
    with dissolve
    co_mentora "Bom dia, [player_name]. Vamos por partes: primeiro a gente lê, depois conversa."

    $ advance_minutes(40)
    "{i}VPN, senha, notebook sem rede, sistema de campo fora do ar. Você marca cada chamado estranho.{/i}"

    show expression "images/artifacts/co_sgc_legado.png" as tela_sgc at artefato_tela
    with dissolve
    "{i}No monitor, o SGC abre o chamado 48213. Estado: Resolvido. Campo Solução: vazio.{/i}"
    "{i}Ele não está sozinho. Na contagem final, nove dos 30 chamados estão assim.{/i}"
    hide tela_sgc
    with dissolve

    show co_mentora thinking at left_zoom
    co_mentora "Nove em trinta. Quase um terço. Quem abriu esses chamados não sabe o que foi feito. E a central também não."
    co_mentora "Na quarta a gente entrevista a [NOME_CO_SUPERVISORA], supervisora da central, e o [NOME_CO_SOLICITANTE], que abre chamado toda semana."
    co_mentora "Num legado, a preparação começa descobrindo o que o sistema faz de verdade."

    show co_legado neutral at right_zoom
    with dissolve
    co_legado "Ouvi meu nome? Não ouvi, mas ouvi \"SGC\". Dá no mesmo."
    "{i}[NOME_CO_LEGADO] para ao lado da mesa, com a caneca de 2008 nas duas mãos.{/i}"

    show co_mentora neutral at left_zoom
    co_mentora "Chegou na hora, [NOME_CO_LEGADO]. [player_name], me diz você: onde a gente busca isso?"

    menu (tipo="trabalho"):
        "Onde buscar o comportamento real do SGC antes da entrevista?"

        "No manual de 2011; é a documentação oficial.":
            $ co_erro("co_ok_fontes")
            show co_legado serious at right_zoom
            co_legado "O manual diz que existe o estado Pendente. Ele sumiu em 2015."
            co_legado "Você ia perguntar à [NOME_CO_SUPERVISORA] sobre um estado que não existe. Ela ia achar que a TI nem conhece o próprio sistema."

        "Cruzar fontes: chamados reais, o código e as rotinas do banco, e quem usa no dia a dia.":
            $ co_acerto("co_ok_fontes")
            show co_mentora neutral at left_zoom
            co_mentora "Isso. Cada fonte mostra um pedaço. Quando duas discordam, aí tem pergunta boa para a entrevista."
            show co_legado neutral at right_zoom
            co_legado "E quando as três concordam, desconfia um pouco. Mas só um pouco."

        "Perguntar só ao [NOME_CO_LEGADO]; ele fez o sistema.":
            $ co_erro("co_ok_fontes")
            show co_legado thinking at right_zoom
            co_legado "Agradeço a confiança. Mas eu lembro do que eu fiz, não do que os outros mudaram depois."
            co_legado "E eu não vou estar aqui para sempre. Se a resposta mora só na minha cabeça, o projeto tem um problema."

    if not co_ok_fontes:
        show co_mentora thinking at left_zoom
        co_mentora "Uma fonte sozinha engana. Como você reformula?"
        menu (tipo="trabalho"):
            "Como confirmar o que o sistema faz hoje?"
            "Comparar o que os dados mostram com o código e com o relato de quem usa.":
                show co_mentora neutral at left_zoom
                co_mentora "Agora sim. Dados, código e pessoas. Se uma das três discordar, a gente anota a dúvida."

    co_mentora "Então começamos pelas pessoas. Antes do almoço, uma hora ao lado da Neusa, na central."
    hide co_legado
    hide co_mentora
    with dissolve

    $ set_time(11, 0)
    scene bg central_atendimento_manha
    with fade

    "{i}A central ocupa o andar inteiro. Neusa, atendente há doze anos, puxa duas cadeiras para vocês.{/i}"
    "{i}Um técnico de Campos, uma analista de Recife, outro técnico. Todas as ligações começam igual: \"E meu chamado?\"{/i}"
    "{i}Para cada uma, Neusa troca de aba quatro, cinco vezes: chamado, histórico, fila técnica, e-mail. Em duas, encontra só \"Resolvido\".{/i}"
    "\"Senhor, aqui diz que foi resolvido, mas não diz o que fizeram. Vou abrir outro chamado para perguntar.\""
    "{i}Em uma hora, seis ligações. Nenhuma era um problema novo. Todas eram perguntas sobre um problema antigo.{/i}"

    show co_mentora serious at left_zoom
    with dissolve
    co_mentora "Eu fazia exatamente isso em 2004. Só mudou a cor das abas."
    hide co_mentora
    with dissolve

    $ set_time(14, 30)
    scene bg sala_arquivo_tarde
    with fade

    "{i}À tarde, [NOME_CO_LEGADO] leva vocês até a sala de arquivo. Estantes de aço, caixas com etiqueta de papel, cheiro de poeira.{/i}"

    show co_legado thinking at right_zoom
    show co_mentora neutral at left_zoom
    with dissolve
    co_legado "Isso aí tem história. Se existe um papel sobre o SGC, ele está nesta sala. Se está certo, aí é outra conversa."
    "{i}Ele puxa uma pasta encadernada em espiral: \"SGC_manual_v3_FINAL_revisado2.doc\", impresso em 2011.{/i}"
    "{i}Na página dos estados, lá está ele: Pendente. O estado que deixou de existir em 2015.{/i}"
    co_legado "Viu? O manual mostra o que alguém planejou. O banco mostra o que roda."

    $ advance_minutes(90)
    "{i}Você abre o notebook ao lado das folhas da manhã e cruza os nove chamados vazios com os dados do banco.{/i}"
    "{i}Sete são de \"Reset de senha\". E os sete foram fechados exatamente 72 horas depois de abertos. Nem um minuto a mais.{/i}"

    show co_mentora thinking at left_zoom
    co_mentora "72 horas cravadas não é gente. Gente não é tão pontual."

    show co_legado serious at right_zoom
    co_legado "Não é gente. É a TRG_FECHA_SENHA_72H. Uma rotina do banco."
    co_legado "Nasceu em 2013, depois de uma greve. A fila de senha passou de três mil chamados. A gente fez a rotina para fechar sozinha os chamados sem resposta em 72 horas."
    co_legado "Funcionou. E ninguém registrou. Nem eu."

    "{i}[NOME_CO_LEGADO] segura a pasta empoeirada, meio sem jeito.{/i}"

    menu (tipo="conversa"):
        "O que você faz?"

        "Me conta como essa regra das 72 h nasceu.":
            $ add_friendship_point("co_legado", 1)
            show co_legado thinking at right_zoom
            co_legado "Março de 2013. A central estava pela metade, e todo mundo esquecia a senha depois do Carnaval."
            co_legado "Eu escrevi a rotina numa quinta à noite, testei no servidor da Tia Neide e subi na sexta. A fila caiu pela metade em uma semana."
            co_legado "Era para ser provisória. Provisório aqui dura onze anos."

        "Vamos registrar isso no wiki agora, com a data e o motivo.":
            $ add_friendship_point("co_mentora", 1)
            show co_mentora neutral at left_zoom
            co_mentora "Agora mesmo. Se a gente deixar para depois, vira mais uma regra que só o [NOME_CO_LEGADO] sabe."
            "{i}[NOME_CO_MENTORA] abre o wiki no celular e cria a página \"TRG_FECHA_SENHA_72H: origem e motivo\". [NOME_CO_LEGADO] dita a data e você revisa o texto.{/i}"

        "Anoto e sigo.":
            "{i}Você anota a rotina, o ano e o motivo no notebook e volta para os chamados.{/i}"

    $ co_registrar("co_reg_legado")

    $ set_time(16, 45)
    show co_mentora neutral at left_zoom
    co_mentora "Agora o roteiro de quarta. Perguntas abertas. Pedir um episódio concreto. Atenção a palavras vagas, tipo \"fácil\"."
    show co_mentora thinking at left_zoom
    co_mentora "E espere um conflito. A [NOME_CO_SUPERVISORA] cuida da fila, o [NOME_CO_SOLICITANTE] cuida do campo. Cada um vai puxar para um lado."
    show co_legado neutral at right_zoom
    co_legado "Leva o dado das 72 horas. Pergunta difícil com dado na mão vira conversa."

    $ set_time(17, 30)
    "{i}Você fecha o notebook. Três fontes, uma regra escondida e um roteiro pronto para quarta.{/i}"

    $ co_conceder("co_conq_arqueologia")

    hide co_legado
    hide co_mentora
    with dissolve

    return
