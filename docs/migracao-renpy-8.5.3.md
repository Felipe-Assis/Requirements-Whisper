# Migração Ren'Py 8.3.7 → 8.5.3

> Análise gerada em 2026-06-06. Versão atual do jogo: **Ren'Py 8.3.7** (build `8.3.7.25031702`).
> Versão estável mais recente: **Ren'Py 8.5.3** ("We Can Go to the Moon", 15/05/2026).

## Resumo executivo

**Veredito:** a migração é **viável e sem bloqueadores rígidos**. A maior parte do trabalho é
mecânico (baixar o SDK, recompilar sob Python 3.12, rodar `lint`, testar). O ponto de maior
atenção **não** é a engine em si, e sim um padrão já existente no código: o **chat usa uma thread
crua que altera o `store` e força `restart_interaction()` fora da main thread** — isso já é frágil
hoje e fica mais arriscado com o salto Python 3.9 → 3.12.

**Esforço estimado:** **baixo a médio** — ~0,5 a 1 dia de trabalho focado (recompilar + corrigir o
punhado de itens abaixo + teste de regressão de uma playthrough completa).

| Eixo | Avaliação |
|---|---|
| Bloqueadores rígidos | Nenhum |
| `pygame_sdl2` removido (8.5) | **Não afeta** — não é usado em lugar algum |
| Live2D 5.3 obrigatório (8.5.3) | **Não afeta** — o jogo não usa Live2D |
| Salto Python 3.9 → 3.12 (8.4) | Afeta — recompilar bytecode; revalidar `requests`/threading |
| Mudança de semântica de `default` (8.5) | Afeta — interage com bugs latentes de estado |
| `zoom` passa a afetar eixo Z (8.5) | Verificar — o jogo usa transforms `*_zoom` em sprites |

---

## 1. O que muda entre 8.3.7 e 8.5.3

### Ren'Py 8.4.0
- **Python 3.12** em todas as plataformas (era ~3.9). O bytecode `.rpyc` 3.9 é incompatível → recompilar.
- `pygame_SDL2` fundido na engine como `renpy.pygame` (alias mantido).
- **Oversampling automático** de imagens em telas high-DPI (desabilita com `config.automatic_oversampling = None`).
- **Mipmaps** só são gerados abaixo de 75% da escala (volta o comportamento antigo com `config.mipmap = True`).
- RTL habilitado por padrão; Windows 10+ obrigatório (você está no 11 ✓).
- `show expression "x"` passa a equivaler a `show x` (reverte com `config.old_show_expression = True`).
- Novidades: shaders aprimorados, modelos GLTF, features OpenType, salvamento automático de estado em traceback, organização de projetos em pastas no launcher.

### Ren'Py 8.5.0
- Continua em **Python 3.12**.
- ⚠️ **Variáveis `default` agora são salvas/carregadas como variáveis normais** e (re)inicializadas apenas em um *start/restart* real.
- ⚠️ **`zoom` agora afeta o eixo Z** (reverte com `config.zoom_zaxis = False`).
- `config.images_directory` → `config.image_directories` (lista). **N/A** — o template não define isso.
- `xmaximum`/`ymaximum` podem exceder o container (`config.maximum_embiggens = False` reverte).
- Detecção de idioma prefere `"en"` a `"us"`. Remoção definitiva do `pygame_SDL2`.
- Novidades: Live2D na web, framework de testes automatizados, Unicode 17.

### Ren'Py 8.5.1 – 8.5.3
- Apenas correções; `config.safe_text` adicionado. 8.5.3 exige Live2D 5.3 (**N/A** aqui).

---

## 2. O que de fato afeta ESTE jogo (cross-map)

| Mudança da engine | Afeta? | Ação |
|---|---|---|
| Python 3.9 → 3.12 | **Sim** | Recompilar (`force_recompile` já está `true`); limpar `game/cache` e `.rpyc` |
| `requests` sob 3.12 | Verificar | Confirmar que o SDK 8.5.3 ainda fornece `requests` (o chat depende disso; não é vendorizado no repo) |
| `threading.Thread` mutando store | **Sim (alto)** | Migrar para `renpy.invoke_in_thread` / marshaling para a main thread |
| `default` salvo/resetado (8.5) | **Sim** | Revisar estado transitório (`is_waiting`, `chat_history`) e o replay via `jump start` |
| `zoom` no eixo Z (8.5) | Verificar | Testar sprites com `*_zoom`; se necessário `define config.zoom_zaxis = False` |
| Oversampling/mipmap (8.4) | Qualidade | Backgrounds usam `im.Scale`; verificar nitidez em high-DPI |
| `config.check_conflicting_properties = True` | **Sim** | Já está ligado (`gui.rpy:15`) → conflitos latentes viram erro; rodar `lint` |
| `pygame_sdl2` removido | Não | Não usado |
| Live2D 5.3 | Não | Não usado |

---

## 3. Riscos no código (priorizados)

### 🔴 Alto — Modelo de threading do chat
`game/scripts/mechanics/chat_screen.rpy` dispara uma `threading.Thread` que roda `requests.post`
(bloqueante) e, no callback, **altera o `store`** (`chat_history`, `is_waiting`) e chama
`renpy.exports.restart_interaction()` **fora da main thread**. O `store`/UI do Ren'Py não são
thread-safe; funciona "por sorte". As mudanças de finalização de threads/GIL do Python 3.12 (8.4)
aumentam a chance de corrupção de estado, exceção no shutdown ou deadlock. A thread também não é
`daemon` nem sofre `join`.
**Correção:** usar `renpy.invoke_in_thread(...)` (integra ao modelo de interação) ou postar o
resultado para a main thread; só mutar `store` e chamar `restart_interaction()` na main thread.

### 🟠 Médio
- **Detecção de web por `import emscripten`** (`chat_screen.rpy:75-80`): trocar pela API suportada
  `renpy.variant('web')` / `'web' in renpy.config.variants` / `renpy.emscripten`. O 8.4 reconstruiu o runtime web sobre Python 3.12.
- **`user_id` como `default` por-save** (`chat_screen.rpy:6` + `script.rpy:2-3`): não é identidade
  estável por instalação. Se correlação entre saves importa, mover para `persistent.user_id`.
- **Replay via `jump start` + `default` (8.5)** (`scene_epilogo_conquistas_final.rpy:82`): "Jogar
  novamente" faz `jump start`, que **não** é restart real → uma segunda jogada herda estado antigo
  (amizades, contatos, itens, relógio). Com o 8.5 esse estado obsoleto também passa a circular por
  save/load. **Correção:** usar `renpy.full_restart()` (ou resetar explicitamente os `default` no topo de `start`).
- **Estado transitório em `default`** (`variables/progress.rpy`): `is_waiting`, `user_input`,
  `server_response` não deveriam ser persistidos; com o 8.5 um save feito durante uma requisição
  restaura `is_waiting=True`. Resetar em `start`/`after_load`.

### 🟡 Baixo / limpeza
- **`renpy.store.__dict__` / `setattr` dinâmico** (`inventory_screen.rpy:96-99`, `contacts_screen.rpy:432-440`):
  prefira `getattr/setattr(store, ...)`; contorna o rastreamento de `default` do 8.5.
- **`except:` nu** no chat → `except Exception:`. Consolidar as 3 rotinas de normalização de resposta.
- **`im.Scale` em todos os backgrounds** (`backgrounds.rpy`): legado; perde o oversampling do 8.4 (risco de nitidez em 4K, não de crash).

> Nota: o scan repo-wide confirmou **nenhum** `import pygame_sdl2`, **nenhum** uso de `renpy.version`/`config.version`
> como gate de lógica, e **nenhum** uso de stdlib removida.

---

## 4. Como migrar (passo a passo)

### O que baixar
1. Baixe o **Ren'Py 8.5.3 SDK** (Windows) em <https://www.renpy.org/latest.html>.
2. Extraia/instale (ex.: `C:\Program Files (x86)\renpy-8.5.3-sdk`). **Mantenha o 8.3.7 instalado** como rollback.
3. (Se for buildar web) no launcher 8.5.3, instale o **Web platform support** (e, para builds mobile/Live2D, o respectivo support).

### O que modificar / executar
4. Abra o `renpy.exe` (launcher) do **8.5.3** e adicione/selecione este projeto (a raiz que contém `game/`).
5. Limpe artefatos do Python 3.9 (PowerShell):
   ```powershell
   Remove-Item -Recurse -Force "c:\Users\Felipe\Documents\GitHub\Renpy Projects\Requirements-Whisper\game\cache" -ErrorAction SilentlyContinue
   Get-ChildItem "c:\Users\Felipe\Documents\GitHub\Renpy Projects\Requirements-Whisper\game" -Recurse -Include *.rpyc,*.rpymc | Remove-Item -Force
   ```
   (`project.json` já tem `force_recompile: true`, o que ajuda.)
6. No launcher: **Force Recompile** → **Check script (lint)**. Equivalente em CLI:
   ```powershell
   & "C:\Program Files (x86)\renpy-8.5.3-sdk\renpy.exe" "c:\Users\Felipe\Documents\GitHub\Renpy Projects\Requirements-Whisper" lint
   ```
7. **Launch Project** e jogue. Corrija o que o `lint`/traceback apontar.
8. Aplique as correções de código da seção 3 (prioridade: threading → detecção web → estado/replay).
9. Teste de regressão: playthrough completa, com foco em **chat**, **save/load**, **"Jogar novamente"**,
   e renderização de sprites com `*_zoom` (eixo Z) e backgrounds (oversampling).

### Verificação rápida (gates)
- `lint` sem erros novos.
- Chat envia/recebe e não trava `is_waiting`.
- Save em meio a uma cena → load → estado coerente.
- Nova jogada após o epílogo começa "do zero".

---

## 5. Vantagens de migrar

- **Python 3.12**: melhor performance, stdlib moderna e correções de segurança.
- **Engine suportada**: 8.3.7 está duas minors atrás; ficar no 8.5.x garante bugfixes/segurança.
- **Qualidade visual**: oversampling/high-DPI, features OpenType, shaders melhores, GLTF.
- **Produtividade/depuração**: salvamento automático de estado em traceback; organização de projetos.
- **Framework de testes automatizados (8.5)**: permitiria criar testes de fluxo do jogo (hoje inexistentes).
- **Web melhorada**: relevante se um dia o chat web for habilitado (hoje desativado).
- Unicode 17 / emojis; Live2D na web (caso venha a usar).

## 6. Desvantagens / riscos

- **Custo de re-teste**: é obrigatório validar manualmente (não há suíte de testes) — chat, save/load, replay, render.
- **Mudanças visuais sutis**: `zoom` no eixo Z e oversampling podem alterar a aparência → possível ajuste de `config.*`.
- **Semântica de `default` (8.5)** expõe bugs latentes de estado (replay, estado transitório persistido).
- **Dependência `requests`**: precisa confirmar que o runtime do SDK 8.5.3 a fornece.
- **Compatibilidade de saves**: a migração em si não renomeia variáveis (saves seguem válidos), mas
  qualquer refator que **renomeie** variável/label invalida saves antigos (ver doc de reestruturação).
- **Recência**: 8.5.3 é recente; extensões/Live2D exigiriam updates (N/A neste projeto).

## 7. Checklist

- [ ] Baixar e instalar o SDK 8.5.3 (manter 8.3.7 para rollback)
- [ ] (Opcional) instalar Web platform support
- [ ] Limpar `game/cache` + `.rpyc`/`.rpymc`
- [ ] Force Recompile + `lint` (sem erros novos)
- [ ] Confirmar `import requests` no runtime 8.5.3
- [ ] Corrigir threading do chat (`renpy.invoke_in_thread`)
- [ ] Trocar detecção web (`renpy.variant('web')`)
- [ ] Tratar replay (`jump start` → `full_restart`) e estado transitório
- [ ] Testar `*_zoom` (eixo Z) e backgrounds (oversampling)
- [ ] Playthrough completa de regressão
