# s06.rpy
# -------------------------------
# TEMPO LIVRE DA SAÚDE · SEMANA 6 (Dia da codificação)
# -------------------------------
# Conteúdos próprios da semana (docs/design/intermissoes-saude.md, S6). A
# ajuda ao Joseph desta semana é im_saude_ajudar_developer_coding (s05.rpy,
# com a variação da S6). As conversas de fio, os descansos e a mentoria ficam
# em comum.rpy e mentoria.rpy. Recompensas (amizade, pista, registro extra,
# energia) são aplicadas pelo motor depois de cada label: aqui só há falas.

label im_saude_abertura_6:
    # finalizou_no_escritorio nasce na scene_18 (sem default); getattr evita
    # erro se a intermissão for chamada fora da cena, como nos testes.
    if getattr(store, "finalizou_no_escritorio", False):
        "{i}O módulo está entregue para o [NOME_DEVELOPER_TEST] testar. Até o fim do expediente, o tempo é seu.{/i}"
    else:
        "{i}O módulo ainda não fechou. Enquanto a bateria de testes do [NOME_DEVELOPER_TEST] roda, não há o que mexer nele. O que falta você decide no fim do dia.{/i}"
    if energia_cansaco():
        "{i}Foi um dia inteiro olhando para código. Os olhos pedem outra paisagem.{/i}"
    return


# Estudar na sala de reuniões: o triângulo do Heitor (extra saude_extra_piramide).
label im_saude_s6_estudar_sala_reunioes:
    "{i}A sala de reuniões está vazia, a não ser por [NOME_DEVELOPER_PROJECT], de pé diante do quadro branco.{/i}"
    show developer_project thinking at right_zoom
    with dissolve
    "{i}Ele desenha um triângulo grande, divide em três faixas e estende o pincel para você. Não diz nada.{/i}"
    "{i}Você abre no notebook um texto sobre a pirâmide de testes e lê duas vezes antes de levantar.{/i}"
    "{i}Na base, a faixa mais larga: unidade. Muitos testes, rápidos e baratos. Como o cálculo da HAD: entra um conjunto de respostas, sai um escore.{/i}"
    "{i}No meio: integração. Menos testes. O cadastro gravando no banco de verdade.{/i}"
    "{i}No topo, estreito: ponta a ponta. Poucos, lentos e frágeis. A médica abrindo o navegador, cadastrando um paciente e conferindo o histórico.{/i}"
    "{i}Você devolve o pincel. [NOME_DEVELOPER_PROJECT] olha o quadro um tempo e só acena com a cabeça.{/i}"
    show developer_project serious
    developer_project "Agora vira."
    "{i}Ele desenha o mesmo triângulo de ponta-cabeça: quase tudo de ponta a ponta em cima, quase nada de unidade embaixo.{/i}"
    developer_project "Sistema antigo. Teste só na mão, pela tela. Quarenta minutos para saber que quebrou."
    "{i}Você entende sem ele precisar dizer: com a pirâmide invertida, a pipeline demora e o erro aparece tarde, quando já custa caro.{/i}"
    developer_project "O nosso não vai ser assim."
    hide developer_project
    with dissolve
    return


# Observar no ambulatório: "Erro 0x80004005" (só cena, sem pista).
label im_saude_s6_observar_ambulatorio:
    "{i}Você atravessa a praça até o Instituto. A [NOME_DOUTORA_2] tem uma consulta de retorno e deixa você assistir do canto, com a permissão da paciente.{/i}"
    show doutora_2 neutral at right_zoom
    with dissolve
    "{i}A consulta corre bem. Ela preenche o histórico, atualiza os cigarros por dia, marca o próximo retorno e clica em Salvar.{/i}"
    "{i}Na tela aparece uma caixa cinza: \"Erro 0x80004005\". Embaixo, um único botão: OK.{/i}"
    doutora_2 "Salvou ou não salvou?"
    "{i}Ela clica em OK. A ficha volta com os campos preenchidos. Gravados ou não, não dá para saber.{/i}"
    doutora_2 "Se eu clicar em Salvar de novo, pode duplicar a consulta. Se eu não clicar, pode não ter salvado nada."
    "{i}Ela liga para a TI. Música de espera. A paciente olha para o relógio na parede.{/i}"
    "{i}Dez minutos depois, alguém atende, pede o número do erro, consulta alguma coisa e diz que salvou, sim.{/i}"
    show doutora_2 serious at right_zoom
    doutora_2 "Dez minutos. Ela veio de ônibus, de longe, e passou dez minutos me vendo ouvir musiquinha."
    "{i}Depois que a paciente sai, você pergunta o que a mensagem deveria ter dito.{/i}"
    doutora_2 "Qualquer coisa que uma pessoa entenda."
    doutora_2 "Salvou ou não. Se perdi alguma coisa, o quê. E o que eu faço agora. Só isso."
    menu (tipo="conversa"):
        "Perguntar se esse erro aparece sempre":
            doutora_2 "Esse número eu já decorei. Aparece para tudo: rede, senha, impressora."
            doutora_2 "Um erro que serve para tudo não diz nada."
        "Perguntar o que ela fazia nas outras vezes":
            doutora_2 "Na dúvida, eu anoto no papel e digito de novo à noite. O papel é o meu botão de desfazer."
    "{i}Você anota no caderno, sem nome: mensagem de erro também é requisito. Ela precisa dizer o que aconteceu, se algo se perdeu e o que fazer agora, com palavras de gente.{/i}"
    doutora_2 "Escreve isso em letra grande. E manda para o [NOME_DEVELOPER_CODING] antes que ele invente outro código de erro."
    hide doutora_2
    with dissolve
    return


# Ajudar Mateus na sala de servidores: "O backup verde" (pista saude_p_backup).
# Sem semana no nome porque a S6 é a semana dele; a S7 tem o próprio label
# (im_saude_s7_ajudar_developer_security, em s07.rpy).
label im_saude_ajudar_developer_security:
    "{i}No subsolo, a sala de servidores está fria e barulhenta. [NOME_DEVELOPER_SECURITY] tira caixas do chão para abrir espaço num rack para o servidor novo.{/i}"
    show developer_security serious at right_zoom
    with dissolve
    developer_security "Chegou ajuda. Pega a ponta dessa caixa, por favor. Devagar, que tem cabo por baixo."
    "{i}Vocês passam meia hora tirando poeira, caixas vazias e um monitor de tubo que ninguém sabe de onde veio.{/i}"
    "{i}Na parede, uma tela pequena mostra o painel da rotina de backup: uma fileira de quadradinhos verdes, um por dia.{/i}"
    developer_security "Dois anos sem falhar. Toda noite, às onze, copia o banco inteiro para o outro prédio."
    "{i}Você pergunta quando foi a última vez que alguém restaurou uma dessas cópias.{/i}"
    show developer_security thinking
    developer_security "..."
    developer_security "Boa pergunta."
    "{i}Ele procura no wiki: 'restauração', 'restore', 'recuperar'. Só aparece a página que explica como configurar a rotina, de dois anos atrás. Nenhum teste. Nenhuma data.{/i}"
    developer_security "Verde quer dizer que a cópia foi gravada. Não quer dizer que ela abre."
    developer_security "Backup que nunca foi restaurado é um arquivo que a gente torce para estar certo."
    menu (tipo="conversa"):
        "Sugerir testar uma restauração agora":
            developer_security "Restaurar o banco inteiro leva horas, e a homologação está ocupada com os testes de hoje."
            developer_security "Hoje não dá. Mas não vou fingir que não ouvi."
        "Perguntar o que poderia faltar numa cópia":
            developer_security "Tudo o que ninguém lembrou de incluir. O backup copia o que mandaram copiar, não o que a gente precisa."
    "{i}Ele anota no caderno de capa preta: 'Testar restauração do backup. Depois do deploy.'{/i}"
    developer_security "Escrevi. Assim não fica só na minha cabeça."
    "{i}Vocês voltam às caixas. No fim, o rack tem espaço, os cabos estão presos com velcro e o monitor de tubo foi para o corredor, à espera de alguém com coragem de levar embora.{/i}"
    developer_security "Obrigado, [player_name]. Arrumar sala de servidor é a parte do trabalho que ninguém vê."
    hide developer_security
    with dissolve
    return
