# F5 — Piloto automático e correção de erros de execução

Executor: agente Claude (general-purpose), 2026-11-02. Interrompido pelo limite semanal de uso e retomado com a
mensagem "O limite de uso foi reiniciado: continue a tarefa F5 de onde parou (...)". Resultado: commit `e86d11b`.
Prompt usado:

---

Você vai verificar em execução real, e corrigir, as três rotas de um jogo Ren'Py 8.5.3 em português.

Worktree git (branch `integracao-rotas`): `C:/Users/Felipe/Documents/GitHub/Renpy Projects/Requirements-Whisper-integracao` (W). Não faça commit; o orquestrador commita. Nenhum outro agente está editando o jogo agora.

Contexto: leia W/CLAUDE.md, W/docs/plans/2026-11-02-integracao-rotas.md, W/game/script.rpy, W/game/data/routes.rpy, W/game/logic/learning.rpy, W/game/scripts/mechanics/learning_activities.rpy e os testes existentes em W/game/tests/ (sintaxe testsuite/testcase do Ren'Py 8.5.3; rode com `& "C:\Program Files (x86)\renpy-8.5.3-sdk\lib\py3-windows-x86_64\python.exe" "C:\Program Files (x86)\renpy-8.5.3-sdk\renpy.py" "<W>" test --savedir "<W>/.test-saves" --report-detailed`; lint com o mesmo python e `"<W>" lint`). O conteúdo das rotas Startup (game/story/rota_startup/, 18 cenas) e Corporativo (game/story/rota_corporativo/, 18 cenas) e as mudanças nas cenas da saúde foram escritos por agentes e só passaram no lint: nada foi executado. Erros de execução prováveis: nomes Python inexistentes em `$`/`if`, chamadas de função com assinatura errada, atributos de imagem inexistentes, `show expression` com caminho errado, interpolação `[x]` de variável inexistente, `%` mal escapado, telas chamadas (`call screen`) que travam, `renpy.input` no exercício de escrita, laços de menu sem saída.

Tarefa:
1. Construa um piloto automático de teste que percorra cada rota do início ao fim do epílogo, sem rede: entra pela escolha da vaga em scene_1 (ou faz o mínimo equivalente: preenche perfil, define chosen_job e segue o fluxo real de `start`), avança todas as falas, escolhe opções nos menus, fecha telas chamadas (contacts_screen, notebook, resumo, chat se abrir), preenche o exercício de escrita e o planejamento. Pode ser um testcase do Ren'Py, um modo de autopiloto ativado por variável de ambiente (ex.: config.auto_choice_delay + auto-avanço + callbacks que dispensam telas), ou uma combinação; mantenha o código de autopiloto fora do jogo distribuído (em game/tests/, que o build exclui) e sem efeito no jogo normal.
2. Rode cada rota várias vezes com escolhas diferentes: pelo menos (a) sempre a primeira opção, (b) sempre a última, (c) 3 sementes aleatórias. As escolhas devem incluir distratores (para exercitar a revisão orientada) e os ramos alternativos (ex.: 'descansar'/'virar a noite' na scene_18 da saúde, os dois acordos de negociação, coberturas 0/1/2 no planejamento).
3. Para cada erro (traceback.txt, exceção no relatório, travamento/timeout), encontre a causa e corrija no arquivo certo, mantendo o texto e a intenção. Não renomeie labels nem variáveis existentes. Rode de novo até as três rotas chegarem ao epílogo sem erro em todos os modos.
4. Verifique também ao fim de cada execução: a cena de final da rota calculou um resultado ("excelente"/"bom"/"ok"), o resumo do epílogo mostra registros N de 8 coerentes com a rota, e nenhuma imagem ausente foi exibida (registre chamadas ao callback de imagem ausente / `_missing_image`; arte de personagem pode estar como placeholder "arte pendente" em 2 arquivos: st_mobile/serious e co_legado/serious, o que é esperado).
5. Deixe como testes permanentes em game/tests/ pelo menos um teste de ponta a ponta por rota (modo determinístico) que rode em tempo razoável, e mantenha os 22 testes existentes passando. Lint 100% limpo no fim.

Responda com: como o piloto funciona e como rodá-lo; tabela por rota e modo (chegou ao epílogo? final calculado? registros); lista de cada bug encontrado com arquivo:linha, causa e correção; resultado final do lint e dos testes.
