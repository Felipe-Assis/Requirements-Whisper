# Processo: prompts de cada etapa

Este projeto foi construído por orquestração de agentes. Um orquestrador (Claude Code) planejou, dividiu o
trabalho, revisou e commitou; agentes Claude escreveram design, código e texto; o Codex (OpenAI) gerou as imagens
e fez revisões de código somente leitura. Esta pasta guarda os prompts usados, para repetir, auditar ou adaptar
qualquer etapa.

- `workflows/`: scripts de orquestração com vários agentes em paralelo. Cada script contém, no próprio código, o
  prompt completo de cada agente (procure as strings passadas para `agent(...)`).
- `agentes/`: prompts de agentes lançados sozinhos.
- `codex/`: prompts das revisões de código feitas pelo Codex (`codex exec -s read-only`).
- Arte: prompts, referências e ferramentas em [`../arte/`](../arte/README.md).

Os caminhos absolutos nos prompts (`C:/Users/Felipe/...`, `X:/dev-tmp/...`) são os desta máquina; ajuste ao repetir.
Worktrees citadas (`Requirements-Whisper-integracao`, `Requirements-Whisper-evolucao`) eram cópias de trabalho
temporárias deste repositório.

## Integração da demo e rotas longas (2026-11-02)

Plano: [`../plans/2026-11-02-integracao-rotas.md`](../plans/2026-11-02-integracao-rotas.md).

| Etapa | Executor | Prompt | Saída | Commit |
|---|---|---|---|---|
| F0 Mapeamento das duas versões | 4 agentes Claude em paralelo | `workflows/01-f0-mapeamento.js` | mapa de cenas, mecânicas, assets e ideias da demo (não versionado) | — |
| F1 Bíblias das rotas | 2 agentes Claude | `workflows/02-f1-biblias-rotas.js` | `docs/rotas/*.md`, `docs/rotas/*-assets.json` | `144e1b6` |
| F2a Infraestrutura de rotas | 1 agente Claude | `agentes/03-f2a-infraestrutura-rotas.md` | despacho, `ROUTES`, personagens, contatos, chat offline | `c2028d3` |
| F2b Mecânicas da demo + estado das rotas | 3 agentes Claude | `workflows/04-f2b-mecanicas-e-estado.js` | `logic/learning.rpy`, telas, testes, `estado_*.rpy` | `f7e6a35` |
| F3 Arte das rotas novas | Codex (`imagegen`) | `../arte/prompts/rotas-novas-2026-11-02.json` | 12 personagens, 9 fundos, 8 telas | `e9bbf72` |
| F4 Conteúdo | 10 escritores + 2 revisores + 2 agentes na saúde (Claude) | `workflows/05-f4-conteudo.js` | 36 cenas novas, mudanças na saúde | `14cf489` |
| F5 Piloto automático | 1 agente Claude | `agentes/06-f5-piloto-automatico.md` | `game/tests/autopiloto.*`, correção do chat | `e86d11b` |
| Revisão da infraestrutura | Codex, só leitura | `codex/revisao-infraestrutura.txt` | relatório (1 achado corrigido na F6a) | — |
| F6a UI/UX e design | 1 agente Claude | `agentes/07-f6a-ui-ux-design.md` | telas, escolhas, artefatos, acessibilidade | `113f45f` |
| Revisão da interface | Codex, só leitura | `codex/revisao-interface.txt` | relatório (achados avaliados, sem mudança) | — |
| Documentação, build | orquestrador | — | `CLAUDE.md`, `README.md`, `tools/build-windows.ps1` | `113f45f`, `7066ed1` |

## Evolução (a partir de 2026-11-02)

Plano: [`../plans/2026-11-02-evolucao.md`](../plans/2026-11-02-evolucao.md).

| Etapa | Executor | Prompt | Saída |
|---|---|---|---|
| Brainstorming | orquestrador (skill `product-management:brainstorm`) | — | posições no plano de evolução |
| Comparação de estilos | Codex | `../arte/prompts/comparacao-estilos-2026-11-02.json` | página de escolha; estilo C aprovado |
| Pesquisa Live2D/3D | 1 agente Claude com busca web | `agentes/09-pesquisa-live2d-3d.md` | `../pesquisa/live2d-3d.md` |
| E1 Design das intermissões | 1 agente de sistemas + 3 de rota (Claude) | `workflows/10-e1-design-intermissoes.js` | `docs/design/*.md` |
| E3 Regeração no estilo C | Codex | `../arte/prompts/estilo-c.json` | elenco e fundos no estilo C |

As próximas etapas acrescentam suas linhas aqui, com o arquivo do prompt, quando forem executadas.
