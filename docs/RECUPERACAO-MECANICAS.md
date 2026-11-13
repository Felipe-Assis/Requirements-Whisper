# Mecânicas do jogo original completo

Inventário factual para apresentar e avaliar o jogo existente, sem reconstruir a abertura, substituir as rotas ou escolher uma base de integração.

## Base e limites desta leitura

- Repositório original: `C:/Users/Felipe/Documents/GitHub/Renpy Projects/Requirements-Whisper`.
- Commit examinado: **`d6b9403b341b700b5cc899c1b53a4928ea640cfa`** (`d6b9403`, 02/11/2026). `git status --porcelain -- game` estava vazio nesta leitura. Todas as referências de caminho e linha abaixo pertencem a esse commit, salvo indicação contrária.
- Repositório curto atual: `C:/Users/Felipe/Documents/GitHub/Requirements-Whisper`, main `c934289`; worktree `campanha-completa` separado. Esse histórico contém a demo curta e a campanha nova, e não contém a história completa do original após `c3ad023`.
- O original foi apenas lido. Nenhum SDK, jogo, GUI, API de chat ou teste foi executado: o usuário estava jogando. Este documento registra comportamento presente no código, não uma validação visual ou um playtest novo.
- `AGENTS.md` original foi lido. Seu texto descreve uma versão mais antiga, com uma rota e sem testes. `CLAUDE.md`, `game/script.rpy` e os arquivos de `game/tests/` já descrevem/implementam três rotas. Nos pontos divergentes, esta leitura segue o código de `d6b9403`.
- TodoWrite não está exposto nesta sessão; acompanhamento: leitura do original concluída, inventário concluído, documentação e revisão concluídas. Somente este arquivo foi autorizado para escrita por este agente.

## O que é o jogo completo

Uma visual novel sobre o estágio ao longo do ciclo de engenharia de software, com cenas de trabalho, casa, convivência, escolhas técnicas, relações, registros, atividades e encerramento. A escolha da vaga muda a cadeia narrativa efetivamente executada.

| Rota | Empresa/produto | Pessoas e conflito central | Encadeamento |
|---|---|---|---|
| Saúde | Instituto XX / ByeByeFumo | Equipe de desenvolvimento e duas médicas; sistema clínico, entrevistas, especificação, arquitetura, implementação, segurança e implantação | `game/script.rpy:13–46`; cenas `scene_3` a `scene_21`, após chegada em `scene_2_escritorio` |
| Startup | Trocado / app Trocado | Tainá, Otávio, Davi, Lorena, Vinícius e Bia; gastos de universitários, confiança no total e sincronização, prazo do semestre e demo day | `game/story/rota_startup/rota_startup.rpy:8–39`; 18 cenas `st_01` a `st_18` |
| Corporativo | Grupo Vértice / SGC e módulo Farol | Valéria, Jorge, Kauã, Ingrid, Rosângela e Edson; sistema legado de chamados, solução vazia, histórico, auditoria e implantação controlada | `game/story/rota_corporativo/rota_corporativo.rpy:9–41`; 18 cenas `co_01` a `co_18` |

Fonte dos nomes de empresa, times, stakeholders e produto: `game/data/routes.rpy:12–44`. Fonte dos nomes dos personagens: `game/data/character_names.rpy:8–63`. Os arquivos de rotas também inserem intermissões e pontos de parada entre cenas; eles não são três versões de uma única missão curta.

## Entrada e preparação reais

`game/script.rpy:1–12` gera o identificador de usuário quando necessário, faz `call scene_1_quarto from _scene_1_quarto` e despacha `chosen_job`: `startup` chama `rota_startup`, `corporativo` chama `rota_corporativo`; qualquer outro valor segue a Saúde. `game/data/routes.rpy:47–69` conserva a mesma interpretação para os dados das telas.

Sequência de `game/story/act1_descoberta/scene_1_quarto.rpy`:

1. Linhas 1–20: limpa nome/gênero/idade do perfil, entra no quarto de manhã com `fade`, toca o alarme e a música `music_home_dreamy`; o texto mostra o protagonista acordando. O relógio avança por chamadas explícitas de `advance_minutes`.
2. Linhas 22–29: pega notebook; exibe `images/items/notebook_fechado.png` em `center_zoom`, chama `add_to_inventory("notebook")`, esconde com `dissolve`.
3. Linhas 31–38: pega celular com notificação; exibe `images/items/celular.png` em `left_zoom`, adiciona ao inventário e dissolve.
4. Linhas 40–55: encontra bloco de notas e caneta; mostra `images/items/bloco_de_notas.png` e `images/items/caneta.png` em `right_zoom`, adiciona os dois; mostra `screen inventory_button`.
5. Linhas 60–88: atualiza currículo pelo notebook. Nome é opcional, vazio vira Alex, e há escolha de gênero. A idade não é mais pedida. Não há formulário de emblemas Ideias/Código/Diálogo nesta versão.
6. Linhas 101–124: escolhe uma de três vagas. Saúde define `chosen_job = "saude"`; startup define `"startup"`; grande corporação define `"corporativo"`. As opções têm descrições próprias dos produtos e ambientes.
7. Linhas 126–153: conclui candidatura, pega mochila e garrafinha. Mostra `images/items/mochila.png` em `left_zoom` e `images/items/garrafinha.png` em `right_zoom`. O tutorial explica que a mochila fica no canto superior esquerdo, o celular leva aos contatos e o estado de amizade aparece ali; algumas pessoas não recebem mensagens durante certas cenas.
8. Linhas 155–169: o protagonista troca de roupa em texto, a música sai gradualmente, passa por tela preta e salta para `scene_2_escritorio`. Na Saúde essa cena apresenta chegada/equipe; nas outras rotas retorna para `start`, e a chegada ocorre em `st_01`/`co_01`.

Precisão histórica: no completo `d6b9403` o alarme, pegar itens e trocar roupa são encenados por falas/imagens/sons; não são cinco telas obrigatórias de clicar em objetos. O protótipo `07c435a:game/scripts/scene_1_quarto.rpy:1–96` chamava cinco `pointclick_*`, porém não continha as definições dessas screens. A demo curta posteriormente implementou etapas próprias via `room_action`. Apresentar o completo como se usasse essas cinco telas seria misturar versões.

### Imagens e som da abertura

| Uso | Arquivo exato dentro de `game/` | Definição/uso |
|---|---|---|
| Quarto de manhã | `images/bg/quarto_manha.png` | `data/backgrounds.rpy:41`; `scene_1_quarto.rpy:6` |
| Quarto à noite | `images/bg/quarto_noite.png` | `data/backgrounds.rpy:42`; epílogo linha 74 |
| Notebook fechado | `images/items/notebook_fechado.png` | `scene_1_quarto.rpy:24`; `data/items.rpy:61` |
| Notebook aberto | `images/items/notebook_aberto.png` | `data/items.rpy:62` e 68–69 |
| Celular | `images/items/celular.png` | `scene_1_quarto.rpy:33`; `data/items.rpy:28–31` |
| Bloco | `images/items/bloco_de_notas.png` | `scene_1_quarto.rpy:42`; `data/items.rpy:16–19` |
| Caneta | `images/items/caneta.png` | `scene_1_quarto.rpy:49`; `data/items.rpy:22–25` |
| Mochila fechada | `images/items/mochila.png` | `scene_1_quarto.rpy:132`; `data/items.rpy:33–38` |
| Mochila aberta no hover | `images/items/mochila_aberta_vazia.png` | `data/items.rpy:41–44`; inventário linha 117 |
| Garrafinha | `images/items/garrafinha.png` | `scene_1_quarto.rpy:145–149`; `data/items.rpy:79–82` |
| Despertador | `audio/effects/alarm_clock.ogg` | `scene_1_quarto.rpy:11` |
| Digitação | `audio/effects/computer_typing.ogg` | `scene_1_quarto.rpy:90,127` |
| Música da casa | `audio/music/home_dreamy - Ian Post - Closer.mp3` | `data/audio_library.rpy:5` |

Os nomes de imagem em `data/items.rpy` usam caminhos `items/...`, resolvidos pelo mecanismo de busca de imagens do Ren'Py; os arquivos físicos ficam em `game/images/items/`.

## Mochila e inventário

Fonte principal: `game/scripts/mechanics/inventory_screen.rpy:1–123`.

- `inventory_button`, linhas 113–123: `imagebutton` em `(30,30)`, tamanho `120×120`, condicionado a `inventory_enabled`; `idle "item mochila_idle"`, `hover "item mochila_aberta_vazia_idle"`, `focus_mask True`, texto alternativo Mochila. Clicar executa `ShowMenu("inventory_screen")`. Passar o mouse muda a imagem para aberta; não abre sozinho a janela de inventário.
- `ITENS_ORDER`, linha 4: notebook, celular, bloco_de_notas, caneta, garrafinha. A mochila é o acesso visual, não um sexto tile nesse conjunto.
- `inventory_tile`, linhas 42–60: só aparece quando `item_<id>` é verdadeiro. Tile com arte de 128 px e nome; hover/foco mostra descrição; fundo muda no foco. Notebook fecha a mochila e abre `notebook_registros`; celular fecha a mochila e abre `contacts_screen`; demais itens mostram descrição.
- `inventory_screen`, linhas 62–110: modal, escurecimento de fundo, título Mochila, tiles visuais, descrição em área de altura fixa, instruções por teclado. Fechar usa `Return()` se foi aberta como menu, ou `Hide` se foi aberta diretamente; Esc e I também fecham.
- `game/logic/inventory.rpy:6–12`: `add_to_inventory` liga o booleano `item_*` e notifica. Essas flags são distintas da lista `inventario` de conquistas da Saúde e da lista antiga `inventory` do protótipo curto.
- `game/logic/state_flags.rpy:7–22`: flags dos objetos e `inventory_enabled`. Não renomear essas variáveis ao preservar partidas.

## Celular, contatos e amizade

Fontes: `game/scripts/mechanics/contacts_screen.rpy:33–128`; `game/logic/friendship.rpy:3–99`; `game/logic/state_flags.rpy:25–106`; `game/data/routes.rpy:12–69`.

O celular é um item funcional: o tile abre a grade da rota. Saúde tem dez contatos (oito integrantes e duas médicas); Startup e Corporativo têm seis cada (quatro integrantes e dois stakeholders). A grade usa cinco ou três colunas conforme a rota. O Colega de República participa da história mas não integra essas listas de contatos.

Cada contato tem dois estados: `contato_<id>` significa conhecido/desbloqueado; `disponivel_<id>` significa acessível naquele momento. Contatos desconhecidos não aparecem. Os indisponíveis aparecem com retrato acinzentado, texto explícito e sem ação. Disponíveis mostram descrição no foco e abrem conversa. Todos mostram coração, barra e número de amizade `/10` (`contacts_screen.rpy:33–77`).

O clique faz `SetVariable("amigo_selecionado", cid)`, esconde contatos e faz **`Call("chat_amigo")`**, preservando o retorno à cena. Trocar por `Jump` interromperia a cena que abriu os contatos (`contacts_screen.rpy:46–49`).

`set_available(*ids)` só mantém disponíveis os IDs passados; `'all'` habilita a rota toda. Na Saúde administra os oito developers; as médicas têm controle explícito nas cenas. Nas outras rotas inclui equipe e stakeholders. A mesma função reinicia `chat_amizade_dada`, permitindo um novo ganho por contato naquele momento (`state_flags.rpy:96–106`).

`add_contact` desbloqueia e notifica (`friendship.rpy:33–49`). `add_friendship_point` limita o valor a 0–10 (`52–72`); o padrão é +0,5, mas cenas passam outros valores. Cor da barra tem cinco faixas (`85–99`). Conversas e decisões sociais afetam amizade; avaliações finais usam a soma da equipe, não a soma de todos os contatos indiscriminadamente.

## Chat: o que funciona online e offline

Fontes: `game/scripts/mechanics/chat_screen.rpy:20–161`; `game/python/chat_backend.rpy:25–167`; `game/data/friends_data.rpy:73–269`; `game/logic/state_progress.rpy:12`. Endereço de serviço e identificadores remotos foram deliberadamente omitidos.

### Experiência da tela

- Retrato, nome, histórico de balões com autoria escrita, rolagem, campo de até 200 caracteres e Enviar/Enter. Botão fica inativo quando vazio ou aguardando (`chat_screen.rpy:20–132`).
- Fechar/Esc retorna à cena. O histórico visual é zerado ao iniciar `chat_amigo` (`136–140`); não apresentar a interface como caixa de entrada persistente ou e-mail.
- Ao abrir, ganha +1 de amizade apenas na primeira conversa com aquele contato desde o último `set_available` (`148–152`). Abrir repetidamente no mesmo momento não acumula pontos.
- Startup e Corporativo exibem a legenda **respostas roteirizadas, sem internet** (`51–54`).

### Doze contatos locais

Todos os seis contatos da Startup e os seis do Corporativo têm assistente remoto ausente. `chat_is_offline` detecta esse estado. `send_offline_reply` escolhe a próxima fala da lista do contato, em rodízio, mostra usuário+resposta e avança o índice; tudo na thread principal, sem rede e sem espera (`chat_backend.rpy:132–154`). A resposta é roteirizada, não depende semanticamente da pergunta digitada. O índice fica em `chat_offline_idx` e o texto é traduzível.

### Saúde e serviço remoto

Os contatos da Saúde possuem configuração de assistente remoto. No desktop, o cliente envia POST ao caminho `/chat/message/send` com `user_id`, `assistant_id` e `message`; timeout de 60 segundos; lê o campo `response`. Normaliza string, lista ou lista serializada (`chat_backend.rpy:29–69`). Não há fallback local geral para esses contatos: erro vira mensagem na conversa. Concluir o roteiro não exige que o serviço tenha respondido; apresentar esse chat como plenamente offline seria incorreto.

Na Web, o fluxo público ativo mostra aviso de indisponibilidade e recomenda baixar o jogo (`43–49`, `161–167`). Existe uma função de `fetch` no arquivo (`72–99`), mas ela não é o transporte usado por esse caminho ativo. Não prometer IA online no navegador com base na mera existência dessa função.

### Restrições importantes ao preservar o recurso

- Thread de rede publica a resposta em buffer; `drain_pending_response` atualiza histórico e espera na thread principal. Timer de 0,1 s da tela faz a drenagem (`chat_backend.rpy:102–129`; `chat_screen.rpy:28–30`).
- Callback após carregar save limpa espera, entrada e buffer; impede manter digitando para sempre após um load (`chat_backend.rpy:123–129`).
- Não copiar os assistentes da Saúde para os personagens de outras rotas: suas respostas locais evitam falar de um projeto que não conhecem. O HTML pode mostrar chat local representativo e distinguir claramente IA remota de diálogo roteirizado.
- Não incluir endereço, IDs remotos, usuário real ou conversas reais na apresentação. Este inventário não testa disponibilidade do serviço nem confirma a configuração externa.

## Notebook e aprendizagem

O notebook abre pela mochila. `game/scripts/mechanics/notebook_screen.rpy:67–145` lista oito registros da rota, informa empresa e contagem, separa registrado/pendente e só revela o conteúdo descoberto. Esc ou N fecha; roda e PgUp/PgDn rolam. Não é o desktop com e-mail da campanha curta nova.

`game/logic/learning.rpy:49–78`: `registrar` valida o ID da rota, marca uma vez e notifica. `105–121`: `decisao` guarda somente a primeira tentativa; `True` significa adequada sem apoio, `False` significa revisão orientada. Repetir não apaga o primeiro resultado. `84–103`: conquistas e resultado final consultam os contratos da rota.

| Rota | Oito assuntos registrados | Fonte |
|---|---|---|
| Saúde | Ciclo de vida; entrevista; classificação; casos de uso; inspeção; arquitetura e trade-offs; testes e segurança; implantação | `game/data/routes.rpy:76–117` |
| Startup | MVP e ciclo curto; da queixa ao requisito; tipos; história/critério/caso limite; inspeção; mudança de escopo; capacidade/riscos/métricas; LGPD e Open Finance | `game/story/rota_startup/estado_startup.rpy:95–136` |
| Corporativo | Manutenção e mudança; leitura do legado; episódio/palavra vaga/conflito; classificação; história/critério/caso limite; inspeção; transição; regressão/perfis/trilha | `game/story/rota_corporativo/estado_corporativo.rpy:100–141` |

### Escrita livre e autoavaliação

`game/scripts/mechanics/learning_activities.rpy:23–40,102–128,213–298`: escreve requisito e critério, até 400 caracteres cada; pode reescrever, confirmar ou guardar pendente. O mesmo ID retoma o rascunho e as marcas. Confirmar exige dois campos preenchidos e quatro marcas; não há avaliação automática do significado do texto.

Quatro perguntas da rubrica de autoavaliação: fica claro quem age; condições limitantes explícitas; resultado observável no critério; exceção ou caso a recusar (`23–27`). Estado em `escritas[eid]`: textos, checks 0–4, status e quatro booleanos. Texto livre tem `{` e `[` escapados para exibição segura (`game/logic/learning.rpy:129–141`).

Exemplos reais: Saúde escreve sobre aviso no mesmo dia quando paciente falta ao retorno (`game/story/act3_especificacao/scene_12_especificacao_requisitos.rpy:223`); Startup corrige valor positivo de gasto e atualiza total (`estado_startup.rpy:174–176`); Corporativo escreve sobre reabrir chamado (`estado_corporativo.rpy:13–14,235–243`).

### Planejamento e escolhas com feedback

`learning_activities.rpy:52–96,134–163`: monta plano com capacidade, normalmente dois itens. Pode adicionar, retirar, conferir, rever e concluir. Cobertura conta os itens necessários; registra também `primeira_cobertura`, preservada nas revisões. Não é estimativa de esforço real nem quadro Kanban livre.

Saúde escolhe dois entre autosave do histórico, cálculo HAD com incompletude, gráficos 3D e integração com outro app (`game/story/act4_arquitetura/scene_16_reuniao_gerenciamento.rpy:112–113`). Startup prioriza confirmação/cancelamento de exclusão e atualização de lista/total; medalhas e compartilhamento competem pelas duas vagas (`estado_startup.rpy:178–185`). Corporativo possui plano próprio em `co_15_gestao.rpy`.

Startup usa `st_decidir` e Corporativo usa `co_acerto`/`co_erro`: decisão adequada inicial, distratores com consequência e revisão orientada; score/flags e primeira tentativa têm funções distintas (`estado_startup.rpy:193–203`; `estado_corporativo.rpy:182–191`). A revisão ajuda a avançar sem reescrever o histórico do desempenho inicial.

### Autoavaliação de maturidade da Saúde

`game/story/act5_implementacao/scene_19_testes_seguranca.rpy:108–174` tem uma rubrica distinta. Testes de permissões, injeção, autenticação e logs realizados no dia valem dois pontos cada, limitados a seis pontos. Três perguntas sobre exportação de dados, auditoria e resposta a vazamento valem 0/1/2 cada. O percentual é a divisão inteira dos pontos por 12, multiplicada por 100. Faixas: ≥91 Excelente; ≥71 Avançado; ≥41 Básico; ≥11 Inicial; restante Inexistente. Não é porcentagem fixa. Excelente libera a conquista Privacidade Levada a Sério (`242–245`). É uma pontuação ficcional do exercício; não comprova conformidade ou maturidade real de uma organização.

### Caça à ambiguidade e rastreabilidade

`game/scripts/mechanics/ambiguidade.rpy:1–36,222–263`: seleciona palavras vagas entre iscas, confere, recebe ajuda caso precise e escolhe reescritas verificáveis. Resultado mostra o requisito reescrito. Primeira marcação e primeira reescrita são registradas; distrator explica a consequência e permite tentar outra opção. Dados específicos ficam em `game/data/ambiguidade_dados.rpy`.

`game/scripts/mechanics/rastreabilidade.rpy:1–34,243–274,457`: relaciona requisito → critério → teste. Seletores aceitam nenhum teste cobre; há lacuna deliberada. Conferência aponta vínculos errados, permite revisão e mostra cobertura. A lacuna não é simplesmente revelada pelo feedback. Registra primeira conferência de ligações e identificação da lacuna. `rast_lembrar` retoma o quadro na semana de testes. Dados em `game/data/rastreabilidade_dados.rpy`.

## Escolhas, linguagem visual e controle

`game/screens.rpy:225–344`: `screen choice(items, tipo=None)` conserva texto/ação originais e acrescenta selo opcional. Tipos: Trabalho (`▤`), Conversa (`❝`), Negociação (`⇄`), Pista (`⚲`). Pode declarar tipo no menu ou em uma opção. Selo contém ícone, rótulo e faixa de cor; texto alternativo inclui o nome do tipo. São glifos de fonte, não arquivos PNG. Menu sem tipo continua funcionando.

Lista rola quando necessário e respeita fonte maior; tela mantém opções acima da fala. Não basta copiar quatro ícones: o contrato inclui `MENU_TIPOS`, `menu_tipo`, `choice_selo`, estilos e argumento `tipo`.

## Conquistas, avaliação e finais

O jogo tem variações de resultado e diálogo; a existência de três graus não significa três campanhas completamente diferentes no encerramento. As condições usam fatos da partida. O epílogo compartilhado mostra conquistas, oito registros, decisões adequadas sem apoio/com revisão e escritas confirmadas/pendentes; depois oferece novo ciclo (`renpy.full_restart`), créditos ou encerrar (`game/story/epilogue/scene_epilogo_conquistas_final.rpy:1–8,74–98,106–182`).

| Rota | Excelente | Bom | Demais casos | Fonte |
|---|---|---|---|---|
| Saúde | Amizade dos oito developers ≥40 e selos Código sem Bugs + Caça a Bugs e Vulnerabilidades | Amizade ≥30 | `ok` | `game/data/routes.rpy:167–176`; `scene_21_avaliacao_final.rpy:53–60` |
| Startup | Amizade dos quatro integrantes ≥20 e ≥5 conquistas pedagógicas | Amizade ≥15 **ou** ≥5 conquistas pedagógicas | `ok` | `estado_startup.rpy:241–258` |
| Corporativo | Amizade dos quatro integrantes ≥20 e ≥4 conquistas de aprendizagem | Amizade ≥15 **ou** ≥5 conquistas de aprendizagem | `ok` | `estado_corporativo.rpy:245–269` |

### Saúde

Treze conquistas registradas em `game/data/routes.rpy:123–163`: Código sem Bugs, Privacidade Levada a Sério, Visão DevOps, Bug Crítico Resolvido, Trabalho em Equipe, Resiliência, Caça a Bugs e Vulnerabilidades, Medalha de Estudo, Checklist de Qualidade, Código Limpo, Demo Colaborativa, PR Transparente e Mindfulness Dev. São itens em `inventario`, não tiles da mochila física.

`game/story/act5_implementacao/scene_21_avaliacao_final.rpy:63–71` distingue resultado técnico DevOps/Teamwork/Padrão conforme os selos; linhas 95–118 variam falas e revisão. Amizade ≥50 acrescenta fala de gestão (`140`). O resumo final consulta conquistas efetivamente adquiridas; não contar o grande bloco antigo comentado do epílogo como cena executada.

### Startup

Dez conquistas, das quais oito entram no cálculo pedagógico: escuta, critério, inspeção, rascunho, acordo, foco no MVP, revisão e proteção dos dados. Lançamento gradual e Time Trocado ficam fora desse subtotal (`estado_startup.rpy`, achievements; `245–279`). Time Trocado exige amizade ≥5 com cada um dos quatro integrantes.

Semana 8 encena submissão às lojas, rollout, pico de cadastros e demo day (`st_18_lancamento.rpy`). Decisões anteriores alteram tempo de aprovação/ajuste da exclusão de conta (`76`), comportamento no pico e custo de energia (`110–133`), e o acordo negociado repercute no lançamento (`229`). Avaliação usa `st_final_grade` (`257–269`); a conquista de equipe abre convite para voltar nas férias (`324`). Não é uma simulação executável de app financeiro completo: as telas do produto são artefatos exibidos durante a narrativa.

### Corporativo

Nove conquistas: oito de aprendizagem (Arqueologia do Legado, Escuta que Pergunta, Inspeção em Dia, Acordo Registrado, Troca com o Avião Voando, Rede de Regressão, Guardião da Trilha, Janela Cumprida) e Memória Viva, social, fora do subtotal (`estado_corporativo.rpy:143–176,198–220`). Memória Viva envolve homenagem/wiki e amizade com Jorge.

`co_18_implantacao_avaliacao.rpy` encena janela de 0h às 4h, carga histórica defeituosa, critério de parada e rollback parcial. A escolha inicial de risco altera a proporção de registros com problema; o acordo de arquitetura/WhatsApp altera piloto versus liberação geral. Há avaliação com dados da central e possibilidade de reabrir chamado; memória de Jorge e amizade alta abrem despedidas próprias. O final é calculado e salvo por `co_calcular_final`; amizade ≥28 acrescenta convite para a próxima rodada. Os produtos exibidos são `images/artifacts/co_farol_consulta.png` e `images/artifacts/co_farol_auditoria.png`.

## Transições, poses, movimento e som

- Composição de personagens: `game/ui/styles/sprite_transforms.rpy:7–36` define `left_zoom`, `left_zoom_2`, `center_zoom`, `right_zoom`, `right_zoom2`, normalmente zoom 0,6 e pés na base. Troca de atributo muda a pose da mesma tag; não são modelos Live2D.
- Respiração discreta e deslocamento lateral: `game/ui/styles/vida_transforms.rpy:23–32,47–51`; amplitude vertical 0,6%, períodos diferentes por personagem. O wrapper acrescenta o movimento automaticamente a sprites mostrados com posição explícita.
- Destaque de fala: `game/ui/styles/fala_destaque.rpy:24–90`; quem não fala escurece e perde um pouco de saturação em 0,15 s. Narrador/jogador sem sprite não escurecem todos. `FalaFoco` pode fazer parte de saves: renomear/remover quebra compatibilidade.
- Câmera leve: `vida_transforms.rpy:35–67` fornece aproximação de 4% e reset. Não foram encontradas chamadas a `cam_foco` em `game/story/` neste commit; não apresentar a câmera aproximando nas cenas como recurso já utilizado. Preferência de movimento desliga, e transições desligadas tornam a mudança instantânea.
- Abertura e várias cenas usam `fade`, `dissolve`, entradas/saídas, `show expression` de objeto, pausas e fade de música. Gestos são poses PNG (neutral/thinking/serious etc.), não captura de movimento.
- `game/options.rpy:30–31`: `config.zoom_zaxis = False` e `config.old_show_expression = True` preservam enquadramento e exibição dos objetos da versão anterior. Retirar muda a apresentação.
- `game/data/backgrounds.rpy:41–62`: quarto manhã/noite, coworking manhã/tarde/noite, terraço, auditório do demo day, central de atendimento manhã/tarde e sala de servidores têm arquivos próprios.
- Artefatos de produto usam `game/ui/styles/artefato_transforms.rpy:11–16`, `fit contain`, área de 1500×640 acima da fala. Esse enquadramento preserva a leitura da imagem, inclusive com texto maior; não usar o transform de sprite, que esconderia parte do documento atrás da caixa de diálogo.
- `game/scripts/mechanics/intermissao_fluxo.rpy:103–127` controla telas de deslocamento e pontos de parada. Com transições desligadas, trajeto vira cartão de texto. Ao final das semanas 1 a 7, `im_ponto_parada` prepara autosave e abre resumo com Continuar/Salvar/Voltar ao menu. Esses retornos fazem parte do ritmo do jogo.
- Relógio original: `game/scripts/mechanics/clock_screen.rpy:4–28`, ícone `images/items/clock.png`, horário HH:MM no canto superior direito. Tempo muda por ações da narrativa; a tela modal usa o desenho compartilhado quando necessário. Não substituí-lo por horário meramente decorativo.

## Elenco e arte: leitura para a apresentação

Os nomes vêm de `game/data/character_names.rpy`; os mapeamentos exatos estão em `game/data/characters.rpy`. Cada retrato usado nos contatos aponta ao arquivo de seu personagem. Saúde possui expressões próprias e alguns aliases; Startup/Corporativo têm neutral/thinking como base, membros da equipe têm serious própria, e várias outras expressões são aliases para neutral/thinking. Não anunciar cada alias como roupa/pose desenhada exclusiva.

O colega de república usa `images/characters/amigo/base.png`. Os demais arquivos físicos seguem `images/characters/<id>/<pose>.png`. A tabela abaixo é gerada das declarações `image` do arquivo em `d6b9403`; permite ao HTML usar a arte verdadeira sem inferir nomes de arquivos. As expressões repetindo o mesmo arquivo são aliases.

O catálogo contém 23 personagens, 149 declarações e 87 PNG distintos; todos os arquivos mapeados foram encontrados. Não há conjunto de roupas alternativas selecionáveis nesse catálogo: variações de pose e aliases não devem ser apresentadas como troca de roupa. A troca de roupa da abertura é um gesto narrado.

| ID do personagem / pasta | Arquivos e atributos que apontam a eles | Linhas em `data/characters.rpy` |
|---|---|---|
| `npc_roommate` / `images/characters/amigo` | `base.png` ← neutral | 31–31 |
| `doutora_1` / `images/characters/doutora_1` | `portrait.png` ← portrait; `neutral.png` ← neutral; `serious.png` ← serious; `thinking.png` ← thinking; `positive.png` ← positive | 34–38 |
| `doutora_2` / `images/characters/doutora_2` | `portrait.png` ← portrait; `neutral.png` ← neutral; `serious.png` ← serious; `thinking.png` ← thinking; `positive.png` ← positive | 41–45 |
| `developer_ai` / `images/characters/developer_ai` | `portrait.png` ← portrait; `concentrated.png` ← concentrated; `positive.png` ← positive, enthusiastic; `thinking.png` ← thinking | 50–55 |
| `developer_coding` / `images/characters/developer_coding` | `portrait.png` ← portrait; `neutral.png` ← neutral, positive; `serious.png` ← serious; `thinking.png` ← thinking | 58–62 |
| `developer_management` / `images/characters/developer_management` | `portrait.png` ← portrait; `serious.png` ← serious; `thinking.png` ← thinking, positive, enthusiastic | 65–70 |
| `developer_project` / `images/characters/developer_project` | `portrait.png` ← portrait; `confident.png` ← confident, neutral, positive; `serious.png` ← serious; `thinking.png` ← thinking | 73–79 |
| `developer_quality` / `images/characters/developer_quality` | `portrait.png` ← portrait; `positive.png` ← positive, enthusiastic; `serious.png` ← serious; `thinking.png` ← thinking | 82–87 |
| `developer_requirements` / `images/characters/developer_requirements` | `portrait.png` ← portrait; `enthusiastic.png` ← enthusiastic, positive; `neutral.png` ← neutral; `serious.png` ← serious; `thinking.png` ← thinking | 90–95 |
| `developer_security` / `images/characters/developer_security` | `portrait.png` ← portrait; `serious.png` ← serious; `thinking.png` ← thinking, enthusiastic | 98–102 |
| `developer_test` / `images/characters/developer_test` | `portrait.png` ← portrait; `confident.png` ← confident, positive; `enthusiastic.png` ← enthusiastic; `serious.png` ← serious; `thinking.png` ← thinking | 105–110 |
| `st_mentora` / `images/characters/st_mentora` | `portrait.png` ← portrait; `neutral.png` ← neutral, positive, enthusiastic, confident, concentrated; `thinking.png` ← thinking; `serious.png` ← serious | 134–142 |
| `st_techlead` / `images/characters/st_techlead` | `portrait.png` ← portrait; `neutral.png` ← neutral, positive, enthusiastic, confident, concentrated; `thinking.png` ← thinking; `serious.png` ← serious | 145–153 |
| `st_mobile` / `images/characters/st_mobile` | `portrait.png` ← portrait; `neutral.png` ← neutral, positive, enthusiastic, confident, concentrated; `thinking.png` ← thinking; `serious.png` ← serious | 156–164 |
| `st_qualidade` / `images/characters/st_qualidade` | `portrait.png` ← portrait; `neutral.png` ← neutral, positive, enthusiastic, confident, concentrated; `thinking.png` ← thinking; `serious.png` ← serious | 167–175 |
| `st_ceo` / `images/characters/st_ceo` | `portrait.png` ← portrait; `neutral.png` ← neutral, positive, enthusiastic, confident, concentrated; `thinking.png` ← thinking, serious | 178–186 |
| `st_estudante` / `images/characters/st_estudante` | `portrait.png` ← portrait; `neutral.png` ← neutral, positive, enthusiastic, confident, concentrated; `thinking.png` ← thinking, serious | 189–197 |
| `co_mentora` / `images/characters/co_mentora` | `portrait.png` ← portrait; `neutral.png` ← neutral, positive, enthusiastic, confident, concentrated; `thinking.png` ← thinking; `serious.png` ← serious | 200–208 |
| `co_legado` / `images/characters/co_legado` | `portrait.png` ← portrait; `neutral.png` ← neutral, positive, enthusiastic, confident, concentrated; `thinking.png` ← thinking; `serious.png` ← serious | 211–219 |
| `co_dev` / `images/characters/co_dev` | `portrait.png` ← portrait; `neutral.png` ← neutral, positive, enthusiastic, confident, concentrated; `thinking.png` ← thinking; `serious.png` ← serious | 222–230 |
| `co_qualidade` / `images/characters/co_qualidade` | `portrait.png` ← portrait; `neutral.png` ← neutral, positive, enthusiastic, confident, concentrated; `thinking.png` ← thinking; `serious.png` ← serious | 233–241 |
| `co_supervisora` / `images/characters/co_supervisora` | `portrait.png` ← portrait; `neutral.png` ← neutral, positive, enthusiastic, confident, concentrated; `thinking.png` ← thinking, serious | 244–252 |
| `co_solicitante` / `images/characters/co_solicitante` | `portrait.png` ← portrait; `neutral.png` ← neutral, positive, enthusiastic, confident, concentrated; `thinking.png` ← thinking, serious | 255–263 |

## Uso deste levantamento

Este documento descreve o original completo como objeto de avaliação. Não recomenda trocá-lo pela intro reconstruída da demo nem substituir suas três rotas pela campanha nova do repositório curto. Qualquer integração precisa primeiro conservar a identidade das rotas, os pontos de retorno das cenas, estado de inventário/contatos, disponibilidade, amizade, registros e os resultados já existentes.

Para o HTML neutro de avaliação, mostrar separadamente: abertura real com objetos, mochila/contatos/notebook, cenas e elenco de cada rota, atividades reais, efeitos de escolhas e limites online/offline. Imagens de software exibidas na história devem ser identificadas como artefatos da narrativa. Não atribuir ao jogo original o desktop/e-mail, os botões textuais da campanha curta ou produtos com outros nomes.

