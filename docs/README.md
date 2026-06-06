# Documentação — Requirements Whisper

Análises técnicas do jogo (migração de engine, arquitetura e bugs críticos), geradas em 2026-06-06.

## Índice

- [migracao-renpy-8.5.3.md](migracao-renpy-8.5.3.md) — migração Ren'Py **8.3.7 → 8.5.3**: esforço, o que muda, passo a passo (o que baixar/modificar), vantagens e desvantagens.
- [reestruturacao-projeto.md](reestruturacao-projeto.md) — avaliação de **reestruturação/reorganização** (o que vale a pena, o que é over-engineering, restrições do modelo Ren'Py).
- [pontos-criticos.md](pontos-criticos.md) — **pontos que podem quebrar o jogo** (P1–P7) e ações de correção, com verificação adversarial (inclui evidência do lint 8.5.3).
- [plans/2026-06-06-refatoracao-manutenibilidade.md](plans/2026-06-06-refatoracao-manutenibilidade.md) — **plano de refatoração** (manutenibilidade + i18n), 6 fases. **← prioridade atual.**
- [plans/2026-06-06-migracao-e-reestruturacao.md](plans/2026-06-06-migracao-e-reestruturacao.md) — plano de **migração** 8.3.7→8.5.3 + correções (executar **depois** da refatoração).

## Por onde começar

Ordem decidida: **(1) refatorar** com `plans/...-refatoracao-manutenibilidade.md` (corrige os pontos
críticos pelo caminho), depois **(2) migrar** para 8.5.3 com `plans/...-migracao-e-reestruturacao.md`.
Referências de apoio: `pontos-criticos.md` e `migracao-renpy-8.5.3.md`.
