# co_01_chegada.rpy
# Rota Corporativo, semana 1, segunda, 8h50 às 11h30.
# Fonte: docs/rotas/corporativo.md, cena co_01. Sem variáveis novas.

label co_01_chegada:
    $ set_available()
    $ set_time(8, 50)

    play music music_office_motivated fadein 1.5
    scene bg empresa_exterior_manha
    with fade

    "{i}Segunda-feira. A torre de vidro do Grupo Vértice reflete o céu do Rio, e as catracas do saguão não param de apitar.{/i}"
    "{i}Dezoito mil funcionários em vinte e dois estados. A partir de hoje, um a mais na lista.{/i}"

    $ advance_minutes(10)
    "{i}Na recepção, tiram sua foto, imprimem um crachá provisório e entregam um termo de confidencialidade.{/i}"
    "{i}O termo cita a LGPD, a Lei Geral de Proteção de Dados: nada de levar para fora informação de funcionários ou de chamados. Você lê até o fim e assina.{/i}"

    $ advance_minutes(5)
    show co_mentora neutral at center_zoom
    with dissolve
    co_mentora "[player_name]? Eu sou a [NOME_CO_MENTORA] Nogueira, analista de sistemas. Vou acompanhar seu estágio. Boas-vindas!"
    co_mentora "A gente fica no décimo segundo andar, na Coordenação de Sistemas Corporativos. É a parte da Diretoria de TI que cuida dos sistemas internos da empresa."
    co_mentora "Vamos por partes: primeiro a equipe, depois o sistema."
    $ add_contact("co_mentora")
    $ add_friendship_point("co_mentora", 1)
    hide co_mentora
    with dissolve

    $ advance_minutes(10)
    scene bg escritorio_interior_manha
    with fade

    "{i}O andar é amplo, com baias cinzentas, ar-condicionado forte e um quadro cheio de post-its perto da janela.{/i}"

    show co_mentora neutral at left_zoom
    show co_legado neutral at right_zoom
    with dissolve
    co_mentora "Este é o [NOME_CO_LEGADO] Takeda. Ele está no SGC, o Sistema de Gestão de Chamados, desde o começo."
    co_legado "Desde 2008, [player_name]. Eu e esta caneca. Ela já sobreviveu a três reestruturações. Eu, a duas e meia."
    $ add_contact("co_legado")
    $ add_friendship_point("co_legado", 1)

    hide co_legado
    show co_dev neutral at right_zoom
    with dissolve
    co_dev "E aí! Eu sou o [NOME_CO_DEV]. Cuido do módulo novo, o Farol. Bora, que tem muita coisa pra te mostrar."
    $ add_contact("co_dev")
    $ add_friendship_point("co_dev", 1)

    hide co_dev
    show co_qualidade neutral at right_zoom
    with dissolve
    co_qualidade "[NOME_CO_QUALIDADE]. Qualidade, testes e gestão de mudanças. Por aqui eu sou \"a pessoa do CAB\"."
    co_mentora "CAB é o comitê que aprova mudanças em produção. Você vai ouvir muito essa sigla."
    co_qualidade "E vai me ouvir muito também. Se não está registrado, não aconteceu."
    $ add_contact("co_qualidade")
    $ add_friendship_point("co_qualidade", 1)
    hide co_qualidade
    hide co_mentora
    with dissolve

    $ advance_minutes(20)
    "{i}[NOME_CO_MENTORA] puxa uma cadeira para você ao lado da mesa dela e abre o SGC no monitor.{/i}"
    show expression "images/artifacts/co_sgc_legado.png" as tela_sgc at artefato_tela
    with dissolve
    "{i}A tela é cinza, com abas em degradê azul e botões em relevo. A tabela de chamados tem uma letra tão pequena que você chega mais perto.{/i}"
    co_mentora "Olha o chamado 48213. O que você vê aí?"
    "{i}Estado: Resolvido. Campo Solução: vazio. Alguém fechou o chamado e não escreveu o que fez.{/i}"
    co_mentora "Isso. Agora pensa em quem abriu. A pessoa vê \"Resolvido\" e mais nada. Se o problema continua, o que ela faz?"
    "{i}Liga para a central. Provavelmente mais de uma vez.{/i}"
    co_mentora "Exato. A central trata uns 1.300 chamados por dia, com 140 atendentes. E boa parte das ligações é gente perguntando \"e o meu chamado?\"."
    hide tela_sgc
    with dissolve

    $ advance_minutes(15)
    show co_mentora neutral at left_zoom
    with dissolve
    co_mentora "É para isso que existe o Projeto Farol. Um módulo novo, construído ao lado do SGC."
    co_mentora "Quem abre chamado vai consultar pelo número e ver o estado, quem está atendendo e o que foi feito. Sem precisar ligar."
    co_mentora "Temos oito semanas. A implantação vai ser numa janela de sábado, de madrugada, com a central fechada."

    show co_legado thinking at center_zoom
    with dissolve
    co_legado "Detalhe importante: o SGC tem dezesseis anos e nenhum teste automatizado. Cada mudança é um passeio no escuro. Com lanterna, se der sorte."

    show co_dev serious at right_zoom
    with dissolve
    co_dev "Um dia isso vai ter que ser reescrito. Não dá pra viver de remendo pra sempre."
    co_legado "Já ouvi essa frase antes, [NOME_CO_DEV]. Outro dia eu conto como terminou."

    hide co_dev
    show co_qualidade thinking at right_zoom
    with dissolve
    "{i}[NOME_CO_QUALIDADE] não diz nada. Só aponta com a caneta para um calendário grande na parede, cheio de sábados marcados em vermelho e siglas escritas à mão.{/i}"
    hide co_mentora
    hide co_legado
    hide co_qualidade
    with dissolve

    $ advance_minutes(95)
    "{i}O resto da manhã passa entre senhas de acesso, e-mails de boas-vindas e um manual de 2011 que ninguém parece abrir.{/i}"
    "{i}Perto das onze e meia, o andar começa a falar de almoço. Você ainda tem alguns minutos.{/i}"

    menu (tipo="conversa"):
        "Antes do almoço, com quem você puxa conversa?"

        "\"[NOME_CO_LEGADO], como era o SGC quando nasceu?\"":
            $ add_friendship_point("co_legado", 1)
            show co_legado thinking at center_zoom
            with dissolve
            co_legado "Isso aí tem história. Em 2008 o SGC rodava num servidor bege que a gente chamava de Tia Neide. Fazia barulho de liquidificador."
            co_legado "No dia do lançamento, às dez da manhã, a central já tinha aberto quinhentos chamados. A Tia Neide esquentou tanto que eu levei um ventilador de casa."
            co_legado "Por que Tia Neide? Não pergunte. Essa história fica para quando você tiver crachá definitivo."
            hide co_legado
            with dissolve

        "\"[NOME_CO_DEV], o que já existe do Farol?\"":
            $ add_friendship_point("co_dev", 1)
            show co_dev neutral at center_zoom
            with dissolve
            co_dev "Por enquanto, um protótipo da tela de consulta. Fiz em duas noites, tipo speedrun."
            co_dev "E uma vontade enorme de reescrever o resto. O SGC é aquele save de 2008 que ninguém tem coragem de apagar."
            co_dev "Mas aí o [NOME_CO_LEGADO] me olha daquele jeito e eu volto a ler PL/SQL. Bora almoçar?"
            hide co_dev
            with dissolve

        "\"[NOME_CO_QUALIDADE], o que é esse calendário na parede?\"":
            $ add_friendship_point("co_qualidade", 1)
            show co_qualidade neutral at center_zoom
            with dissolve
            co_qualidade "As janelas de mudança. Cada sábado em vermelho é uma madrugada em que alguma coisa sobe para produção."
            co_qualidade "Nada sobe sem passar por aqui. Pedido registrado, comitê de acordo, plano de volta e gente de plantão."
            co_qualidade "O cinza com um X é mudança que precisou voltar. Também está registrada, claro."
            hide co_qualidade
            with dissolve

    $ set_time(11, 30)
    "{i}Você sai para o almoço com o crachá provisório no pescoço e o número 48213 na cabeça.{/i}"

    return
