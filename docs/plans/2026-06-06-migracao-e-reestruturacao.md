# Migração Ren'Py 8.5.3 + Reestruturação — Plano de Implementação

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Migrar "The Requirements Whisperer" de Ren'Py 8.3.7 para 8.5.3 e aplicar a reestruturação de alto valor, sem quebrar saves nem o fluxo narrativo.

**Architecture:** Jogo Ren'Py single-store; cenas em `call`-chain a partir de `label start`; mecânicas (chat/inventário/contatos/relógio) em `game/scripts/mechanics/`; estado em `default` globais.

**Tech Stack:** Ren'Py 8.5.3 SDK (Python 3.12), backend HTTP externo (chat), Windows 11.

---

## ⚠️ Verificação neste projeto (não há suíte de testes)

Não existe framework de testes unitários. **Em cada tarefa, o "teste" é:**
1. **Lint:** `& "C:\Program Files (x86)\renpy-8.5.3-sdk\renpy.exe" "c:\Users\Felipe\Documents\GitHub\Renpy Projects\Requirements-Whisper" lint` → **0 erros novos**.
2. **Playthrough dirigida** do trecho afetado (instruções específicas por tarefa).

Use `SDK83 = "C:\Program Files (x86)\renpy-8.3.7-sdk\renpy.exe"` e `SDK85 = "C:\Program Files (x86)\renpy-8.5.3-sdk\renpy.exe"`, `PROJ = "c:\Users\Felipe\Documents\GitHub\Renpy Projects\Requirements-Whisper"` como abreviações.

**Ordem recomendada:** Fase 0 → Fase 2 (bugs que já quebram hoje) → Fase 1 (migração) → Fase 3 (reestruturação). Bugs primeiro garantem uma base estável antes de trocar a engine.

---

## Fase 0 — Baseline e rede de segurança

### Task 0: Baseline no 8.3.7
**Files:** nenhum (apenas git + lint)

- [ ] **Step 1:** Branch de segurança.
  ```powershell
  git -C $PROJ checkout -b migracao-8.5.3
  ```
- [ ] **Step 2:** Lint baseline no SDK atual e salvar a saída.
  ```powershell
  & "C:\Program Files (x86)\renpy-8.3.7-sdk\renpy.exe" "c:\Users\Felipe\Documents\GitHub\Renpy Projects\Requirements-Whisper" lint
  ```
  Esperado: registrar os erros/avisos existentes (servem de referência).
- [ ] **Step 3:** Commit do estado inicial (caso haja mudanças pendentes intencionais).

---

## Fase 1 — Migração para 8.5.3

### Task 1: Instalar SDK 8.5.3 e recompilar
**Files:** `game/cache/` (apagar), `*.rpyc/*.rpymc` (apagar)

- [ ] **Step 1:** Baixar o **Ren'Py 8.5.3 SDK** (Windows) de <https://www.renpy.org/latest.html> e extrair em `C:\Program Files (x86)\renpy-8.5.3-sdk`. **Manter** o 8.3.7 instalado (rollback).
- [ ] **Step 2:** Limpar bytecode do Python 3.9.
  ```powershell
  Remove-Item -Recurse -Force "c:\Users\Felipe\Documents\GitHub\Renpy Projects\Requirements-Whisper\game\cache" -ErrorAction SilentlyContinue
  Get-ChildItem "c:\Users\Felipe\Documents\GitHub\Renpy Projects\Requirements-Whisper\game" -Recurse -Include *.rpyc,*.rpymc | Remove-Item -Force
  ```
- [ ] **Step 3:** Abrir o launcher do 8.5.3 (`renpy.exe`), adicionar o projeto, **Force Recompile**.
- [ ] **Step 4 (verificação):** Lint no 8.5.3.
  ```powershell
  & "C:\Program Files (x86)\renpy-8.5.3-sdk\renpy.exe" "c:\Users\Felipe\Documents\GitHub\Renpy Projects\Requirements-Whisper" lint
  ```
  Esperado: nenhum erro **novo** vs. baseline (corrigir os novos nas tarefas seguintes).
- [ ] **Step 5 (verificação):** Confirmar `requests` no runtime do SDK. No console do jogo (Shift+O) ou num label de teste: `$ import requests` não deve lançar `ImportError`.
- [ ] **Step 6:** Commit.
  ```powershell
  git -C $PROJ add -A; git -C $PROJ commit -m "Recompile project under Ren'Py 8.5.3 (Python 3.12)"
  ```

### Task 2: Corrigir threading do chat (🔴 risco de corromper estado)
**Files:** Modify `game/scripts/mechanics/chat_screen.rpy` (envio desktop, ~linhas 96-102 / 212-218)

- [ ] **Step 1:** Localizar o disparo da thread:
  ```python
  import threading
  threading.Thread(target=lambda: send_message_to_backend(user_message, process_respostas)).start()
  ```
- [ ] **Step 2:** Substituir pela API suportada do Ren'Py (roda em thread integrada ao modelo de interação):
  ```python
  # main thread agenda; o request roda fora da main thread
  renpy.invoke_in_thread(send_message_to_backend, user_message, process_respostas)
  ```
- [ ] **Step 3:** Garantir que a mutação de `store` + `restart_interaction` ocorra de forma segura. Em `process_respostas`, em vez de mutar direto da thread, agendar para a main thread:
  ```python
  def process_respostas(resposta):
      def _apply():
          global chat_history, is_waiting
          chat_history.append(("bot", normalize_resposta(resposta)))
          is_waiting = False
          renpy.restart_interaction()
          return False  # timer dispara uma vez
      renpy.invoke_in_thread(lambda: None)  # no-op de segurança se necessário
      renpy.call_in_new_context if False else None
      renpy.restart_interaction()  # acorda a tela; _apply roda via timer abaixo
  ```
  > Nota de implementação: o caminho mais simples e robusto é a tela `chat_with_backend` ter um
  > `timer 0.1 repeat True action Function(drain_pending_response)` que, na **main thread**, consome
  > um buffer simples preenchido pela thread (`pending_response`). Implemente `drain_pending_response`
  > para mover `pending_response` → `chat_history` e zerar `is_waiting`. Isso evita qualquer mutação de
  > `store`/UI fora da main thread.
- [ ] **Step 4 (verificação):** Lint + jogar uma conversa de chat completa (enviar 3 mensagens), confirmar respostas aparecendo, sem travar `is_waiting` e sem erro ao fechar o jogo. Repetir com a internet desligada (deve degradar com mensagem de erro, não crashar).
- [ ] **Step 5:** Commit `Fix chat threading to marshal store updates onto the main thread`.

### Task 3: Trocar a detecção de web pela API suportada
**Files:** Modify `game/scripts/mechanics/chat_screen.rpy:75-80`

- [ ] **Step 1:** Substituir:
  ```python
  def is_web():
      try:
          import emscripten
          return True
      except ImportError:
          return False
  ```
  por:
  ```python
  def is_web():
      return renpy.variant("web")
  ```
- [ ] **Step 2 (verificação):** Lint + rodar no desktop (deve usar o caminho desktop normalmente). Se houver build web, confirmar que continua exibindo a mensagem "chat indisponível na web".
- [ ] **Step 3:** Commit `Use renpy.variant('web') for web detection`.

### Task 4: Replay e estado transitório vs. semântica de `default` (8.5)
**Files:** Modify `game/scripts/scene_epilogo_conquistas_final.rpy` (opção "Jogar novamente"); revisar `game/scripts/variables/progress.rpy`

- [ ] **Step 1:** No epílogo, trocar o replay por restart real:
  ```renpy
  "Jogar novamente (novo ciclo, novos desafios)":
      $ renpy.full_restart()
  ```
- [ ] **Step 2:** Evitar que estado transitório do chat sobreviva a save/load. Adicionar um callback:
  ```renpy
  define config.after_load_callbacks = config.after_load_callbacks + [__reset_transient]
  init python:
      def __reset_transient():
          store.is_waiting = False
          store.user_input = ""
          store.server_response = ""
  ```
- [ ] **Step 3 (verificação):** Lint; jogar até o fim → "Jogar novamente" → confirmar que amizades/contatos/itens/relógio começam **zerados**. Salvar durante uma espera do chat → carregar → `is_waiting` deve estar `False`.
- [ ] **Step 4:** Commit `Use full_restart on replay; reset transient chat state on load`.

### Task 5: Validar renderização (zoom eixo-Z + oversampling)
**Files:** possivelmente `game/scripts/backgrounds.rpy`, `game/options.rpy` (apenas se necessário)

- [ ] **Step 1 (verificação):** Jogar cenas com sprites usando `*_zoom` e observar posição/tamanho. Se algo deslocar por causa do eixo Z:
  ```renpy
  define config.zoom_zaxis = False
  ```
- [ ] **Step 2 (verificação):** Observar backgrounds em tela cheia/high-DPI. Se houver "shimmer"/borrado:
  ```renpy
  define config.mipmap = True
  ```
  (ou, melhor, remover `im.Scale` e deixar o Ren'Py escalar a fonte full-res — ver Fase 3 opcional.)
- [ ] **Step 3:** Commit somente se algum `config.*` foi alterado: `Tune zoom/mipmap config for 8.5 rendering`.

---

## Fase 2 — Bugs que já quebram o jogo (independem da versão)

> Ver `docs/pontos-criticos.md` para o detalhamento (P1–P6) e a nota sobre crash-vs-placeholder.

### Task 5.5: Imagens/atributos ausentes (P1, P2) + rede de segurança
**Files:** Modify scenes 1/4/9/10/13/17 (notebook), 18_2/19/20 (ui), 21 (npcs), 14/16 (diagrams); `game/scripts/characters.rpy`; `game/options.rpy`

- [ ] **Step 1 (rede de segurança):** em `game/options.rpy`, adicionar fallback global para imagens ausentes:
  ```renpy
  init python:
      def _img_ausente(fn):
          return Text("[imagem ausente: %s]" % fn, size=20, color="#f55")
      config.missing_image_callback = _img_ausente
  ```
- [ ] **Step 2 (P1 — notebook):** substituir `images/items/notebook.png` por `images/items/notebook_aberto.png` em: scene_1:64, scene_4:29, scene_9:32, scene_10:28, scene_13:25, scene_17:19.
- [ ] **Step 3 (P1 — ui/npcs/diagrams):** em scene_18_2:17/55, scene_19:26, scene_20:31/164 criar os assets em `game/images/ui/` **ou** repontar p/ assets de `images/artifacts/` existentes **ou** remover os pares `show`/`hide`; em scene_21:45/46 usar `show doutora_1 neutral` / `show doutora_2 neutral`; conferir scene_14:96 e scene_16:26 (diagrams).
- [ ] **Step 4 (P2 — atributos):** em `characters.rpy`, adicionar aliases para os atributos ausentes (`developer_ai enthusiastic`, `developer_project positive`, `developer_quality enthusiastic`, `developer_security enthusiastic`, `developer_management positive/enthusiastic`) apontando para `.png` existentes do respectivo personagem.
- [ ] **Step 4b (P7 — transform):** em `scene_11_almoco_equipe.rpy:127`, trocar `at left_zoom2` por `at left_zoom_2` (transform definido em `characters.rpy:131`).
- [ ] **Step 5 (verificação):** `lint` sem avisos de imagem não-carregável / `'X attr' is not an image` / `Could not evaluate 'left_zoom2'`; playthrough cobrindo scene_1, scene_11, scene_16, scene_18_2 (rota "finalizar pela manhã"), scene_19, scene_20, scene_21 e os menus que disparam os atributos.
- [ ] **Step 6:** Commit `Fix missing image files/attributes and add missing-image safety net`.

### Task 6: Definir `image bg creditos` (crash no epílogo)
**Files:** Modify `game/scripts/backgrounds.rpy`

- [ ] **Step 1:** Confirmar o uso: o label `creditos_finais` faz `scene bg creditos`. Verificar que não existe `image bg creditos`.
- [ ] **Step 2:** Adicionar a definição apontando para um asset existente (criar/escolher uma arte de créditos):
  ```renpy
  image bg creditos = im.Scale("images/bg/creditos.png", config.screen_width, config.screen_height)
  ```
  Se não houver arte dedicada, reaproveitar um background existente temporariamente.
- [ ] **Step 3 (verificação):** Lint (não deve mais acusar imagem indefinida) + jogar o caminho dos créditos.
- [ ] **Step 4:** Commit `Define missing bg creditos image`.

### Task 7: Fallback de portrait do chat (crash/imagem ausente)
**Files:** add asset `game/images/characters/generic_portrait.png` OU Modify `chat_amigo` em `game/scripts/mechanics/chat_screen.rpy`

- [ ] **Step 1:** Adicionar o arquivo `generic_portrait.png` em `game/images/characters/` **ou** repontar o fallback do `chat_amigo` para um portrait existente.
- [ ] **Step 2 (verificação):** Forçar o fallback (selecionar contato sem portrait) e confirmar que carrega sem erro.
- [ ] **Step 3:** Commit `Add generic_portrait fallback asset`.

### Task 8: Bug do contato `doutora_2`
**Files:** Modify `game/scripts/mechanics/contacts_screen.rpy`

- [ ] **Step 1:** Localizar a ação que seta `amigo_selecionado = "amizade_doutora_2"`.
- [ ] **Step 2:** Corrigir para o id correto:
  ```renpy
  action [SetVariable("amigo_selecionado", "doutora_2"), Hide("contacts_screen"), Jump("chat_amigo")]
  ```
- [ ] **Step 3 (verificação):** Abrir contatos → selecionar a doutora 2 → o chat deve abrir com nome/portrait corretos (não o genérico).
- [ ] **Step 4:** Commit `Fix doutora_2 contact selection id`.

### Task 9: Corrigir caminho de áudio e imagem duplicada
**Files:** Modify `game/scripts/scene_1_quarto.rpy`, `game/scripts/items.rpy`

- [ ] **Step 1:** Corrigir `audio/effectssend_email.ogg` → `audio/effects/send_email.ogg` (confirmar o caminho real do asset) e alinhar `.wav`/`.ogg` de `computer_typing`.
- [ ] **Step 2:** Remover a definição duplicada de `image item notebook` em `items.rpy:60-61` (manter a intencional).
- [ ] **Step 3 (verificação):** Lint (sem avisos de asset/imagem duplicada) + jogar `scene_1`.
- [ ] **Step 4:** Commit `Fix send_email audio path and duplicate notebook image`.

### Task 10: Remover linha morta `inventory = []`
**Files:** Modify `game/scripts/scene_1_quarto.rpy`

- [ ] **Step 1:** Apagar a linha `$ inventory = []` (órfã; o estado real é `inventario`). **Não** renomear `inventario`.
- [ ] **Step 2 (verificação):** Jogar até `scene_21` e confirmar que as condições de vitória que leem `inventario` continuam funcionando.
- [ ] **Step 3:** Commit `Remove dead inventory variable`.

---

## Fase 3 — Reestruturação de alto valor

### Task 11: Agrupar cenas em `story/actN_*/` + renomear arquivos com typo
**Files:** Move `game/scripts/scene_*.rpy` → `game/story/actN_*/...`; rename 2 arquivos

- [ ] **Step 1:** Criar pastas `game/story/act1_intro/`, `act2_requisitos/`, `act3_construcao/`, `act4_final/`.
- [ ] **Step 2:** Mover cada `scene_*.rpy` para o ato correspondente com `git mv` (preserva histórico). **Não alterar nomes de label.**
- [ ] **Step 3:** Renomear arquivos (não labels): `scene_15_aniversario_supresa.rpy` → `...surpresa.rpy`; `scene_18_2_codificacaso_final.rpy` → `...codificacao_final.rpy`.
- [ ] **Step 4 (verificação):** Lint (labels resolvem globalmente → 0 referências quebradas) + abrir o jogo e avançar algumas cenas.
- [ ] **Step 5:** Commit `Group scenes into act folders; fix typo'd filenames`.

### Task 12: Tela de contatos *data-driven*
**Files:** Create `game/data/contacts.rpy` (tabela `CONTACTS` + `CONTACTS_ORDER`); Modify `game/scripts/mechanics/contacts_screen.rpy`

- [ ] **Step 1:** Criar a tabela (em `init python` simples, para enxergar `NOME_*`/`COR_*`):
  ```renpy
  init python:
      CONTACTS = {
          "developer_ai": {"name": NOME_DEVELOPER_AI, "portrait": "developer_ai portrait",
                            "assistant_id": "asst_...", "desc": "...", "color": COR_DEVELOPER_AI},
          # ... demais contatos ...
      }
      CONTACTS_ORDER = ["developer_ai", "developer_requirements", "developer_coding",
                        "developer_management", "developer_quality", "developer_project",
                        "developer_security", "developer_test", "doutora_1", "doutora_2"]
      def friendship_color(v):
          if v >= 10: return "#FFD700"
          elif v >= 7: return "#7CFC00"
          elif v >= 4: return "#FFA500"
          else: return "#AAAAAA"
  ```
- [ ] **Step 2:** Substituir os 10 blocos copiados por um loop e uma `screen friendship_bar`:
  ```renpy
  screen friendship_bar(value):
      bar value AnimatedValue(value, 10) xsize 200 ysize 14
  screen contacts_screen():
      # ... moldura ...
      vbox:
          for cid in CONTACTS_ORDER:
              if getattr(store, "contato_" + cid, False):
                  $ disponivel = getattr(store, "disponivel_" + cid, False)
                  imagebutton:
                      idle ("%s portrait" % cid)
                      sensitive disponivel
                      action [SetVariable("amigo_selecionado", cid), Hide("contacts_screen"), Jump("chat_amigo")]
                  use friendship_bar(getattr(store, "amizade_" + cid, 0.0))
                  text CONTACTS[cid]["desc"]
  ```
- [ ] **Step 3:** Declarar `default contacts = set()` num arquivo de estado (em vez de criação preguiçosa) para o 8.5 resetar corretamente.
- [ ] **Step 4 (verificação):** Lint + abrir contatos: todos os 10 aparecem na ordem certa, disponíveis/indisponíveis corretos, cada um abre o chat certo (especialmente `doutora_2`). Playtest do chat de 2-3 contatos.
- [ ] **Step 5:** Commit `Make contacts screen data-driven (CONTACTS table + loop)`.

### Task 13: Centralizar config do backend
**Files:** Modify `game/scripts/mechanics/chat_screen.rpy` (2 ocorrências do IP)

- [ ] **Step 1:** Definir um único ponto:
  ```renpy
  define BACKEND_BASE_URL = "http://15.229.14.83:8000"
  ```
- [ ] **Step 2:** Substituir **as duas** ocorrências hardcoded por `BACKEND_BASE_URL + "/chat/message/send"`.
- [ ] **Step 3 (verificação):** Lint + enviar uma mensagem no chat (desktop). Confirmar a mensagem "indisponível na web" intacta no caminho web.
- [ ] **Step 4:** Commit `Centralize backend URL in one define`.

### Task 14 (opcional): Consolidar helpers + `>= 10`
**Files:** Create `game/logic/helpers.rpy`; Modify `contacts_screen.rpy`, `inventory_screen.rpy`

- [ ] **Step 1:** Mover `add_friendship_point`/`get_friendship_point`/`add_contact`/`add_to_inventory` (todos `init python`) para 1-2 arquivos de lógica. Não mudar assinaturas.
- [ ] **Step 2:** Trocar comparações `== 10` por `>= 10` na cor de amizade.
- [ ] **Step 3 (verificação):** Lint + playthrough curta exercitando ganho de amizade e coleta de item.
- [ ] **Step 4:** Commit `Consolidate gameplay helpers; use >= for friendship cap`.

---

## Self-review (cobertura do spec)

- Migração 8.5.3 (baixar/recompilar/lint/testar): Tasks 1-5 ✅
- Riscos de código da migração (threading, web, replay/transient, render): Tasks 2-5 ✅
- Bugs game-breaking: Tasks 5.5–10 ✅ (P1–P6; ver `docs/pontos-criticos.md`)
- Reestruturação de alto valor (cenas, contatos data-driven, config): Tasks 11-13 ✅
- Itens descartados (taxonomia 6 pastas, split de estado, chat_client.py, mexer no fluxo de cenas): **fora do plano por decisão** (ver `docs/reestruturacao-projeto.md` §5).

## Handoff de execução

Plano salvo. Duas opções de execução:
1. **Subagent-Driven (recomendado)** — um subagente novo por tarefa, com review entre tarefas.
2. **Inline** — executar nesta sessão com checkpoints.

> ⚠️ Pré-requisito real: as Tasks 1, 5 e várias verificações exigem o **SDK 8.5.3 instalado** e
> rodar/jogar o jogo localmente — isso é manual (não automatizável por agente sem o app).
