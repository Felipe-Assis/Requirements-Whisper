# F6a — Passe de UI, UX e design visual

Executor: agente Claude (general-purpose), 2026-11-02. O usuário pediu Claude para UI, UX e design. Resultado:
commit `113f45f` (mais o ajuste do orquestrador nos artefatos da cena 18 da saúde). Prompt usado:

---

Você vai fazer o passe de UI, UX e design visual de um jogo Ren'Py 8.5.3 em português (visual novel educacional "The Requirements Whisperer"). Trate isto como trabalho de design de verdade: olhe as telas renderizadas, julgue hierarquia, legibilidade, espaçamento, consistência com o tema do jogo e acessibilidade, e ajuste.

Worktree git (branch `integracao-rotas`): `C:/Users/Felipe/Documents/GitHub/Renpy Projects/Requirements-Whisper-integracao` (W). Não faça commit; o orquestrador commita. Nenhum outro agente edita arquivos do jogo agora (o orquestrador só mexe em CLAUDE.md, AGENTS.md, README.md e docs/).

Contexto obrigatório: W/CLAUDE.md; W/docs/plans/2026-11-02-integracao-rotas.md; W/game/gui.rpy e W/game/screens.rpy (tema atual: cores, fontes, tamanhos); W/game/ui/styles/*; as telas novas em W/game/scripts/mechanics/notebook_screen.rpy, learning_activities.rpy, inventory_screen.rpy, contacts_screen.rpy, chat_screen.rpy e a tela resumo_rota em W/game/story/epilogue/scene_epilogo_conquistas_final.rpy; os testes em W/game/tests/ (inclusive o piloto automático autopiloto.rpy e ponta_a_ponta.rpy, que você pode reaproveitar para chegar às telas). Princípios de design herdados da demo (sem a paleta dela): fundo opaco atrás de texto, estado escrito além da cor, foco visível por teclado, nada essencial só em cor/som/animação.

Capturas: use a instrução `screenshot` dos testes do Ren'Py (ou renpy.screenshot) em uma suíte de inspeção desligada por padrão (enabled False ou variável de ambiente), salvando em `X:/dev-tmp/requirements-whisper/integracao-rotas/capturas/` (não salve capturas dentro do repositório). Abra as imagens com a ferramenta Read para avaliar. Capture antes e depois de cada mudança relevante.

O que avaliar e melhorar:
1. Telas novas: notebook de registros (com 0, 4 e 8 registros), exercício de escrita (entrada do requisito, entrada do critério, revisão do rascunho com texto longo, autoavaliação), atividade de planejamento, resumo do epílogo, preferências/acessibilidade, Mochila, grade de contatos com os 6 contatos das rotas novas, chat offline. Em tamanho normal e com "texto maior" ligado. Consistência com o restante da interface (mesma família de fontes, cores e molduras do gui), hierarquia clara, nada cortado ou sobreposto, barras de rolagem usáveis, foco de teclado visível, estados escritos.
2. Composição das cenas das rotas novas: capture pelo menos 6 quadros representativos (ex.: st_01 com a equipe, st_05 entrevista com 2-3 pessoas, st_13 com artefato de tela, co_01, co_05, co_17 na sala de servidores) e verifique posições dos sprites (left/center/right_zoom), sobreposição de personagens, cortes, tamanho e legibilidade dos artefatos de tela (images/artifacts/st_*.png, co_*.png) e se os fundos novos combinam com os antigos. Ajuste transforms/posições ou o tamanho de exibição dos artefatos quando necessário (pode criar transforms novos em ui/styles/; não altere os existentes usados pela saúde). Não reescreva o texto das cenas; mudanças em cenas só em linhas de show/hide/at/with.
3. Corrija este bug (achado por revisão independente): em learning_activities.rpy o label exercicio_escrita reinicia `escrita_marcas` para quatro False ao entrar, então ao retomar um rascunho as marcas da autoavaliação se perdem e uma escrita confirmada volta a ficar pendente. Restaure as marcas salvas ao retomar (persistindo por eid de forma compatível com saves).
4. Ao fim, rode lint (`& "C:\Program Files (x86)\renpy-8.5.3-sdk\lib\py3-windows-x86_64\python.exe" "C:\Program Files (x86)\renpy-8.5.3-sdk\renpy.py" "<W>" lint`) e a suíte de testes (`... "<W>" test --savedir "<W>/.test-saves"`): lint 100% limpo e todos os testes passando (27 hoje). Não deixe arquivos temporários dentro do repositório.

Responda com: problemas de UI/UX encontrados (com captura antes/depois por caminho), mudanças feitas por arquivo, o que você decidiu não mudar e por quê, lint e testes.
