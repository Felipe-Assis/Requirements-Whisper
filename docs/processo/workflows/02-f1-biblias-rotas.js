export const meta = {
  name: 'rw-biblias-rotas',
  description: 'Escreve a biblia narrativa e a especificacao de arte das rotas Startup e Corporativo',
  phases: [{ title: 'Biblias', detail: 'um agente por rota' }],
}
const W = 'C:/Users/Felipe/Documents/GitHub/Renpy Projects/Requirements-Whisper-integracao'
const MAPA = 'C:/Users/Felipe/AppData/Local/Temp/claude/C--Users-Felipe-Documents-GitHub-Requirements-Whisper/035474e1-2837-496d-9663-aefedeba92b6/scratchpad/mapa.json'
const DEMO = 'C:/Users/Felipe/Documents/GitHub/Requirements-Whisper'

const ROTAS = [
  { id: 'startup', prefix: 'st', titulo: 'Startup', vaga: 'vaga 2 em scene_1_quarto: desenvolvimento mobile em uma startup de tecnologia voltada para educacao financeira', semente: 'contexto Startup da demo (registro de gastos de estudantes: gasto lancado duas vezes, exclusao com confirmacao e total atualizado, cancelar a exclusao, importar gastos do banco como mudanca negociada, corrigir valor de gasto como escrita livre)', foco: 'MVP, Scrum/Kanban enxuto, metricas de produto, lojas de apps, LGPD de dados financeiros, Open Finance, pico de uso no inicio do semestre, demo day com investidores' },
  { id: 'corporativo', prefix: 'co', titulo: 'Corporativo', vaga: 'vaga 3 em scene_1_quarto: estagio em manutencao de sistemas legados em uma grande corporacao nacional', semente: 'contexto Empresa legada da demo (chamados de suporte: solicitante liga varias vezes porque ninguem registrou a mudanca, estado Resolvido com descricao da solucao, descricao vazia como caso limite, aviso por WhatsApp como mudanca negociada, reabrir chamado como escrita livre)', foco: 'manutencao evolutiva de legado, engenharia reversa e documentacao ausente, gestao de mudancas (janela, CAB), ITIL, RBAC atendente/supervisor/admin, trilha de auditoria, integracao com sistema antigo, migracao de dados, regressao' },
]

const SCHEMA = {
  type: 'object',
  properties: {
    bible_path: { type: 'string' },
    assets_path: { type: 'string' },
    characters: { type: 'array', items: { type: 'object', properties: { id: { type: 'string' }, name: { type: 'string' }, role: { type: 'string' } }, required: ['id', 'name', 'role'] } },
    scenes: { type: 'array', items: { type: 'object', properties: { label: { type: 'string' }, title: { type: 'string' } }, required: ['label', 'title'] } },
    notes: { type: 'string', description: 'duvidas, riscos ou decisoes tomadas que o orquestrador precisa saber' },
  },
  required: ['bible_path', 'assets_path', 'characters', 'scenes', 'notes'],
}

phase('Biblias')
const res = await parallel(ROTAS.map(r => () => agent(`Voce vai escrever a BIBLIA NARRATIVA da rota ${r.titulo} de um jogo educacional Ren'Py em portugues ("The Requirements Whisperer"), em que o jogador e estagiario e vive o ciclo de vida de um software ao longo de 8 semanas.

Leia antes:
- ${W}/docs/plans/2026-11-02-integracao-rotas.md (plano e decisoes; siga-as).
- ${W}/CLAUDE.md (arquitetura e mecanicas da versao longa).
- ${MAPA} (mapa cena a cena da rota saude existente, mecanicas, personagens, estilo visual e ideias da demo). Use as chaves atos12, atos35, mecanicas, demo.
- Leia por inteiro 3 cenas da saude para pegar tom, ritmo e uso das mecanicas: ${W}/game/story/act2_levantamento/scene_6_entrevista_stakeholders.rpy, ${W}/game/story/act3_especificacao/scene_12_especificacao_requisitos.rpy, ${W}/game/story/act4_arquitetura/scene_16_reuniao_gerenciamento.rpy.
- Da demo curta, leia ${DEMO}/scripts/scene_2_estagio.rpy, scene_3_planejamento.rpy, scene_4_negociacao.rpy e scene_5_sintese.rpy: a rota ${r.titulo} deve usar como semente o ${r.semente}, mas expandido para um projeto de 8 semanas.

Rota: ${r.titulo} (chosen_job == "${r.id}"), ${r.vaga}. Temas que a rota deve explorar alem do ciclo comum: ${r.foco}.

Restricoes de design (obrigatorias):
- Equipe propria com exatamente 4 pessoas (uma delas e a mentora/mentor que guia o jogador, papel equivalente a Emily na saude) e 2 stakeholders. Ids de personagem no formato ${r.prefix}_<papel> em minusculas ascii (ex.: ${r.prefix}_mentora). Elenco diverso (genero, idade, tom de pele, estilo), nomes brasileiros, sem repetir nomes da saude (Emily, Lucas, Joseph, Robert, Daiana, Heitor, Mateus, Cesar, Michelle, Nathalia) nem da demo (Sabrina, Carlos, Julio, Rodrigo).
- Esqueleto de 18 cenas, labels no formato ${r.prefix}_NN_<slug> (NN = 01..18), na ordem: Ato 1 Descoberta: 01 chegada e apresentacao da equipe e do produto; 02 reuniao inicial sobre o ciclo de vida adaptado ao contexto; 03 retorno para casa (fim da semana 1, abre contatos). Ato 2 Levantamento: 04 preparacao da entrevista; 05 entrevista com os 2 stakeholders (conflito entre eles, pedir um episodio concreto, esclarecer ambiguidade); 06 avaliacao/classificacao dos requisitos levantados; 07 momento social com parte da equipe; 08 retorno para casa (semana 2). Ato 3 Especificacao: 09 historias de usuario/casos de uso com criterio de aceitacao e caso limite; 10 almoco/social; 11 especificacao e inspecao de requisitos (defeitos ausente/ambiguo/inconsistente) terminando com escrita livre de um requisito e criterio com autoavaliacao; 12 retorno para casa (semana 3). Ato 4 Arquitetura e gestao: 13 decisao de arquitetura e modelagem de dados, com uma mudanca de escopo pedida por um stakeholder que precisa ser negociada (dois acordos validos, duas opcoes ruins com consequencia); 14 comemoracao/social da equipe; 15 reuniao de gestao com planejamento de capacidade (escolher 2 de 4 itens) e riscos. Ato 5 Implementacao: 16 codificacao com abordagem escolhida e code review por pull request; 17 testes e seguranca; 18 deploy e avaliacao final com os stakeholders (o final varia com amizade da equipe e conquistas). Depois vem o epilogo comum (nao escreva).
- Cada decisao pedagogica tem 1 opcao adequada e 2 distratores plausiveis, cada distrator com feedback que explica a consequencia concreta, e revisao orientada quando o jogador erra (sem punicao). Menus sociais mexem em amizade (add_friendship_point(id, 1)). Indique por cena as variaveis/flags/conquistas novas (nomes com prefixo ${r.prefix}_) e quem esta presente (para set_available).
- Defina 8 registros do notebook de aprendizagem (titulo + conteudo curto + em que cena e descoberto) e as conquistas da rota (cada uma alcancavel, com a cena e a condicao que a concede), alem da regra do final (excelente/bom/ok) proporcional a uma equipe de 4 (amizade 0-10 por pessoa).
- Para cada personagem: nome, papel, personalidade, jeito de falar, cor do nome (hex), descricao curta para o contato, 8 respostas roteirizadas de chat offline (mensagens curtas que fazem sentido em qualquer momento da rota, no tom do personagem, algumas com dica do conteudo), e uma descricao visual detalhada para gerar o sprite (idade aparente, tom de pele, cabelo, roupa, acessorios, postura) mais 3 poses: neutral (ou positive), thinking, serious - descreva a pose de cada uma (no estilo da arte existente, expressao vem mais da pose). Stakeholders podem ter 2 poses (neutral e thinking).
- Reuse fundos existentes sempre que fizer sentido (lista em mapa.json mecanicas.assets.backgrounds: quarto_manha/noite, cozinha_noite, transito_manha/tarde/noite, sala_reunioes_manha/tarde, empresa_cafe_manha/tarde, refeitorio_tarde, escritorio_interior_manha/tarde/noite/festa/vazio, empresa_exterior_manha/noite). Liste os fundos NOVOS necessarios (no maximo 6 por rota, contando variantes de horario) e as telas/artefatos de produto (no maximo 4 por rota), cada um com nome de arquivo, descricao visual detalhada e em que cenas aparece.
- Por cena, escreva: label, titulo, semana/horario, fundos, musica sugerida (das music_* existentes), presentes, resumo do que acontece (6-12 frases), objetivos de aprendizagem, cada menu com opcoes e efeitos, registros do notebook descobertos, e meta de palavras (total da rota entre 8.000 e 10.000 palavras).

Entregaveis (crie a pasta se preciso):
1. ${W}/docs/rotas/${r.id}.md - a biblia completa, em portugues simples e objetivo.
2. ${W}/docs/rotas/${r.id}-assets.json - JSON com {"characters":[{"id","name","color","sprite_dir":"images/characters/<id>","poses":{"neutral":"descricao da pose",...},"visual":"descricao visual"}],"backgrounds":[{"file":"images/bg/<nome>.png","define":"bg <nome>","desc":"...","scenes":[...]}],"artifacts":[{"file":"images/artifacts/<nome>.png","desc":"...","scenes":[...]}]}.
Nao edite nenhum outro arquivo do repositorio.`, { label: `biblia:${r.id}`, schema: SCHEMA })))
return res
