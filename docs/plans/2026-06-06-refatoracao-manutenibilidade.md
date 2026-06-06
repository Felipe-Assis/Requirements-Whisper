# Refatoração para Manutenibilidade + i18n — Plano de Implementação

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Reorganizar o projeto Ren'Py "The Requirements Whisperer" para manutenibilidade (pastas, módulos, paths de assets, deduplicação, comentários) e prepará-lo para i18n — **sem** migrar de engine e **sem** quebrar saves nem o fluxo narrativo.

**Architecture:** Jogo Ren'Py de store único e global; cenas em `call`-chain a partir de `label start`; estado em `default` globais; mecânicas (chat/contatos/inventário/relógio) hoje misturando UI + lógica + dados. O alvo separa responsabilidades em `story/ ui/ logic/ data/ python/`.

**Tech Stack:** Ren'Py **8.3.7** SDK (Python 3.9) em `C:\Program Files (x86)\renpy-8.3.7-sdk`. A migração para 8.5.3 é um trabalho **posterior** (ver `docs/plans/2026-06-06-migracao-e-reestruturacao.md`).

---

## 🔒 Regra de ouro (vale para TODAS as fases)

> **RELOCAR, nunca RENOMEAR identificadores.** Nenhuma variável `default` salva e nenhum `label`
> ganha nome novo. Só renomeie **arquivos** (os 2 typos de cena) e **literais** (wrap `_()`).
> Isso elimina ~todo o risco de compatibilidade de save.

**Por quê (modelo Ren'Py):**
- O `store` é **um namespace global** — dividir arquivos **não** cria módulos/escopo; cada `default` deve existir **uma única vez** (cuidado com colisão ao dividir).
- `label`s resolvem **globalmente** — mover `.rpy` entre pastas **não** afeta `jump/call`. **Renomear** label/variável **quebra saves** (a pilha de `call` e o `store` são serializados).
- **Paths de asset são literais** — mover um arquivo de imagem/áudio exige editar **todas** as strings que apontam pra ele (≠ mover `.rpy`, que é grátis).
- **Ordem de init:** `define` (prio 0) roda antes de `init python` de mesma prio. Tabelas que referenciam `NOME_*`/`COR_*` **devem** ficar em `init python` prio 0 (**não** `python early`). `generate_user_id` fica em `init -1` antes do `default user_id`.

## 🛑 Correções da auditoria pré-execução (varredura completa, 2026-06-06)

A varredura (validador de referências + lint-doctor + inventário + censo) confirmou a estrutura, mas exige tratar isto **antes** de mover arquivos:

1. **🔴 MAIOR RISCO — vars de jogador sem `default`:** `player_name`, `player_gender`, `player_age` são atribuídas em runtime (`scene_1_quarto.rpy:2-4`) mas **não têm `default`** e são interpoladas em ~15 cenas. **Criar `logic/state_player.rpy` com `default player_name="" / player_gender="" / player_age=""` (`init -1`) ANTES de qualquer split.** Regra estendida: *todo store var salvo tem exatamente um `default`* (sem isto, save/rollback pode dar NameError em `[player_name]`).
2. **Órfão `inventory`:** `scene_1_quarto.rpy:5 $ inventory = []` é atribuição **morta** (o real é `inventario`; `inventory_enabled` é um 3º var legítimo — **não tocar**). Apagar **só** a linha 5.
3. **Descrições com `\` + n literal:** os tiles `developer_coding` e `developer_requirements` usam barra-invertida-n literal (bug); os outros 8 usam quebra real. **Não** copiar esses 2 protótipos no loop — normalizar todos para quebra de linha real.
4. **`add_contact` p/ developers é "dead path":** só é chamado em `scene_2_escritorio` (comentada fora do call-chain) e na scene_6 (doutoras). Verificar como os `contato_developer_*` viram `True` no fluxo ativo (gap de gameplay pré-existente) antes de assumir que a grade popula.
5. **Antes do split (verificação):** após dividir `characters.rpy`, confirmar que `NOME_*/COR_*` continuam `define`, tabelas em `init python` (não `python early`), o bloco `default` em `init -1`, e **nenhum `default` declarado 2x** (lint + grep).

## ⚠️ Verificação (não há suíte de testes)

Em cada tarefa o "teste" é:
1. **Lint:** `& "C:\Program Files (x86)\renpy-8.3.7-sdk\renpy.exe" "c:\Users\Felipe\Documents\GitHub\Renpy Projects\Requirements-Whisper" lint` → sem erros novos vs. baseline.
2. **Playthrough dirigida** do trecho afetado.

(`SDK = "C:\Program Files (x86)\renpy-8.3.7-sdk\renpy.exe"`, `PROJ = "c:\Users\Felipe\Documents\GitHub\Renpy Projects\Requirements-Whisper"`.)

## 🔁 Mudanças de comportamento INTENCIONAIS (decidir com o autor antes de mergear)
1. **doutora_2** passa a abrir o assistente real (corrige `amizade_doutora_2` → `doutora_2`).
2. As **3 normalizações** de resposta do chat viram **uma**.
3. **Incremento/clamp de amizade** unificado (decidir 0.5 vs 1 e o cap 0..10; `amizade_*` são floats salvos).

## Estrutura-alvo (target tree)

```
game/
  script.rpy, options.rpy, gui.rpy, screens.rpy   # entry da engine — NÃO mover
  story/                  # narrativa; 1 .rpy por cena (labels globais)
    act1_descoberta/ act2_levantamento/ act3_especificacao/
    act4_arquitetura/ act5_implementacao/ epilogue/
  ui/                     # screens + styles/transforms de apresentação
    chat_screen.rpy contacts_screen.rpy inventory_screen.rpy clock_screen.rpy
    styles/  (chat_styles.rpy, sprite_transforms.rpy)
  logic/                  # estado (default) + mutadores no store, sem UI
    state_time.rpy state_flags.rpy state_progress.rpy friendship.rpy inventory.rpy
  data/                   # tabelas declarativas (init python prio 0 / define)
    characters.rpy character_names.rpy friends_data.rpy
    backgrounds.rpy items.rpy audio_library.rpy
  python/                 # python puro / backend
    chat_backend.rpy user_id.rpy   (+ game/python/*.py se usar import)
  images/  bg/ characters/ items/ artifacts/ ui/ diagrams/ npcs/   # (3 últimas: criar)
  audio/   music/ effects/
  gui/                    # skin Ren'Py — NÃO mover
```
> Subpastas por ato são opcionais (um `story/` plano já entrega a navegabilidade). Mantê-las é seguro (labels globais).

---

## Fase 0 — Baseline + correções baratas (save-safe, sem mover estrutura)

### Task 0.1: Baseline verde
**Files:** git + lint
- [ ] **Step 1:** `git -C $PROJ checkout -b refatoracao`
- [ ] **Step 2:** Rodar o lint e salvar a saída como referência (já conhecemos os avisos atuais: atributos `developer_* enthusiastic/positive`, `bg creditos`, `left_zoom2`, áudios faltando — ver `docs/pontos-criticos.md`).
- [ ] **Step 3:** Commit do baseline.

### Task 0.2: Correções pontuais (cruzam com pontos-críticos)
**Files:** `mechanics/contacts_screen.rpy`, `mechanics/chat_screen.rpy`, `scripts/items.rpy`, `scripts/scene_11_almoco_equipe.rpy`, renomear 2 arquivos, remover `functions.rpy`
- [ ] **Step 1 (P4):** `contacts_screen.rpy:390` → `SetVariable("amigo_selecionado", "doutora_2")`.
- [ ] **Step 2:** `chat_screen.rpy` — apagar blocos de style duplicados em **271-280** (`chat_log_viewport` definido em 271-273 **e** 276-278; `style chat_send_button is default` em 275 **e** 280). Manter 1 de cada antes do corpo real de `chat_send_button` (281-288).
- [ ] **Step 3:** `items.rpy:60-61` — remover a definição duplicada de `image item notebook` (manter o zoom intencional) e alinhar idle/hover.
- [ ] **Step 4 (P7):** `scene_11_almoco_equipe.rpy:127` → `at left_zoom_2`.
- [ ] **Step 5:** Renomear **arquivos** (labels intactos): `scene_15_aniversario_supresa.rpy`→`...surpresa.rpy`; `scene_18_2_codificacaso_final.rpy`→`...codificacao_final.rpy` (use `git mv`).
- [ ] **Step 6:** Remover `scripts/functions.rpy` (vazio).
- [ ] **Step 7 (verificação):** lint sem `left_zoom2`/duplicados; abrir Contatos→doutora_2; jogar scene_11 e scene_1.
- [ ] **Step 8:** Commit `chore: cheap correctness fixes + file-name typos (save-safe)`.

---

## Fase 1 — Mover `.rpy` para a nova árvore (sem renomear, sem mudar lógica)

### Task 1.1: Mover cenas para `story/actN/`
**Files:** `git mv` de `scripts/scene_*.rpy` → `story/actN_*/`
- [ ] **Step 1:** Criar `game/story/{act1_descoberta,act2_levantamento,act3_especificacao,act4_arquitetura,act5_implementacao,epilogue}/`.
- [ ] **Step 2:** `git mv` cada cena para o ato (mapa no target tree). **Não** alterar labels.
- [ ] **Step 3 (verificação):** lint (alvos de `call`/`jump` resolvem) + abrir o jogo e avançar 3-4 cenas.
- [ ] **Step 4:** Commit `refactor: group scenes into story/act folders (labels unchanged)`.

### Task 1.2: Mover estado/lógica para `logic/` e dados para `data/`
**Files:** `git mv`/split de `scripts/variables/*`, `characters.rpy`, `backgrounds.rpy`, `items.rpy`, `music.rpy`; **novo** `logic/state_player.rpy`
- [ ] **Step 0 (🔴 fazer primeiro):** Criar `logic/state_player.rpy` com `default player_name = ""`, `default player_gender = ""`, `default player_age = ""` em `init -1` (hoje não têm `default` e são usados em ~15 cenas). Opcional: remover as atribuições `= ""` no topo de `scene_1_quarto.rpy:2-4` (ou mantê-las e documentar).
- [ ] **Step 1:** `variables/variables.rpy` → dividir em `logic/state_time.rpy` (relógio + `set_time`/`advance_minutes`, **des-aninhar** de `init -1:`) e `logic/state_flags.rpy` (`item_*`/`contato_*`/`disponivel_*`). Preservar a prioridade `init -1` do bloco de `default`.
- [ ] **Step 2:** `variables/progress.rpy` → `logic/state_progress.rpy`; `variables/amizade.rpy` → `logic/friendship.rpy`.
- [ ] **Step 3:** `characters.rpy` → `data/characters.rpy` (Character()+image maps), `data/character_names.rpy` (`NOME_*`/`COR_*` defines), `ui/styles/sprite_transforms.rpy` (transforms). **Sem renomear** `developer_*`, `NOME_*`, transforms.
- [ ] **Step 4:** `backgrounds.rpy`/`items.rpy` → `data/`; `music.rpy` → `data/audio_library.rpy`.
- [ ] **Step 5 (verificação):** lint; abrir o jogo, ver sprites/bg/itens/relógio normais. Confirmar que **cada `default` existe uma única vez** (sem colisão).
- [ ] **Step 6:** Commit `refactor: relocate state to logic/ and content to data/ (no renames)`.

---

## Fase 2 — Reorg de assets + correção de paths (atômico por grupo de asset)

> Cruza com `docs/pontos-criticos.md` P1 e a §7 (áudio). Cada movimento de asset = editar as strings em lockstep.

### Task 2.1: Música para `audio/music/`
- [ ] **Step 1:** Mover os 11 `.mp3` soltos de `game/audio/` para `game/audio/music/` e atualizar **os 11 valores** `define music_* = "audio/..."` em `data/audio_library.rpy` (cenas referenciam o NOME do define, então não mudam).
- [ ] **Step 2 (verificação):** lint sem áudio não-carregável de música; jogar cenas com música.
- [ ] **Step 3:** Commit `refactor: move music to audio/music/ and update defines`.

### Task 2.2: Corrigir paths de áudio quebrados (pré-existentes)
- [ ] **Step 1:** Corrigir os caminhos listados em `pontos-criticos.md §7` (ex.: `audio/effectssend_email.ogg`→`audio/effects/<arquivo>.ogg`; `computer_typing.wav`→`.ogg`; scene_20 sem `effects/`; scene_14 `porta_abrindo`; scene_21 `onibus`). Onde o asset não existe, repontar para um existente ou remover o `play sound`.
- [ ] **Step 2 (verificação):** lint sem `'audio/...' is not loadable`.
- [ ] **Step 3:** Commit `fix: broken audio paths (lint clean)`.

### Task 2.3: Imagens ausentes + migrar `show expression` para imagens definidas
- [ ] **Step 1:** Criar `images/ui/`, `images/diagrams/`, `images/npcs/` e adicionar os assets ausentes (ou remover/repontar — ver `pontos-criticos.md` P1). `bg creditos` (P3) e `generic_portrait` (P4) inclusos.
- [ ] **Step 2:** Migrar `show expression "images/items/notebook.png"` (6 cenas: scene_1:64, scene_4:29, scene_9:32, scene_10:28, scene_13:25, scene_17:19) para a imagem **definida** `show item notebook_fechado ...` (notebook_fechado = fechado, que é o sentido do path ausente; `notebook_aberto` é o ABERTO). Em `scene_21:45-46`, trocar `show expression "images/npcs/dr_almeida.png"`/`enf_marta.png` pelos sprites definidos `show doutora_1 portrait` / `show doutora_2 portrait` (em vez de criar `npcs/`).
- [ ] **Step 3 (rede de segurança):** `options.rpy` → `config.missing_image_callback` (ver `pontos-criticos.md §8`).
- [ ] **Step 4 (verificação):** lint sem imagem não-carregável; jogar scene_1/18_2/19/20/21 e os créditos.
- [ ] **Step 5:** Commit `fix: missing image assets + migrate show-expression to defined images`.

---

## Fase 3 — Extração de helpers/módulos (puro → python; glue fica .rpy)

### Task 3.1: Cliente de chat puro + glue
**Files:** `data/friends_data.rpy`, `python/chat_backend.rpy`, `ui/chat_screen.rpy`, `python/user_id.rpy`
- [ ] **Step 1:** Mover `AMIGOS_DATA` para `data/friends_data.rpy` em **`init python` prio 0** (referencia `NOME_*`). **Preservar** o bootstrap `if not hasattr(renpy.store,"current_assistant_id")` — **não** virar `default`.
- [ ] **Step 2:** Mover o cliente HTTP (`is_web`, `normalize_resposta`, envio desktop com `requests`/threading, branch web/emscripten) para `python/chat_backend.rpy` (`init python`). Passar `url`/`user_id`/`assistant_id` por **parâmetro** (não ler `store` no corpo puro).
- [ ] **Step 3 (dedup):** unificar as **3 normalizações** num único `normalize_resposta(raw) -> list[str]`, usado por desktop e web; `process_respostas` passa a só iterar (sem 2º `ast`). *(mudança intencional nº2)*
- [ ] **Step 4:** `define config.chat_backend_url = "http://15.229.14.83:8000"` (um lugar; ambos os transportes usam).
- [ ] **Step 5:** `chat_screen.rpy` fica **só UI** (`screen chat_with_backend` + `label chat_amigo`); styles em `ui/styles/chat_styles.rpy`. Mover `generate_user_id`+`default user_id` para `python/user_id.rpy` mantendo `init -1`.
- [ ] **Step 6 (verificação):** lint; enviar mensagens no chat (desktop); confirmar a mensagem "indisponível na web" no branch web. Trocar `except:` nus por `except (ValueError, SyntaxError):`/`KeyError`.
- [ ] **Step 7:** Commit `refactor: extract chat backend + unify response normalizer`.

### Task 3.2: Helpers de amizade/contatos/inventário em `logic/`
**Files:** `logic/friendship.rpy`, `logic/inventory.rpy`
- [ ] **Step 1:** Mover `add_contact`/`add_friendship_point`/`get_friendship_point` (de `contacts_screen.rpy`) para `logic/friendship.rpy`; `add_to_inventory` (de `inventory_screen.rpy`) para `logic/inventory.rpy`. Trocar `renpy.store.__dict__[...]` por `getattr/setattr(store, ...)`.
- [ ] **Step 2 (dedup):** `def friendship_color(level)` (escada única 10/8/5/3/else, usar `>=`). `def friendly_name(id)` (AMIGOS_DATA ou title-case).
- [ ] **Step 3 (mudança intencional nº3):** Estado atual (registrar antes de mudar): `add_friendship_point` (contacts_screen.rpy:451) hoje usa `amount=0.5` e **NÃO tem clamp**; o único clamp `min(...+1, 10)` está **inline** em `chat_amigo` (chat_screen.rpy:323, que ainda cria `amizade_*` via `store.__dict__`). Unificar em `add_friendship_point(id, amount=...)` com clamp 0..10 e chamar de `chat_amigo` via `$ add_friendship_point(amigo_selecionado)`. ⚠️ Isso **muda comportamento em duas direções** (adiciona cap no caminho da UI, onde hoje pode passar de 10; e troca o `+1` do chat). Decidir `amount` (0.5 vs 1) com o autor.
- [ ] **Step 4 (verificação):** lint; ganhar amizade via chat e via UI; coletar item; abrir Mochila/Contatos.
- [ ] **Step 5:** Commit `refactor: consolidate gameplay helpers in logic/`.

---

## Fase 4 — UI data-driven (maior remoção de duplicação)

### Task 4.1: Contatos data-driven
**Files:** `data/friends_data.rpy` (estender com `desc`/`order`), `ui/contacts_screen.rpy`
- [ ] **Step 1:** Garantir em `friends_data.rpy`: `CONTACTS[cid] = {name, portrait, assistant_id, desc}` e a ordem explícita `CONTACTS_ORDER = ["developer_ai","developer_requirements","developer_coding","developer_management","developer_quality","developer_project","developer_security","developer_test","doutora_1","doutora_2"]`.
- [ ] **Step 2:** Criar `screen contact_tile(cid)` que **substitui os 10 tiles atuais (linhas 38-414**, não só o developer_ai 38-73): ler `getattr(store,"contato_"+cid)`, `"disponivel_"+cid`, `"amizade_"+cid`; imagem `"%s portrait" % cid`; `left_bar Solid(friendship_color(amizade))`; `action [SetVariable("amigo_selecionado", cid), Hide("contacts_screen"), Jump("chat_amigo")]`. O loop deve cobrir os 10 ids (incluindo `doutora_1`/`doutora_2`, cujas descrições diferem).
- [ ] **Step 3:** `contacts_screen` vira `for cid in CONTACTS_ORDER: use contact_tile(cid)`. Usar `\n` real (não `\\n`).
- [ ] **Step 4:** `default contacts = set()` em `logic/state_flags.rpy` (em vez de criação preguiçosa) **e remover** o init preguiçoso `if not hasattr(store,'contacts')` em `add_contact` (evita inicialização divergente).
- [ ] **Step 5 (verificação):** lint; abrir Contatos — 10 contatos na ordem certa, disponíveis/cinza corretos, cada um abre o chat certo (especialmente doutora_2). Conferir barras reativas.
- [ ] **Step 6:** Commit `refactor: data-driven contacts screen (10x tile -> 1 loop)`.

### Task 4.2: `set_available()` nas cenas
**Files:** `logic/state_flags.rpy`, ~16 cenas
- [ ] **Step 1:** `def set_available(*ids)` que zera todos `disponivel_developer_*` e liga os passados (suporte a `"all"`), sobre a lista `DEVELOPERS`. ⚠️ **Tratar também** `disponivel_doutora_1`/`disponivel_doutora_2` (default `True`, ao contrário dos developers que são `False`) — estender a lista iterada **ou** manter `scene_21:10-11` verbatim ao lado do helper.
- [ ] **Step 2:** Substituir o bloco de 8 linhas no topo de **16 cenas** por `$ set_available('developer_x', ...)` — **conferindo contra o bloco original de cada cena**. ⚠️ Há também blocos **no meio da cena** (não no topo): `scene_17:136-143`, `scene_18:162-169`, `scene_18_2:145-152` — converter esses também. E **scene_5:3-10 / scene_7:2-9 estão parcialmente comentados** (só 1-2 flags ativas) → **decisão do autor** antes de substituir (não é passe mecânico). *Não-mecânico: este passo precisa de julgamento, não roda só por agente.*
- [ ] **Step 3 (verificação):** lint; em cada cena alterada, abrir Contatos e conferir quem está disponível bate com o original.
- [ ] **Step 4:** Commit `refactor: scene availability via set_available() helper`.

### Task 4.3 (opcional): Inventário data-driven + loop de imagens de item
- [ ] **Step 1:** `screen inventory_tile(item_id)` + tabela `ITENS = {id:{desc, action}}`; `define_item_images(name)` num loop `init python` com `renpy.image(...)`.
- [ ] **Step 2 (verificação):** lint; abrir Mochila, hover/uso de cada item.
- [ ] **Step 3:** Commit `refactor: data-driven inventory tiles + item image loop`.

---

## Fase 5 — i18n: wrap `_()` + geração de traduções

> Fazer **junto** das tabelas da Fase 4 evita tocar as mesmas linhas 2x. Tudo aqui é **save-safe** (só envolve literais).

### Task 5.1: Wrap de strings de UI/Python em `_()`
**Files:** `ui/*screen*.rpy`, `data/character_names.rpy`, `scene_1_quarto.rpy`
- [ ] **Step 1:** Envolver `text`/`textbutton` literais: chat (`Bate-papo`, `[char_name] está digitando...`, `Enviar`, `Fechar`, msg web), contatos (`Contatos`, `Fechar`), inventário (`Mochila`, `Fechar`). Ex.: `text _("Bate-papo")`.
- [ ] **Step 2:** `NOME_*` defines e `'Colega de República'` → `_("...")` (avaliam no init; save-safe).
- [ ] **Step 3:** Descrições (10 contatos + 5 itens) → mover para as tabelas de dados com `_(...)` e interpolação `[name]` do Ren'Py (não `%`/f-string).
- [ ] **Step 4:** `renpy.notify`/`renpy.input` — **de-f-string**: `renpy.notify(_("Contato adicionado: [name]").format(name=nome))`; `renpy.input(_("Nome completo:"))` etc. Wrap fallbacks `'Nenhuma resposta recebida.'`, `'Erro ao enviar mensagem: ...'`, `'Contato'`.
- [ ] **Step 5 (verificação):** lint; jogo continua em pt-BR idêntico.
- [ ] **Step 6:** Commit `i18n: wrap UI/python strings in _() (save-safe)`.

### Task 5.2: Gerar locale + seletor de idioma
**Files:** `game/tl/english/` (gerado), `screens.rpy` (preferences), `options.rpy`
- [ ] **Step 1:** `& $SDK $PROJ translate english` → cria `game/tl/english/` (diálogos/menus auto + strings `_()`). Re-rodar após cada lote de `_()`.
- [ ] **Step 2:** Em `screens.rpy` (preferences), adicionar seletor: `textbutton _("Português") action Language(None)` / `textbutton _("English") action Language("english")`. Opcional: `persistent.lang`.
- [ ] **Step 3:** Preencher `tl/english/*.rpy` (`new "..."`), mantendo `[var]`/`{tags}` idênticos.
- [ ] **Step 4 (verificação):** lint; trocar idioma em Preferences e percorrer scene_1 + Mochila/Contatos/Chat; confirmar pt-BR baseline intacto.
- [ ] **Step 5:** Commit `i18n: generate english locale + language selector`.

### Task 5.3: Fontes/glyphs + chat remoto
- [ ] **Step 1:** Resolver o `💗` (DejaVuSans não tem emoji): trocar por uma imagem de coração (`add`) ou bundle de fonte emoji. (Acentos pt/en já OK.)
- [ ] **Step 2 (fora do tl estático, planejar):** localizar o chat = mudar o **backend** (campo `language` no POST **ou** `assistant_id` por idioma em `CONTACTS`). Ren'Py não traduz texto remoto.
- [ ] **Step 3:** Commit `i18n: heart glyph fix + document remote-chat localization`.

---

## Fase 6 — Comentários / convenções / limpeza

### Task 6.1: Comentários e convenções
- [ ] **Step 1:** Cabeçalho por cena (`# Propósito / Hora / Flags que seta / Próxima`) e docstrings de módulo (contrato do `AMIGOS_DATA`/`CONTACTS`, notas de ordem de init).
- [ ] **Step 2:** `# alias` nos reusos intencionais de imagem de emoção (ex.: `coding positive = neutral`) para ninguém "consertar".
- [ ] **Step 3:** Documentar em `CLAUDE.md` a convenção pt/en e o aviso "estes `default` são salvos — não renomear".
- [ ] **Step 4:** Triagem de inventário (3 nomes parecidos): apagar **só** `scene_1_quarto.rpy:5 $ inventory = []` (atribuição runtime morta), manter `inventario` (`progress.rpy:5`, o estado real lido em scene_21) e **não tocar** em `inventory_enabled` (`variables.rpy:2`, flag legítima). Confirmar via `grep` que `inventory` (singular) não é lido antes de apagar.
- [ ] **Step 5 (verificação):** lint final + playthrough completa.
- [ ] **Step 6:** Commit `docs: scene headers, module docstrings, conventions`.

---

## ⛔ Fora de escopo (over-engineering — não fazer)
- `clock.py` como módulo puro (3 linhas de aritmética) — só des-aninhar `set_time`/`advance_minutes`.
- `asset_helpers.py` separado — usar loop `init python` com `renpy.image()`.
- Mutador genérico `_set_store_flag` unificando os 3 `add_*` (corpos legitimamente diferentes) — compartilhar só `friendly_name()`.
- Registry de SFX elaborado antecipado — centralizar `sfx_*` só quando migrar os `play sound` inline.
- Subpastas por ato são opcionais (um `story/` plano basta).

## Self-review (cobertura do spec)
- Reorganizar pastas → Fases 1 e estrutura-alvo ✅
- Importações/módulos → Fase 3 (python/chat_backend, glue .rpy) ✅
- Paths de assets → Fase 2 ✅
- Quebrar arquivos grandes → Fases 1/3/4 (chat 5-way, contacts, characters 4-way) ✅
- Reúso de código → Fase 4 (contact_tile, friendship_color, set_available, normalize_resposta) ✅
- Comentários/boas práticas → Fases 3/6 ✅
- Preparar i18n → Fase 5 ✅
- Restrições Ren'Py (save/label/init/asset) → "Regra de ouro" + verificações por fase ✅
- Migração 8.5.3 → **fora deste plano** (posterior) ✅

## Mapa de agentes por fase (do audit)

| Fase / tarefa | Agente | Obs. |
|---|---|---|
| Baseline + lint + verificação em TODO checkpoint | `renpy-lint-doctor` + `renpy-reference-validator` | validator pega o que o lint não vê (show-expression, ids) |
| 0.2 fix doutora_2 | `chat-backend-agent` | contrato AMIGOS_DATA/amigo_selecionado |
| 0.2 styles dup / notebook dup / left_zoom2 / rm functions | `renpy-lint-doctor` / `refactor-restructure-agent` | triviais lint-surfaced |
| 0.2 renomear 2 arquivos | `refactor-restructure-agent` | só `git mv` |
| Fase 1 (mover/split + `state_player`) | `refactor-restructure-agent` | regra de ouro; preservar `init -1` |
| 2.1/2.2 áudio (paths) | `scene-author-agent` (edita) + `renpy-reference-validator` (valida) | |
| 2.3 assets/bg creditos/show-expr/callback | ⚠️ **misto** | cenas→`scene-author-agent`; backgrounds/options→`refactor-restructure-agent`; PNGs reais→humano/pipeline |
| 3.1 chat backend + normalizador | `chat-backend-agent` | |
| 3.2 helpers/clamp amizade | `refactor-restructure-agent` | clamp = decisão do autor |
| 4.1/4.3 UI data-driven | `screen-ui-agent` | coordena shape de CONTACTS c/ chat-backend |
| 4.2 `set_available` | ⚠️ **não-mecânico** | helper→`refactor`; cenas→`scene-author`; doutoras/mid-scene/comentadas = autor |
| Fase 5 i18n | `i18n-tl-agent` | coordena c/ screen-ui e scene-author |
| Fase 6 comentários/limpeza | `refactor-restructure-agent` | triagem `inventory` com cuidado |

## Handoff de execução
Plano salvo. Duas opções:
1. **Subagent-Driven (recomendado)** — um subagente por tarefa, com review entre tarefas.
2. **Inline** — executar nesta sessão com checkpoints.

> Pré-requisito real: as verificações exigem o **SDK 8.3.7** e **rodar/jogar** o jogo localmente (manual; não automatizável por agente). Ideal: você roda lint/playthrough nos checkpoints.
