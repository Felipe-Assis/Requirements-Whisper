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

Top-level `game/` layout (after the Fase 1 refactor): `story/act{1..5}_*/` + `story/epilogue/` (scenes), `logic/` (mutable state defaults & helpers), `data/` (static content: characters, names, items, audio, backgrounds), `ui/styles/` (transforms), and `scripts/mechanics/` (the inventory/contacts/clock/chat screens). Entry points `script.rpy`/`screens.rpy`/`options.rpy`/`gui.rpy` stay at the `game/` root.

### Flow: linear `call` chain
`game/script.rpy` defines `label start`, which `call`s the 22 scene labels strictly in order (`scene_1_quarto` -> ... -> `scene_21_avaliacao_final` -> `scene_epilogo_conquistas_final`). Scene files live in `game/story/act{1..5}_*/scene_*.rpy` (one label per file, named after its narrative beat), with the epilogue at `game/story/epilogue/scene_epilogo_conquistas_final.rpy`. Labels are unchanged by the move, so the `call` chain still resolves them by name. `scene_2_escritorio` is deliberately commented out of the chain. The epilogue offers replay (`jump start`) / credits / quit. To change story order, edit the `call` list in `script.rpy` — scenes do not auto-discover each other.

### State model: flat `default` globals, no classes
Game state is a large set of module-level `default` variables under `game/logic/` (static content data lives alongside in `game/data/`), all living in Ren'Py's `store` and auto-included in saves:
- `logic/state_flags.rpy` — `item_*` booleans (inventory), per-contact `contato_*` (unlocked at all) and `disponivel_*` (reachable right now) booleans.
- `logic/state_time.rpy` — the in-game clock (`game_hour`, `game_minute`, `show_clock`) with `set_time()` / `advance_minutes()` helpers.
- `logic/state_progress.rpy` — `progresso_roteiro`, `nivel_estresse`, `energia_diaria`, plus chat runtime state (`chat_history`, `user_input`, `is_waiting`, `server_response`). `logic/state_player.rpy` holds the remaining player-scoped defaults.
- `logic/friendship.rpy` — `amizade_*` floats (0–10) per character (friendship/affinity).
- `data/characters.rpy` — `Character()` objects and sprite `image` mappings; `data/character_names.rpy` — character display names (`NOME_*`) and colors (`COR_*`). Reusable sprite-position transforms (`left_zoom`, `center_zoom`, `right_zoom`, etc.) live in `game/ui/styles/sprite_transforms.rpy`. Always reference names via the `NOME_*` defines, never hardcode "Emily"/"Lucas".

### Two flag layers gate the phone/chat
This is the non-obvious core mechanic. Each contact has BOTH a `contato_<id>` (have you met them — show in the contacts grid) and a `disponivel_<id>` (can you message them *now*) flag. Scenes flip `disponivel_*` at their top to model "you can't text someone who's in the same room" (e.g. `scene_11_almoco_equipe` sets all to `False`; `scene_13_retorno_casa_sem3` sets all to `True`; `scene_14` sets a mix). In the contacts UI, an unavailable contact is rendered grayed-out and non-clickable. When editing a scene, call `set_available(...)` (in `logic/state_flags.rpy`) at the label start to declare who is physically present — it resets all `disponivel_developer_*` and enables only the ids passed (`set_available('all')` = everyone). Exceptions: `scene_5`/`scene_7` keep partial inline blocks; doutora availability is set by explicit lines in `scene_21`.

Helpers (in `game/logic/`, called from scenes via `$`):
- `add_contact("developer_ai")` — unlocks a contact (sets `contato_developer_ai = True`, adds to the `contacts` set, notifies). [`logic/friendship.rpy`]
- `add_friendship_point("developer_ai", amount)` / `get_friendship_point(id)` — adjust/read `amizade_*` (clamped 0–10). [`logic/friendship.rpy`]
- `friendship_color(level)` — bar color for a friendship level, used by the contacts UI. [`logic/friendship.rpy`]
- `add_to_inventory("notebook")` — sets the matching `item_*` flag. [`logic/inventory.rpy`]

Contact/character ids are the canonical keys used everywhere (`developer_ai`, `developer_requirements`, `developer_coding`, `developer_management`, `developer_quality`, `developer_project`, `developer_security`, `developer_test`, `doutora_1`, `doutora_2`). Adding a new contact means touching all layers: a `Character`/image in `data/characters.rpy` plus `NOME_*`/`COR_*` in `data/character_names.rpy`, `contato_*`/`disponivel_*` defaults (`logic/state_flags.rpy`, plus the id in the `DEVELOPERS` list there) and `amizade_*` (`logic/friendship.rpy`), and an `AMIGOS_DATA` entry (with `assistant_id` and `desc`) in `data/friends_data.rpy` listed in `CONTACTS_ORDER`. The contacts grid is data-driven (a `contact_tile` loop), so no per-contact UI block is needed.

### UI mechanics (`game/scripts/mechanics/` screens; styles in `game/ui/styles/`)
- `inventory_screen.rpy` — the "Mochila" screen + persistent `inventory_button` (gated by `inventory_enabled`). Data-driven: `ITENS_ORDER`/`ITENS_DESC` + a `inventory_tile(item_id)` loop. The phone (`item_celular`) opens `contacts_screen`.
- `contacts_screen.rpy` — the contacts grid. Data-driven: `for cid in CONTACTS_ORDER: use contact_tile(cid)`; an available tile sets `amigo_selecionado` and jumps to `chat_amigo`.
- `clock_screen.rpy` — `top_right_clock` overlay driven by `game_hour`/`game_minute`/`show_clock`.
- `chat_screen.rpy` — chat UI only (`screen chat_with_backend` + `label chat_amigo`); the HTTP client is in `python/chat_backend.rpy`, styles in `ui/styles/chat_styles.rpy`.

### AI chat: live external backend (load-bearing)
The chat is NOT scripted dialogue — it calls a remote LLM-assistant service over HTTP, split across files:
- `data/friends_data.rpy` — `AMIGOS_DATA` maps each contact id -> `{name, portrait, assistant_id, desc}` (`asst_...` ids); also bootstraps `current_assistant_id` (intentionally NOT a `default`).
- `python/chat_backend.rpy` — the client: `is_web()`, the single `normalize_resposta()`, the desktop (`requests` + `threading`) and web (`js.fetch`) sends, and `send_and_update_chat()`. The endpoint is built from one `define BACKEND_BASE_URL`.
- `python/user_id.rpy` — `generate_user_id()` (`init -1`) + `default user_id`, called from `label start`.
- `mechanics/chat_screen.rpy` — `label chat_amigo` looks up the friend, sets `current_assistant_id`, calls `add_friendship_point(amigo_selecionado, 1)`, and shows `screen chat_with_backend`.
- Desktop runs the request on a background `threading.Thread`; `is_web()` branches to a JS `fetch` path (web currently returns a "download the game" notice). `requests` relies on the SDK's bundled Python (not vendored).

When touching chat, keep the desktop/web split and the single `normalize_resposta` (the backend may return a string, a JSON list, or a stringified list). Remote responses arrive at runtime and are NOT statically translatable.

### Notes
- A root `.gitignore` ignores `*.rpyc`/`*.rpymc`, `game/cache/`, `game/saves/`, the diagnostics, and `.playwright-mcp/`. After renaming/moving `.rpy` files, delete stale `.rpyc` (or Force Recompile) before linting — orphaned compiled copies cause phantom "line id appears twice" errors.
- Audio: `define music_*` in `game/data/audio_library.rpy` (music files under `game/audio/music/`, SFX in `game/audio/effects/`); backgrounds in `game/data/backgrounds.rpy`; item images in `game/data/items.rpy`.
- i18n: UI/Python/`define` strings are wrapped in `_()` (dialogue/menus auto-extract); a language selector is in Preferences. Regenerate the locale skeleton with `renpy.exe "<project>" translate english` (the `tl/` tree is gitignored); `NOME_*` are translatable. Remote chat text is not statically translatable.
- Analysis + execution plans (migration to 8.5.3, this refactor, critical bugs) live in `docs/` — see `docs/README.md`.
