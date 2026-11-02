# friends_data.rpy
# -------------------------------
# DICIONÁRIO DE AMIGOS E ASSISTANT_IDS
# -------------------------------
# AMIGOS_DATA mapeia cada id de contato -> {name, portrait, assistant_id, desc}.
# Contatos com assistant_id None têm também "offline": falas locais usadas
# pelo chat no lugar do backend (ver python/chat_backend.rpy).
# Fica em `init python` prio 0 porque referencia os defines NOME_* (também
# prio 0, em data/character_names.rpy) — NÃO usar `python early`.

init python:
    AMIGOS_DATA = {
        "developer_ai": {
            "name": NOME_DEVELOPER_AI,
            "portrait": "images/characters/developer_ai/portrait.png",
            "assistant_id": "asst_fbVtwWljzUZhHtmllEphxkYn",
            "desc": _("Especialista em IA e ML. Animado, detalhista, sempre com ideias inovadoras.")
        },
        "developer_requirements": {
            "name": NOME_DEVELOPER_REQUIREMENTS,
            "portrait": "images/characters/developer_requirements/portrait.png",
            "assistant_id": "asst_t5wjZ9SCpAbHNCg7utEcY2et",
            "desc": _("Especialista em requisitos, comunicativa, detalhista e proativa.")
        },
        "developer_coding": {
            "name": NOME_DEVELOPER_CODING,
            "portrait": "images/characters/developer_coding/portrait.png",
            "assistant_id": "asst_d8n3ntyqOsHfdBkJA2LqrZFh",
            "desc": _("Desenvolvedor sênior, crítico e experiente, já liderou vários projetos.")
        },
        "developer_management": {
            "name": NOME_DEVELOPER_MANAGEMENT,
            "portrait": "images/characters/developer_management/portrait.png",
            "assistant_id": "asst_DzfYAhfiHWBPKborojHC50lZ",
            "desc": _("Gerente jovem, organizado, querido pela equipe.")
        },
        "developer_quality": {
            "name": NOME_DEVELOPER_QUALITY,
            "portrait": "images/characters/developer_quality/portrait.png",
            "assistant_id": "asst_YkbAOJa4eudUqFL1NMTLkEAA",
            "desc": _("Apaixonada por ensinar e qualidade de software.")
        },
        "developer_project": {
            "name": NOME_DEVELOPER_PROJECT,
            "portrait": "images/characters/developer_project/portrait.png",
            "assistant_id": "asst_UrbLbKIjf7i5bBzDpvwTkAWn",
            "desc": _("Arquiteto de software e bancos, fala pouco, mas certeiro.")
        },
        "developer_security": {
            "name": NOME_DEVELOPER_SECURITY,
            "portrait": "images/characters/developer_security/portrait.png",
            "assistant_id": "asst_FylyYRTtZVHXYpVpqCxVk6AX",
            "desc": _("Senior, fala devagar e preza segurança dos sistemas.")
        },
        "developer_test": {
            "name": NOME_DEVELOPER_TEST,
            "portrait": "images/characters/developer_test/portrait.png",
            "assistant_id": "asst_r5MMYuijOxJHRmqdynMewgWA",
            "desc": _("Jovem prodígio dos testes, faz tudo com eficiência.")
        },
        "doutora_1": {
            "name": NOME_DOUTORA_1,
            "portrait": "images/characters/doutora_1/portrait.png",
            "assistant_id": "asst_nUAGJlGDbfdxhxpADXSRdLwC",
            "desc": _("Experiente médica.")
        },
        "doutora_2": {
            "name": NOME_DOUTORA_2,
            "portrait": "images/characters/doutora_2/portrait.png",
            "assistant_id": "asst_0RVJbliiBedg7ADSndhb1BnS",
            "desc": _("Jovem médica.")
        },
        # Rotas Startup e Corporativo: sem assistente remoto (assistant_id None).
        # O chat responde localmente com a lista "offline", em rodízio.
        "st_mentora": {
            "name": NOME_ST_MENTORA,
            "portrait": "images/characters/st_mentora/portrait.png",
            "assistant_id": None,
            "desc": _("Head de produto. Te ajuda a transformar queixa em requisito."),
            "offline": [
                _("Oi! Tô no meio de uma call, mas me conta: qual foi a última dúvida que apareceu?"),
                _("Quando alguém disser 'fácil', pergunta: fácil pra fazer o quê?"),
                _("Lembra: um exemplo com número vale mais que três adjetivos."),
                _("Hoje vi a Bia lançando gasto no bandejão. Observar ensina coisa que entrevista não pega."),
                _("Se o Vinícius pedir algo novo, não diga sim nem não ainda. Pergunta o que muda no prazo."),
                _("Tá cansado? Descansar também está no planejamento, viu."),
                _("Critério bom tem dado inicial, ação e resultado. O resto é desejo."),
                _("Valeu por hoje! Amanhã a gente continua, com café."),
            ],
        },
        "st_techlead": {
            "name": NOME_ST_TECHLEAD,
            "portrait": "images/characters/st_techlead/portrait.png",
            "assistant_id": None,
            "desc": _("CTO e cofundador. Arquitetura, dados e segurança."),
            "offline": [
                _("Veja bem: antes de escolher a ferramenta, desenha o caminho do dado."),
                _("Se der para repetir a mesma requisição sem estragar nada, você dormiu tranquilo."),
                _("Dinheiro em float é como medir farinha com régua. Centavo é inteiro."),
                _("Log não é diário. Não escreva nele o que você não mostraria para a Bia."),
                _("Estou revisando um PR. Respondo com calma daqui a pouco."),
                _("Em 2009 derrubei um banco de dados numa sexta. Desde então, não publico na sexta."),
                _("Dado que você não guarda não vaza."),
                _("Bom trabalho hoje. Vai pra casa, o servidor se vira até amanhã."),
            ],
        },
        "st_mobile": {
            "name": NOME_ST_MOBILE,
            "portrait": "images/characters/st_mobile/portrait.png",
            "assistant_id": None,
            "desc": _("Dev mobile. Topa um pair programming a qualquer hora."),
            "offline": [
                _("Fala! Tô esperando o build terminar, pode mandar kkk"),
                _("PR pequeno é PR revisado. PR gigante é PR aprovado sem ler."),
                _("Testei no celular mais barato da loja. Se roda nele, roda em qualquer um."),
                _("Mano, deploy de app não é site. Não dá pra dar F5 no celular de 800 pessoas."),
                _("Escreve o teste do cancelamento antes, confia."),
                _("Sábado tem partida online, se quiser entrar no time."),
                _("Trocadilho do dia: o app tá tão leve que nem pesa no bolso. Desculpa."),
                _("Fechou! Amanhã a gente pareia nisso."),
            ],
        },
        "st_qualidade": {
            "name": NOME_ST_QUALIDADE,
            "portrait": "images/characters/st_qualidade/portrait.png",
            "assistant_id": None,
            "desc": _("Qualidade e pesquisa com usuários. Lê todas as avaliações da loja."),
            "offline": [
                _("Oi! Tô lendo avaliação da loja. Hoje tem 3 novas, uma falando de total errado."),
                _("Primeiro: o que a pessoa tentou fazer. Segundo: o que aconteceu. Terceiro: o que esperava."),
                _("Oxe, 'confuso' não é defeito. Confuso onde, em qual passo?"),
                _("Teste o caminho de cancelar também. Usuário desiste o tempo todo."),
                _("O botão de excluir precisa ter nome para o leitor de tela, não só um ícone."),
                _("Cadê a evidência? Uma avaliação é um sinal; nove é um padrão."),
                _("Mês que vem tem teste de usabilidade com calouros. Quer assistir?"),
                _("Bom descanso! Amanhã eu te mostro o que achei."),
            ],
        },
        "st_ceo": {
            "name": NOME_ST_CEO,
            "portrait": "images/characters/st_ceo/portrait.png",
            "assistant_id": None,
            "desc": _("CEO da Trocado. Sempre com um investidor na outra linha."),
            "offline": [
                _("Fala! Saindo de uma reunião com fundo agora. O que manda?"),
                _("Investidor não quer só número grande. Quer ver gente voltando a usar."),
                _("Open Finance vai ser nosso diferencial. Mas só quando estiver redondo, prometo."),
                _("Se eu estiver pedindo coisa demais, me fala com o impacto. Eu escuto."),
                _("Demo day chegando! Tô ensaiando o pitch no espelho."),
                _("Mil estudantes cadastrados! Mas a Lorena me lembrou da retenção..."),
                _("Eu era bolsista. Esse app é o que eu queria ter tido."),
                _("Valeu, time! Agora vou ligar pro próximo investidor."),
            ],
        },
        "st_estudante": {
            "name": NOME_ST_ESTUDANTE,
            "portrait": "images/characters/st_estudante/portrait.png",
            "assistant_id": None,
            "desc": _("Estudante e beta tester. Anota tudo, até o cafezinho."),
            "offline": [
                _("Oi! Tô entre uma aula e outra, pode falar."),
                _("Hoje lancei o bandejão, R$ 4,50. Apareceu uma vez só. Progresso, né?"),
                _("Égua, recebi um alerta estranho do app. Brincadeira, foi do banco mesmo."),
                _("Antes de pedir meu banco, me mostra que o total está certo."),
                _("Se eu desistir de excluir, o gasto tem que ficar lá. Simples assim."),
                _("Minhas amigas da república perguntaram do app. Disse que tá melhorando."),
                _("Tipo assim: eu só quero saber quanto sobra até a bolsa cair."),
                _("Obrigada por ouvir! Até a próxima."),
            ],
        },
        "co_mentora": {
            "name": NOME_CO_MENTORA,
            "portrait": "images/characters/co_mentora/portrait.png",
            "assistant_id": None,
            "desc": _("Analista sênior de requisitos. Sua mentora no Projeto Farol. Começou atendendo telefone na central."),
            "offline": [
                _("Oi! Tô fechando uma ata aqui. Vamos por partes: o que te deixou com dúvida hoje?"),
                _("Dica de quem começou atendendo telefone: antes de propor solução, pergunta \"quando foi a última vez que isso aconteceu?\"."),
                _("Se a palavra é \"fácil\", \"rápido\" ou \"intuitivo\", ainda não é requisito. Pergunta o que a pessoa precisa conseguir fazer."),
                _("Critério de aceitação bom tem situação inicial, ação e um resultado que alguém consegue conferir."),
                _("A Rosângela parece dura, mas ela protege a equipe dela. Entender isso ajuda na conversa."),
                _("Descansa também. Estágio é maratona de oito semanas, não tiro de cem metros."),
                _("Mudança em produção sem RFC, nem pensar. A Ingrid tem razão em insistir nisso."),
                _("Anotou no notebook? O que não foi registrado a gente esquece até segunda."),
            ],
        },
        "co_legado": {
            "name": NOME_CO_LEGADO,
            "portrait": "images/characters/co_legado/portrait.png",
            "assistant_id": None,
            "desc": _("Desenvolvedor do SGC desde 2008. Sabe onde cada regra nasceu. Caneca de 2008 inclusa."),
            "offline": [
                _("Isso aí tem história. Em 2008 o SGC rodava num servidor que a gente chamava de Tia Neide. Não pergunte."),
                _("Manual de 2011? Lê como curiosidade. Quem manda é o que está rodando no banco."),
                _("Antes de apagar uma regra estranha, descobre por que ela nasceu. Quase sempre foi um incêndio."),
                _("Trigger é aquele código que ninguém lembra que existe até aparecer num relatório."),
                _("Tô tomando café na caneca de 2008. Ela já sobreviveu a três reestruturações."),
                _("Teste de regressão é o jeito educado de dizer \"não confio na minha memória\". E faz bem."),
                _("Se eu me aposentar e ninguém souber das rotinas noturnas do SGC, a culpa é minha. Me cobra."),
                _("Pergunta boba não existe. Existe pergunta que eu respondi em 2012 e esqueci de documentar."),
            ],
        },
        "co_dev": {
            "name": NOME_CO_DEV,
            "portrait": "images/characters/co_dev/portrait.png",
            "assistant_id": None,
            "desc": _("Dev do módulo Farol. Fã de código novo, aprendendo a respeitar o velho. Topa pair a qualquer hora."),
            "offline": [
                _("Bora! Tô com três abas de documentação do Oracle abertas e nenhuma me ajudando kkk"),
                _("Confesso: se dependesse de mim, eu reescrevia o SGC inteiro. O Jorge vive dizendo que não é tão simples."),
                _("Se o teste passou de primeira, desconfia um pouco. Vê se ele testa mesmo o que você acha."),
                _("Validação só na tela não vale. A API tem que recusar também."),
                _("Tô ouvindo lo-fi e lendo PL/SQL. Combinação estranha, mas funciona."),
                _("Me chama pra pair quando quiser. Explicar pra alguém me ajuda a achar meus próprios bugs."),
                _("Camada anticorrupção parece nome de série policial, mas é só um tradutor entre dois sistemas."),
                _("Commit pequeno, mensagem clara. Aprendi do jeito difícil num PR de duas mil linhas."),
            ],
        },
        "co_qualidade": {
            "name": NOME_CO_QUALIDADE,
            "portrait": "images/characters/co_qualidade/portrait.png",
            "assistant_id": None,
            "desc": _("Qualidade, testes e gestão de mudanças. Se não está registrado, não aconteceu."),
            "offline": [
                _("Se não está registrado, não aconteceu. Vale para requisito, teste e mudança."),
                _("RFC sem plano de rollback eu devolvo antes do CAB. Nada pessoal."),
                _("Perfil se testa pelo lado do \"não\": o atendente tenta abrir a auditoria e tem que dar acesso negado."),
                _("Toda vez que acho senha em arquivo de configuração eu respiro fundo. Registra, troca, sem caça às bruxas."),
                _("Mudança emergencial é para restaurar serviço, não para furar fila."),
                _("Tô revisando o plano de testes. Se quiser ver, vem. É menos chato do que parece."),
                _("Dica de inspeção: procura o que falta, o que tem duas leituras e o que briga com outra regra."),
                _("O café da copa hoje tá horrível. Registrado como incidente, prioridade baixa."),
            ],
        },
        "co_supervisora": {
            "name": NOME_CO_SUPERVISORA,
            "portrait": "images/characters/co_supervisora/portrait.png",
            "assistant_id": None,
            "desc": _("Supervisora da central de atendimento. Conhece cada fila do SGC e cada número do SLA."),
            "offline": [
                _("Oi, tudo bem? Tô no pico das nove, respondo direitinho depois."),
                _("Meu indicador é SLA, mas o que me tira o sono é atendente respondendo a mesma pergunta três vezes."),
                _("Se for mexer no fechamento de chamado, me avisa antes. Minha equipe precisa de treinamento."),
                _("Quer entender a central? Senta uma manhã do lado de um atendente. Vale mais que reunião."),
                _("Descrição obrigatória eu aceito, desde que seja curta e tenha modelo pronto para os casos comuns."),
                _("A trilha de auditoria me salvaria uma semana na auditoria interna de 2021. Não deixa isso de lado."),
                _("Se tiver dúvida de regra, pergunta pra mim. Prefiro pergunta agora do que retrabalho depois."),
                _("Bom trabalho hoje. Agora vai descansar, que amanhã tem fila."),
            ],
        },
        "co_solicitante": {
            "name": NOME_CO_SOLICITANTE,
            "portrait": "images/characters/co_solicitante/portrait.png",
            "assistant_id": None,
            "desc": _("Coordenador de manutenção de campo. Abre chamado toda semana e quer saber o que foi feito."),
            "offline": [
                _("Fala! Tô na estrada indo pra uma subestação. Se eu sumir, é falta de sinal."),
                _("Meu problema é simples: quero saber o que fizeram no chamado sem ter que ligar."),
                _("Técnico de campo não abre intranet. Abre o celular. Pensa nisso."),
                _("Quando o chamado diz \"resolvido\" e o problema continua, eu quero poder reabrir."),
                _("Pode me mandar a tela pra eu testar? Prefiro testar do que imaginar."),
                _("Esse negócio de aviso no WhatsApp, se não der agora, me explica o porquê que eu entendo."),
                _("Choveu tanto aqui que a equipe parou. Boa hora pra testar sistema."),
                _("Valeu por ouvir a gente do campo. Normalmente ninguém pergunta."),
            ],
        },
        # Adicione outros se necessário...
    }

    # Ordem de exibição dos contatos da rota saúde. Cada rota tem a sua em
    # ROUTES (data/routes.rpy); a tela usa route_contacts_order().
    CONTACTS_ORDER = [
        "developer_ai",
        "developer_requirements",
        "developer_coding",
        "developer_management",
        "developer_quality",
        "developer_project",
        "developer_security",
        "developer_test",
        "doutora_1",
        "doutora_2",
    ]

    # Inicializa o assistant_id global para uso no backend
    if not hasattr(renpy.store, "current_assistant_id"):
        renpy.store.current_assistant_id = "asst_default"
