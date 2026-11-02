export const meta = {
  name: 'rw-e1-design',
  description: 'Design de jogo das intermissoes, tempo/energia, novas mecanicas e conteudo por rota',
  phases: [
    { title: 'Sistemas', detail: 'GDD de intermissoes, tempo, energia, mecanicas novas e UI' },
    { title: 'Rotas', detail: 'conteudo das intermissoes e mecanicas por rota' },
  ],
}
const E = 'C:/Users/Felipe/Documents/GitHub/Renpy Projects/Requirements-Whisper-evolucao'
const BASE = `Projeto: jogo educacional Ren'Py 8.5.3 em portugues ("The Requirements Whisperer"), worktree git ${E} (branch evolucao). Nao faca commit e nao edite arquivos .rpy: esta etapa e so de design, em markdown. Escopo definido pelo usuario: jogo educacional que serve tanto para aula (objetivos de aprendizagem claros, sessoes que podem ser retomadas) quanto para jogar sozinho por diversao, completo do inicio ao fim. Live2D fica fora desta etapa.
Leia antes: ${E}/CLAUDE.md; ${E}/docs/plans/2026-11-02-evolucao.md (posicoes do brainstorming e plano aprovados pelo usuario); ${E}/docs/plans/2026-11-02-integracao-rotas.md; ${E}/game/script.rpy; ${E}/game/data/routes.rpy; ${E}/game/logic/learning.rpy; ${E}/game/logic/state_time.rpy; ${E}/game/logic/state_progress.rpy; ${E}/game/scripts/mechanics/learning_activities.rpy; ${E}/game/screens.rpy (tela choice e say).
Escreva em portugues simples e objetivo.`

phase('Sistemas')
const sistemas = await agent(`${BASE}

SUA TAREFA: escrever o documento de design de sistemas ${E}/docs/design/sistemas-intermissoes.md (crie a pasta). Ele sera a referencia para quem implementa (um agente Claude) e para quem escreve o conteudo de cada rota. Seja concreto: nomes de variaveis/labels/funcoes propostos (com prefixos que nao colidem com os existentes; nada existente e renomeado), formatos de dados, regras numericas, e o que entra no save.
Cubra:
1. Intermissoes: uma por semana em cada rota (8 por rota; a saude tem 22 cenas e as outras 18 - mapeie em que ponto da cadeia de cada rota cada intermissao entra, de preferencia antes do retorno para casa ou no fim do expediente de sexta; leia game/script.rpy e as cadeias game/story/rota_*/rota_*.rpy e os cards "Fim da Semana N" com grep para achar as semanas). Bloco de tempo (ex.: 180 min), custo das acoes (30/60/90), quantas cabem, teto de amizade por intermissao, o que acontece quando o tempo acaba. Garantia de que nada obrigatorio para aprender fica so na intermissao.
2. Mapa: tela por rota com 5 a 6 pontos de interesse (POI) comuns a semana e alguns que abrem depois; agenda dos personagens (quem esta em cada POI por semana), formato de dados por rota; o que o jogador ve (nome do POI, quem esta la por retrato e nome, custo em tempo, rotulo do tipo de acao); acessibilidade (teclado, estado escrito, nada so por cor).
3. Tipos de acao e recompensas: conversar (amizade), observar usuario (gera uma pista), estudar (registro bonus no notebook, alem dos 8), descansar (energia), ajudar alguem (amizade + pista tecnica). Pistas: conjunto no save; como uma pista libera uma opcao extra/melhor numa cena posterior (formato de menu condicional, sem quebrar decisao()). Arcos de mentoria: um por rota, em 4 a 5 encontros ao longo das intermissoes, com conclusao e uma conquista.
4. Tempo e energia: energia semanal visivel (0 a 10?), o que gasta (acoes intensas, virar a noite, horas extras citadas nas cenas) e recupera; efeito de energia baixa (menos acoes, falas diferentes), sem game over e sem punir aprendizado; relogio real usando set_time/advance_minutes existentes; HUD de tempo/energia (onde, quando aparece).
5. Novas mecanicas pedagogicas, reaproveitaveis nas 3 rotas com dados por rota: (a) Caca a ambiguidade: o jogador seleciona palavras vagas de um requisito e escolhe como torna-las verificaveis; formato de dados, regras de feedback e revisao orientada, registro em decisao(); (b) Rastreabilidade: ligar requisito -> criterio de aceitacao -> teste num quadro; um elo faltando vira o bug encontrado na semana de testes; formato de dados e interacao por mouse e teclado. Diga em que cena de cada rota cada uma entra (sugestao) e o tempo de jogo.
6. Ajustes de UI de dialogo: destacar quem fala (escurecer sprites que nao falam: proponha a tecnica no Ren'Py 8.5.3, ex.: Character(image=...) + config.speaking_attribute ou callback; avalie o efeito nas cenas que mostram sprites com show expression e nos personagens sem image=), alinhar nome e texto da fala, rotulo/icone por tipo de menu (trabalho, conversa, negociacao) usando argumentos de item de menu do Ren'Py, sem depender so de cor.
7. Vida nos personagens, degrau 1 da pesquisa ${E}/docs/pesquisa/live2d-3d.md: respiracao/balanco por ATL nos transforms de sprite, fundos com fit "cover", movimentos leves de camera. Especifique sem quebrar config.zoom_zaxis/old_show_expression.
8. Duracao: estimativa de minutos adicionados por rota; como manter sessoes de aula (pontos de parada claros por semana, salvar).
9. Testes: o que o autopiloto (game/tests/autopiloto.rpy) precisa aprender para atravessar mapa e mecanicas novas.
Responda com um resumo de 10 a 15 linhas das decisoes principais (o documento completo fica no arquivo).`, { label: 'gdd:sistemas', phase: 'Sistemas' })

phase('Rotas')
const ROTAS = [
  { id: 'saude', nome: 'Saude', docs: `${E}/docs/plans/2026-11-02-integracao-rotas.md e as cenas em ${E}/game/story/act*/ e epilogue/`, mentor: 'acompanhar um atendimento com a Dra. Nathalia (doutora_2) ou outro arco coerente com o elenco da saude' },
  { id: 'startup', nome: 'Startup', docs: `${E}/docs/rotas/startup.md e as cenas em ${E}/game/story/rota_startup/`, mentor: 'o grupo de beta testers da Bia (st_estudante) ou outro arco coerente' },
  { id: 'corporativo', nome: 'Corporativo', docs: `${E}/docs/rotas/corporativo.md e as cenas em ${E}/game/story/rota_corporativo/`, mentor: 'Jorge (co_legado) passando o conhecimento tacito do SGC antes de se aposentar' },
]
const rotas = await parallel(ROTAS.map(r => () => agent(`${BASE}

Leia tambem o documento de sistemas recem-escrito ${E}/docs/design/sistemas-intermissoes.md e siga-o a risca (formatos, regras, nomes). Resumo dele: ${sistemas}

SUA TAREFA: escrever ${E}/docs/design/intermissoes-${r.id}.md, o design de conteudo da rota ${r.nome}. Fontes da rota: ${r.docs} (leia as cenas que precisar para nao contradizer a historia). Inclua:
1. Os POIs da rota (5 a 6), cada um com nome, descricao visual detalhada para gerar a arte do mapa ilustrado e o icone (estilo: ilustracao com traco limpo, cores suaves, mesma familia dos fundos do jogo), e em que semana abre.
2. As 8 intermissoes: semana, ponto exato da cadeia (entre quais labels), horario, agenda (quem esta em cada POI), acoes disponiveis em cada POI com custo, resultado e falas-chave (resumo de 2 a 4 frases por acao e a meta de palavras), pistas geradas e EXATAMENTE onde cada pista e usada depois (arquivo, label, menu e o texto da opcao liberada ou da fala alterada), registros bonus do notebook (id, titulo, texto).
3. O arco de mentoria (${r.mentor}): 4 a 5 encontros, o que se aprende em cada um, conclusao e conquista (id, titulo, condicao).
4. Onde entram a Caca a ambiguidade e a Rastreabilidade nesta rota: cena, momento, dados completos (textos dos requisitos, palavras vagas, opcoes de reescrita com feedback; itens do quadro de rastreabilidade e o elo faltando que vira bug), coerentes com o conteudo ja existente da rota.
5. Efeitos de energia nesta rota (que cenas gastam, falas alternativas com energia baixa).
6. Estimativa de palavras e minutos adicionados.
Mantenha o tom e os personagens da rota. Nada obrigatorio para aprender fica so na intermissao. Responda com um resumo curto (POIs, arco, onde ficam as mecanicas, palavras estimadas).`, { label: `gdd:${r.id}`, phase: 'Rotas' })))
return { sistemas, rotas }
