export const meta = {
  name: 'rw-f2b-estado',
  description: 'F2b mecanicas genericas da demo + arquivos de estado das rotas Startup e Corporativo',
  phases: [{ title: 'Infra', detail: '3 agentes, arquivos disjuntos' }],
}
const W = 'C:/Users/Felipe/Documents/GitHub/Renpy Projects/Requirements-Whisper-integracao'
const DEMO = 'C:/Users/Felipe/Documents/GitHub/Requirements-Whisper'
const LINT = `& "C:\\Program Files (x86)\\renpy-8.5.3-sdk\\lib\\py3-windows-x86_64\\python.exe" "C:\\Program Files (x86)\\renpy-8.5.3-sdk\\renpy.py" "${W}" lint`
const COMUM = `Projeto: jogo educacional Ren'Py 8.5.3 em portugues. Worktree git em ${W} (branch integracao-rotas). Leia ${W}/CLAUDE.md, ${W}/docs/plans/2026-11-02-integracao-rotas.md, ${W}/game/data/routes.rpy (registro ROUTES e funcoes current_route(), route_data(), route_team(), route_contact_ids(), route_contacts_order()), ${W}/game/logic/state_flags.rpy (set_available por rota) e ${W}/game/logic/friendship.rpy.
Restricoes: nao renomeie labels/variaveis/ids existentes; cada variavel nova tem um unico default; tabelas com NOME_* em init python prioridade >= 0; nao faca commit; no fim o lint deve estar 100% limpo (PowerShell: ${LINT}; leia ${W}/errors.txt se houver). Outros dois agentes trabalham ao mesmo tempo no mesmo diretorio em arquivos diferentes: edite SOMENTE os arquivos atribuidos a voce. Se o lint acusar erro em arquivo de outro agente, ignore-o e relate.

CONTRATO DE API (a F2b implementa; os arquivos de estado das rotas e os escritores de cena usam):
- default registros = set(); funcao registrar(rid): marca o registro rid da rota atual como descoberto e mostra renpy.notify("Anotado no notebook: <titulo>"); ignora ids repetidos.
- ROUTES[rota]["records"] = lista de dicts {"id": str, "title": str (com _()), "text": str (com _())} - 8 por rota.
- ROUTES[rota]["achievements"] = lista de dicts {"id": str, "title": str, "desc": str, "var": nome de variavel booleana do store} (rotas novas) ou {"id","title","desc","inv": item da lista inventario} (saude). Funcao achievement_unlocked(a) -> bool.
- ROUTES[rota]["final"] = nome de uma funcao (string) que devolve "excelente"/"bom"/"ok" para a rota.
- default aprendizagem = {}; funcao decisao(did, adequada): registra a PRIMEIRA tentativa da decisao did (True = escolha adequada sem apoio; False = precisou de revisao orientada); chamadas repetidas com o mesmo did nao sobrescrevem.
- label exercicio_escrita(eid, pedido): escrita livre de um requisito e de um criterio de aceitacao com revisao do rascunho e autoavaliacao em 4 perguntas (quem age, condicoes, resultado observavel, excecoes); guarda em default escritas = {} como escritas[eid] = {"req","crit","checks": int 0-4,"status": "confirmado"|"pendente"}; se chamado de novo com o mesmo eid, retoma o rascunho. Texto livre saneado ({ e [ escapados).
- label atividade_planejamento(pid, itens, necessarios, capacidade=2): menu em loop para escolher itens ate a capacidade, com adicionar/retirar e conferir; feedback por cobertura; devolve a cobertura (0..len(necessarios)) em _return e guarda em default planejamentos = {}.
- As rotas novas registram seus records/achievements/final em init 2 python, dentro do proprio arquivo de estado, mutando ROUTES (ex.: ROUTES["startup"]["records"] = [...]).`

const ROTA = r => `${COMUM}

SUA TAREFA: criar o arquivo de estado da rota ${r.nome}: ${W}/game/story/rota_${r.id}/estado_${r.id}.rpy (arquivo NOVO; e o unico que voce cria/edita). Leia por inteiro ${W}/docs/rotas/${r.id}.md e liste todas as variaveis, flags, conquistas, registros do notebook e a regra do final que a biblia define. No arquivo:
1. Um default para cada variavel da rota citada na biblia (prefixo ${r.p}_), com valor inicial correto (contadores 0, flags False, escolhas "" ou None).
2. Em init 2 python: ROUTES["${r.id}"]["records"] (os 8 registros da biblia, ids ${r.p}_reg_*), ROUTES["${r.id}"]["achievements"] (conquistas da biblia, cada uma com "var" apontando para a variavel booleana correspondente) e ROUTES["${r.id}"]["final"] = "${r.p}_final_grade".
3. Funcoes: ${r.p}_amizade_equipe() (soma amizade_* de route_team("${r.id}")), ${r.p}_conquistas() (quantas conquistas pedagogicas), ${r.p}_final_grade() (regra da biblia), e helpers pequenos que varias cenas da biblia vao usar (por ex. pontuacao de acerto), cada um com docstring curta.
4. No topo do arquivo, um comentario curto listando a API para os escritores de cena (variaveis e funcoes, e o que cada cena deve setar).
Nao implemente registrar/decisao/exercicio_escrita/atividade_planejamento: sao da F2b. Se o lint falhar porque registrar ainda nao existe, nao chame registrar no seu arquivo (so dados). Responda com um resumo da API criada e o resultado do lint.`

const F2B = `${COMUM}

SUA TAREFA (F2b): implementar as mecanicas genericas trazidas da demo curta (${DEMO}). Leia na demo: scripts/notebook.rpy, scripts/functions.rpy, scripts/inventory_screen.rpy, scripts/scene_3_planejamento.rpy, scripts/scene_5_sintese.rpy, screens.rpy (telas transfer_input, transfer_review, rw_accessibility, preferencias, say/choice/history com texto maior), tests/*.rpy, tools/build-windows.ps1 e DESIGN.md (so os principios). Adapte ao estilo e as telas da versao longa; nao copie a paleta da demo.
Arquivos que voce pode criar/editar: game/logic/learning.rpy (novo: registros, decisao, escritas, planejamentos e o contrato acima), game/scripts/mechanics/notebook_screen.rpy (novo), game/scripts/mechanics/learning_activities.rpy (novo: labels exercicio_escrita e atividade_planejamento e suas telas), game/scripts/mechanics/inventory_screen.rpy, game/screens.rpy, game/options.rpy, game/data/routes.rpy (somente para acrescentar records/achievements/final da SAUDE), game/story/act1_descoberta/scene_1_quarto.rpy (somente o perfil), game/story/epilogue/scene_epilogo_conquistas_final.rpy, game/tests/ (novo), tools/build-windows.ps1 (novo).
Itens:
1. Contrato de API completo (acima), com docstrings.
2. Notebook: o tile notebook da Mochila (hoje NullAction) abre a tela de registros da rota atual: lista com titulo, "registrado"/"pendente", contador "N de 8", viewport rolavel, fecha com Esc/N e botao. Estado escrito alem da cor.
3. Saude: defina ROUTES["saude"]["records"] com 8 registros tirados do conteudo das cenas da saude (ciclo de vida, elicitacao por entrevista, classificacao de requisitos, casos de uso, inspecao de requisitos, arquitetura e trade-offs, testes e seguranca, implantacao), ids saude_reg_*; ROUTES["saude"]["achievements"] com as conquistas que hoje existem como strings em inventario e sao realmente concedidas (verifique por grep: selo_codigo_sem_bugs, conquista_bug_vuln, medalha_estudioso, badges da scene_18_2 etc.); ROUTES["saude"]["final"] apontando para uma funcao que reproduz a regra atual da scene_21 (nao altere a scene_21). NAO acrescente chamadas registrar() nas cenas da saude: outro agente fara isso depois; apenas deixe os ids prontos.
4. Perfil (scene_1_quarto): nome opcional (vazio vira "Alex"), saneado (exclude "{}[]\\\\" no input e remocao de { e [), deixe de pedir a idade (mantenha o default player_age), mantenha o genero. Nao mexa no resto da cena.
5. Acessibilidade em screens.rpy: preferencias para texto maior (persistent, aumenta fala, nome, escolhas e historico), texto instantaneo e desligar transicoes; textos das preferencias em portugues; Mochila operavel por teclado (foco, descricao ao focar, fecha com Esc/I). Nao quebre o seletor de idioma existente.
6. Epilogo: alem do que ja existe (replay com renpy.full_restart, creditos, sair), mostre um resumo da rota jogada: nome da empresa, conquistas obtidas (achievement_unlocked), registros N de 8, decisoes adequadas sem apoio vs com apoio (aprendizagem), escritas confirmadas, e uma frase honesta de que o jogo nao certifica dominio. Use uma tela rolavel. Nao reative o bloco comentado de depoimentos.
7. Testes no motor em game/tests/*.rpy (sintaxe testsuite/testcase do Ren'Py 8.5.3, como na demo), excluidos do build (build.classify em options.rpy, junto com docs/ e tools/). Casos minimos: despacho de cada rota (setar chosen_job e chegar ao primeiro label de cada rota), notebook abre/fecha e conta registros, registrar/decisao nao duplicam, exercicio_escrita guarda e retoma, atividade_planejamento calcula cobertura, chat offline responde sem rede, set_available por rota. Rode-os: & "C:\\Program Files (x86)\\renpy-8.5.3-sdk\\lib\\py3-windows-x86_64\\python.exe" "C:\\Program Files (x86)\\renpy-8.5.3-sdk\\renpy.py" "${W}" test --savedir "${W}/.test-saves" --report-detailed (confira a sintaxe exata nos testes da demo) e garanta que .test-saves esteja no .gitignore.
8. tools/build-windows.ps1 adaptado da demo para este layout (raiz com game/): lint, distribute --package win, confere que o ZIP tem o .exe e nao tem tests/docs/saves, grava SHA256 em dist/ (dist/ no .gitignore). Nao precisa rodar o build agora.
Responda com: arquivos criados/alterados, a API final (assinaturas exatas), resultado do lint e dos testes (numeros), decisoes e riscos.`

phase('Infra')
const r = await parallel([
  () => agent(F2B, { label: 'F2b:mecanicas' }),
  () => agent(ROTA({ id: 'startup', p: 'st', nome: 'Startup' }), { label: 'estado:startup' }),
  () => agent(ROTA({ id: 'corporativo', p: 'co', nome: 'Corporativo' }), { label: 'estado:corporativo' }),
])
return { f2b: r[0], startup: r[1], corporativo: r[2] }
