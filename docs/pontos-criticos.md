# Pontos críticos que podem quebrar o jogo + ações

> Revisão adversarial gerada em 2026-06-06 (caça em 4 lentes → verificação que tentou **refutar**
> cada candidato rastreando o código e os assets em disco). 39 candidatos → 15 "confirmados" /
> 24 refutados. Os 15 confirmados colapsam em **6 causas-raiz** (vários eram relatos duplicados).

## ⚠️ Nota metodológica importante (leia antes)

Houve **discordância entre os verificadores** sobre uma classe de problema: **imagens ausentes**.
Há dois desfechos possíveis no Ren'Py e eles dependem de flags de config (`config.developer`,
`config.debug`, `config.raise_image_load_exceptions`, `config.missing_image_callback`):

- **Pior caso:** exceção não tratada → tela vermelha "An exception has occurred" (trava a cena).
- **Caso brando:** um placeholder de texto vermelho "Image ... not found" no lugar da arte, e o jogo continua.

**O que é fato (verificado em disco, sem controvérsia):** os arquivos/atributos/ids citados
**realmente não existem**. **O que é incerto:** se cada um *trava* ou só *degrada* — os traces do
SDK feitos pelos agentes chegaram a conclusões opostas. Evidência empírica a favor do "degrada":
o `traceback.txt` commitado é de **outro** bug (`is_web`/`renpy_platform`), e uma sessão registrada
em `log.txt` chegou até o **chat** (ou seja, passou pela `scene_1`, que tem uma imagem ausente na
linha 64) sem travar ali.

**Conclusão prática:** trate todos como **must-fix** (um jogo "pronto" não pode mostrar placeholders
de erro nas cenas principais), aplique a **rede de segurança global** (`config.missing_image_callback`,
ver §8) e **confirme rodando** (lint + playthrough) — é a única forma de saber crash vs. placeholder
na sua config. Os itens **P3** e **P4** abaixo **independem** dessa controvérsia (são bugs de lógica/softlock).

---

## Resumo (por causa-raiz)

| # | Ponto crítico | Onde | Quebra? | Sev. |
|---|---|---|---|---|
| **P1** | Arquivos de imagem ausentes via `show expression "<path>"` | scenes 1,4,9,10,13,14,16,17,18_2,19,20,21 | Placeholder→Crash (disputado) | 🔴 |
| **P2** | Atributos de sprite ausentes (`show dev_X enthusiastic/positive`) | ~16 locais (scenes 11,12,14,15,16,19,20,21) | Placeholder→Crash (disputado) | 🟠 |
| **P3** | `bg creditos` indefinido | epílogo `creditos_finais:89` | Placeholder→Crash (disputado) | 🟠 |
| **P4** | Contato `doutora_2` com id errado → persona/portrait errados | `contacts_screen.rpy:390` | Funcional (persona/afinidade) ± crash | 🔴 |
| **P5** | Replay `jump start` não reseta estado → **final errado** | `scene_epilogo...:81-82` | **Sim (lógica)** | 🔴 |
| **P6** | Chat: save durante request → **softlock** do chat | `chat_screen.rpy` + `progress.rpy` | **Sim (softlock)** | 🔴 |
| **P7** | Transform **`left_zoom2` indefinido** no `at` de um `show` | `scene_11_almoco_equipe.rpy:127` | **Sim (NameError em runtime)** | 🔴 |

> ✅ O fluxo `scene_1 → jump scene_2 → (retry) jump scene_1` foi **investigado e NÃO é bug** — é
> lógica intencional de re-escolha de emprego. Não mexer (ver `reestruturacao-projeto.md §5.4`).

---

## Evidência: lint do SDK 8.5.3 (executado em 2026-06-06)

`renpy 8.5.3.26051504 lint` rodou com **exit 0** (compila/linta sob Python 3.12 — compatibilidade de
engine OK). Porém reportou os defeitos abaixo. **Crucial:** o lint é **estático** e **não** pega:
P1 (imagens via `show expression "<path>"` — caminho é string avaliada em runtime), P4 (id errado),
P5 (replay), P6 (chat). Ou seja, "o jogo abriu/rodou" + "lint exit 0" **não** significam que esses
pontos estão OK — eles só aparecem em runtime nas cenas/escolhas certas.

O que o lint **confirmou**:
- **P2** (atributos `'X' is not an image`): `developer_project positive` (scene_11:52,64,67; scene_20:69,117,153), `developer_quality enthusiastic` (scene_11:162,165; scene_12:165), `developer_ai enthusiastic` (scene_14:134; scene_15:38; scene_20:121), `developer_security enthusiastic` (scene_15:111; scene_19:73), `developer_management positive` (scene_16:63), `developer_management enthusiastic` (scene_21:131).
- **P3** (`'bg creditos' is not an image`): scene_epilogo:89.
- **P7** (novo): scene_11:127 `Could not evaluate 'left_zoom2'` (transform indefinido).
- **Áudio não carregável** (muito além do que tínhamos — ver §7).
- **`im.Scale` obsoleto** em `backgrounds.rpy` (21 ocorrências) — ver `migracao-renpy-8.5.3.md §3`.
- Estatísticas: 728 blocos de diálogo, 115 imagens, 29 telas, 49 menus.

---

## P7 — Transform `left_zoom2` indefinido 🔴 (NameError garantido)

`scene_11_almoco_equipe.rpy:127` faz `show developer_project serious at left_zoom2`, mas esse transform
**não existe**. Os definidos em `characters.rpy` são: `left_zoom`, **`left_zoom_2`**, `center_zoom`,
`right_zoom`, `right_zoom2`. Um nome indefinido no `at` levanta erro ao executar o `show` → crash.

**Ação P7:** em `scene_11_almoco_equipe.rpy:127`, trocar `at left_zoom2` por **`at left_zoom_2`**
(o transform realmente definido). 
**Verificação:** lint sem `Could not evaluate 'left_zoom2'`; jogar scene_11 até esse `show`.

---

## P1 — Arquivos de imagem ausentes (`show expression "<path>.png"`) 🔴

`show expression "<path>"` vira um `Image()` que carrega o arquivo no render. Os caminhos abaixo
**não existem em disco**:

| Caminho ausente | Locais | Ação |
|---|---|---|
| `images/items/notebook.png` | scene_1:64, scene_4:29, scene_9:32, scene_10:28, scene_13:25, scene_17:19 | Trocar por `images/items/notebook_aberto.png` (existe) — ou usar a imagem definida: `show item notebook_aberto as notebook ...` |
| `images/ui/pr_placeholder.png` | scene_18_2:17 | Criar `game/images/ui/` + asset, **ou** repontar p/ `images/artifacts/cadastro_screen.png` (existe), **ou** remover o `show`/`hide pr` |
| `images/ui/checklist_placeholder.png` | scene_18_2:55 | idem (ex.: `images/artifacts/listagem_screen.png`) |
| `images/ui/checklist_teste_seguranca.png` | scene_19:26 | idem |
| `images/ui/checklist_deploy.png` | scene_20:31 | idem |
| `images/ui/placeholder_sucesso_deploy.png` | scene_20:164 | idem |
| `images/npcs/dr_almeida.png` | scene_21:45 | **Usar a imagem já definida:** `show doutora_1 neutral at right_zoom` (igual à linha 72) |
| `images/npcs/enf_marta.png` | scene_21:46 | **Usar:** `show doutora_2 neutral at right_zoom2` (igual à linha 74) |
| `images/diagrams/*` (arquitetura/cronograma) | scene_14:96, scene_16:26 | **Verificar** existência; criar asset ou repontar/remover |

**Ações P1:**
1. Para `notebook.png`: substituir as 6 ocorrências por `images/items/notebook_aberto.png` (ou pela imagem definida `item notebook_aberto`).
2. Para `images/ui/*` e `images/npcs/*`: criar os assets reais **ou** repontar para assets existentes **ou** remover os pares `show`/`hide`. Em `scene_21`, preferir as imagens já definidas (`doutora_1/2 neutral`).
3. Confirmar `scene_14:96` e `scene_16:26` (diagramas) — corrigir do mesmo modo.
4. **Verificação:** `lint` não deve mais reportar imagens não-carregáveis; jogar `scene_1` (até o input de nome), `scene_18_2` (escolher "finalizar pela manhã"), `scene_19`, `scene_20`, `scene_21` sem placeholder/crash.

> ⚠️ `scene_1:64` está no caminho da **primeira** cena (toda playthrough). Mesmo no "caso brando",
> aparece um placeholder de erro logo no início — inaceitável para entrega.

## P2 — Atributos de sprite ausentes 🟠

`show <tag> <attr>` onde `<attr>` não foi definido nem existe como `.png`. O projeto já usa o padrão
de **alias** (ex.: `characters.rpy:74` e `:99`), então a correção é uma linha por atributo.

| Atributo ausente | Locais |
|---|---|
| `developer_ai enthusiastic` | scene_14:134, scene_15:38, scene_20:121 |
| `developer_project positive` | scene_11:52,64,67; scene_20:69,117,153 |
| `developer_quality enthusiastic` | scene_11:162,165; scene_12:165 |
| `developer_security enthusiastic` | scene_15:111; scene_19:73 |
| `developer_management positive` | scene_16:63 |
| `developer_management enthusiastic` | scene_21:131 |

**Ação P2:** em `game/scripts/characters.rpy`, adicionar aliases para atributos existentes, ex.:
```renpy
image developer_ai enthusiastic = "images/characters/developer_ai/positive.png"
image developer_management positive = "images/characters/developer_management/thinking.png"
image developer_project positive = "images/characters/developer_project/positive.png"   # ajustar p/ um asset que exista
image developer_quality enthusiastic = "images/characters/developer_quality/positive.png"
image developer_security enthusiastic = "images/characters/developer_security/positive.png"
image developer_management enthusiastic = "images/characters/developer_management/thinking.png"
```
(Conferir o nome do `.png` real de cada personagem antes de aliasar.)
**Verificação:** `lint` sem avisos `'developer_X attr' is not an image`; jogar as cenas/menus citados.

## P3 — `bg creditos` indefinido 🟠

Em `scene_epilogo_conquistas_final.rpy:89` (label `creditos_finais`), `scene bg creditos` referencia
uma imagem **nunca definida** (o `log.txt`/lint do projeto já reporta: `'bg creditos' is not an image`).
Caminho **opcional** (menu "Ver créditos finais").

**Ação P3 (escolher uma):**
- **A (mais simples):** trocar por um bg existente — `scene bg tela_conquistas`.
- **B:** adicionar `game/images/bg/creditos.png` e definir em `backgrounds.rpy`:
  `image bg creditos = im.Scale("images/bg/creditos.png", config.screen_width, config.screen_height)`.

**Verificação:** lint sem `'bg creditos' is not an image`; escolher "Ver créditos finais" no epílogo.

## P4 — Contato `doutora_2` com id errado 🔴 (funcional, garantido)

`contacts_screen.rpy:390` faz `SetVariable("amigo_selecionado", "amizade_doutora_2")` (com prefixo
`amizade_`). Em `chat_amigo`, `AMIGOS_DATA.get("amizade_doutora_2")` → `None` → cai no else que usa
`char_image = "images/characters/generic_portrait.png"` (**arquivo ausente**) e `assistant_id =
"asst_default"`. Resultado **garantido** (independe da controvérsia de crash): a Dra. Nathalia abre
com **nome "Contato", portrait quebrado, persona de IA errada e afinidade que não conta**
(`amizade_amizade_doutora_2`). No pior caso, o portrait ausente ainda pode travar a tela.

**Ações P4:**
1. **Raiz:** em `contacts_screen.rpy:390`, trocar para `"doutora_2"`:
   ```renpy
   action [SetVariable("amigo_selecionado", "doutora_2"), Hide("contacts_screen"), Jump("chat_amigo")]
   ```
2. **Defesa:** em `chat_screen.rpy:329`, repontar o fallback de portrait para um asset existente
   (ex.: `"images/characters/doutora_2/portrait.png"`) **ou** adicionar `generic_portrait.png`.
3. **Verificação:** após a `scene_6`, abrir Contatos → clicar Dra. Nathalia → deve abrir com nome/portrait
   reais, `current_assistant_id == "asst_0RVJbliiBedg7ADSndhb1BnS"` e afinidade somando.

## P5 — Replay não reseta estado → final errado 🔴 (lógica, garantido)

"Jogar novamente" (`scene_epilogo_conquistas_final.rpy:81-82`) faz `jump start`, que **não** é restart
real. Variáveis `default` (amizades, `inventario`, contatos, itens, relógio) **não** são reinicializadas.
No 2º ciclo, a condição de vitória de `scene_21:53` (`amizade_total >= 40 and "selo_codigo_sem_bugs"
in inventario and "conquista_bug_vuln" in inventario`) já está satisfeita pelos selos/afinidades do
1º ciclo → **o final "excelente" é dado independentemente das escolhas**. Barras de amizade também
estouram o range 10. *(Obs.: a linha `$ inventory = []` em `scene_1:5` reseta a variável **errada**,
em inglês; o estado real é `inventario`.)*

**Ação P5:**
- Trocar `jump start` por **restart real**: `$ renpy.full_restart()` (reaplica todos os `default` limpos — mais robusto).
- Remover a linha morta `$ inventory = []` em `scene_1`.
- **Verificação:** terminar com escolhas fracas → "Jogar novamente" → no 2º ciclo amizades/`inventario`
  começam zerados e `scene_21` **não** dá "excelente" com escolhas fracas.

## P6 — Chat: softlock por estado transitório persistido 🔴 (softlock, garantido)

`is_waiting`/`user_input`/`chat_history` são `default` (`progress.rpy`) → **salvos** no save. O envio do
chat dispara uma `threading.Thread` que faz `requests.post(timeout=60)` e, no callback, **muta o store
e chama `restart_interaction()` fora da main thread**. Se o jogador **salvar enquanto o chat está
"digitando..."** (janela de até 60s), o save grava `is_waiting=True`; ao **carregar**, o chat fica
travado em "está digitando..." para sempre e o botão "Enviar" permanece desabilitado
(`sensitive (not is_waiting ...)`) — **softlock do chat sem recuperação**. (Hazard de thread piora com Python 3.12 — ver `migracao-renpy-8.5.3.md §3`.)

**Ações P6:**
1. Trocar a thread crua por `renpy.invoke_in_thread(send_message_to_backend, user_message, process_respostas)`.
2. Fazer `process_respostas` **marshalizar** a escrita no store para a main thread (não mutar `chat_history`/`is_waiting` da worker).
3. Não persistir estado transitório: `label after_load` (e reset em `start`) forçando `is_waiting = False`, `user_input = ""`.
4. Resetar `is_waiting = False` ao fechar o chat (após o `call screen` em `chat_amigo`).
5. **Verificação:** com o backend lento/inacessível, enviar mensagem, salvar durante "digitando...", carregar → "Enviar" habilitado e sem indicador preso. Caminho feliz: resposta aparece normalmente.

---

## 7. Itens reais porém **não** quebra-jogo (corrigir como limpeza)

- **Áudio ausente (14 refs, confirmado pelo lint 8.5.3)** → soft-fail (silêncio + warning), **não trava**.
  Arquivos não carregáveis: scene_1:96 `audio/effects/computer_typing.wav` (asset é `.ogg`),
  scene_1:132 `audio/effectssend_email.ogg` (sem barra), scene_14:61/84/93 (`porta_abrindo`,
  `feedback_tech`, `feedback_curious`), scene_15:55/77 (`music_party`, `ambiente_agitado`),
  scene_17:84 (`music_focus`), scene_18:123 (`porta_abrindo`), scene_20:17/79/126/169
  (`ambiente_reuniao`, `xicara_cafe`, `cell_vibration`, `aplausos`), scene_21:29 (`onibus`).
  Ação: criar os assets ou repontar para arquivos existentes / remover os `play sound`; centralizar
  via `define audio.* = ...` em `options.rpy` para o lint pegar futuros typos.
- **`image item notebook` duplicada** (`items.rpy:60-61`) → último vence; o nome nem é usado. Limpeza apenas.

## 8. 🛡️ Rede de segurança global recomendada

Independentemente das correções pontuais, adicionar em `game/options.rpy` um fallback para imagens
ausentes degradarem de forma controlada (e nunca travarem), durante o desenvolvimento:
```renpy
init python:
    def _img_ausente(fn):
        return Text("[imagem ausente: %s]" % fn, size=20, color="#f55")
    config.missing_image_callback = _img_ausente
```
> Isto é **rede de segurança**, não substituto: o correto é corrigir/repor os assets (P1–P3).

## 9. Ordem sugerida de resolução

1. **P5**, **P6** e **P7** (bugs garantidos: lógica / softlock / NameError de transform).
2. **P4** (persona/contato errado — garantido).
3. **P1/P3** (assets ausentes nas cenas principais; usar a §8 como rede).
4. **P2** (aliases de atributos — uma linha cada).
5. §7 (limpeza de áudio/imagem duplicada).
6. Rodar `lint` + **playthrough completa** confirmando cada ponto.

> Estas correções estão refletidas no plano `docs/plans/2026-06-06-migracao-e-reestruturacao.md` (Fase 2).
