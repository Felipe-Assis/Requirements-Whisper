export const meta = {
  name: 'rw-e5-conteudo-intermissoes',
  description: 'Alinha dados do mapa, escreve o conteudo das intermissoes, encaixa mecanicas/pistas/energia nas cenas, revisa e verifica com o autopiloto',
  phases: [
    { title: 'Escrita', detail: 'alinhamento do mapa + 9 escritores + 3 encaixes' },
    { title: 'Revisao', detail: '1 revisor por rota' },
    { title: 'Verificacao', detail: 'autopiloto nas 3 rotas' },
  ],
}
const E = 'C:/Users/Felipe/Documents/GitHub/Renpy Projects/Requirements-Whisper-evolucao'
const PY = 'C:\\Program Files (x86)\\renpy-8.5.3-sdk\\lib\\py3-windows-x86_64\\python.exe'
const RP = 'C:\\Program Files (x86)\\renpy-8.5.3-sdk\\renpy.py'
const BASE = `Projeto: jogo educacional Ren'Py 8.5.3 em portugues do Brasil ("The Requirements Whisperer"), worktree git ${E} (branch evolucao). Nao faca commit. Temporarios em X:/dev-tmp/requirements-whisper/evolucao/e5/<sua-tarefa>/, nunca no repositorio.
Leia antes: ${E}/CLAUDE.md; ${E}/docs/plans/2026-11-02-evolucao.md; ${E}/docs/design/sistemas-intermissoes.md; ${E}/docs/design/mapa-cidade.md (decisao final do mapa: cidade unica inspirada no Rio, lugares e sub-locais, deslocamento, folga de +30 min nas semanas 2-8 da Saude e da Startup, lugar "aterro" ACEITO no Corporativo, a cidade e o Rio com liberdade artistica e a fala "transito do Rio de Janeiro" da scene_21 fica). O motor ja implementado: ${E}/game/logic/intermissao.rpy, ${E}/game/logic/energia.rpy, ${E}/game/scripts/mechanics/intermissao_fluxo.rpy, ${E}/game/scripts/mechanics/mapa_screen.rpy, ${E}/game/data/intermissoes_*.rpy, ${E}/game/data/mapa_cidade.rpy, as mecanicas ${E}/game/scripts/mechanics/ambiguidade.rpy e rastreabilidade.rpy com dados em game/data/*_dados.rpy, e o destaque de fala/selos de menu em game/screens.rpy (screen choice(items, tipo=None)) e game/ui/styles/. Entenda as convencoes de nomes de label de conteudo do motor (ele chama labels de conteudo por convencao e usa fala provisoria quando o label nao existe) lendo esses arquivos antes de escrever.
Regras: nao renomeie labels/variaveis/ids existentes; cada variavel nova com um unico default (no seu proprio arquivo); portugues natural, frases curtas, sem jargao gratuito, voz de cada personagem como nas cenas existentes; evite flexao de genero do jogador; nunca [ ou { literais em falas; nada obrigatorio para aprender fica so na intermissao. Edite SOMENTE os arquivos atribuidos a voce; outros agentes trabalham em paralelo no mesmo diretorio. Lint: & "${PY}" "${RP}" "${E}" lint ; testes: & "${PY}" "${RP}" "${E}" test --savedir "X:/dev-tmp/requirements-whisper/evolucao/e5/test-saves-<sua-tarefa>". Rode lint/testes perto do fim; se o erro for de arquivo alheio ou .rpyc ("defined twice"), espere e rode de novo antes de concluir que e seu.`

const ROTAS = [
  { id: 'saude', nome: 'Saude', p: 'saude', cenas: `${E}/game/story/act1_descoberta/, act2_levantamento/, act3_especificacao/, act4_arquitetura/, act5_implementacao/ e epilogue/` },
  { id: 'startup', nome: 'Startup', p: 'st', cenas: `${E}/game/story/rota_startup/` },
  { id: 'corporativo', nome: 'Corporativo', p: 'co', cenas: `${E}/game/story/rota_corporativo/` },
]
const BLOCOS = [{ s: '1 a 3', n: [1, 2, 3] }, { s: '4 a 6', n: [4, 5, 6] }, { s: '7 e 8 e os 5 encontros do arco de mentoria', n: [7, 8, 'mentoria'] }]

const ALINHA = `${BASE}

SUA TAREFA (alinhamento dos dados do mapa e do motor). Arquivos seus: game/data/mapa_cidade.rpy, game/data/intermissoes_saude.rpy, intermissoes_startup.rpy, intermissoes_corporativo.rpy, game/logic/intermissao.rpy, game/logic/energia.rpy, game/scripts/mechanics/mapa_screen.rpy, game/scripts/mechanics/intermissao_fluxo.rpy, game/tests/intermissoes.rpy. O agente que escreveu o mapa anotou na secao 8 de docs/design/mapa-cidade.md onde os dados provisorios divergem (ids de lugar como casa/escritorio_saude/campus/metro/tijuca, coordenadas pelo centro numa base 1920, caminhos das transicoes em images/mapa/transicoes/<meio>.png, icones atendendo/observando/conversando). Alinhe os dados ao documento: ids e nomes dos 12 lugares, coordenadas na base 2560x1440 (ajuste a tela para essa base, escalando para 1920x1080), sub-locais por pessoa nos baloes, tabela de deslocamento, meio de transporte, tela de transicao e sons por trajeto, os 8 icones e o marcador, o lugar aterro no Corporativo a partir da semana 2, a folga de +30 min nas semanas 2-8 da Saude e da Startup e a linha "No caminho: X min" no resumo. Os caminhos de imagem devem ser exatamente os destinos de ${E}/docs/arte/prompts/mapa-saidas.json (a arte esta sendo gerada agora e entra depois; enquanto nao existir, os placeholders do motor continuam funcionando). Mantenha os 63 testes passando e ajuste/acrescente testes de intermissoes para os dados novos. NAO escreva falas de conteudo e NAO edite cenas de historia.
Responda com o que mudou, a lista final de ids de lugar e de icone, as convencoes de label de conteudo que os escritores devem usar (confirme lendo o codigo) e lint/testes.`

const escritor = (r, b) => `${BASE}

SUA TAREFA: escrever o CONTEUDO das intermissoes da rota ${r.nome}, semanas/partes ${b.s}, conforme ${E}/docs/design/intermissoes-${r.id}.md (siga a secao de cada semana: agenda, acoes, resultado, falas-chave, pistas, registros bonus, mentoria, falas com energia baixa, meta de palavras) e o mapeamento de lugares de ${E}/docs/design/mapa-cidade.md. Crie SOMENTE arquivos novos em ${E}/game/story/intermissoes/${r.id}/ (um por semana, ex.: s01.rpy, s02.rpy, e mentoria.rpy se for o seu bloco), contendo os labels de conteudo com os NOMES EXATOS que o motor chama (leia game/logic/intermissao.rpy, game/scripts/mechanics/intermissao_fluxo.rpy e game/data/intermissoes_${r.id}.rpy para descobrir a convencao e a lista de acoes de cada semana; outro agente esta alinhando ids de LUGAR nesses dados agora, mas os ids de pessoa/acao e a convencao de label nao mudam). Cada label de conteudo: falas curtas e vivas (2 a 8 blocos por acao, mais para mentoria e observar), show/hide dos sprites com os transforms existentes, sem scene (o motor cuida do fundo do lugar) a menos que o documento peca, e terminando com return. Use as funcoes do motor para pistas, registros bonus, energia e mentoria exatamente como o motor define (nao dupla-conte recompensas que o motor ja aplica: verifique o que o motor faz sozinho). Leia 2 cenas da rota em ${r.cenas} para pegar a voz dos personagens. Rode o lint no fim. Responda com os labels criados por semana, palavras aproximadas, e qualquer acao do documento que o motor nao suporta.`

const encaixe = (r) => `${BASE}

SUA TAREFA: encaixar as novidades nas CENAS da rota ${r.nome} (${r.cenas}), conforme ${E}/docs/design/intermissoes-${r.id}.md (em especial as secoes de pontos de insercao, pistas, energia, mecanicas e a lista de edicoes por arquivo, se houver) e os ajustes de horario de ${E}/docs/design/mapa-cidade.md. Arquivos seus: somente as cenas da rota ${r.nome}${r.id === 'saude' ? ' (scene_1_quarto e scene_2_escritorio NAO, sao comuns)' : ` e ${E}/game/story/rota_${r.id}/estado_${r.id}.rpy`}. Faca:
1. Inserir call im_intermissao(N) from _<label_unico> nos 8 pontos definidos (com o rotulo from unico para saves), redesenhando fundo/musica/sprites depois quando o documento indicar.
2. Chamar a Caca a ambiguidade e a Rastreabilidade nos pontos definidos para esta rota, com os ids de dados que estao em game/data/ambiguidade_dados.rpy e rastreabilidade_dados.rpy, e as consequencias posteriores (o bug que aparece ou nao, falas para quem achou e quem nao achou a lacuna).
3. Usar as pistas exatamente onde o documento define (pista_lembrar antes do menu, ou opcao extra condicional em menu social/negociacao), sem mexer na contagem de decisao()/acertos.
4. Eventos de energia nas cenas indicadas e as falas alternativas com energia baixa; falas de conclusao do arco de mentoria onde o documento pede (sem mexer nas regras de final).
5. Selos de tipo nos menus existentes da rota: menu decisoes pedagogicas com tipo "trabalho", sociais "conversa", negociacao "negociacao" (use a sintaxe de argumentos de menu que game/screens.rpy aceita - confira em screens.rpy).
6. Ajustes de set_time pedidos pelo documento do mapa.
Rode lint e testes no fim (o autopiloto de ponta a ponta precisa continuar chegando ao epilogo). Responda com a lista de edicoes por arquivo e lint/testes.`

const revisor = (r) => `${BASE}

SUA TAREFA: revisar a rota ${r.nome} depois que o conteudo das intermissoes (${E}/game/story/intermissoes/${r.id}/) e os encaixes nas cenas (${r.cenas}) foram escritos por outros agentes. Voce pode editar esses arquivos. Verifique e corrija: continuidade entre intermissoes e cenas (o que o jogador viu, horarios, quem esta onde, pistas usadas depois do prazo ou antes de existirem); vozes dos personagens; nenhum conteudo obrigatorio para aprender preso a intermissao; precisao tecnica e pedagogica das falas; portugues natural; ausencia de [ { soltos; todo label que o motor chama existe (compare com game/data/intermissoes_${r.id}.rpy e a convencao do motor; nenhuma fala provisoria do motor deve sobrar para esta rota); mecanicas chamadas com ids validos. Rode lint e testes. Responda com problemas encontrados e corrigidos (arquivo), contagem de palavras das intermissoes e pendencias.`

const verificador = `${BASE}

SUA TAREFA (verificacao final em execucao real): rode o autopiloto (${E}/game/tests/autopiloto.ps1 e os testes de ponta a ponta; leia ${E}/game/tests/autopiloto.rpy) nas 3 rotas, nos modos primeira, ultima, 3 sementes aleatorias, e um modo que pula todas as intermissoes. Saidas e relatorios em X:/dev-tmp/requirements-whisper/evolucao/e5/verificacao/. Para cada erro de execucao, travamento, imagem/audio ausente (exceto arte do mapa ainda nao entregue, que deve cair nos placeholders sem erro), label de conteudo faltando (fala provisoria do motor aparecendo) ou laco, encontre a causa e corrija no arquivo certo, mantendo texto e intencao. Confirme: toda rota chega ao epilogo; o modo que pula intermissoes tem 8 de 8 registros; finais calculados; tempo e energia nunca negativos; nenhuma pista usada sem ter sido obtida. Lint 100% limpo e todos os testes passando no fim. Responda com a tabela rota x modo, bugs corrigidos (arquivo:linha, causa, correcao), lint e testes.`

phase('Escrita')
const [alinha, escritas, encaixes] = await Promise.all([
  agent(ALINHA, { label: 'alinhamento:mapa', phase: 'Escrita' }),
  parallel(ROTAS.flatMap(r => BLOCOS.map(b => () => agent(escritor(r, b), { label: `escrita:${r.id}:${b.n[0]}`, phase: 'Escrita' })))),
  parallel(ROTAS.map(r => () => agent(encaixe(r), { label: `encaixe:${r.id}`, phase: 'Escrita' }))),
])
phase('Revisao')
const revisoes = await parallel(ROTAS.map(r => () => agent(revisor(r), { label: `revisor:${r.id}`, phase: 'Revisao' })))
phase('Verificacao')
const verif = await agent(verificador, { label: 'verificacao:autopiloto', phase: 'Verificacao' })
return { alinha, escritas, encaixes, revisoes, verif }
