# Integração da demo curta e rotas longas Startup e Corporativo

Data: 2026-11-02. Branch: `integracao-rotas` (worktree `Requirements-Whisper-integracao`, criada a partir de `migracao-8.5.3`).

## Objetivo

Usar esta versão longa como base única do jogo. Trazer da demo curta (`Documents/GitHub/Requirements-Whisper`, commits de 2026-10-29) os mecanismos que melhoram o aprendizado. Escrever versões longas das vagas Startup e Corporativo, que hoje voltam para a escolha da vaga.

## Situação de partida

- Saúde: 22 cenas, cerca de 13 mil palavras, lint limpo no 8.5.3, sem testes automatizados.
- Startup e Corporativo: só o texto da vaga em `scene_1_quarto`; a `scene_2_escritorio` manda o jogador escolher de novo.
- Demo curta: 3 contextos curtos (reservas, gastos, chamados) com decisões que têm distratores e feedback, planejamento, negociação, escrita livre com autoavaliação, notebook de registros, acessibilidade, 27 testes no motor e build Windows. A arte dos personagens da demo é a mesma da longa, com outros nomes.

## Decisões

1. **Fluxo por rota.** `label start` continua chamando `scene_1_quarto`. Depois dela, `chosen_job` escolhe a cadeia: a da saúde fica como está, dentro do ramo `else`, com os mesmos `from`; Startup e Corporativo ganham `call rota_startup` e `call rota_corporativo`, cada uma com sua cadeia de cenas. O epílogo é comum. A `scene_2_escritorio` deixa de mandar o jogador de volta: os ramos startup/corporativo saltam para a chegada de cada rota. Isso revoga o item 4 de `restricoes-e-decisoes.md` §2, que foi escrito quando as rotas não existiam. Nenhum label ou variável existente é renomeado.
2. **Equipes próprias.** Cada empresa tem sua equipe: 4 pessoas na equipe e 2 stakeholders por rota (12 personagens novos). Reaproveitar os 8 colegas da saúde em outras empresas confundiria quem joga mais de uma rota, e trocar só o nome da arte repetiria o problema da demo.
3. **Mecânicas por rota.** Contatos, disponibilidade, amizade e cálculo do final passam a ler a lista de personagens da rota. Os ids novos ganham `default` próprios. A saúde continua lendo exatamente as mesmas variáveis.
4. **Chat dos personagens novos.** Os assistentes remotos (`asst_…`) só conhecem o projeto de saúde e não temos acesso ao servidor para criar outros. Personagens sem `assistant_id` respondem com falas roteirizadas locais, sem rede. A regra de threading do chat continua valendo para os personagens com backend.
5. **Ideias da demo a trazer** (conforme a análise de 2026-11-02):
   - decisões com distratores, feedback e revisão orientada sem punição: nas cenas pedagógicas da saúde (6, 12) e em todas as rotas novas;
   - sequência elicitação → ambiguidade → critério de aceitação → caso limite: espinha dos atos 2 e 3 das rotas novas, usando o conteúdo da demo como semente;
   - planejamento com capacidade (2 de 4 itens): reunião de gerenciamento;
   - negociação de mudança com dois acordos válidos: arquitetura/gerenciamento;
   - escrita livre de requisito e critério com autoavaliação: fim da especificação;
   - notebook de registros: o item notebook da Mochila abre a tela de registros da rota;
   - perfil sem idade e com nome saneado (`{` e `[` quebram falas);
   - acessibilidade: texto maior, texto instantâneo, transições, Mochila por teclado;
   - testes no motor e script de build Windows;
   - resumo honesto de aprendizagem no epílogo.
   Fica de fora: a preparação point-and-click (a longa já tem arte do quarto), os menus de repetir missão e a paleta da demo.
6. **Assets.** Reaproveitar os fundos genéricos: quarto, cozinha, trânsito, sala de reuniões, café, refeitório, escritório e fachada de vidro (a fachada serve à corporação). Gerar com o Codex (skill `imagegen`) os sprites dos 12 personagens novos (3 poses cada, mesma especificação dos atuais: PNG RGBA 1024x1536, corpo inteiro, contorno fino, cel shading), os fundos que faltam (escritório da startup, auditório do demo day, central de atendimento, sala de servidores) e as telas de produto de cada rota. Os retratos saem por recorte da pose neutra, sem nova geração. Toda imagem gerada passa por revisão visual antes de entrar no jogo.
7. **Correções encontradas no mapeamento** que afetam as três rotas: placeholders visíveis (s14, s16), id cru no menu da s5, badges inalcançáveis (DevOps, Teamwork, Guardião da Privacidade), `amizade_x +=` sem limite, caminho "descansar" da s18 que impede o final excelente, epílogo de conquistas comentado.

## Fases e orquestração

| Fase | Executor | Saída | Verificação |
|---|---|---|---|
| F0 Mapeamento | 4 agentes Claude em paralelo | mapa de cenas, mecânicas, assets e ideias da demo | concluída |
| F1 Bíblias das rotas | 2 agentes Claude (uma rota cada) | elenco, empresa, produto, arco de 8 semanas, cena a cena, objetivos de aprendizagem, especificação de arte | revisão do orquestrador |
| F2 Infraestrutura | 1 agente Claude, em série | despacho por rota, dados de rota, contatos/amizade/chat offline, notebook de registros, perfil, acessibilidade, base de testes | lint limpo + testes |
| F3 Assets | Codex `exec` (até 3 em paralelo) + revisão por agente Claude | sprites, fundos e telas em `game/images/` | revisão visual; recorte e tamanho por script |
| F4 Conteúdo | agentes Claude por ato, um arquivo por agente; revisor por rota | cenas das rotas Startup e Corporativo; mecanismos da demo nas cenas da saúde; correções | lint + revisão de consistência e pedagogia |
| F5 Integração | orquestrador + agentes de correção | rotas completas jogáveis | lint limpo, testes de ponta a ponta nas 3 rotas |
| F6 Entrega | orquestrador | build Windows, README/CLAUDE.md/AGENTS.md, decisões atualizadas | build verificado, revisão final |

F3 e F4 rodam em paralelo: as cenas usam nomes de imagem definidos na F2; até a arte chegar, o `missing_image_callback` mostra o placeholder.

## Regras de execução

- Não renomear labels nem variáveis existentes; toda variável nova tem um único `default`.
- Lint 100% limpo ao fim de cada fase; qualquer saída do lint é regressão.
- Agentes escrevem só arquivos novos ou os arquivos atribuídos a eles; arquivos compartilhados (`script.rpy`, `data/*`, `logic/*`) só na F2 ou pelo orquestrador.
- Texto em português, tom igual ao da versão longa, flexão de gênero do jogador via `player_gender` quando houver.
- Commits por fase na branch `integracao-rotas`. Nada é enviado ao GitHub sem confirmação.
