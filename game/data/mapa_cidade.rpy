# mapa_cidade.rpy
# -------------------------------
# MAPA DA CIDADE: lugares, bairros, deslocamento e transições
# -------------------------------
# Um mapa só para as três rotas (cidade fictícia inspirada no Rio). Valores de
# docs/design/mapa-cidade.md (seções 2, 4 e 6.3). Cada rota liga os seus
# locais de intermissão (POIs, em data/intermissoes_<rota>.rpy) a um destes
# lugares pelo campo "lugar"; vários POIs no mesmo lugar são salas do mesmo
# prédio (0 min de deslocamento).
#
# Só dados: a tela (scripts/mechanics/mapa_screen.rpy) e o motor
# (logic/intermissao.rpy) leem daqui. Imagens que ainda não existem não
# quebram nada: a tela desenha um retângulo com o nome do lugar.
#
# Coordenadas na base do mapa (MAPA_CIDADE["tamanho"], 2560x1440, mostrada a
# 1920x1080). "ancora" = ponto do chão no meio da base do sprite; "largura" =
# largura do sprite na base.

init python:

    MAPA_CIDADE = {
        "base": "images/mapa/cidade_base.png",
        "tamanho": (2560, 1440),
        "voce": "images/mapa/voce.png",
        "pasta_icones": "images/mapa/icones/",
        "pasta_lugares": "images/mapa/lugares/",
        # Fundo da tela de transição de cada meio: images/bg/transicao_<meio>.png
        "pasta_transicoes": "images/bg/transicao_",
    }

    # "pos" só serve para escrever o nome do bairro no mapa provisório.
    MAPA_BAIRROS = {
        "laranjeiras": {"nome": _("Laranjeiras"), "pos": (620, 930)},
        "botafogo": {"nome": _("Botafogo"), "pos": (1150, 1380)},
        "aterro": {"nome": _("Aterro"), "pos": (1420, 960)},
        "centro": {"nome": _("Centro"), "pos": (1180, 690)},
        "cais_mare": {"nome": _("Cais da Maré"), "pos": (1590, 560)},
        "cidade_universitaria": {"nome": _("Cidade Universitária"), "pos": (2140, 300)},
        "caju": {"nome": _("Caju"), "pos": (1380, 360)},
    }

    # balao: lado preferido do balão (acima, abaixo, direita, esquerda);
    # voce: lado do marcador "Você"; interno: meio da troca de sala dentro do
    # lugar (None = só um dissolve); predio: toca a porta ao chegar.
    MAPA_LUGARES = {
        "republica": {"nome": _("República das Amendoeiras"), "bairro": "laranjeiras",
                      "ancora": (620, 800), "largura": 220, "balao": "acima", "voce": "esquerda",
                      "interno": None, "predio": True},
        "predio_projeto": {"nome": _("Prédio da equipe (Polo de Tecnologia)"), "bairro": "cidade_universitaria",
                           "ancora": (1960, 600), "largura": 330, "balao": "acima", "voce": "esquerda",
                           "interno": None, "predio": True},
        "praca_campus": {"nome": _("Praça das Palmeiras"), "bairro": "cidade_universitaria",
                         "ancora": (2160, 700), "largura": 250, "balao": "abaixo", "voce": "esquerda",
                         "interno": None, "predio": False},
        "instituto": {"nome": _("Instituto (ambulatório)"), "bairro": "cidade_universitaria",
                      "ancora": (2360, 580), "largura": 310, "balao": "acima", "voce": "esquerda",
                      "interno": None, "predio": True},
        "bandejao": {"nome": _("Bandejão da universidade"), "bairro": "cidade_universitaria",
                     "ancora": (2140, 900), "largura": 290, "balao": "abaixo", "voce": "esquerda",
                     "interno": None, "predio": True},
        "casarao": {"nome": _("Casarão amarelo (Trocado)"), "bairro": "botafogo",
                    "ancora": (1000, 1090), "largura": 330, "balao": "acima", "voce": "esquerda",
                    "interno": "escada", "predio": True},
        "cafe_esquina": {"nome": _("Café da esquina"), "bairro": "botafogo",
                         "ancora": (1225, 1120), "largura": 170, "balao": "direita", "voce": "abaixo",
                         "interno": None, "predio": True},
        "orla": {"nome": _("Orla de Botafogo"), "bairro": "botafogo",
                 "ancora": (1440, 1260), "largura": 280, "balao": "direita", "voce": "esquerda",
                 "interno": None, "predio": False},
        "aterro": {"nome": _("Parque do Aterro"), "bairro": "aterro",
                   "ancora": (1420, 860), "largura": 300, "balao": "direita", "voce": "esquerda",
                   "interno": None, "predio": False},
        "torre_vertice": {"nome": _("Torre do Grupo Vértice"), "bairro": "centro",
                          "ancora": (1180, 600), "largura": 270, "balao": "esquerda", "voce": "direita",
                          "interno": "elevador", "predio": True},
        "aceleradora": {"nome": _("Aceleradora Maré"), "bairro": "cais_mare",
                        "ancora": (1590, 470), "largura": 320, "balao": "direita", "voce": "esquerda",
                        "interno": None, "predio": True},
        "subestacao": {"nome": _("Subestação Caju"), "bairro": "caju",
                       "ancora": (1380, 270), "largura": 260, "balao": "direita", "voce": "esquerda",
                       "interno": None, "predio": False},
    }

    # Lugar da casa: destino de "Ir para casa" (encerra o tempo livre).
    MAPA_CASA = "republica"

    # Minutos e meio entre bairros (sem ordem no par). Mesmo bairro: 10 min a
    # pé (no campus, meio "campus").
    MAPA_TRAJETOS = {
        ("laranjeiras", "botafogo"): (15, "onibus"),
        ("laranjeiras", "aterro"): (15, "onibus"),
        ("laranjeiras", "centro"): (20, "metro"),
        ("laranjeiras", "cais_mare"): (25, "metro"),
        ("laranjeiras", "cidade_universitaria"): (40, "onibus"),
        ("laranjeiras", "caju"): (35, "onibus"),
        ("botafogo", "aterro"): (15, "calcada"),
        ("botafogo", "centro"): (20, "metro"),
        ("botafogo", "cais_mare"): (25, "metro"),
        ("botafogo", "cidade_universitaria"): (30, "onibus"),
        ("botafogo", "caju"): (40, "onibus"),
        ("aterro", "centro"): (15, "calcada"),
        ("aterro", "cais_mare"): (20, "onibus"),
        ("aterro", "cidade_universitaria"): (35, "onibus"),
        ("aterro", "caju"): (30, "onibus"),
        ("centro", "cais_mare"): (15, "calcada"),
        ("centro", "cidade_universitaria"): (30, "onibus"),
        ("centro", "caju"): (20, "onibus"),
        ("cais_mare", "cidade_universitaria"): (25, "onibus"),
        ("cais_mare", "caju"): (15, "onibus"),
        ("cidade_universitaria", "caju"): (20, "onibus"),
    }
    MAPA_MINUTOS_BAIRRO = 10
    MAPA_MEIO_BAIRRO = {"cidade_universitaria": "campus"}   # os outros: "calcada"
    # Exceções entre dois lugares (sem ordem no par).
    MAPA_TRAJETOS_LUGAR = {
        ("cafe_esquina", "casarao"): (0, "escada"),
    }

    # Tela de transição por meio. "fundo": bg que já existe e serve até a arte
    # images/bg/transicao_<meio>.png chegar. Metrô e elevador ainda não têm
    # som próprio: metrô usa o ônibus a 60%; elevador, o ambiente de reunião.
    MAPA_MEIOS = {
        "onibus": {"nome": _("Ônibus"), "fundo": "transito_tarde",
                   "som": "audio/effects/bus.ogg", "volume": 1.0},
        "metro": {"nome": _("Metrô"), "fundo": "transito_tarde",
                  "som": "audio/effects/bus.ogg", "volume": 0.6},
        "calcada": {"nome": _("A pé"), "fundo": "transito_tarde",
                    "som": "audio/effects/passos.ogg", "volume": 1.0},
        "campus": {"nome": _("A pé pelo campus"), "fundo": "fachada_instituto_tarde",
                   "som": "audio/effects/steps.ogg", "volume": 1.0},
        "elevador": {"nome": _("Elevador"), "fundo": "escritorio_interior_vazio",
                     "som": "audio/effects/ambiente_reuniao.ogg", "volume": 1.0},
        "escada": {"nome": _("Escada do casarão"), "fundo": "startup_coworking_tarde",
                   "som": "audio/effects/passos.ogg", "volume": 1.0},
    }
    MAPA_SOM_CAFE = "audio/effects/xicara_cafe.ogg"
    MAPA_SOM_PORTA = "audio/effects/abrindo_porta.ogg"
    MAPA_SOM_NOVO_LUGAR = "audio/effects/cell_vibration.ogg"

    # Duração (s) da caminhada do marcador e da tela de transição por minutos
    # de trajeto: (até N min, segundos).
    MAPA_TEMPO_MARCADOR = 1.0
    MAPA_TEMPO_TRANSICAO = [(0, 1.0), (10, 1.5), (25, 1.8), (999, 2.0)]
    # Com "Transições: desligadas": cartão de texto curto.
    MAPA_TEMPO_CARTAO = 1.0

    # Atividades dos balões: id -> (rótulo, arquivo do ícone em
    # pasta_icones). "atendendo" e "computador" reaproveitam ícones.
    MAPA_ATIVIDADES = {
        "programando": (_("programando"), "programando"),
        "reuniao": (_("em reunião"), "reuniao"),
        "cafe": (_("tomando café"), "cafe"),
        "conversando": (_("conversando"), "conversando"),
        "descansando": (_("descansando"), "descansando"),
        "observando": (_("observando usuários"), "observando"),
        "atendendo": (_("atendendo"), "observando"),
        "estudando": (_("estudando"), "estudando"),
        "celular": (_("no celular"), "celular"),
        "computador": (_("no computador"), "celular"),
    }

    # Ícone das ações no painel (reaproveita os de atividade).
    MAPA_ICONE_ACAO = {
        "conversar": "conversando", "observar": "observando", "estudar": "estudando",
        "descansar": "descansando", "ajudar": "celular", "mentoria": "reuniao",
    }
