# Execução da evolução jogável

Plano: docs/superpowers/plans/2026-11-09-evolucao-jogo.md.
TodoWrite indisponível; este registro mantém a retomada.

- [completed] Implementar estado determinístico, regras do projeto e testes.
- [completed] Integrar exploração, evidências, quadro de requisitos e calendário.
- [completed] Integrar campanha, compromissos, incidente e finais.
- [completed] Gerar e integrar artes, feedback visual e HUD.
- [completed] Criar portfólio HTML interativo.
- [completed] Executar testes, inspeção visual, revisão independente e corrigir achados.
- [in_progress] Gerar pacote, integrar main e limpar worktree/temporários.

Decisões: campanha nova acessível pelo menu principal, preservando a demo guiada e seus saves. A campanha é o fluxo recomendado; não duplicar seu estado nos campos da demo. Ren'Py 8.5.3 reutilizado de C:/Users/Felipe/.cache/requirements-whisper-tools. Trabalho e testes no X:. Baseline lint: 145 blocos, 21 menus, 39 telas, sem erros.

Revisão prévia das tarefas: estado produz evidências/plano/compromisso para telas e roteiro; telas apenas chamam ações do estado; roteiro muda fases e confirma compromissos; arte é consumida pelas telas; portfólio documenta somente o integrado. Nenhum trabalhador altera arquivos de outro. Testes humanos continuam pendentes; expansão técnica pode prosseguir por autorização expressa, sem afirmar validação de diversão.

## Contrato compartilhado — campanha independente da demo

Estado em `scripts/project_state.rpy`; prefixo `lab_`. UI em `scripts/lab_screens.rpy`; narrativa em `scripts/lab_story.rpy`. Coordenador integra menu, assets e portfólio. Todos leem este contrato antes de alterar interfaces.

Defaults: `lab_active=False`, `lab_phase="investigation"`, `lab_evidence=[]`, `lab_links={}`, `lab_plan=[]`, `lab_initial_plan=[]`, `lab_commitment=""`, `lab_commitment_status="open"`, `lab_delivery="not_delivered"`, `lab_events=[]`, `lab_sidequest=False`, `lab_repaired=False`, `lab_test_results={}`, `lab_location="laboratorio"`, `lab_feedback=""`, `lab_revision=1`, `lab_return_milestone="reunião de sexta-feira da próxima semana"`, `lab_commitment_owner="Júlio e Carlos"`.

Evidências: `sheets` duas planilhas conflitantes; `preparation` ficha de dez minutos do microscópio confirmada pela técnica; `interview` relato Carlos; `offline` motivo da planilha paralela (opcional). Regras/itens: `conflict` custo 2; `preparation` custo 1 depende de conflict; `clarity` calendário legível custo 1. Capacidade 3. Ligações esperadas conflict→sheets, preparation→preparation, clarity→interview. Pesquisa de integração é uma rodada dedicada escolhida na negociação, que adia a execução do plano; não ocupa simultaneamente pontos do pacote.

Funções do estado (UI e roteiro podem assumir estas assinaturas):
- `lab_reset()` limpa campanha, ativa e mantém preferências.
- `lab_collect(evidence_id)` registra pista única e feedback, offline ativa sidequest.
- `lab_link(rule_id, evidence_id)` registra ligação, retorna bool de suporte adequado; hipótese inadequada permanece visível e pode ser refeita.
- `lab_toggle_plan(item_id)` adiciona/remove respeitando capacidade/dependência, devolve bool e feedback.
- `lab_plan_cost()` retorna int; `lab_plan_ready()` bool (não vazio e dependências válidas).
- `lab_confirm_commitment(option)` aceita base_primeiro/investigar_agora; congela plano inicial e registra acordo, mantendo entrega pendente.
- `lab_mark_delivery()` marca a chegada à bancada na sexta-feira, apenas na rota base; roteiro chama depois da demonstração.
- `lab_run_test(case_id)` casos overlap/adjacent/preparation/other, registra resultado e feedback; não muda regras. Retorna str.
- `lab_repair()` acrescenta conflict+preparation preservando itens anteriores e snapshot inicial; revision=2, delivery=revision_pending, repaired=True. A revisão é uma rodada adicional; resultados antigos são limpos. `lab_mark_delivery()` exige os dois resultados de regressão antes de marcar repaired. Evidência e compromisso permanecem.
- `lab_reservation_result(existing, candidate, rules)` tuplas (equipment,start,end), rules lista IDs; allowed/conflict/preparation_required/invalid. Intervalos semiabertos e preparação apenas microscópio.
- `lab_ending()` retorna reliable/waiting/repaired/unowned; prioridade waiting se não entregue, repaired se reparado, reliable se proteção+preparação entregues, unowned caso restante. Não executar testes nunca cria bug.
- `lab_objective()` texto da próxima ação por fase.

Constantes de conteúdo: `LAB_EVIDENCE` dict id→dict title/source/text; `LAB_ITEMS` dict id→dict title/cost/description; `LAB_CASES` dict id→dict title. Estado mantém funções autocontidas; dados novos precisam ser comunicados.

Telas públicas (call screen retorna token ou True):
- `lab_map()` Return local laboratorio/equipe/conversa ou continue (apenas três evidências essenciais obtidas); possui sidebar objetivos.
- `lab_location_screen(location)` Return evidence id ou back; hotspot e lista equivalentes; mostra itens desse local (laboratorio:sheets/preparation; equipe:offline; conversa:interview).
- `lab_board()` seleciona origem/destino, chama lab_link; Return True quando conflict e preparation corretamente ligados. Permite abandonar hipótese errada e rever fonte. Arrastar é adicional, seleção acessível é obrigatória.
- `lab_planning()` chama toggle; Return True com plano válido, mostra capacidade e dependências.
- `lab_demo()` chama run_test, Return True após pelo menos um teste; casos e resultados visíveis, reserva anterior preservada.
- `lab_journal()` modal Show/Hide, evidências/projeto/compromissos sem interceptar digitação.
- `lab_hud()` fase, objetivo e pasta de trabalho; somente se lab_active.
- `lab_final(ending)` Return replay/menu/legacy; resultado, causa e pendências.

Labels públicas: `lab_campaign` inicia; narrativa chama telas acima. `lab_campaign_end` limpa HUD e retorna ao menu. Root criará entrada Start("lab_campaign") na navegação. Fases investigation/definition/planning/negotiation/delivery/followup/ending. Narrativa deve mostrar passagem de dias explícita e decisões reparáveis, sidequest e cenas de desenvolvimento/adoção. Nenhuma pista essencial só aparece na sidequest.

Assets previstos root: `images/bg/laboratorio.png`, `images/bg/quarto_ilustrado.png`, `images/characters/sabrina/return.png` (variação de roupa), `images/items/evidence_sheet.png`. Até disponíveis, UI pode usar bg escritorio e formas nativas; versões finais devem consumir as artes.

## Rodadas de implementação e revisão

- Sol/high: três implementadores para estado, interface e narrativa; Astra/high: revisão ampla e conferência das correções.
- TDD: label da campanha falhou antes da implementação; regras novas falharam nos testes Python antes de serem implementadas.
- Rodada 1: demo antiga preservada; falhas novas revelaram retorno de valor em ações Function fechando telas indevidamente, e HUD sobreposta. Corrigidos retornos e camadas; testes verificam permanência da tela.
- Rodada 2: rolagem necessária para pista fora da área visível e seletor textual inadequado em elementos estáticos. Não aumentar timeout para ocultar a causa.
- Revisão Astra: preservação do plano inicial e itens no reparo; pesquisa separada da entrega; calendário legível com efeito visível; memória condicionada à investigação real. Entrega só é marcada na chegada à bancada.
- Rodada 3: campanha, estado, demos anteriores e capturas de jornada passaram. Os seletores de textos estáticos da suíte de interface foram corrigidos. Testes Python: 15 passaram.
- Portfólio: abas por clique/teclado, simulador causal, modal de imagem e Esc verificados em navegador; sem overflow horizontal em 390px, imagens locais carregadas.

Arte final do objeto: `images/items/notebook_evidencias.png`, usada no inventário; não será gerada evidence_sheet adicional. Fontes da campanha usam texto e dados do motor.

- Verificação final: 53 casos e 388 asserções no motor, 15 testes de estado em Python e 15 casos/77 asserções na variante compacta passaram. Lint sem erros.
- Pacote Windows gerado e verificado com seu próprio runtime: 50 casos e 387 asserções passaram, com três capturas opcionais desativadas. Hash e limites em `VALIDACAO-CAMPANHA.md`.
