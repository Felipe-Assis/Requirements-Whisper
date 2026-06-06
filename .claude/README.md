# Requirements-Whisper — Índice de Agentes Claude Code

## Agentes disponíveis

| Agente | Gatilho / Quando usar |
|--------|----------------------|
| `renpy-lint-doctor` | Verificar uma mudança Ren'Py, diagnosticar crash/red-screen, rodar o lint, interpretar `traceback.txt` |
| `renpy-reference-validator` | Validar referências que o lint não pega: `jump`/`call` a labels inexistentes, `show <tag> <attr>` vs `characters.rpy`, caminhos de imagem/áudio, consistência de ids de contato |
| `refactor-restructure-agent` | Executar o plano de refatoração de manutenibilidade (`docs/plans/2026-06-06-refatoracao-manutenibilidade.md`): mover cenas para `story/`, data-driven para `contact_tile`, centralizar URL do backend |
| `renpy-migration-853-agent` | Migrar para Ren'Py 8.5.3: threading do chat, `full_restart` no replay, zoom/oversampling, recompilação Python 3.12 |
| `chat-backend-agent` | Mudar URL do backend, novo `assistant_id` para um contato, diagnosticar chat travando / "está digitando…" |
| `screen-ui-agent` | Mudar layout/estilo de telas, data-driven para o `contact_tile`, consolidar o bloco de contato duplicado, barra de amizade |
| `scene-author-agent` | Escrever ou editar uma cena, novo menu de escolha, ligar uma cena nova no chain de `call` em `script.rpy` |
| `i18n-tl-agent` | Fase 5 i18n: embrulhar strings em `_()`, gerar `tl/english/`, seletor de idioma |

## Sobre agentes vs. habilidades

Os **agentes** acima são executores isolados de contexto — invoque-os explicitamente para tarefas focadas. Não há skills neste repositório (skills são companions passivos de edição, relevantes para projetos maiores com múltiplos subsistemas).

## Gate de qualidade

> **Não há suite de testes automatizados.** O único gate é: `renpy.exe "<raiz do projeto>" lint` + playthrough manual. Os arquivos `log.txt`, `errors.txt` e `traceback.txt` na raiz do repositório são **desatualizados** — regenere rodando o jogo, nunca confie nas cópias commitadas.

## Referências

- Convenções do projeto: [`.claude/CONVENTIONS.md`](./CONVENTIONS.md) (§A–§I)
- Instruções gerais de sessão: [`CLAUDE.md`](../CLAUDE.md) na raiz do repositório
- Planos de refatoração e migração: [`docs/plans/`](../docs/plans/)
