# F2a — Infraestrutura de rotas

Executor: agente Claude (general-purpose), 2026-11-02, worktree `Requirements-Whisper-integracao`, branch
`integracao-rotas`. Resultado: commit `c2028d3`. Prompt usado:

---

Você vai implementar a infraestrutura de rotas (fase F2a) de um jogo Ren'Py 8.5.3 em português.

Repositório de trabalho (worktree git, branch `integracao-rotas`): `C:/Users/Felipe/Documents/GitHub/Renpy Projects/Requirements-Whisper-integracao` (abreviado como W). Edite só dentro de W. Não faça commit; o orquestrador revisa e commita.

Leia antes, por inteiro:
- W/CLAUDE.md (arquitetura, restrições, regra de threading do chat, lint).
- W/docs/plans/2026-11-02-integracao-rotas.md (plano e decisões).
- W/docs/rotas/startup.md e W/docs/rotas/corporativo.md: só as seções de elenco/personagens (nomes, cores, descrições, respostas de chat offline), lista de cenas, quem está presente por cena e variáveis. Também W/docs/rotas/*-assets.json.
- O código atual de: game/script.rpy, game/story/act1_descoberta/scene_1_quarto.rpy e scene_2_escritorio.rpy, game/logic/*.rpy, game/data/*.rpy, game/scripts/mechanics/*.rpy, game/python/chat_backend.rpy, game/ui/styles/*.rpy.

Restrições obrigatórias:
- NÃO renomeie nenhum label, variável, id de personagem ou arquivo de imagem existente (quebra saves). Mudar a localização de código é permitido.
- Toda variável nova tem exatamente um `default`. Tabelas que usam NOME_*/COR_* ficam em `init python` prioridade 0 (não `python early`).
- A rota saúde deve se comportar exatamente como hoje (mesmas variáveis, mesmo set_available para os 8 developers, mesmos contatos), exceto pelo limite de amizade no chat descrito abaixo.
- Regra de threading do chat: a thread nunca escreve no store; só o dreno na main thread altera chat_history.
- Ao final, lint 100% limpo. Rode: `& "C:\Program Files (x86)\renpy-8.5.3-sdk\lib\py3-windows-x86_64\python.exe" "C:\Program Files (x86)\renpy-8.5.3-sdk\renpy.py" "<W>" lint` (PowerShell) e leia W/errors.txt se houver. Antes de lintar depois de mover/criar arquivos, apague .rpyc órfãos se aparecer erro de "defined twice".

O que implementar:
1. **Registro de rotas** em game/data/routes.rpy: `ROUTES` com uma entrada por rota ("saude", "startup", "corporativo"): nome da empresa/produto (da bíblia), lista `team` (ids da equipe, na saúde os 8 developer_*), `stakeholders` (na saúde doutora_1, doutora_2), `contacts_order` (na saúde é o CONTACTS_ORDER atual, inalterado). Funções auxiliares: `current_route()` (retorna chosen_job ou "saude" se vazio), `route_team()`, `route_contact_ids()`, `route_contacts_order()`. Acrescente `default chosen_job = ""` (hoje não existe default).
2. **12 personagens novos** (st_mentora, st_techlead, st_mobile, st_qualidade, st_ceo, st_estudante, co_mentora, co_legado, co_dev, co_qualidade, co_supervisora, co_solicitante), seguindo todas as camadas descritas em CLAUDE.md "Adding a new contact": Character com NOME_*/COR_* (nomes e cores das bíblias; Rosângela é "Rosângela Arruda"), imagens `image <id> <pose> = "images/characters/<id>/<pose>.png"` para as poses do assets.json (neutral, thinking, serious; stakeholders neutral e thinking) e `portrait`, mais aliases para os atributos usados nas cenas existentes (positive, enthusiastic, confident, concentrated -> neutral; para stakeholders, serious -> thinking), `contato_*`/`disponivel_*`/`amizade_*` defaults, entradas em AMIGOS_DATA com `assistant_id: None`, `desc` e `offline`: a lista das 8 respostas roteirizadas da bíblia (strings com `_()`, sem `[`/`{` não escapados). Os arquivos de imagem ainda não existem: crie PLACEHOLDERS PNG (use Python com Pillow: sprites RGBA 1024x1536 com silhueta cinza translúcida e o texto "arte pendente" + id; retratos 520x430) em todos os caminhos referenciados, e grave a lista exata desses arquivos em W/docs/rotas/placeholders.txt (um caminho relativo a game/ por linha). Nunca sobrescreva uma imagem que já exista.
3. **set_available por rota**: hoje reseta `disponivel_*` dos 8 developers e liga só os ids passados ('all' = todos). Generalize para resetar os ids de `route_contact_ids()` da rota atual (na saúde continua resetando só os 8 developers, exatamente como hoje; as doutoras continuam controladas à mão). 'all' liga todos da rota.
4. **Contatos por rota**: contacts_screen itera `route_contacts_order()` em vez de CONTACTS_ORDER. Nada muda visualmente na saúde.
5. **Chat offline**: quando o contato tem `assistant_id` None, o chat não usa rede: ao enviar, acrescenta a mensagem do jogador e uma resposta da lista `offline` daquele personagem (rotacionando; guarde o índice num `default chat_offline_idx = {}`), na main thread, sem `is_waiting` travado. Personagens com assistant_id continuam usando o backend como hoje.
6. **Limite de amizade no chat**: hoje `chat_amigo` dá +1 de amizade a cada abertura, o que torna os finais fáceis de farmar. Passe a dar +1 só na primeira conversa com cada contato desde o último `set_available` (guarde os ids num `default chat_amizade_dada = set()`, esvaziado dentro de set_available). Vale para todas as rotas.
7. **Despacho por rota**: em game/script.rpy, depois de `call scene_1_quarto`, `if chosen_job == "startup": call rota_startup from _rota_startup` / `elif chosen_job == "corporativo": call rota_corporativo from _rota_corporativo` / `else:` com as chamadas atuais da saúde exatamente como estão (mesmos `from`). O epílogo continua sendo chamado depois, para todas. Em scene_2_escritorio, troque o ramo que faz `jump scene_1_quarto` para startup/corporativo por `return` (a cena da saúde segue igual), já que agora cada rota tem sua chegada. Garanta que scene_1 não seja reexecutada.
8. **Cadeias e arquivos de cena das rotas**: crie game/story/rota_startup/rota_startup.rpy com `label rota_startup:` chamando, em ordem, as 18 labels da bíblia (st_01_chegada ... st_18_lancamento) com `from _<label>`, e `return`. Idem game/story/rota_corporativo/rota_corporativo.rpy com as 18 labels co_*. Crie um arquivo por cena (game/story/rota_startup/st_01_chegada.rpy etc.) contendo só um stub: `label <nome>:` + uma linha de narração "[Cena em construção: <título>]" + `return`. Os escritores vão substituir esses stubs depois; não escreva o conteúdo das cenas.
9. Em scene_1_quarto, enriqueça minimamente o texto das vagas 2 e 3 com os nomes da empresa/produto das bíblias (Trocado; Grupo Vértice/SGC), sem mudar `chosen_job`.

Ao terminar, responda com: lista de arquivos criados/alterados, as APIs novas (nomes e assinaturas) que os escritores de cena devem usar, o resultado do lint (copie o resumo) e qualquer decisão ou risco.
