export const meta = {
  name: 'rw-f4-conteudo',
  description: 'Escreve as 36 cenas das rotas Startup e Corporativo e aplica as mecanicas da demo nas cenas da saude',
  phases: [
    { title: 'Escrita', detail: '5 escritores por rota + 2 agentes na saude' },
    { title: 'Revisao', detail: '1 revisor por rota' },
  ],
}
const W = 'C:/Users/Felipe/Documents/GitHub/Renpy Projects/Requirements-Whisper-integracao'
const LINT = `& "C:\\Program Files (x86)\\renpy-8.5.3-sdk\\lib\\py3-windows-x86_64\\python.exe" "C:\\Program Files (x86)\\renpy-8.5.3-sdk\\renpy.py" "${W}" lint`
const BASE = `Projeto: jogo educacional Ren'Py 8.5.3 em portugues do Brasil ("The Requirements Whisperer"). Worktree git em ${W} (branch integracao-rotas). Nao faca commit.
Leia antes: ${W}/CLAUDE.md; ${W}/docs/plans/2026-11-02-integracao-rotas.md; ${W}/game/data/routes.rpy; ${W}/game/logic/learning.rpy e ${W}/game/scripts/mechanics/learning_activities.rpy (API: registrar, decisao, exercicio_escrita, atividade_planejamento); ${W}/game/logic/state_flags.rpy (set_available por rota: os ids passados sao quem esta FORA da cena e pode receber mensagem); ${W}/game/data/characters.rpy e character_names.rpy (personagens, atributos de pose: neutral, thinking, serious, positive, enthusiastic, confident, concentrated; stakeholders so neutral/thinking/serious-alias); ${W}/game/data/backgrounds.rpy (fundos disponiveis) e audio_library.rpy (music_*); ${W}/game/ui/styles/sprite_transforms.rpy (left_zoom, center_zoom, right_zoom etc.). Artefatos de tela aparecem com show expression "images/artifacts/<arquivo>.png" as <tag> at center_zoom (veja scene_18_codificacao_implementacao.rpy) e devem ser escondidos depois.
Para pegar tom, ritmo e uso das mecanicas, leia por inteiro ${W}/game/story/act2_levantamento/scene_6_entrevista_stakeholders.rpy e ${W}/game/story/act3_especificacao/scene_12_especificacao_requisitos.rpy.
Regras de escrita: portugues natural, frases curtas, sem jargao desnecessario e sem tom artificial; cada personagem com a voz descrita na biblia; narracao interna em italico como nas cenas existentes; evite flexao de genero do jogador (reescreva de forma neutra); use [player_name] quando citar o jogador; nunca use [ ou { literais em falas (escreva [[ ou {{ se precisar); set_time/advance_minutes coerentes com a biblia; musica com play music; sprites entram e saem com show/hide e with dissolve; nao deixe placeholders visiveis.
Regras tecnicas: nao renomeie labels nem variaveis existentes; nao edite arquivos que nao sejam os seus; variaveis novas so se indispensaveis, com default no topo do seu proprio arquivo e prefixo da cena. Outros agentes editam outros arquivos ao mesmo tempo: rode o lint (PowerShell: ${LINT}) no maximo duas vezes, no fim, e corrija so erros nos seus arquivos; se aparecer erro de arquivo alheio ou "defined twice"/rpyc, ignore e relate.`

const ROTAS = [
  { id: 'startup', nome: 'Startup', p: 'st', estado: 'game/story/rota_startup/estado_startup.rpy', dir: 'game/story/rota_startup',
    atos: [['st_01_chegada', 'st_02_reuniao_ciclo', 'st_03_casa_sem1'], ['st_04_preparacao', 'st_05_entrevista', 'st_06_classificacao', 'st_07_social', 'st_08_casa_sem2'], ['st_09_historias', 'st_10_almoco', 'st_11_inspecao', 'st_12_casa_sem3'], ['st_13_arquitetura', 'st_14_comemoracao', 'st_15_gestao'], ['st_16_codificacao', 'st_17_testes_seguranca', 'st_18_lancamento']] },
  { id: 'corporativo', nome: 'Corporativo', p: 'co', estado: 'game/story/rota_corporativo/estado_corporativo.rpy', dir: 'game/story/rota_corporativo',
    atos: [['co_01_chegada', 'co_02_ciclo_legado', 'co_03_casa_sem1'], ['co_04_preparacao', 'co_05_entrevista', 'co_06_avaliacao', 'co_07_cafe', 'co_08_casa_sem2'], ['co_09_historias', 'co_10_almoco', 'co_11_inspecao', 'co_12_casa_sem3'], ['co_13_arquitetura', 'co_14_comemoracao', 'co_15_gestao'], ['co_16_codificacao', 'co_17_testes_seguranca', 'co_18_implantacao_avaliacao']] },
]

const escritor = (r, cenas, i) => `${BASE}

SUA TAREFA: escrever por inteiro as cenas ${cenas.join(', ')} da rota ${r.nome} (chosen_job == "${r.id}"), substituindo os stubs nos arquivos ${cenas.map(c => `${W}/${r.dir}/${c}.rpy`).join(', ')}. Sao os unicos arquivos que voce edita.
Fonte da verdade: ${W}/docs/rotas/${r.id}.md (leia a biblia INTEIRA para conhecer o arco, mas siga a risca a secao de cada uma das suas cenas: horario, fundos, musica, presentes, acontecimentos, objetivos, menus e efeitos, registros, meta de palavras). Leia tambem ${W}/${r.estado} por inteiro e use exatamente as variaveis e funcoes dele (nomes de decisoes, conquistas, registros, helpers de acerto/erro, escrita, planejamento, final). Leia ${W}/${r.dir}/rota_${r.id}.rpy para ver a ordem das cenas. ${i > 0 ? 'Cenas anteriores estao sendo escritas por outros agentes agora; baseie-se na biblia para a continuidade.' : ''}
Em cada cena: comece com o label existente, set_available(...) com quem esta fora da cena, set_time conforme a biblia, scene bg + musica; apresente personagens com add_contact na primeira aparicao (conforme a biblia); menus pedagogicos com 1 opcao adequada e 2 distratores, feedback que explica a consequencia concreta de cada distrator e revisao orientada quando o jogador erra (sem punicao), usando os helpers do arquivo de estado (que chamam decisao); menus sociais com add_friendship_point(id, 1); chame registrar(<id>) quando a biblia diz que um registro e descoberto; conceda conquistas pelos helpers do estado; termine com return. Retornos para casa terminam com call screen contacts_screen e o card de fim de semana como nas cenas da saude. Atinja a meta de palavras de cada cena (contando so o texto exibido).
Responda com: por cena, palavras aproximadas, menus, registros e conquistas cobertos; variaveis novas; resultado do lint; pendencias.`

const revisor = (r) => `${BASE}

SUA TAREFA: revisar e corrigir a rota ${r.nome} inteira, agora escrita por 5 agentes diferentes: os 18 arquivos ${W}/${r.dir}/${r.p}_*.rpy. Voce pode editar esses 18 arquivos e ${W}/${r.estado}. Fonte da verdade: ${W}/docs/rotas/${r.id}.md.
Verifique e corrija:
1. Continuidade: nomes, papeis, horarios e semanas, fatos que uma cena cita de outra, fios da biblia que atravessam a rota, falas repetidas entre cenas vizinhas, quem esta presente vs set_available.
2. Estado: toda variavel/funcao usada existe no arquivo de estado ou em learning.rpy; decisoes, registros (ids validos da rota) e conquistas cobrem o que a biblia pede; cada conquista e alcancavel; variaveis lidas em cenas posteriores sao setadas antes; o final (cena 18) usa a regra do estado; nenhum caminho trava (todo menu tem saida, toda cena termina em return).
3. Pedagogia e precisao tecnica: opcao adequada realmente correta; distratores plausiveis com feedback que explica a consequencia; nada tecnicamente errado (LGPD, Open Finance, lojas de apps, ITIL/CAB, legado, testes, seguranca). Corrija afirmacoes imprecisas.
4. Texto: portugues natural e correto, sem jargao gratuito, sem frases artificiais, sem placeholders, sem [ ou { soltos, sem flexao de genero do jogador.
5. Tamanho: some as palavras exibidas da rota (meta 8.000 a 10.000) e complete cenas muito abaixo da meta da biblia.
Rode o lint no fim (pode haver erros transitorios de outros agentes; corrija os seus). Responda com: lista de problemas encontrados e corrigidos (com arquivo), contagem de palavras por cena e total, e o que ficou pendente.`

const saude = [
  `${BASE}

SUA TAREFA: aplicar na rota SAUDE (cenas existentes) as mecanicas trazidas da demo e corrigir defeitos, nas cenas dos atos 1 a 3. Arquivos que voce pode editar: ${W}/game/story/act1_descoberta/scene_2_escritorio.rpy, scene_3_reuniao_inicial.rpy, scene_4_retorno_casa.rpy, ${W}/game/story/act2_levantamento/*.rpy, ${W}/game/story/act3_especificacao/*.rpy. NAO edite scene_1_quarto.rpy.
Use o mapa de defeitos em C:/Users/Felipe/AppData/Local/Temp/claude/C--Users-Felipe-Documents-GitHub-Requirements-Whisper/035474e1-2837-496d-9663-aefedeba92b6/scratchpad/mapa.json (chaves atos12 e atos35, campo problems de cada cena) e as ideias em mapa.json demo.ideas. Itens:
1. registrar(...) nos pontos certos: saude_reg_ciclo (scene_3), saude_reg_entrevista (scene_6), saude_reg_classificacao (scene_7), saude_reg_casos_uso (scene_10), saude_reg_inspecao (scene_12). Confira os ids em game/data/routes.rpy.
2. scene_6: transforme os menus pedagogicos (abertura, aprofundamento) em 1 opcao adequada + 2 distratores com feedback e revisao orientada, registrando decisao("saude_d6_<nome>", adequada) na primeira tentativa; mantenha os efeitos de amizade atuais da opcao adequada; inclua pedir um episodio concreto e esclarecer uma palavra ambigua (como na demo), usando o contexto clinico ja existente.
3. scene_7: acrescente uma atividade curta de classificar requisitos (funcional, nao funcional, desejo) com exemplos da saude, distratores, feedback e decisao(...). A avaliacao deve refletir o que o jogador escolheu na scene_6 quando possivel.
4. scene_12: os 4 menus de analise hoje aceitam qualquer resposta; de a cada um 1 opcao adequada e 2 distratores com feedback e revisao orientada (+1 amizade de Emily so na adequada na primeira tentativa), com decisao(...). No fim, call exercicio_escrita("saude_escrita", <pedido novo da saude>) com um pedido clinico coerente com o projeto. Corrija o checklist quebrado (aspas e \\n soltos).
5. Correcoes: id cru 'developer_requirements' no menu da scene_5; inconsistencia 'diretor medico/enfermeira' vs as duas doutoras (scenes 5 e 9); scene_9 citando fatos que o jogador pode nao ter visto (use as variaveis das escolhas da scene_6 ou generalize); continuidade de horario scene_7 -> scene_8; set_available coerente com quem esta presente nas cenas 6, 8, 10; nome do projeto consistente (ByeByeFumo) nos atos 1-3; fala gendrada fixa 'bem-vindo' na scene_2 (neutralize).
Nao mude a ordem das cenas nem labels. Mantenha o tom. Responda com a lista de mudancas por arquivo, decisoes/registros adicionados e o lint.`,
  `${BASE}

SUA TAREFA: aplicar na rota SAUDE (cenas existentes) as mecanicas trazidas da demo e corrigir defeitos, nas cenas dos atos 4 e 5 e no final. Arquivos que voce pode editar: ${W}/game/story/act4_arquitetura/*.rpy, ${W}/game/story/act5_implementacao/*.rpy e, somente na entrada "saude" (achievements), ${W}/game/data/routes.rpy.
Use o mapa de defeitos em C:/Users/Felipe/AppData/Local/Temp/claude/C--Users-Felipe-Documents-GitHub-Requirements-Whisper/035474e1-2837-496d-9663-aefedeba92b6/scratchpad/mapa.json (chave atos35, campo problems) e mapa.json mecanicas.endings_and_scoring. Itens:
1. registrar(...): saude_reg_arquitetura (scene_14), saude_reg_testes (scene_19), saude_reg_implantacao (scene_20). Confira os ids em routes.rpy.
2. scene_14: remova os placeholders visiveis; acrescente uma negociacao de mudanca de escopo como na demo (a doutora pede a integracao com o app 'Adeus Cigarro' ja citado nas cenas 6 e 10): duas opcoes ruins (prometer tudo no mesmo prazo; recusar porque nao estava escrito) com consequencia e volta ao menu, e dois acordos validos; guarde a escolha numa variavel nova (default no seu arquivo) e cite-a em scene_16 ou scene_21; decisao(...).
3. scene_16: remova o placeholder do cronograma; acrescente call atividade_planejamento("saude_plano", <4 itens concretos dos requisitos da saude>, <2 necessarios>, 2) com falas de feedback; decisao(...).
4. Conquistas e final: faca as escolhas da scene_20 concederem 'docker'/'badge_devops', 'badge_bug_buster', 'badge_resiliencia' ou 'badge_team_work' em inventario conforme a escolha (para que resultado_tech DevOps/Teamwork da scene_21 seja alcancavel); torne 'conquista_guardiao_privacidade' alcancavel na scene_19 calculando a maturidade a partir das escolhas (em vez de 85 fixo); no caminho 'descansar' da scene_18 garanta que o selo_codigo_sem_bugs ainda possa ser obtido; troque amizade_x += n por add_friendship_point(...) (scenes 15, 17, 18_2); acrescente em ROUTES["saude"]["achievements"] as conquistas que passaram a ser alcancaveis. Verifique o problema relatado de atributos de imagem em falas na scene_18_2 e corrija se for real.
5. Correcoes: na scene_21 os nomes 'Dr. Almeida' e 'Enfermeira Marta' devem ser as doutoras reais (NOME_DOUTORA_1/2); 'acertos_extra' in globals() fragil na scene_17 (use default); falas incoerentes no ramo 'virar a noite' da scene_18; Emily citando reuniao das 15h que nao acontece (scene_11 e de outro agente: ignore).
Nao mude a ordem das cenas nem labels. Mantenha o tom. Responda com a lista de mudancas por arquivo, conquistas agora alcancaveis e o lint.`,
]

phase('Escrita')
const saudeP = parallel(saude.map((s, i) => () => agent(s, { label: `saude:${i ? 'atos-4-5' : 'atos-1-3'}`, phase: 'Escrita' })))
const rotasP = pipeline(ROTAS,
  r => parallel(r.atos.map((cenas, i) => () => agent(escritor(r, cenas, i), { label: `${r.p}:ato-${i + 1}`, phase: 'Escrita' }))),
  (escritos, r) => agent(revisor(r), { label: `revisor:${r.id}`, phase: 'Revisao' }).then(rev => ({ rota: r.id, escritos, revisao: rev })),
)
const [s, rr] = await Promise.all([saudeP, rotasP])
return { saude: s, rotas: rr }
