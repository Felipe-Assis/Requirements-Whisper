export const meta = {
  name: 'rw-entender-versoes',
  description: 'Mapeia historia, mecanicas e assets da versao longa e as ideias reaproveitaveis da demo curta',
  phases: [{ title: 'Mapear', detail: '4 leitores em paralelo, somente leitura' }],
}

const LONG = 'C:/Users/Felipe/Documents/GitHub/Renpy Projects/Requirements-Whisper-integracao'
const DEMO = 'C:/Users/Felipe/Documents/GitHub/Requirements-Whisper'
const RULES = `Regras: somente leitura, nao edite nem crie arquivos em nenhum repositorio. Responda em portugues, de forma objetiva. Cite caminhos relativos e numeros de linha quando util. Contexto: existem duas versoes de um jogo educacional Ren'Py sobre engenharia de software/requisitos. A versao LONGA fica em ${LONG} (raiz com game/; leia ${LONG}/CLAUDE.md e tambem C:/Users/Felipe/Documents/GitHub/Renpy Projects/Requirements-Whisper/docs/restricoes-e-decisoes.md). A versao CURTA (demo) fica em ${DEMO}. Na longa, so a rota de vaga "saude" existe; "startup" e "corporativo" voltam para a escolha da vaga. O objetivo futuro e usar a longa como base, trazer ideias da curta e escrever versoes longas das rotas startup e corporativo.`

const SCENE = {
  type: 'object',
  properties: {
    scenes: { type: 'array', items: { type: 'object', properties: {
      label: { type: 'string' }, file: { type: 'string' }, act: { type: 'string' },
      summary: { type: 'string', description: '3-6 frases do que acontece' },
      se_topic: { type: 'string', description: 'conteudo de engenharia de software ensinado' },
      characters: { type: 'array', items: { type: 'string' } },
      backgrounds_and_images: { type: 'array', items: { type: 'string' } },
      music_sfx: { type: 'array', items: { type: 'string' } },
      choices: { type: 'string', description: 'menus, o que muda (amizade, flags, inventario, pontos)' },
      state_touched: { type: 'array', items: { type: 'string' } },
      domain_specificity: { type: 'string', enum: ['generica', 'parcial', 'especifica_saude'] },
      reuse_notes: { type: 'string', description: 'o que precisaria mudar para servir a rota startup (app de financas para estudantes) e corporativo (sistema legado de atendimento/chamados)' },
      word_estimate: { type: 'integer' },
      problems: { type: 'string', description: 'bugs, inconsistencias, trechos fracos, se houver' },
    }, required: ['label', 'file', 'summary', 'se_topic', 'characters', 'backgrounds_and_images', 'choices', 'domain_specificity', 'reuse_notes'] } },
    overall_notes: { type: 'string' },
  },
  required: ['scenes', 'overall_notes'],
}

const MECH = {
  type: 'object',
  properties: {
    mechanics: { type: 'array', items: { type: 'object', properties: {
      name: { type: 'string' }, files: { type: 'array', items: { type: 'string' } },
      how_it_works: { type: 'string' }, route_coupling: { type: 'string', description: 'quanto depende do dominio saude / dos personagens atuais' },
    }, required: ['name', 'files', 'how_it_works', 'route_coupling'] } },
    endings_and_scoring: { type: 'string', description: 'como scene_21 e o epilogo decidem final, conquistas, condicoes de vitoria (inventario, amizade etc.)' },
    characters: { type: 'array', items: { type: 'object', properties: {
      id: { type: 'string' }, name: { type: 'string' }, role: { type: 'string' },
      sprite_files: { type: 'array', items: { type: 'string' } }, expressions: { type: 'array', items: { type: 'string' } },
      health_specific: { type: 'boolean' },
    }, required: ['id', 'name', 'role', 'sprite_files', 'health_specific'] } },
    assets: { type: 'object', properties: {
      backgrounds: { type: 'array', items: { type: 'object', properties: { file: { type: 'string' }, used: { type: 'boolean' }, generic: { type: 'boolean' }, note: { type: 'string' } }, required: ['file', 'used', 'generic'] } },
      items: { type: 'array', items: { type: 'string' } },
      audio_summary: { type: 'string' },
      unused_or_missing: { type: 'string' },
    }, required: ['backgrounds', 'items', 'audio_summary', 'unused_or_missing'] },
    visual_style: { type: 'string', description: 'descricao precisa do estilo dos sprites e fundos (traço, paleta, sombreamento, proporcao, resolucao em px, fundo transparente, enquadramento), apos abrir e ver pelo menos 4 sprites e 4 fundos com a ferramenta Read' },
    style_reference_files: { type: 'array', items: { type: 'string' }, description: 'caminhos absolutos de 3-5 imagens melhores para servir de referencia de estilo' },
    risks: { type: 'string' },
  },
  required: ['mechanics', 'endings_and_scoring', 'characters', 'assets', 'visual_style', 'style_reference_files', 'risks'],
}

const DEMOSCHEMA = {
  type: 'object',
  properties: {
    ideas: { type: 'array', items: { type: 'object', properties: {
      name: { type: 'string' }, demo_files: { type: 'array', items: { type: 'string' } },
      what_it_is: { type: 'string' }, pedagogical_value: { type: 'string' },
      fit_with_long: { type: 'string', description: 'onde e como encaixaria na versao longa, respeitando store global, nao renomear variaveis/labels, lint limpo' },
      cost: { type: 'string', enum: ['baixo', 'medio', 'alto'] },
      recommendation: { type: 'string', enum: ['portar', 'adaptar', 'descartar'] },
      reason: { type: 'string' },
    }, required: ['name', 'demo_files', 'what_it_is', 'fit_with_long', 'cost', 'recommendation', 'reason'] } },
    tests_and_build: { type: 'string', description: 'como funcionam os testes Ren\'Py (testcase) e o build Windows da demo e o que seria preciso para leva-los a versao longa' },
    demo_route_content: { type: 'string', description: 'resumo do conteudo especifico das rotas Startup e Empresa legada da demo (problemas, regras, criterios, casos limite, negociacao, transferencia) que pode semear as rotas longas' },
  },
  required: ['ideas', 'tests_and_build', 'demo_route_content'],
}

phase('Mapear')
const [a, b, c, d] = await parallel([
  () => agent(`${RULES}\n\nTarefa: leia por inteiro as cenas da versao LONGA dos atos 1 e 2: ${LONG}/game/script.rpy e todos os arquivos em ${LONG}/game/story/act1_descoberta/ e ${LONG}/game/story/act2_levantamento/. Produza o mapa cena a cena.`, { label: 'historia:atos-1-2', schema: SCENE }),
  () => agent(`${RULES}\n\nTarefa: leia por inteiro as cenas da versao LONGA dos atos 3, 4, 5 e epilogo: todos os arquivos em ${LONG}/game/story/act3_especificacao/, act4_arquitetura/, act5_implementacao/ e epilogue/. Produza o mapa cena a cena.`, { label: 'historia:atos-3-5', schema: SCENE }),
  () => agent(`${RULES}\n\nTarefa: mapeie mecanicas, estado, finais/pontuacao, personagens e assets da versao LONGA: ${LONG}/game/logic/, data/, scripts/mechanics/, python/, ui/, screens.rpy, options.rpy, e as pastas ${LONG}/game/images e ${LONG}/game/audio. Para saber se um asset e usado, faca grep pelos nomes nos .rpy. Abra com Read pelo menos 4 sprites de personagens e 4 fundos para descrever o estilo visual com precisao (isso vai orientar a geracao de novas imagens no mesmo estilo). Informe a resolucao (px) dos sprites e fundos (pode usar python para ler o cabecalho PNG).`, { label: 'mecanicas-e-assets', schema: MECH }),
  () => agent(`${RULES}\n\nTarefa: analise a versao CURTA (demo) em ${DEMO}: README.md, docs/, scripts/*.rpy, screens.rpy, tests/*.rpy, tools/build-windows.ps1. Liste as ideias e mecanismos (atividades com feedback e revisao, planejamento, negociacao, aplicacao final com escrita livre e autoavaliacao, notebook de registros, perfil/emblema, acessibilidade, testes automatizados, build) e avalie o que vale portar para a versao LONGA. Para avaliar o encaixe, leia tambem ${LONG}/CLAUDE.md e passe os olhos nas cenas da longa que tratam dos mesmos temas (ex.: scene_6_entrevista_stakeholders, scene_7_avaliacao_requisitos, scene_12_especificacao_requisitos, scene_21_avaliacao_final).`, { label: 'ideias-da-demo', schema: DEMOSCHEMA }),
])
return { atos12: a, atos35: b, mecanicas: c, demo: d }
