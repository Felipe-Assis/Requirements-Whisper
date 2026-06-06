# Migração Ren'Py 8.3.7 → 8.5.3 — Plano de Implementação

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) ou superpowers:executing-plans. Steps usam checkbox (`- [ ]`). Agente dono: `renpy-migration-853-agent`; verificação: `renpy-lint-doctor`.

> **Revisado em 2026-06-06**, APÓS a refatoração (branch `refatoracao`). A versão estável mais recente do Ren'Py é **8.5.3** ("We Can Go to the Moon", 15/05/2026 — confirmado). Toda a antiga Fase 2 (bugs) e Fase 3 (reestruturação) **já foram concluídas na refatoração** — ver §"Já concluído". O que resta é **migração de engine pura** (comportamental/runtime), não sintática.

**Goal:** Migrar o "The Requirements Whisperer" já-refatorado de Ren'Py 8.3.7 → 8.5.3 **preservando todo o comportamento e sem quebrar nada** (saves, fluxo, chat, render).

**Architecture (pós-refatoração):** store único; cenas em `game/story/actN_*/`; estado em `game/logic/`; dados em `game/data/`; UI em `game/scripts/mechanics/` + `game/ui/styles/`; backend do chat em `game/python/chat_backend.rpy`.

**Tech Stack:** Ren'Py 8.5.3 SDK (**Python 3.12**, com `requests` empacotado), backend HTTP externo, Windows 11.

**Pré-requisito:** este plano parte do código refatorado (branch `refatoracao`). Faça a migração **sobre** essa branch (ou após mergeá-la na `main`).

---

## ✅ Já concluído na refatoração (NÃO refazer)

Riscado do plano antigo — feito na branch `refatoracao`:
- Imagens/atributos ausentes (P1/P2), `left_zoom2`→`left_zoom_2` (P7), `bg creditos` (P3), fallback de portrait (P7), `doutora_2` id (P4), paths de áudio + imagem duplicada, órfão `inventory` (P5-parcial), `missing_image_callback`.
- Reestruturação: cenas→`story/actN_*/`, estado→`logic/`, dados→`data/`, contatos/inventário data-driven, `BACKEND_BASE_URL`, helpers em `logic/`, `set_available()`, normalizador unificado.
- **Lint do código refatorado (8.3.7): 100% limpo** (0 erros, 0 avisos de imagem/áudio) — só resta o *notice* `im.Scale` obsoleto (tratado opcionalmente abaixo).

## ⚠️ Verificação (sem suíte de testes)
Cada tarefa: **(1) lint 8.5.3 sem erros novos** + **(2) playthrough dirigida**.
- Lint via python embutido (o `renpy.exe` no Windows não devolve saída ao console):
  `& "C:\Program Files (x86)\renpy-8.5.3-sdk\lib\py3-windows-x86_64\python.exe" "C:\Program Files (x86)\renpy-8.5.3-sdk\renpy.py" "<PROJ>" lint`
- Abrev.: `SDK85 = C:\Program Files (x86)\renpy-8.5.3-sdk`, `PROJ = c:\Users\Felipe\Documents\GitHub\Renpy Projects\Requirements-Whisper`.

## 🔑 Descoberta-chave: `config.version` e os shims de compat
`game/options.rpy:26` tem `define config.version = "1.0"`. O layer de compat do Ren'Py (`renpy/common/00compat.rpy`) faz parse de `config.version` em tupla e aplica shims por versão. `"1.0"` → `(1,0)` ≤ `(8,3,99)`, então **os shims antigos se aplicam por acidente** (`old_show_expression=True`, `zoom_zaxis=False`, etc.). **Não confie nisso.** Em 8.5.3 vários defaults mudaram (`config.zoom_zaxis=True`, `automatic_oversampling=4`, `mipmap=True`). A ação correta e transparente é **setar as flags relevantes explicitamente** (Task 5) — assim o comportamento independe do parse de `config.version`.

---

## Fase 0 — Branch e baseline

### Task 0: Branch de migração + baseline
- [ ] **Step 1:** A partir do código refatorado: `git -C "<PROJ>" checkout -b migracao-8.5.3` (a partir de `refatoracao` ou da `main` já com a refatoração).
- [ ] **Step 2 (baseline):** lint no **8.3.7** (deve sair limpo — já validado: 0 erros/avisos, só o notice `im.Scale`). Guardar para comparação.
- [ ] **Step 3:** commit do ponto de partida, se houver pendências.

---

## Fase 1 — Migração para 8.5.3

### Task 1: Instalar SDK 8.5.3, recompilar sob Python 3.12 (P0, mecânico)
**Files:** `game/cache/`, `*.rpyc/*.rpymc/*.rpyb` (apagar — todos gitignored, nada a commitar)
- [ ] **Step 1:** SDK 8.5.3 já instalado em `C:\Program Files (x86)\renpy-8.5.3-sdk` (manter o 8.3.7 p/ rollback).
- [ ] **Step 2:** Purgar bytecode do Python 3.9:
  ```powershell
  Remove-Item -Recurse -Force "<PROJ>\game\cache" -ErrorAction SilentlyContinue
  Get-ChildItem "<PROJ>\game" -Recurse -Include *.rpyc,*.rpymc,*.rpyb | Remove-Item -Force
  ```
- [ ] **Step 3:** Abrir o projeto no launcher **8.5.3** → **Force Recompile**.
- [ ] **Step 4 (verificação):** lint no 8.5.3 → nenhum erro novo vs. baseline.
- [ ] **Step 5 (verificação):** confirmar `requests` (já empacotado em `…\renpy-8.5.3-sdk\lib\python3.12\requests`): no console (Shift+O) `import requests` sem `ImportError`.
- [ ] **Step 6:** Commit `Recompile under Ren'Py 8.5.3 (Python 3.12)`.

> Auditoria 3.12: o Python refatorado (`chat_backend.rpy`, `logic/*`, `user_id.rpy`) usa só APIs estáveis 3.9→3.12 — nada a mudar pela versão do Python em si.

### Task 2: 🔴 Corrigir threading do chat (softlock + mutação de store fora da main thread) — P0
**Files:** Modify `game/python/chat_backend.rpy` (`send_and_update_chat`/`process_respostas`, ~linhas 105-132); `game/scripts/mechanics/chat_screen.rpy` (`screen chat_with_backend`); `game/logic/state_progress.rpy` (novo default)

Problemas: (a) `process_respostas` muta `chat_history`/`is_waiting` e chama `restart_interaction()` **dentro da thread** (inseguro no 8.5); (b) `is_waiting`/`chat_history` são `default` (`state_progress.rpy:8-10`) → **salvar durante "está digitando…"** persiste `is_waiting=True` → ao carregar, "Enviar"/Enter ficam desabilitados (`chat_screen.rpy:54,58`) = **softlock**.

- [ ] **Step 1:** Em `state_progress.rpy`, adicionar `default pending_response = None` (buffer transitório).
- [ ] **Step 2:** Em `chat_backend.rpy`, a thread de fundo deve **apenas** computar a resposta e escrever no buffer — **sem** tocar `chat_history`/`is_waiting`/`restart_interaction`:
  ```python
  def process_respostas(respostas):
      # roda na thread: só publica no buffer; a main thread drena (ver chat_screen)
      store.pending_response = respostas if respostas else []
      renpy.restart_interaction()   # acorda a tela; o timer drena na main thread
  ```
  (Manter o `threading.Thread(...).start()` no caminho desktop e o branch web como estão.)
- [ ] **Step 3:** Em `screen chat_with_backend` (chat_screen.rpy), adicionar um dreno na **main thread**:
  ```renpy
  timer 0.1 repeat True action Function(drain_pending_response)
  ```
  e em `init python` (chat_backend.rpy ou logic):
  ```python
  def drain_pending_response():
      if store.pending_response is not None:
          for r in store.pending_response:
              chat_history.append(("assistant", r))
          if not store.pending_response:
              chat_history.append(("assistant", _("Nenhuma resposta recebida.")))
          store.pending_response = None
          store.is_waiting = False
          renpy.restart_interaction()
  ```
- [ ] **Step 4 (reset obrigatório):** garantir que estado transitório nunca sobreviva a save/rollback:
  ```python
  init python:
      def __reset_chat_transient():
          store.is_waiting = False
          store.user_input = ""
          store.server_response = ""
          store.pending_response = None
      config.after_load_callbacks = config.after_load_callbacks + [__reset_chat_transient]
  ```
- [ ] **Step 5 (verificação):** playthrough — abrir telefone → conversar (resposta chega); **salvar durante "digitando…"** → carregar → input utilizável (`is_waiting=False`); fechar o chat no meio e reabrir sem indicador preso; com a rede off, degrada com mensagem de erro (não trava). Lint limpo.
- [ ] **Step 6:** Commit `Fix chat threading: marshal store updates to main thread; reset transient state on load`.

> Alternativa mais enxuta: `renpy.invoke_in_thread(...)` + dreno na main thread. O padrão buffer+timer acima é o mais robusto. (Decidir com o autor; é mudança comportamental → playtest.)

### Task 3: `is_web()` → API suportada
**Files:** Modify `game/python/chat_backend.rpy:25-30`
- [ ] **Step 1:** Trocar o `try: import emscripten` por:
  ```python
  def is_web():
      return renpy.variant("web")
  ```
- [ ] **Step 2 (verificação):** desktop continua no caminho desktop (variant web = False); se houver build web, mostra o aviso "baixe o jogo". Lint limpo.
- [ ] **Step 3:** Commit `Use renpy.variant('web') for web detection`.

### Task 4: Replay limpo (`full_restart`) — P5
**Files:** Modify `game/story/epilogue/scene_epilogo_conquistas_final.rpy:82`
- [ ] **Step 1:** Trocar `jump start` por restart real (re-inicializa todos os `default`):
  ```renpy
          "Jogar novamente (novo ciclo, novos desafios)":
              $ renpy.full_restart()
  ```
- [ ] **Step 2 (verificação):** jogar até o epílogo → "Jogar novamente" → iniciar novo jogo → contatos travados de novo, amizades zeradas, `inventario` vazio, relógio resetado. Lint limpo.
- [ ] **Step 3:** Commit `Use renpy.full_restart() for replay (clean default reset)`.

> O reset de estado transitório do chat já vem da Task 2 (after_load). O bloco de conquistas comentado no epílogo (linhas 7-68) não tem impacto — deixar como está.

### Task 5: Render/config explícitos (zoom z-axis, show expression, version) — P1
**Files:** Modify `game/options.rpy`
- [ ] **Step 1:** Setar as flags explicitamente (não depender do parse de `config.version`):
  ```renpy
  define config.zoom_zaxis = False        # preserva o framing 2D dos transforms *_zoom (8.5 default = True)
  define config.old_show_expression = True # preserva o show expression legado usado nas cenas
  ```
- [ ] **Step 2:** Definir um `config.version` numérico real (ex.: `"1.1"`) — apenas higiene; o comportamento agora vem das flags acima.
- [ ] **Step 3 (verificação):** validar enquadramento dos sprites com `*_zoom` (`ui/styles/sprite_transforms.rpy`: `sprite_zoom`, `left_zoom`, `left_zoom_2`, `center_zoom`, `right_zoom`, `right_zoom2`) e o portrait do chat (`chat_screen.rpy` `zoom 0.18`) — devem casar com o 8.3.7. Conferir scene_1 (pop-ups de item), scene_11/18/20. Confirmar que os `show expression` de item ainda aparecem.
- [ ] **Step 4:** Commit `Set zoom_zaxis/old_show_expression explicitly for 8.5; bump config.version`.

### Task 6 (opcional, follow-up): `im.Scale` → escala nativa
**Files:** `game/data/backgrounds.rpy` (22× `im.Scale`)
- [ ] **Step 1:** **Não bloqueante** — `im.Scale` funciona no 8.5.3. Se, após validar, os backgrounds ficarem suaves/borrados (8.5 liga `mipmap`/`automatic_oversampling`), migrar `image bg x = im.Scale("images/bg/x.png", w, h)` → `image bg x = "images/bg/x.png"` (deixa a engine escalar com oversampling), ou `define config.mipmap = True`.
- [ ] **Step 2 (verificação):** comparar nitidez dos backgrounds em tela cheia/high-DPI vs. 8.3.7.
- [ ] **Step 3:** Commit `Migrate backgrounds off im.Scale to native scaling` (só se feito).

### Task 7: Traduções + compat de saves
- [ ] **Step 1:** Regenerar o esqueleto de tradução (os paths mudaram na refatoração): `… renpy.py "<PROJ>" translate english` (o `tl/` é gitignored; regenerável).
- [ ] **Step 2 (verificação de save):** com o reset da Task 2 aplicado, carregar **um save por ato** (se existirem) no 8.5.3. Saves são quase todos primitivos + um `set` (`contacts`) + listas de tuplas (`chat_history`) → fazem pickle limpo 3.9→3.12. O único problemático (save no meio do chat) é coberto pelo reset. Compat backward **não** é meta — aceitável invalidar saves antigos se algum falhar.
- [ ] **Step 3:** Commit `Regenerate english translation skeleton for 8.5.3`.

---

## Compat dos constructos da refatoração sob 8.5 (auditado — OK, só validar)
- `config.missing_image_callback(fn)` — assinatura inalterada no 8.5.3 ✓
- `define BACKEND_BASE_URL` — store define, sem dependência de engine ✓
- `default contacts = set()` — `set` salvável/picklável 3.9→3.12; `add_contact` guarda com `not in` ✓
- `set_available()` / `getattr/setattr(store,...)` — version-independent ✓
- `_()` em `define`/`init python`/`notify` — marcação inalterada ✓
- `pygame_sdl2` — **não usado** (confirmado) → remoção do 8.5 é não-issue ✓
- paths de imagem explícitos → mudança de `images_directory` (8.4) não afeta ✓

## Self-review (cobertura)
- Recompilar sob 3.12 + requests: Task 1 ✅
- Riscos de runtime: threading/softlock (Task 2), is_web (Task 3), replay (Task 4), zoom/oversampling/show-expression (Task 5/6) ✅
- Saves + i18n: Task 7 ✅
- Tudo de bug-fix/reestruturação do plano antigo: **OBSOLETO** (feito na refatoração) ✅

## Riscos (ranqueados)
1. **Altíssimo:** mutação de `store` fora da main thread + softlock `is_waiting` no chat (`chat_backend.rpy`) → Task 2.
2. **Alto:** replay sem reset (`jump start`) → Task 4.
3. **Médio:** re-enquadramento de sprites se `config.zoom_zaxis` ficar no default `True` do 8.5 → Task 5 (setar explícito, não confiar no parse de `config.version`).
4. **Baixo:** saves no meio do chat; suavidade de `im.Scale`; branch web (stub). Todos limitados.

## Handoff de execução
1. **Subagent-Driven (recomendado)** — `renpy-migration-853-agent` por tarefa (report-first; edita após aprovação), `renpy-lint-doctor` verifica cada checkpoint.
2. **Inline** — com checkpoints.

> Pré-requisito real: Tasks 1/5/6 e as verificações exigem o **SDK 8.5.3** e **rodar/jogar** localmente (manual). Ordem: Task 1 → 2 → 3 → 4 → 5 → 7 (Task 6 opcional ao final).
