# ambiguidade_dados.rpy
# -------------------------------
# DADOS DA CAÇA À AMBIGUIDADE (uma atividade por rota, semana 3)
# -------------------------------
# Conteúdo dos documentos de design de rota (docs/design/intermissoes-*.md,
# seções da caça à ambiguidade). Formato (docs/design/sistemas-intermissoes.md, 5.1):
#   "contexto": de onde veio o requisito;
#   "segmentos": texto corrido; ("vaga", termo, texto) e ("isca", termo, texto)
#       viram botões; o resto é texto comum, não clicável;
#   "iscas": termo -> por que não é vago;
#   "vagas": termo -> {"porque", "opcoes": 3 reescritas, 1 com "adequada": True
#       e 2 distratores com "feedback" (a consequência concreta)};
#   "resultado" (opcional): o requisito reescrito; sem ele, o jogo monta
#       trocando cada vaga pela reescrita adequada entre [[ ]. Colchetes no
#       texto vão como [[ (interpolação do Ren'Py).
# Mecânica: scripts/mechanics/ambiguidade.rpy. init 3: ROUTES nasce em init 1.

init 3 python:
    ROUTES["saude"]["ambiguidades"] = {
        "saude_amb_historico": {
            "contexto": _("Rascunho de requisito montado a partir das anotações da entrevista com as médicas."),
            "segmentos": [
                _("O sistema deve permitir que a médica registre o "),
                ("isca", "historico", _("histórico")),
                _(" do paciente "),
                ("vaga", "rapida", _("de forma rápida")),
                _(" e "),
                ("vaga", "simples", _("simples")),
                _(", e emitir "),
                ("isca", "alertas", _("alertas")),
                _(" "),
                ("vaga", "necessario", _("sempre que necessário")),
                _("."),
            ],
            "iscas": {
                "historico": _("'Histórico de saúde' está definido no UC2: tratamentos em andamento, medicamentos, gravidez, comorbidades. A equipe sabe o que entra."),
                "alertas": _("'Alerta' já tem forma combinada com as médicas: um aviso na tela inicial de quem acompanha o caso. O vago aqui é quando ele aparece, não o que ele é."),
            },
            "vagas": {
                "rapida": {
                    "porque": _("Rápida para quem? Num plantão cheio, 'rápido' muda de sentido. Sem número, o teste não passa nem falha."),
                    "opcoes": [
                        {"texto": _("com a tela abrindo em até 2 s e um retorno sem mudanças registrado em até 3 minutos"), "adequada": True},
                        {"texto": _("o mais rápido possível"), "adequada": False,
                         "feedback": _("Continua sem número. Cada pessoa da equipe para num ponto diferente, e o teste não tem como passar ou falhar.")},
                        {"texto": _("mais rápido que no sistema atual"), "adequada": False,
                         "feedback": _("Ninguém mediu o sistema atual. Sem a medida de antes, a comparação vira opinião na hora da entrega.")},
                    ],
                },
                "simples": {
                    "porque": _("'Simples' é opinião. A Dra. Nathalia já disse o que atrapalha; é isso que precisa estar escrito."),
                    "opcoes": [
                        {"texto": _("com os campos obrigatórios marcados antes de salvar e os dados da visita anterior já preenchidos"), "adequada": True},
                        {"texto": _("com uma interface intuitiva e amigável"), "adequada": False,
                         "feedback": _("Troca uma palavra vaga por duas. Ainda não dá para conferir nada.")},
                        {"texto": _("com no máximo uma tela e poucos campos"), "adequada": False,
                         "feedback": _("Isso já é solução, e pode cortar campos que o atendimento exige, como as escalas. O problema dela não era o número de telas.")},
                    ],
                },
                "necessario": {
                    "porque": _("Necessário segundo quem? Sem dizer o evento e quem recebe, o sistema avisa de tudo ou de nada."),
                    "opcoes": [
                        {"texto": _("para a profissional que acompanha o caso, no mesmo dia em que o paciente faltar à consulta de retorno"), "adequada": True},
                        {"texto": _("a cada alteração no prontuário"), "adequada": False,
                         "feedback": _("Seriam dezenas de avisos por plantão. Aviso demais vira ruído, e a médica passa a ignorar até o importante.")},
                        {"texto": _("quando a médica achar importante"), "adequada": False,
                         "feedback": _("Devolve a decisão para a médica em cada caso. O sistema continua sem saber quando avisar.")},
                    ],
                },
            },
        },
    }

    ROUTES["startup"]["ambiguidades"] = {
        "st_amb_total": {
            "contexto": _("Pedido do Vinícius, copiado do quadro de ideias."),
            "segmentos": [
                _("O app deve mostrar o "), ("isca", "total", _("total do mês")), _(" atualizado "),
                ("vaga", "rapido", _("rapidamente")), _(" e deixar a pessoa excluir "),
                ("isca", "gastos", _("gastos")), _(" "), ("vaga", "facil", _("facilmente")),
                _(", "), ("vaga", "sem_perder", _("sem perder dados")), _("."),
            ],
            "iscas": {
                "total": _("\"Total do mês\" está definido no glossário da Trocado: a soma dos gastos do mês corrente. Dá para conferir com uma conta."),
                "gastos": _("\"Gasto\" é termo do domínio, com campos definidos: valor, data e categoria. Todo mundo na equipe entende a mesma coisa."),
            },
            "vagas": {
                "rapido": {
                    "porque": _("Cada pessoa imagina um tempo diferente, e o celular do Davi não é o da Bia. Sem número, o teste não passa nem falha."),
                    "opcoes": [
                        {"texto": _("em até 2 segundos depois de salvar, em 95% das vezes, num celular de entrada com 4G"), "adequada": True},
                        {"texto": _("o mais rápido possível"), "adequada": False,
                         "feedback": _("Continua sem número. O Davi diz que já está o mais rápido possível, e o teste não tem como discordar.")},
                        {"texto": _("instantaneamente"), "adequada": False,
                         "feedback": _("Promessa impossível de medir e de cumprir no 4G do ônibus. Na primeira demora de meio segundo, o requisito já falhou.")},
                    ],
                },
                "facil": {
                    "porque": _("\"Fácil\" para quem e para fazer o quê? A Bia mostrou que \"fácil\" escondia uma tarefa e um medo: apagar o gasto certo sem querer."),
                    "opcoes": [
                        {"texto": _("a partir do próprio gasto na lista, com uma confirmação que mostra o nome e o valor antes de apagar"), "adequada": True},
                        {"texto": _("de forma intuitiva"), "adequada": False,
                         "feedback": _("Trocou um adjetivo por outro. \"Intuitivo\" também não diz o que a pessoa consegue fazer nem como alguém confere.")},
                        {"texto": _("com um botão grande e colorido"), "adequada": False,
                         "feedback": _("Diz como o botão é, não o que a pessoa consegue fazer. E cor sozinha não ajuda quem usa leitor de tela: a Lorena devolveria o cartão.")},
                    ],
                },
                "sem_perder": {
                    "porque": _("Perder quais dados, em que situação? No túnel, o problema nem foi perder: foi gravar duas vezes. Sem a situação, ninguém sabe o que testar."),
                    "opcoes": [
                        {"texto": _("um gasto salvo sem internet fica guardado no celular, é enviado quando o sinal volta e aparece uma única vez na lista e no total"), "adequada": True},
                        {"texto": _("com segurança total"), "adequada": False,
                         "feedback": _("Segurança contra o quê? Senha, roubo, sinal caindo? Cada pessoa testaria uma coisa diferente, e nenhuma delas é o túnel.")},
                        {"texto": _("com backup diário no servidor"), "adequada": False,
                         "feedback": _("O backup da madrugada não salva o bandejão lançado no túnel há cinco minutos. Resolve outro problema e deixa este igual.")},
                    ],
                },
            },
            "resultado": _("O app deve mostrar o total do mês atualizado {b}[[em até 2 segundos depois de salvar, em 95% das vezes, num celular de entrada com 4G]{/b} e deixar a pessoa excluir gastos {b}[[a partir do próprio gasto na lista, com uma confirmação que mostra o nome e o valor antes de apagar]{/b}; {b}[[um gasto salvo sem internet fica guardado no celular, é enviado quando o sinal volta e aparece uma única vez na lista e no total]{/b}."),
        },
    }

    ROUTES["corporativo"]["ambiguidades"] = {
        "co_amb_termo": {
            "contexto": _("Termo de abertura do Projeto Farol, escrito pela diretoria em janeiro."),
            "segmentos": [
                _("A consulta deve ser "), ("vaga", "rapida", _("rápida")),
                _(" e mostrar informações "), ("vaga", "completas", _("completas")),
                _(" do "), ("isca", "chamado", _("chamado")),
                _("; o atendente deve descrever a "), ("isca", "solucao", _("solução")),
                _(" "), ("vaga", "adequadamente", _("adequadamente")), _("."),
            ],
            "iscas": {
                "chamado": _("'Chamado' é termo do domínio: um pedido registrado no SGC, com número, como o 48213."),
                "solucao": _("'Solução' é o nome de um campo do SGC. Todo atendente sabe onde ele fica."),
            },
            "vagas": {
                "rapida": {
                    "porque": _("Cada pessoa imagina um tempo diferente. No pico das 9h, 'rápida' para a diretoria pode ser lenta para a central."),
                    "opcoes": [
                        {"texto": _("responder em até 3 s para 95% das consultas, com 1.500 usuários simultâneos no pico das 9h"), "adequada": True},
                        {"texto": _("ser o mais rápida possível"), "adequada": False,
                         "feedback": _("Continua sem número. Nenhum teste consegue reprovar 'o mais rápida possível'.")},
                        {"texto": _("ser mais rápida que o SGC"), "adequada": False,
                         "feedback": _("O SGC leva de 2 a 40 s, conforme a hora. Mais rápida que qual medida? Com 39 s ela já cumpriria.")},
                    ],
                },
                "completas": {
                    "porque": _("'Completas' não diz quais campos. Cada pessoa completa a lista do seu jeito."),
                    "opcoes": [
                        {"texto": _("mostrar o estado, o atendente responsável, a data da última mudança e a solução registrada"), "adequada": True},
                        {"texto": _("mostrar todas as informações"), "adequada": False,
                         "feedback": _("'Todas' inclui telefone, endereço de subestação e notas internas. O UC01 acabou de dizer que isso precisa de proteção.")},
                        {"texto": _("mostrar as informações que o solicitante precisar"), "adequada": False,
                         "feedback": _("Cada solicitante precisa de uma coisa. A lista continua aberta e ninguém sabe quando a tela está pronta.")},
                    ],
                },
                "adequadamente": {
                    "porque": _("Ninguém consegue conferir se uma descrição foi 'adequada'. Dois atendentes caprichosos escrevem coisas opostas."),
                    "opcoes": [
                        {"texto": _("em texto curto que diga o que foi feito, usando um modelo pronto quando houver, antes de mudar o chamado para Resolvido"), "adequada": True},
                        {"texto": _("com capricho e atenção"), "adequada": False,
                         "feedback": _("Capricho não se testa. O chamado 48213 também foi fechado por alguém caprichoso.")},
                        {"texto": _("com pelo menos 200 caracteres"), "adequada": False,
                         "feedback": _("Agora tem número, mas ele mede tamanho, não conteúdo. A Rosângela aceitou descrição curta; 200 caracteres estoura o TMA e vira texto de enchimento.")},
                    ],
                },
            },
            # "rápida" troca junto com o "ser": a reescrita é um verbo.
            "resultado": _("A consulta deve {b}[[responder em até 3 s para 95% das consultas, com 1.500 usuários simultâneos no pico das 9h]{/b} e mostrar {b}[[o estado, o atendente responsável, a data da última mudança e a solução registrada]{/b} do chamado; o atendente deve descrever a solução {b}[[em texto curto que diga o que foi feito, usando um modelo pronto quando houver, antes de mudar o chamado para Resolvido]{/b}."),
        },
    }
