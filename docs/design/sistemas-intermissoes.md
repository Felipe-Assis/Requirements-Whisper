# Design de sistemas: intermissões, mapa, tempo, energia e novas mecânicas

Data: 2026-11-02. Branch `evolucao`. Etapa E1 (sistemas) do plano `docs/plans/2026-11-02-evolucao.md`.
Escopo do usuário: jogo educacional que serve para aula (objetivos claros, sessões que podem ser retomadas) e para
jogar sozinho por diversão, completo do início ao fim. Estilo de arte: personagens C, fundos C. Live2D fica fora.

Este documento é a referência para quem implementa (E4, E6, E7) e para quem escreve o conteúdo de cada rota (E5).
Ele não altera nenhum `.rpy`. Os números aqui são o ponto de partida; ajuste só com motivo registrado.

---

## 0. Regras gerais

### 0.1 Princípios
1. **Nada obrigatório para aprender fica só no tempo livre.** Os 8 registros do notebook, as decisões pedagógicas
   (`decisao`, `st_decidir`, `co_acerto`/`co_erro`), a escrita livre, o planejamento, a caça à ambiguidade e a
   rastreabilidade ficam nas cenas. Uma intermissão nunca chama `registrar()`, `decisao()`, `exercicio_escrita`,
   `atividade_planejamento`, `amb_atividade` ou `rast_atividade`.
2. **Cada ação volta para a história**: amizade, uma pista que muda uma cena, um registro extra, energia ou um passo
   de mentoria. Nada de ponto solto.
3. **Sem punição.** Energia baixa, pista perdida ou mentoria incompleta nunca alteram nota de decisão, registros,
   conquistas pedagógicas nem a regra do final.
4. **Regras de finais intactas.** `final_saude`, `st_final_grade`, `co_final_grade` e a conta da `scene_21` não mudam.
   Conquistas novas ficam numa lista separada (`ROUTES[rota]["conquistas_extra"]`).
5. **Nada existente é renomeado.** Toda variável nova tem um único `default`. Calls novos na cadeia levam `from`.

### 0.2 Prefixos novos (conferidos por grep; nenhum existe hoje)

| Prefixo | Uso |
|---|---|
| `im_` | intermissão, mapa, ações, agenda (labels, telas, funções e estado) |
| `pista_` / `pistas` | pistas (funções `pista_*`, estado `pistas`, `pistas_usadas`) |
| `mentoria_` | arcos de mentoria |
| `energia_` | energia semanal (`energia_semana` etc.; `energia_diaria` continua existindo e não é lida) |
| `amb_` | caça à ambiguidade |
| `rast_` | quadro de rastreabilidade |
| `fala_` | destaque de quem fala |
| `vida_`, `cam_` | respiração/balanço dos sprites e câmera |
| `menu_tipo` | rótulo de tipo de menu |

Ids de conteúdo (strings) seguem o prefixo da rota: `saude_`, `st_`, `co_` (ex.: `st_p_tunel`, `co_extra_rfc`).

### 0.3 Arquivos novos

| Arquivo | Conteúdo | Quem escreve |
|---|---|---|
| `game/logic/intermissao.rpy` | defaults e funções de intermissão, ações, pistas, mentoria | E4 |
| `game/logic/energia.rpy` | defaults e funções de energia | E4 |
| `game/scripts/mechanics/intermissao_fluxo.rpy` | labels `im_intermissao`, `im_executar`, `im_ponto_parada`, `pista_lembrar` | E4 |
| `game/scripts/mechanics/mapa_screen.rpy` | telas `im_mapa`, `im_resumo`, `im_parada`, `energia_hud` | E4 |
| `game/scripts/mechanics/ambiguidade.rpy` | label `amb_atividade`, tela `amb_marcar` | E6 |
| `game/scripts/mechanics/rastreabilidade.rpy` | labels `rast_atividade` e `rast_lembrar`, tela `rast_quadro` | E6 |
| `game/logic/fala_destaque.rpy` | destaque de quem fala (wrapper de `config.show`) | E4 |
| `game/ui/styles/vida_transforms.rpy` | `vida_respira`, `cam_*`, `bg_cobrir` | E7 |
| `game/data/intermissoes/saude.rpy`, `startup.rpy`, `corporativo.rpy` | dados de mapa, agenda, pistas, extras, mentoria, ambiguidade e rastreabilidade da rota (`init 3 python`) | E5 (um por rota) |
| `game/story/intermissoes/<rota>/s1.rpy` … `s8.rpy` e `mentoria.rpy` | labels de conteúdo das ações | E5 (um escritor por rota) |
| `game/tests/intermissoes.rpy` | testes no motor | E4/E8 |

Arquivos existentes que mudam (sem renomear nada): `script.rpy`, `story/rota_*/rota_*.rpy` (calls novos),
algumas cenas (ganchos de semana, pistas, energia, mecânicas), `data/characters.rpy` (`image=`), `gui.rpy`
(alinhamento do nome), `screens.rpy` (tela `choice`, preferências), `data/backgrounds.rpy` (fundos),
`notebook_screen.rpy` (extras e pistas), `scene_epilogo_conquistas_final.rpy` (linhas do resumo),
`tests/autopiloto.rpy`.

Os dados por rota rodam em `init 3 python` porque `ROUTES` nasce em `init 1` e Startup/Corporativo registram os
seus dados em `init 2`.

---

## 1. Intermissões

### 1.1 Onde cada intermissão entra

Uma intermissão por semana, 8 por rota. Dois tipos de gancho:

- **A (cadeia):** `call im_intermissao(N) from _im_<rota>_sN` entre duas cenas em `script.rpy` ou
  `rota_<rota>.rpy`. Preferido: não mexe na cena.
- **B (na cena):** a mesma linha dentro da cena, no ponto indicado. Usado quando a semana tem uma cena só (o cartão
  "Fim da Semana N" fica dentro dela). Âncora pelo texto, porque o número da linha muda.

Campos: `inicio` (hora), `bloco` (minutos), `mesmo_dia` (a cena anterior aconteceu no mesmo dia; ver 1.3).

**Saúde** (22 cenas; semanas pelos cartões "Fim da Semana N")

| Sem. | Cenas da semana | Gancho | Ponto | Dia e horário | Bloco | mesmo_dia | Ajuste necessário |
|---|---|---|---|---|---|---|---|
| 1 | 3, 4 | A | antes de `scene_4_retorno_casa` | sexta 16h–18h | 120 (tutorial) | não | `scene_4`: `advance_minutes(150)` vira `advance_minutes(50)` (o "resto do expediente" agora é a intermissão) |
| 2 | 5, 6, 7, 8, 9 | A | antes de `scene_9_retorno_casa_sem2` | sexta 16h–19h | 180 | sim | — |
| 3 | 10, 11, 12, 13 | A | antes de `scene_13_retorno_casa_sem3` | sexta 15h–18h | 180 | não | — |
| 4 | 14, 15 | A | antes de `scene_15_aniversario_surpresa` | sexta 12h–15h (almoço estendido; a festa começa às 15h) | 180 | não | `scene_15`: a fala "Já no dia seguinte..." vira "Depois do almoço..." |
| 5 | 16, 17 | B | `scene_17`, logo depois de "Você salva suas anotações, fecha o notebook..." e antes de `$ set_available('all')` | 16h–19h | 180 | sim | — |
| 6 | 18 (e 18_2) | B | `scene_18`, antes do comentário `# Decisão: se não finalizou no escritório` (vale para todos os caminhos) | 16h30–19h30 | 180 | sim | — (a cena marca 19h40 depois) |
| 7 | 19 | B | `scene_19`, antes de `# Fechamento: Reflexão e estatísticas` | 15h30–18h30 | 180 | sim | — |
| 8 | 20, 21 | B | `scene_21`, antes de `scene bg transito_tarde` ("Após o almoço...") | 9h30–12h30 | 180 | sim | — |

**Startup** (18 cenas)

| Sem. | Cenas | Gancho | Ponto | Dia e horário | Bloco | mesmo_dia | Ajuste |
|---|---|---|---|---|---|---|---|
| 1 | 01–03 | A | antes de `st_03_casa_sem1` | sexta 15h–17h | 120 | não | — |
| 2 | 04–08 | A | antes de `st_08_casa_sem2` | sexta 15h–18h | 180 | não | — |
| 3 | 09–12 | A | antes de `st_12_casa_sem3` | sexta 15h–18h | 180 | não | — |
| 4 | 13, 14 | A | antes de `st_14_comemoracao` | sexta 15h–18h (a festa começa às 18h) | 180 | não | — |
| 5 | 15 | B | `st_15`, antes de `# Volta para casa.` | segunda 16h–19h | 180 | sim | — |
| 6 | 16 | B | `st_16`, depois dos `hide` finais e antes de `stop music fadeout 1.0` / `scene bg quarto_noite` | terça 18h–20h30 (noite no coworking) | 150 | sim | `st_16`: `set_time(19, 0)` vira `set_time(21, 0)` |
| 7 | 17 | B | `st_17`, antes de `scene bg startup_coworking_tarde` / `set_time(14, 30)` | quarta 12h–14h30 (almoço) | 150 | sim | — |
| 8 | 18 | B | `st_18`, depois do bloco do pico e antes de `# Quinta: todos estão juntos no demo day.` | quarta 13h30–16h30 | 180 | sim | — |

**Corporativo** (18 cenas)

| Sem. | Cenas | Gancho | Ponto | Dia e horário | Bloco | mesmo_dia | Ajuste |
|---|---|---|---|---|---|---|---|
| 1 | 01–03 | A | antes de `co_03_casa_sem1` | sexta 15h–17h | 120 | não | — |
| 2 | 04–08 | A | antes de `co_08_casa_sem2` | sexta 16h30–19h30 (depois do café da `co_07`) | 180 | sim | — |
| 3 | 09–12 | A | antes de `co_12_casa_sem3` | sexta 15h–18h | 180 | não | — |
| 4 | 13, 14 | A | antes de `co_14_comemoracao` | sexta 13h–16h (a surpresa do Jorge é às 16h) | 180 | não | — |
| 5 | 15 | B | `co_15`, antes do `scene black` do cartão da semana 5 | sexta 15h–18h | 180 | não | — |
| 6 | 16 | B | `co_16`, antes do `scene black` do cartão da semana 6 | sexta 15h–18h | 180 | não | — |
| 7 | 17 | B | `co_17`, antes do `scene black` do cartão da semana 7 | quinta 14h–17h | 180 | não | — |
| 8 | 18 | A | antes de `co_18_implantacao_avaliacao` | sexta 18h–21h (antes da janela de sábado, 0h) | 180 | não | — |

Ponto de parada de aula (ver 8.2): `call im_ponto_parada(N) from _pp_<rota>_sN` logo depois, na cadeia, da cena que
mostra o cartão "Fim da Semana N" (semanas 1 a 7). Na semana 8 o epílogo já é a parada.

### 1.2 Tempo, custos e quantas ações cabem

| Ação | Minutos | Energia | Recompensa | Limite por intermissão |
|---|---|---|---|---|
| Conversar | 30 | 0 | amizade +0,5 | 1 por pessoa |
| Observar o uso | 90 | −1 | pista de uso (se houver na semana) + amizade +0,5 com quem é observado | 1 por local |
| Estudar | 60 | −1 | registro extra no notebook | 1 |
| Descansar | 60 | +2 | energia | 1 |
| Ajudar alguém | 90 | −2 | amizade +1,0 + pista técnica (se houver) | 1 por pessoa |
| Mentoria | 90 | −1 | amizade +1,0 com quem orienta + passo do arco (às vezes pista) | 1 |

- Bloco padrão: 180 min. Semana 1: 120 min (tutorial). Startup semanas 6 e 7: 150 min.
- Em 180 min cabem de 2 a 4 ações (ex.: ajudar 90 + observar 90; ou 3 conversas + estudar; ou mentoria + descansar
  + conversar). Nunca dá para fazer tudo o que o mapa oferece.
- **Teto de amizade por intermissão:** +1,0 por pessoa e +2,0 no total. Ao bater o teto, a ação continua (a cena
  roda, a pista vem), só a amizade não sobe; o aviso diz isso. Máximo teórico: 15 pontos em 8 semanas.
- A intermissão **não chama `set_available`**: o celular continua como a cena anterior deixou, e o ponto de amizade
  do chat não reabre.

### 1.3 Relógio no início
`im_iniciar(semana)`:
1. `fim = inicio + bloco`.
2. Se `mesmo_dia` e o relógio já passou de `inicio`, começa no relógio atual e mantém `fim` (bloco menor, mínimo
   90 min). Se `mesmo_dia` é falso, faz `set_time(inicio)`.
3. Desconta do bloco: hora extra pendente (`im_hora_extra`, até 60 min) e o efeito da energia baixa (seção 4.3).
   Mínimo final: 60 min.
4. Se `mesmo_dia` e o relógio já passou de `fim − 90`, o bloco fica com 90 min e termina depois do previsto (a cena
   seguinte pode voltar o relógio). Nesse caso grava o aviso `relogio_volta` no log (`renpy.log`) para o autopiloto
   relatar.

Cada ação chama `advance_minutes(custo)`. O relógio do canto (`top_right_clock`) mostra a hora real.

### 1.4 Quando o tempo acaba
- Quando os minutos restantes não pagam nenhuma ação disponível, o mapa não volta: aparece o fechamento.
- O jogador pode **encerrar antes** a qualquer momento ("Encerrar o tempo livre"). Se sobraram 60 min ou mais,
  ganha +1 de energia ("Você vai para casa mais cedo").
- Fechamento (`screen im_resumo`): o que fez, amizade ganha, pistas novas, registro extra, energia, e uma linha
  "Ficou para outra vez: ..." com até 3 coisas que estavam no mapa e não couberam. É a lição de capacidade: escolher é
  deixar algo de fora.
- Depois do fechamento, `im_encerrar(semana)` aplica a recuperação de fim de semana (+3 de energia, teto 10),
  zera `im_semana_atual` e devolve o controle à cena.

### 1.5 Fluxo (labels)

```renpy
label im_intermissao(semana):
    if persistent.im_pular:            # preferência "Tempo livre: pular" (aula curta)
        $ im_iniciar(semana, pulada=True)
        $ im_encerrar(semana)
        return
    $ im_iniciar(semana)
    call im_abertura(semana)           # cartão: "Tempo livre · Semana 3 · Sexta, 15h às 18h · 180 min"
label .mapa:
    if not im_opcoes(semana):
        jump .fim
    call screen im_mapa(semana)
    if _return == "encerrar":
        jump .fim
    call im_executar(_return)          # desconta tempo/energia, chama o conteúdo, aplica recompensas
    jump .mapa
label .fim:
    call screen im_resumo(semana)
    $ im_encerrar(semana)
    return
```

`im_abertura` da semana 1 é o tutorial: 4 a 6 falas da guia da rota (Emily, Tainá, Valéria) explicando mapa,
custo em minutos, energia, pistas e que "nada aqui é obrigatório para aprender; é o seu tempo".

### 1.6 Conteúdo: labels por convenção
`im_executar` procura, nesta ordem, e chama a primeira que existir (`renpy.has_label`):

1. `im_<rota>_s<N>_<acao>_<alvo>` (alvo = id da pessoa para conversar/ajudar; id do local para observar, estudar,
   descansar). Ex.: `im_startup_s5_ajudar_st_techlead`, `im_saude_s2_observar_ambulatorio`.
2. `im_<rota>_<acao>_<alvo>` (vale para qualquer semana).
3. `im_generico_<acao>` (texto curto com os dados da ação; para conversar com personagem offline, usa a próxima fala
   de `AMIGOS_DATA[cid]["offline"]`).

Mentoria: `im_<rota>_mentoria_<k>` (k = 1..5), independente da semana. Toda vez que cair no genérico, escreve no
log (`renpy.log`) o nome do label que faltou; o autopiloto junta esses nomes no relatório para os escritores verem o
que falta. Isso não vai para o save.

Tamanho de referência: conversar 8–14 falas; observar 15–25; estudar 6–10 (termina no registro extra); ajudar 15–25;
mentoria 20–30; descansar 3–6. Cada conteúdo pode testar `energia_cansaco()` para uma fala alternativa.

---

## 2. Mapa

### 2.1 Locais (POI) por rota

Cada rota tem 5 locais desde a semana 1 e 1 ou 2 que abrem depois. `acoes` lista as ações ligadas ao local (as
ações com pessoa — conversar, ajudar, mentoria — vêm da agenda).

**Saúde**

| id | Nome | Fundo | Abre | Ações do local |
|---|---|---|---|---|
| `mesa` | Mesa da equipe | `escritorio_interior_tarde` | 1 | — |
| `sala_reunioes` | Sala de reuniões | `sala_reunioes_tarde` | 1 | estudar |
| `cafe` | Café | `empresa_cafe_tarde` | 1 | descansar |
| `refeitorio` | Refeitório | `refeitorio_tarde` | 1 | — |
| `praca` | Praça em frente | `empresa_exterior_manha` | 1 | descansar |
| `ambulatorio` | Ambulatório do Instituto | `escritorio_medica` | 2 (depois da entrevista) | observar |
| `servidores` | Sala de servidores | `sala_servidores` | 6 | — |

**Startup**

| id | Nome | Fundo | Abre | Ações do local |
|---|---|---|---|---|
| `mesa` | Mesa da equipe | `startup_coworking_tarde` (noite na sem. 6) | 1 | — |
| `sala_vidro` | Sala de vidro | `sala_reunioes_tarde` | 1 | estudar |
| `cafe` | Café da esquina | `empresa_cafe_tarde` | 1 | descansar |
| `terraco` | Terraço | `startup_terraco_noite` (E3 pode gerar versão de tarde) | 1 | descansar |
| `ponto` | Ponto de ônibus | `transito_tarde` | 1 | descansar (caminhada) |
| `bandejao` | Bandejão da universidade | `refeitorio_tarde` | 2 (depois da entrevista com a Bia) | observar |
| `aceleradora` | Aceleradora Maré | `demo_day_auditorio` | 6 | — |

**Corporativo**

| id | Nome | Fundo | Abre | Ações do local |
|---|---|---|---|---|
| `baia` | Baia do Farol | `escritorio_interior_tarde` | 1 | — |
| `central` | Central de atendimento | `central_atendimento_tarde` | 1 | observar |
| `cafe` | Café do térreo | `empresa_cafe_tarde` | 1 | descansar |
| `refeitorio` | Refeitório | `refeitorio_tarde` | 1 | descansar |
| `arquivo` | Sala do arquivo | `sala_arquivo_tarde` | 1 | estudar |
| `sala_cab` | Sala do CAB | `sala_reunioes_tarde` | 5 | — |
| `servidores` | Sala de servidores | `sala_servidores` | 7 | — |

Um local pode aparecer fechado numa semana (`"fechado": _("Fechado à noite")`), com o motivo escrito.

### 2.2 Agenda (quem está onde, por semana)

Ids curtos nas tabelas: saúde — Emily `developer_requirements`, Lucas `developer_ai`, Joseph `developer_coding`,
Robert `developer_management`, Daiana `developer_quality`, Heitor `developer_project`, Mateus `developer_security`,
César `developer_test`, Michelle `doutora_1`, Nathalia `doutora_2`. Negrito = aceita **ajudar** nessa semana
(com a pista entre parênteses, quando houver). ★ = mentoria disponível ali.

**Saúde**

| Sem. | mesa | sala_reunioes | cafe | refeitorio | praca | ambulatorio | servidores |
|---|---|---|---|---|---|---|---|
| 1 | Emily, Joseph | Robert | Lucas, César | Daiana, Heitor | Mateus | — | — |
| 2 | **Joseph**, Mateus | Robert, Heitor | Emily | Daiana, César | Lucas | Nathalia ★, Michelle | — |
| 3 | Daiana, Lucas | Emily, **Robert** | Joseph, César | Heitor, Mateus | — | Nathalia ★ | — |
| 4 | Mateus (não sabe da festa) | Robert, Heitor | Emily, Daiana | Joseph, **César**, Lucas | — | Nathalia ★, Michelle | — |
| 5 | **Joseph** (saude_p_memoria), César | Robert, Emily | Lucas | Daiana, Heitor | **Mateus** (saude_p_papeis) | Nathalia ★ | — |
| 6 | **Joseph** (saude_p_memoria), Lucas | Heitor | Emily, Daiana | Robert | César | Nathalia ★ | **Mateus** (saude_p_backup) |
| 7 | **César** (saude_p_memoria), Daiana | Robert, Heitor | Joseph | Lucas, Emily | — | Nathalia ★, Michelle | **Mateus** (saude_p_backup) |
| 8 | Emily, Robert | Heitor, Daiana | Lucas, Joseph | — | César | Nathalia ★ | Mateus |

Observar no ambulatório: S2 → `saude_p_cpf`; S3 e S4 → `saude_p_autosave`; demais semanas, só cena.

**Startup** (Tainá `st_mentora`, Otávio `st_techlead`, Davi `st_mobile`, Lorena `st_qualidade`, Vinícius `st_ceo`,
Bia `st_estudante`)

| Sem. | mesa | sala_vidro | cafe | terraco | ponto | bandejao | aceleradora |
|---|---|---|---|---|---|---|---|
| 1 | **Davi**, Otávio | Tainá | Lorena | Vinícius | — | — | — |
| 2 | **Otávio**, Davi | Vinícius | Tainá | — | — | Bia, Lorena ★ | — |
| 3 | Davi, Tainá | Otávio | Vinícius | — | — | Bia, Lorena ★ | — |
| 4 | Davi | Vinícius, Tainá | Otávio | fechado ("arrumando a festa") | — | Bia, Lorena ★ | — |
| 5 | **Otávio** (st_p_conexoes), **Davi** (st_p_logs) | Tainá | Vinícius | — | — | Bia, Lorena ★ | — |
| 6 | **Davi** (st_p_loja), **Otávio** (st_p_conexoes) | — | Bia e duas testers | Tainá, Lorena ★ | — | fechado à noite | **Vinícius** (st_p_retencao) |
| 7 | Otávio | **Davi** (st_p_loja) | Tainá | — | — | Bia, Lorena ★ | **Vinícius** (st_p_retencao) |
| 8 | Davi, Otávio | Tainá | — | — | — | Bia, Lorena ★ | **Vinícius** (st_p_retencao) |

Observar: S2 bandejão → `st_p_cancelar`; S3 bandejão → `st_p_tunel`; S4 bandejão → `st_p_bolsa`; S6 café, S5/S7/S8
bandejão → só cena.

**Corporativo** (Valéria `co_mentora`, Jorge `co_legado`, Kauã `co_dev`, Ingrid `co_qualidade`, Rosângela
`co_supervisora`, Edson `co_solicitante`)

| Sem. | baia | central | cafe | refeitorio | arquivo | sala_cab | servidores |
|---|---|---|---|---|---|---|---|
| 1 | **Kauã** | Rosângela | Valéria | — | Jorge | — | — |
| 2 | Kauã, Ingrid | Rosângela | Edson | Valéria | Jorge ★ | — | — |
| 3 | Valéria | Rosângela, Edson | Kauã | Ingrid | Jorge ★ | — | — |
| 4 | Jorge ★ (não sabe da festa) | Rosângela | Valéria, Ingrid | Kauã | — | — | — |
| 5 | Kauã | Rosângela, Edson | Valéria | — | Jorge ★ | **Ingrid** (co_p_botao) | — |
| 6 | **Kauã** (co_p_senha), Valéria | Rosângela | Edson | — | Jorge ★ | **Ingrid** (co_p_botao) | — |
| 7 | Kauã | Rosângela | Valéria | Edson | Jorge ★ | — | **Ingrid** (co_p_parada) |
| 8 | Kauã, Ingrid | turno da noite (sem personagem) | Valéria | — | Jorge ★ | — | — |

Observar na central: S1 → `co_p_ligacoes`; S2 → `co_p_vazio`; demais semanas, só cena.

### 2.3 Formato de dados (exemplo: Startup, trecho)

```python
init 3 python:
    ROUTES["startup"]["mapa"] = {
        "imagem": "images/mapas/startup.png",      # opcional (E3); sem ela, a tela usa a grade
        "musica": "music_office_relaxed",
        "pois": [
            {"id": "mesa", "nome": _("Mesa da equipe"), "bg": "startup_coworking_tarde",
             "pos": (420, 380), "abre": 1, "acoes": []},
            {"id": "sala_vidro", "nome": _("Sala de vidro"), "bg": "sala_reunioes_tarde",
             "pos": (900, 260), "abre": 1, "acoes": ["estudar"]},
            {"id": "bandejao", "nome": _("Bandejão da universidade"), "bg": "refeitorio_tarde",
             "pos": (1300, 700), "abre": 2, "acoes": ["observar"]},
            # ...
        ],
    }

    ROUTES["startup"]["intermissoes"] = {
        3: {
            "dia": _("Sexta"), "inicio": (15, 0), "bloco": 180, "mesmo_dia": False,
            "agenda": {                      # local -> pessoas
                "mesa": ["st_mobile", "st_mentora"],
                "sala_vidro": ["st_techlead"],
                "cafe": ["st_ceo"],
                "bandejao": ["st_estudante", "st_qualidade"],
            },
            "fechados": {},                  # local -> motivo escrito
            "ajudar": {},                    # pessoa -> pista ou None (só quem está aqui aceita ajuda)
            "observar": {"bandejao": "st_p_tunel"},   # local -> pista ou None
            "estudar": "st_extra_invest",    # registro extra da semana
        },
        # 1..8
    }

    ROUTES["startup"]["pistas"] = {
        "st_p_tunel": {
            "titulo": _("O salvar repetido no subsolo"),
            "texto": _("No subsolo do bandejão o 4G cai. A Bia tocou em Salvar duas vezes porque a tela não respondeu."),
            "ate_semana": 3,                 # depois disso a ação acontece, mas a pista não é dada
            "uso": _("Semana 4: a causa do gasto duplicado."),
        },
    }

    ROUTES["startup"]["extras"] = [
        {"id": "st_extra_invest", "title": _("INVEST para histórias"), "text": _("...")},
    ]

    ROUTES["startup"]["mentoria"] = {...}             # seção 3.4
    ROUTES["startup"]["conquistas_extra"] = [...]     # seção 3.4
```

`im_validar_dados(rota)` (chamada pelos testes) confere: toda pessoa da agenda está em `route_contact_ids` (ou é
`doutora_*` na saúde); todo local existe e está aberto na semana; toda pista citada existe e `ate_semana` ≥ semana de
origem; `inicio + bloco` cabe antes de meia-noite; a mentora está na agenda de pelo menos 5 das semanas 2–8.

### 2.4 Tela `im_mapa(semana)`

Layout 1920x1080:
- **Barra superior:** "Semana 3 · Sexta · 15:30 · Tempo livre: faltam 150 min · Energia 7/10 (Boa)". O HUD de
  energia some enquanto o mapa está aberto para não repetir.
- **Área do mapa (2/3 da largura):** imagem ilustrada da rota (E3) com um botão por local na posição `pos`. Sem
  imagem, uma grade de cartões (3 colunas). Cada botão mostra: nome do local; retratos de 64 px com o nome embaixo
  de quem está lá; uma linha de estado escrita ("2 pessoas", "Ninguém agora", "Fechado à noite", "Abre na semana 6",
  "★ Mentoria 2 de 5").
- **Painel do local (1/3):** ao focar ou clicar um local, mostra o fundo do local em miniatura, as pessoas
  (retrato 96 px, nome, papel curto de `AMIGOS_DATA[cid]["desc"]`) e a lista de ações. Cada ação é um botão com
  ícone + texto: "Conversar com Davi · 30 min · Amizade", "Ajudar Otávio · 90 min · −2 energia · Amizade e pista
  técnica", "Observar o uso · 90 min · −1 energia · Pista de uso", "Estudar · 60 min · Registro extra",
  "Descansar · 60 min · +2 energia", "Mentoria com Lorena (3 de 5) · 90 min · −1 energia".
- Ação indisponível aparece desabilitada **com o motivo escrito**: "Falta tempo (precisa de 90 min)", "Precisa de 2
  de energia", "Já feito hoje", "Teto de amizade atingido" (esta não bloqueia; só avisa).
- **Rodapé:** "Encerrar o tempo livre" e a dica "Tab ou setas escolhem; Enter confirma".

Retorno da tela: `("acao", poi, acao, alvo)` ou `"encerrar"`. A lista de opções vem de `im_opcoes(semana)`, a mesma
função que o autopiloto usa.

### 2.5 Acessibilidade
- Teclado: todos os locais e ações são botões focáveis; a ordem de foco segue a ordem de `pois`; o primeiro local
  aberto recebe o foco (`default_focus`). Enter no local foca a primeira ação do painel. Esc abre o menu do jogo,
  como hoje.
- Nada só por cor: estado, custo e recompensa sempre em texto; ícones têm forma diferente por ação.
- Leitor de tela (self-voicing): cada botão tem `alt` completo ("Café da esquina. Aqui: Tainá. Ações: descansar,
  60 minutos; conversar com Tainá, 30 minutos.").
- "Texto maior" ou a opção "Ver como lista" troca o mapa por uma lista vertical rolável dos locais, com as mesmas
  informações.
- Mochila e notebook continuam acessíveis por cima do mapa.

---

## 3. Ações, recompensas, pistas e mentoria

### 3.1 Funções principais (`logic/intermissao.rpy`)

| Função | O que faz |
|---|---|
| `im_dados(semana, rota=None)` | dict da intermissão da semana |
| `im_pois(semana)` | locais visíveis, com estado (`aberto`, `fechado`, motivo) |
| `im_quem_esta(poi, semana)` | lista de ids da agenda |
| `im_opcoes(semana)` | lista de opções disponíveis `(poi, acao, alvo, minutos, energia, rotulo)`; vazia quando nada cabe |
| `im_executar` (label) | desconta minutos (`advance_minutes`), aplica energia, chama o conteúdo, aplica recompensa, grava em `im_feitas` |
| `im_amizade(cid, valor)` | soma amizade respeitando os tetos (usa `add_friendship_point`) |
| `im_registrar_extra(rid)` | grava o registro extra em `registros` e avisa "Anotado no notebook (extra): ..." |
| `pista_ganhar(pid)` | adiciona a `pistas` se a semana ≤ `ate_semana`; avisa "Pista: <título>" |
| `pista_tem(pid)` / `pista_usar(pid)` | consulta / marca em `pistas_usadas` |
| `mentoria_proximo(rota=None)` | número do próximo encontro (1..5) ou None |
| `mentoria_avancar()` | registra o encontro; no 5º concede a conquista |

Os registros extras usam o mesmo conjunto `registros` (ids diferentes). `registros_contagem()` continua contando só
os 8 da rota; o notebook ganha a seção "Extras (opcionais): n de 7".

### 3.2 Recompensas
- **Conversar:** amizade +0,5. Conteúdo curto que mostra a pessoa fora do trabalho e às vezes antecipa o tema da
  semana seguinte.
- **Observar o uso** (elicitação por observação): o jogador vê alguém usando o sistema ou o processo real. Se a semana
  tem pista para aquele local, ganha a pista. Amizade +0,5 com a pessoa observada.
- **Estudar:** um registro extra do notebook (7 por rota, um por semana de 1 a 7). Os extras aprofundam; nunca são
  pré-requisito.
- **Descansar:** +2 de energia. Fala curta e diferente quando a energia está baixa.
- **Ajudar:** amizade +1,0 e, se a agenda indicar, uma pista técnica.
- **Mentoria:** amizade +1,0 com quem orienta e um passo do arco.

Registros extras por rota (título; o texto é escrito na E5):

| Sem. | Saúde | Startup | Corporativo |
|---|---|---|---|
| 1 | `saude_extra_glossario` Glossário do projeto | `st_extra_kanban` Kanban e limite de trabalho em andamento | `co_extra_itil` Incidente, problema e mudança |
| 2 | `saude_extra_fluxos` Fluxo alternativo e exceção | `st_extra_episodio` Perguntas abertas e episódio | `co_extra_reversa` Engenharia reversa de um banco |
| 3 | `saude_extra_acoplamento` Coesão e acoplamento | `st_extra_invest` INVEST para histórias | `co_extra_casos_uso` Caso de uso ou história? |
| 4 | `saude_extra_estimativa` Estimativa em equipe | `st_extra_idempotencia` Idempotência numa página | `co_extra_anticorrupcao` Camada anticorrupção |
| 5 | `saude_extra_revisao` O que olhar numa revisão de código | `st_extra_coorte` Retenção por coorte | `co_extra_rfc` Anatomia de uma RFC |
| 6 | `saude_extra_piramide` Pirâmide de testes | `st_extra_carga` O que medir num teste de carga | `co_extra_caracterizacao` Teste de caracterização |
| 7 | `saude_extra_rollback` Plano de rollback | `st_extra_rollout` Lançamento gradual nas lojas | `co_extra_parada` Critério de parada |

O tema de cada extra prepara a semana seguinte.

### 3.3 Pistas

Estado: `pistas` (set de ids) e `pistas_usadas` (set). Uma pista é um fato que o jogador viu. Ela entra numa cena
posterior de dois jeitos, nunca dentro da contagem de `decisao()`:

**Formato 1 — evidência antes de um menu pedagógico.** Uma linha antes do menu:

```renpy
    call pista_lembrar("st_p_tunel") from _pl_st13_idempotencia
    menu:
        "Por que o gasto apareceu duas vezes?"
        # opções pedagógicas sem mudança, com st_decidir(...) como hoje
```

`label pista_lembrar(pid)`: se o jogador não tem a pista (ou já usou), retorna sem mostrar nada. Se tem, mostra um menu
`(tipo="pista")` com "Lembrar: <título da pista>" e "Seguir sem lembrar". Lembrar mostra o `texto` da pista numa fala
do narrador e chama `pista_usar`. O menu pedagógico seguinte não muda; a primeira tentativa continua sendo do
jogador. Como a evidência foi colhida por ele, isso é elicitação, não resposta pronta. O resumo do epílogo mostra à
parte "Pistas usadas: n".

**Formato 2 — opção extra num menu social, de negociação ou de narrativa (sem `decisao`):**

```renpy
    menu (tipo="conversa"):
        "Opção que já existe":
            ...
        "Contar o que você viu: o servidor de testes reinicia toda madrugada" (tipo="pista") if pista_tem("saude_p_memoria"):
            $ pista_usar("saude_p_memoria")
            # resultado melhor: atalho na história, fala própria, +0,5 amizade, ou um risco evitado
```

A opção extra é sempre adicional: todas as opções antigas continuam e o caminho sem pista chega ao mesmo fim.

**Pistas por rota**

Saúde

| id | O que o jogador vê | Onde ganha | Até | Uso |
|---|---|---|---|---|
| `saude_p_cpf` | paciente sem CPF; a recepção anota num papel | S2 observar ambulatório | S2 | `scene_10` (S3): formato 2, incluir o fluxo do paciente sem CPF; fala da Emily, +0,5 Emily |
| `saude_p_had` | paciente pula perguntas da escala HAD no papel | S2 mentoria 1 | S2 | `scene_12` (S3): formato 1 antes de `saude_d12_had` |
| `saude_p_autosave` | a médica perde o formulário quando a internet cai | S3–S4 observar ambulatório | S4 | `scene_16` (S5): formato 1 antes de `atividade_planejamento("saude_plano")` |
| `saude_p_papeis` | a recepção usa a senha da médica | S4 mentoria 3 ou S5 ajudar Mateus | S6 | `scene_19` (S7): formato 2 na revisão de papéis de acesso |
| `saude_p_memoria` | o servidor de testes reinicia toda madrugada | S5–S6 ajudar Joseph, S7 ajudar César | S7 | `scene_20` (S8): formato 2, achar o vazamento de memória mais cedo |
| `saude_p_backup` | ninguém nunca restaurou o backup | S6–S7 ajudar Mateus | S7 | `scene_20` (S8): formato 2 no checklist de deploy |

Startup

| id | O que o jogador vê | Onde ganha | Até | Uso |
|---|---|---|---|---|
| `st_p_cancelar` | Bia começa a excluir um gasto e desiste no meio | S2 observar bandejão | S2 | `st_09` (S3): formato 1 antes de `st_d09_limite` |
| `st_p_tunel` | o 4G cai no subsolo e Bia toca Salvar duas vezes | S3 observar bandejão | S3 | `st_13` (S4): formato 1 antes de `st_d13_idempotencia` |
| `st_p_bolsa` | as estudantes só abrem o app no dia da bolsa | S4 observar bandejão | S4 | `st_15` (S5): formato 1 antes de `st_d15_metrica` |
| `st_p_leitor` | o botão excluir não tem nome para o leitor de tela | mentoria 3 | S5 | `st_16` (S6): formato 2 no comentário de review; fala da Lorena |
| `st_p_conexoes` | o teste de carga usa conexões demais no banco | S5–S6 ajudar Otávio | S6 | `st_17` (S7): formato 1 antes de `st_d17_carga` |
| `st_p_logs` | o log de sincronização imprime o e-mail da pessoa | S5 ajudar Davi | S6 | `st_17` (S7): formato 2 quando o log aparece |
| `st_p_loja` | a revisão da loja levou dois dias na última versão | S6–S7 ajudar Davi | S7 | `st_18` (S8, segunda): formato 1 antes de `st_d18_rollout` |
| `st_p_retencao` | o investidor do ensaio só perguntou de retenção | S6–S8 ajudar Vinícius | S8 | `st_18` (demo day): formato 2 no pitch |

Corporativo

| id | O que o jogador vê | Onde ganha | Até | Uso |
|---|---|---|---|---|
| `co_p_ligacoes` | atendente atende três ligações de "e o meu chamado?" em 20 min | S1 observar central | S1 | `co_05` (S2): formato 1 antes de `co_ok_conflito` |
| `co_p_vazio` | atendente fecha chamado com descrição de três espaços | S2 observar central | S2 | `co_09` (S3): formato 1 antes de `co_ok_caso_limite` |
| `co_p_acentos` | o banco trocou de codificação em 2014 | mentoria 2 | S4 | `co_15` (S5): formato 1 antes de `co_ok_risco` |
| `co_p_norte` | o relatório do Norte usa outro fuso | mentoria 3 | S5 | `co_16` (S6): formato 2, registrar o fuso como problema conhecido antes; fala do Jorge |
| `co_p_botao` | o perfil atendente só não vê o botão; pela URL a ação funciona | S5–S6 ajudar Ingrid | S6 | `co_17` (S7): formato 1 antes de `co_ok_rbac` |
| `co_p_senha` | uma senha de serviço num arquivo de configuração | S6 ajudar Kauã | S6 | `co_17` (S7): formato 2 no caso da senha em arquivo |
| `co_p_parada` | no ensaio, o rollback da carga levou 40 min | S7 ajudar Ingrid | S7 | `co_18` (S8): formato 1 antes de `co_ok_janela` |

O texto exato de cada menu e o ponto da linha `pista_lembrar` ficam com o escritor da rota (E5), que conhece a cena.

### 3.4 Arcos de mentoria

Um por rota, 5 encontros. O encontro k fica disponível a partir da semana `semana_min` e só depois do encontro k−1.
São 7 intermissões possíveis (S2 a S8) para 5 encontros: dá para pular até duas semanas. Um encontro por
intermissão. Quem não concluir não perde nada; o resumo mostra "Mentoria: 3 de 5".

Formato:

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

| Rota | Arco | Quem orienta | Encontros (semana mínima) | Pistas | Conquista |
|---|---|---|---|---|---|
| Saúde | Um dia de ambulatório | Dra. Nathalia (`doutora_2`) | 1 triagem e escala no papel (2) · 2 retorno de um paciente (3) · 3 quem vê o quê (4) · 4 a consulta de 15 minutos (5) · 5 a paciente testa o protótipo (6) | 1 → `saude_p_had`, 3 → `saude_p_papeis` | `mentoria_conq_saude` "Olhar de Ambulatório" |
| Startup | Clube das testers | Lorena (`st_qualidade`), com a Bia e colegas | 1 apresentar o beta (2) · 2 cinco tarefas cronometradas (3) · 3 leitor de tela (4) · 4 calouros e o pico (5) · 5 o primeiro relato de bug das testers (6) | 3 → `st_p_leitor` | `mentoria_conq_startup` "Clube das Testers" |
| Corporativo | Causos do SGC | Jorge (`co_legado`) | como no exemplo acima | 2 → `co_p_acentos`, 3 → `co_p_norte` | `mentoria_conq_corporativo` "Causos Registrados" |

Na saúde, a mentoria com uma stakeholder não conta para a amizade do final (a regra soma só os 8 developers); é
intencional: o arco é sobre ouvir quem usa.

No corporativo, se `mentoria_passos["corporativo"] >= 2` antes da `co_14`, a homenagem ao Jorge ganha uma fala extra
(sem mudar `co_conq_memoria`).

Conquistas extras: `default mentoria_conq_saude = False` (e as outras duas). Ficam em
`ROUTES[rota]["conquistas_extra"]`, que `resumo_rota` mostra numa linha própria ("Do tempo livre"). Não entram em
`route_achievements()`, por isso `st_conquistas()`, `co_conquistas()` e `final_saude()` não mudam.

---

## 4. Tempo e energia

### 4.1 Energia semanal
- `default energia_semana = 8`, escala 0 a 10, sempre inteira.
- Estados (texto sempre visível junto do número):

| Energia | Estado |
|---|---|
| 8–10 | Alta |
| 4–7 | Boa |
| 2–3 | Cansaço |
| 0–1 | Exaustão |

- Funções: `energia_gastar(n, motivo)`, `energia_ganhar(n, motivo)` (limitam a 0..10 e avisam
  "Energia −3: virou a noite (7 → 4)"), `energia_estado()`, `energia_cansaco()` (True com 3 ou menos).
- `energia_diaria` e `nivel_estresse` continuam no save e não são lidos. A linha `$ energia_diaria = 1` da `scene_18`
  fica; ao lado entra `energia_gastar(3, ...)`.

### 4.2 O que gasta e o que recupera

| Gasta | Quanto |
|---|---|
| Observar, estudar, mentoria | −1 |
| Ajudar | −2 |
| Horas extras e viradas citadas nas cenas (tabela abaixo) | −1 a −3 |

| Recupera | Quanto |
|---|---|
| Descansar na intermissão | +2 |
| Encerrar a intermissão com 60 min ou mais sobrando | +1 |
| Fim de semana (`im_encerrar`, toda semana) | +3 |

Eventos nas cenas (o escritor da rota põe a linha no ponto indicado; `im_hora_extra_somar(min)` tira tempo da
próxima intermissão):

| Rota | Cena | Gatilho | Efeito |
|---|---|---|---|
| Saúde | `scene_12` | fim da especificação, já de noite | −1 |
| Saúde | `scene_18` | "Virar a noite e entregar tudo ainda hoje." | −3 e hora extra 60 |
| Saúde | `scene_19` | caça a bugs do dia inteiro | −1 |
| Saúde | `scene_20` | dia de deploy | −2 |
| Startup | `st_11` | inspeção até 19h30 | −1 |
| Startup | `st_17` | "Tento resolver por conta própria até tarde." | −2 e hora extra 60 |
| Startup | `st_18` | pico sem o ajuste de conexões (`not st_d17_carga`) | −1 |
| Corporativo | `co_11` | inspeção até 18h30 | −1 |
| Corporativo | `co_15` | ensaio de quarta, 22h30 | −2 e hora extra 30 |
| Corporativo | `co_18` | janela de madrugada | −3 |

### 4.3 Efeitos da energia baixa
- **Cansaço (2–3):** a próxima intermissão perde 30 min de bloco; a abertura da intermissão tem fala própria;
  "Descansar" aparece primeiro na lista com a marca "Recomendado".
- **Exaustão (0–1):** perde 60 min de bloco; ações que custam mais energia do que há ficam desabilitadas com o motivo.
  Descansar e conversar continuam disponíveis.
- **Falas diferentes:** cada rota escreve pelo menos 3 falas que testam `energia_cansaco()` (ex.: a guia comenta o
  cansaço no começo da semana seguinte; o colega oferece café).
- **Nunca:** game over, bloqueio de cena, mudança em `decisao()`, registros, conquistas ou final.

A lição aparece no próprio jogo: virar a noite rende a entrega de hoje e encolhe o tempo e as escolhas da semana
seguinte.

### 4.4 HUD de tempo e energia
- Relógio: o `top_right_clock` atual, sem mudança.
- `screen energia_hud()` em `config.overlay_screens`, logo abaixo do relógio (canto superior direito, ~y 110).
  Mostra "Energia 7/10 · Boa" e 10 quadradinhos (cheio/vazado, com borda; a diferença não depende de cor).
- Aparece a partir da primeira intermissão (`energia_mostrar = True`, ligado em `im_abertura(1)`), em todas as
  cenas. Some no menu principal, nos menus do jogo e durante o mapa (que tem a própria barra).
- Toda mudança de energia também sai em `renpy.notify`, com o motivo.

---

## 5. Novas mecânicas pedagógicas

As duas são do caminho principal (não da intermissão), reaproveitáveis: o código é um só e cada rota entra com dados.
Ambas registram em `decisao()` só a primeira tentativa e seguem o padrão do jogo: feedback com consequência concreta e
revisão orientada, sem punição.

### 5.1 Caça à ambiguidade

**Ideia:** o jogador marca as palavras vagas de um requisito e depois escolhe como tornar cada uma verificável.

**Dados:**

```python
ROUTES["startup"]["ambiguidades"] = {
    "st_amb_total": {
        "contexto": _("Pedido do Vinícius, copiado do quadro de ideias."),
        "segmentos": [
            _("O app deve mostrar o "), ("isca", "total", _("total do mês")), _(" atualizado "),
            ("vaga", "rapido", _("rapidamente")), _(" e deixar a pessoa excluir "),
            ("isca", "gastos", _("gastos")), _(" "), ("vaga", "facil", _("facilmente")),
            _(", "), ("vaga", "sem_perder", _("sem perder dados")), _("."),
        ],
        "iscas": {   # termo -> por que não é vago
            "total": _("'Total do mês' está definido no glossário: soma dos gastos do mês corrente."),
            "gastos": _("'Gasto' é um termo do domínio, com campos definidos."),
        },
        "vagas": {   # termo -> por que é vago + 3 reescritas (1 adequada, 2 distratores)
            "rapido": {
                "porque": _("Cada pessoa imagina um tempo diferente; não dá para testar."),
                "opcoes": [
                    {"texto": _("em até 2 s depois de salvar, em 95% das vezes no 4G"), "adequada": True},
                    {"texto": _("o mais rápido possível"), "adequada": False,
                     "feedback": _("Continua sem número. O teste não tem como passar ou falhar.")},
                    {"texto": _("instantaneamente"), "adequada": False,
                     "feedback": _("Promessa impossível de medir e de cumprir no 4G.")},
                ],
            },
            # "facil", "sem_perder"
        },
    },
}
```

Regras de escrita: 2 a 4 palavras vagas e 2 iscas por requisito; todo distrator explica a consequência concreta.

**Interação** (`call amb_atividade("st_amb_total") from _amb_st09`):
1. **Marcar** (`screen amb_marcar`): o requisito aparece como texto corrido; palavras vagas e iscas são botões que
   alternam "marcada/não marcada". A marcação aparece como sublinhado + colchete e o estado vai no `alt` ("rapidamente,
   marcada como vaga"), não só por cor. Teclado: Tab/setas entre as palavras, Enter alterna, botão "Conferir".
   O texto comum não é clicável.
2. **Conferir:** "Você achou 2 de 3 palavras vagas e marcou 1 termo que não é vago." Para cada isca marcada, mostra o
   motivo. **Revisão orientada:** se faltou alguma vaga, a tela mostra quantas faltam e deixa marcar de novo; na
   segunda conferência, as que faltaram aparecem indicadas com a explicação. `decisao("<id>_marcar", True)` só se a
   primeira conferência achou todas as vagas sem iscas.
3. **Tornar verificável:** para cada vaga, um menu normal (`renpy.display_menu`, `tipo="trabalho"`) com as 3
   reescritas em ordem embaralhada fixa por id. Distrator: mostra o feedback e volta ao menu.
   `decisao("<id>_<termo>", acertou_de_primeira)`.
4. **Resultado:** o requisito reescrito, com as trocas destacadas por colchete e negrito, e uma fala do personagem
   da cena.

**Estado no save:**
`amb_resultados[aid] = {"marcadas_primeira": [termos], "iscas_primeira": [termos], "faltaram": [termos],
"trocas": {termo: índice escolhido}, "primeira_ok": {termo: bool}, "concluido": bool}`.

**Onde entra (sugestão) — semana 3, especificação, nas três rotas:**

| Rota | Cena | Requisito | Vagas | Iscas | Tempo |
|---|---|---|---|---|---|
| Saúde | `scene_10_criacao_casos_uso`, antes dos casos de uso | "O sistema deve permitir que a médica registre o histórico do paciente de forma rápida e simples, e emitir alertas sempre que necessário." | rápida, simples, sempre que necessário | histórico, alertas | 6–8 min |
| Startup | `st_09_historias`, antes da primeira história | o do exemplo acima | rapidamente, facilmente, sem perder dados | total do mês, gastos | 6–8 min |
| Corporativo | `co_09_historias`, antes do critério | "A consulta deve ser rápida e mostrar informações completas; o atendente deve descrever a solução adequadamente." | rápida, completas, adequadamente | chamado, solução | 6–8 min |

A palavra "sempre que necessário" da saúde fecha com a reescrita "quando o paciente faltar à consulta de retorno,
avisar no mesmo dia a profissional que acompanha o caso", o mesmo pedido da escrita livre da `scene_12`.

### 5.2 Rastreabilidade

**Ideia:** num quadro, o jogador liga cada critério de aceitação ao requisito de origem e ao teste que o cobre. Um
critério fica sem teste de propósito. Quem acha a lacuna evita o bug; quem não acha encontra o bug na semana de
testes e vê de onde ele veio.

**Dados:**

```python
ROUTES["startup"]["rastreabilidade"] = {
    "st_rast_exclusao": {
        "requisitos": [
            {"id": "R1", "texto": _("A pessoa exclui um gasto com confirmação.")},
            {"id": "R2", "texto": _("O total do mês reflete todos os gastos sincronizados.")},
            {"id": "R3", "texto": _("Um gasto reenviado não é gravado duas vezes.")},
        ],
        "criterios": [   # "de" = requisito certo; "teste" = teste certo ou None (a lacuna)
            {"id": "C1", "de": "R1", "teste": "T1", "texto": _("Dado um gasto de R$ 20, quando confirma a exclusão, então some da lista.")},
            {"id": "C2", "de": "R1", "teste": "T2", "texto": _("Dado um gasto de R$ 20, quando cancela, então o total segue em R$ 100.")},
            {"id": "C3", "de": "R3", "teste": "T3", "texto": _("Dado o mesmo id enviado duas vezes, então o servidor grava uma vez.")},
            {"id": "C4", "de": "R2", "teste": None, "texto": _("Dado um gasto lançado offline, quando a sincronização termina, então o total mostra o novo valor sem reabrir a tela.")},
            {"id": "C5", "de": "R2", "teste": "T4", "texto": _("Dado R$ 100 no mês, quando lança R$ 5 online, então o total vai a R$ 105.")},
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

**Interação** (`call rast_atividade("st_rast_exclusao") from _rast_st16`), tela `rast_quadro`:
- À esquerda a lista de requisitos; à direita a lista de testes; no meio, uma linha por critério com dois seletores:
  "Requisito: R2" e "Teste: T4 / Nenhum teste cobre". Clique ou Enter abre um pequeno menu de escolha do seletor;
  setas esquerda/direita trocam o valor quando o seletor está focado. A lista "Ligações" ao lado repete tudo em texto
  ("C4 → R2 → sem teste").
- Botão "Conferir quadro". Retorno da tela: `("conferir", {"C1": ["R1", "T1"], ...})`.
- **Feedback das ligações** (requisito e teste errados): a linha ganha a marca "(confira)" e a explicação; o jogador
  corrige e confere de novo, quantas vezes quiser. `decisao("<id>_ligacoes", True)` se a primeira conferência acertou
  todas as ligações (exceto a lacuna).
- **A lacuna não é revelada.** Se o jogador não marcou "Nenhum teste cobre" em C4, o feedback só diz "Todo critério
  tem teste?" na primeira conferência. Na segunda, o quadro fecha com "Quadro conferido", sem apontar a lacuna.
  `decisao("<id>_lacuna", achou_na_primeira)`; `lacuna_achada` = marcou em qualquer conferência antes de fechar.
- Ao final, um resumo de cobertura por requisito ("R2: 2 critérios, 1 teste").

**Estado no save:**
`rast_quadros[qid] = {"ligacoes": {...}, "conferencias": int, "primeira": {"ligacoes_ok": bool, "lacuna_ok": bool},
"lacuna_achada": bool, "concluido": bool}`. Função `rast_lacuna_achada(qid)`.

**Onde entra e qual bug vira na semana de testes:**

| Rota | Quadro (cena, semana) | Lacuna | Bug na semana 7 | Tempo |
|---|---|---|---|---|
| Saúde | `scene_17_tarde_estudos_tecnicos` (S5), depois das perguntas | "Dado o perfil recepção, quando abre o histórico de saúde, então o acesso é negado" | `scene_19`: com a lacuna achada, César diz que o teste de papéis já pegou a falha na pipeline; sem ela, a falha aparece na revisão de segurança e a equipe volta ao quadro para ver o elo que faltou. Só narrativa: os contadores `bugs_encontrados`/`vulnerabilidades` não mudam | 8–10 min |
| Startup | `st_16_codificacao` (S6), antes do PR | C4 do exemplo | `st_17`: o bug do total que não atualiza depois da sincronização já existe na cena. Com a lacuna achada, o menu de investigação ganha a opção `(tipo="pista") if rast_lacuna_achada(...)` "Rodar o teste que você pediu na semana passada" (resolve às 16h, +0,5 Lorena); sem ela, a cena segue como hoje e Lorena liga o bug ao critério sem teste | 8–10 min |
| Corporativo | `co_16_codificacao` (S6), depois dos testes de caracterização | "Dado um atendente, quando abre pela URL a reabertura de chamado de outro setor, então recebe acesso negado e a tentativa vai para a trilha" | `co_17`: `call rast_lembrar("co_rast_farol")` antes de `co_ok_rbac` (mesma lógica de `pista_lembrar`, ativa quando `rast_lacuna_achada`); sem ela, Ingrid acha o furo na regressão e mostra o elo que faltou | 8–10 min |

---

## 6. Ajustes de UI de diálogo

### 6.1 Destacar quem fala (escurecer quem não fala)

**Técnica escolhida** (conferida no código do SDK 8.5.3):
1. `Character(..., image="<id>")` em todos os personagens com sprite (8 developers, 2 doutoras, `npc_roommate` e os
   12 das rotas novas). Isso só liga o personagem à tag da imagem; `renpy.get_say_image_tag()` passa a devolver a tag
   de quem fala. Não existe imagem `side <id>`, então o `SideImage()` da tela `say` continua sem mostrar nada.
2. Um wrapper de `config.show` (documentado: "função usada no lugar de `renpy.show` pelos comandos show e scene";
   o padrão é `renpy.exports.show`, `renpy/config.py:1656`):

```python
init python:
    FALA_TAGS = set()   # preenchido em init 3 com DEVELOPERS, doutoras, npc_roommate e route_contact_ids das rotas

    _fala_show_original = config.show

    def fala_show(name, at_list=[], layer=None, what=None, zorder=None, tag=None, behind=[], atl=None, **kwargs):
        t = tag or (name[0] if isinstance(name, tuple) else name.split()[0])
        # Só sprites de personagem; show expression (what) e fundos passam direto.
        if what is None and t in FALA_TAGS and at_list:
            extra = [fala_foco(t)]
            if persistent.vida_movimento:
                extra.append(vida_respira_para(t))
            at_list = list(at_list) + extra
        return _fala_show_original(name, at_list=at_list, layer=layer, what=what, zorder=zorder,
                                   tag=tag, behind=behind, atl=atl, **kwargs)

    config.show = fala_show
```

3. O transform `fala_foco(tag)` usa `function` com um objeto `FalaFoco(tag)` que, a cada 0,05–0,1 s, lê
   `renpy.get_say_image_tag()`: se quem fala está na tela (`renpy.showing(falante)`) e não é esta tag, escurece; se
   não, volta ao normal. Transição de 0,15 s. Escurecer = `matrixcolor = BrightnessMatrix(-0.22 * n) *
   SaturationMatrix(1.0 - 0.25 * n)`, com `n` de 0 a 1. Sem `zoom`, sem posição.

**Por que não `config.speaking_attribute`:** com imagens simples (`image developer_ai positive = "...png"`), o
atributo extra exige uma imagem com aquele atributo para cada pose; sem ela, o show falha. Isso fica para o degrau 2
(`layeredimage` com boca), quando o atributo `falando` fará sentido.

**Efeitos conferidos:**
- `show <id> <pose> at left_zoom`: ganha o foco; `show <id> <outra pose>` sem `at` mantém os transforms antigos,
  inclusive o foco.
- `show expression ... as tela at artefato_tela` (31 usos) e itens (`show item ... as notebook`): passam direto,
  porque `what` não é None ou a tag não é de personagem. `config.old_show_expression` não é afetado.
- `scene bg ...`: tag `bg`, passa direto.
- Narrador, jogador e personagens sem sprite na tela: ninguém escurece.
- Mensagem de celular (`show st_qualidade portrait at center_zoom` + fala dela): quem fala é a própria tag, fica
  normal.
- Saves: o objeto `FalaFoco` vai para a lista de cenas do save. A classe nunca pode ser removida depois de publicada
  (se precisar desligar, a preferência faz isso).
- Preferência nova: "Destacar quem fala: sim/não" (`persistent.fala_destaque`, padrão sim).

### 6.2 Alinhar nome e fala
Hoje o nome começa em `gui.name_xpos = 360` + 5 de borda = 365 px e a fala em `gui.dialogue_xpos = 402`. Mudar
`gui.name_xpos` para **397** (402 − 5). Na variante `small` (`gui.rpy`, ~linha 446), `gui.name_xpos = 130`
(135 − 5). A tela `say` não muda; o modo texto maior só altera tamanhos. Conferir por captura nos dois modos.

### 6.3 Rótulo por tipo de menu
Argumentos de menu do Ren'Py: argumentos do comando `menu` vão para a tela `choice`; argumentos de item ficam em
`i.kwargs`.

```renpy
menu (tipo="trabalho"):                     # todo item recebe o tipo do menu
    "Opção A":
        ...
    "Opção B" (tipo="conversa"):            # item pode sobrescrever
        ...
```

Tela: `screen choice(items, tipo=None)`; para cada item, `t = i.kwargs.get("tipo", tipo)`. Com `t`, o botão mostra
um selo à esquerda com ícone + texto curto e o `alt` vira "Trabalho: <texto>".

| tipo | Selo | Ícone (E3) | Usar em |
|---|---|---|---|
| `trabalho` | TRABALHO | pasta | menus pedagógicos (`decisao`, `st_decidir`, `co_acerto`), planejamento, ambiguidade |
| `conversa` | CONVERSA | balão de fala | menus sociais |
| `negociacao` | NEGOCIAÇÃO | duas setas trocando | `scene_14`, `st_13`, `co_13` e acordos |
| `pista` | PISTA | lupa | `pista_lembrar` e opções extras de pista |

O texto do selo diferencia os tipos mesmo sem cor e sem ícone. Menus sem tipo continuam iguais. `i.caption` e
`i.action` não mudam, então o autopiloto e os testes que clicam pelo texto seguem funcionando. Marcar os 223 menus é
trabalho de E5 por grep: primeiro os pedagógicos e as negociações, depois os sociais.

---

## 7. Vida nos personagens (degrau 1)

### 7.1 Respiração e balanço
```renpy
transform vida_respira(t1=2.6, t2=3.9, amp=0.006, dx=1.5):
    subpixel True
    parallel:
        ease t1 yzoom 1.0 + amp
        ease t1 yzoom 1.0
        repeat
    parallel:
        ease t2 xoffset dx
        ease t2 xoffset -dx
        repeat
```
- Entra pelo mesmo wrapper de `config.show` (6.1), só nos sprites de personagem. `left_zoom`, `center_zoom` etc.
  não mudam e os itens não respiram.
- `vida_respira_para(tag)` escolhe `t1` e `t2` estáveis por personagem: `k = sum(map(ord, tag)) % 5`,
  `t1 = 2.4 + 0.12 * k`, `t2 = 3.5 + 0.15 * k` (não usar `hash()`, que muda a cada execução).
- Amplitude máxima 0,6% (acima de 1,5% a cabeça parece esticar, segundo a pesquisa).
- Pés parados: o transform externo herda a posição do filho (`config.transform_uses_child_position`, conferido em
  `renpy/display/transform.py`), então `yalign 1.0` do `left_zoom` segura a base.
- Sem `zoom` nos transforms novos: `config.zoom_zaxis = False` não interfere.
- Preferência "Movimento dos personagens: sim/não" (`persistent.vida_movimento`, padrão sim). Vale no próximo `show`.

### 7.2 Fundos sem distorção
Todos os fundos têm 1536x1024 (3:2) e hoje são esticados para 1920x1080 (~18% na horizontal). Trocar por recorte
central 16:9, que é o resultado de `fit "cover"` centralizado:

```python
init -1 python:
    def bg_cobrir(arquivo, foco_y=0.5):
        # 1536x1024 -> recorte 1536x864 (16:9) -> 1920x1080. foco_y escolhe a faixa vertical (0 = topo).
        return Transform(arquivo, crop=(0, int(160 * foco_y), 1536, 864),
                         xysize=(config.screen_width, config.screen_height))

image bg escritorio_interior_manha = bg_cobrir("images/bg/escritorio_interior_manha.png")
```
- Mesmo nome de imagem, só muda a definição em `data/backgrounds.rpy`. Usar o recorte explícito em vez de
  `Transform(fit="cover")` evita depender de como o tamanho com sobra é posicionado pela `scene`.
- `tela_conquistas`/`creditos`: conferir por captura; se cortar texto, usar `foco_y` ou manter como está.
- Fundos novos da E3 (estilo C) já devem vir em 16:9 com sobra (ex.: 2304x1296); aí `bg_cobrir` recebe o tamanho
  como parâmetro.

### 7.3 Câmera leve
```renpy
transform cam_neutra:
    subpixel True
    zoom 1.0 xoffset 0 yoffset 0

transform cam_aproxima(x=0.5, z=1.04, t=0.8):
    subpixel True
    xanchor x xpos x yanchor 0.35 ypos 0.35
    ease t zoom z
```
- Uso só pelos helpers `cam_foco(x=0.5, z=1.04)` e `cam_reset()`, que chamam `renpy.show_layer_at(...,
  layer="master", camera=True)`. Com "Transições: desligadas" ou "Movimento: não", o tempo é 0 ou nada acontece.
- Sem `perspective True` neste degrau. A câmera mexe só na camada `master`; caixa de diálogo, relógio e HUD ficam
  fixos. Com `config.zoom_zaxis = False` e imagens planas, o zoom da câmera é igual ao 2D de sempre.
- Regras: nunca usar com artefato na tela (`artefato_tela` também está na `master`); todo `cam_foco` tem
  `cam_reset` na mesma cena; `im_intermissao` e `label start` chamam `cam_reset()` por segurança. `cam_ativo`
  (default False) registra o estado para o autopiloto.
- Dois a três momentos por rota: saúde — festa da `scene_15`, deploy da `scene_20`; startup — mil estudantes na
  `st_14`, demo day na `st_18`; corporativo — homenagem ao Jorge na `co_14`, critério de parada na `co_18`.

---

## 8. Duração e uso em aula

### 8.1 Minutos adicionados por rota (estimativa)

| Item | Minutos |
|---|---|
| Hoje (11 a 13 mil palavras por partida, decisões e atividades) | 75–90 |
| 8 intermissões (S1 ~4; S2–S8 ~6 cada: mapa + 2 a 4 ações) | +45 |
| Caça à ambiguidade | +7 |
| Rastreabilidade | +9 |
| Pontos de parada e HUD | +2 |
| **Total por rota** | **≈ 140–155** (≈ 18 min por semana de jogo) |
| Com "Tempo livre: pular" | ≈ 95–110 |

### 8.2 Sessões de aula
- **Ponto de parada por semana** (`im_ponto_parada(N)`, depois do cartão "Fim da Semana N"): tela `im_parada` com o
  resumo da semana (registros novos, decisões adequadas e com apoio, pistas, energia) e três botões: "Continuar"
  (foco inicial), "Salvar" (`ShowMenu("save")`) e "Voltar ao menu" (faz autosave antes, `MainMenu(confirm=True)`).
  Antes de mostrar a tela, `renpy.force_autosave()`.
- `save_name` (variável padrão do Ren'Py, hoje sem uso no projeto) recebe "Semana N+1 · <empresa>" no ponto de
  parada; o nome aparece na lista de saves.
- Sugestão para o professor (vai no README): 4 aulas de 50 min, duas semanas de jogo por aula (~35 min) e 10–15 min de
  discussão. Para aulas curtas, ligar "Tempo livre: pular" (`persistent.im_pular`): as atividades do caminho
  principal continuam todas.
- Objetivos de aprendizagem por semana: o cartão de fim de semana já traz o "Aprendizado"; a tela de parada repete
  o título dos registros ganhos, para fechar a aula.

---

## 9. Testes e autopiloto

### 9.1 O que o autopiloto precisa aprender (`game/tests/autopiloto.rpy`)

| Tela | Como responder | Por modo |
|---|---|---|
| `im_mapa` | devolver uma opção de `store.im_opcoes(store.im_semana_atual)` ou `"encerrar"` | `primeira`: prioridade fixa (mentoria > observar > ajudar > estudar > conversar > descansar), para cobrir pistas e mentoria; `ultima`: nas semanas pares encerra logo, nas ímpares usa a prioridade invertida; `aleatorio:n`: sorteio entre as opções, 15% de chance de encerrar |
| `im_resumo`, `im_parada` | `True` (continuar) | — |
| `amb_marcar` | `("conferir", termos)` | `primeira`: as vagas certas; `ultima`: só as iscas; `aleatorio`: subconjunto sorteado |
| `rast_quadro` | `("conferir", ligacoes)` | `primeira`: respostas certas com a lacuna; `ultima`: ligações erradas sem lacuna; `aleatorio`: sorteio |
| menus de `pista_lembrar` e das reescritas | já são `choice`: nada novo | — |

Variável de ambiente `RW_AUTOPILOTO_MAPA=prioridade|pular|aleatorio` sobrepõe a estratégia do mapa. Limite de 20
voltas ao mapa por intermissão (laço vira erro).

Novos campos no relatório JSON: `intermissoes` (quantas rodaram; esperado 8), `acoes_intermissao`, `pistas`,
`pistas_usadas`, `mentoria`, `energia` (valor no fim de cada semana), `amb_resultados`, `rast_quadros`,
`conteudo_generico` (labels de conteúdo que caíram no genérico), `relogio_volta`, `camera_nao_resetada` (o label
callback confere `cam_ativo` em cada label de cena).

### 9.2 Testes no motor (`game/tests/intermissoes.rpy`)
- `im_validar_dados` nas 3 rotas sem erro.
- `im_opcoes`: com 30 min sobrando só aparece conversar; com energia 1, ajudar fica fora; ação feita não volta.
- Teto de amizade: três ajudas simuladas na mesma intermissão somam no máximo 2,0 e 1,0 por pessoa.
- `pista_ganhar` fora da janela (`ate_semana`) não grava; `pista_lembrar` sem a pista não mostra menu.
- Mentoria: passo 2 não aparece antes do passo 1; o 5º concede a conquista extra e não muda `st_conquistas()`,
  `co_conquistas()` nem o final.
- Energia: nunca sai de 0..10; Cansaço tira 30 min e Exaustão 60 min do bloco; `im_encerrar` soma 3.
- Isolamento: `len(aprendizagem)` e `registros_contagem()` não mudam ao rodar uma intermissão inteira.
- Ambiguidade e rastreabilidade: pontuação da primeira tentativa, revisão orientada e retomada (chamar de novo com o
  mesmo id não sobrescreve `decisao`).
- `fala_show`: `show expression` e `scene` passam sem foco; sprite de personagem recebe `fala_foco`.
- Save antigo: carregar um save da versão atual (antes da intermissão) cai nos `default` e segue.
- `ponta_a_ponta` (3 rotas, `primeira`): além das asserções de hoje, `intermissoes == 8`, `relogio_volta == []`,
  `camera_nao_resetada == []`. Uma rodada extra com `RW_AUTOPILOTO_MAPA=pular` deve chegar a 8 de 8 registros no
  modo `primeira` (prova de que nada obrigatório depende do tempo livre).

---

## 10. O que entra no save

| Variável | Tipo e valor inicial | Uso |
|---|---|---|
| `im_semana_atual` | int, 0 | semana da intermissão em curso (0 = fora) |
| `im_minutos` | int, 0 | minutos que restam no bloco |
| `im_fim` | tupla (h, m), (0, 0) | fim do bloco |
| `im_feitas` | dict, {} | `{rota: {semana: {"acoes": [[poi, acao, alvo]], "amizade": {cid: x}, "minutos_usados": n, "encerrou_cedo": bool}}}` |
| `im_hora_extra` | int, 0 | minutos a descontar da próxima intermissão |
| `pistas` | set, set() | ids das pistas ganhas |
| `pistas_usadas` | set, set() | ids lembrados ou usados numa cena |
| `mentoria_passos` | dict, {} | `{rota: encontros feitos}` |
| `mentoria_conq_saude`, `mentoria_conq_startup`, `mentoria_conq_corporativo` | bool, False | conquistas extras |
| `energia_semana` | int, 8 | energia 0..10 |
| `energia_mostrar` | bool, False | HUD ligado depois da primeira intermissão |
| `amb_resultados` | dict, {} | seção 5.1 |
| `rast_quadros` | dict, {} | seção 5.2 |
| `cam_ativo` | bool, False | câmera fora do neutro |
| `save_name` | já existe no Ren'Py | nome do save por semana |

Os registros extras entram no `registros` que já existe. Preferências (fora do save, em `persistent`):
`fala_destaque` (True), `vida_movimento` (True), `im_pular` (False).

Saves antigos: todos os novos estados têm `default`, então carregam com o valor inicial. Os calls novos na cadeia têm
`from`, e os pontos de retorno antigos (`_scene_X`, `_st_X`, `_co_X`) não mudam; um save feito no meio de uma cena
volta para o retorno de sempre e encontra a intermissão como próxima instrução. Ganchos B dentro de cenas também
levam `from`.

---

## 11. Ordem de implementação e riscos

1. E4: energia, estado da intermissão, `im_opcoes`, fluxo, tela do mapa com a grade (sem a arte), ponto de parada,
   autopiloto do mapa, testes. Dados de teste mínimos para as 3 rotas.
2. E4: `fala_show` + `image=` + alinhamento do nome + tipos de menu.
3. E6: ambiguidade e rastreabilidade com dados das 3 rotas.
4. E5: dados completos e conteúdo por rota (um escritor por rota, arquivos próprios), ganchos B, pistas nas cenas,
   eventos de energia.
5. E7: `vida_respira`, `bg_cobrir`, câmera; E3 entrega mapas ilustrados e ícones.
6. E8: matriz do autopiloto (3 rotas × modos, mais `pular`), lint limpo, capturas de UX.

Riscos:
- **Farm de amizade:** contido pelos tetos (2,0 por intermissão). O chat já permite mais; não mexer nele agora.
- **Excesso de texto:** 24 intermissões × ~3 conteúdos lidos por partida. O genérico cobre lacunas; o relatório lista
  o que falta.
- **Pistas dentro de menus pedagógicos:** só pelo formato 1, fora da contagem. Revisor da rota confere que a pista
  descreve o que foi visto, não a resposta.
- **Classe `FalaFoco` no save:** não remover depois de publicar.
- **Relógio:** a tabela 1.1 foi montada com os `set_time` atuais; o aviso `relogio_volta` pega qualquer mudança
  futura nas cenas.
