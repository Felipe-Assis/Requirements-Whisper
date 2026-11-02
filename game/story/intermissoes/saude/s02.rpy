# s02.rpy
# -------------------------------
# TEMPO LIVRE DA ROTA SAÚDE · SEMANA 2 (dia da entrevista, 16h às 19h30)
# -------------------------------
# docs/design/intermissoes-saude.md §2 (S2). Conversas dos developers e da
# Dra. Nathalia: fios em comum.rpy. Mentoria: mentoria.rpy.
# A pista saude_p_cpf (observar), a amizade e o registro extra são dados pelo
# motor depois de cada label.

label im_saude_abertura_2:
    "{i}Fim da tarde do dia da entrevista. Na saída do Instituto, a [NOME_DOUTORA_2] comentou que o ambulatório fica aberto até o começo da noite, se você quiser ver a rotina de perto.{/i}"
    "{i}No mapa, do outro lado da praça, o Instituto aparece aceso pela primeira vez.{/i}"
    if energia_cansaco():
        "{i}A entrevista gastou mais do que parecia. Hoje a tarde rende menos.{/i}"
    return


label im_saude_s2_ajudar_developer_coding:
    # O README (sem pista)
    show developer_coding neutral at center_zoom
    "{i}[NOME_DEVELOPER_CODING] está cercado de janelas de terminal. Na tela do meio, o repositório do ByeByeFumo no GitLab, ainda quase vazio.{/i}"
    developer_coding "Chegou na hora certa. Lint configurado, modelo de mensagem de commit pronto. Falta a parte que eu mais adio."
    developer_coding "O README. Mais exatamente, a seção 'Como rodar o projeto'."
    show developer_coding thinking
    developer_coding "E você é a pessoa perfeita: chegou agora e não conhece o ambiente. Sem ofensa. Para um README, isso é elogio."
    "{i}Você lê os arquivos do repositório por alguns minutos e escreve, com alguma confiança:{/i}"
    "{i}'Instale as dependências e rode o projeto.'{/i}"
    show developer_coding serious
    developer_coding "Hum."
    developer_coding "'Rode o projeto' não é instrução. Qual comando? Em qual pasta? O que aparece quando dá certo?"
    developer_coding "Pensa em alguém que chega daqui a seis meses, numa sexta à tarde, sem ninguém por perto. Essa pessoa lê isso e faz o quê?"
    menu:
        "Tentar rodar o projeto do zero, seguindo só o que escreveu":
            "{i}Você abre uma pasta vazia e segue o próprio texto. Trava na segunda linha: que dependências? Instaladas onde?{/i}"
            developer_coding "Viu? Você escreveu de memória. E a memória pula justamente o passo que parece óbvio para quem já sabe."
        "Pedir para [NOME_DEVELOPER_CODING] rodar do zero enquanto você anota cada passo":
            "{i}Ele apaga a pasta, clona tudo de novo e vai devagar. Você anota cada passo, até o que parece bobo.{/i}"
            developer_coding "Repara: eu copiei o arquivo de configuração sem nem pensar. Se isso não estiver escrito, ninguém mais vai saber que precisa."
    "{i}Você reescreve a seção em passos numerados:{/i}"
    "{i}1. Clone o repositório. 2. Na pasta do projeto, copie o arquivo .env.exemplo para .env. 3. Rode docker compose up. 4. Abra o navegador em localhost, porta 8080.{/i}"
    show developer_coding thinking
    developer_coding "Melhor. Agora a última pergunta: como a pessoa sabe que deu certo?"
    "{i}Você acrescenta: 'Resultado esperado: a tela de login do ByeByeFumo. Se aparecer erro de porta ocupada, feche o outro programa que usa a porta 8080.'{/i}"
    show developer_coding neutral
    developer_coding "Agora sim. Dá para conferir. Quem ler sabe se chegou lá ou em que passo se perdeu."
    "{i}Você olha a seção pronta e lembra da entrevista de hoje. 'Um cadastro mais prático' também não dizia o que conferir.{/i}"
    developer_coding "É tudo a mesma coisa, né? Requisito, README, mensagem de commit. Se não dá para conferir, não está pronto."
    developer_coding "Valeu pela ajuda. Vou pedir para a próxima pessoa que chegar testar o seu README. Se ela travar, a culpa é sua."
    show developer_coding thinking
    developer_coding "Brincadeira. Metade é minha."
    hide developer_coding
    return


label im_saude_s2_estudar_sala_reunioes:
    # Fluxo alternativo e exceção (saude_extra_fluxos)
    "{i}Você se senta no fundo da sala de reuniões com o material sobre casos de uso. No quadro branco, sobrou um canto livre.{/i}"
    show developer_project thinking at center_zoom
    "{i}[NOME_DEVELOPER_PROJECT] levanta, pega um pincel e desenha uma linha reta com uma seta no fim. Depois, dois desvios.{/i}"
    developer_project "Caminho principal. O paciente chega, tem documento, é cadastrado."
    "{i}Ele aponta o primeiro desvio, que volta a encontrar a linha antes da seta.{/i}"
    developer_project "Um desvio ainda chega lá."
    show developer_project serious
    "{i}O segundo desvio termina num X.{/i}"
    developer_project "O outro não chega. E o sistema tem que dizer o que fazer."
    "{i}Você lê o resto com o desenho na cabeça. O primeiro é um fluxo alternativo; o segundo, uma exceção. Os dois entram no caso de uso, com o passo onde começam.{/i}"
    developer_project "Pode ficar com o desenho. Eu apago amanhã."
    hide developer_project
    "{i}Você tira uma foto do quadro e resume tudo no notebook.{/i}"
    return


label im_saude_s2_observar_ambulatorio:
    # A recepção às quatro (pista saude_p_cpf, dada pelo motor)
    "{i}A sala de espera do ambulatório tem cadeiras azuis, um bebedouro e uma televisão sem som. Você se senta perto do balcão da recepção, com o caderno no colo.{/i}"
    "{i}Atrás do balcão, a recepcionista, Sônia, atende o telefone com o ombro e digita com as duas mãos.{/i}"
    saude_npc_recepcao "Instituto, boa tarde. Retorno? Só um minutinho, que o sistema está pensando."
    "{i}O sistema pensa por quase um minuto. Ela aproveita para entregar uma senha a quem acabou de chegar.{/i}"
    "{i}Um senhor se aproxima do balcão, meio sem jeito, com uma sacola de farmácia na mão.{/i}"
    "Paciente" "Boa tarde. A doutora mandou eu vir hoje. Mas esqueci a carteira em casa."
    saude_npc_recepcao "Sem documento eu não consigo abrir a ficha, senhor. O sistema não deixa salvar sem CPF."
    "Paciente" "Eu moro longe. Se eu voltar para buscar, não chego mais hoje."
    "{i}Sônia olha para a fila, depois para ele. Pega um papel de rascunho e escreve o nome dele em letra de forma.{/i}"
    saude_npc_recepcao "Faz assim: o senhor é atendido, e eu cadastro depois. Na próxima vez, traz o documento, tá?"
    "{i}Ela escreve 'cadastrar depois' embaixo do nome e prende o papel com um clipe na borda do monitor.{/i}"
    "{i}Você conta: já são três papéis assim, presos em volta da tela. Um deles está amarelado.{/i}"
    menu (tipo="conversa"):
        "Perguntar à Sônia o que acontece com esses papéis":
            saude_npc_recepcao "Quando dá, eu cadastro no fim do dia. Quando não dá... eles ficam aí. Uns caem atrás da mesa."
        "Só observar e anotar":
            "{i}Você anota sem interromper. Sônia tira o papel mais antigo, olha, suspira e prende de novo no mesmo lugar.{/i}"
    show doutora_2 neutral at center_zoom
    "{i}A [NOME_DOUTORA_2] passa pelo balcão com uma pasta debaixo do braço e vê você ali.{/i}"
    doutora_2 "Veio mesmo! Viu os papéis?"
    show doutora_2 serious at center_zoom
    doutora_2 "Esses papéis somem. Aí o paciente volta e é como se fosse a primeira vez. Sem histórico, sem nada."
    doutora_2 "E às vezes ele ganha uma ficha nova, com outro número. Pronto: dois pacientes no sistema que são a mesma pessoa."
    "{i}Você lembra da [NOME_DOUTORA_1] na entrevista, falando de paciente duplicado. Agora você sabe de onde ele vem.{/i}"
    hide doutora_2
    "{i}No caderno, você escreve: 'Paciente sem documento: a recepção anota no papel e o cadastro fica para depois. Três papéis no monitor.' Sem o nome de ninguém.{/i}"
    "{i}Na entrevista, ninguém falou desses papéis. Eles só aparecem para quem fica olhando.{/i}"
    return


label im_saude_s2_conversar_doutora_1:
    # Dra. Michelle: o dado alterado sem registro
    show doutora_1 neutral at center_zoom
    doutora_1 "[player_name]. Que bom. Queria falar com alguém da equipe sem a sala cheia."
    doutora_1 "Na entrevista eu contei dos dois dias conferindo fichas de papel. Não contei a pior parte."
    show doutora_1 serious at center_zoom
    doutora_1 "O número errado já tinha ido para o relatório da diretoria. E para um resumo de pesquisa, enviado a um congresso."
    doutora_1 "Tive que escrever para os organizadores corrigindo o dado. Você imagina a vergonha."
    menu (tipo="conversa"):
        "Perguntar se ela descobriu quem mudou o dado":
            doutora_1 "Nunca. E, sinceramente, isso é o que menos importa."
        "Perguntar o que teria ajudado naquele dia":
            doutora_1 "Uma linha. Uma só. 'Este campo mudou de 12 para 21, em tal dia, a partir de tal tela.' Eu teria resolvido em dez minutos."
    doutora_1 "Não quero saber quem errou. Quero saber o que mudou, quando e de onde veio."
    doutora_1 "Gente erra. Dígito trocado acontece. O que não pode é o sistema esconder o erro de quem precisa corrigir."
    "{i}Você anota: registro de alteração, com valor antigo, valor novo, data e origem. Ela lê a anotação e faz que sim com a cabeça.{/i}"
    doutora_1 "Isso. Escreve exatamente assim, que eu assino embaixo."
    hide doutora_1
    return
