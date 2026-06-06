# CONVENTIONS.md — Requirements-Whisper

> Documento de referência compartilhado. Agentes referenciam seções por `§` (ex.: `CONVENTIONS.md §A`).
> Regras detalhadas de arquitetura, comandos e fluxo de trabalho estão em `../CLAUDE.md`; este
> documento **distila** as políticas mais críticas para acesso rápido e não duplica o `CLAUDE.md`.

---

## §A Regra de ouro: RELOCAR, nunca RENOMEAR identificadores

> **Nenhuma variável `default` salva e nenhum `label` ganha nome novo.**

O `store` do Ren'Py é serializado no save junto com a pilha de `call`. Renomear qualquer
`default`-variável ou `label` **quebra saves existentes** e pode corromper o estado de jogos em
andamento. As únicas exceções seguras são:

- **Arquivos** `.rpy`: renomear/mover o arquivo é grátis — labels resolvem globalmente.
- **Literais de texto** (`_()`): envolver strings de UI em `_()` é save-safe (só afeta strings).

Fonte: `docs/plans/2026-06-06-refatoracao-manutenibilidade.md` ("Regra de ouro").

---

## §B Verificação: lint + playthrough manual

Não há suíte de testes, Makefile, nem CI neste projeto. A única verificação automatizada disponível é o lint do SDK:

```powershell
& "C:\Program Files (x86)\renpy-8.3.7-sdk\renpy.exe" `
  "c:\Users\Felipe\Documents\GitHub\Renpy Projects\Requirements-Whisper" lint
```

(Substitua o caminho do SDK se usar o 8.5.3.)

A verificação completa exige lint + playthrough manual do trecho afetado.

**Os arquivos `log.txt`, `errors.txt` e `traceback.txt` commitados no root do repo são STALE
(artefatos históricos de bugs já corrigidos ou irrelevantes).** Nunca confie nas cópias commitadas;
regenere rodando o jogo.

---

## §C Fluxo da história

A ordem narrativa vive **exclusivamente** na lista de `call`s em `game/script.rpy` (`label start`).
As cenas não se auto-descobrem. Para alterar a sequência de cenas, edite a lista de `call`s em
`script.rpy` — somente lá.

`scene_2_escritorio` está **intencionalmente** comentada fora da cadeia principal (branch via `jump`,
não via `call`). Isto **não é um bug**.

---

## §D Estado: flat `default` globals, store único

O estado do jogo é um conjunto plano de variáveis `default` em `game/scripts/variables/` e
`game/scripts/mechanics/`, todas no namespace global `store` do Ren'Py — sem classes, sem módulos
separados de escopo.

- Todo `default` é **salvo automaticamente** no save.
- Cada `default` deve existir **uma única vez** em todo o projeto (colisão de nomes causa sobrescrição silenciosa).
- Tabelas que referenciam `NOME_*`/`COR_*` devem ficar em `init python` prio 0 (não `python early`).
- `generate_user_id` fica em `init -1`, antes do `default user_id`.

---

## §E Telefone: gating de 2 flags

Cada contato é controlado por **duas flags independentes**:

| Flag | Semântica |
|---|---|
| `contato_<id>` | O jogador já conheceu este contato (mostra na grade de Contatos). |
| `disponivel_<id>` | O contato pode ser chamado agora (click habilitado). |

Ao editar uma cena, **defina o bloco `disponivel_*` no início do label** para refletir quem está
fisicamente presente (ex.: `scene_11_almoco_equipe` seta todos para `False`; cenas de retorno para
casa setam os remotos de volta para `True`).

Contato indisponível é renderizado em cinza e não é clicável na tela de Contatos.

---

## §F Personagens: sempre via `NOME_*` defines

**Nunca hardcode nomes como `"Emily"` ou `"Lucas"` em diálogos ou telas.** Use sempre os defines:

```renpy
NOME_EMILY, NOME_LUCAS, ...  # definidos em characters.rpy
```

**Adicionar um novo contato exige tocar todos estes pontos (sem exceção):**

1. `characters.rpy` — `Character()`, `NOME_*`, `image` mappings.
2. Defaults de flags — `default contato_<id>`, `default disponivel_<id>`, `default amizade_<id>`.
3. `AMIGOS_DATA` em `mechanics/chat_screen.rpy` — entrada `{name, portrait, assistant_id}`.
4. Bloco na grade de contatos em `mechanics/contacts_screen.rpy`.

---

## §G Chat: cliente LLM load-bearing

O chat é um cliente HTTP real, não diálogo scriptado. Pontos críticos a preservar em qualquer edição:

- **Split desktop/web:** o caminho desktop usa `threading.Thread` + `requests`; o web usa `js.fetch` (ou retorna aviso de download).
- **Normalização defensiva de resposta:** o backend pode retornar uma `string` simples, uma JSON list (`[...]`), ou uma lista stringificada. O normalizador deve tratar os três casos antes de adicionar ao `chat_history`.
- **Estado transitório:** `is_waiting`, `user_input`, `server_response` são `default` (salvos). Resetar em `after_load` e no fechamento do chat para evitar o softlock P6.

Veja `CLAUDE.md §AI chat` para detalhes de implementação.

---

## §H Commits

- Linha de assunto única e concisa; **sem** trailers `Co-Authored-By` ou "Generated with".
- **Não commitar** bytecode churny (`bytecode-*.rpyb`, cache).
- Ignorar `old-game/` (versão compilada legada — não tocar).

---

## §I Bugs conhecidos (P1–P7) — referência de regressão

Lista canônica extraída de `docs/pontos-criticos.md` (revisão 2026-06-06). Qualquer mudança deve
verificar que não introduz novos itens desta lista, e as correções planejadas devem validar que o
item foi resolvido.

| # | Descrição | Localização | Tipo |
|---|---|---|---|
| **P1** | Arquivos de imagem ausentes referenciados via `show expression "<path>"` (ex.: `images/items/notebook.png`, paths `images/ui/*`, `images/npcs/dr_almeida.png`, `images/diagrams/*`) | scenes 1, 4, 9, 10, 13, 14, 16, 17, 18_2, 19, 20, 21 | Asset ausente (placeholder→crash) |
| **P2** | ~16 atributos de sprite ausentes (`developer_ai enthusiastic`, `developer_project positive`, `developer_quality enthusiastic`, `developer_security enthusiastic`, `developer_management positive/enthusiastic`) | scenes 11, 12, 14, 15, 16, 19, 20, 21 | Attribute ausente (lint) |
| **P3** | `bg creditos` nunca definido — `scene bg creditos` em `creditos_finais:89` | `scene_epilogo_conquistas_final.rpy:89` | Imagem indefinida |
| **P4** | Id de contato errado: `SetVariable("amigo_selecionado", "amizade_doutora_2")` (prefixo `amizade_` sobrando) → `AMIGOS_DATA.get(...)` retorna `None` → nome "Contato", portrait quebrado, persona errada, afinidade não conta | `contacts_screen.rpy:390` | Bug de id (lógico, garantido) |
| **P5** | Replay "Jogar novamente" usa `jump start` em vez de restart real → variáveis `default` (amizades, inventário, contatos, relógio) **não** são reinicializadas → no 2º ciclo o final "excelente" é dado independentemente das escolhas; `$ inventory = []` em `scene_1:5` reseta variável errada (`inventario` é o nome real) | `scene_epilogo_conquistas_final.rpy:81-82` | Bug de lógica (garantido) |
| **P6** | Save durante request do chat grava `is_waiting=True` → ao carregar o save, o chat fica travado em "está digitando..." para sempre (softlock sem recuperação); agravado pelo threading fora da main thread | `chat_screen.rpy` + `variables/progress.rpy` | Softlock (garantido) |
| **P7** | Transform `left_zoom2` usado em `at left_zoom2` mas não definido — os transforms existentes são `left_zoom`, `left_zoom_2` (com underscore), `center_zoom`, `right_zoom`, `right_zoom2` | `scene_11_almoco_equipe.rpy:127` | NameError em runtime (garantido) |
