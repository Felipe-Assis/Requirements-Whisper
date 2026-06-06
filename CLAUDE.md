# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this is

"The Requirements Whisperer" (`config.name`) is an educational Ren'Py visual novel built as a UFRJ Game Design course project. The player is an intern living through the full software-engineering lifecycle (requirements, specification, design, coding, testing, deploy) of a clinical healthcare web system, while choices affect friendships, branching, and the ending. The narrative content and all UI strings are in Brazilian Portuguese. Developed and tested with Ren'Py 8.3.7 (build `8.3.7.25031702`; SDK at `C:\Program Files (x86)\renpy-8.3.7-sdk`); minimum Ren'Py 8.2+ / Python 3.8+.

## Common commands

There is no Makefile, npm, or CI — everything goes through the Ren'Py SDK launcher. The project root passed to the launcher is the repo root (the folder containing `game/`), NOT the `game/` folder itself.

GUI workflow (primary, on Windows): launch `renpy.exe` from the SDK, then in the launcher select/add this repo as a project and use Launch Project / Build Distributions / "Check script (lint)" / "Force recompile".

CLI equivalents (run from the SDK directory; `<project>` = absolute path to this repo root):
- Run the game: `renpy.exe "<project>"` (or `./renpy.sh "<project>"`)
- Lint (do this before committing script changes): `renpy.exe "<project>" lint`
- Compile `.rpy` -> `.rpyc`: `renpy.exe "<project>" compile`
- Build distributions: `renpy.exe "<project>" distribute` — `project.json` targets `pc`, `mac`, `win`, `linux`, with `force_recompile: true` and `build_update: false`. `options.rpy` sets `build.name = "TheRequirementsWhisperer"`; `progressive_download.txt` configures RenPyWeb progressive download.

There is no test suite. "Verification" means launching the game and walking the relevant scene; Ren'Py writes diagnostics to `log.txt`, `errors.txt` (lint/parse errors), and `traceback.txt` (runtime exceptions) at the repo root — read these to debug. Note: `traceback.txt`/`errors.txt` in the repo are stale historical artifacts (e.g. an `is_web()`/`renpy_platform` error that no longer matches current code, and a `backgrounds.rpy` parse error); regenerate them by running, don't trust the committed copies.

## Architecture

### Flow: linear `call` chain
`game/script.rpy` defines `label start`, which `call`s the 22 scene labels strictly in order (`scene_1_quarto` -> ... -> `scene_21_avaliacao_final` -> `scene_epilogo_conquistas_final`). Scene files live in `game/scripts/scene_*.rpy`, one label per file, named after its narrative beat. `scene_2_escritorio` is deliberately commented out of the chain. The epilogue offers replay (`jump start`) / credits / quit. To change story order, edit the `call` list in `script.rpy` — scenes do not auto-discover each other.

### State model: flat `default` globals, no classes
Game state is a large set of module-level `default` variables in `game/scripts/variables/` and `game/scripts/mechanics/`, all living in Ren'Py's `store` and auto-included in saves:
- `variables/variables.rpy` — `item_*` booleans (inventory), per-contact `contato_*` (unlocked at all) and `disponivel_*` (reachable right now) booleans, plus the in-game clock (`game_hour`, `game_minute`, `show_clock`) with `set_time()` / `advance_minutes()` helpers.
- `variables/amizade.rpy` — `amizade_*` floats (0–10) per character (friendship/affinity).
- `variables/progress.rpy` — `progresso_roteiro`, `nivel_estresse`, `energia_diaria`, plus chat runtime state (`chat_history`, `user_input`, `is_waiting`, `server_response`).
- `characters.rpy` — single source of truth for character display names (`NOME_*`), colors (`COR_*`), `Character()` objects, sprite `image` mappings, and reusable sprite-position transforms (`left_zoom`, `center_zoom`, `right_zoom`, etc.). Always reference names via the `NOME_*` defines, never hardcode "Emily"/"Lucas".

### Two flag layers gate the phone/chat
This is the non-obvious core mechanic. Each contact has BOTH a `contato_<id>` (have you met them — show in the contacts grid) and a `disponivel_<id>` (can you message them *now*) flag. Scenes flip `disponivel_*` at their top to model "you can't text someone who's in the same room" (e.g. `scene_11_almoco_equipe` sets all to `False`; `scene_13_retorno_casa_sem3` sets all to `True`; `scene_14` sets a mix). In the contacts UI, an unavailable contact is rendered grayed-out and non-clickable. When editing a scene, set the `disponivel_*` block at the label start to match who's physically present.

Helpers (defined in `mechanics/contacts_screen.rpy`, called from scenes via `$`):
- `add_contact("developer_ai")` — unlocks a contact (sets `contato_developer_ai = True`, notifies).
- `add_friendship_point("developer_ai", amount)` / `get_friendship_point(id)` — adjust/read `amizade_*`. Scene choices call this to reward branches.
- `add_to_inventory("notebook")` (in `mechanics/inventory_screen.rpy`) — sets the matching `item_*` flag.

Contact/character ids are the canonical keys used everywhere (`developer_ai`, `developer_requirements`, `developer_coding`, `developer_management`, `developer_quality`, `developer_project`, `developer_security`, `developer_test`, `doutora_1`, `doutora_2`). Adding a new contact means touching all layers: a `Character`/`NOME_*`/image in `characters.rpy`, `contato_*`/`disponivel_*`/`amizade_*` defaults, an `AMIGOS_DATA` entry (with `assistant_id`), and a block in the `contacts_screen` grid.

### UI mechanics (`game/scripts/mechanics/`)
- `inventory_screen.rpy` — the "Mochila" (backpack) screen + persistent `inventory_button` (top-left, gated by `inventory_enabled`). The phone item (`item_celular`) button opens `contacts_screen`.
- `contacts_screen.rpy` — the contacts grid; selecting an available contact sets `amigo_selecionado`, hides itself, and jumps to `chat_amigo`.
- `clock_screen.rpy` — `top_right_clock` overlay driven by `game_hour`/`game_minute`/`show_clock`.
- `chat_screen.rpy` — the AI chat (see below).

### AI chat: live external backend (load-bearing)
The chat is NOT scripted dialogue — it calls a remote LLM-assistant service over HTTP. Mechanics in `mechanics/chat_screen.rpy`:
- `AMIGOS_DATA` maps each contact id -> `{name, portrait, assistant_id}`. The `assistant_id` values are hardcoded OpenAI-style assistant ids (`asst_...`).
- `label chat_amigo` resets `chat_history`, looks up the selected friend, sets `renpy.store.current_assistant_id`, bumps that friend's `amizade_*` (+1, capped at 10), and calls `screen chat_with_backend`.
- POSTs `{user_id, assistant_id, message}` to a hardcoded endpoint `http://15.229.14.83:8000/chat/message/send`. `user_id` is a random `USER...` id generated once in `label start` via `generate_user_id()` and persisted.
- Desktop path runs the request on a background `threading.Thread` (keeps the UI responsive) and uses `requests` (relies on the SDK's bundled Python having it — not vendored in-repo). `is_web()` branches to a JS `fetch` path for the web build, but web currently just returns a "download the game" notice. Responses are defensively normalized (string-of-list parsing, bracket/quote stripping) before appending to `chat_history`.

When touching chat, keep the desktop/web split and the response normalization; the backend can return a single string, a JSON list, or a stringified list.

### Notes
- `old-game/` holds an earlier compiled version (`.rpyc` only) — legacy, ignore for changes.
- There is no root `.gitignore`; `game/cache/` (and would-be `game/saves/`) are tracked. Don't commit churny `bytecode-*.rpyb` / cache regenerations unless intended.
- Audio is defined as `define music_*` constants in `game/scripts/music.rpy`; backgrounds in `game/scripts/backgrounds.rpy`.
