# Design de conteúdo: intermissões da rota Corporativo

Data: 2026-11-02. Branch `evolucao`. Etapa E1 (conteúdo da rota), para uso na E5 (escrita), E6 (ambiguidade e
rastreabilidade) e E3 (arte do mapa).

Segue `docs/design/sistemas-intermissoes.md` (abreviado aqui como **SIS**): mesmos nomes, formatos, custos, agenda,
pistas, extras, arco de mentoria e pontos de gancho. Fontes da rota: `docs/rotas/corporativo.md` (bíblia) e as cenas em
`game/story/rota_corporativo/`. Este documento não altera nenhum `.rpy`.

Escopo do usuário: jogo educacional para aula e para jogar sozinho, completo do início ao fim. Nada que é preciso para
aprender fica só no tempo livre: os 8 registros, as 21 decisões, a escrita livre, o planejamento, a negociação, a caça
à ambiguidade e a rastreabilidade continuam nas cenas. Uma intermissão nunca chama `registrar`, `co_registrar`,
`decisao`, `co_acerto`, `co_erro`, `exercicio_escrita`, `atividade_planejamento`, `amb_atividade` ou `rast_atividade`.

---

## 0. Resumo e ajustes em relação ao SIS

**Resumo**
- Mapa: corte ilustrado da torre do Grupo Vértice, com 7 locais (5 desde a semana 1, Sala do CAB na 5 e Sala de
  servidores na 7). O SIS fixa 7 locais para esta rota; o pedido de "5 a 6" fica atendido nos 5 iniciais + 2 que abrem.
- 8 intermissões, com 43 conversas, 8 observações, 5 ajudas, 7 estudos, 2 descansos e 5 encontros de mentoria.
- 7 pistas, todas com uso marcado em cena (seção 3). 7 registros extras (seção 4).
- Mentoria "Causos do SGC" com o Jorge, 5 encontros (seção 5).
- Caça à ambiguidade na `co_09` (seção 6). Rastreabilidade na `co_16`, com o bug na `co_17` (seção 7).
- Energia: 3 eventos de cena e 6 falas alternativas (seção 8).

**Ajustes, com motivo** (o SIS pede motivo registrado para qualquer mudança)
1. **Texto da pista `co_p_parada`.** O SIS resume como "o rollback da carga levou 40 min". A `co_18` já diz que a
   reversão da carga leva seis minutos. Texto adotado: desfazer a janela inteira pelo backup levou 40 min; reverter só a
   carga levou 6 min. Assim a pista continua sendo evidência para a decisão 21 e não contradiz a cena.
2. **Evento de energia da `co_15`.** O SIS dá −2 e hora extra de 30 min a todos. Na cena, uma das três respostas é "Vou
   descansar; tenho prova na quinta", e o jogador não vai ao ensaio. Adotado: −2 e hora extra 30 para quem fica no
   ensaio; −1 para quem revisa o rollback com o Jorge; 0 para quem vai descansar. A linha entra dentro de cada opção do
   menu, porque a cena não guarda a escolha numa variável.
3. **Locais fechados na semana 8** (sexta à noite): Refeitório ("Fechado depois das 18h") e Sala de servidores
   ("Reservada para a janela, abre às 23h30"). O SIS permite `fechados` com motivo; ninguém da agenda está neles.
4. **Observar na central nas semanas 1 a 7** dá amizade +0,5 à Rosângela. Os atendentes observados (Paulo, Neusa) não
   têm id de amizade; a Rosângela autoriza e acompanha a observação. Na semana 8 (turno da noite) não há amizade.
5. **Rastreabilidade:** o quadro tem um teste isca que nenhum critério usa (`T6`, que só confere se o botão some) e um
   campo opcional `"explica"` por critério para o feedback "(confira)". Os dois são pedidos para a E6; o formato do
   SIS aceita listas de testes livres, e a explicação por linha já está prevista no texto do SIS.
6. **Fundo à noite na semana 8:** a Baia do Farol usa `escritorio_interior_noite`. Usar o mesmo mecanismo que a E4
   adotar para a mesa da Startup na semana 6 (troca de fundo por semana).

---

## 1. Mapa e locais

### 1.1 Imagem do mapa (`images/mapas/corporativo.png`, para a E3)

**Conceito:** a torre do Grupo Vértice em corte, como uma maquete aberta. O jogador vê os andares onde a rota acontece,
um sobre o outro, e entende de relance que o arquivo e os servidores ficam no subsolo e a diretoria lá em cima.

**Descrição para gerar a base** (estilo C dos fundos: paleta suave, leve textura de papel, traço limpo e escuro, luz
contida, perspectiva precisa, sem texto, figurantes de costas e sem rosto; anexar `docs/arte/referencias/estilo-c-escritorio.png`):

> Corte ilustrado de uma torre de escritórios de vidro no Centro do Rio de Janeiro, vista em três quartos e levemente
> de cima, como uma maquete aberta: a fachada frontal foi removida e mostra seis andares empilhados. De baixo para cima:
> subsolo com duas salas lado a lado (à esquerda um corredor de racks escuros com pequenas luzes azuis e verdes e um rack
> bege antigo no canto; à direita uma sala de estantes de aço com caixas-arquivo e uma janela basculante alta no nível da
> calçada); térreo com porta giratória, um café com balcão de madeira clara, banquetas e plantas; segundo andar inteiro
> de refeitório com mesas compridas e janelas para a baía; terceiro andar inteiro de central de atendimento com fileiras
> de baias baixas azul-acinzentadas, headsets e um painel de TV com barras sem texto; uma faixa de corte em zigue-zague
> indica os andares omitidos; décimo segundo andar com baias de trabalho, monitores duplos, um quadro com post-its e um
> calendário grande na parede; outra faixa de corte; décimo quinto andar com uma sala de reunião envidraçada, mesa
> comprida e um calendário de parede. Ao fundo, o Centro do Rio no fim da tarde: céu laranja-rosado suave, a Baía de
> Guanabara à direita com o Pão de Açúcar pequeno e enevoado, prédios vizinhos simplificados em tons frios. Paleta:
> azul-acinzentado, areia, verde-musgo das plantas, laranja de fim de tarde nas janelas. Cada andar com piso de tom
> suave diferente para leitura rápida. Figurantes minúsculos de costas. Sem letreiros, sem números de andar, sem logotipos.

- Tamanho de geração: 2304x1296 (16:9 com sobra, como pede o SIS 7.2). A tela reduz para a área do mapa.
- Deixar uma área calma (parede ou céu) logo acima de cada local para o botão e o rótulo da tela.
- Coordenadas `pos` abaixo estão na imagem reduzida para 1920x1080. A E2 converte para a área de 2/3 da tela.
- Compatibilidade com o mapa da cidade (plano de evolução, seção "Mapa da cidade"): se a E2 adotar a cidade única, a
  torre vira um sprite de lugar ("Torres do Centro") e este corte vira a vista de dentro, com a transição do elevador.

### 1.2 Locais

Ícones: 96x96 RGBA, legíveis a 48 px, traço limpo escuro de 2 a 3 px, preenchimento chapado em 2 tons suaves, leve
textura de papel, fundo transparente, sem texto. A forma muda de um para outro (a tela não depende só da cor).

| id | Nome | Fundo da cena | `pos` | Abre | Ações do local |
|---|---|---|---|---|---|
| `baia` | Baia do Farol | `escritorio_interior_tarde` (noite na S8) | (820, 300) | 1 | — |
| `central` | Central de atendimento | `central_atendimento_tarde` | (760, 560) | 1 | observar |
| `cafe` | Café do térreo | `empresa_cafe_tarde` | (700, 830) | 1 | descansar |
| `refeitorio` | Refeitório | `refeitorio_tarde` | (1160, 690) | 1 | descansar |
| `arquivo` | Sala do arquivo | `sala_arquivo_tarde` | (1130, 960) | 1 | estudar |
| `sala_cab` | Sala do CAB | `sala_reunioes_tarde` | (1180, 170) | 5 | — |
| `servidores` | Sala de servidores | `sala_servidores` | (720, 985) | 7 | — |

**Baia do Farol** (`baia`, 12º andar, abre na semana 1)
- No mapa: canto do andar aberto com quatro mesas juntas; dois monitores por mesa, um notebook prateado com adesivos
  coloridos, uma caneca branca com faixa azul, um caderno vinho, um quadro branco com colunas de post-its e o calendário
  de mudanças na parede. Luz de fim de tarde entrando de lado.
- Ícone: um monitor visto de frente com uma caneca de faixa azul ao lado.

**Central de atendimento** (`central`, 3º andar, abre na semana 1)
- No mapa: o andar inteiro com fileiras de baias de divisória baixa azul-acinzentada, headsets apoiados nas mesas,
  atendentes de costas, um painel de TV grande com barras de fila (sem números legíveis), persianas meio abertas e
  plantas nas pontas das fileiras.
- Ícone: um headset de call center com o microfone curvo.

**Café do térreo** (`cafe`, térreo, abre na semana 1)
- No mapa: ao lado da porta giratória, balcão de madeira clara, máquina de café, banquetas, duas mesinhas redondas na
  calçada interna e uma vitrine pequena de loja de presentes (as canecas da `co_14` saem daqui).
- Ícone: uma xícara com três linhas curvas de vapor.

**Refeitório** (`refeitorio`, 2º andar, abre na semana 1)
- No mapa: andar com mesas compridas, bandejas empilhadas, um balcão de pratos quentes e janelas largas para a baía.
  Poucas pessoas à tarde.
- Ícone: uma bandeja vista de cima com prato e talheres.

**Sala do arquivo** (`arquivo`, subsolo, abre na semana 1)
- No mapa: estantes de aço com caixas-arquivo e fichários de lombadas coloridas, uma mesa com documentos encadernados em
  espiral, um monitor de tubo velho no canto e um feixe de luz laranja com poeira entrando pela janela basculante alta.
- Ícone: uma caixa-arquivo com uma etiqueta em branco e uma alça recortada.

**Sala do CAB** (`sala_cab`, 15º andar, abre na semana 5)
- No mapa: sala de reunião envidraçada com mesa comprida, cadeiras iguais, um projetor desligado e um calendário de
  parede grande com alguns dias marcados por círculos. Persianas abaixadas pela metade.
- Ícone: uma folha de calendário com um selo redondo de visto (check) no canto.
- Estado nas semanas 1 a 4: "Abre na semana 5". Motivo na história: o jogador só entra na rotina do CAB a partir da
  `co_15`.

**Sala de servidores** (`servidores`, subsolo, abre na semana 7)
- No mapa: corredor estreito de racks pretos com LEDs azuis e verdes, piso elevado de placas perfuradas e, no canto, o
  rack bege antigo da Tia Neide com uma etiqueta de papel amarelada (sem texto legível). Mesa dobrável com notebook.
- Ícone: um rack visto de frente, com três fileiras de pontinhos de luz.
- Estado nas semanas 1 a 6: "Abre na semana 7". Na semana 8: "Reservada para a janela (abre às 23h30)".

### 1.3 Dados (`game/data/intermissoes/corporativo.rpy`, `init 3 python`)

```python
init 3 python:
    ROUTES["corporativo"]["mapa"] = {
        "imagem": "images/mapas/corporativo.png",   # opcional; sem ela, grade de cartões
        "musica": "music_office_relaxed",
        "pois": [
            {"id": "baia", "nome": _("Baia do Farol"), "bg": "escritorio_interior_tarde",
             "pos": (820, 300), "abre": 1, "acoes": []},
            {"id": "central", "nome": _("Central de atendimento"), "bg": "central_atendimento_tarde",
             "pos": (760, 560), "abre": 1, "acoes": ["observar"]},
            {"id": "cafe", "nome": _("Café do térreo"), "bg": "empresa_cafe_tarde",
             "pos": (700, 830), "abre": 1, "acoes": ["descansar"]},
            {"id": "refeitorio", "nome": _("Refeitório"), "bg": "refeitorio_tarde",
             "pos": (1160, 690), "abre": 1, "acoes": ["descansar"]},
            {"id": "arquivo", "nome": _("Sala do arquivo"), "bg": "sala_arquivo_tarde",
             "pos": (1130, 960), "abre": 1, "acoes": ["estudar"]},
            {"id": "sala_cab", "nome": _("Sala do CAB"), "bg": "sala_reunioes_tarde",
             "pos": (1180, 170), "abre": 5, "acoes": []},
            {"id": "servidores", "nome": _("Sala de servidores"), "bg": "sala_servidores",
             "pos": (720, 985), "abre": 7, "acoes": []},
        ],
    }

    ROUTES["corporativo"]["intermissoes"] = {
        1: {"dia": _("Sexta"), "inicio": (15, 0), "bloco": 120, "mesmo_dia": False,
            "agenda": {"baia": ["co_dev"], "central": ["co_supervisora"], "cafe": ["co_mentora"],
                       "arquivo": ["co_legado"]},
            "fechados": {}, "ajudar": {"co_dev": None},
            "observar": {"central": "co_p_ligacoes"}, "estudar": "co_extra_itil"},
        2: {"dia": _("Sexta"), "inicio": (16, 30), "bloco": 180, "mesmo_dia": True,
            "agenda": {"baia": ["co_dev", "co_qualidade"], "central": ["co_supervisora"],
                       "cafe": ["co_solicitante"], "refeitorio": ["co_mentora"], "arquivo": ["co_legado"]},
            "fechados": {}, "ajudar": {},
            "observar": {"central": "co_p_vazio"}, "estudar": "co_extra_reversa"},
        3: {"dia": _("Sexta"), "inicio": (15, 0), "bloco": 180, "mesmo_dia": False,
            "agenda": {"baia": ["co_mentora"], "central": ["co_supervisora", "co_solicitante"],
                       "cafe": ["co_dev"], "refeitorio": ["co_qualidade"], "arquivo": ["co_legado"]},
            "fechados": {}, "ajudar": {},
            "observar": {"central": None}, "estudar": "co_extra_casos_uso"},
        4: {"dia": _("Sexta"), "inicio": (13, 0), "bloco": 180, "mesmo_dia": False,
            "agenda": {"baia": ["co_legado"], "central": ["co_supervisora"],
                       "cafe": ["co_mentora", "co_qualidade"], "refeitorio": ["co_dev"]},
            "fechados": {}, "ajudar": {},
            "observar": {"central": None}, "estudar": "co_extra_anticorrupcao"},
        5: {"dia": _("Sexta"), "inicio": (15, 0), "bloco": 180, "mesmo_dia": False,
            "agenda": {"baia": ["co_dev"], "central": ["co_supervisora", "co_solicitante"],
                       "cafe": ["co_mentora"], "arquivo": ["co_legado"], "sala_cab": ["co_qualidade"]},
            "fechados": {}, "ajudar": {"co_qualidade": "co_p_botao"},
            "observar": {"central": None}, "estudar": "co_extra_rfc"},
        6: {"dia": _("Sexta"), "inicio": (15, 0), "bloco": 180, "mesmo_dia": False,
            "agenda": {"baia": ["co_dev", "co_mentora"], "central": ["co_supervisora"],
                       "cafe": ["co_solicitante"], "arquivo": ["co_legado"], "sala_cab": ["co_qualidade"]},
            "fechados": {}, "ajudar": {"co_dev": "co_p_senha", "co_qualidade": "co_p_botao"},
            "observar": {"central": None}, "estudar": "co_extra_caracterizacao"},
        7: {"dia": _("Quinta"), "inicio": (14, 0), "bloco": 180, "mesmo_dia": False,
            "agenda": {"baia": ["co_dev"], "central": ["co_supervisora"], "cafe": ["co_mentora"],
                       "refeitorio": ["co_solicitante"], "arquivo": ["co_legado"],
                       "servidores": ["co_qualidade"]},
            "fechados": {}, "ajudar": {"co_qualidade": "co_p_parada"},
            "observar": {"central": None}, "estudar": "co_extra_parada"},
        8: {"dia": _("Sexta"), "inicio": (18, 0), "bloco": 180, "mesmo_dia": False,
            "agenda": {"baia": ["co_dev", "co_qualidade"], "cafe": ["co_mentora"], "arquivo": ["co_legado"]},
            "fechados": {"refeitorio": _("Fechado depois das 18h"),
                         "servidores": _("Reservada para a janela (abre às 23h30)")},
            "ajudar": {}, "observar": {"central": None}, "estudar": None},
    }
```

Conferência com `im_validar_dados`: todas as pessoas estão em `route_contact_ids()`; nenhum local fechado tem pessoa;
`ate_semana` de cada pista ≥ semana de origem; o maior fim é 21h (S8); o Jorge (mentor) está na agenda das semanas 2 a 8.

---

## 2. As 8 intermissões

### 2.0 Cadeia e ganchos

`game/story/rota_corporativo/rota_corporativo.rpy` fica assim (linhas novas marcadas):

```renpy
label rota_corporativo:
    call co_01_chegada from _co_01_chegada
    call co_02_ciclo_legado from _co_02_ciclo_legado
    call im_intermissao(1) from _im_corporativo_s1          # novo
    call co_03_casa_sem1 from _co_03_casa_sem1
    call im_ponto_parada(1) from _pp_corporativo_s1         # novo
    call co_04_preparacao from _co_04_preparacao
    call co_05_entrevista from _co_05_entrevista
    call co_06_avaliacao from _co_06_avaliacao
    call co_07_cafe from _co_07_cafe
    call im_intermissao(2) from _im_corporativo_s2          # novo
    call co_08_casa_sem2 from _co_08_casa_sem2
    call im_ponto_parada(2) from _pp_corporativo_s2         # novo
    call co_09_historias from _co_09_historias
    call co_10_almoco from _co_10_almoco
    call co_11_inspecao from _co_11_inspecao
    call im_intermissao(3) from _im_corporativo_s3          # novo
    call co_12_casa_sem3 from _co_12_casa_sem3
    call im_ponto_parada(3) from _pp_corporativo_s3         # novo
    call co_13_arquitetura from _co_13_arquitetura
    call im_intermissao(4) from _im_corporativo_s4          # novo
    call co_14_comemoracao from _co_14_comemoracao
    call im_ponto_parada(4) from _pp_corporativo_s4         # novo
    call co_15_gestao from _co_15_gestao                    # gancho B da S5 dentro da cena
    call im_ponto_parada(5) from _pp_corporativo_s5         # novo
    call co_16_codificacao from _co_16_codificacao          # gancho B da S6
    call im_ponto_parada(6) from _pp_corporativo_s6         # novo
    call co_17_testes_seguranca from _co_17_testes_seguranca  # gancho B da S7
    call im_ponto_parada(7) from _pp_corporativo_s7         # novo
    call im_intermissao(8) from _im_corporativo_s8          # novo
    call co_18_implantacao_avaliacao from _co_18_implantacao_avaliacao
    return
```

Ganchos B (âncora por texto, como pede o SIS):
- `co_15_gestao.rpy`: depois de `"{i}Na sexta, [NOME_CO_QUALIDADE] lê a RFC de ponta a ponta e devolve com dois comentários pequenos. Nenhum sobre o plano de volta.{/i}"` e antes de `scene black`: `call im_intermissao(5) from _im_corporativo_s5`.
- `co_16_codificacao.rpy`: depois de `hide co_legado` / `hide co_dev` / `with dissolve` que seguem `co_legado "Chamava de coragem até a primeira sexta-feira à noite."` e antes de `scene black`: `call im_intermissao(6) from _im_corporativo_s6`.
- `co_17_testes_seguranca.rpy`: depois de `hide co_qualidade` / `hide co_dev` / `with dissolve` que seguem os dois `co_conceder` e antes de `scene black`: `call im_intermissao(7) from _im_corporativo_s7`.

Nenhum `set_time` das cenas precisa mudar (conferido com os horários de cada cena):

| Sem. | Cena antes | Fim dela | Bloco | Cena depois | Começa |
|---|---|---|---|---|---|
| 1 | `co_02` (segunda) | 17h30 | sexta 15h–17h | `co_03` | sexta 19h30 |
| 2 | `co_07` (sexta) | 16h15 | sexta 16h30–19h30 (`mesmo_dia`) | `co_08` | sexta 20h |
| 3 | `co_11` (quinta) | 18h30 | sexta 15h–18h | `co_12` | sexta 19h |
| 4 | `co_13` (terça) | 17h | sexta 13h–16h | `co_14` | sexta 16h |
| 5 | `co_15` (quarta 22h30, texto da sexta) | — | sexta 15h–18h | cartão da semana 5 | — |
| 6 | `co_16` (quarta) | 16h30 | sexta 15h–18h | cartão da semana 6 | — |
| 7 | `co_17` (quinta) | 11h40 | quinta 14h–17h | cartão da semana 7 | — |
| 8 | `co_17` (cartão) | — | sexta 18h–21h | `co_18` | sexta 23h30 |

### 2.1 Conteúdos que valem para todas as semanas

**Tutorial da semana 1** (`im_abertura(1)`, guia: Valéria). Seis falas:
1. "Sexta à tarde a torre fica mais calma. Até as cinco, o tempo é seu."
2. "Vamos por partes. No mapa, cada lugar mostra quem está lá e o que dá para fazer. Cada ação diz quanto tempo custa."
3. "Não cabe tudo. Escolher o que fica de fora também é planejamento. Você vai ver isso de novo no projeto."
4. "A energia aparece embaixo do relógio. Ajudar e estudar cansam. Descansar recupera."
5. "Se você observar alguém usando o sistema de verdade, pode sair com uma pista. Ela volta numa conversa mais adiante."
6. "E nada aqui é obrigatório para aprender. O que o projeto precisa acontece no trabalho. Aqui é o seu tempo."

**Abertura com energia baixa** (semanas 2 a 8, testa `energia_estado()`), uma fala da Valéria antes do mapa:
- Cansaço: "Você está com cara de semana longa. Hoje o tempo livre é mais curto. Se eu fosse você, começava pelo café do térreo."
- Exaustão: "Vamos por partes, e a primeira parte é sentar. Hoje dá para pouca coisa, e tudo bem."

**Descansar** (valem para todas as semanas; 60 min; +2 de energia; 3 a 6 falas; meta 70 palavras cada):
- `im_corporativo_descansar_cafe`: você pega um café coado no balcão e senta perto da porta giratória. Por quinze
  minutos ninguém fala de SLA; dá para ver o Centro passando lá fora. Com `energia_cansaco()`: você quase cochila na
  banqueta e o atendente do café deixa um copo d'água sem perguntar nada.
- `im_corporativo_descansar_refeitorio`: o refeitório vazio da tarde, a baía pela janela, um chá de máquina. Você não
  abre o notebook. Com `energia_cansaco()`: você deita a cabeça nos braços por dez minutos; ninguém repara.

**Observar** só gera pista nas semanas 1 e 2 (SIS 2.2). Nas outras, é cena curta que aprofunda a central e prepara
algo da história. Toda observação na central nas semanas 1 a 7 dá +0,5 à Rosângela (ajuste 4).

**Estudar** acontece sempre na Sala do arquivo e termina no registro extra da semana (o texto está na seção 4; a
recompensa é aplicada por `im_executar`, nunca pelo conteúdo).

Convenção de labels (SIS 1.6): `im_corporativo_s<N>_<acao>_<alvo>`; mentoria `im_corporativo_mentoria_<k>`.
Metas de palavras seguem o SIS 1.6: conversar 8–14 falas (≈130 palavras), observar 15–25 (≈200–300), estudar 6–10
(≈120), ajudar 15–25 (≈300), mentoria 20–30 (≈420).

---

### 2.2 Semana 1 · Sexta, 15h às 17h · 120 min (tutorial)

- **Gancho:** A, entre `co_02_ciclo_legado` e `co_03_casa_sem1` (seção 2.0).
- **Contexto:** o jogador conheceu a equipe e o SGC na segunda. A entrevista com Rosângela e Edson será na quarta da
  semana 2. Ninguém tem pressa numa sexta à tarde.
- **Para a aula:** ver o problema do chamado sem registro do lado de quem atende (observação como técnica de elicitação).

| baia | central | café | refeitório | arquivo | sala_cab | servidores |
|---|---|---|---|---|---|---|
| **Kauã** (ajuda, sem pista) | Rosângela | Valéria | ninguém | Jorge | abre na S5 | abre na S7 |

**Baia do Farol**
- *Conversar com Kauã* · 30 min · amizade +0,5 · `im_corporativo_s1_conversar_co_dev` · 130 palavras.
  Kauã está de fone, lendo sobre IA para prever pico de chamados. Mostra os adesivos do notebook e confessa que
  reescreveria o SGC inteiro "num fim de semana bem dormido". Pergunta o que o jogador achou da Tia Neide.
  Fala-chave: Kauã "Bora! Senta aí. Se o Jorge perguntar, eu estava lendo documentação do Oracle."
- *Ajudar Kauã* · 90 min · −2 energia · amizade +1,0 · sem pista · `im_corporativo_s1_ajudar_co_dev` · 300 palavras.
  Kauã monta o ambiente de desenvolvimento na máquina nova do jogador. Os dois instalam tudo em pair: ele mostra a
  pasta do Farol, nova e com testes, e a pasta `sgc-ponte`, onde "mora o mistério". O jogador faz perguntas em voz alta
  e Kauã acha um passo da instalação que ele mesmo tinha esquecido de anotar no wiki.
  Fala-chave: Kauã "Pair é isso: um digita, o outro pergunta. Quem pergunta acha os bugs."

**Central de atendimento**
- *Conversar com Rosângela* · 30 min · amizade +0,5 · `im_corporativo_s1_conversar_co_supervisora` · 120 palavras.
  Primeira troca rápida, de pé, ao lado do painel de filas. Ela sabe que vem gente da TI conversar na quarta e pede
  pergunta boa. Cita o TMA de cabeça. Não há `add_contact` aqui: o contato continua nascendo na `co_05`.
  Fala-chave: Rosângela "Quarta a gente conversa direito. Traz pergunta, não traz solução pronta."
- *Observar o uso* · 90 min · −1 energia · pista `co_p_ligacoes` · amizade +0,5 Rosângela ·
  `im_corporativo_s1_observar_central` · 300 palavras.
  A Rosângela deixa o jogador sentar ao lado do atendente Paulo. Em vinte minutos entram três ligações de "e o meu
  chamado?". Para cada uma, Paulo troca de aba quatro vezes; numa delas não acha resposta e promete retornar. Depois de
  cada ligação, ele faz um risquinho num post-it colado no monitor: "só para eu saber quantas são".
  Fala-chave: Paulo "Três. E ainda nem deu quatro horas."

**Café do térreo**
- *Conversar com Valéria* · 30 min · amizade +0,5 · `im_corporativo_s1_conversar_co_mentora` · 130 palavras.
  Valéria pergunta o que deixou o jogador com dúvida na semana e responde com outra pergunta. Diz que está separando
  uns chamados reais para lerem juntos na segunda (a mensagem da `co_03` confirma à noite). Sugere a apostila velha de
  ITIL que está no arquivo.
  Fala-chave: Valéria "Vamos por partes. Primeiro, o que você viu. Depois, o que você acha."
- *Descansar* · 60 min · +2 energia · `im_corporativo_descansar_cafe`.

**Refeitório**
- *Descansar* · 60 min · +2 energia · `im_corporativo_descansar_refeitorio`.

**Sala do arquivo**
- *Conversar com Jorge* · 30 min · amizade +0,5 · `im_corporativo_s1_conversar_co_legado` · 130 palavras.
  Jorge procura uma caixa de CDs com a etiqueta "Renova 2016", a reescrita cancelada. Não acha e diz que é melhor
  assim. O jogador pergunta da Tia Neide e ouve a mesma resposta da segunda: só com crachá definitivo.
  Fala-chave: Jorge "Isso aí tem história. E caixa perdida também é história."
- *Estudar* · 60 min · −1 energia · registro extra `co_extra_itil` · `im_corporativo_s1_estudar_arquivo` · 120 palavras.
  Na estante, a apostila do treinamento interno de ITIL de 2012, com anotações a lápis na margem ("isso aqui vale",
  "isso aqui ninguém faz"). O jogador lê o capítulo de incidente, problema e mudança e compara com o caso do Wellington
  que ainda vai ouvir.

Combinações que cabem em 120 min: observar + conversar; ajudar + conversar; estudar + descansar; quatro conversas.

---

### 2.3 Semana 2 · Sexta, 16h30 às 19h30 · 180 min

- **Gancho:** A, entre `co_07_cafe` e `co_08_casa_sem2`. `mesmo_dia` verdadeiro: a `co_07` termina às 16h15.
- **Contexto:** semana da arqueologia do SGC, da entrevista (18% das ligações) e da classificação. No café de agora há
  pouco, Kauã e Jorge discutiram reescrever ou conviver. Na semana 3 vêm história de usuário, critério e inspeção.
- **Para a aula:** caso limite visto no uso real (descrição só com espaços).

| baia | central | café | refeitório | arquivo | sala_cab | servidores |
|---|---|---|---|---|---|---|
| Kauã, Ingrid | Rosângela | Edson | Valéria | Jorge ★ | abre na S5 | abre na S7 |

**Baia do Farol**
- *Conversar com Kauã* · 30 min · `im_corporativo_s2_conversar_co_dev` · 130 palavras.
  Kauã está montando o meme do comentário "NAO MEXER - JT 2010" numa moldura dourada (é a foto que ele manda às 20h na
  `co_08`). Pede opinião sobre a moldura. Conta que gosta de legado porque "todo arquivo tem um mistério".
  Fala-chave: Kauã "Patrimônio tombado. Vou pedir para a Ingrid registrar como ativo."
- *Conversar com Ingrid* · 30 min · `im_corporativo_s2_conversar_co_qualidade` · 130 palavras.
  Ingrid passa a limpo o quadro de quatro colunas da quinta. Explica por que registra até os desejos: o que fica fora
  hoje volta na próxima rodada com nome. Conta a história da tatuagem de check no pulso, com uma piada de checklist.
  Fala-chave: Ingrid "Desejo também é registro. Só não tem data."

**Central de atendimento**
- *Conversar com Rosângela* · 30 min · `im_corporativo_s2_conversar_co_supervisora` · 120 palavras.
  O número da entrevista não saiu da cabeça dela: puxou o relatório do ano passado e deu 17%. Pergunta, desconfiada,
  quanto tempo a descrição vai custar por chamado. Já trata o jogador pelo nome.
  Fala-chave: Rosângela "Dezoito este ano, dezessete no passado. Isso não é acaso, é rotina."
- *Observar o uso* · 90 min · −1 energia · pista `co_p_vazio` · amizade +0,5 Rosângela ·
  `im_corporativo_s2_observar_central` · 300 palavras.
  Troca de turno, fila cheia. Uma atendente no fim do turno fecha um chamado de VPN digitando três espaços no campo
  Solução; o SGC aceita e marca Resolvido. A Rosângela vê, suspira e não dá bronca: liga o caso ao TMA e ao cansaço do
  fim de turno. Pede ao jogador que não anote o nome da atendente em lugar nenhum.
  Fala-chave: Rosângela "Fim de turno. É disso que eu falava. Ninguém aqui é preguiçoso; a fila é que não acaba."

**Café do térreo**
- *Conversar com Edson* · 30 min · `im_corporativo_s2_conversar_co_solicitante` · 130 palavras.
  Edson veio deixar o notebook do Wellington na TI e aproveita o café. Conta de uma subestação alagada na Baixada.
  Pergunta quando vai ver "uma tela de verdade" e lembra que prefere testar a imaginar.
  Fala-chave: Edson "Fala! Se for para testar, me chama. Se for para imaginar, chama a diretoria."
- *Descansar* · `im_corporativo_descansar_cafe`.

**Refeitório**
- *Conversar com Valéria* · 30 min · `im_corporativo_s2_conversar_co_mentora` · 130 palavras.
  Lanche da tarde, pão de queijo. Valéria pergunta o que mais surpreendeu o jogador na semana e ouve sem corrigir.
  Antecipa a segunda-feira: transformar o episódio do Edson numa frase que a equipe inteira entenda igual.
  Fala-chave: Valéria "Segunda a gente transforma conversa em especificação. Hoje, só come."
- *Descansar* · `im_corporativo_descansar_refeitorio`.

**Sala do arquivo**
- *Mentoria com Jorge (encontro 1 se for o próximo)* · 90 min · −1 energia · seção 5.
- *Conversar com Jorge* · 30 min · `im_corporativo_s2_conversar_co_legado` · 120 palavras.
  Jorge volta ao assunto do café: a figueira mata-pau. Diz que viu a reescrita de 2016 morrer de "regra que ninguém
  escreveu" e que hoje fica feliz quando alguém pergunta antes de apagar.
  Fala-chave: Jorge "Regra estranha quase sempre foi um incêndio. Pergunta antes de apagar o fogo velho."
- *Estudar* · `co_extra_reversa` · `im_corporativo_s2_estudar_arquivo` · 120 palavras.
  O jogador acha um mapa do banco desenhado à mão pelo Jorge em 2010, com setas a caneta e uma lista de gatilhos
  ("triggers") com datas. Compara com a busca de rotinas que fizeram na segunda.

---

### 2.4 Semana 3 · Sexta, 15h às 18h · 180 min

- **Gancho:** A, entre `co_11_inspecao` e `co_12_casa_sem3`.
- **Contexto:** história, casos de uso, critério e caça à ambiguidade (segunda); almoço (terça); inspeção e escrita
  livre (quinta, até 18h30, −1 de energia). Na semana 4 vêm arquitetura e os 25 anos do Jorge.
- **Para a aula:** ver o outro lado do chamado (Edson na central) e a origem histórica dos dados.

| baia | central | café | refeitório | arquivo | sala_cab | servidores |
|---|---|---|---|---|---|---|
| Valéria | Rosângela, Edson | Kauã | Ingrid | Jorge ★ | abre na S5 | abre na S7 |

**Baia do Farol**
- *Conversar com Valéria* · `im_corporativo_s3_conversar_co_mentora` · 150 palavras.
  Valéria comenta a inspeção. Com `co_escrita_status == "rascunho"`, ela leu o texto sobre reabrir chamado e diz que o
  Edson vai dizer se entende o mesmo. Com "pendente", lembra que pendência registrada não se perde. Antecipa a terça:
  reunião de arquitetura, "e o Kauã vai chegar com slide".
  Fala-chave: Valéria "Ninguém escreve requisito bom sozinho. A gente escreve, o outro lê, a gente reescreve."

**Central de atendimento**
- *Conversar com Rosângela* · `im_corporativo_s3_conversar_co_supervisora` · 130 palavras.
  Ela decidiu pelo chat, na quinta, que a rotina das 72 h continua com descrição padrão. Conta que pensou nisso a
  noite inteira e que a equipe vai precisar de treinamento curto.
  Fala-chave: Rosângela "Decidi rápido, mas não decidi sozinha. Perguntaram para mim. Isso é raro."
- *Conversar com Edson* · `im_corporativo_s3_conversar_co_solicitante` · 130 palavras.
  O Kauã mandou o print do protótipo. Edson repassou ao Wellington, que perguntou onde fica o botão de reabrir. Edson
  acha graça: a primeira dúvida do técnico foi justamente a da escrita livre.
  Fala-chave: Edson "O Wellington olhou dois segundos e perguntou: e se não resolver de novo?"
- *Observar o uso* (só cena) · amizade +0,5 Rosângela · `im_corporativo_s3_observar_central` · 220 palavras.
  Edson senta pela primeira vez do lado de dentro, ao lado da Rosângela, e ouve um atendente explicar a mesma correção
  de VPN pela terceira vez no dia. Ele fica quieto um bom tempo. Na saída, os dois combinam de se ligar menos e
  escrever mais.
  Fala-chave: Edson "Então é isso que acontece quando eu ligo. Eu só via o meu lado."

**Café do térreo**
- *Conversar com Kauã* · `im_corporativo_s3_conversar_co_dev` · 130 palavras.
  Kauã ensaia os slides de microsserviços para terça e mostra o primeiro, "A Grande Virada". Pergunta, meio rindo, se
  o Jorge vai acabar com ele. O jogador não decide nada aqui; a decisão de arquitetura é da `co_13`.
  Fala-chave: Kauã "Slide bonito eu tenho. Resposta para o Jorge eu não tenho."
- *Descansar* · `im_corporativo_descansar_cafe`.

**Refeitório**
- *Conversar com Ingrid* · `im_corporativo_s3_conversar_co_qualidade` · 130 palavras.
  Ingrid ri do "chatbot com avatar 3D" cortado na inspeção. Explica a fama de "chata do CAB": desde 2019 prefere
  incomodar na quinta a ver alguém trabalhando no sábado por causa de uma mudança mal planejada.
  Fala-chave: Ingrid "Chata na quinta, para ninguém chorar no sábado. É o meu acordo comigo mesma."
- *Descansar* · `im_corporativo_descansar_refeitorio`.

**Sala do arquivo**
- *Mentoria com Jorge* · seção 5 (o encontro 2 dá `co_p_acentos` até a S4).
- *Conversar com Jorge* · `im_corporativo_s3_conversar_co_legado` · 140 palavras.
  Com `get_friendship_point("co_legado") >= 4` (é o combinado de meia hora da `co_10`): Jorge abre o PL/SQL da
  `TRG_FECHA_SENHA_72H`, quarenta linhas e um comentário "greve - JT 03/2013". Sem esse nível: ele está escaneando
  uma foto do lançamento de 2008 (a mesma que manda à noite na `co_12`) e diz "depois te mando".
  Fala-chave: Jorge "O código conta metade. A outra metade eu conto, enquanto lembro."
- *Estudar* · `co_extra_casos_uso` · `im_corporativo_s3_estudar_arquivo` · 120 palavras.
  O jogador compara o UC01 de segunda com uma pasta de "casos de uso do SGC" de 2008, cheia de passos que nunca foram
  implementados. Anota quando cada formato ajuda.

---

### 2.5 Semana 4 · Sexta, 13h às 16h · 180 min

- **Gancho:** A, entre `co_13_arquitetura` e `co_14_comemoracao`. A surpresa do Jorge começa às 16h e ninguém sabe dos
  25 anos ainda (a Valéria descobre na intranet na `co_14`). O Jorge sai às 15h45 para a reunião na diretoria.
- **Contexto:** terça teve arquitetura de transição, trilha de auditoria e a negociação do WhatsApp. Na semana 5 vêm
  capacidade, CAB e o risco da carga.
- **Para a aula:** problema conhecido sem registro (fuso do Norte) e por que traduzir dados entre sistemas.

| baia | central | café | refeitório | arquivo | sala_cab | servidores |
|---|---|---|---|---|---|---|
| Jorge ★ | Rosângela | Valéria, Ingrid | Kauã | ninguém | abre na S5 | abre na S7 |

**Baia do Farol**
- *Mentoria com Jorge* · seção 5 (o encontro 3 dá `co_p_norte` até a S5). Nesta semana acontece na baia.
- *Conversar com Jorge* · `im_corporativo_s4_conversar_co_legado` · 130 palavras.
  Jorge imprime "uma papelada do RH, coisa chata" e vira a folha quando o jogador chega. Comenta a reunião de terça com
  bom humor: "a figueira ganhou nome técnico". Não fala de aposentadoria; o anúncio é da `co_14`.
  Fala-chave: Jorge "Às quatro tenho diretoria. Se eu não voltar, a Tia Neide herda a caneca."

**Central de atendimento**
- *Conversar com Rosângela* · `im_corporativo_s4_conversar_co_supervisora` · 130 palavras.
  Ela soube da trilha de auditoria decidida na terça e mostra a planilha de 2021 que ainda guarda: catorze abas para
  explicar chamado fechado. Pede que a trilha seja fácil de ler por quem não é da TI.
  Fala-chave: Rosângela "Catorze abas. Se essa trilha funcionar, eu apago essa planilha com prazer."
- *Observar o uso* (só cena) · amizade +0,5 Rosângela · `im_corporativo_s4_observar_central` · 200 palavras.
  Hora do almoço, meia equipe. A Neusa cobre duas filas e a Rosângela remaneja gente olhando o relógio de pulso. O
  jogador vê como uma escala curta muda o TMA na hora.
  Fala-chave: Rosângela "Meio-dia é quando o SLA mostra quem planejou e quem torceu."

**Café do térreo**
- *Conversar com Valéria* · `im_corporativo_s4_conversar_co_mentora` · 140 palavras.
  Lê `co_negociacao_opcao`: "base_primeiro", o Edson mandou um joinha e já pergunta da próxima rodada;
  "investigar_agora", o Kauã marcou conversa com o jurídico. Ela conta como aprendeu a mostrar impacto em vez de dizer
  não, ainda na central.
  Fala-chave: Valéria "Quem diz só 'não cabe' perde a conversa. Quem mostra o que sai para caber, ganha um acordo."
- *Conversar com Ingrid* · `im_corporativo_s4_conversar_co_qualidade` · 130 palavras.
  Ingrid já abriu o modelo de RFC do Farol e preencheu só o título. Diz que a semana que vem é "de calendário" e que o
  CAB lê primeiro o plano de volta.
  Fala-chave: Ingrid "RFC é como mala de viagem. Você descobre o que esqueceu quando já está longe."
- *Descansar* · `im_corporativo_descansar_cafe`.

**Refeitório**
- *Conversar com Kauã* · `im_corporativo_s4_conversar_co_dev` · 130 palavras.
  Almoço atrasado. Kauã ainda sente falta da reescrita, mas repete a frase que ouviu na terça sobre destino e caminho.
  Com "investigar_agora", lê a documentação da API oficial do WhatsApp no celular.
  Fala-chave: Kauã "Perdi a reescrita, ganhei um tradutor. Camada anticorrupção parece nome de série policial."
- *Descansar* · `im_corporativo_descansar_refeitorio`.

**Sala do arquivo** (sem ninguém)
- *Estudar* · `co_extra_anticorrupcao` · `im_corporativo_s4_estudar_arquivo` · 120 palavras.
  O jogador encontra a impressão do diagrama de terça esquecida na mesa e um relatório de 2014 com códigos de estado
  numéricos. Escreve, para cada código, a tradução que o Farol mostraria.

---

### 2.6 Semana 5 · Sexta, 15h às 18h · 180 min

- **Gancho:** B, dentro da `co_15` (seção 2.0). Se o jogador ficou no ensaio de quarta, o bloco perde 30 min
  (hora extra, seção 8).
- **Contexto:** capacidade (2 de 4), RFC para o CAB, risco da carga e ensaio com 2,7% de acentos quebrados. Na
  semana 6 vêm caracterização e revisão de pull request.
- **Para a aula:** permissão que só esconde o botão (prepara a semana 7).

| baia | central | café | refeitório | arquivo | sala_cab | servidores |
|---|---|---|---|---|---|---|
| Kauã | Rosângela, Edson | Valéria | ninguém | Jorge ★ | **Ingrid** (`co_p_botao`) | abre na S7 |

**Baia do Farol**
- *Conversar com Kauã* · `im_corporativo_s5_conversar_co_dev` · 130 palavras.
  Kauã escreveu o script da carga e ainda pensa nos 2,7%. Conta das três vezes que a primeira RFC dele voltou.
  Fala-chave: Kauã "Achei que era bug meu. Era bug de 2014. Mesmo assim, o script é meu."

**Central de atendimento**
- *Conversar com Rosângela* · `im_corporativo_s5_conversar_co_supervisora` · 130 palavras.
  Ela e a Neusa rascunham os modelos de descrição (senha, VPN, notebook). Pede ao jogador que leia um em voz alta e
  cronometra: se passar de vinte segundos, reescreve.
  Fala-chave: Rosângela "Modelo bom cabe numa respiração. O resto é romance."
- *Conversar com Edson* · `im_corporativo_s5_conversar_co_solicitante` · 130 palavras.
  O Wellington testou o print do protótipo com dois colegas. Edson pergunta do WhatsApp; a resposta muda com
  `co_negociacao_opcao` (próxima rodada ou piloto da equipe dele).
  Fala-chave: Edson "Se não der agora, me explica o porquê. Eu explico para o meu pessoal."
- *Observar o uso* (só cena) · amizade +0,5 Rosângela · `im_corporativo_s5_observar_central` · 200 palavras.
  A Neusa tenta usar um modelo em papel durante a fila real; a Rosângela marca o tempo. Na terceira tentativa, a
  descrição sai em vinte e poucos segundos.

**Café do térreo**
- *Conversar com Valéria* · `im_corporativo_s5_conversar_co_mentora` · 140 palavras.
  Lê `co_plano_cobertura`: com 2, ela elogia o corte do tema de cores "sem dó"; com menos, lembra que olhar o problema
  vem antes de olhar o item. Antecipa sem dar resposta: "semana que vem você mexe no fechamento; pergunta muito ao Jorge".
  Fala-chave: Valéria "Sempre sobra pedido e falta gente. O plano é o jeito de dizer isso em voz alta."
- *Descansar* · `im_corporativo_descansar_cafe`.

**Refeitório** (sem ninguém)
- *Descansar* · `im_corporativo_descansar_refeitorio`.

**Sala do arquivo**
- *Mentoria com Jorge* · seção 5.
- *Conversar com Jorge* · `im_corporativo_s5_conversar_co_legado` · 130 palavras.
  Primeira conversa depois do anúncio de março. Muda com `co_homenagem_jorge`: "wiki" com `co_conq_memoria`, ele já
  gravou a da Tia Neide na quarta; nos outros casos, diz que ainda está pensando em como guardar o que sabe.
  Fala-chave: Jorge "Março chega rápido. Mais rápido que RFC no CAB, pelo menos."
- *Estudar* · `co_extra_rfc` · `im_corporativo_s5_estudar_arquivo` · 130 palavras.
  O jogador lê a RFC de 2019 (a do fechamento que quebrou o relatório) ao lado do modelo atual da Ingrid e marca o que
  faltava na velha.

**Sala do CAB** (abre nesta semana)
- *Conversar com Ingrid* · `im_corporativo_s5_conversar_co_qualidade` · 130 palavras.
  Ingrid monta a pauta do CAB. Explica padrão, normal e emergencial com exemplos do prédio. A RFC do Farol vai na
  quinta da semana 7.
  Fala-chave: Ingrid "Emergencial é para restaurar serviço. Pressa não é emergência."
- *Ajudar Ingrid* · 90 min · −2 energia · amizade +1,0 · pista `co_p_botao` · `im_corporativo_s5_ajudar_co_qualidade` ·
  300 palavras.
  Ingrid escreve a parte de perfis da RFC e quer saber como o SGC controla acesso hoje. Pede ao jogador que entre na
  homologação do SGC com um usuário de teste do perfil atendente. Num chamado de outro setor, o botão Reabrir não
  aparece. Ela copia o endereço da ação, cola no navegador e a reabertura acontece. Ela pede que o jogador anote só o
  que viu, sem conclusão.
  Fala-chave: Ingrid "Anota o que você viu, não o que você acha. O que achar fica para a semana de testes."

---

### 2.7 Semana 6 · Sexta, 15h às 18h · 180 min

- **Gancho:** B, dentro da `co_16`.
- **Contexto:** testes de caracterização, fuso do Norte registrado, revisão do pull request (API aceitava descrição
  vazia), quadro de rastreabilidade, consulta funcionando em homologação na quarta. Na semana 7 vêm perfis, regressão,
  aceitação e CAB.
- **Para a aula:** segredo em arquivo de configuração e permissão por endereço direto (os dois casos da semana 7).

| baia | central | café | refeitório | arquivo | sala_cab | servidores |
|---|---|---|---|---|---|---|
| **Kauã** (`co_p_senha`), Valéria | Rosângela | Edson | ninguém | Jorge ★ | **Ingrid** (`co_p_botao`) | abre na S7 |

**Baia do Farol**
- *Conversar com Kauã* · `im_corporativo_s6_conversar_co_dev` · 130 palavras.
  Lê `co_ok_review`: com acerto, ele agradece "pela porta dos fundos"; sem, diz que os dois chegaram lá juntos. Conta
  que o teste de carga roda de madrugada na semana que vem.
  Fala-chave: Kauã "Botão desabilitado é só a porta da frente. Agora eu tranco as duas."
- *Ajudar Kauã* · 90 min · −2 energia · amizade +1,0 · pista `co_p_senha` · `im_corporativo_s6_ajudar_co_dev` · 300 palavras.
  Kauã prepara a configuração da integração para os testes da semana 7. A credencial nova do Farol já vai para o cofre
  de segredos da homologação. Lendo o script de build juntos, o jogador vê a linha que carrega
  `config/sgc-integracao.properties` com o comentário "senha provisória - 2012". Kauã nunca abriu esse arquivo. O
  jogador sugere registrar já; Kauã abre o registro "verificar segredo em arquivo da integração", para segunda, com a
  Ingrid. Nenhum dos dois abre o arquivo.
  Fala-chave: Kauã "Não abre, não copia, não manda print. Segunda, com testemunha e com a Ingrid."
- *Conversar com Valéria* · `im_corporativo_s6_conversar_co_mentora` · 130 palavras.
  Valéria soube pelo Jorge que o jogador recebeu a revisão dele "como gente grande". Antecipa a semana 7 sem dar
  resposta: "a Ingrid traz o plano de testes; leva perguntas".
  Fala-chave: Valéria "Revisão boa é a que você agradece e corrige. A de hoje foi assim."

**Central de atendimento**
- *Conversar com Rosângela* · `im_corporativo_s6_conversar_co_supervisora` · 120 palavras.
  Os modelos de descrição foram aprovados pela equipe. Ela pergunta quanto o Farol vai somar ao TMA e lembra os seis
  minutos e quarenta de hoje.
  Fala-chave: Rosângela "Seis e quarenta hoje. Se virar sete, eu quero saber por quê antes da diretoria."
- *Observar o uso* (só cena) · amizade +0,5 Rosângela · `im_corporativo_s6_observar_central` · 200 palavras.
  Sexta de VPN instável: muitas ligações iguais. O jogador vê na prática a diferença entre incidente (fazer voltar) e
  problema (descobrir por que cai), tema do registro extra da semana 1.
  Fala-chave: Rosângela "Hoje é dia de apagar incêndio. Segunda alguém descobre quem acendeu."

**Café do térreo**
- *Conversar com Edson* · `im_corporativo_s6_conversar_co_solicitante` · 130 palavras.
  Edson quer testar a homologação. O teste de aceitação é com a central; para o campo, a resposta muda com
  `co_negociacao_opcao` (piloto na janela ou depois dela).
  Fala-chave: Edson "Três linhas de solução valem mais que três ligações. Isso eu já ensinei lá no campo."
- *Descansar* · `im_corporativo_descansar_cafe`.

**Refeitório** (sem ninguém)
- *Descansar* · `im_corporativo_descansar_refeitorio`.

**Sala do arquivo**
- *Mentoria com Jorge* · seção 5 (encontro 5 é possível a partir desta semana).
- *Conversar com Jorge* · `im_corporativo_s6_conversar_co_legado` · 120 palavras.
  Comenta o fuso do Norte provado na segunda: dez anos de desconfiança e uma manhã de teste. Pergunta se o jogador
  trocou o nome do `teste_fechamento_2`.
  Fala-chave: Jorge "Dez anos todo mundo desconfiando. Bastou um teste com nome decente."
- *Estudar* · `co_extra_caracterizacao` · `im_corporativo_s6_estudar_arquivo` · 130 palavras.
  O jogador relê os testes de segunda e reescreve, num papel, o roteiro de como escrever um teste de caracterização.

**Sala do CAB**
- *Conversar com Ingrid* · `im_corporativo_s6_conversar_co_qualidade` · 120 palavras.
  Ingrid fecha a versão final do plano de testes (os seis blocos que apresenta na segunda). Diz que não está nervosa
  com o CAB, enquanto alinha as canetas pela terceira vez.
- *Ajudar Ingrid* · 90 min · −2 energia · amizade +1,0 · pista `co_p_botao` (se ainda não tiver) ·
  `im_corporativo_s6_ajudar_co_qualidade` · 330 palavras.
  Ensaio da apresentação do CAB: o jogador faz o papel do comitê e faz as perguntas difíceis. Sem a pista
  (`not pista_tem("co_p_botao")`), a Ingrid usa a homologação do SGC como exemplo de risco e acontece a mesma cena da
  semana 5: botão escondido, endereço colado, reabertura feita. Com a pista, os dois revisam a seção de perfis da RFC e
  ela agradece as perguntas.
  Fala-chave: Ingrid "Pergunta de novo, mais chato. O CAB não vai ser mais gentil que você."

---

### 2.8 Semana 7 · Quinta, 14h às 17h · 180 min

- **Gancho:** B, dentro da `co_17`, depois do CAB aprovado (11h40).
- **Contexto:** perfis, regressão, senha de 2012 no repositório, aceitação na central (quarta) e CAB (hoje de manhã).
  Amanhã à noite é a janela.
- **Para a aula:** quanto custa voltar (rollback inteiro × reverter um passo), base do critério de parada.

| baia | central | café | refeitório | arquivo | sala_cab | servidores |
|---|---|---|---|---|---|---|
| Kauã | Rosângela | Valéria | Edson | Jorge ★ | ninguém | **Ingrid** (`co_p_parada`) |

**Baia do Farol**
- *Conversar com Kauã* · `im_corporativo_s7_conversar_co_dev` · 130 palavras.
  O teste de carga de madrugada passou (1.500 usuários, 2,4 s no percentil 95). Mesmo assim ele está ansioso: o script
  da carga do histórico é dele. Lê `co_senha_relato` para uma frase sobre a senha de 2012.
  Fala-chave: Kauã "Passou no teste e mesmo assim eu sonhei com acento quebrado."

**Central de atendimento**
- *Conversar com Rosângela* · `im_corporativo_s7_conversar_co_supervisora` · 130 palavras.
  Treinamento amanhã, quinze minutos por turno. O turno da noite ainda não tem horário e isso a preocupa (prepara a
  fala do final "bom" da `co_18`).
  Fala-chave: Rosângela "Manhã e tarde eu garanto. A noite é a minha dor de cabeça."
- *Observar o uso* (só cena) · amizade +0,5 Rosângela · `im_corporativo_s7_observar_central` · 200 palavras.
  Na pausa, a Neusa treina os modelos na homologação por conta própria e pergunta: "e o de impressora, não tem?"
  (prepara a outra melhoria citada no final "bom").
  Fala-chave: Neusa "Senha, VPN, notebook. E a impressora, que é metade da minha fila de sexta?"

**Café do térreo**
- *Conversar com Valéria* · `im_corporativo_s7_conversar_co_mentora` · 130 palavras.
  CAB aprovado. Valéria conta da primeira janela dela, em 2011, quando ninguém tinha critério de parada e todo mundo
  ficou até as sete da manhã. Pede que o jogador chegue descansado amanhã.
  Fala-chave: Valéria "Em 2011 a gente não tinha plano de volta. Tinha café e fé. Não recomendo."
- *Descansar* · `im_corporativo_descansar_cafe`.

**Refeitório**
- *Conversar com Edson* · `im_corporativo_s7_conversar_co_solicitante` · 130 palavras.
  Com "investigar_agora", veio para a conversa do piloto da equipe dele; com "base_primeiro", veio a uma reunião na
  diretoria. Conta que o notebook do Wellington ainda falha de vez em quando (prepara a reabertura da `co_18`).
  Fala-chave: Edson "O notebook do Wellington tem personalidade. Se voltar a dar problema, eu vou querer reabrir."
- *Descansar* · `im_corporativo_descansar_refeitorio`.

**Sala do arquivo**
- *Mentoria com Jorge* · seção 5.
- *Conversar com Jorge* · `im_corporativo_s7_conversar_co_legado` · 130 palavras.
  Fala da senha de 2012. Com `co_senha_relato == "historia"`, agradece por terem perguntado a ele antes. Nos outros
  casos, conta que a senha era dele e que gostou de ver o caso registrado sem nome.
  Fala-chave: Jorge "Era minha. 'Só até segunda.' A segunda durou doze anos."
- *Estudar* · `co_extra_parada` · `im_corporativo_s7_estudar_arquivo` · 130 palavras.
  O jogador lê o roteiro aprovado no CAB e escreve, para cada passo, o que faria voltar e quem decide.

**Sala do CAB** (sem ninguém; aberta)

**Sala de servidores** (abre nesta semana)
- *Conversar com Ingrid* · `im_corporativo_s7_conversar_co_qualidade` · 120 palavras.
  Ingrid está ali "só conferindo" o agendamento do backup. Faz piada consigo mesma sobre descanso.
  Fala-chave: Ingrid "Eu disse para descansar. Eu disse para vocês, não para mim."
- *Ajudar Ingrid* · 90 min · −2 energia · amizade +1,0 · pista `co_p_parada` · `im_corporativo_s7_ajudar_co_qualidade` ·
  300 palavras.
  Ensaio de volta numa cópia de produção. Primeiro, restaurar a janela inteira pelo backup: 40 minutos no cronômetro.
  Depois, rodar só o script de reversão da carga do histórico: 6 minutos, sem tocar no resto. Ingrid escreve os dois
  tempos no roteiro da janela e pede ao jogador que confira a anotação.
  Fala-chave: Ingrid "Quarenta para voltar tudo, seis para voltar um passo. Agora a gente sabe quanto custa cada volta."

---

### 2.9 Semana 8 · Sexta, 18h às 21h · 180 min

- **Gancho:** A, entre `call im_ponto_parada(7)` e `co_18_implantacao_avaliacao`. A janela começa às 23h30.
- **Contexto:** a equipe espera a noite. Não há registro extra nesta semana (SIS 3.2: os extras vão de 1 a 7).
- **Para a aula:** quem é afetado pela mudança e ainda não foi ouvido (turno da noite).

| baia | central | café | refeitório | arquivo | sala_cab | servidores |
|---|---|---|---|---|---|---|
| Kauã, Ingrid | turno da noite (sem personagem) | Valéria | fechado ("Fechado depois das 18h") | Jorge ★ | ninguém | fechado ("Reservada para a janela") |

**Baia do Farol** (fundo `escritorio_interior_noite`)
- *Conversar com Kauã* · `im_corporativo_s8_conversar_co_dev` · 130 palavras.
  Kauã pede pizza para a sala de guerra e repassa o script da carga pela quinta vez.
  Fala-chave: Kauã "Bora... Bora. Falei duas vezes para ver se acredito."
- *Conversar com Ingrid* · `im_corporativo_s8_conversar_co_qualidade` · 130 palavras.
  Ingrid imprime o roteiro dos seis passos e grampeia uma cópia para cada pessoa. Pede ao jogador que leia em voz alta o
  critério de parada que já está na RFC ("zero registro corrompido"), sem discutir o que fazer se ele estourar.
  Fala-chave: Ingrid "Hoje à noite ninguém inventa nada. A gente lê, executa e registra."

**Central de atendimento**
- *Observar o uso* (só cena) · 90 min · −1 energia · sem amizade · `im_corporativo_s8_observar_central` · 200 palavras.
  O turno da noite trabalha sem ter feito o treinamento: o horário deles caiu por causa da VPN instável. Um supervisor
  da noite (figurante, sem nome) pergunta ao jogador "esse Farol muda o quê para a gente?". O jogador explica em duas
  frases. É a origem da melhoria que a Rosângela cita no final "bom".

**Café do térreo**
- *Conversar com Valéria* · `im_corporativo_s8_conversar_co_mentora` · 130 palavras.
  Valéria recomenda comer agora e cochilar se der. Conta que, em janela, a pessoa mais útil é a que lê o roteiro com
  calma, não a que digita mais rápido.
  Fala-chave: Valéria "Vamos por partes, inclusive o jantar."
- *Descansar* · `im_corporativo_descansar_cafe` (com `energia_cansaco()` aparece "Recomendado", SIS 4.3).

**Sala do arquivo**
- *Mentoria com Jorge* · seção 5 (última chance de completar o arco).
- *Conversar com Jorge* · `im_corporativo_s8_conversar_co_legado` · 130 palavras.
  "A última janela antes de março." Com `mentoria_conq_corporativo`, mostra o mapa dos causos impresso e preso na
  estante. Sem, diz que ainda dá tempo até março.
  Fala-chave: Jorge "Última janela com crachá. A próxima eu acompanho de casa, de pijama."

---

## 3. Pistas

### 3.1 Dados

```python
    ROUTES["corporativo"]["pistas"] = {
        "co_p_ligacoes": {
            "titulo": _("Três ligações em vinte minutos"),
            "texto": _("Na central, o Paulo atendeu três ligações de 'e o meu chamado?' em vinte minutos. Para cada uma, abriu quatro abas. Depois de cada ligação, fez um risquinho num post-it: 'só para eu saber quantas são'."),
            "ate_semana": 1,
            "uso": _("Semana 2: a entrevista com Rosângela e Edson."),
        },
        "co_p_vazio": {
            "titulo": _("Três espaços no campo Solução"),
            "texto": _("No fim do turno, uma atendente fechou um chamado digitando três espaços no campo Solução. O SGC aceitou e marcou Resolvido."),
            "ate_semana": 2,
            "uso": _("Semana 3: o caso limite da história do Edson."),
        },
        "co_p_acentos": {
            "titulo": _("A troca de codificação de 2014"),
            "texto": _("Em 2014 o banco do SGC saiu da Tia Neide para o Oracle novo e trocou de codificação. Textos antigos ainda guardam acentos de outro padrão: 'manutenção' aparece como 'manutenÃ§Ã£o' em relatórios velhos."),
            "ate_semana": 4,
            "uso": _("Semana 5: o risco da carga do histórico."),
        },
        "co_p_norte": {
            "titulo": _("A hora do Norte"),
            "texto": _("Desde a migração de 2014, a rotina das 72 h grava o fechamento no horário de Brasília. No relatório das filiais do Norte, os chamados de senha parecem levar 73 h. A supervisora de Manaus reclamou em 2015; ninguém registrou."),
            "ate_semana": 5,
            "uso": _("Semana 6: o teste de caracterização que falha."),
        },
        "co_p_botao": {
            "titulo": _("O botão que só sumiu"),
            "texto": _("Na homologação do SGC, com o perfil atendente, o botão Reabrir não aparecia num chamado de outro setor. Colando o endereço da ação no navegador, a reabertura funcionou."),
            "ate_semana": 6,
            "uso": _("Semana 7: os testes de perfil."),
        },
        "co_p_senha": {
            "titulo": _("A linha provisória do build"),
            "texto": _("No script de build da integração, uma linha carrega o arquivo de configuração do usuário de serviço do SGC, com o comentário 'senha provisória - 2012'. Você e o Kauã não abriram o arquivo e registraram para verificar com a Ingrid."),
            "ate_semana": 6,
            "uso": _("Semana 7: o caso da senha no repositório."),
        },
        "co_p_parada": {
            "titulo": _("Quanto tempo leva para voltar"),
            "texto": _("No ensaio de quinta, desfazer a janela inteira pelo backup levou 40 min. Reverter só a carga do histórico levou 6 min e não mexeu no resto."),
            "ate_semana": 7,
            "uso": _("Semana 8: a decisão na janela."),
        },
    }
```

Revisão pedagógica: cada texto descreve o que foi visto e nenhum diz qual opção escolher. As pistas de formato 1
ficam antes de menus pedagógicos e não entram na contagem de `co_acerto`/`co_erro`.

### 3.2 Onde cada pista é usada

| Pista | Onde ganha | Arquivo e label | Âncora (inserir depois de) | Formato |
|---|---|---|---|---|
| `co_p_ligacoes` | S1 observar central | `co_05_entrevista.rpy`, `co_05_entrevista` | `"{i}Silêncio. Os dois olham para você.{/i}"`, antes do menu "[NOME_CO_SUPERVISORA] e [NOME_CO_SOLICITANTE] puxam para lados opostos. Como você conduz?" | 1 |
| `co_p_vazio` | S2 observar central | `co_09_historias.rpy`, `co_09_historias` | `co_mentora "Boa, [NOME_CO_DEV]. Isso é um caso limite. [player_name], o que você propõe?"`, antes do menu "E se o atendente tentar resolver sem descrever a solução?" | 1 |
| `co_p_acentos` | mentoria 2 (S3–S4) | `co_15_gestao.rpy`, `co_15_gestao` | `co_legado "Tem texto de 2008, tem gente que colou do Word, tem campo com 4 mil caracteres. Isso aí tem história, e nem toda é bonita."`, antes do menu "Como tratar o risco da carga do histórico?" | 1 |
| `co_p_norte` | mentoria 3 (S4–S5) | `co_16_codificacao.rpy`, `co_16_codificacao` | `co_dev "Olha isso. É o tal bug de fuso de 2014. Todo mundo desconfiava, ninguém tinha provado. Bora consertar?"` | 2 |
| `co_p_botao` | S5–S6 ajudar Ingrid | `co_17_testes_seguranca.rpy`, `co_17_testes_seguranca` | `co_qualidade "Quatro perfis. Como você prova que essa matriz vale de verdade?"`, antes do menu "Como verificar os perfis?" | 1 |
| `co_p_senha` | S6 ajudar Kauã | `co_17_testes_seguranca.rpy`, `co_17_testes_seguranca` | menu "Como você relata a senha no repositório?" (opção nova) | 2 |
| `co_p_parada` | S7 ajudar Ingrid | `co_18_implantacao_avaliacao.rpy`, `co_18_implantacao_avaliacao` | `co_qualidade "[player_name], faltam menos de duas horas de janela. Fala o que você faria."`, antes do menu "Faltam menos de duas horas de janela. O que fazer?" | 1 |

**Formato 1** (uma linha antes do menu; o menu pedagógico não muda, só ganha `(tipo="trabalho")`):

```renpy
    call pista_lembrar("co_p_ligacoes") from _pl_co05_conflito
    call pista_lembrar("co_p_vazio") from _pl_co09_caso_limite
    call pista_lembrar("co_p_acentos") from _pl_co15_risco
    call pista_lembrar("co_p_botao") from _pl_co17_rbac
    call pista_lembrar("co_p_parada") from _pl_co18_janela
```

Ecos opcionais (só narração, não chamam `pista_usar`, não mudam nota):
- `co_05`, depois de `co_supervisora "Cobrança de andamento... 18\%. Quase uma em cada cinco ligações."`:
  `if "co_p_ligacoes" in pistas_usadas:` → `"{i}Você lembra dos risquinhos no post-it do Paulo. Alguém já estava contando.{/i}"`
- `co_16`, depois de `co_legado "Em 2011 um atendente descobriu que três espaços passavam na validação do SGC. Virou moda na central."`:
  `if "co_p_vazio" in pistas:` → `"{i}Você lembra do fim de turno na central, na semana 2. Três espaços, e o SGC aceitou.{/i}"`

**Formato 2 — `co_p_norte` na `co_16`.** A cena não tem menu nesse ponto. O menu só aparece para quem tem a pista;
sem ela, a cena segue exatamente como hoje:

```renpy
    if pista_tem("co_p_norte"):
        menu (tipo="conversa"):
            "Contar o causo do Jorge: a supervisora de Manaus reclamou disso em 2015" (tipo="pista"):
                $ pista_usar("co_p_norte")
                show co_legado neutral at left_zoom
                with dissolve
                co_legado "A hora do Norte. Em 2015 a gente riu, prometeu olhar e não registrou nada."
                co_legado "Desta vez registra com o causo junto: desde quando, quem reclamou, qual relatório. Aí o problema tem história e tem dono."
                $ add_friendship_point("co_legado", 0.5)
                hide co_legado
                with dissolve
            "Seguir com o [NOME_CO_DEV]":
                pass
```

Resultado melhor: o registro de problema da linha seguinte ("abrem um registro de problema para a próxima rodada")
nasce com causa, data e relatório afetado. Fala própria do Jorge e +0,5 de amizade.

**Formato 2 — `co_p_senha` na `co_17`.** Opção nova no menu "Como você relata a senha no repositório?" (as três
antigas continuam):

```renpy
        "Mostrar o registro de sexta: o script de build também lê esse arquivo" (tipo="pista") if pista_tem("co_p_senha"):
            $ pista_usar("co_p_senha")
            $ co_senha_relato = "registro"
            $ add_friendship_point("co_qualidade", 1)
            show co_qualidade neutral at left_zoom
            with dissolve
            co_qualidade "Dois lugares, não um. Sem isso, a gente trocava a senha e o build da madrugada quebrava no sábado."
            co_dev "E o registro já existia desde sexta. Só faltava abrir o arquivo com testemunha."
```

Mais duas linhas na mesma cena:
- Depois de `"{i}O histórico do arquivo mostra a data: 2012.{/i}"`: `if pista_tem("co_p_senha"):` →
  `"{i}É o arquivo do registro que você e o [NOME_CO_DEV] fizeram na sexta. Agora ele foi aberto com a [NOME_CO_QUALIDADE] do lado.{/i}"`
- Depois de `co_qualidade "Dois: por isso trocamos a senha do usuário de integração. É mudança padrão, pré-aprovada. Não espera o CAB."`:
  `if "co_p_senha" in pistas_usadas:` → `co_qualidade "E o script de build passa a ler do cofre também. Entra na mesma mudança padrão."`

O valor `"registro"` de `co_senha_relato` é o mesmo da primeira opção; nenhuma conquista lê essa variável.

---

## 4. Registros extras do notebook

Ganhos só por "Estudar" na Sala do arquivo. Não contam nos 8 registros da rota; aparecem em "Extras (opcionais)".

```python
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
```

Cada extra prepara a semana seguinte: ITIL → entrevista sobre chamados; engenharia reversa → especificação a partir do
que existe; caso de uso → inspeção e arquitetura; anticorrupção → carga e RFC; RFC → caracterização da mudança;
caracterização → regressão; critério de parada → janela.

---

## 5. Arco de mentoria: Causos do SGC

**Ideia.** O Jorge guarda 16 anos de SGC na cabeça e vai se aposentar em março (revelado na `co_14`). Em cinco
encontros, o jogador aprende a tirar conhecimento tácito de uma pessoa e a transformá-lo em registro útil: perguntar
pelo causo, desconfiar dos dados antigos, registrar problema conhecido, escrever o porquê e mapear o que só uma pessoa
sabe. O arco é opcional. As decisões sobre esses temas continuam nas cenas (`co_04`, `co_15`, `co_16`).

**Regras de texto.** Encontros feitos antes da `co_14` (`co_homenagem_jorge == ""`) não citam aposentadoria; os feitos
depois citam março. Local: Sala do arquivo, exceto na semana 4 (baia); a primeira fala de cada encontro testa
`im_semana_atual == 4` para o lugar. Cada encontro dá +1,0 de amizade com o Jorge (teto do SIS) e 20 a 30 falas.

```python
    ROUTES["corporativo"]["mentoria"] = {
        "id": "co_mentoria_causos",
        "titulo": _("Causos do SGC"),
        "mentor": "co_legado",
        "passos": [
            {"n": 1, "semana_min": 2, "pista": None,           "resumo": _("A caneca de 2008 e o servidor Tia Neide")},
            {"n": 2, "semana_min": 3, "pista": "co_p_acentos", "resumo": _("A troca de codificação de 2014")},
            {"n": 3, "semana_min": 4, "pista": "co_p_norte",   "resumo": _("O fuso do Norte")},
            {"n": 4, "semana_min": 5, "pista": None,           "resumo": _("O primeiro causo gravado no wiki")},
            {"n": 5, "semana_min": 6, "pista": None,           "resumo": _("O mapa dos causos")},
        ],
    }
    ROUTES["corporativo"]["conquistas_extra"] = [
        {"id": "mentoria_conq_corporativo", "var": "mentoria_conq_corporativo",
         "title": _("Causos Registrados"), "desc": _("Concluiu os cinco encontros com o Jorge.")},
    ]
```

### Encontro 1 · A caneca de 2008 e o servidor Tia Neide (semana 2+) · `im_corporativo_mentoria_1` · 420 palavras
- **O que acontece:** Jorge pergunta se o crachá definitivo chegou; chegou, então ele conta por que o servidor se chama
  Tia Neide: um dos DBAs da foto de 2008 batizou o rack com o nome da tia, "que também esquentava, fazia barulho e nunca
  dormia". Depois mostra a caneca e lista o que ela "viu": o lançamento, a greve de 2013, a reescrita cancelada.
- **O que se aprende:** a diferença entre conhecimento explícito (está num documento) e tácito (está em alguém). Uma
  boa pergunta para tirar o tácito é a mesma da entrevista: "quando foi a última vez que isso aconteceu?". O jogador
  combina com o Jorge uma regra simples: toda vez que ele disser "isso aí tem história", o jogador anota a data e pede o
  causo.
- **Falas-chave:** Jorge "Metade do SGC é código. A outra metade é causo." · Jorge "Me pergunta 'por que', não 'o
  quê'. O 'o quê' está no banco."

### Encontro 2 · A troca de codificação de 2014 (semana 3+) · `im_corporativo_mentoria_2` · 420 palavras · pista `co_p_acentos` (até a S4)
- **O que acontece:** Jorge acha na estante um relatório impresso de 2014 com "manutenÃ§Ã£o" no lugar de
  "manutenção". Conta a migração daquele ano: o SGC saiu da Tia Neide para o Oracle novo, o DBA trocou a codificação e
  os textos novos ficaram certos. Os antigos guardaram os bytes do padrão velho em alguns campos, e ninguém consertou
  porque "ninguém lê chamado velho".
- **O que se aprende:** dado antigo carrega a história das migrações. Antes de mover dados, perguntar: por quais
  mudanças esse dado já passou? Que codificação, formato de data, campo reaproveitado ou valor "mágico" ele guarda?
- **Falas-chave:** Jorge "Ninguém lê chamado velho. Até a auditoria ler." · Jorge "Todo dado tem sotaque. O de 2008
  fala outra língua."

### Encontro 3 · O fuso do Norte (semana 4+) · `im_corporativo_mentoria_3` · 420 palavras · pista `co_p_norte` (até a S5)
- **O que acontece:** desde a migração de 2014, a rotina das 72 h grava o fechamento no horário de Brasília. Nas
  filiais do Norte com outro fuso, os chamados de senha parecem levar 73 h. Em 2015 a supervisora de Manaus reclamou; a
  equipe riu, chamou aquilo de "hora do Norte" e esqueceu. Na semana 4 (antes da festa), Jorge olha o relógio, fala da
  "papelada do RH" e muda de assunto.
- **O que se aprende:** problema conhecido sem registro vira folclore e some com quem lembra. Registrar um problema não
  é prometer consertar agora: é escrever causa, impacto e dono para alguém decidir depois.
- **Falas-chave:** Jorge "Bug que vira apelido nunca mais é consertado." · Jorge (semana 4) "Tem coisa que eu preciso
  contar para alguém antes de... bom. Antes de esquecer."

### Encontro 4 · O primeiro causo gravado no wiki (semana 5+) · `im_corporativo_mentoria_4` · 450 palavras
- **O que acontece:** depois do anúncio de março, Jorge quer começar pelo causo das 72 h. Com `co_conq_memoria`, ele
  conta que já gravou a da Tia Neide na quarta e que "ficou divertido e inútil: ninguém sabe o que fazer com aquilo".
  Sem `co_conq_memoria`, ele diz que pensou desde a festa e quer começar. Os dois escrevem a página num modelo de seis
  campos: o que faz; quando e por que nasceu (greve, março de 2013, fila de três mil); onde está (`TRG_FECHA_SENHA_72H`,
  job das 2h); o que mudou depois (descrição padrão e autor "sistema", decididos na semana 3); o que quebra se mexer
  (fila de senha, relatório mensal, hora do Norte); quem sabe mais.
- **O que se aprende:** causo vira documentação quando responde "o que eu faço com isso?". Registrar a decisão junto
  com o contexto (o porquê) é o que protege quem vem depois.
- **Falas-chave:** Jorge "História boa diverte. Registro bom avisa." · Jorge "No campo 'quem sabe mais' eu escrevi meu
  nome. Agora risca e põe mais um."

### Encontro 5 · O mapa dos causos (semana 6+) · `im_corporativo_mentoria_5` · 450 palavras · conclusão
- **O que acontece:** os dois listam tudo que hoje só o Jorge sabe: a rotina das 72 h, o cálculo do SLA com feriados
  escritos à mão (2010), a integração com o RH que bloqueia acesso de quem sai, a réplica da Tia Neide e os 14
  relatórios. Para cada item, marcam o que quebra, quem percebe e com que frequência acontece. Escolhem os cinco mais
  arriscados para gravar até março e dão a cada um uma segunda pessoa: Kauã (integração com o RH), Ingrid (relatórios),
  Valéria (regras da central), o jogador (página das 72 h enquanto durar o estágio) e o próprio Jorge, que revisa todos.
- **O que se aprende:** o "fator ônibus" da `co_14` se trata com um mapa de conhecimento priorizado por risco e com uma
  segunda pessoa por assunto, não com um documento gigante.
- **Conclusão:** Jorge imprime o mapa e assina embaixo. `mentoria_avancar()` concede a conquista extra.
- **Falas-chave:** Jorge "Em 2008 eu era o SGC. Agora sou só um dos autores. Melhor assim." · Jorge "Março ficou
  menos assustador."

**Conquista:** `mentoria_conq_corporativo`, "Causos Registrados", condição `mentoria_passos["corporativo"] >= 5`
(concedida por `mentoria_avancar()` no 5º encontro). Fica em `conquistas_extra`; não entra em `co_conquistas()` nem em
`co_final_grade()`. `co_conq_memoria` continua dependendo só do menu da `co_14`.

**Falas novas nas cenas (só texto):**
- `co_14_comemoracao.rpy`, depois de `co_legado "Eu sei. Está tudo aqui na cabeça, e isso é um risco. Eu mesmo devia ter resolvido antes."`:

```renpy
    if mentoria_passos.get("corporativo", 0) >= 2:
        co_legado "[player_name] já ouviu dois causos meus lá no arquivo e anotou tudo com data. Foi aí que eu vi o tamanho do que não está escrito."
```

- `co_18_implantacao_avaliacao.rpy`, na saída (`scene bg empresa_exterior_noite`): dentro do bloco `if co_conq_memoria:`,
  depois de `"{i}A caneca branca de faixa azul, lascada na borda, pesa mais do que parece.{/i}"`, e num bloco próprio
  quando só a mentoria foi concluída:

```renpy
        if mentoria_conq_corporativo:
            co_legado "E o mapa dos causos está na primeira página do wiki. Cada causo tem uma segunda pessoa."
    ...
    if mentoria_conq_corporativo and not co_conq_memoria:
        show co_legado neutral at center_zoom
        with dissolve
        co_legado "[player_name], o mapa dos causos está na primeira página do wiki. Cada causo tem uma segunda pessoa. Março ficou menos assustador."
        hide co_legado
        with dissolve
```

---

## 6. Caça à ambiguidade na rota (`co_09`)

**Onde:** `game/story/rota_corporativo/co_09_historias.rpy`, label `co_09_historias`, de manhã, depois das exceções do
UC01 e antes do critério de aceitação. Âncora: depois de `co_mentora "Acesso negado. Chamado tem nome, telefone,
endereço de subestação. Proteger isso também é requisito."` e antes de `$ advance_minutes(45)`.

**Por que aqui:** a semana 3 fecha com "requisito bom é aquele que duas pessoas leem e entendem a mesma coisa". O
texto do termo de abertura usa palavras que a rota já discutiu ("fácil" na `co_05`, o número de desempenho na `co_06`),
e as reescritas adequadas usam os mesmos números da história.

**Texto na cena:**

```renpy
    show co_mentora thinking at left_zoom
    co_mentora "Antes do critério, olha como o pedido chegou da diretoria. É o texto do termo de abertura do Farol."
    show co_dev neutral at right_zoom
    co_dev "Parece ótimo. Eu assinaria embaixo."
    co_mentora "Por isso mesmo. Marca as palavras que cada pessoa leria de um jeito."
    call amb_atividade("co_amb_termo") from _amb_co09
    show co_dev thinking at right_zoom
    co_dev "Três segundos, quatro campos e um modelo. Isso eu sei programar. 'Rápida' eu não sabia."
    show co_mentora neutral at left_zoom
    co_mentora "Agora duas pessoas leem e entendem a mesma coisa. Era isso que faltava no termo."
```

**Dados:**

```python
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
        },
    }
```

- `decisao` registra só a primeira tentativa: `co_amb_termo_marcar`, `co_amb_termo_rapida`, `co_amb_termo_completas`,
  `co_amb_termo_adequadamente`. Isso não mexe em `co_score` (as 21 decisões da bíblia não mudam).
- Resultado mostrado: "A consulta deve [responder em até 3 s para 95% das consultas, com 1.500 usuários simultâneos no
  pico das 9h] e mostrar [o estado, o atendente responsável, a data da última mudança e a solução registrada] do
  chamado; o atendente deve descrever a solução [em texto curto que diga o que foi feito, usando um modelo pronto quando
  houver, antes de mudar o chamado para Resolvido]."
- Coerência: a reescrita de "adequadamente" usa o acordo da `co_05` (descrição curta com modelos) e não responde a
  decisão 9 (o que fazer com a descrição vazia), que vem logo depois.
- Eco na `co_11`, depois do bloco da decisão 11 (após o `if not co_ok_insp_ambiguo:`), só se `amb_resultados` tiver
  `co_amb_termo` concluído: `co_qualidade "É o mesmo 'rápida' que vocês caçaram no termo de abertura. Palavra vaga
  volta quando alguém copia frase velha."` A fala vem depois da decisão para não dar a resposta.
- Tempo de jogo: 6 a 8 min.

---

## 7. Rastreabilidade na rota (`co_16` → `co_17`)

### 7.1 O quadro (`co_16`)

**Onde:** `game/story/rota_corporativo/co_16_codificacao.rpy`, label `co_16_codificacao`, depois dos testes de
caracterização e da mudança pequena. Âncora: depois de `"{i}Com a rede pronta, a mudança cabe em poucas linhas: sem
descrição, o chamado continua Em atendimento; na rotina das 72 h, entra o texto padrão e o autor \"sistema\".{/i}"` e
antes de `$ set_time(14, 0)`.

**Texto na cena:**

```renpy
    show co_dev neutral at right_zoom
    co_dev "Antes do almoço, a [NOME_CO_QUALIDADE] pediu o quadro de rastreabilidade do que a gente mexeu. Vai anexo na RFC."
    co_dev "Cada critério liga num requisito e num teste. Se não liga, alguém pergunta no CAB."
    call rast_atividade("co_rast_farol") from _rast_co16
    if rast_lacuna_achada("co_rast_farol"):
        co_dev "Critério sem teste. Bem achado. Escrevo agora: atendente pela URL, acesso negado, tentativa na trilha."
        "{i}O teste novo entra na suíte. Ele falha, como devia: a verificação ainda está só na tela. O [NOME_CO_DEV] anota para corrigir no servidor.{/i}"
    else:
        co_dev "Quadro fechado. Mando para a [NOME_CO_QUALIDADE]."
```

O ramo `else` não revela nada (SIS 5.2).

**Dados:**

```python
    ROUTES["corporativo"]["rastreabilidade"] = {
        "co_rast_farol": {
            "requisitos": [
                {"id": "RF-01", "texto": _("O solicitante consulta o próprio chamado pelo número e vê estado, atendente e solução.")},
                {"id": "RF-03", "texto": _("O chamado só vai para Resolvido com a solução descrita.")},
                {"id": "RN-07", "texto": _("Chamados de Reset de senha sem retorno em 72 h são resolvidos pela rotina com a descrição padrão, e a trilha registra 'sistema'.")},
                {"id": "RF-05", "texto": _("O solicitante reabre um chamado resolvido informando o motivo; a solução anterior fica no histórico.")},
                {"id": "RF-06", "texto": _("Cada perfil só faz o que a matriz de permissões permite; toda tentativa negada vai para a trilha.")},
            ],
            "criterios": [
                {"id": "C1", "de": "RF-01", "teste": "T1",
                 "texto": _("Dado o chamado 48213 Resolvido com solução registrada, quando o solicitante o consulta pelo número, então vê Resolvido, o nome do atendente e o texto da solução."),
                 "explica": _("C1 descreve o que a consulta mostra: vem do RF-01. O T1 abre o 48213 e confere os três campos.")},
                {"id": "C2", "de": "RF-03", "teste": "T2",
                 "texto": _("Dado um chamado Em atendimento, quando o atendente tenta resolver com a descrição só com espaços, então o chamado continua Em atendimento e a tela orienta o preenchimento."),
                 "explica": _("C2 é o bloqueio da descrição vazia (RF-03), no caso que o Jorge apontou. O T2 tem o nome desse comportamento.")},
                {"id": "C3", "de": "RN-07", "teste": "T3",
                 "texto": _("Dado um chamado de Reset de senha sem retorno há 72 h, quando a rotina roda, então ele vai para Resolvido com a descrição padrão e a trilha registra o autor 'sistema'."),
                 "explica": _("C3 é a regra herdada da rotina (RN-07), não o bloqueio. O T3 é o teste de caracterização da rotina.")},
                {"id": "C4", "de": "RF-05", "teste": "T4",
                 "texto": _("Dado um chamado Resolvido, quando o solicitante reabre informando o motivo, então o chamado volta a Em atendimento e a solução anterior fica no histórico."),
                 "explica": _("C4 é a reabertura (RF-05). O T4 confere o estado e o histórico.")},
                {"id": "C5", "de": "RF-06", "teste": "T5",
                 "texto": _("Dado um solicitante, quando tenta consultar o chamado de outra pessoa, então recebe acesso negado e a tentativa vai para a trilha."),
                 "explica": _("C5 fala de quem é impedido, não do que a consulta mostra: vem dos perfis (RF-06). O T5 tenta e espera a negativa.")},
                {"id": "C6", "de": "RF-06", "teste": None,
                 "texto": _("Dado um atendente, quando abre pela URL a reabertura de chamado de outro setor, então recebe acesso negado e a tentativa vai para a trilha."),
                 "explica": _("C6 vem dos perfis (RF-06).")},   # a parte do teste nunca é explicada (lacuna)
            ],
            "testes": [
                {"id": "T1", "texto": _("teste_consulta_mostra_estado_atendente_e_solucao")},
                {"id": "T2", "texto": _("teste_resolver_so_com_espacos_mantem_em_atendimento")},
                {"id": "T3", "texto": _("teste_rotina_72h_grava_descricao_padrao_e_autor_sistema")},
                {"id": "T4", "texto": _("teste_reabrir_com_motivo_preserva_solucao_anterior")},
                {"id": "T5", "texto": _("teste_solicitante_chamado_de_outro_acesso_negado")},
                {"id": "T6", "texto": _("teste_atendente_nao_ve_botao_reabrir_de_outro_setor")},   # isca: confere a tela, não o acesso
            ],
            "lacuna": "C6",
            "explica_lacuna": _("Nenhum teste tenta a reabertura pela URL com o perfil atendente. O T6 só confere que o botão some da tela."),
        },
    }
```

- Armadilhas plausíveis: C3 → RF-03 (os dois falam de descrição); C5 → RF-01 (os dois falam de consulta); C6 → T6 ou T5
  (os dois falam de acesso). Ligar C6 a qualquer teste conta como lacuna não achada, sem revelar.
- `decisao("co_rast_farol_ligacoes", ...)` e `decisao("co_rast_farol_lacuna", ...)` como no SIS 5.2. Não mexem em
  `co_score`.
- Resumo de cobertura no fim: "RF-01: 1 critério, 1 teste · RF-03: 1 e 1 · RN-07: 1 e 1 · RF-05: 1 e 1 · RF-06: 2
  critérios, 1 teste" (o último número só aparece certo se o jogador marcou a lacuna; senão mostra o que ele ligou).
- Coerência com a história: o critério C2 usa o caso dos espaços que o Jorge apontou na revisão; o T2 tem o nome de
  comportamento que ele pediu; a lacuna é o mesmo furo visto na pista `co_p_botao` e ensinado na decisão 19 ("botão
  escondido não é controle de acesso").
- Tempo de jogo: 8 a 10 min.

### 7.2 O bug na semana 7 (`co_17`)

1. Antes do menu "Como verificar os perfis?" (depois de `call pista_lembrar("co_p_botao") from _pl_co17_rbac`):
   `call rast_lembrar("co_rast_farol") from _rl_co17_rbac`. Com a lacuna achada, o menu "Lembrar" mostra: "No quadro
   da semana passada, o critério do atendente que abre pela URL a reabertura de outro setor estava sem teste. Você
   marcou, e o Kauã escreveu o teste."
2. Depois de `co_dev "Esse teria virado manchete na auditoria. Bem achado."` (fim dos doze casos negativos), entra:

```renpy
    if rast_lacuna_achada("co_rast_farol"):
        "{i}O teste que nasceu do quadro já está na suíte. Na segunda rodada, com a correção no servidor, ele passa: pela URL, o atendente recebe acesso negado, e a tentativa aparece na trilha.{/i}"
        co_qualidade "Elo fechado: requisito, critério e teste. É assim que eu gosto de achar bug: na quarta da semana anterior."
    else:
        "{i}Antes do almoço, [NOME_CO_QUALIDADE] tenta por conta própria os endereços diretos das ações. Com o perfil atendente, ela cola a URL da reabertura de um chamado de outro setor. A reabertura acontece.{/i}"
        co_qualidade "Abre o quadro de rastreabilidade da semana passada."
        "{i}A linha está lá: o critério do atendente que abre a reabertura pela URL. Na coluna do teste, nada que prove o acesso negado por esse caminho.{/i}"
        co_qualidade "O critério existia. O teste que provava o 'não' não existia. O elo que faltou virou bug."
        co_dev "Corrijo no servidor e escrevo o teste que faltou. Ainda bem que foi aqui, e não depois da janela."
```

Só narrativa: nenhum contador, decisão ou conquista muda. Os dois caminhos chegam ao mesmo ponto da cena.

---

## 8. Energia na rota

### 8.1 Eventos de cena

| Cena | Âncora | Linha | Efeito |
|---|---|---|---|
| `co_11_inspecao` | depois de `$ set_time(18, 30)` (fim da cena) | `$ energia_gastar(1, _("inspeção até 18h30"))` | −1 |
| `co_15_gestao` | dentro da opção "\"Eu fico com você no ensaio.\"" | `$ energia_gastar(2, _("ensaio de quarta até tarde"))` e `$ im_hora_extra_somar(30)` | −2, bloco da S5 −30 min |
| `co_15_gestao` | dentro da opção "\"Reviso o roteiro de rollback com o [NOME_CO_LEGADO].\"" | `$ energia_gastar(1, _("revisão do rollback depois do expediente"))` | −1 |
| `co_15_gestao` | opção "\"Vou descansar; tenho prova na quinta.\"" | nenhuma | 0 (ajuste 2) |
| `co_18_implantacao_avaliacao` | depois de `co_legado "Vão para casa. A Tia Neide e eu cuidamos do resto. Brincadeira, eu também vou."` | `$ energia_gastar(3, _("janela de madrugada"))` | −3 |

As ações das intermissões gastam e recuperam conforme o SIS 1.2 e 4.2. Ajudar duas pessoas na semana 6 (Kauã e Ingrid)
custa −4 e é o caminho mais pesado da rota.

### 8.2 Falas com energia baixa (`energia_cansaco()`)

Todas são falas a mais; nenhuma muda menu, decisão ou nota.

1. **Abertura das intermissões 2 a 8** (Valéria): seção 2.1.
2. **`co_15`**, antes do menu "Quem fica no ensaio de quarta à noite?":
   `co_qualidade "E você, pensa bem antes de ficar. Está com olheira de quem já fez a janela."`
3. **`co_16`**, depois de `co_legado "Mentira. Tem pressão, sim. Mas a gente divide."`:
   `co_legado "E você chegou com cara de quarta-feira de ensaio. Café primeiro, código depois. Código com sono vira incidente."`
4. **`co_17`**, depois de `co_qualidade "Agora é descansar antes de sexta à noite. Janela de madrugada com sono é incidente esperando acontecer."`:
   `co_qualidade "[player_name], isso vale em dobro para você. Hoje à tarde, nada de ficar até tarde."`
5. **`co_18`**, depois de `co_mentora "A [NOME_CO_SUPERVISORA] está de plantão no telefone. Ela disse que vai dormir de headset."`:
   `co_qualidade "[player_name], hoje você lê o roteiro em voz alta e confere cada passo. O terminal fica com quem dormiu. Não é castigo, é gestão de risco."`
6. **`co_18`**, segunda-feira, depois de `co_mentora "[NOME_CO_SUPERVISORA], [NOME_CO_SOLICITANTE], obrigada por virem. Hoje quem conduz a conversa é [player_name]."`:
   `"{i}[NOME_CO_MENTORA] chega perto e fala baixo: \"Dormiu pouco, eu sei. Começa pelo número da [NOME_CO_SUPERVISORA] e vai devagar.\"{/i}"`

Descansar na intermissão tem fala própria com cansaço (seção 2.1). Encerrar cedo com 60 min ou mais dá +1 (SIS 1.4).

---

## 9. Lista de edições nas cenas (para a E5)

Todas com âncora por texto; nenhuma renomeia label ou variável; todo `call` novo tem `from`.

| Arquivo | Edição |
|---|---|
| `rota_corporativo.rpy` | 8 `im_intermissao` (5 na cadeia + 3 nas cenas) e 7 `im_ponto_parada` (seção 2.0) |
| `co_05_entrevista.rpy` | `pista_lembrar("co_p_ligacoes")`; eco dos risquinhos; `(tipo=...)` nos menus |
| `co_09_historias.rpy` | bloco da caça à ambiguidade; `pista_lembrar("co_p_vazio")` |
| `co_11_inspecao.rpy` | eco do "rápida" depois da decisão 11; `energia_gastar(1)` no fim |
| `co_14_comemoracao.rpy` | fala do Jorge com `mentoria_passos >= 2` |
| `co_15_gestao.rpy` | `pista_lembrar("co_p_acentos")`; energia nas três opções do ensaio; fala de cansaço; gancho B da S5 |
| `co_16_codificacao.rpy` | menu de pista `co_p_norte`; eco dos três espaços; fala de cansaço; quadro de rastreabilidade; gancho B da S6 |
| `co_17_testes_seguranca.rpy` | `pista_lembrar("co_p_botao")`; `rast_lembrar`; bloco do bug; opção de pista `co_p_senha` e duas linhas; fala de cansaço; gancho B da S7 |
| `co_18_implantacao_avaliacao.rpy` | `pista_lembrar("co_p_parada")`; `energia_gastar(3)`; duas falas de cansaço; falas da mentoria na saída |

Rótulos de menu nos menus tocados: pedagógicos `(tipo="trabalho")`; sociais `(tipo="conversa")`; negociação da `co_13`
`(tipo="negociacao")`; opções de pista `(tipo="pista")`.

---

## 10. Estimativa de palavras e minutos

### 10.1 Palavras escritas para a rota

| Item | Quantidade | Palavras |
|---|---|---|
| Conversar | 43 × ~130 | 5.600 |
| Observar | 2 com pista (300) + 6 só cena (200) | 1.800 |
| Ajudar | 5 × ~300 (uma com ramo) | 1.550 |
| Estudar | 7 × ~125 | 880 |
| Mentoria | 5 × ~430 | 2.150 |
| Descansar | 2 labels com variante | 160 |
| Tutorial e aberturas de cansaço | — | 150 |
| Registros extras (texto do notebook) | 7 × ~75 | 530 |
| Pistas (título e texto) | 7 | 260 |
| Caça à ambiguidade (dados e falas) | — | 480 |
| Rastreabilidade (dados e falas em `co_16` e `co_17`) | — | 750 |
| Outras edições nas cenas (pistas de formato 2, ecos, energia, mentoria) | — | 600 |
| **Total escrito** | | **≈ 14.900** |

### 10.2 O que uma partida lê

- Intermissões: semana 1 com 2 a 3 ações (~450 palavras com o tutorial) e semanas 2 a 8 com cerca de 3 ações
  (~500 palavras cada): ≈ 4.000.
- Ambiguidade, rastreabilidade, pistas lembradas e falas novas nas cenas: ≈ 1.100.
- **Total lido a mais por partida: ≈ 5.100 palavras**, sobre as ~11 mil de hoje.

### 10.3 Minutos

| Item | Minutos |
|---|---|
| Leitura das intermissões (~4.000 palavras) | 22 |
| Escolhas no mapa, resumos e cartões (8 intermissões) | 12–15 |
| Caça à ambiguidade | 6–8 |
| Rastreabilidade (quadro + bug) | 8–10 |
| Pistas lembradas, falas novas e pontos de parada | 4–5 |
| **Total adicionado** | **≈ 52–60** |
| Com "Tempo livre: pular" (fica ambiguidade, rastreabilidade e falas de cena) | ≈ 15–18 |

Partida completa da rota: ≈ 130–150 min; com "pular", ≈ 95–105 min. Bate com a faixa do SIS 8.1. Para 4 aulas de
50 min, os pontos de parada caem bem depois das semanas 2, 4 e 6.

### 10.4 Conferências para a E8

- Rodada com `RW_AUTOPILOTO_MAPA=pular`: 8 de 8 registros e as 21 decisões alcançáveis (nenhum conteúdo desta rota
  chama registro ou decisão dentro da intermissão).
- `conteudo_generico` vazio para a rota: todos os labels citados nas seções 2 e 5 existem.
- `relogio_volta` vazio: a tabela 2.0 não tem sobreposição de horário.
- Pistas: as 7 têm pelo menos um caminho de ganho dentro do `ate_semana` e um uso em cena depois dele.
