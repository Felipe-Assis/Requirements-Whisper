# s04.rpy
# -------------------------------
# TEMPO LIVRE DA SAÚDE · SEMANA 4 (sexta, almoço estendido)
# -------------------------------
# Conteúdos próprios da semana (docs/design/intermissoes-saude.md, S4). As
# conversas de fio, os descansos e a mentoria ficam em comum.rpy e
# mentoria.rpy. Recompensas (amizade, pista, registro extra, energia) são
# aplicadas pelo motor depois de cada label: aqui só há falas. pista_tem()
# ainda reflete as semanas anteriores.

label im_saude_abertura_4:
    # A semana 4 começa no dia seguinte à scene_14, que termina à noite: sem
    # este fundo, a abertura do almoço apareceria sobre o escritório escuro.
    scene bg escritorio_interior_tarde
    with dissolve
    "{i}Sexta. O [NOME_DEVELOPER_MANAGEMENT] liberou um almoço estendido até as três: a reunião de arquitetura de ontem rendeu.{/i}"
    if energia_cansaco():
        "{i}A reunião de ontem foi até as sete, e o corpo ainda lembra.{/i}"
    return


# Conversar com Mateus: "Um dia comum" (retorno na scene_15).
label im_saude_s4_conversar_developer_security:
    "{i}[NOME_DEVELOPER_SECURITY] almoça na própria mesa: marmita aberta, garfo trazido de casa e, ao lado do monitor, o bonsai de sempre.{/i}"
    show developer_security serious at right_zoom
    with dissolve
    developer_security "Senta aí, [player_name]. A cadeira do [NOME_DEVELOPER_CODING] está livre, ele desceu para o refeitório."
    developer_security "Eu prefiro comer aqui. Refeitório na sexta parece estação de metrô."
    "{i}Você pergunta como está o dia dele.{/i}"
    show developer_security thinking
    developer_security "Um dia comum. Log, café, mais log."
    play sound "audio/effects/cell_vibration.ogg"
    "{i}O celular dele vibra em cima da mesa. Ele vira a tela para baixo rápido, mas não tão rápido.{/i}"
    "{i}Deu para ler: \"Parabéns, filho. Vem jantar?\"{/i}"
    show developer_security serious
    developer_security "Então. O log de acesso do sistema antigo."
    developer_security "Ele guarda quem entrou e a que horas. Não guarda o que a pessoa abriu."
    developer_security "Se um prontuário vazar, a gente sabe que alguém entrou. Não sabe em qual ficha."
    developer_security "No sistema novo, cada vez que alguém abrir um histórico fica o rastro: quem, quando e de qual paciente. Sem isso, auditoria vira adivinhação."
    "{i}Ele fala devagar, como sempre, e não olha mais para o celular.{/i}"
    "{i}Você decide não comentar a mensagem. Se ele quisesse contar, teria contado.{/i}"
    developer_security "Obrigado pela companhia. O bonsai é ótimo para almoçar junto, mas não discute log."
    hide developer_security
    with dissolve
    return


# Conversar com a Dra. Michelle: o pedido do Adeus Cigarro, um dia depois.
label im_saude_s4_conversar_doutora_1:
    "{i}Na sala das médicas, a [NOME_DOUTORA_1] separa uma pilha de planilhas impressas, com uma caneta marca-texto sem tampa na mão.{/i}"
    show doutora_1 neutral at right_zoom
    with dissolve
    doutora_1 "[player_name]. Pode sentar. Só não mexe nessa pilha, que ela está em ordem. Na minha ordem."
    doutora_1 "Ontem eu entrei na reunião de vocês pedindo a integração com o Adeus Cigarro. Não foi o melhor momento."
    if s14_acordo_escopo == "base_primeiro":
        doutora_1 "Fiquei chateada, confesso. Mas pensei à noite e o autosave é mais urgente mesmo. A [NOME_DOUTORA_2] perde histórico toda semana."
    elif s14_acordo_escopo == "investigar_agora":
        doutora_1 "Obrigada por não prometer o que ninguém sabia se dava. Prefiro esperar uns dias pela investigação a descobrir o problema na véspera."
    else:
        doutora_1 "Mas vocês me ouviram sem prometer nada no impulso. Isso já é mais do que eu costumo ter."
    show doutora_1 serious at right_zoom
    doutora_1 "Já ouvi muito 'sim' de fornecedor. Sim para tudo, prazo para nada. O último sistema chegou um ano depois, sem metade do que tinham prometido."
    doutora_1 "Prefiro ouvir 'ainda não sei' a ouvir 'sim' e esperar um ano."
    menu (tipo="conversa"):
        "Perguntar para que servem os números da pilha":
            doutora_1 "Pesquisa do Instituto. Recaídas por mês, por faixa de idade, por estágio de motivação."
            doutora_1 "Se um número sai errado, sai errado num artigo. Com o meu nome em cima."
        "Comentar que copiar tudo à mão deve tomar muito tempo":
            doutora_1 "Duas horas toda sexta. Oito horas por mês em que eu não atendo ninguém."
            doutora_1 "Por isso eu pedi a integração. Não é capricho, é tempo de consulta."
    doutora_1 "Agora vai almoçar. O [NOME_DEVELOPER_MANAGEMENT] deu até as três, e eu não quero ser a culpada pela sua fome."
    hide doutora_1
    with dissolve
    return


# Estudar na sala de reuniões: o cartão do autosave (extra saude_extra_estimativa).
label im_saude_s4_estudar_sala_reunioes:
    show developer_management thinking at left_zoom
    show developer_project serious at right_zoom
    with dissolve
    "{i}No quadro, os cartões dos casos de uso estão em fila, esperando estimativa. [NOME_DEVELOPER_MANAGEMENT] e [NOME_DEVELOPER_PROJECT] olham para o mesmo cartão: autosave do histórico.{/i}"
    developer_management "Eu diria 3. É salvar um rascunho de tempos em tempos."
    developer_project "8."
    developer_management "8? É quase o tamanho do cadastro inteiro."
    "{i}Você abre no notebook um texto sobre planning poker: todos mostram a estimativa ao mesmo tempo, sem ver a dos outros, e as diferenças grandes viram conversa.{/i}"
    developer_project "A conexão cai no meio da gravação. O que fica salvo? Metade do formulário? A versão anterior? As duas?"
    show developer_management serious
    developer_management "Eu estava estimando o caminho feliz."
    developer_project "Eu estava estimando a internet do ambulatório."
    "{i}O número não era o ponto. A distância entre 3 e 8 mostrou um risco que só um dos dois estava vendo.{/i}"
    developer_management "Fica 5, e a queda de conexão vira um cartão separado. Tamanho relativo, não horas. Depois a gente compara com o que a equipe entrega numa semana."
    developer_management "E na próxima rodada a gente vota junto, [player_name]. Você também mostra a carta."
    hide developer_management
    hide developer_project
    with dissolve
    return


# Ajudar César: "A massa de testes da HAD" (sem pista).
label im_saude_s4_ajudar_developer_test:
    "{i}No refeitório, [NOME_DEVELOPER_TEST] empurra a bandeja para o lado e abre um guardanapo na mesa como se fosse um mapa.{/i}"
    show developer_test enthusiastic at right_zoom
    with dissolve
    developer_test "[player_name], me salva. Segunda eu começo a escrever os testes do cálculo da HAD, antes do código, e quero chegar com a massa de testes pronta."
    developer_test "Você estava na especificação. Me lembra a regra?"
    "{i}Você explica: são duas subescalas, ansiedade e depressão, com sete perguntas cada. Cada resposta vale de 0 a 3, então cada subescala vai de 0 a 21.{/i}"
    "{i}E as faixas: de 0 a 7, normal; de 8 a 10, caso possível; de 11 a 21, caso provável.{/i}"
    show developer_test thinking
    developer_test "Beleza. Agora a pergunta que importa: onde eu testo?"
    developer_test "Se eu testar 3, 9 e 15, tudo passa. E eu não aprendo nada."
    "{i}Você pega a caneta dele e marca no guardanapo os pontos onde uma faixa vira a outra: 7 e 8, 10 e 11. E as pontas: 0 e 21.{/i}"
    show developer_test confident
    developer_test "Isso! Bug adora morar na borda. Alguém escreve 'menor que 7' quando queria 'até 7', e o 7 cai na faixa errada."
    developer_test "E o que não devia entrar?"
    "{i}Você completa a lista: escore 22, número negativo, uma resposta faltando.{/i}"
    developer_test "A resposta faltando é a minha favorita. O que o sistema faz? Soma como zero?"
    "{i}Se somar como zero, o escore sai menor do que devia. Um paciente ansioso pode aparecer como normal.{/i}"
    show developer_test serious
    developer_test "Pois é. É o tipo de erro que ninguém vê na tela. O número parece certinho."
    developer_test "Faltou resposta, o sistema avisa que está incompleta. Nunca inventa o que faltou."
    show developer_test enthusiastic
    developer_test "Teste bom não confirma que funciona. Procura onde não funciona."
    "{i}Quando o guardanapo acaba, tem duas colunas de casos, uma mancha de feijão e três setas que só vocês dois entendem.{/i}"
    developer_test "Esse vai para o bolso. Segunda cedo vira teste automatizado."
    "{i}Ele dobra o guardanapo com cuidado, como quem guarda um documento oficial. Para ele, é.{/i}"
    hide developer_test
    with dissolve
    return


# Observar no ambulatório: "Papel de garantia" (pista saude_p_autosave, se
# ainda não tem; quem é observada é a Dra. Michelle).
label im_saude_s4_observar_ambulatorio:
    "{i}Você atravessa a praça até o Instituto. A [NOME_DOUTORA_1] tem um último paciente antes do almoço e, com a permissão dele, você fica num canto da sala.{/i}"
    show doutora_1 neutral at right_zoom
    with dissolve
    "{i}Ela aplica a escala HAD no sistema antigo. Ao mesmo tempo, marca as mesmas respostas num formulário de papel, ao lado do teclado.{/i}"
    "{i}Pergunta, resposta, clique, risco de caneta. Pergunta, resposta, clique, risco de caneta.{/i}"
    "{i}O paciente sai um instante para buscar um exame na recepção. Você pergunta, baixinho, por que ela faz tudo duas vezes.{/i}"
    doutora_1 "Porque já perdi tanta coisa que agora faço duas vezes."
    doutora_1 "O papel não trava. Não cai. Não pede para fazer login de novo."
    "{i}O paciente volta, e ela retoma do ponto onde tinha parado.{/i}"
    "{i}Na décima pergunta, o ícone da rede no canto da tela ganha um xis. A página recarrega.{/i}"
    "{i}O formulário volta em branco.{/i}"
    doutora_1 "Pronto. Viu?"
    "{i}Ela não se altera. Puxa o papel, confere que está tudo ali e termina as últimas perguntas na caneta.{/i}"
    doutora_1 "Pelo menos não precisei perguntar tudo de novo para ele."
    "{i}Depois da consulta, ela guarda o formulário numa pasta já gorda.{/i}"
    show doutora_1 serious at right_zoom
    doutora_1 "À noite eu digito isso em casa. Cansada, eu erro número. Aí o relatório da pesquisa sai torto e eu volto para as fichas."
    doutora_1 "O problema não é só perder. É o que vem depois de perder."
    "{i}Você anota no caderno, sem nome: paciente C, escala HAD, a rede caiu na pergunta 10, o sistema perdeu, o papel salvou. Custo: digitar tudo de novo à noite.{/i}"
    doutora_1 "Sem nome. Gostei. Nome de paciente não sai desta sala."
    if pista_tem("saude_p_autosave"):
        "{i}É a segunda vez que você vê a mesma perda, com outra médica. Já não é azar: é padrão.{/i}"
    else:
        "{i}O papel ao lado do teclado não é teimosia. É o jeito que ela achou de não depender da sorte.{/i}"
    hide doutora_1
    with dissolve
    return
