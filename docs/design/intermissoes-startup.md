# Intermissões da rota Startup (Trocado): design de conteúdo

Data: 2026-11-02. Branch `evolucao`. Etapa E1 (conteúdo por rota) do plano `docs/plans/2026-11-02-evolucao.md`.
Segue `docs/design/sistemas-intermissoes.md` (chamado aqui de "doc de sistemas"): formatos, custos, nomes de labels,
prefixos e regras valem como lá. Fontes da rota: `docs/rotas/startup.md` e `game/story/rota_startup/`.
Nenhum `.rpy` foi alterado. As mudanças nas cenas estão listadas na seção 11 para a E5/E6.

Escopo: jogo para aula e para jogar sozinho, completo do início ao fim. Tudo o que é obrigatório para aprender continua
nas cenas (8 registros, decisões, escrita, planejamento, ambiguidade e rastreabilidade). O tempo livre dá pistas,
amizade, registros extras, energia e o arco de mentoria.

Tom da rota: narração curta em itálico, humor leve, nenhum vilão. Jeito de falar (bíblia, seção 2): Tainá ("a gente",
"me conta", "bora", valores concretos); Otávio ("veja bem", perguntas, obra e cozinha, humor seco); Davi ("pô",
"fechou", "mano", trocadilho ruim); Lorena (listas "primeiro...", "cadê a evidência?", "oxe"); Vinícius (jargão de
startup, exclamações, números redondos); Bia (valores exatos, "égua", "tipo assim"). Narração sem adjetivo
flexionado para o jogador.

---

## 1. Mapa e locais

### 1.1 Locais (POI)

Os 7 locais vêm da tabela 2.1 do doc de sistemas (5 desde a semana 1 e 2 que abrem depois). Três deles (mesa, sala de
vidro e terraço) ficam no mesmo prédio, o casarão amarelo; no mapa da cidade isso vira um sprite com três pontos.

| id | Nome | Fundo da ação | Abre | Ações do local | Trajeto (texto da transição) |
|---|---|---|---|---|---|
| `mesa` | Mesa da equipe | `startup_coworking_tarde` (S6: `startup_coworking_noite`) | 1 | — (pessoas pela agenda) | escada de madeira do casarão |
| `sala_vidro` | Sala de vidro | `sala_reunioes_tarde` | 1 | estudar | mesmo andar, porta de vidro |
| `cafe` | Café da esquina | `empresa_cafe_tarde` | 1 | descansar (S6 também observar) | térreo do casarão |
| `terraco` | Terraço | `startup_terraco_noite` (E3: versão de tarde) | 1 | descansar | escada até o terraço |
| `ponto` | Ponto de ônibus | `transito_tarde` | 1 | descansar (caminhada) | calçadão da praia |
| `bandejao` | Bandejão da universidade | `refeitorio_tarde` (E3: `bandejao_tarde`, opcional) | 2 | observar | ônibus até o campus |
| `aceleradora` | Aceleradora Maré | `demo_day_auditorio` | 6 | — | ônibus até o Centro |

O "Café da esquina" é o café do térreo da `st_07`: fica na esquina, no térreo do próprio casarão. Os dois nomes valem.
O fundo `refeitorio_tarde` também é a copa da `st_10`; se a E3 gerar `bandejao_tarde`, o bandejão passa a usar ele.

### 1.2 Arte do mapa

Estilo C (mescla escolhida pelo usuário): ilustração com traço limpo e fino escuro, cel shading com 1 a 2 tons, cores
suaves e levemente dessaturadas, mesma luz de tarde da base do mapa (sol vindo da esquerda), vista de cima em
perspectiva leve (cerca de 30°), fundo transparente, nenhum texto legível. Os sprites seguem a base da cidade
fictícia inspirada no Rio (plano, seção "Mapa da cidade"): o polo da Startup é o casarão em Botafogo.

**Casarão amarelo (sprite único com 3 pontos: `mesa`, `sala_vidro`, `terraco`).** Casarão de dois andares do início
do século XX, fachada amarelo-ocre desbotada com frisos brancos, janelas altas em arco com venezianas verde-garrafa
abertas. No segundo andar, pelas janelas, aparece a mesa comprida de madeira clara com notebooks e três celulares num
suporte, e uma parede de vidro com post-its coloridos (coral, menta e amarelo). Portão de ferro com uma plaquinha
sem texto, bicicleta encostada no muro e uma amendoeira na calçada. No telhado, um terraço de deck de madeira com
guarda-corpo de ferro, varal de lâmpadas amarelas e vasos de manjericão. Pontos de clique: janela do meio do 2º andar
(mesa), janela de canto com reflexo de vidro (sala de vidro), terraço.
- Ícone `mesa`: notebook aberto com três celulares em pé num suporte, tela coral.
- Ícone `sala_vidro`: retângulo de vidro azul-petróleo com três post-its (coral, menta, amarelo).
- Ícone `terraco`: arco de lâmpadas amarelas sobre um vaso de manjericão.

**Café da esquina (`cafe`).** A esquina do térreo do mesmo casarão (pode ser uma camada à parte para reagir sozinha):
toldo listrado verde e creme, duas mesinhas redondas na calçada com cadeiras de ferro, vitrine com cesta de pão de
queijo, lousa de cardápio com rabiscos sem letras, xícaras na mesa. Ícone: xícara branca com vapor e um pão de queijo
ao lado.

**Ponto de ônibus (`ponto`).** Abrigo de ônibus com cobertura curva e banco, no calçadão de ondas pretas e brancas
da orla de Botafogo; palmeiras, mureta da praia e, ao fundo à esquerda, a boca de um túnel no morro (o túnel da
`st_03`). Ícone: placa de ponto com a silhueta de um ônibus e duas ondinhas embaixo.

**Bandejão da universidade (`bandejao`).** Prédio baixo de concreto aparente sobre pilotis, com um painel de azulejos
azuis geométricos na fachada, fila de estudantes de mochila até a porta, bicicletário, um ipê-amarelo no gramado e
uma escada que desce para o subsolo (onde o sinal cai). Fica no campus perto da baía, longe do casarão. Ícone: bandeja
de refeitório com prato, copo de suco e um celular apoiado na borda.

**Aceleradora Maré (`aceleradora`).** Galpão portuário reformado no Centro: tijolo aparente, portões de metal
azul-petróleo, faixa lateral com padrão geométrico azul e laranja sem palavras, um guindaste antigo pintado ao lado
e a baía ao fundo. Ícone: onda azul estilizada com uma seta laranja subindo.

Fundos opcionais para a E3 (não bloqueiam nada): `startup_terraco_tarde` (o terraço da `st_14` com luz de tarde
laranja, sem pizza e sem varal aceso) e `bandejao_tarde` (salão com mesas compridas, bandejas de inox, janelas altas e,
num canto, a escada para o subsolo de luz fria).

### 1.3 Dados do mapa

Posições provisórias na imagem do mapa (1920x1080, antes de escalar para a área do mapa); a E2/E3 ajustam sobre a base.

```python
init 3 python:
    ROUTES["startup"]["mapa"] = {
        "imagem": "images/mapas/cidade.png",   # base comum (E3b); sem ela, a tela usa a grade
        "musica": "music_office_relaxed",
        "pois": [
            {"id": "mesa", "nome": _("Mesa da equipe"), "bg": "startup_coworking_tarde",
             "pos": (740, 600), "abre": 1, "acoes": []},
            {"id": "sala_vidro", "nome": _("Sala de vidro"), "bg": "sala_reunioes_tarde",
             "pos": (800, 560), "abre": 1, "acoes": ["estudar"]},
            {"id": "cafe", "nome": _("Café da esquina"), "bg": "empresa_cafe_tarde",
             "pos": (690, 650), "abre": 1, "acoes": ["descansar"]},
            {"id": "terraco", "nome": _("Terraço"), "bg": "startup_terraco_noite",
             "pos": (770, 500), "abre": 1, "acoes": ["descansar"]},
            {"id": "ponto", "nome": _("Ponto de ônibus"), "bg": "transito_tarde",
             "pos": (600, 740), "abre": 1, "acoes": ["descansar"]},
            {"id": "bandejao", "nome": _("Bandejão da universidade"), "bg": "refeitorio_tarde",
             "pos": (1500, 260), "abre": 2, "acoes": ["observar"]},
            {"id": "aceleradora", "nome": _("Aceleradora Maré"), "bg": "demo_day_auditorio",
             "pos": (1250, 700), "abre": 6, "acoes": []},
        ],
    }
```

Na semana 6 a mesa usa `startup_coworking_noite` (campo `bg_semana: {6: "startup_coworking_noite"}` ou teste em
`im_executar`, a critério da E4).

### 1.4 Balões de atividade

O plano pede balões com retrato, ícone de atividade e uma frase. O doc de sistemas não tem esse campo, então ele entra
como chave **opcional** `"atividade": {cid: (icone, frase)}` em cada semana; sem ela, o balão mostra só os nomes.
Ícones (8, do plano): `cafe`, `estudando`, `reuniao`, `celular`, `descansando`, `atendendo`, `programando`,
`observando`. As frases estão nas tabelas de agenda da seção 3.

---

## 2. Ganchos na cadeia

Cadeia de `game/story/rota_startup/rota_startup.rpy` depois da mudança (linhas novas marcadas com `# novo`):

```renpy
label rota_startup:
    call st_01_chegada from _st_01_chegada
    call st_02_reuniao_ciclo from _st_02_reuniao_ciclo
    call im_intermissao(1) from _im_startup_s1          # novo (gancho A)
    call st_03_casa_sem1 from _st_03_casa_sem1
    call im_ponto_parada(1) from _pp_startup_s1         # novo
    call st_04_preparacao from _st_04_preparacao
    call st_05_entrevista from _st_05_entrevista
    call st_06_classificacao from _st_06_classificacao
    call st_07_social from _st_07_social
    call im_intermissao(2) from _im_startup_s2          # novo
    call st_08_casa_sem2 from _st_08_casa_sem2
    call im_ponto_parada(2) from _pp_startup_s2         # novo
    call st_09_historias from _st_09_historias
    call st_10_almoco from _st_10_almoco
    call st_11_inspecao from _st_11_inspecao
    call im_intermissao(3) from _im_startup_s3          # novo
    call st_12_casa_sem3 from _st_12_casa_sem3
    call im_ponto_parada(3) from _pp_startup_s3         # novo
    call st_13_arquitetura from _st_13_arquitetura
    call im_intermissao(4) from _im_startup_s4          # novo
    call st_14_comemoracao from _st_14_comemoracao
    call im_ponto_parada(4) from _pp_startup_s4         # novo
    call st_15_gestao from _st_15_gestao                # S5 dentro da cena (gancho B)
    call im_ponto_parada(5) from _pp_startup_s5         # novo
    call st_16_codificacao from _st_16_codificacao      # S6 dentro da cena
    call im_ponto_parada(6) from _pp_startup_s6         # novo
    call st_17_testes_seguranca from _st_17_testes_seguranca  # S7 dentro da cena
    call im_ponto_parada(7) from _pp_startup_s7         # novo
    call st_18_lancamento from _st_18_lancamento        # S8 dentro da cena
    return
```

Ganchos B (linha `call im_intermissao(N) from _im_startup_sN`, âncora por texto):

| Sem. | Arquivo / label | Entre | Dia e horário | Bloco | mesmo_dia |
|---|---|---|---|---|---|
| 5 | `st_15_gestao.rpy` / `st_15_gestao` | depois de `hide st_mentora` / `with dissolve` (após `$ set_time(16, 0)`) e antes do comentário `# Volta para casa.` | segunda 16h–19h | 180 | sim |
| 6 | `st_16_codificacao.rpy` / `st_16_codificacao` | depois dos `hide st_mobile/st_qualidade/st_techlead` + `with dissolve` que seguem `$ st_checar_conquistas()` e antes de `stop music fadeout 1.0` | terça 18h–20h30 | 150 | sim |
| 7 | `st_17_testes_seguranca.rpy` / `st_17_testes_seguranca` | depois de `hide st_qualidade` / `hide st_techlead` / `with dissolve` (após "Dado financeiro é emprestado...") e antes de `scene bg startup_coworking_tarde` | quarta 12h–14h30 | 150 | sim |
| 8 | `st_18_lancamento.rpy` / `st_18_lancamento` | depois de `hide st_qualidade` / `hide st_techlead` / `with dissolve` do bloco do pico e antes do comentário `# Quinta: todos estão juntos no demo day.` | quarta 13h30–16h30 | 180 | sim |

Ajuste de relógio: `st_16`, linha `$ set_time(19, 0)` depois de `scene bg quarto_noite` vira `$ set_time(21, 0)`.
Nenhum outro horário muda (S7: a cena já pula para 14h30; S8: a cena pula para quinta 14h20).

---

## 3. As 8 intermissões

Convenções das tabelas:
- Custos do doc de sistemas: conversar 30 min (amizade +0,5); observar 90 min, −1 energia (pista da semana + 0,5 com
  quem é observado); estudar 60 min, −1 (registro extra); descansar 60 min, +2; ajudar 90 min, −2 (amizade +1,0 +
  pista, se houver); mentoria 90 min, −1 (amizade +1,0 com Lorena + passo do arco).
- Label = nome do label de conteúdo. Pessoa: `im_startup_s<N>_<acao>_<cid>`; local: `im_startup_s<N>_<acao>_<poi>`.
  Descansar é por local e vale para todas as semanas: `im_startup_descansar_<poi>`. Mentoria: `im_startup_mentoria_<k>`.
- "Palavras" = meta do conteúdo. Tamanho de referência do doc de sistemas: conversar 8–14 falas, observar 15–25,
  estudar 6–10, ajudar 15–25, mentoria 20–30, descansar 3–6.
- Toda pista nova sai com `pista_ganhar(pid)` dentro da janela `ate_semana`. Fora dela, a cena roda igual.
- Arquivos: `game/story/intermissoes/startup/s1.rpy` … `s8.rpy` (labels da semana; `s1.rpy` também guarda os três
  `im_startup_descansar_*`) e `mentoria.rpy`.

### Descansar (todas as semanas)

| Label | Conteúdo | Palavras |
|---|---|---|
| `im_startup_descansar_cafe` | Pão de queijo saindo do forno e o barulho da máquina de espresso. Normal: o jogador olha a rua e anota uma coisa boa da semana. Com `energia_cansaco()`: a atendente deixa um café a mais na mesa sem cobrar ("tá com cara de quem precisa"). | 60 + 40 |
| `im_startup_descansar_terraco` | Vista do Pão de Açúcar entre os prédios e os vasos de manjericão do Otávio. Normal: o jogador rega o manjericão, que tem um cartãozinho "não arrancar, assinado: O.". Cansaço: deita no puff e cochila dez minutos. Semana 6 (noite): o varal de lâmpadas acende sozinho às 19h. | 60 + 40 |
| `im_startup_descansar_ponto` | Caminhada pelo calçadão até o ponto, sem fone. Semana 1: o ônibus entra no túnel e o sinal do celular cai para uma barrinha (prenúncio da `st_03`, sem pista). Demais semanas: o mar, um vendedor de mate, o jogador volta mais leve. Cansaço: senta no banco do ponto e deixa passar três ônibus. | 60 + 40 |

### Semana 1 · Sexta, 15h–17h · bloco 120 (tutorial)

Gancho A: entre `st_02_reuniao_ciclo` e `st_03_casa_sem1`. `mesmo_dia` não (a `st_02` é quarta). A `st_03` começa às
19h30 no ônibus e não muda.

**Abertura (tutorial, Tainá, 6 falas):**
1. "Sexta, três da tarde, e a semana já rendeu. Aqui a tarde de sexta é livre: cada um escolhe onde pôr o tempo."
2. "Esse é o mapa. Cada lugar mostra quem está lá e o que dá para fazer. Toda ação custa minutos, e o relógio não volta."
3. "Ajudar alguém e observar gente usando o app cansam mais. Sua energia fica embaixo do relógio. Descansar também é escolha, viu?"
4. "Às vezes você vai ver alguma coisa que vira pista. Ela pode ajudar numa conversa mais para frente."
5. "E o mais importante: nada aqui é obrigatório para aprender. O que precisa, a gente faz junto durante a semana. Isso aqui é o seu tempo."
6. "Hoje são duas horas. Não dá para fazer tudo. Escolher já é metade do trabalho."

**Agenda**

| Local | Quem (balão) | Ações |
|---|---|---|
| mesa | Davi (`programando`, "Davi esperando o build no celular que trava"), Otávio (`programando`, "Otávio revisando um PR, caneca na mão") | conversar Davi, **ajudar Davi**, conversar Otávio |
| sala_vidro | Tainá (`estudando`, "Tainá reorganizando a coluna de descoberta") | conversar Tainá, estudar |
| cafe | Lorena (`cafe`, "Lorena lendo avaliações com um café") | conversar Lorena, descansar |
| terraco | Vinícius (`celular`, "Vinícius ensaiando o pitch para os vasos de planta") | conversar Vinícius, descansar |
| ponto | — | descansar |

**Ações**

| Label | Custo | Resultado | Conteúdo e falas-chave | Palavras |
|---|---|---|---|---|
| `im_startup_s1_conversar_st_mobile` | 30 | +0,5 Davi | Davi apresenta os três celulares de teste pelo apelido: Foguete, Tartaruga e Tijolo. O Tijolo é o modelo que mais aparece nas avaliações do beta (a Lorena conferiu). "O Tijolo é meu chefe. Se ele aprova, ninguém reclama." Trocadilho: "Celular de teste não tira férias. No máximo, tira print." | 150 |
| `im_startup_s1_ajudar_st_mobile` | 90, −2 | +1,0 Davi; sem pista | O jogador monta o projeto no próprio notebook e roda o app no Tijolo: o build leva seis minutos. Davi mostra o caminho de um gasto, do toque em Salvar até a lista, e a pasta de testes com só três arquivos. O primeiro commit do jogador corrige um texto de botão ("Salva" vira "Salvar"). "Seis minutos pra ver uma vírgula mudar. Por isso a gente testa antes, e não no olho." | 300 |
| `im_startup_s1_conversar_st_techlead` | 30 | +0,5 Otávio | A caneca esmaltada foi presente da primeira equipe dele, em 1998: "a única coisa daquela época que nunca deu bug". Ele desenha num guardanapo o caminho do dado: celular, nuvem, banco. "Veja bem: se não cabe num guardanapo, você ainda não entendeu o sistema." | 140 |
| `im_startup_s1_conversar_st_mentora` | 30 | +0,5 Tainá | Tainá mostra o caderno laranja: post-it coral para dúvida de usuário, amarelo para dúvida técnica, verde para "já sei". Pergunta a dúvida da semana do jogador e cola um post-it coral para levar à entrevista de segunda. "Dúvida anotada vira pergunta de entrevista. Dúvida só lembrada some na sexta." | 150 |
| `im_startup_s1_estudar_sala_vidro` | 60, −1 | extra `st_extra_kanban` | O jogador conta os cartões em "Fazendo" no quadro da parede e lê sobre limite de trabalho em andamento. Tainá passa e só comenta: "Repara quantos cartões estão parados esperando alguém." Termina com o registro extra. | 130 |
| `im_startup_s1_conversar_st_qualidade` | 30 | +0,5 Lorena | Lorena guarda num caderninho as frases mais estranhas das avaliações ("o app me julgou pelo café"). Ensina o jogo dela: achar o verbo escondido na queixa. "Primeiro, ache o verbo. 'Meu total está errado' esconde 'conferir'. Segundo, pergunte quando foi." | 150 |
| `im_startup_s1_conversar_st_ceo` | 30 | +0,5 Vinícius | Vinícius ensaia o pitch para os vasos de manjericão e pede a opinião do jogador. O primeiro investidor dele disse não em quatro minutos. "Ele perguntou quem voltava a usar. Eu não sabia. Nunca mais vou não saber!" | 150 |

Pistas: nenhuma. Registro extra: `st_extra_kanban`.

### Semana 2 · Sexta, 15h–18h · bloco 180

Gancho A: entre `st_07_social` e `st_08_casa_sem2`. `mesmo_dia` não (a `st_07` é quinta). O bandejão abre.

**Abertura:** "{i}Sexta, três da tarde. A semana teve roteiro, entrevista e post-its. Um lugar novo aparece no mapa: o
bandejão da universidade, onde a Bia almoça e estuda.{/i}" Cansaço (vale para todas as semanas, com a hora do dia):
"{i}Você boceja antes de abrir o mapa. Hoje o tempo livre vai ser mais curto.{/i}"

**Agenda**

| Local | Quem (balão) | Ações |
|---|---|---|
| mesa | Otávio (`programando`, "Otávio passando decisões antigas a limpo"), Davi (`celular`, "Davi testando o app no Tijolo") | **ajudar Otávio**, conversar Otávio, conversar Davi |
| sala_vidro | Vinícius (`reuniao`, "Vinícius saindo de uma call com o fundo") | conversar Vinícius, estudar |
| cafe | Tainá (`cafe`, "Tainá relendo as anotações da entrevista") | conversar Tainá, descansar |
| bandejao | Bia (`estudando`, "Bia estudando Cálculo com um suco"), Lorena ★ (`observando`, "Lorena com a Bia e duas amigas dela") | conversar Bia, conversar Lorena, **observar** (`st_p_cancelar`), mentoria |
| terraco, ponto | — | descansar |

**Ações**

| Label | Custo | Resultado | Conteúdo e falas-chave | Palavras |
|---|---|---|---|---|
| `im_startup_s2_ajudar_st_techlead` | 90, −2 | +1,0 Otávio; sem pista | Otávio começa um registro de decisões: uma página por decisão, com contexto, opção escolhida e o que se perde. O jogador passa a limpo três decisões antigas: funções na nuvem em vez de servidor ligado, app que funciona sem internet, React Native. Na terceira ninguém lembra o porquê. "Viu? Decisão sem registro vira lenda." "Registro de decisão é carta pro você de daqui a seis meses." | 300 |
| `im_startup_s2_conversar_st_techlead` | 30 | +0,5 Otávio | Otávio pergunta como foi a entrevista, escuta calado e faz uma pergunta só: "Ela disse a hora?" Comenta que história boa tem hora e lugar, e bug também. Prepara a mensagem que ele manda à noite na `st_08`, sem pedir o horário ainda. | 140 |
| `im_startup_s2_conversar_st_mobile` | 30 | +0,5 Davi | Davi conta o primeiro bug dele em produção: o gasto lançado às 23h50 caía no dia seguinte por causa do fuso. Convida de novo para a partida de sábado. "Mano, o tempo é o pior inimigo do programador. Fuso, relógio e prazo." | 140 |
| `im_startup_s2_conversar_st_ceo` | 30 | +0,5 Vinícius | Depois da call, Vinícius pergunta, sem jeito, o que a Bia achou dele. Conta da mãe contando moeda no fim do mês. "Eu falo 'tração' porque é a língua do fundo. Mas quando fecho o olho, penso na minha mãe contando moeda." | 150 |
| `im_startup_s2_estudar_sala_vidro` | 60, −1 | extra `st_extra_episodio` | O jogador relê o roteiro de segunda e marca quais perguntas abriram a conversa e quais fecharam. | 130 |
| `im_startup_s2_conversar_st_mentora` | 30 | +0,5 Tainá | Tainá relê as anotações da entrevista e conta o truque dela para conflito: voltar ao problema e repetir com as palavras da pessoa. "Quando duas pessoas brigam por solução, eu volto pro problema. Ninguém briga pelo problema." | 150 |
| `im_startup_s2_conversar_st_estudante` | 30 | +0,5 Bia | Bia conta da avó, no Rio Negro, onde sinal de celular é luxo; ela aprendeu cedo a anotar tudo no papel, daí o caderno. Mostra o chaveiro de boto, presente da avó. "Tipo assim: o caderno nunca ficou sem sinal." | 150 |
| `im_startup_s2_observar_bandejao` | 90, −1 | pista `st_p_cancelar`; +0,5 Bia | Quarenta minutos só olhando. Bia lança o bandejão (R$ 4,50) com uma mão, a bandeja na outra. Começa a lançar um suco de R$ 6, a amiga paga, ela toca em Cancelar e logo confere a lista e depois o caderno. Abre o total três vezes em vinte minutos. Depois ela explica: "Depois do almoço duplicado, toda vez que eu desisto eu confiro se nada mudou." Lorena, baixinho: "Ninguém conta isso numa entrevista." | 300 |
| `im_startup_s2_conversar_st_qualidade` | 30 | +0,5 Lorena | Lorena defende o bandejão ("R$ 4,50 com suco, oxe, melhor negócio do Rio") e fala da parte difícil de observar: ficar quieta quando a pessoa erra. "Se eu ajudo, eu aprendo como eu uso o app. Não como ela usa." | 140 |
| mentoria (`im_startup_mentoria_<k>`) | 90, −1 | +1,0 Lorena; passo do arco | Seção 6. Na S2 só o encontro 1 está liberado. | — |

Pistas: `st_p_cancelar`. Registro extra: `st_extra_episodio`.

### Semana 3 · Sexta, 15h–18h · bloco 180

Gancho A: entre `st_11_inspecao` e `st_12_casa_sem3`. `mesmo_dia` não (a `st_11` é quarta).

**Abertura:** "{i}Sexta, três da tarde. A especificação passou pela lupa da Lorena na quarta. Na parede de vidro, um
post-it sozinho na coluna de perguntas abertas: \"e se ela excluir sem internet?\".{/i}"

**Agenda**

| Local | Quem (balão) | Ações |
|---|---|---|
| mesa | Davi (`programando`, "Davi ligando o protótipo da confirmação"), Tainá (`estudando`, "Tainá escrevendo critérios") | conversar Davi, conversar Tainá |
| sala_vidro | Otávio (`programando`, "Otávio cruzando registros do servidor") | conversar Otávio, estudar |
| cafe | Vinícius (`estudando`, "Vinícius lendo um livro de métricas") | conversar Vinícius, descansar |
| bandejao | Bia (`estudando`, "Bia no subsolo, estudando para a prova"), Lorena ★ | conversar Bia, conversar Lorena, **observar** (`st_p_tunel`), mentoria |
| terraco, ponto | — | descansar |

**Ações**

| Label | Custo | Resultado | Conteúdo e falas-chave | Palavras |
|---|---|---|---|---|
| `im_startup_s3_conversar_st_mobile` | 30 | +0,5 Davi | Davi fala do pareamento de segunda e do sonho de fazer um jogo de ritmo sobre pegar ônibus. "Quando você navega, eu erro menos. Quando eu navego, você pergunta mais. Todo mundo ganha." | 140 |
| `im_startup_s3_conversar_st_mentora` | 30 | +0,5 Tainá | Tainá mostra a coluna "perguntas abertas" do quadro e diz que não vai chutar a resposta do Davi; ela espera o Otávio. "Pergunta aberta não é falha. Falha é chutar a resposta e esquecer que chutou." | 140 |
| `im_startup_s3_conversar_st_techlead` | 30 | +0,5 Otávio | Otávio cruza o horário que o jogador mandou com os registros do servidor e não conta o que achou. "Achei uma coisa no registro daquele minuto. Segunda, com o Davi e três celulares, eu te mostro. Bug se mostra reproduzindo, não contando." Fecha com uma comparação de cozinha: provar o molho antes de servir. | 150 |
| `im_startup_s3_estudar_sala_vidro` | 60, −1 | extra `st_extra_invest` | O jogador passa as três versões da história da `st_09` pela lista INVEST e anota onde cada uma falha. | 140 |
| `im_startup_s3_conversar_st_ceo` | 30 | +0,5 Vinícius | Vinícius lê um livro de métricas de capa laranja para a segunda reunião com o fundo. "Sublinhei a palavra 'vaidade' três vezes. Acho que o livro tava falando comigo!" | 140 |
| `im_startup_s3_conversar_st_estudante` | 30 | +0,5 Bia | Bia é monitora de Cálculo e explica derivada com dinheiro. "Égua, derivada é só quanto o saldo cai por dia. Isso eu entendo bem." | 140 |
| `im_startup_s3_observar_bandejao` | 90, −1 | pista `st_p_tunel`; +0,5 Bia | No subsolo do bandejão, onde a Bia estuda, o 4G cai. Ela lança de propósito dois sucos de R$ 6, um dela e um da colega Rayane. Depois lança o bandejão de R$ 4,50, a tela trava, ela toca em Salvar de novo e aparecem dois. "Égua, de novo." Ela anota no caderno: "duplicou no subsolo". Na lista, as duas duplas parecem iguais. | 300 |
| `im_startup_s3_conversar_st_qualidade` | 30 | +0,5 Lorena | Lorena conta do São João de Campina Grande e de como a fila da quadrilha ensinou a ela a observar gente. "Oxe, quem organiza quadrilha sabe testar fluxo: sempre tem um par que entra na hora errada." | 140 |
| mentoria | 90, −1 | +1,0 Lorena; passo | Encontros 1 ou 2. | — |

Pistas: `st_p_tunel`. Registro extra: `st_extra_invest`.

### Semana 4 · Sexta, 15h–18h · bloco 180

Gancho A: entre `st_13_arquitetura` e `st_14_comemoracao`. `mesmo_dia` não. A festa começa às 18h, e a `st_14` diz que
a notícia dos mil correu às 15h: a abertura usa isso.

**Abertura:** "{i}Sexta, três da tarde. O grupo da equipe explode de mensagens: o beta passou de mil estudantes.
Vinícius já encomendou pizza. O terraço fechou para arrumar a festa das seis.{/i}"

**Agenda**

| Local | Quem (balão) | Ações |
|---|---|---|
| mesa | Davi (`programando`, "Davi montando a fila com id único") | conversar Davi |
| sala_vidro | Vinícius (`reuniao`, "Vinícius e Tainá escrevendo o post dos mil"), Tainá | conversar Vinícius, conversar Tainá, estudar |
| cafe | Otávio (`cafe`, "Otávio fugindo do barulho com um café") | conversar Otávio, descansar |
| terraco | fechado: "Fechado: arrumando a festa" | — |
| bandejao | Bia (`celular`, "Bia mostrando o app para a república"), Lorena ★ | conversar Bia, conversar Lorena, **observar** (`st_p_bolsa`), mentoria |
| ponto | — | descansar |

**Ações**

| Label | Custo | Resultado | Conteúdo e falas-chave | Palavras |
|---|---|---|---|---|
| `im_startup_s4_conversar_st_mobile` | 30 | +0,5 Davi | Davi monta o id único na fila ("o número do pedido da pizza") e pede sugestão para a playlist da festa. "Ia pôr uma música chamada 'Duas vezes'. Brincadeira. Talvez." | 140 |
| `im_startup_s4_conversar_st_ceo` | 30 | +0,5 Vinícius | Vinícius, eufórico, pede ajuda com o post dos mil. Se o jogador perguntar quantos voltam, ele murcha um pouco e responde com honestidade. "Mil! ... Tá, tá: quantos voltam. Segunda a gente olha. Hoje deixa eu sorrir!" | 150 |
| `im_startup_s4_conversar_st_mentora` | 30 | +0,5 Tainá | Tainá pergunta como foi negociar com o Vinícius na segunda e lê o acordo registrado. Variante por `st_acordo_opcao`: "base primeiro" ("o protótipo do consentimento já tem dono: uma tarde do Davi") ou "investigar agora" ("o Otávio já marcou a primeira call com a instituição"). "Acordo bom é aquele que os dois contam do mesmo jeito uma semana depois." | 160 |
| `im_startup_s4_estudar_sala_vidro` | 60, −1 | extra `st_extra_idempotencia` | Com o diagrama da `st_13` ainda no vidro, o jogador escreve numa página a diferença entre "excluir o gasto X" e "somar R$ 20 ao total". | 140 |
| `im_startup_s4_conversar_st_techlead` | 30 | +0,5 Otávio | Otávio não gosta de barulho e veio ao café antes da festa. Conta da filha que estuda Física em Niterói e do manjericão no terraço. "Festa eu frequento como servidor: ligado, mas em modo econômico." | 140 |
| `im_startup_s4_conversar_st_estudante` | 30 | +0,5 Bia | Metade da república da Bia baixou o app hoje. Ela tem medo de que dê erro com as amigas. "Se duplicar pra elas, eu mudo de república." | 140 |
| `im_startup_s4_observar_bandejao` | 90, −1 | pista `st_p_bolsa`; +0,5 Bia | Na mesa da Bia, cinco estudantes. O jogador anota quem abre o app e quando. Três só abrem no dia em que a bolsa cai; duas instalaram esta semana pelo boca a boca e nunca lançaram nada; só a Bia lança todo dia. Rayane: "Eu só abro no dia 10, pra ver quanto tenho. Depois dá medo." | 300 |
| `im_startup_s4_conversar_st_qualidade` | 30 | +0,5 Lorena | Lorena montou a lista de quem mais mandou feedback, com a Bia em primeiro, e vai levar para a festa. "Quase ninguém agradece a quem reclama direitinho. Hoje eu agradeço." | 140 |
| mentoria | 90, −1 | +1,0 Lorena; passo | Encontros 1 a 3. | — |

Pistas: `st_p_bolsa`. Registro extra: `st_extra_idempotencia`.

### Semana 5 · Segunda, 16h–19h · bloco 180

Gancho B na `st_15` (seção 2). `mesmo_dia` sim. O planejamento, os riscos e a métrica já aconteceram de manhã; a
intermissão não repete a conversa da Tainá sobre pressão (ela está na cena).

**Abertura:** "{i}Segunda, quatro da tarde. O plano das três últimas semanas está no quadro: dois itens e três
riscos, cada um com dono. O resto da tarde é seu.{/i}"

**Agenda**

| Local | Quem (balão) | Ações |
|---|---|---|
| mesa | Otávio (`programando`, "Otávio olhando o painel do banco da noite da festa"), Davi (`programando`, "Davi caçando um erro na fila de sincronização") | **ajudar Otávio** (`st_p_conexoes`), **ajudar Davi** (`st_p_logs`), conversar com os dois |
| sala_vidro | Tainá (`estudando`, "Tainá atualizando a lista de riscos") | conversar Tainá, estudar |
| cafe | Vinícius (`celular`, "Vinícius refazendo o slide principal") | conversar Vinícius, descansar |
| bandejao | Bia (`atendendo`, "Bia ajudando a Rayane com o app"), Lorena ★ | conversar Bia, conversar Lorena, observar (só cena), mentoria |
| terraco, ponto | — | descansar |

**Ações**

| Label | Custo | Resultado | Conteúdo e falas-chave | Palavras |
|---|---|---|---|---|
| `im_startup_s5_ajudar_st_techlead` | 90, −2 | +1,0 Otávio; pista `st_p_conexoes` | Otávio é o dono do risco do pico e abre o painel do banco da noite da festa dos mil. O jogador acha o gráfico de conexões: 80% do limite com umas duzentas pessoas ao mesmo tempo. Otávio explica que cada função que acorda abre a própria conexão. "Veja bem: a festa quase achou o limite com duzentas pessoas. Anota aí, que esse risco é meu." | 300 |
| `im_startup_s5_conversar_st_techlead` | 30 | +0,5 Otávio | Otávio comenta o planejamento da manhã. "Dizer não para medalha é o trabalho mais difícil desta empresa. E o mais barato." | 130 |
| `im_startup_s5_ajudar_st_mobile` | 90, −2 | +1,0 Davi; pista `st_p_logs` | Uma falha na fila trava o envio quando o app fecha no meio. O jogador ajuda a reproduzir no Tijolo e abre o relatório de falhas: cada erro vai para o serviço de monitoramento com o e-mail da pessoa junto. Davi: "Pô, depois eu tiro isso. Anota pra me cobrar." Corrigem a falha da fila; o e-mail fica para depois. | 300 |
| `im_startup_s5_conversar_st_mobile` | 30 | +0,5 Davi | As medalhas foram para "Depois da 1.0", e Davi já tinha desenhado os ícones. "Fiz doze medalhas. Doze! Tá, tá, depois da 1.0." O jogador pode rir junto ou consolar; o efeito é o mesmo. | 140 |
| `im_startup_s5_conversar_st_mentora` | 30 | +0,5 Tainá | Tainá conta do tempo no banco, quando trabalhava doente para bater meta. "No banco eu achava que cansaço era prova de dedicação. Era só cansaço." Prepara o tema de energia das semanas finais. | 150 |
| `im_startup_s5_estudar_sala_vidro` | 60, −1 | extra `st_extra_coorte` | O jogador refaz o gráfico de retenção da `st_15` separando quem entrou antes e depois da festa dos mil. | 140 |
| `im_startup_s5_conversar_st_ceo` | 30 | +0,5 Vinícius | O slide grande agora é de retenção. A mãe liga e ele pede que o jogador explique "retenção" numa frase. "Mãe, é quantos voltam. Isso. Não, não é empréstimo!" | 150 |
| `im_startup_s5_conversar_st_estudante` | 30 | +0,5 Bia | Bia vai ter sessenta calouros na monitoria no semestre e está nervosa. "Tipo assim: eu ainda lembro de quando eu era a perdida." | 140 |
| `im_startup_s5_observar_bandejao` | 90, −1 | sem pista; +0,5 Bia | Rayane está sem dados no pré-pago (o 4G dela acaba todo dia 20). Ela lança um café sem internet e a rodinha gira sem dizer nada. "Salvou ou não salvou? A rodinha não me diz nada." Bia mostra que o app guarda no celular, mas nenhuma das duas tem certeza. O jogador anota: falta um aviso de "salvo no celular, enviando" (é a melhoria que a Lorena cita no final "bom" da `st_18`). | 280 |
| `im_startup_s5_conversar_st_qualidade` | 30 | +0,5 Lorena | Lorena explica por que pôs o leitor de tela na definição de pronto. Com o encontro 3 feito: "Foi a Joana que me convenceu, no clube." Sem ele: "Leitor de tela não é extra. Tem gente que só usa assim." | 140 |
| mentoria | 90, −1 | +1,0 Lorena; passo | Encontros 1 a 4. | — |

Pistas: `st_p_conexoes`, `st_p_logs`. Registro extra: `st_extra_coorte`.

### Semana 6 · Terça, 18h–20h30 · bloco 150 (noite)

Gancho B na `st_16` (seção 2). `mesmo_dia` sim. A Aceleradora abre. O bandejão fecha à noite.

**Abertura:** "{i}Terça, seis da tarde. Os dois PRs passaram no celular da Lorena. O coworking esvazia, mas quase
ninguém foi para casa. No mapa, um lugar novo: a Aceleradora Maré, onde o Vinícius ensaia o pitch hoje.{/i}"

**Agenda**

| Local | Quem (balão) | Ações |
|---|---|---|
| mesa (noite) | Davi (`programando`, "Davi tirando prints para as lojas"), Otávio (`programando`, "Otávio preparando o teste de carga") | **ajudar Davi** (`st_p_loja`), **ajudar Otávio** (`st_p_conexoes`), conversar com os dois |
| sala_vidro | — (luz apagada, uma luminária acesa) | estudar |
| cafe | Bia e duas testers (`observando`, "Bia, Joana e Rayane testando a versão nova") | conversar Bia, **observar** (só cena), descansar |
| terraco | Tainá (`descansando`, "Tainá respirando depois de uma reunião"), Lorena ★ (`estudando`, "Lorena anotando o teste com calouros") | conversar Tainá, conversar Lorena, mentoria, descansar |
| bandejao | fechado: "Fechado à noite" | — |
| aceleradora | Vinícius (`reuniao`, "Vinícius ensaiando o pitch no palco") | **ajudar Vinícius** (`st_p_retencao`), conversar Vinícius |
| ponto | — | descansar |

**Ações**

| Label | Custo | Resultado | Conteúdo e falas-chave | Palavras |
|---|---|---|---|---|
| `im_startup_s6_ajudar_st_mobile` | 90, −2 | +1,0 Davi; pista `st_p_loja` | O jogador monta com o Davi os prints das lojas com dados fictícios (nada de gasto real de estudante) e a lista de envio. No histórico de envios: a última versão do beta ficou dois dias em revisão no Google, e uma anterior voltou rejeitada por falta do link da política de privacidade. "Dois dias de fila e uma rejeição por causa de um link. Loja não tem pressa nenhuma." | 300 |
| `im_startup_s6_conversar_st_mobile` | 30 | +0,5 Davi | Davi come o resto da pizza fria da geladeira e comemora o PR pequeno. "PR pequeno, noite tranquila. Quem diria." | 130 |
| `im_startup_s6_ajudar_st_techlead` | 90, −2 | +1,0 Otávio; pista `st_p_conexoes` (se ainda não tem) | Otávio monta a ferramenta do teste de carga com dados fictícios e roda um ensaio com cinquenta usuários virtuais. As conexões do banco saltam de dez para sessenta. "Cinquenta pessoas de mentira e o banco já sentiu. O cenário de verdade quem define é você, semana que vem." Se o jogador já tem a pista, Otávio cita a noite da festa e o conteúdo segue igual. | 300 |
| `im_startup_s6_conversar_st_techlead` | 30 | +0,5 Otávio | Otávio já avisou que às nove fecha o notebook, aconteça o que acontecer. "Não publico na sexta e não fico depois das nove. As duas regras nasceram no mesmo dia." | 130 |
| `im_startup_s6_estudar_sala_vidro` | 60, −1 | extra `st_extra_carga` | Na sala escura, com uma luminária, o jogador lê sobre teste de carga e desenha o que mediria além do tempo. | 130 |
| `im_startup_s6_conversar_st_estudante` | 30 | +0,5 Bia | Bia apresenta (ou reapresenta) Joana e Rayane e convida o jogador para o teste do clube de sexta. "Égua, a gente virou equipe de qualidade sem salário." | 140 |
| `im_startup_s6_observar_cafe` | 90, −1 | sem pista; +0,5 Bia | O jogador observa as três testando a versão que vai para as lojas. Joana navega pelo leitor de tela e ouve o rótulo novo da lixeira; Rayane cancela uma exclusão no 4G fraco e confere que nada mudou. Se não houve encontro 1, Bia apresenta as duas em duas falas. Fecha com Bia sorrindo para o total. | 280 |
| `im_startup_s6_conversar_st_mentora` | 30 | +0,5 Tainá | Tainá chegou de uma reunião na aceleradora e confessa o nervoso com a 1.0. Conta o ritual da revisão de sexta com bolo. "Ninguém aqui precisa virar a noite. Bolo na sexta, sim." | 140 |
| `im_startup_s6_conversar_st_qualidade` | 30 | +0,5 Lorena | Lorena conta o teste de hoje com calouros (o que ela cita na `st_16`): quatro de cinco acharam que o "+" era para adicionar dinheiro, não gasto. "Oxe, nunca tinha pensado: pra quem chega, '+' é dinheiro entrando." | 150 |
| `im_startup_s6_ajudar_st_ceo` | 90, −2 | +1,0 Vinícius; pista `st_p_retencao` | O jogador cronometra o pitch (devia ter 3 min, deu 4 min 40). A mentora da aceleradora, ex-investidora, ouve tudo e faz uma pergunta só: quantos dos que entraram há um mês ainda usam. Vinícius corta quatro slides. "Ela ouviu quatro minutos de mim e perguntou uma coisa só." | 300 |
| `im_startup_s6_conversar_st_ceo` | 30 | +0,5 Vinícius | Primeira vez no palco da Maré. Vinícius admite medo de palco. "Pitch eu faço dormindo. Acordado é que é difícil!" | 130 |
| mentoria (terraço) | 90, −1 | +1,0 Lorena; passo | Encontros 1 a 5. Com `im_semana_atual == 6`, a primeira fala do encontro muda para o terraço (seção 6). | — |

Pistas: `st_p_loja`, `st_p_conexoes`, `st_p_retencao`. Registro extra: `st_extra_carga`.

### Semana 7 · Quarta, 12h–14h30 · bloco 150 (almoço)

Gancho B na `st_17` (seção 2). `mesmo_dia` sim. A manhã já teve teste de carga, token e exclusão de conta. A versão 1.0
vai para as lojas nesta quarta (a `st_18` diz "na quarta passada").

**Abertura:** "{i}Quarta, meio-dia. De manhã vocês decidiram o teste de carga, o cofre do token e a exclusão de conta.
Hoje à tarde a 1.0 vai para as lojas. Duas horas e meia de almoço pela frente.{/i}"

**Agenda**

| Local | Quem (balão) | Ações |
|---|---|---|
| mesa | Otávio (`programando`, "Otávio comendo marmita de olho no teste de carga") | conversar Otávio |
| sala_vidro | Davi (`programando`, "Davi preenchendo os formulários das lojas") | **ajudar Davi** (`st_p_loja`), conversar Davi, estudar |
| cafe | Tainá (`estudando`, "Tainá reescrevendo o texto de exclusão de conta") | conversar Tainá, descansar |
| bandejao | Bia (`celular`, "Bia na fila do bandejão"), Lorena ★ | conversar Bia, conversar Lorena, observar (só cena), mentoria |
| aceleradora | Vinícius (`reuniao`, "Vinícius no segundo ensaio") | **ajudar Vinícius** (`st_p_retencao`), conversar Vinícius |
| terraco, ponto | — | descansar |

**Ações**

| Label | Custo | Resultado | Conteúdo e falas-chave | Palavras |
|---|---|---|---|---|
| `im_startup_s7_conversar_st_techlead` | 30 | +0,5 Otávio | Otávio conta o causo de 2009 inteiro (a `st_18` volta a ele): numa sexta às seis, tudo junto, banco novo, tela nova e cobrança nova; às sete caiu e às onze ele ainda estava lá, sozinho. "Por isso: nada na sexta, nada tudo junto." | 160 |
| `im_startup_s7_ajudar_st_mobile` | 90, −2 | +1,0 Davi; pista `st_p_loja` (se ainda não tem) | O jogador preenche com o Davi o formulário de segurança de dados das lojas (o que o app coleta, para quê, como apaga) e confere o link da política de privacidade. No histórico, a última versão levou dois dias em revisão. "Envia hoje e reza. Brincadeira: envia hoje e acompanha." | 300 |
| `im_startup_s7_conversar_st_mobile` | 30 | +0,5 Davi | Davi está nervoso com o envio. Trocadilho: "Se a loja rejeitar, a gente não se loja. Desculpa, saiu." | 130 |
| `im_startup_s7_estudar_sala_vidro` | 60, −1 | extra `st_extra_rollout` | Enquanto o Davi preenche formulário, o jogador lê como funciona a liberação em etapas em cada loja. | 140 |
| `im_startup_s7_conversar_st_mentora` | 30 | +0,5 Tainá | Tainá reescreve em linguagem simples o texto da tela de exclusão de conta e pede que o jogador leia em voz alta. "Se você lê em voz alta e tropeça, a Bia também tropeça." | 150 |
| `im_startup_s7_conversar_st_estudante` | 30 | +0,5 Bia | Bia agradece a resposta sobre apagar a conta (a mensagem da manhã). "A Rayane quase chorou de alívio. Ela achava que o app ia guardar tudo pra sempre." | 140 |
| `im_startup_s7_observar_bandejao` | 90, −1 | sem pista; +0,5 Bia | O almoço da universidade às 12h10: fila até a escada e quarenta pessoas lançando o almoço ao mesmo tempo. Se `st_d17_carga`: "É o horário que você simulou de manhã." Senão: "É o horário que a Lorena te ajudou a escolher de manhã." Bia conta que no primeiro dia de aula a fila dobra. | 280 |
| `im_startup_s7_conversar_st_qualidade` | 30 | +0,5 Lorena | Lorena mostra o caderninho de frases com a primeira avaliação de cinco estrelas de uma tester: "agora eu confio no total". "Primeiro: guardei. Segundo: vou reler no dia ruim." | 140 |
| `im_startup_s7_ajudar_st_ceo` | 90, −2 | +1,0 Vinícius; pista `st_p_retencao` (se ainda não tem) | Segundo ensaio, agora só perguntas e respostas. A mentora da aceleradora repete a pergunta do primeiro ensaio e mais nenhuma. O jogador anota a resposta que o Vinícius dá. | 300 |
| `im_startup_s7_conversar_st_ceo` | 30 | +0,5 Vinícius | Vinícius pergunta se o jogador fica para o demo day e conta que vai levar a mãe. "Ela vai sentar na primeira fila e filmar na vertical. Já aceitei." | 130 |
| mentoria | 90, −1 | +1,0 Lorena; passo | Encontros 1 a 5. | — |

Pistas: `st_p_loja`, `st_p_retencao`. Registro extra: `st_extra_rollout`.

### Semana 8 · Quarta, 13h30–16h30 · bloco 180

Gancho B na `st_18` (seção 2). `mesmo_dia` sim. Primeiro dia do semestre, depois do pico. Sem estudar (os extras são
das semanas 1 a 7). É a última chance de concluir a mentoria e de ganhar `st_p_retencao` para o demo day.

**Abertura:** com `st_d17_carga`: "{i}Quarta, uma e meia. O pico do primeiro dia passou sem ninguém notar. Amanhã é o
demo day.{/i}" Sem: "{i}Quarta, uma e meia. O pico passou depois de vinte minutos de aperto. Amanhã é o demo day.{/i}"

**Agenda**

| Local | Quem (balão) | Ações |
|---|---|---|
| mesa | Davi (`celular`, "Davi de olho no painel"), Otávio (`programando`, "Otávio com o painel e a caneca") | conversar Davi, conversar Otávio |
| sala_vidro | Tainá (`estudando`, "Tainá rascunhando a retrospectiva") | conversar Tainá (sem estudar nesta semana) |
| cafe | — | descansar |
| bandejao | Bia (`atendendo`, "Bia com os calouros da monitoria"), Lorena ★ (`observando`, "Lorena observando calouros") | conversar Bia, conversar Lorena, observar (só cena), mentoria |
| aceleradora | Vinícius (`reuniao`, "Vinícius no ensaio geral") | **ajudar Vinícius** (`st_p_retencao`), conversar Vinícius |
| terraco, ponto | — | descansar |

**Ações**

| Label | Custo | Resultado | Conteúdo e falas-chave | Palavras |
|---|---|---|---|---|
| `im_startup_s8_conversar_st_mobile` | 30 | +0,5 Davi | Davi ainda está elétrico com o pico. "Hoje três mil pessoas usaram um botão que eu fiz. Três mil, mano." | 130 |
| `im_startup_s8_conversar_st_techlead` | 30 | +0,5 Otávio | Com `st_d17_carga`: "O melhor pico é o que ninguém nota." Sem: "Vinte minutos de gente esperando a lista. Teste que acha problema só ajuda se a correção entra antes. Aprendi de novo hoje, aos cinquenta." | 140 |
| `im_startup_s8_conversar_st_mentora` | 30 | +0,5 Tainá | Tainá rascunha a retrospectiva das oito semanas e pergunta o que o jogador faria diferente na próxima volta. "Retrospectiva não é tribunal. É pra próxima volta ser mais leve." | 150 |
| `im_startup_s8_conversar_st_estudante` | 30 | +0,5 Bia | Bia está nervosa com o palco. Uma caloura perguntou a ela se o total do app mente. "Eu disse: agora não. E é verdade." | 140 |
| `im_startup_s8_observar_bandejao` | 90, −1 | sem pista; +0,5 Bia | Calouros comparam três apps de finanças na fila. Um deles fica com o Trocado porque "a veterana disse que o total não mente". O jogador vê um primeiro uso de verdade, do cadastro ao primeiro gasto. | 280 |
| `im_startup_s8_conversar_st_qualidade` | 30 | +0,5 Lorena | Lorena lê as primeiras avaliações da 1.0: nota 4,6 nas últimas cinquenta. "Cadê a evidência? Tá aqui. E ninguém falou de total errado." | 140 |
| `im_startup_s8_ajudar_st_ceo` | 90, −2 | +1,0 Vinícius; pista `st_p_retencao` (se ainda não tem) | Ensaio geral na aceleradora, com o telão de verdade. O jogador confere os números do slide contra o painel e ensaia as perguntas. A mentora da Maré faz a mesma pergunta de sempre. | 300 |
| `im_startup_s8_conversar_st_ceo` | 30 | +0,5 Vinícius | Vinícius treina a frase de abertura. "Eu quase larguei a faculdade por falta de dinheiro. ... Muito dramático? Não? Fica." | 130 |
| mentoria | 90, −1 | +1,0 Lorena; passo | Encontros 1 a 5. | — |

Pistas: `st_p_retencao`. Registro extra: nenhum.

### 3.9 Dados das intermissões (formato do doc de sistemas, 2.3)

```python
init 3 python:
    ROUTES["startup"]["intermissoes"] = {
        1: {"dia": _("Sexta"), "inicio": (15, 0), "bloco": 120, "mesmo_dia": False,
            "agenda": {"mesa": ["st_mobile", "st_techlead"], "sala_vidro": ["st_mentora"],
                       "cafe": ["st_qualidade"], "terraco": ["st_ceo"]},
            "fechados": {}, "ajudar": {"st_mobile": None}, "observar": {},
            "estudar": "st_extra_kanban"},
        2: {"dia": _("Sexta"), "inicio": (15, 0), "bloco": 180, "mesmo_dia": False,
            "agenda": {"mesa": ["st_techlead", "st_mobile"], "sala_vidro": ["st_ceo"],
                       "cafe": ["st_mentora"], "bandejao": ["st_estudante", "st_qualidade"]},
            "fechados": {}, "ajudar": {"st_techlead": None},
            "observar": {"bandejao": "st_p_cancelar"}, "estudar": "st_extra_episodio"},
        3: {"dia": _("Sexta"), "inicio": (15, 0), "bloco": 180, "mesmo_dia": False,
            "agenda": {"mesa": ["st_mobile", "st_mentora"], "sala_vidro": ["st_techlead"],
                       "cafe": ["st_ceo"], "bandejao": ["st_estudante", "st_qualidade"]},
            "fechados": {}, "ajudar": {}, "observar": {"bandejao": "st_p_tunel"},
            "estudar": "st_extra_invest"},
        4: {"dia": _("Sexta"), "inicio": (15, 0), "bloco": 180, "mesmo_dia": False,
            "agenda": {"mesa": ["st_mobile"], "sala_vidro": ["st_ceo", "st_mentora"],
                       "cafe": ["st_techlead"], "bandejao": ["st_estudante", "st_qualidade"]},
            "fechados": {"terraco": _("Fechado: arrumando a festa")}, "ajudar": {},
            "observar": {"bandejao": "st_p_bolsa"}, "estudar": "st_extra_idempotencia"},
        5: {"dia": _("Segunda"), "inicio": (16, 0), "bloco": 180, "mesmo_dia": True,
            "agenda": {"mesa": ["st_techlead", "st_mobile"], "sala_vidro": ["st_mentora"],
                       "cafe": ["st_ceo"], "bandejao": ["st_estudante", "st_qualidade"]},
            "fechados": {}, "ajudar": {"st_techlead": "st_p_conexoes", "st_mobile": "st_p_logs"},
            "observar": {"bandejao": None}, "estudar": "st_extra_coorte"},
        6: {"dia": _("Terça"), "inicio": (18, 0), "bloco": 150, "mesmo_dia": True,
            "agenda": {"mesa": ["st_mobile", "st_techlead"], "cafe": ["st_estudante"],
                       "terraco": ["st_mentora", "st_qualidade"], "aceleradora": ["st_ceo"]},
            "fechados": {"bandejao": _("Fechado à noite")},
            "ajudar": {"st_mobile": "st_p_loja", "st_techlead": "st_p_conexoes",
                       "st_ceo": "st_p_retencao"},
            "observar": {"cafe": None}, "estudar": "st_extra_carga"},
        7: {"dia": _("Quarta"), "inicio": (12, 0), "bloco": 150, "mesmo_dia": True,
            "agenda": {"mesa": ["st_techlead"], "sala_vidro": ["st_mobile"], "cafe": ["st_mentora"],
                       "bandejao": ["st_estudante", "st_qualidade"], "aceleradora": ["st_ceo"]},
            "fechados": {}, "ajudar": {"st_mobile": "st_p_loja", "st_ceo": "st_p_retencao"},
            "observar": {"bandejao": None}, "estudar": "st_extra_rollout"},
        8: {"dia": _("Quarta"), "inicio": (13, 30), "bloco": 180, "mesmo_dia": True,
            "agenda": {"mesa": ["st_mobile", "st_techlead"], "sala_vidro": ["st_mentora"],
                       "bandejao": ["st_estudante", "st_qualidade"], "aceleradora": ["st_ceo"]},
            "fechados": {}, "ajudar": {"st_ceo": "st_p_retencao"},
            "observar": {"bandejao": None}, "estudar": None},
    }
```

Notas para a E4: (1) `"observar"` da semana diz onde a ação aparece; o café só tem observar na S6; (2) a chave
opcional `"atividade"` dos balões fica fora do bloco para não pesar, com as frases das tabelas acima; (3) a "Bia e duas
testers" da S6 é só a Bia na agenda; as testers são NPCs do conteúdo; (4) `im_validar_dados`: Lorena está em 7 das
semanas 2–8, todos os `inicio + bloco` terminam antes das 21h.

---

## 4. Pistas

### 4.1 Dados

```python
init 3 python:
    ROUTES["startup"]["pistas"] = {
        "st_p_cancelar": {"titulo": _("Desistir no meio"), "ate_semana": 2,
            "texto": _("No bandejão, a Bia começou a lançar um suco de R$ 6, desistiu porque a amiga pagou e tocou em Cancelar. Na mesma hora conferiu a lista e o caderno: \"Depois do almoço duplicado, toda vez que eu desisto eu confiro se nada mudou.\""),
            "uso": _("Semana 3: o caso do cancelamento.")},
        "st_p_tunel": {"titulo": _("Salvar duas vezes no subsolo"), "ate_semana": 3,
            "texto": _("No subsolo do bandejão o 4G cai. A Bia lançou o bandejão de R$ 4,50, a tela travou e ela tocou em Salvar de novo: apareceram dois. Antes, ela tinha lançado de propósito dois sucos de R$ 6, um dela e um da colega. Na lista, as duas duplas pareciam iguais."),
            "uso": _("Semana 4: a causa do gasto duplicado.")},
        "st_p_bolsa": {"titulo": _("Só no dia da bolsa"), "ate_semana": 4,
            "texto": _("Na mesa da Bia, de cinco estudantes, três só abrem o app no dia em que a bolsa cai. Duas instalaram nesta semana e nunca lançaram um gasto. Só a Bia lança todo dia."),
            "uso": _("Semana 5: a métrica do demo day.")},
        "st_p_leitor": {"titulo": _("A lixeira sem nome"), "ate_semana": 5,
            "texto": _("No clube das testers, o leitor de tela da Joana leu a lixeira do protótipo só como \"botão\". Ela não sabia qual gasto ia apagar."),
            "uso": _("Semana 6: a revisão do seu PR.")},
        "st_p_conexoes": {"titulo": _("Conexões no limite"), "ate_semana": 6,
            "texto": _("No painel do banco, com umas duzentas pessoas usando ao mesmo tempo, as conexões abertas chegaram a 80% do limite. Cada função que acorda abre a própria conexão."),
            "uso": _("Semana 7: o teste do pico.")},
        "st_p_logs": {"titulo": _("O e-mail no relatório de falhas"), "ate_semana": 6,
            "texto": _("O relatório de falhas do app manda o e-mail da pessoa junto com cada erro para o serviço de monitoramento. O Davi disse: \"depois eu tiro isso\"."),
            "uso": _("Semana 7: os logs da sincronização.")},
        "st_p_loja": {"titulo": _("Dois dias na fila da loja"), "ate_semana": 7,
            "texto": _("No histórico de envios, a última versão do beta ficou dois dias em revisão no Google. Uma anterior voltou rejeitada por falta do link da política de privacidade."),
            "uso": _("Semana 8: como liberar a 1.0.")},
        "st_p_retencao": {"titulo": _("A única pergunta do ensaio"), "ate_semana": 8,
            "texto": _("No ensaio na Aceleradora Maré, a mentora ouviu o pitch inteiro e fez uma pergunta só: quantos dos que entraram há um mês ainda usam."),
            "uso": _("Semana 8: o demo day.")},
    }
```

Cada texto descreve o que o jogador viu, não a resposta da decisão (revisão pedida no doc de sistemas, risco 3).

### 4.2 Onde cada pista é usada

| Pista | Origem | Arquivo / label | Formato | Ponto exato e texto |
|---|---|---|---|---|
| `st_p_cancelar` | S2 observar bandejão | `st_09_historias.rpy` / `st_09_historias` | 1 | Depois de `st_mentora "Ela achou o caso limite antes da gente. O que a gente responde e escreve no cartão?"` e antes do `menu:` "Bia pergunta: e se eu tocar em Excluir e depois cancelar?": `call pista_lembrar("st_p_cancelar") from _pl_st09_limite` |
| `st_p_tunel` | S3 observar bandejão | `st_13_arquitetura.rpy` / `st_13_arquitetura` | 1 | Depois de `st_techlead "Então, [player_name]. Como você evitaria o gasto duplicado?"` e antes do `menu:` "Como evitar o gasto duplicado?": `call pista_lembrar("st_p_tunel") from _pl_st13_idempotencia` |
| `st_p_bolsa` | S4 observar bandejão | `st_15_gestao.rpy` / `st_15_gestao` | 1 | Depois de `st_ceo "O gráfico de cadastros é lindo, né? ... qual número a gente leva?"` e antes do `menu:` "Que métrica Vinícius deve mostrar no demo day?": `call pista_lembrar("st_p_bolsa") from _pl_st15_metrica` |
| `st_p_leitor` | mentoria 3 | `st_16_codificacao.rpy` / `st_16_codificacao` | 2 | Opção nova no menu "Como você responde ao review do Davi?" (abaixo) e fala alterada da Lorena |
| `st_p_conexoes` | S5 ou S6 ajudar Otávio | `st_17_testes_seguranca.rpy` / `st_17_testes_seguranca` | 1 | Depois de `st_qualidade "Esse último é seu. Quarta que vem o semestre começa e os calouros chegam. Como a gente testa o pico?"` e antes do `menu:` "Como testar o pico do início do semestre?": `call pista_lembrar("st_p_conexoes") from _pl_st17_carga` |
| `st_p_logs` | S5 ajudar Davi | `st_17_testes_seguranca.rpy` | 2 | Opção nova no menu "Como você ataca o bug do modo avião?" (abaixo) |
| `st_p_loja` | S6 ou S7 ajudar Davi | `st_18_lancamento.rpy` / `st_18_lancamento` | 1 | Depois de `st_techlead "E na quinta tem demo day. ... como você soltaria essa versão?"` e antes do `menu:` "Como liberar a 1.0?": `call pista_lembrar("st_p_loja") from _pl_st18_rollout` |
| `st_p_retencao` | S6, S7 ou S8 ajudar Vinícius | `st_18_lancamento.rpy` | 2 | Opção nova no menu "Antes do pitch, quem você ajuda?" e uma fala nova no pitch (abaixo) |

**`st_p_leitor` na `st_16`.** No `menu:` "Como você responde ao review do Davi?", depois das três opções atuais:

```renpy
        "\"Ajustei. E lembrei do clube: no leitor de tela, a lixeira dizia só 'botão'.\"" (tipo="pista") if pista_tem("st_p_leitor"):
            $ pista_usar("st_p_leitor")
            $ add_friendship_point("st_mobile", 1)
            show st_mobile thinking at left_zoom
            st_mobile "Pô, sério? Liguei o leitor de tela aqui... \"botão\". Só isso."
            st_mobile "Põe o nome e o valor no rótulo: \"Excluir Almoço, R$ 20\". Aprovado com louvor."
```

Mais adiante, a fala `st_qualidade "Oxe, passou tudo. E o leitor de tela já fala \"Excluir Almoço, R$ 20\", não só \"botão\"."`
fica dentro de um `if`:

```renpy
    if "st_p_leitor" in pistas_usadas:
        st_qualidade "Oxe, passou tudo. E o leitor de tela fala \"Excluir Almoço, R$ 20\". O Davi disse que a ideia veio do clube. A Joana vai gostar de saber."
        $ add_friendship_point("st_qualidade", 0.5)
    else:
        st_qualidade "Oxe, passou tudo. E o leitor de tela já fala \"Excluir Almoço, R$ 20\", não só \"botão\"."
```

Sem a pista, o rótulo acessível existe do mesmo jeito (veio da definição de pronto da `st_15`): mesmo fim, outra fala.

**`st_p_logs` na `st_17`.** No `menu:` "Como você ataca o bug do modo avião?", opção nova:

```renpy
        "Peço os logs ao Otávio e conferimos também o relatório de falhas que mandava o e-mail" (tipo="pista") if pista_tem("st_p_logs"):
            $ pista_usar("st_p_logs")
            $ add_friendship_point("st_techlead", 1)
            # mesmo diagnóstico e correção da opção "Peço ao Otávio para olhar os logs..."
            st_techlead "E o relatório de falhas... olha aí: o e-mail em cada erro, indo para o monitoramento. O log o Davi limpou; esse aqui ficou."
            st_techlead "Corrijo agora, antes da 1.0. Dado que você não manda não vaza."
            $ set_time(18, 30)
```

Risco evitado: o e-mail dos calouros não vai para o monitoramento. A amizade é a mesma da opção do Otávio.

**`st_p_retencao` na `st_18`.** No `menu:` "Antes do pitch, quem você ajuda?", opção nova:

```renpy
        "Ensaio com o Vinícius e a Tainá a resposta sobre retenção, a única pergunta do ensaio na Maré" (tipo="pista") if pista_tem("st_p_retencao"):
            $ pista_usar("st_p_retencao")
            $ add_friendship_point("st_mentora", 1)
            $ add_friendship_point("st_ceo", 0.5)
            show st_mentora neutral at left_zoom
            show st_ceo thinking at right_zoom
            with dissolve
            st_mentora "Se a pergunta é sempre essa, a resposta tem que caber numa frase."
            st_ceo "Quantos voltam: 57%% na semana. E os calouros de ontem a gente mostra em trinta dias, por coorte. Uma frase. Consigo!"
```

No pitch, depois de `"{i}É a métrica que vocês combinaram na semana 5, no aquário. Na plateia, alguém anota.{/i}"`:

```renpy
    if "st_p_retencao" in pistas_usadas:
        "{i}Na primeira fila, uma investidora levanta a mão: \"E os calouros que entraram ontem?\"{/i}"
        st_ceo "A coorte do semestre a gente mostra em trinta dias. Hoje, a do beta: 57%% voltam toda semana."
        "{i}A investidora fecha o caderno e sorri. Vinícius nem olha para o slide.{/i}"
```

---

## 5. Registros extras (estudar)

```python
init 3 python:
    ROUTES["startup"]["extras"] = [
        {"id": "st_extra_kanban", "title": _("Kanban e limite de trabalho em andamento"),
         "text": _("O quadro mostra o fluxo do trabalho: descoberta, pronto para desenvolver, fazendo, revisão, pronto. O limite de trabalho em andamento diz quantos cartões cabem em \"Fazendo\" ao mesmo tempo. Bateu o limite? Ninguém puxa cartão novo: termina um ou ajuda a destravar outro. Menos coisa aberta quer dizer menos espera e problemas aparecendo cedo.")},
        {"id": "st_extra_episodio", "title": _("Perguntas abertas e episódio"),
         "text": _("Pergunta aberta começa com \"como\", \"o que\" ou \"me conta\". Pergunta de sim ou não serve para confirmar, não para descobrir. Peça o episódio mais recente: quando foi, onde a pessoa estava, o que tentou fazer, o que aconteceu e o que fez depois. Anote as palavras dela, sem traduzir.")},
        {"id": "st_extra_invest", "title": _("INVEST para histórias"),
         "text": _("Uma boa história é Independente (dá para entregar sozinha), Negociável (é conversa, não contrato), Valiosa (alguém ganha com ela), Estimável (a equipe sabe o tamanho), Pequena (cabe num ciclo) e Testável (tem critério). \"Quero um app fácil\" falha em quase todas. \"Excluir um gasto com confirmação para o total voltar a ser confiável\" passa.")},
        {"id": "st_extra_idempotencia", "title": _("Idempotência numa página"),
         "text": _("Uma operação é idempotente quando repetir dá o mesmo resultado de fazer uma vez. Em rede instável, o app reenvia quando não sabe se deu certo. Receita: o app gera uma chave única por operação (o id do gasto); o servidor guarda as chaves que já recebeu e, se a mesma chegar de novo, devolve a resposta anterior sem gravar outra vez. \"Excluir o gasto X\" é idempotente; \"somar R$ 20 ao total\" não é.")},
        {"id": "st_extra_coorte", "title": _("Retenção por coorte"),
         "text": _("Coorte é o grupo que começou no mesmo período, como quem se cadastrou na semana da festa dos mil. Retenção da coorte é quantas dessas pessoas ainda fazem a ação que importa (lançar um gasto) depois de 1, 4 e 8 semanas. Olhar por coorte impede que um pico de cadastros esconda quem foi embora. Defina a ação e a janela antes de medir.")},
        {"id": "st_extra_carga", "title": _("O que medir num teste de carga"),
         "text": _("Defina o cenário (quantas pessoas, fazendo o quê, em que horário) e a meta (por exemplo, lista em até 2 s em 95% das vezes). Além do tempo, observe erros, conexões abertas no banco, filas e custo. Suba a carga aos poucos até ver onde quebra. Use dados fictícios, nunca dados reais de pessoas. Teste sem meta vira opinião.")},
        {"id": "st_extra_rollout", "title": _("Lançamento gradual nas lojas"),
         "text": _("Nas lojas, cada versão passa por revisão (horas ou dias) e uma instalação não se desfaz. Por isso: envie com folga, libere em etapas (no Google você escolhe a porcentagem; na Apple a liberação em fases leva sete dias), deixe o que é novo atrás de uma feature flag que desliga sem versão nova e acompanhe falhas e tempos no painel.")},
    ]
```

O notebook mostra "Extras (opcionais): n de 7". Nenhum extra é pré-requisito: os temas também aparecem nas cenas
(Kanban na `st_02`, episódio na `st_05`, idempotência na `st_13`, carga na `st_17`, rollout na `st_18`).

---

## 6. Arco de mentoria: Clube das Testers

Quem orienta: Lorena (`st_qualidade`), com a Bia e duas colegas de república dela. A mentoria acontece onde a Lorena
estiver (bandejão nas S2–S5, S7, S8; terraço na S6). Cada encontro: 90 min, −1 energia, +1,0 de amizade com a Lorena,
20 a 30 falas (350 a 450 palavras), arquivo `game/story/intermissoes/startup/mentoria.rpy`.

**NPCs do arco** (sem sprite, sem contato, sem `image=`; um `define` com `Character` no próprio `mentoria.rpy`):
- **Joana** (`st_npc_joana`, cor `#C9A0FF`): estudante de Letras, tem baixa visão e usa leitor de tela e fonte
  grande. Fala rápido e com ironia ("O leitor de tela não tem paciência. Nem eu."). É especialista no próprio uso,
  nunca objeto de pena.
- **Rayane** (`st_npc_rayane`, cor `#FFB870`): Educação Física, faz entrega de bicicleta aos sábados, celular de 2018
  com a tela trincada e plano pré-pago que acaba todo dia 20.
- **Ítalo** (`st_npc_italo`, cor `#9FD3C7`, só no encontro 4): primo da Rayane, calouro de Engenharia, veio do
  interior para a matrícula.

(Nomes conferidos por grep: não existem em nenhuma rota.)

| k | Semana mín. | Resumo (`resumo`) | O que acontece | O que se aprende | Pista |
|---|---|---|---|---|---|
| 1 | 2 | Apresentar o beta ao clube | Bia traz Joana e Rayane. Lorena explica o combinado: um teste curto toda sexta, com termo de consentimento simples (o que se observa, que só a tela é gravada, com dados fictícios, nunca o rosto, e que dá para parar quando quiser). Cada uma conta como usa o celular. Rayane: "Tem camisa?" Bia batiza o grupo de Clube das Testers. | Recrutar gente diferente (aparelho, internet, acessibilidade) acha problemas diferentes; consentimento antes de observar; a regra de ouro: não ajudar durante o teste. | — |
| 2 | 3 | Cinco tarefas cronometradas | O jogador cronometra cinco tarefas no beta das lojas: lançar o bandejão de R$ 4,50; dizer o total do mês; achar o gasto de ontem; apagar um gasto lançado errado; lançar em modo avião e dizer se salvou. As três primeiras passam. Na quarta, ninguém consegue (não existe ainda) e as três tentam arrastar o item para o lado. Na quinta, ninguém sabe dizer se salvou. Quando Rayane pergunta "é aqui?", o jogador devolve "o que você acha?". | Teste de usabilidade com tarefas: sucesso, tempo e erros; pensar em voz alta; relatar com número ("0 de 3 conseguiram apagar; 3 de 3 tentaram arrastar"). Lorena: "Cadê a evidência? Tá aqui: três de três." | — |
| 3 | 4 | O leitor de tela da Joana | Joana mostra como usa o leitor de tela no beta e no protótipo da confirmação do Davi (instalado como versão de teste). O total é lido certo; o ícone de categoria vira "imagem"; a lixeira vira só "botão". "Eu não preciso de app especial. Preciso que o botão diga o nome." Lorena anota para a definição de pronto (que ela leva à `st_15`). | Rótulo acessível diz ação e objeto; não depender só de ícone ou cor; área de toque grande; ordem de leitura; testar com quem usa de verdade. | `st_p_leitor` |
| 4 | 5 | Calouros e o pico | Ítalo faz as cinco tarefas pela primeira vez na vida no app. Ele não sabe o que é "total do mês" e procura "saldo"; o clube reescreve a tarefa com as palavras dele. Depois, Bia e Rayane descrevem o primeiro dia de aula: o bandejão abre às 11h30, a fila vai até a escada e todo mundo lança o almoço no mesmo minuto. Lorena: "Anota: comportamento coletivo. Mil pessoas fazendo a mesma coisa ao mesmo tempo." | Primeiro uso é outro teste (quem chega não conhece nossas palavras); poucos participantes já mostram a maioria dos problemas; o uso real se concentra em horários. | — |
| 5 | 6 | O primeiro relato de bug do clube | Rayane manda no grupo do clube: "o app bugou". Lorena e o jogador mostram a estrutura: o que fez, o que aconteceu, o que esperava, passos, aparelho, versão, frequência, print sem dado real. Rayane reescreve: "Celular de 2018, teclado sem vírgula. Digitei 4.50 no bandejão. Salvou R$ 450,00. Esperava R$ 4,50. Acontece sempre que uso ponto." Davi reproduz em cinco minutos por mensagem e põe o conserto na fila com prioridade (é a origem provável do "R$ 45" da Bia na `st_11`). Lorena passa a coordenação do clube para a Bia. | Relato de bug reproduzível; o clube continua sem a Lorena. Lorena: "Bug com passo a passo é bug pela metade." | — |

**Variação por local:** com `im_semana_atual == 6`, o encontro abre no terraço ("As três subiram do café com o
notebook da Bia debaixo do braço."). Nas demais semanas, no bandejão.

**Conclusão (fim do encontro 5):** Lorena entrega à Bia o caderninho de frases de avaliação. "Primeiro: vocês acham o
que eu não acho. Segundo: vocês sabem relatar. Terceiro: eu vou continuar aparecendo, que eu gosto do suco."
`mentoria_avancar()` concede a conquista.

**Ecos opcionais nas cenas** (só falas; não mexem em decisões, registros, conquistas pedagógicas nem final):
- `st_15`, depois de `st_qualidade "Segundo: o botão Excluir precisa ter um nome que o leitor de tela fale. Hoje ele é só um ícone de lixeira."`:
  `if mentoria_passos.get("startup", 0) >= 3:` → `st_qualidade "Quem me mostrou isso foi a Joana, no clube."`
- `st_18`, depois de `st_estudante "Tipo assim: eu só quero saber quanto sobra até a bolsa cair. Agora eu sei."`:
  `if mentoria_conq_startup:` → `st_estudante "E agora eu, a Joana e a Rayane testamos cada versão antes de chegar em vocês. A gente até tem nome: Clube das Testers."`

**Dados:**

```python
init 3 python:
    ROUTES["startup"]["mentoria"] = {
        "id": "st_mentoria_testers",
        "titulo": _("Clube das Testers"),
        "mentor": "st_qualidade",
        "passos": [
            {"n": 1, "semana_min": 2, "pista": None,          "resumo": _("Apresentar o beta ao clube")},
            {"n": 2, "semana_min": 3, "pista": None,          "resumo": _("Cinco tarefas cronometradas")},
            {"n": 3, "semana_min": 4, "pista": "st_p_leitor", "resumo": _("O leitor de tela da Joana")},
            {"n": 4, "semana_min": 5, "pista": None,          "resumo": _("Calouros e o pico")},
            {"n": 5, "semana_min": 6, "pista": None,          "resumo": _("O primeiro relato de bug do clube")},
        ],
    }
    ROUTES["startup"]["conquistas_extra"] = [
        {"id": "mentoria_conq_startup", "var": "mentoria_conq_startup",
         "title": _("Clube das Testers"),
         "desc": _("Concluiu os cinco encontros do clube de testers com a Lorena e a Bia.")},
    ]
```

Condição da conquista: `mentoria_passos["startup"] == 5` (marcada por `mentoria_avancar()` no 5º encontro). Fica fora de
`route_achievements()`, então `st_conquistas()` e `st_final_grade()` não mudam. A pista do encontro 3 só é dada se ele
acontecer até a semana 5 (`ate_semana`).

---

## 7. Caça à ambiguidade (semana 3, `st_09_historias`)

**Momento:** depois da explicação de história e critério, antes da escolha da história. Na `st_09`, logo após a linha
`$ advance_minutes(20)` que segue `st_mentora "Caso de uso completo, com fluxo principal e todos os desvios, ..."` e antes
de `show st_mentora thinking at left_zoom` / `st_mentora "Rabisquei três versões do cartão no fim de semana. ..."`:

```renpy
    show st_mentora thinking at left_zoom
    st_mentora "Antes do cartão, um aquecimento. Na sexta, o Vinícius colou isso no quadro de ideias."
    "\"O app deve mostrar o total do mês atualizado rapidamente e deixar a pessoa excluir gastos facilmente, sem perder dados.\""
    st_mobile "Pô, parece ótimo."
    st_mentora "Parece. Agora tenta escrever o teste. Marca as palavras que cada um aqui leria de um jeito."
    call amb_atividade("st_amb_total") from _amb_st09
    show st_mentora neutral at left_zoom
    st_mentora "Agora o Vinícius lê e reconhece o pedido dele. E a Lorena consegue testar cada pedaço."
    st_mobile "\"Rapidamente\" era minha palavra favorita. Era."
    $ advance_minutes(15)
```

A `st_09` termina com `set_time(12, 0)`, então o relógio não precisa de outro ajuste. A história D2 ("Como usuário,
quero um app fácil de usar") ganha eco natural: a Tainá já pergunta "Lembra o que a Bia ensinou sobre 'fácil'?".

**Dados (completam o exemplo do doc de sistemas, 5.1):**

```python
init 3 python:
    ROUTES["startup"]["ambiguidades"] = {
        "st_amb_total": {
            "contexto": _("Pedido do Vinícius, copiado do quadro de ideias."),
            "falante": "st_mentora",
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
            "resultado": _("O app deve mostrar o total do mês atualizado {b}[em até 2 segundos depois de salvar, em 95% das vezes, num celular de entrada com 4G]{/b} e deixar a pessoa excluir gastos {b}[a partir do próprio gasto na lista, com uma confirmação que mostra o nome e o valor antes de apagar]{/b}; {b}[um gasto salvo sem internet fica guardado no celular, é enviado quando o sinal volta e aparece uma única vez na lista e no total]{/b}."),
        },
    }
```

Notas: (1) `falante` e `resultado` são opcionais (a E6 pode montar o resultado sozinha a partir das trocas); se não
usar, a fala da Tainá depois do `call` fecha a atividade. Os colchetes no texto do `resultado` precisam ir como `[[`
se ele passar por interpolação. (2) Decisões gravadas: `st_amb_total_marcar`, `st_amb_total_rapido`,
`st_amb_total_facil`, `st_amb_total_sem_perder`, todas por `decisao()`. Não usam `st_decidir`, então `st_acertos` e
`ST_ACERTOS_MAX = 24` não mudam. (3) A reescrita de "rapidamente" repete a medida da `st_06` (2 s, 95%, celular de
entrada, 4G); a de "sem perder dados" fala do que o app deve garantir, não de como (o id único continua sendo a
decisão da `st_13`). (4) Tempo: 6–8 min.

---

## 8. Rastreabilidade (semana 6, `st_16_codificacao`; bug na semana 7, `st_17`)

**Momento (ajuste registrado):** o doc de sistemas diz "antes do PR". Na cena, o teste T3 (mesmo id enviado duas
vezes) só passa a existir depois do review do PR do Davi, porque é justamente o teste que falta no diff. Por isso o
quadro entra depois do menu "Como você responde ao review do Davi?" e antes de os PRs irem para a Lorena: depois de
`hide st_mobile` / `hide st_techlead` / `with dissolve` e antes de `$ set_time(17, 10)`.

```renpy
    $ advance_minutes(20)
    show st_techlead thinking at center_zoom
    with dissolve
    st_techlead "Antes de os dois PRs irem para a Lorena, um hábito da casa: o quadro."
    st_techlead "Cada critério, de qual requisito veio e qual teste cobre. Se um elo falta, é por ali que o bug entra."
    hide st_techlead
    call rast_atividade("st_rast_exclusao") from _rast_st16
    show st_techlead neutral at center_zoom
    if rast_lacuna_achada("st_rast_exclusao"):
        st_techlead "Bem visto. Critério sem teste é porta destrancada. Vira cartão: a Lorena escreve esse teste semana que vem, com o plano."
    else:
        st_techlead "Quadro conferido. Agora os PRs vão para a Lorena."
    hide st_techlead
```

A fala do "else" não aponta a lacuna (o quadro nunca a revela).

**Dados:**

```python
init 3 python:
    ROUTES["startup"]["rastreabilidade"] = {
        "st_rast_exclusao": {
            "requisitos": [
                {"id": "R1", "texto": _("A pessoa exclui um gasto lançado por engano, com confirmação.")},
                {"id": "R2", "texto": _("O total do mês reflete todos os gastos sincronizados.")},
                {"id": "R3", "texto": _("Um gasto reenviado não é gravado duas vezes.")},
            ],
            "criterios": [
                {"id": "C1", "de": "R1", "teste": "T1",
                 "texto": _("Dado um total de R$ 100 com um almoço de R$ 20, quando a pessoa confirma a exclusão, então o almoço sai da lista e o total passa a R$ 80."),
                 "dica": _("Confirmar a exclusão: veio do pedido de excluir com confirmação, e um teste confere a exclusão confirmada.")},
                {"id": "C2", "de": "R1", "teste": "T2",
                 "texto": _("Dado o mesmo total, quando a pessoa toca em Excluir e depois em Cancelar, então o almoço continua na lista e o total continua R$ 100."),
                 "dica": _("Cancelar também é parte da exclusão com confirmação. Procure o teste do caminho de cancelar.")},
                {"id": "C3", "de": "R3", "teste": "T3",
                 "texto": _("Dado um café de R$ 5 com o id A1, quando o mesmo pedido chega duas vezes ao servidor, então só um café é gravado."),
                 "dica": _("É o caso do túnel: reenvio. O teste é o que o Davi acrescentou depois do review.")},
                {"id": "C4", "de": "R2", "teste": None,
                 "texto": _("Dado um bandejão de R$ 4,50 lançado sem internet, quando a sincronização termina, então o total mostra o novo valor sem reabrir a tela.")},
                {"id": "C5", "de": "R2", "teste": "T4",
                 "texto": _("Dado R$ 100 no mês, quando a pessoa lança R$ 5 com internet, então o total vai para R$ 105."),
                 "dica": _("Fala do total, com internet. Qual teste confere o total online?")},
            ],
            "testes": [
                {"id": "T1", "texto": _("teste_excluir_confirmado")},
                {"id": "T2", "texto": _("teste_excluir_cancelado")},
                {"id": "T3", "texto": _("teste_sync_idempotente")},
                {"id": "T4", "texto": _("teste_total_online")},
            ],
            "lacuna": "C4",
            "explica_lacuna": _("Nenhum teste cobre o total depois da sincronização offline."),
        },
    }
```

`dica` é opcional (texto da explicação quando a ligação está errada; sem ela, a E6 usa um texto genérico). A armadilha
esperada é ligar C4 a T4 ("total" nos dois): pela regra do doc de sistemas, C4 não recebe "(confira)"; só a pergunta
"Todo critério tem teste?" na primeira conferência. Decisões: `st_rast_exclusao_ligacoes` e
`st_rast_exclusao_lacuna`. Tempo: 8–10 min.

**O elo que falta vira o bug da semana 7 (`st_17`).** O bug já existe na cena: às 15h20 a Lorena acha o total que não
atualiza ao sair do modo avião (é o C4). Mudanças:

1. Plano de testes da manhã, depois de `st_qualidade "Fora do triângulo, mas na lista: teste exploratório em modo avião, leitor de tela no botão Excluir e um teste de carga."`:
   ```renpy
       if rast_lacuna_achada("st_rast_exclusao"):
           st_qualidade "E o teste do C4, o total depois da sincronização, que você achou sem teste no quadro. Escrevo à tarde, depois do exploratório."
   ```
2. Depois de `st_qualidade "Só atualiza se eu fechar e abrir o app. Para a Bia, é o \"meu total está errado\" de novo."`:
   ```renpy
       if not rast_lacuna_achada("st_rast_exclusao"):
           st_qualidade "Oxe, espera. Lembra do quadro da semana passada? O C4: total depois da sincronização offline. Nenhum teste cobria. O bug morava nesse elo."
   ```
3. Opção nova no `menu:` "Como você ataca o bug do modo avião?" (texto do doc de sistemas):
   ```renpy
           "Rodar o teste que você pediu na semana passada" (tipo="pista") if rast_lacuna_achada("st_rast_exclusao"):
               $ add_friendship_point("st_qualidade", 0.5)
               "{i}A Lorena tinha acabado de escrever o teste do C4. Ele falha em três segundos, sempre no mesmo passo: a sincronização termina e a tela do total não fica sabendo.{/i}"
               "{i}Às 16h, o total sobe na hora e o teste fica verde. Ele fica no conjunto de testes de vez.{/i}"
               st_qualidade "Critério com teste é bug com endereço. Sobrou a tarde pro leitor de tela."
               $ set_time(18, 30)
   ```
   As três opções atuais continuam e chegam ao mesmo fim.

---

## 9. Energia nesta rota

### 9.1 Eventos nas cenas (tabela 4.2 do doc de sistemas)

| Cena | Ponto exato | Linha nova | Efeito |
|---|---|---|---|
| `st_11` | depois de `$ set_time(19, 30)` e antes de `hide st_qualidade` | `$ energia_gastar(1, _("inspeção até 19h30"))` | −1 |
| `st_17` | no ramo "Tento resolver por conta própria até tarde.", depois de `$ set_time(20, 0)` | `$ energia_gastar(2, _("ficou até tarde sozinho"))` e `$ im_hora_extra_somar(60)` | −2 e 60 min a menos na S8 |
| `st_18` | no `else` do pico (sem `st_d17_carga`), depois de `st_techlead "Anota para a retrospectiva: ..."` | `$ energia_gastar(1, _("pico do semestre sem o ajuste"))` | −1, logo antes da S8 |

Ordem que importa: a S7 acontece antes do bug da tarde; o −2 do "até tarde" cai depois do +3 de fim de semana da S7,
então pesa na segunda da `st_18` e encurta a S8 (hora extra). É a lição do doc de sistemas: virar a noite rende hoje e
encolhe a semana seguinte.

### 9.2 Falas com energia baixa (`energia_cansaco()`)

| Cena | Ponto | Fala |
|---|---|---|
| `st_14` | depois de `st_techlead "Vai pra casa cedo hoje. Segunda a gente precisa da sua cabeça descansada, não de heroísmo."` | `st_techlead "E pelo seu jeito, você sabe do que eu tô falando. Pega um pedaço de pizza pra viagem e vai."` |
| `st_16` | depois de `st_mobile "Bom dia! Pô, chegou o dia. Primeiro cartão seu indo para o código."` | `st_mobile "Pera. Tá com olheira de sprint, hein? Toma, café forte da copa. Hoje é PR pequeno, não maratona."` |
| `st_17` | depois de `st_qualidade "Bom dia, [player_name]! Senta aqui. Hoje é dia de plano de testes, e eu trouxe desenho."` | `st_qualidade "Oxe, cansaço dá pra ver de longe. Primeiro: água. Segundo: começamos pelo que é rápido. Terceiro: ninguém fica depois das seis."` |
| `st_18` | depois de `st_mentora "Bom dia, gente! Bora, que hoje a 1.0 sai de casa."` | `st_mentora "E você, [player_name], dormiu? Semana de lançamento não é semana de heroísmo. Hoje ninguém fica depois das sete."` |

Dentro do tempo livre: a abertura de cada semana tem a variante de cansaço (seção 3, S2); os três `descansar` têm fala
própria; o Otávio da S6 ("não fico depois das nove") e a Tainá da S5 ("cansaço não é prova de dedicação") reforçam o
tema em qualquer energia. Nada disso muda decisões, registros, conquistas ou o final.

### 9.3 Conta de referência

Jogando "no máximo" (duas ajudas por semana): −4 por intermissão, +3 no fim, −1 na `st_11`, −2/−1 na semana 7–8.
Começando em 8, o cansaço (3 ou menos) aparece por volta das semanas 6–7. Quem alterna com conversar e descansar fica
entre 6 e 9 a rota toda.

---

## 10. Estimativa de palavras e minutos

**Escritas (conteúdo novo da rota):**

| Item | Quantidade | Palavras |
|---|---|---|
| Conversar | 47 labels × ~145 | 6.800 |
| Ajudar | 10 × ~300 | 3.000 |
| Observar | 7 × ~290 | 2.000 |
| Estudar (falas) | 7 × ~135 | 950 |
| Descansar | 3 labels, com variantes | 450 |
| Mentoria | 5 × ~400 | 2.000 |
| Aberturas (tutorial + 7 semanas + variantes) | — | 700 |
| Dados: pistas, extras, resumos, ambiguidade, rastreabilidade | — | 2.100 |
| Mudanças nas cenas: ambiguidade, quadro, pistas, energia, ecos da mentoria | — | 1.200 |
| **Total escrito** | 79 labels de conteúdo | **≈ 19.200** |

**Lidas numa partida:** cerca de 23 ações de tempo livre (2 na S1, 3 nas demais) ≈ 5.000 palavras, mais ≈ 1.500 das
cenas (ambiguidade, quadro, 3 a 6 pistas, energia) e aberturas/resumos ≈ 500. Total ≈ 7.000 palavras.

**Minutos adicionados por partida:**

| Item | Minutos |
|---|---|
| 8 intermissões (mapa + leitura) | ≈ 42 |
| Caça à ambiguidade | ≈ 7 |
| Rastreabilidade | ≈ 9 |
| Pistas lembradas nas cenas e falas de energia | ≈ 2 |
| Pontos de parada | ≈ 2 |
| **Total** | **≈ +62** (rota de ~80 para ~140–145 min) |
| Com "Tempo livre: pular" | ≈ +18 (ambiguidade, quadro, paradas) |

Para aula: duas semanas de jogo por aula de 50 min dá ~35 min de jogo; as paradas caem depois das semanas 2, 4 e 6.

---

## 11. Mudanças nos `.rpy` desta rota (para E5/E6)

| Arquivo | Mudança |
|---|---|
| `rota_startup.rpy` | 4 ganchos A e 7 pontos de parada (seção 2) |
| `st_09_historias.rpy` | ambiguidade (seção 7); `pista_lembrar("st_p_cancelar")` (4.2) |
| `st_11_inspecao.rpy` | energia −1 (9.1) |
| `st_13_arquitetura.rpy` | `pista_lembrar("st_p_tunel")` |
| `st_14_comemoracao.rpy` | fala de cansaço do Otávio |
| `st_15_gestao.rpy` | gancho B S5; `pista_lembrar("st_p_bolsa")`; eco da mentoria 3 |
| `st_16_codificacao.rpy` | gancho B S6; `set_time(19, 0)` → `set_time(21, 0)`; quadro (seção 8); opção e fala de `st_p_leitor`; fala de cansaço do Davi |
| `st_17_testes_seguranca.rpy` | gancho B S7; `pista_lembrar("st_p_conexoes")`; opções `st_p_logs` e "Rodar o teste..."; duas falas do C4; energia −2 e hora extra; fala de cansaço da Lorena |
| `st_18_lancamento.rpy` | gancho B S8; `pista_lembrar("st_p_loja")`; opção e fala de `st_p_retencao`; energia −1; fala de cansaço da Tainá; eco da conquista da mentoria |
| novos | `game/data/intermissoes/startup.rpy` (seções 1.3, 3.9, 4.1, 5, 6, 7, 8); `game/story/intermissoes/startup/s1.rpy`…`s8.rpy`, `mentoria.rpy` |

Todos os `call` novos levam `from`. Os menus novos usam `tipo` (`trabalho` nos pedagógicos já existentes quando a E5
marcar, `pista` nas opções novas). Nenhuma variável ou label existente muda de nome. Regras dos finais intactas.

## 12. Pontos para revisão

1. O doc de sistemas põe o quadro "antes do PR"; aqui ele vem depois do review, para o T3 existir (seção 8).
2. `st_p_logs` foi descrita como relatório de falhas, e não como o log revisado na `st_16`: assim ela não entrega a
   resposta do `st_d16_review` e ainda tem uso próprio na `st_17` (risco evitado).
3. `st_p_cancelar` mostra a Bia cancelando um lançamento, não uma exclusão: o beta das lojas ainda não exclui gasto
   (`st_01`: "Hoje, se você lança errado, não tem como apagar").
4. Os extras de carga e rollout preparam diretamente as decisões das semanas 7 e 8. É estudo opcional (o doc de
   sistemas pede que o extra prepare a semana seguinte), mas o revisor pode preferir textos mais gerais.
5. NPCs da mentoria (Joana, Rayane, Ítalo) precisam de `define` sem sprite; se a E3 quiser retrato, fica para depois.
