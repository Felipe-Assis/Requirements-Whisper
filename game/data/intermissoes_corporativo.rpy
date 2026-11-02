# intermissoes_corporativo.rpy
# -------------------------------
# TEMPO LIVRE DA ROTA CORPORATIVO: locais, agenda, pistas, extras e mentoria
# -------------------------------
# Só dados (docs/design/intermissoes-corporativo.md, seções 1.3, 3, 4 e 5). O
# motor está em logic/intermissao.rpy; o formato de cada chave está descrito
# no topo daquele arquivo. Todos os locais ficam na torre do Grupo Vértice
# (um lugar só no mapa da cidade). Falas ficam nos labels de conteúdo
# (im_corporativo_s<N>_<acao>_<alvo>, im_corporativo_<acao>_<alvo>,
# im_corporativo_mentoria_<k>, im_corporativo_abertura_<N>); sem eles, o motor
# usa uma fala genérica.

init 3 python:
    ROUTES["corporativo"]["mapa"] = {
        "musica": "music_office_relaxed",
        "inicio": "baia",
        # Lugar da cidade que aparece na rota, mas sempre fechado (focável para
        # ler o motivo) e quem pode aparecer "longe" num balão acinzentado
        # quando não está na agenda da semana (docs/design/mapa-cidade.md 2.3).
        "lugares_fechados": {"subestacao": _("Área restrita: só equipe de campo")},
        "longe": {"co_solicitante": ("subestacao", "celular", _("em campo, sem sinal"))},
        "pois": [
            {"id": "baia", "nome": _("Baia do Farol"), "lugar": "torre_vertice", "sub": _("12º andar · baia do Farol"),
             "bg": "escritorio_interior_tarde",
             "bg_semana": {8: "escritorio_interior_noite"}, "abre": 1, "acoes": [], "icone": "programando"},
            {"id": "central", "nome": _("Central de atendimento"), "lugar": "torre_vertice", "sub": _("3º andar · central de atendimento"),
             "bg": "central_atendimento_tarde",
             "abre": 1, "acoes": ["observar"], "icone": "atendendo"},
            {"id": "cafe", "nome": _("Café do térreo"), "lugar": "torre_vertice", "sub": _("térreo · café"),
             "bg": "empresa_cafe_tarde",
             "abre": 1, "acoes": ["descansar"], "icone": "cafe"},
            {"id": "refeitorio", "nome": _("Refeitório"), "lugar": "torre_vertice", "sub": _("2º andar · refeitório"),
             "bg": "refeitorio_tarde",
             "abre": 1, "acoes": ["descansar"], "icone": "conversando"},
            {"id": "arquivo", "nome": _("Sala do arquivo"), "lugar": "torre_vertice", "sub": _("subsolo · arquivo"),
             "bg": "sala_arquivo_tarde",
             "abre": 1, "acoes": ["estudar"], "icone": "estudando"},
            {"id": "sala_cab", "nome": _("Sala do CAB"), "lugar": "torre_vertice", "sub": _("15º andar · sala do CAB"),
             "bg": "sala_reunioes_tarde",
             "abre": 5, "acoes": [], "icone": "reuniao"},
            {"id": "servidores", "nome": _("Sala de servidores"), "lugar": "torre_vertice", "sub": _("subsolo · servidores"),
             "bg": "sala_servidores",
             "abre": 7, "acoes": [], "icone": "computador"},
        ],
    }

    # "atividade" (opcional, por semana): {cid: (icone, frase curta)} para os
    # balões do mapa. Sem ela, o balão usa o ícone do local. Frases: E5.
    ROUTES["corporativo"]["intermissoes"] = {
        1: {"dia": _("Sexta"), "inicio": (15, 0), "bloco": 120, "mesmo_dia": False,
            "agenda": {"baia": ["co_dev"], "central": ["co_supervisora"], "cafe": ["co_mentora"],
                       "arquivo": ["co_legado"]},
            "fechados": {}, "ajudar": {"co_dev": None},
            "observar": {"central": "co_p_ligacoes"}, "estudar": "co_extra_itil",
            "atividade": {}},
        2: {"dia": _("Sexta"), "inicio": (16, 30), "bloco": 180, "mesmo_dia": True,
            "agenda": {"baia": ["co_dev", "co_qualidade"], "central": ["co_supervisora"],
                       "cafe": ["co_solicitante"], "refeitorio": ["co_mentora"], "arquivo": ["co_legado"]},
            "fechados": {}, "ajudar": {},
            "observar": {"central": "co_p_vazio"}, "estudar": "co_extra_reversa",
            "atividade": {}},
        3: {"dia": _("Sexta"), "inicio": (15, 0), "bloco": 180, "mesmo_dia": False,
            "agenda": {"baia": ["co_mentora"], "central": ["co_supervisora", "co_solicitante"],
                       "cafe": ["co_dev"], "refeitorio": ["co_qualidade"], "arquivo": ["co_legado"]},
            "fechados": {}, "ajudar": {},
            "observar": {"central": None}, "estudar": "co_extra_casos_uso",
            "atividade": {}},
        4: {"dia": _("Sexta"), "inicio": (13, 0), "bloco": 180, "mesmo_dia": False,
            "agenda": {"baia": ["co_legado"], "central": ["co_supervisora"],
                       "cafe": ["co_mentora", "co_qualidade"], "refeitorio": ["co_dev"]},
            "fechados": {}, "ajudar": {},
            "observar": {"central": None}, "estudar": "co_extra_anticorrupcao",
            "atividade": {}},
        5: {"dia": _("Sexta"), "inicio": (15, 0), "bloco": 180, "mesmo_dia": False,
            "agenda": {"baia": ["co_dev"], "central": ["co_supervisora", "co_solicitante"],
                       "cafe": ["co_mentora"], "arquivo": ["co_legado"], "sala_cab": ["co_qualidade"]},
            "fechados": {}, "ajudar": {"co_qualidade": "co_p_botao"},
            "observar": {"central": None}, "estudar": "co_extra_rfc",
            "atividade": {}},
        6: {"dia": _("Sexta"), "inicio": (15, 0), "bloco": 180, "mesmo_dia": False,
            "agenda": {"baia": ["co_dev", "co_mentora"], "central": ["co_supervisora"],
                       "cafe": ["co_solicitante"], "arquivo": ["co_legado"], "sala_cab": ["co_qualidade"]},
            "fechados": {}, "ajudar": {"co_dev": "co_p_senha", "co_qualidade": "co_p_botao"},
            "observar": {"central": None}, "estudar": "co_extra_caracterizacao",
            "atividade": {}},
        7: {"dia": _("Quinta"), "inicio": (14, 0), "bloco": 180, "mesmo_dia": False,
            "agenda": {"baia": ["co_dev"], "central": ["co_supervisora"], "cafe": ["co_mentora"],
                       "refeitorio": ["co_solicitante"], "arquivo": ["co_legado"],
                       "servidores": ["co_qualidade"]},
            "fechados": {}, "ajudar": {"co_qualidade": "co_p_parada"},
            "observar": {"central": None}, "estudar": "co_extra_parada",
            "atividade": {}},
        8: {"dia": _("Sexta"), "inicio": (18, 0), "bloco": 180, "mesmo_dia": False,
            "agenda": {"baia": ["co_dev", "co_qualidade"], "cafe": ["co_mentora"], "arquivo": ["co_legado"]},
            "fechados": {"refeitorio": _("Fechado depois das 18h"),
                         "servidores": _("Reservada para a janela (abre às 23h30)")},
            "ajudar": {}, "observar": {"central": None}, "estudar": None,
            "atividade": {}},
    }

    ROUTES["corporativo"]["pistas"] = {
        "co_p_ligacoes": {"titulo": _("Três ligações em vinte minutos"),
            "texto": _("Na central, o Paulo atendeu três ligações de 'e o meu chamado?' em vinte minutos. Para cada uma, abriu quatro abas. Depois de cada ligação, fez um risquinho num post-it: 'só para eu saber quantas são'."),
            "ate_semana": 1, "uso": _("Semana 2: a entrevista com Rosângela e Edson.")},
        "co_p_vazio": {"titulo": _("Três espaços no campo Solução"),
            "texto": _("No fim do turno, uma atendente fechou um chamado digitando três espaços no campo Solução. O SGC aceitou e marcou Resolvido."),
            "ate_semana": 2, "uso": _("Semana 3: o caso limite da história do Edson.")},
        "co_p_acentos": {"titulo": _("A troca de codificação de 2014"),
            "texto": _("Em 2014 o banco do SGC saiu da Tia Neide para o Oracle novo e trocou de codificação. Textos antigos ainda guardam acentos de outro padrão: 'manutenção' aparece como 'manutenÃ§Ã£o' em relatórios velhos."),
            "ate_semana": 4, "uso": _("Semana 5: o risco da carga do histórico.")},
        "co_p_norte": {"titulo": _("A hora do Norte"),
            "texto": _("Desde a migração de 2014, a rotina das 72 h grava o fechamento no horário de Brasília. No relatório das filiais do Norte, os chamados de senha parecem levar 73 h. A supervisora de Manaus reclamou em 2015; ninguém registrou."),
            "ate_semana": 5, "uso": _("Semana 6: o teste de caracterização que falha.")},
        "co_p_botao": {"titulo": _("O botão que só sumiu"),
            "texto": _("Na homologação do SGC, com o perfil atendente, o botão Reabrir não aparecia num chamado de outro setor. Colando o endereço da ação no navegador, a reabertura funcionou."),
            "ate_semana": 6, "uso": _("Semana 7: os testes de perfil.")},
        "co_p_senha": {"titulo": _("A linha provisória do build"),
            "texto": _("No script de build da integração, uma linha carrega o arquivo de configuração do usuário de serviço do SGC, com o comentário 'senha provisória - 2012'. Você e o Kauã não abriram o arquivo e registraram para verificar com a Ingrid."),
            "ate_semana": 6, "uso": _("Semana 7: o caso da senha no repositório.")},
        "co_p_parada": {"titulo": _("Quanto tempo leva para voltar"),
            "texto": _("No ensaio de quinta, desfazer a janela inteira pelo backup levou 40 min. Reverter só a carga do histórico levou 6 min e não mexeu no resto."),
            "ate_semana": 7, "uso": _("Semana 8: a decisão na janela.")},
    }

    ROUTES["corporativo"]["extras"] = [
        {"id": "co_extra_itil", "title": _("Incidente, problema e mudança"),
         "text": _("Incidente: algo parou e precisa voltar agora (a VPN do técnico caiu). Problema: a causa por trás de um ou mais incidentes, investigada com calma (por que a VPN cai toda segunda?). Mudança: alteração planejada em produção, com RFC, janela e plano de volta. Primeiro se restaura o serviço; depois se procura a causa, para evitar o próximo incidente. Mudança padrão é pré-aprovada; normal passa pelo CAB; emergencial é só para restaurar serviço.")},
        {"id": "co_extra_reversa", "title": _("Engenharia reversa de um banco"),
         "text": _("Para entender um banco sem documentação: conte registros por estado e por ano; procure gatilhos e rotinas agendadas, que mudam dados sem ninguém clicar; leia as restrições (chaves, campos obrigatórios), que mostram regras que o código não conta; compare datas, porque picos e valores estranhos costumam marcar uma mudança antiga. Anote cada achado com a fonte e confirme com quem usa.")},
        {"id": "co_extra_casos_uso", "title": _("Caso de uso ou história?"),
         "text": _("História de usuário cabe num cartão: quem, o quê e para quê. Ela abre a conversa e se fecha com critérios de aceitação. Caso de uso descreve o diálogo entre ator e sistema passo a passo, com fluxo principal, alternativos e exceções (SGC fora do ar, chamado de outra pessoa). Use história para priorizar e conversar; use caso de uso quando o fluxo tem muitos desvios ou depende de outro sistema. Os dois convivem: o UC01 detalha a história do Edson.")},
        {"id": "co_extra_anticorrupcao", "title": _("Camada anticorrupção"),
         "text": _("Quando um sistema novo conversa com um antigo, um tradutor no meio impede que o modelo velho contamine o novo. No Farol, a camada recebe o código de estado do SGC e entrega 'Resolvido'; recebe texto com acentos de 2008 e entrega texto legível. Regras: o Farol não lê tabela do SGC direto; toda tradução tem teste; se o SGC mudar, só a camada muda. É também o lugar certo para validar o que entra, como a descrição vazia vinda da integração.")},
        {"id": "co_extra_rfc", "title": _("Anatomia de uma RFC"),
         "text": _("Uma RFC responde: o que muda e o que não muda; por quê; impacto (quem usa, quais tabelas, o que para se falhar); quando (janela); como foi testado (regressão, ensaio); como voltar (plano de rollback com tempo estimado e critério de parada); quem responde por cada passo e quem fica de plantão. Diz também se a mudança é padrão, normal ou emergencial. O CAB não aprova intenção, aprova evidência.")},
        {"id": "co_extra_caracterizacao", "title": _("Teste de caracterização"),
         "text": _("Teste de caracterização registra o que o código faz hoje, certo ou errado. Escolha uma entrada real, rode o código, copie a saída para a verificação e dê ao teste o nome do comportamento ('rotina das 72 h fecha sem descrição'). Se o comportamento atual é um defeito, o teste o documenta e um registro de problema guarda a correção para depois, com RFC. A suíte vira uma rede: qualquer mudança que altere o comportamento acende um teste antes de chegar à central.")},
        {"id": "co_extra_parada", "title": _("Critério de parada"),
         "text": _("Critério de parada é a condição, combinada antes da janela, que manda voltar. Bom critério é medível ('zero registro corrompido'), tem dono (quem decide), tem hora limite (até quando dá para tentar) e diz qual passo volta (só a carga ou a janela toda). Saber quanto tempo cada volta leva faz parte do plano. Depois, registre: incidente se algo parou; problema se há causa a investigar.")},
    ]

    ROUTES["corporativo"]["mentoria"] = {
        "id": "co_mentoria_causos",
        "titulo": _("Causos do SGC"),
        "mentor": "co_legado",
        "conquista": "mentoria_conq_corporativo",
        "passos": [
            {"n": 1, "semana_min": 2, "pista": None, "resumo": _("A caneca de 2008 e o servidor Tia Neide")},
            {"n": 2, "semana_min": 3, "pista": "co_p_acentos", "resumo": _("A troca de codificação de 2014")},
            {"n": 3, "semana_min": 4, "pista": "co_p_norte", "resumo": _("O fuso do Norte")},
            {"n": 4, "semana_min": 5, "pista": None, "resumo": _("O primeiro causo gravado no wiki")},
            {"n": 5, "semana_min": 6, "pista": None, "resumo": _("O mapa dos causos")},
        ],
    }

    ROUTES["corporativo"]["conquistas_extra"] = [
        {"id": "mentoria_conq_corporativo", "var": "mentoria_conq_corporativo",
         "title": _("Causos Registrados"),
         "desc": _("Concluiu os cinco encontros com o Jorge.")},
    ]
