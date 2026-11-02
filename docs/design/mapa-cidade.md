# Mapa da cidade: lugares, deslocamento e interface

Data: 2026-11-02. Branch `evolucao`. Etapa E2/E3b do plano `docs/plans/2026-11-02-evolucao.md` (seção "Mapa da
cidade e deslocamento" e decisão do usuário sobre a cidade fictícia inspirada no Rio).
Complementa `docs/design/sistemas-intermissoes.md` (aqui **Sistemas**) e os documentos de conteúdo
`intermissoes-saude.md`, `intermissoes-startup.md` e `intermissoes-corporativo.md`. Não altera nenhum `.rpy`.
Arte: `tools/arte/montar_mapa.py` gera `docs/arte/prompts/mapa.json` e `mapa-saidas.json` (seção 9).

**Decisão que substitui o que os documentos de rota diziam sobre o mapa:** não há mapa por rota nem prédio em corte.
Há **um mapa ilustrado da cidade**, comum às três rotas. O prédio de trabalho de cada rota é **um lugar** do mapa; as
salas que os documentos de rota chamam de locais (POI) viram **sub-locais** desse lugar e aparecem no balão de cada
pessoa ("Davi · mesa da equipe · programando") e no painel de ações. Os ids de POI, a agenda, as ações e os custos
dos documentos de rota continuam valendo; só a forma de mostrar muda, mais o custo de deslocamento (seção 5).

---

## 1. A cidade

Uma cidade fictícia inspirada no Rio, fora de escala. Os bairros usam nomes reais ou inventados sem compromisso com a
geografia: cada lugar fica onde a jogabilidade pede.

- **Nome sugerido: Guanabara** (o nome da baía), só para documentos e arte. Na tela o título é "Mapa da cidade", sem
  nome próprio, porque a `scene_21` fala em "trânsito do Rio de Janeiro" e as cenas da Startup citam Botafogo. Assim
  nada se contradiz (ver dúvidas, seção 11).
- **Identidade visual da base:** morros verdes no horizonte com uma estátua de braços abertos ao longe; baía grande à
  direita com veleiros; ilha do campus ligada por uma ponte; porto com armazéns e guindaste; parque comprido à beira da
  água; enseada com calçadão de ondas pretas e brancas; dois morros de pedra com bondinho na entrada da baía; linha de
  metrô (faixa coral) e linhas de ônibus (tracejado azul-petróleo).

| Bairro | Caráter | Lugares |
|---|---|---|
| Laranjeiras | vale residencial entre morros, sobrados e amendoeiras | casa do jogador |
| Botafogo | casarões antigos, comércio de rua, enseada com praia | casarão da Trocado, café da esquina, orla |
| Aterro | parque comprido à beira da baía, entre Botafogo e Centro | Parque do Aterro |
| Centro | avenidas, torres de escritório, estação de metrô | torre do Grupo Vértice |
| Cais da Maré (inventado) | armazéns portuários reformados | Aceleradora Maré |
| Caju | área industrial e de energia ao norte | subestação |
| Cidade Universitária (ilha, inspirada no Fundão) | campus de prédios modernistas, alamedas de palmeiras | prédio da equipe da Saúde, praça, Instituto, bandejão |

Cada rota tem o seu polo em bairro diferente (decisão do usuário): Saúde na Cidade Universitária, Startup em Botafogo,
Corporativo no Centro. A casa é a mesma nas três (a cena 1 é comum).

---

## 2. Lugares

12 lugares. "Rotas" diz em que rota o lugar acende; nas outras ele aparece apagado (seção 6.4).

| id | Nome | Bairro | Rotas e semanas | Papel |
|---|---|---|---|---|
| `republica` | República das Amendoeiras | Laranjeiras | todas, sempre | casa; "Ir para casa" encerra o tempo livre |
| `predio_projeto` | Prédio da equipe (Polo de Tecnologia) | Cidade Universitária | Saúde, S1+ (servidores S6+) | trabalho da Saúde |
| `praca_campus` | Praça das Palmeiras | Cidade Universitária | Saúde, S1+ | descansar |
| `instituto` | Instituto (ambulatório) | Cidade Universitária | Saúde, S2+ | observar, mentoria |
| `bandejao` | Bandejão da universidade | Cidade Universitária | Startup, S2+ (fechado à noite na S6) | observar, mentoria |
| `casarao` | Casarão amarelo (Trocado) | Botafogo | Startup, S1+ (terraço fechado na S4) | trabalho da Startup |
| `cafe_esquina` | Café da esquina | Botafogo | Startup, S1+ | descansar (S6 observar) |
| `orla` | Orla de Botafogo | Botafogo | Startup, S1+ | descansar (caminhada) |
| `aterro` | Parque do Aterro | Aterro | Corporativo, S2+ (proposta, seção 2.3) | descansar |
| `torre_vertice` | Torre do Grupo Vértice | Centro | Corporativo, S1+ (CAB S5+, servidores S7+) | trabalho do Corporativo |
| `aceleradora` | Aceleradora Maré | Cais da Maré | Startup, S6+ | ajudar o Vinícius |
| `subestacao` | Subestação Caju | Caju | Corporativo, sempre fechada | decorativa: Edson "em campo" |

### 2.1 Posição, tamanho e balão

Base de 2560x1440 (a tela mostra a 1920x1080, escala 0,75). `ancora` = ponto do chão no meio da base do sprite (onde
o lote encosta na base do mapa). `largura` = largura do sprite recortado na base (o pós-processamento grava nesse
tamanho). `balao` = lado preferido do balão. As posições são provisórias: a E2 ajusta sobre a base gerada, por
captura, e só então elas entram nos dados.

| id | `ancora` (x, y) | `largura` | `balao` | Marcador "Você" |
|---|---|---|---|---|
| `republica` | (620, 800) | 220 | acima | à esquerda do lote |
| `predio_projeto` | (1960, 600) | 330 | acima | à esquerda |
| `praca_campus` | (2160, 700) | 250 | abaixo | à esquerda |
| `instituto` | (2360, 580) | 310 | acima | à esquerda |
| `bandejao` | (2140, 900) | 290 | abaixo | à esquerda |
| `casarao` | (1000, 1090) | 330 | acima | à esquerda |
| `cafe_esquina` | (1225, 1120) | 170 | direita | abaixo |
| `orla` | (1440, 1260) | 280 | direita | à esquerda |
| `aterro` | (1420, 860) | 300 | direita | à esquerda |
| `torre_vertice` | (1180, 600) | 270 | esquerda | à direita |
| `aceleradora` | (1590, 470) | 320 | direita | à esquerda |
| `subestacao` | (1380, 270) | 260 | direita | — |

Os quatro lugares do campus ficam a ~200 px um do outro; o balão de cada um vai para o lado indicado para não cobrir o
vizinho. O ícone de foco nunca sai da tela: se o balão passar da borda, ele vira para o lado oposto.

### 2.2 Descrição visual (para o sprite recortado)

Todos: estilo C dos fundos, mesma perspectiva da base (maquete vista a ~30°), luz de fim de tarde vinda da esquerda,
sobre um lote de chão próprio de contorno arredondado (calçada ou gramado) que encaixa num lote vazio da base, fundo
transparente, sem texto. O texto exato de cada prompt está em `tools/arte/montar_mapa.py` (`LUGARES`).

- **`republica`** — sobrado estreito de três andares do início do século XX, fachada verde-água desbotada com frisos
  brancos, varanda de ferro no 2º andar com varal de roupas coloridas e samambaia, janela do sótão com luz acesa,
  porta de madeira com dois degraus, amendoeira na calçada de pedras portuguesas, bicicleta encostada, gato no muro.
- **`predio_projeto`** — prédio baixo de três andares e subsolo, concreto claro e vidro azul-esverdeado com brises de
  madeira (mesma família de `empresa_exterior_manha`, que entra como referência); 3º andar com luz quente mostrando
  mesas e uma sala de quadro branco; copa no 2º; refeitório no térreo visível pela vidraça; porta metálica de serviço
  com grade de ventilação e rampa para o subsolo; bicicletário e duas palmeiras-imperiais jovens.
- **`praca_campus`** — praça quadrada com pedras portuguesas em ondas, três palmeiras-imperiais, dois bancos de
  madeira, bebedouro, canteiro baixo, um ipê-roxo florido, um bem-te-vi num galho.
- **`instituto`** — ala de dois andares, fachada creme, janelas azul-esverdeadas, entrada lateral com toldo verde-água
  e rampa, placa com desenho de folha e pulmão (sem letras), sala de espera com cadeiras azuis, jardim com bancos.
  Sem cruz vermelha, sem "HOSPITAL", sem ambulância (`fachada_instituto_tarde` entra como referência de forma).
- **`bandejao`** — prédio baixo de concreto aparente sobre pilotis, painel de azulejos azuis geométricos, fila de
  estudantes minúsculos de costas, bicicletário, ipê-amarelo no gramado, escada lateral que desce ao subsolo (onde o
  sinal cai, pista `st_p_tunel`).
- **`casarao`** — casarão de dois andares, fachada amarelo-ocre desbotada com frisos brancos, janelas em arco com
  venezianas verde-garrafa; pelas janelas do 2º andar, a mesa comprida com notebooks e a parede de vidro com post-its
  coral, menta e amarelo; portão de ferro com plaquinha sem texto, bicicleta, amendoeira; no telhado, terraço de deck
  com guarda-corpo de ferro, varal de lâmpadas e vasos de manjericão. A quina do térreo fica livre para o café.
- **`cafe_esquina`** — a quina térrea do mesmo casarão (peça separada, encaixada ao lado): toldo listrado verde e
  creme, duas mesinhas redondas com cadeiras de ferro, vitrine com cesta de pão de queijo, lousa com rabiscos sem
  letras. Peça própria para poder reagir sozinha ao foco.
- **`orla`** — abrigo de ônibus de cobertura curva com banco sobre o calçadão de ondas, duas palmeiras, mureta da praia
  com areia e água, carrinho de mate com guarda-sol listrado (o ponto da Startup).
- **`aterro`** — faixa de parque à beira da baía: gramado, árvores de copa larga e palmeiras, caminho sinuoso de pedras
  portuguesas, ciclovia vermelha, quiosque de mate, bancos voltados para a água, pequeno píer com dois barquinhos.
- **`torre_vertice`** — torre de dezesseis andares, alta e esguia, vidro azul-acinzentado com faixas de concreto claro,
  antenas e heliponto; térreo com porta giratória e marquise com um café de mesinhas; um andar alto com luz quente (a
  baia do Farol), o penúltimo com persianas a meia altura (CAB), janela basculante no nível da calçada (subsolo:
  arquivo e servidores). Bem mais alta e escura que o prédio do campus. Sem letreiro.
- **`aceleradora`** — galpão portuário reformado, tijolo aparente, telhado em arco, portões azul-petróleo, faixa com
  padrão geométrico azul e laranja sem palavras, guindaste antigo pintado ao lado, pedaço do cais com água.
- **`subestacao`** — pátio cercado por alambrado, transformadores cinza com isoladores de porcelana marrom, pórticos
  treliçados com cabos, casinha de comando de tijolo com porta azul, caminhonete branca de serviço com faixa laranja
  (sem texto), brita, poste com refletor.

### 2.3 Lugares sem POI nos documentos de rota

- **`republica`**: não é POI. É o destino de "Encerrar o tempo livre", que no mapa aparece também como ação do lugar
  ("Ir para casa"). O trajeto de volta não custa minutos (o tempo livre acabou) e vale a regra do Sistemas §1.4: com
  60 min ou mais sobrando, +1 de energia.
- **`aterro`** (proposta): POI novo `aterro` só no Corporativo, a partir da S2, ação descansar. Motivo: a torre não tem
  nenhum lugar ao ar livre, e é a única rota em que descansar não envolve escolha de distância. Custa 15 min de
  caminhada + 60. Conteúdo: `im_corporativo_descansar_aterro` (3–6 falas); sem ele, cai no `im_generico_descansar`.
  Se a proposta não for aceita, o Aterro fica apagado nas três rotas, como cenário.
- **`subestacao`**: lugar sempre fechado no Corporativo ("Área restrita: só equipe de campo"), não clicável para
  ações, mas focável para ler o estado. Nas semanas em que o Edson não está na agenda e o jogador já o conhece
  (`contato_co_solicitante`; na prática S4 e S8, porque ele aparece na `co_05`), surge um balão acinzentado "Edson ·
  subestação · em campo, sem sinal". Dá vida ao mapa e lembra por que o Edson quer acompanhar o
  chamado pelo celular. Dados opcionais: `"longe": {"co_solicitante": ("subestacao", "celular", _("em campo, sem sinal"))}`.

---

## 3. De POI para lugar e sub-local

Cada POI dos documentos de rota ganha dois campos: `lugar` (id da seção 2) e `sub` (texto curto do sub-local, usado
no balão e no painel). Ids de POI, fundos das ações, `abre`, `acoes` e agenda não mudam. O campo `pos` dos POIs deixa
de ser usado quando a base do mapa existe (continua servindo à grade de reserva).

**Saúde** (base: `predio_projeto`)

| POI | Nome | `lugar` | `sub` |
|---|---|---|---|
| `mesa` | Mesa da equipe | `predio_projeto` | 3º andar · mesa da equipe |
| `sala_reunioes` | Sala de reuniões | `predio_projeto` | 3º andar · sala de reuniões |
| `cafe` | Café | `predio_projeto` | 2º andar · copa |
| `refeitorio` | Refeitório | `predio_projeto` | térreo · refeitório |
| `servidores` | Sala de servidores | `predio_projeto` | subsolo · sala de servidores |
| `praca` | Praça em frente | `praca_campus` | praça em frente ao prédio |
| `ambulatorio` | Ambulatório do Instituto | `instituto` | ambulatório |

**Startup** (base: `casarao`)

| POI | Nome | `lugar` | `sub` |
|---|---|---|---|
| `mesa` | Mesa da equipe | `casarao` | 2º andar · mesa da equipe |
| `sala_vidro` | Sala de vidro | `casarao` | 2º andar · sala de vidro |
| `terraco` | Terraço | `casarao` | terraço |
| `cafe` | Café da esquina | `cafe_esquina` | térreo, na esquina |
| `ponto` | Ponto de ônibus | `orla` | ponto do calçadão |
| `bandejao` | Bandejão da universidade | `bandejao` | salão do bandejão |
| `aceleradora` | Aceleradora Maré | `aceleradora` | auditório do galpão |

**Corporativo** (base: `torre_vertice`)

| POI | Nome | `lugar` | `sub` |
|---|---|---|---|
| `baia` | Baia do Farol | `torre_vertice` | 12º andar · baia do Farol |
| `central` | Central de atendimento | `torre_vertice` | 3º andar · central de atendimento |
| `cafe` | Café do térreo | `torre_vertice` | térreo · café |
| `refeitorio` | Refeitório | `torre_vertice` | 2º andar · refeitório |
| `arquivo` | Sala do arquivo | `torre_vertice` | subsolo · arquivo |
| `sala_cab` | Sala do CAB | `torre_vertice` | 15º andar · sala do CAB |
| `servidores` | Sala de servidores | `torre_vertice` | subsolo · servidores |
| `aterro` (proposta) | Parque do Aterro | `aterro` | beira da baía |

O que sai dos documentos de rota: o "prédio da equipe em corte" (Saúde §1.2), a "torre em corte"
(`images/mapas/corporativo.png`, Corporativo §1.1), as imagens `images/mapas/<rota>.png` e os ícones por POI. No lugar
deles entram a base única `images/mapa/cidade_base.png`, os 12 sprites e os 8 ícones de atividade. A vista "por dentro" de
cada sala continua sendo o fundo da ação (`bg`), que já existe.

---

## 4. Deslocamento: tempos, meios e sons

### 4.1 Regras
- **Mesmo lugar** (troca de sub-local): 0 min. No casarão e na torre há uma transição curta (escada, elevador) sem
  avanço do relógio; no prédio do campus, só um `dissolve`.
- **Mesmo bairro:** 10 min a pé.
- **Bairros vizinhos:** 15–25 min (a pé, ônibus ou metrô).
- **Atravessar a cidade:** 30–40 min (ônibus pela ponte ou metrô + ônibus).
- A ida é cobrada junto com a ação: custo total = trajeto + ação. Depois da ação o jogador está no lugar novo.
- O tempo livre começa no lugar-base da rota (o prédio de trabalho). Voltar para casa no fim não custa.

### 4.2 Tempo entre bairros (minutos e meio)

| | Laranjeiras | Botafogo | Aterro | Centro | Cais da Maré | Cid. Universitária | Caju |
|---|---|---|---|---|---|---|---|
| **Laranjeiras** | 10 a pé | 15 ônibus | 15 ônibus | 20 metrô | 25 metrô | 40 ônibus | 35 ônibus |
| **Botafogo** | | 10 a pé | 15 a pé | 20 metrô | 25 metrô | 30 ônibus | 40 ônibus |
| **Aterro** | | | — | 15 a pé | 20 ônibus | 35 ônibus | 30 ônibus |
| **Centro** | | | | — | 15 a pé | 30 ônibus | 20 ônibus |
| **Cais da Maré** | | | | | — | 25 ônibus | 15 ônibus |
| **Cid. Universitária** | | | | | | 10 a pé (campus) | 20 ônibus |

Exceção: `casarao` ↔ `cafe_esquina` = 0 (mesmo casarão, escada).

### 4.3 Trajetos que cada rota usa

| Rota | De → para | Min | Meio | Tela | Som do trajeto | Som de chegada |
|---|---|---|---|---|---|---|
| Saúde | entre salas do prédio | 0 | — | (dissolve) | — | `xicara_cafe` se for a copa |
| Saúde | prédio ↔ praça ↔ Instituto | 10 | a pé no campus | `transicao_campus` | `steps.ogg` | `abrindo_porta` no Instituto |
| Startup | entre andares do casarão, casarão ↔ café | 0 | escada | `transicao_escada` (1 s) | `passos.ogg` | `xicara_cafe` no café |
| Startup | casarão/café ↔ orla | 10 | a pé | `transicao_calcada` | `passos.ogg` | — |
| Startup | casarão/café/orla ↔ bandejão | 30 | ônibus pela ponte | `transicao_onibus` | `bus.ogg` | `abrindo_porta` |
| Startup | casarão/café/orla ↔ aceleradora | 25 | metrô | `transicao_metro` | `bus.ogg` (provisório) | `abrindo_porta` |
| Startup | bandejão ↔ aceleradora | 25 | ônibus | `transicao_onibus` | `bus.ogg` | `abrindo_porta` |
| Corporativo | entre andares da torre | 0 | elevador | `transicao_elevador` (1 s) | `ambiente_reuniao.ogg` (provisório) | `xicara_cafe` no café |
| Corporativo | torre ↔ Aterro (proposta) | 15 | a pé | `transicao_calcada` | `passos.ogg` | — |
| Todas | qualquer lugar → casa (encerrar) | não cobra | ônibus ou metrô | a do meio | idem | `abrindo_porta` |

- Tela por meio: ônibus → `transicao_onibus`; metrô → `transicao_metro`; a pé fora do campus → `transicao_calcada`;
  a pé no campus → `transicao_campus`; elevador → `transicao_elevador`; escada → `transicao_escada`. Uma tela por
  trajeto, mesmo quando o trajeto real teria dois meios.
- Sons de chegada: `xicara_cafe.ogg` quando o POI de destino é um `cafe`; `abrindo_porta.ogg` quando o destino é um
  prédio (não vale para praça, orla, Aterro e terraço).
- Faltam sons de metrô e de elevador: até existirem, metrô usa `bus.ogg` a 60% do volume e elevador usa
  `ambiente_reuniao.ogg` com fade. `cell_vibration.ogg` toca no início da intermissão em que um lugar abre ("Novo no
  mapa: Bandejão da universidade"), junto com o `renpy.notify`.
- Duração da tela: 1,0 s (0 min com tela), 1,5 s (até 10 min), 1,8 s (15–25 min), 2,0 s (30 min ou mais).

---

## 5. Ajustes nos tempos das intermissões

**Problema.** O Sistemas §1.2 calcula os blocos sem deslocamento ("ajudar 90 + observar 90" cabe em 180). Com o
trajeto, várias combinações que os documentos de rota contam como possíveis deixam de caber. O caso que mais pesa é a
mentoria: na Startup, a Lorena (★) fica no bandejão, a 30 min, junto com a pista de observação das semanas 2–4;
mentoria + observar passaria de 180 para 210, e quem escolhesse as pistas nas semanas 2–4 ficaria com só 4 semanas
para os 5 encontros. Na Saúde, a Dra. Nathalia fica no Instituto (10 min): mentoria + observar = 190.

**Regra adotada: folga de trajeto de 30 min** nas semanas 2–8 da Saúde e da Startup (as rotas com lugares fora do
prédio). O Corporativo não muda: tudo fica na torre (0 min), e o Aterro proposto é escolha extra. A semana 1 (tutorial)
não muda em nenhuma rota: o ambulatório e o bandejão ainda estão fechados. Os custos das ações (Sistemas §1.2) não
mudam. A frase da Saúde §1.1 "os 90 min de observar e de mentoria já incluem o trajeto" deixa de valer: o trajeto é
cobrado à parte.

A folga vai para o fim do bloco; quando a cena seguinte tem hora fixa, vai para o início.

| Rota | Sem. | Antes | Depois | Conferido na cena |
|---|---|---|---|---|
| Saúde | 2 | 16h–19h · 180 | 16h–19h30 · 210 | `scene_9` só usa `advance_minutes` |
| Saúde | 3 | 15h–18h · 180 | 15h–18h30 · 210 | `scene_13` só usa `advance_minutes` |
| Saúde | 4 | 12h–15h · 180 | **11h30**–15h · 210 | `scene_15` faz `set_time(15, 0)` |
| Saúde | 5 | 16h–19h · 180 | 16h–19h30 · 210 | gancho B na `scene_17`; depois só `advance_minutes` |
| Saúde | 6 | 16h30–19h30 · 180 | **16h**–19h30 · 210 | `scene_18` faz `set_time(19, 40)` depois |
| Saúde | 7 | 15h30–18h30 · 180 | 15h30–19h · 210 | `scene_19` sem `set_time` depois do gancho |
| Saúde | 8 | 9h30–12h30 · 180 | 9h30–13h · 210 | `scene_21` faz `set_time(13, 20)` depois |
| Startup | 2 | 15h–18h · 180 | 15h–18h30 · 210 | `st_08` faz `set_time(20, 0)` |
| Startup | 3 | 15h–18h · 180 | 15h–18h30 · 210 | `st_12` faz `set_time(20, 30)` |
| Startup | 4 | 15h–18h · 180 | **14h30**–18h · 210 | `st_14` faz `set_time(18, 0)` |
| Startup | 5 | 16h–19h · 180 | 16h–19h30 · 210 | `st_15` faz `set_time(19, 30)` depois |
| Startup | 6 | 18h–20h30 · 150 | 18h–21h · 180 | o ajuste da `st_16` passa de `set_time(21, 0)` para `set_time(21, 30)` |
| Startup | 7 | 12h–14h30 · 150 | **11h30**–14h30 · 180 | `st_17` faz `set_time(14, 30)` |
| Startup | 8 | 13h30–16h30 · 180 | 13h30–17h · 210 | a cena pula para quinta |

Nas semanas com `mesmo_dia`, continua valendo o Sistemas §1.3: se o relógio já passou do início, o bloco começa na
hora atual e mantém o fim (mínimo de 90 min).

**O que cabe depois do ajuste** (exemplos conferidos):
- Saúde S2: mentoria no Instituto + observar ali = 10 + 90 + 90 = 190 de 210. Voltar ao prédio para conversar (+40) não
  cabe.
- Saúde S5: ajudar o Joseph na mesa (90) + ajudar o Mateus na praça (10 + 90) = 190.
- Startup S2–S4: ir ao bandejão + mentoria + observar = 30 + 90 + 90 = 210, exato.
- Startup S5 e S8: mentoria no bandejão + ajudar alguém em outro lugar deixa de caber (antes cabia). É a escolha da
  semana; o arco continua completável, porque a Lorena tem 7 semanas (S2–S8) para 5 encontros e mentoria + pista no
  mesmo lugar cabem.
- Corporativo: igual ao Sistemas. Descansar no Aterro custa 75 min em vez de 60 no café.

**No fechamento** (`im_resumo`), uma linha nova: "No caminho: 40 min (2 trajetos)". É a mesma lição do planejamento:
trocar de lugar tem custo, como trocar de tarefa no meio do dia.

---

## 6. Interface do mapa

Substitui a área do mapa do Sistemas §2.4. O resto (barra superior, ações, motivos de bloqueio, retorno da tela) vale.

### 6.1 Composição
- O mapa ocupa a tela inteira (base 2560x1440 mostrada a 1920x1080). A barra superior fica por cima, semitransparente:
  "Semana 3 · Sexta · 15:30 · Tempo livre: faltam 150 min · Energia 7/10 (Boa) · Você está em: Casarão amarelo".
- Camadas, de baixo para cima: base; sprites dos lugares (ordenados por `y` da âncora, para quem está mais embaixo
  ficar na frente); marcador "Você"; balões; painel; barra superior e rodapé.
- Com o tempo livre começando às 18h ou depois (Startup S6, Corporativo S8), a tela aplica um tom de noite no mapa
  (`matrixcolor` com escurecimento e azulado leve). Sem arte extra.

### 6.2 Estados do lugar

| Estado | Visual | Texto escrito |
|---|---|---|
| Disponível, sem ninguém | cores normais, nome embaixo do lote | "Ninguém agora" (se houver ação de lugar: "Estudar · Descansar") |
| Com gente | brilho suave pulsando (brilho +0 → +0,08 em 1,2 s; parado se "Transições: desligadas"), balão | o balão (6.3) |
| Fechado agora | dessaturado (saturação 0,15) e mais escuro; um pequeno cadeado desenhado pela tela | o motivo: "Fechado à noite", "Abre na semana 6", "Área restrita: só equipe de campo" |
| Sub-local fechado | o lugar segue aberto; no painel, a linha do sub-local vem desabilitada | "Sala do CAB · Abre na semana 5" |
| Foco (teclado ou mouse) | sobe 12 px e cresce 6% em 0,15 s, contorno claro de 3 px, balão expandido | nome em negrito |
| Você está aqui | marcador "Você" ao lado | "Você está aqui" no rótulo e no painel |
| Apagado (lugar de outra rota) | dessaturado e sem nome; não recebe foco | — |

Um lugar fechado recebe foco (para ler o motivo), mas não abre ações.

### 6.3 Balão
Desenhado pela tela do Ren'Py (moldura creme `#FBF6EC`, contorno escuro de 3 px, ponta apontando para o lugar,
texto `#2B2620`; contraste acima de 12:1). Um balão por lugar, nunca por pessoa.

- **Compacto (sem foco):** retratos empilhados de 48 px (sobrepostos 16 px, no máximo 4 + "+2"), o ícone de atividade
  da primeira pessoa (32 px) e uma linha:
  - 1 pessoa: o nome e a frase curta. "Bia · testando o app com calouros".
  - 2 pessoas: "Davi e Otávio".
  - 3 ou mais: "5 pessoas em 4 salas" (prédio) ou "3 pessoas".
- **Expandido (com foco):** uma linha por pessoa (máximo 6; a torre chega a 6 na S5), cada linha com retrato de 56 px,
  ícone de 32 px e dois textos:
  - linha 1: "Davi · 2º andar, mesa da equipe · programando" (nome · `sub` · rótulo da atividade);
  - linha 2 (opcional, menor): a frase da agenda, "esperando o build no celular que trava".
  - Marcas escritas no fim da linha 1: "★ mentoria" e "aceita ajuda".
- **Longe** (Edson na subestação): balão compacto acinzentado, sem foco próprio; a linha diz "em campo, sem sinal".
- O balão sempre diz a atividade em texto; o ícone é reforço.

**Ícones e rótulos de atividade.** A agenda pode trazer `"atividade": {cid: (icone, frase)}` por semana (Startup §1.4).
Sem esse campo, a tela usa o padrão do sub-local:

| Ícone (id) | Rótulo | Padrão para os sub-locais |
|---|---|---|
| `programando` | programando | mesas de equipe (`mesa`, `baia`) |
| `reuniao` | em reunião | `sala_reunioes`, `sala_vidro`, `sala_cab`, `aceleradora` |
| `cafe` | tomando café | `cafe` (as três rotas) |
| `conversando` | conversando | `refeitorio`, `bandejao` |
| `descansando` | descansando | `praca`, `terraco`, `ponto`, `aterro` |
| `observando` | atendendo (central, ambulatório) / observando usuários (bandejão com testers) | `central`, `ambulatorio` |
| `estudando` | estudando | `arquivo` |
| `celular` | no computador / no celular | `servidores`; Edson "em campo" |

O doc da Startup usa `atendendo` e `observando` como ícones separados; aqui os dois viram `observando` (um só
desenho, rótulo diferente), para caber nos 8 ícones e liberar `conversando`.

### 6.4 Painel de ações
- Abre ao confirmar um lugar (Enter ou clique). Fica do lado oposto ao lugar (lugar com x > 1280 na base → painel à
  esquerda), 600 px de largura, com o mapa escurecido 30% atrás. O marcador e o lugar escolhido continuam visíveis.
- Cabeçalho: nome do lugar, bairro e o trajeto escrito: "Daqui: 30 min de ônibus" ou "Você está aqui".
- Uma seção por sub-local aberto naquela semana: miniatura do fundo da ação, `sub`, as pessoas (retrato 96 px, nome,
  papel de `AMIGOS_DATA[cid]["desc"]`) e os botões de ação. Sub-locais fechados aparecem numa linha desabilitada com o
  motivo.
- Botão de ação com ícone e texto do custo somado: "Conversar com a Bia · 30 min + 30 min de ônibus = 60 min ·
  Amizade". Embaixo, em letra menor: "Depois disso sobram 90 min".
- Bloqueio sempre com motivo escrito: "Falta tempo (precisa de 120 min: 90 + 30 de trajeto)", além dos do Sistemas.
- Ícone por ação, reaproveitando os de atividade (formas diferentes entre si): conversar → `conversando`; observar →
  `observando`; estudar → `estudando`; descansar → `descansando`; ajudar → `celular`; mentoria → `reuniao` com "★".
- Rodapé do painel: "Voltar ao mapa" (também com Backspace ou clique fora do painel). Esc e clique direito continuam
  abrindo o menu do jogo, como no Sistemas §2.5.
- No lugar `republica`: só "Ir para casa (encerrar o tempo livre)", com o aviso de energia do Sistemas §1.4.

### 6.5 Marcador "Você"
- Sprite `images/mapa/voce.png` (pino em gota coral com a silhueta de uma pessoa de mochila), mostrado a 72 px, ponta
  na posição de "Marcador" da tabela 2.1. A palavra "Você" é texto da tela, embaixo do pino, com contorno.
- Parado: sobe e desce 4 px em 1,6 s (parado com transições desligadas).
- No deslocamento: anda em linha reta da origem ao destino em ~1 s (`ease`), com a sombra no chão; em troca de
  sub-local no mesmo lugar, dá um pulinho de 0,3 s.

### 6.6 Acessibilidade
- Teclado: Tab e setas percorrem os lugares acesos na ordem dos POIs da rota (lugar-base primeiro, casa por último);
  Enter abre o painel com foco na primeira ação; "Voltar ao mapa" devolve o foco ao lugar. O primeiro lugar aberto
  recebe o foco inicial (`default_focus`).
- **Modo lista** ("Ver como lista", e automático com "Texto maior"): lista vertical rolável com um bloco por lugar
  aceso: nome, bairro, "A 30 min de ônibus" ou "Você está aqui", estado, uma linha por pessoa (nome · sub-local ·
  atividade · frase) e as ações com o custo somado. Mesma ordem do teclado. Preferência guardada em
  `persistent.im_mapa_lista`.
- Nada só por cor ou forma: estado, custo, trajeto e atividade sempre escritos.
- Leitor de tela: `alt` de cada lugar com tudo em uma frase: "Bandejão da universidade, Cidade Universitária. A 30
  minutos daqui, de ônibus. Aqui: Bia, observando usuários, testando o app com calouros; Lorena, conversando, mentoria
  disponível. Ações: observar o uso, 120 minutos com o trajeto."
- Brilho pulsante, balanço do marcador e caminhada do marcador param com "Transições: desligadas".

---

## 7. Sequência de deslocamento

1. O jogador confirma uma ação no painel. O painel fecha.
2. O marcador "Você" anda até o lugar (~1 s). Se for o mesmo lugar, pulinho de 0,3 s; se for o mesmo sub-local, nada.
3. **Tela de transição** (1,0–2,0 s, seção 4.3): imagem do meio de transporte em tela cheia (recorte 16:9 do fundo
   3:2), zoom lento de 1,00 a 1,03; faixa de baixo com o trajeto escrito: "Ônibus · Casarão amarelo → Bandejão da
   universidade · 30 min"; o relógio do canto avança de 15:00 a 15:30 em passos de 5 min ao longo da tela; som do meio
   (entra e sai com fade de 0,2 s) e, no fim, o som de chegada.
4. Clique, Enter ou Espaço pulam: o relógio vai direto para o valor final e o som para com fade curto.
5. O conteúdo da ação roda como no Sistemas §1.5 (`im_executar`), com o fundo do sub-local.
6. Volta ao mapa com o marcador no lugar novo.

Com "Transições: desligadas": sem caminhada e sem imagem. Aparece um cartão de texto centralizado por 1 s (pulável):
"Ônibus · Casarão amarelo → Bandejão · 30 min · 15:00 → 15:30", com o som de chegada apenas. O relógio é atualizado
de uma vez. "Tempo livre: pular" (Sistemas §1.5) não mostra o mapa, então também não há deslocamento.

---

## 8. Dados e nomes para a E4

Arquivo novo `game/data/mapa_cidade.rpy` (só dados, sem estado):

```python
define MAPA_BASE = "images/mapa/cidade_base.png"          # sem o arquivo, a tela cai na grade do Sistemas §2.4
define MAPA_LUGARES = {
    "casarao": {"nome": _("Casarão amarelo"), "bairro": "botafogo",
                "img": "images/mapa/lugares/casarao.png", "ancora": (1000, 1090), "balao": "acima",
                "voce": "esquerda", "interno": "escada"},     # interno: tela da troca de sub-local (ou None)
    # ... os 12 da seção 2
}
define MAPA_BAIRROS = {"botafogo": _("Botafogo"), ...}
define MAPA_TEMPO = {("botafogo", "fundao"): (30, "onibus"), ...}   # seção 4.2, sem ordem no par
define MAPA_TELA = {"onibus": ("bg transicao_onibus", "audio/effects/bus.ogg"), ...}
```

Nos dados de cada rota (`game/data/intermissoes/<rota>.rpy`): cada POI ganha `"lugar"` e `"sub"` (seção 3), e a rota
ganha `"lugar_base"`. A agenda pode ganhar `"atividade"` e `"longe"` (opcionais).

Estado novo (prefixo `im_`, um `default` cada): `im_lugar_atual` (id do lugar; `im_iniciar` põe o lugar-base) e
`im_trajeto_total` (minutos no caminho na intermissão, para o resumo). Preferência: `persistent.im_mapa_lista`.

Funções e telas novas: `im_trajeto(origem, destino)` → `(minutos, meio)`; `im_opcoes` passa a somar o trajeto ao
custo e a devolver o trajeto na tupla; label `im_deslocar(lugar)` (avança o relógio, soma `im_trajeto_total`, chama a
tela); telas `im_trajeto_tela` e o modo lista dentro de `im_mapa`. `im_validar_dados` confere também: todo POI tem
`lugar` existente e aceso naquela rota, todo par lugar-base → lugar tem tempo, e as combinações-chave da seção 5
(mentoria + observar no mesmo lugar) cabem no bloco de cada semana.

**Se a E4 já tiver começado com valores provisórios** (em 2026-11-02 existe um `game/data/mapa_cidade.rpy` com
`MAPA_CIDADE`, `MAPA_LUGARES`, `MAPA_BAIRROS`, `MAPA_MEIOS` e `MAPA_ATIVIDADES`), vale a estrutura que já existe; o
que este documento fixa são os valores: os 12 ids de lugar e bairro da seção 2 (no lugar de `casa`,
`escritorio_saude`, `campus`, `metro`, `tijuca` etc.), as coordenadas na base 2560x1440 (escala 0,75 para 1920x1080;
âncora no pé do sprite, não no centro), os tempos da seção 4 e os nomes de arquivo do lote de arte: base
`images/mapa/cidade_base.png`, telas de transição em `images/bg/transicao_<meio>.png` (fundos comuns, utilizáveis
também nas cenas) e os ícones `conversando`, `estudando`, `reuniao`, `celular`, `descansando`, `observando`,
`programando`, `cafe` (sem um `atendendo` separado; ver 6.3).

---

## 9. Lote de arte (E3b)

`python tools/arte/montar_mapa.py` gera `docs/arte/prompts/mapa.json` (28 tarefas) e `mapa-saidas.json`.

| Grupo | Tarefas | Referências | Saída (`posproc.py`) |
|---|---|---|---|
| Base do mapa | 1 (`mapa__base`) | `estilo-c-escritorio.png` | `images/mapa/cidade_base.png`, kind `mapa`: RGB 2560x1440 |
| Lugares | 12 (`lugar__<id>`) | `depends: mapa__base` (base como 1ª imagem) + `estilo-c-escritorio.png` (+ `empresa_exterior_manha` no prédio do campus, `fachada_instituto_tarde` no Instituto) | `images/mapa/lugares/<id>.png`, kind `lugar`: RGBA recortado, largura da tabela 2.1 |
| Ícones de atividade | 8 (`icone__<id>`) | `estilo-c-emily.png` (traço) | `images/mapa/icones/<id>.png`, kind `icone`: RGBA 192x192 |
| Marcador | 1 (`marcador__voce`) | `estilo-c-emily.png` | `images/mapa/voce.png`, kind `icone` |
| Transições | 6 (`transicao__<id>`) | `estilo-c-escritorio.png` (+ `startup_coworking_tarde` na escada) | `images/bg/transicao_<id>.png`, kind `bg`: RGB 1536x1024 |

Os kinds `mapa`, `lugar` e `icone` são novos em `tools/arte/posproc.py`; os antigos não mudaram.

Revisão: depois do pós-processamento numa pasta de revisão, montar uma captura com os 12 sprites sobre a base, nas
âncoras da tabela 2.1, e conferir perspectiva, luz e escala. Regerar o que destoar com reforço no início do prompt. Os
fundos opcionais dos documentos de rota (`startup_terraco_tarde`, `bandejao_tarde`) não estão neste lote.

---

## 10. Riscos

1. **Perspectiva e luz dos sprites diferentes da base.** Mitigação: base primeiro, base como 1ª referência de cada
   lugar, cada lugar com o próprio lote de chão (esconde a emenda), revisão por captura composta.
2. **Gerador não respeita os lotes vazios da base.** As âncoras são provisórias; a E2 mede os lotes na base gerada e
   ajusta a tabela 2.1. Se a base vier sem lotes, regerar com o reforço "doze lotes vazios" no início do prompt.
3. **Mapa poluído na torre e no campus.** Balão compacto por lugar e expandido só no foco; lado do balão por lugar.
4. **Tempo demais em transições.** Máximo de 2 s, pulável, desligável; com ~3 trajetos por intermissão, menos de
   10 s por semana.

---

## 11. Dúvidas para o orquestrador ou o usuário

1. **Aterro no Corporativo** (seção 2.3): aceitar o POI novo, ou deixar o Aterro só como cenário?
2. **Nome da cidade:** "Guanabara" só nos documentos e título "Mapa da cidade" na tela, mantendo a fala da `scene_21`
   ("trânsito do Rio de Janeiro"); ou dar nome na tela e trocar essa fala?
3. **Folga de trajeto** (seção 5): os novos horários mexem em 14 intermissões; a E5 precisa conferir as falas de
   abertura que citam hora ("Sexta, três da tarde" segue certo; as que começam 30 min antes mudam).
4. **Prédio de vidro repetido:** `empresa_exterior_manha` é hoje a fachada da equipe da Saúde e também da sede do
   Grupo Vértice. No mapa os dois são prédios diferentes (baixo no campus, torre no Centro). Se o Corporativo ganhar
   uma fachada própria depois, a torre do mapa serve de referência.
5. **Sons de metrô e elevador** ficam provisórios (`bus.ogg` e `ambiente_reuniao.ogg`) até alguém gerar ou escolher
   os definitivos.
