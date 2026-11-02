# Bíblia da rota Corporativo

Rota da vaga 3 de `scene_1_quarto` (`chosen_job == "corporativo"`): estágio em manutenção de sistemas legados numa grande corporação nacional. Este documento orienta a F2 (infraestrutura), a F3 (arte) e a F4 (texto das cenas). Segue as decisões de `docs/plans/2026-11-02-integracao-rotas.md`.

Arquivo de assets que acompanha esta bíblia: `docs/rotas/corporativo-assets.json`.

## 1. Visão geral

### Empresa
**Grupo Vértice**, empresa de distribuição de energia com 18 mil funcionários em 22 estados. Sede numa torre de vidro no Rio (fundo `empresa_exterior_manha`/`_noite`). O estágio fica na Coordenação de Sistemas Corporativos, dentro da Diretoria de TI.

### Produto legado
**SGC (Sistema de Gestão de Chamados)**, criado em 2008: Java 6 com telas JSF e banco Oracle cheio de rotinas PL/SQL. A central de atendimento interna usa o SGC para tratar cerca de 1.300 chamados por dia, com 140 atendentes. São 16 anos de regras acumuladas, nenhum teste automatizado e um manual de 2011 (`SGC_manual_v3_FINAL_revisado2.doc`) que ninguém atualiza.

O problema: funcionários de todo o país abrem chamados (VPN, senha, notebook, sistemas de campo) e não conseguem ver o que foi feito. Ligam para a central para perguntar. Muitos chamados aparecem como "Resolvido" com o campo Solução vazio.

### Projeto da rota
**Projeto Farol**: um módulo novo de acompanhamento, construído ao lado do SGC, em oito semanas. Escopo da primeira entrega:
- a pessoa solicitante consulta o chamado pelo número e vê estado, quem atende e a solução registrada;
- o atendente não consegue resolver um chamado sem descrever a solução;
- toda mudança de estado vai para uma trilha de auditoria que não pode ser editada;
- perfis com permissões diferentes (RBAC): solicitante, atendente, supervisor e admin;
- carga das descrições históricas do SGC para a nova tabela de histórico;
- implantação numa janela de mudança aprovada pelo CAB.

A semente vem do contexto "Empresa legada" da demo (chamado sem registro, estado Resolvido com descrição, descrição vazia como caso limite, aviso por WhatsApp negociado, reabrir chamado como escrita livre), agora dentro de um projeto de oito semanas.

### Regra escondida (fio condutor técnico)
Na semana 2 o jogador descobre a rotina `TRG_FECHA_SENHA_72H`: desde 2013 o banco resolve sozinho os chamados de "Reset de senha" sem retorno do solicitante depois de 72 h, sem descrição. Ela explica parte dos "Resolvido" vazios, vira o defeito de inconsistência na inspeção (semana 3), um teste de caracterização (semana 6) e um item da regressão (semana 7). A decisão tomada na semana 3: a rotina continua, mas grava a descrição padrão "Encerrado automaticamente após 72 h sem retorno do solicitante" e registra a ação na trilha como "sistema".

### Arco das 8 semanas
| Semana | Cenas | O que acontece |
|---|---|---|
| 1 | co_01 a co_03 | Chegada, equipe, SGC; ciclo de vida adaptado a legado, tipos de manutenção e ITIL. |
| 2 | co_04 a co_08 | Engenharia reversa (dados, código, pessoas); entrevista com Rosângela e Edson; classificação dos requisitos; café. |
| 3 | co_09 a co_12 | Histórias de usuário, casos de uso, critério e caso limite; almoço; inspeção e escrita livre. |
| 4 | co_13 a co_14 | Arquitetura de transição e auditoria; pedido do WhatsApp negociado; 25 anos de casa do Jorge. |
| 5 | co_15 | Capacidade (2 de 4), RFC para o CAB, risco da carga do histórico e ensaio. |
| 6 | co_16 | Testes de caracterização, mudança pequena, revisão de pull request. |
| 7 | co_17 | Perfis, regressão, senha em arquivo de configuração, teste de aceitação na central, CAB aprova. |
| 8 | co_18 | Janela de sábado, problema na carga, decisão de rollback parcial, avaliação com os stakeholders. |

### Glossário usado nas falas
- **Incidente**: algo parou e precisa voltar a funcionar. **Problema**: a causa de um ou mais incidentes. **Mudança**: alteração planejada no ambiente de produção.
- **RFC** (pedido de mudança): documento com o que muda, impacto, janela, testes, plano de volta e responsáveis.
- **CAB** (comitê de mudanças): aprova ou devolve RFCs; reúne-se às quintas. Mudança **normal** passa pelo CAB; **padrão** é pré-aprovada (ex.: troca de senha de serviço); **emergencial** é só para restaurar serviço.
- **Janela de mudança**: horário combinado para implantar (aqui, sábado 0h às 4h).
- **Rollback**: voltar ao estado anterior. **Critério de parada**: condição combinada que manda voltar.
- **SLA**: prazo combinado de atendimento. **TMA**: tempo médio de atendimento por chamado.
- **Estrangulamento** (strangler fig; nas falas, "figueira mata-pau"): o sistema novo cresce ao lado do velho e assume uma função por vez.
- **Camada anticorrupção**: tradutor entre o modelo do SGC e o modelo do Farol.
- **Teste de caracterização**: teste que registra o que o código faz hoje, certo ou errado, antes de mexer.

## 2. Elenco

Ids em minúsculas ASCII. Ordem dos contatos da rota: `co_mentora`, `co_legado`, `co_dev`, `co_qualidade`, `co_supervisora`, `co_solicitante`. Nenhum tem `assistant_id`: o chat usa as falas roteirizadas da seção 7.

| Id | Nome | Papel | Cor |
|---|---|---|---|
| co_mentora | Valéria Nogueira | Analista de sistemas sênior (requisitos e processos); guia do jogador | `#E86A5C` |
| co_legado | Jorge Takeda | Desenvolvedor sênior do SGC desde 2008 | `#C9A27E` |
| co_dev | Kauã Ferreira | Desenvolvedor pleno do módulo Farol | `#8FD14F` |
| co_qualidade | Ingrid Batista | Analista de qualidade, testes e gestão de mudanças | `#9BB8F0` |
| co_supervisora | Rosângela Arruda | Stakeholder: supervisora da central de atendimento | `#D98FD0` |
| co_solicitante | Edson Moura | Stakeholder: coordenador de manutenção de campo, solicitante frequente | `#F0C987` |

### Valéria Nogueira (`co_mentora`)
- **Personalidade**: calma, organizada, paciente. Começou como atendente da central em 2004 (foi colega de Rosângela) e passou para a TI em 2009. Por isso defende ouvir quem usa o sistema.
- **Jeito de falar**: frases completas, tom acolhedor; bordão "Vamos por partes". Explica sigla na primeira vez que usa. Nunca dá a resposta antes de perguntar o que o jogador acha.
- **Contato**: "Analista sênior de requisitos. Sua mentora no Projeto Farol. Começou atendendo telefone na central."
- **Arco**: conduz o jogador do "ouvir" ao "registrar"; no fim, deixa o jogador conduzir a avaliação.

### Jorge Takeda (`co_legado`)
- **Personalidade**: humor seco, contador de histórias, protetor do SGC sem ser teimoso. Guarda a memória do sistema na cabeça e sabe que isso é um risco. Vai se aposentar em março (revelado na co_14).
- **Jeito de falar**: "Isso aí tem história."; datas e apelidos ("o servidor Tia Neide"); frases curtas com uma piada no fim. Trata todos pelo nome.
- **Contato**: "Desenvolvedor do SGC desde 2008. Sabe onde cada regra nasceu. Caneca de 2008 inclusa."
- **Arco**: de "está tudo na minha cabeça" a gravar os "Causos do SGC" no wiki.

### Kauã Ferreira (`co_dev`)
- **Personalidade**: animado, rápido, gosta de tecnologia nova; queria reescrever o SGC inteiro em microsserviços. Aprende a trocar o sistema por partes. Estuda IA para triagem de chamados à noite.
- **Jeito de falar**: informal, "Bora!", "kkk" no chat, metáforas de série e jogo. Admite erro sem drama.
- **Contato**: "Dev do módulo Farol. Fã de código novo, aprendendo a respeitar o velho. Topa pair a qualquer hora."
- **Arco**: da reescrita total ao estrangulamento; aprende com a revisão do jogador (co_16) que validação só na tela não basta.

### Ingrid Batista (`co_qualidade`)
- **Personalidade**: direta, rigorosa, ironia leve. Cuida do plano de testes, da segurança do módulo e das RFCs. Tem fama de "chata do CAB" e sabe disso; protege as pessoas de mudanças mal planejadas desde o incidente de 2019.
- **Jeito de falar**: "Se não está registrado, não aconteceu."; listas curtas; humor de checklist ("registrado como incidente, prioridade baixa").
- **Contato**: "Qualidade, testes e gestão de mudanças. Se não está registrado, não aconteceu."
- **Arco**: mostra que processo serve para proteger quem trabalha, não para travar.

### Rosângela Arruda (`co_supervisora`)
- **Personalidade**: cordial e firme; mede tudo em SLA e TMA; defende o tempo da equipe dela. Resiste à descrição obrigatória até ver o dado das ligações de cobrança.
- **Jeito de falar**: "minha equipe", números de cabeça, pouca paciência para jargão de TI.
- **Contato**: "Supervisora da central de atendimento. Conhece cada fila do SGC e cada número do SLA."

### Edson Moura (`co_solicitante`)
- **Personalidade**: prático, caloroso, sempre na rua. Coordena equipes de manutenção de campo na Baixada Fluminense. Liga para a central várias vezes por semana. Pede o aviso por WhatsApp porque técnico de campo não abre a intranet.
- **Jeito de falar**: informal, histórias de campo, "Fala!", pede para testar em vez de imaginar.
- **Contato**: "Coordenador de manutenção de campo. Abre chamado toda semana e quer saber o que foi feito."

### Figurantes sem sprite
- Colega de república (`npc_roommate`, arte existente) na co_03.
- Atendentes da central (citados: Neusa e Paulo) e o técnico de campo Wellington (citado no episódio da VPN). Só narrados.

## 3. Mecânicas da rota

### Padrão de decisão pedagógica (vem da demo)
1. Menu com 1 opção adequada e 2 distratores plausíveis, em ordem variada.
2. Na opção adequada: `$ co_ok_<x> = True` e `$ co_score += 1` dentro do bloco do menu (seguro com rollback) e uma fala que explica por que funciona.
3. Em cada distrator: fala que explica a consequência concreta no Grupo Vértice.
4. `if not co_ok_<x>:` abre um menu de revisão com uma única opção (a reformulação), seguida de confirmação. Revisão não soma ponto e não tira amizade.
5. Decisões pedagógicas não mexem em amizade. Amizade vem só dos menus sociais (`add_friendship_point(id, 1)`). Assim aprender e se relacionar ficam separados, e errar não custa amizade.

São 21 decisões pedagógicas na rota (lista na seção 4). O resumo honesto do epílogo pode mostrar "X de 21 decisões adequadas antes do feedback" e a lista "você fez / com apoio, você fez" por competência.

### Planejamento (co_15) e negociação (co_13)
Mesmos mecanismos da demo (`scene_3_planejamento` e `scene_4_negociacao`), com variáveis `co_plano_*` e `co_negociacao_*`. Sem nota. A negociação tem duas opções ruins que voltam ao menu e dois acordos válidos.

### Escrita livre (co_11)
Mesma tela da demo (`transfer_input`/`transfer_review`, a F2 decide o nome final). Pedido: reabrir um chamado resolvido quando a solução falhar. Texto exibido com `.replace("{", "{{")` e `substitute False`. O jogo diz que não avalia o significado do texto.

### Disponibilidade e contatos
Cada cena começa com `set_available(...)` usando só ids da rota. Os quatro da equipe entram como contato na co_01 (`add_contact` + 1 ponto de amizade cada); os dois stakeholders na co_05. As cenas de casa (co_03, co_08, co_12) chamam `call screen contacts_screen`.

### Variáveis novas (todas com um único `default`)
| Variável | Default | Uso |
|---|---|---|
| `co_score` | 0 | decisões adequadas na primeira escolha (0 a 21) |
| `co_ok_manutencao`, `co_ok_fontes`, `co_ok_episodio`, `co_ok_ambiguidade`, `co_ok_conflito`, `co_ok_class_nf`, `co_ok_class_restricao`, `co_ok_criterio`, `co_ok_caso_limite`, `co_ok_insp_ausente`, `co_ok_insp_ambiguo`, `co_ok_insp_inconsistente`, `co_ok_arquitetura`, `co_ok_auditoria`, `co_ok_cab`, `co_ok_risco`, `co_ok_abordagem`, `co_ok_review`, `co_ok_rbac`, `co_ok_regressao`, `co_ok_janela` | False | uma por decisão |
| `co_reg_manutencao`, `co_reg_legado`, `co_reg_elicitacao`, `co_reg_classificacao`, `co_reg_criterio`, `co_reg_inspecao`, `co_reg_transicao`, `co_reg_verificacao` | False | registros do notebook descobertos |
| `co_conq_arqueologia`, `co_conq_escuta`, `co_conq_inspetor`, `co_conq_acordo`, `co_conq_transicao`, `co_conq_rede`, `co_conq_trilha`, `co_conq_janela`, `co_conq_memoria` | False | conquistas |
| `co_negociacao_opcao` | "" | "base_primeiro" ou "investigar_agora" |
| `co_negociacao_acordo` | "" | texto do acordo confirmado |
| `co_negociacao_sem_atalho` | False | vira True ao abrir a negociação e False se o jogador escolher uma opção ruim |
| `co_negociacao_completa` | False | acordo confirmado |
| `co_plano_selecionados` | [] | índices escolhidos (0 a 3) |
| `co_plano_cobertura` | 0 | itens necessários no plano (0 a 2) |
| `co_plano_completo` | False | plano conferido |
| `co_escrita_requisito`, `co_escrita_criterio` | "" | texto livre do jogador |
| `co_escrita_status` | "" | "rascunho" ou "pendente" |
| `co_almoco_mesa` | "" | "jorge_ingrid" ou "valeria_kaua" |
| `co_contribuicao_festa` | "" | "bolo", "vaquinha" ou "cartao" |
| `co_homenagem_jorge` | "" | "wiki", "brinde" ou "piada" |
| `co_senha_relato` | "" | "registro", "historia" ou "grupo" |
| `co_amizade_total` | 0 | soma das quatro amizades da equipe (calculada na co_18) |
| `co_conq_total` | 0 | conquistas de aprendizagem (0 a 8, calculada na co_18) |
| `co_final_grade` | "" | "excelente", "bom" ou "ok" |

A F2 cria também `contato_*`, `disponivel_*` e `amizade_*` para os seis ids, conforme a decisão 3 do plano.

## 4. Lista das decisões pedagógicas

| # | Cena | Variável | Competência |
|---|---|---|---|
| 1 | co_02 | co_ok_manutencao | entender o legado antes de mudar |
| 2 | co_04 | co_ok_fontes | engenharia reversa por fontes cruzadas |
| 3 | co_05 | co_ok_episodio | pedir um episódio concreto |
| 4 | co_05 | co_ok_ambiguidade | trocar "fácil" por tarefa e resultado |
| 5 | co_05 | co_ok_conflito | mediar conflito com objetivo comum e dado |
| 6 | co_06 | co_ok_class_nf | reconhecer requisito não funcional |
| 7 | co_06 | co_ok_class_restricao | reconhecer restrição |
| 8 | co_09 | co_ok_criterio | critério de aceitação verificável |
| 9 | co_09 | co_ok_caso_limite | caso limite confirmado |
| 10 | co_11 | co_ok_insp_ausente | defeito: informação ausente |
| 11 | co_11 | co_ok_insp_ambiguo | defeito: ambiguidade |
| 12 | co_11 | co_ok_insp_inconsistente | defeito: inconsistência |
| 13 | co_13 | co_ok_arquitetura | arquitetura de transição (estrangulamento) |
| 14 | co_13 | co_ok_auditoria | modelagem da trilha de auditoria |
| 15 | co_15 | co_ok_cab | RFC normal para o CAB |
| 16 | co_15 | co_ok_risco | resposta a risco de migração de dados |
| 17 | co_16 | co_ok_abordagem | testes de caracterização antes de mudar |
| 18 | co_16 | co_ok_review | revisão de pull request que acha o defeito real |
| 19 | co_17 | co_ok_rbac | testes negativos por perfil |
| 20 | co_17 | co_ok_regressao | escopo da regressão |
| 21 | co_18 | co_ok_janela | seguir o critério de parada na janela |

## 5. Notebook de registros (8)

| Variável | Título | Conteúdo | Cena |
|---|---|---|---|
| co_reg_manutencao | Manutenção e mudança controlada | Manutenção corretiva conserta defeito; adaptativa acompanha mudança de ambiente; evolutiva acrescenta ou melhora uma função; preventiva reduz risco futuro. O Farol é evolutiva. Em produção, toda mudança segue um caminho: RFC, avaliação do CAB, janela combinada, plano de volta e revisão depois da implantação. Incidente restaura o serviço; problema investiga a causa. | co_02 |
| co_reg_legado | Ler o legado antes de mudar | Documentação antiga mostra o que alguém planejou, não o que roda hoje. Cruze três fontes: dados reais, código (inclusive rotinas do banco) e quem usa. Quando duas fontes discordam, há uma pergunta para a entrevista. Achado: a rotina das 72 h resolve chamados de senha sem descrição. | co_04 |
| co_reg_elicitacao | Episódio, palavra vaga e conflito | Comece pedindo a última vez que o problema aconteceu. Troque "fácil" pelo que a pessoa precisa conseguir fazer. Em conflito entre stakeholders, pergunte o que cada um quer evitar e procure um dado que os dois aceitem: 18% das ligações da central eram cobrança de andamento. | co_05 |
| co_reg_classificacao | O que é o quê | Funcional: o que o sistema faz (consultar estado e solução). Não funcional: como ele deve se comportar, com número (3 s para 95% das consultas com 1.500 usuários no pico). Restrição: limite imposto à solução (não alterar tabelas do SGC sem CAB). Desejo: ideia sem necessidade confirmada (tema escuro com mascote). Cada tipo é verificado de um jeito. | co_06 |
| co_reg_criterio | História, critério e caso limite | Como solicitante, quero consultar o estado e a solução do meu chamado, para não precisar ligar para a central. Critério: dado um chamado Em atendimento, quando o suporte registra a solução e muda para Resolvido, a consulta mostra Resolvido e o texto registrado. Caso limite: descrição vazia mantém Em atendimento e orienta o preenchimento. | co_09 |
| co_reg_inspecao | Inspeção de requisitos | Procure o que falta (quem, quando, condição), o que tem duas leituras ("rápida") e o que briga com outra regra (bloqueio sem descrição x rotina das 72 h). Conflito se resolve com quem é dono da regra. Autoavaliação: quem age e sob qual condição; dados iniciais e resultado observável; o que não pode mudar ou deve ser recusado. | co_11 |
| co_reg_transicao | Trocar o motor com o avião voando | O Farol cresce ao lado do SGC, atrás de uma camada que traduz os dados, e assume uma função por vez. A trilha de auditoria é uma tabela só de inclusão: quem, perfil, quando, ação, valor anterior e novo. Pedido novo no meio do caminho: mostrar o impacto, combinar a prioridade e registrar o acordo. | co_13 |
| co_reg_verificacao | Regressão, perfis e trilha | Regressão confirma que o que já funcionava continua funcionando, inclusive o que o Farol só toca de leve. Perfil se testa pelo "não": cada um tenta o que não pode e recebe acesso negado, registrado na trilha. Botão escondido não é controle de acesso. Senha não fica em arquivo do repositório: vai para o cofre, é trocada e o caso é registrado sem procurar culpados. | co_17 |

## 6. Conquistas e final

### Conquistas
| Variável | Nome | Cena | Condição |
|---|---|---|---|
| co_conq_arqueologia | Arqueologia do Legado | fim da co_04 | `co_ok_manutencao and co_ok_fontes` |
| co_conq_escuta | Escuta que Pergunta | fim da co_05 | pelo menos 2 de `co_ok_episodio`, `co_ok_ambiguidade`, `co_ok_conflito` |
| co_conq_inspetor | Inspeção em Dia | fim da co_11 | pelo menos 2 das 3 inspeções adequadas e `co_escrita_status == "rascunho"` |
| co_conq_acordo | Acordo Registrado | co_13, ao confirmar | `co_negociacao_sem_atalho` (chegou ao acordo sem escolher opção ruim) |
| co_conq_transicao | Troca com o Avião Voando | fim da co_13 | `co_ok_arquitetura and co_ok_auditoria` |
| co_conq_rede | Rede de Regressão | fim da co_17 | `co_ok_abordagem and co_ok_regressao` |
| co_conq_trilha | Guardião da Trilha | fim da co_17 | `co_ok_review and co_ok_rbac` |
| co_conq_janela | Janela Cumprida | co_18, após a decisão | `co_ok_janela and (co_ok_cab or co_ok_risco)` |
| co_conq_memoria | Memória Viva (social) | co_14, menu da homenagem | escolher "wiki" e `get_friendship_point("co_legado") >= 5` depois do ponto do menu |

Ao conceder, mostrar um aviso curto ("Conquista: Arqueologia do Legado"). Todas são alcançáveis numa partida: as oito de aprendizagem dependem só de acertar de primeira, e a social depende de pontos que o roteiro oferece antes e durante a co_14 (até 12 com Jorge, limitado a 10; bastam 5).

### Regra do final (calculada na co_18)
- `co_amizade_total` = soma de `get_friendship_point` de `co_mentora`, `co_legado`, `co_dev`, `co_qualidade` (0 a 40).
- `co_conq_total` = quantas das 8 conquistas de aprendizagem foram ganhas (todas menos `co_conq_memoria`).
- **excelente**: `co_amizade_total >= 20 and co_conq_total >= 4`.
- **bom**: `co_amizade_total >= 15 or co_conq_total >= 5`.
- **ok**: nos outros casos.

Os limiares mantêm a proporção da saúde (40 de 80 e 30 de 80 viram 20 de 40 e 15 de 40). Os menus sociais oferecem cerca de 25 pontos à equipe sem contar o chat, então 20 é alcançável jogando com atenção às pessoas. Falas extras: `co_conq_memoria` libera a fala final do Jorge sobre o wiki; `co_amizade_total >= 28` libera uma fala coletiva da equipe.

## 7. Falas roteirizadas do chat offline

Mensagens curtas que funcionam em qualquer ponto da rota. A F2 sorteia ou percorre a lista; sem emojis (a fonte pode não ter os glifos).

**Valéria (`co_mentora`)**
1. Oi! Tô fechando uma ata aqui. Vamos por partes: o que te deixou com dúvida hoje?
2. Dica de quem começou atendendo telefone: antes de propor solução, pergunta "quando foi a última vez que isso aconteceu?".
3. Se a palavra é "fácil", "rápido" ou "intuitivo", ainda não é requisito. Pergunta o que a pessoa precisa conseguir fazer.
4. Critério de aceitação bom tem situação inicial, ação e um resultado que alguém consegue conferir.
5. A Rosângela parece dura, mas ela protege a equipe dela. Entender isso ajuda na conversa.
6. Descansa também. Estágio é maratona de oito semanas, não tiro de cem metros.
7. Mudança em produção sem RFC, nem pensar. A Ingrid tem razão em insistir nisso.
8. Anotou no notebook? O que não foi registrado a gente esquece até segunda.

**Jorge (`co_legado`)**
1. Isso aí tem história. Em 2008 o SGC rodava num servidor que a gente chamava de Tia Neide. Não pergunte.
2. Manual de 2011? Lê como curiosidade. Quem manda é o que está rodando no banco.
3. Antes de apagar uma regra estranha, descobre por que ela nasceu. Quase sempre foi um incêndio.
4. Trigger é aquele código que ninguém lembra que existe até aparecer num relatório.
5. Tô tomando café na caneca de 2008. Ela já sobreviveu a três reestruturações.
6. Teste de regressão é o jeito educado de dizer "não confio na minha memória". E faz bem.
7. Se eu me aposentar e ninguém souber das rotinas noturnas do SGC, a culpa é minha. Me cobra.
8. Pergunta boba não existe. Existe pergunta que eu respondi em 2012 e esqueci de documentar.

**Kauã (`co_dev`)**
1. Bora! Tô com três abas de documentação do Oracle abertas e nenhuma me ajudando kkk
2. Confesso: se dependesse de mim, eu reescrevia o SGC inteiro. O Jorge vive dizendo que não é tão simples.
3. Se o teste passou de primeira, desconfia um pouco. Vê se ele testa mesmo o que você acha.
4. Validação só na tela não vale. A API tem que recusar também.
5. Tô ouvindo lo-fi e lendo PL/SQL. Combinação estranha, mas funciona.
6. Me chama pra pair quando quiser. Explicar pra alguém me ajuda a achar meus próprios bugs.
7. Camada anticorrupção parece nome de série policial, mas é só um tradutor entre dois sistemas.
8. Commit pequeno, mensagem clara. Aprendi do jeito difícil num PR de duas mil linhas.

**Ingrid (`co_qualidade`)**
1. Se não está registrado, não aconteceu. Vale para requisito, teste e mudança.
2. RFC sem plano de rollback eu devolvo antes do CAB. Nada pessoal.
3. Perfil se testa pelo lado do "não": o atendente tenta abrir a auditoria e tem que dar acesso negado.
4. Toda vez que acho senha em arquivo de configuração eu respiro fundo. Registra, troca, sem caça às bruxas.
5. Mudança emergencial é para restaurar serviço, não para furar fila.
6. Tô revisando o plano de testes. Se quiser ver, vem. É menos chato do que parece.
7. Dica de inspeção: procura o que falta, o que tem duas leituras e o que briga com outra regra.
8. O café da copa hoje tá horrível. Registrado como incidente, prioridade baixa.

**Rosângela (`co_supervisora`)**
1. Oi, tudo bem? Tô no pico das nove, respondo direitinho depois.
2. Meu indicador é SLA, mas o que me tira o sono é atendente respondendo a mesma pergunta três vezes.
3. Se for mexer no fechamento de chamado, me avisa antes. Minha equipe precisa de treinamento.
4. Quer entender a central? Senta uma manhã do lado de um atendente. Vale mais que reunião.
5. Descrição obrigatória eu aceito, desde que seja curta e tenha modelo pronto para os casos comuns.
6. A trilha de auditoria me salvaria uma semana na auditoria interna de 2021. Não deixa isso de lado.
7. Se tiver dúvida de regra, pergunta pra mim. Prefiro pergunta agora do que retrabalho depois.
8. Bom trabalho hoje. Agora vai descansar, que amanhã tem fila.

**Edson (`co_solicitante`)**
1. Fala! Tô na estrada indo pra uma subestação. Se eu sumir, é falta de sinal.
2. Meu problema é simples: quero saber o que fizeram no chamado sem ter que ligar.
3. Técnico de campo não abre intranet. Abre o celular. Pensa nisso.
4. Quando o chamado diz "resolvido" e o problema continua, eu quero poder reabrir.
5. Pode me mandar a tela pra eu testar? Prefiro testar do que imaginar.
6. Esse negócio de aviso no WhatsApp, se não der agora, me explica o porquê que eu entendo.
7. Choveu tanto aqui que a equipe parou. Boa hora pra testar sistema.
8. Valeu por ouvir a gente do campo. Normalmente ninguém pergunta.

## 8. Arte

### Estilo
Mesma especificação dos sprites atuais: PNG RGBA 1024x1536, corpo inteiro em pé, contorno fino escuro, cel shading chapado com 1 ou 2 tons de sombra, proporção realista (cerca de 7 cabeças), paleta natural levemente dessaturada, fundo transparente com halo suave. A expressão vem mais da pose do que do rosto. Retrato recortado da pose neutral. Fundos em 1536x1024, família `escritorio_interior` (anime/cel, contorno de tinta, leve grão, sem texto legível, figurantes de costas), com a regra de cor por horário: manhã azul-petróleo frio com luz amarelada, tarde laranja/magenta, noite azul-marinho.

### Sprites (equipe: neutral, thinking, serious; stakeholders: neutral, thinking)

**Valéria Nogueira** — 46 anos aparentes, mulher negra de pele retinta, cabelo crespo natural bem curto com fios grisalhos nas têmporas, óculos de armação retangular vermelha, brincos pequenos de argola dourada. Blazer mostarda sobre blusa branca de gola canoa, calça social preta de corte reto, sapatilha preta, crachá azul pendurado no pescoço, caderno de capa dura vinho. Postura ereta e tranquila.
- neutral: um passo à frente, palma da mão direita aberta estendida como quem convida a falar, caderno apoiado no antebraço esquerdo, sorriso sereno.
- thinking: mão no queixo com a caneta encostada no lábio inferior, olhar para o lado, peso numa perna só.
- serious: caderno abraçado junto ao peito com os braços cruzados por cima, cabeça levemente baixa olhando por cima dos óculos.

**Jorge Takeda** — 61 anos aparentes, homem nipo-brasileiro de pele clara amarelada, cabelo grisalho curto penteado para trás com entradas, bigode fino grisalho, óculos de leitura pendurados no pescoço por uma cordinha. Camisa social azul-clara de manga curta com caneta no bolso, colete de lã cinza sem mangas, calça de sarja cáqui, sapato social marrom gasto. Caneca branca lascada com uma faixa azul. Leve barriga, ombros um pouco curvados.
- neutral: segura a caneca com as duas mãos na altura do peito, ombros relaxados, meio sorriso de canto.
- thinking: uma mão coça a nuca, a outra segura os óculos de leitura afastados do rosto, olhar para cima como quem puxa memória.
- serious: braços cruzados, caneca pendurada num dedo, queixo baixo, olhar firme para frente.

**Kauã Ferreira** — 26 anos aparentes, homem brasileiro de ascendência indígena, pele morena acobreada, cabelo preto liso até os ombros preso em coque baixo, barba rala. Moletom verde-musgo com zíper aberto sobre camiseta preta lisa, calça jogger cinza, tênis branco, fones de ouvido grandes no pescoço, notebook prateado com adesivos coloridos sem texto. Corpo magro, postura inquieta.
- neutral: notebook debaixo do braço esquerdo, polegar direito para cima, corpo inclinado para frente, animado.
- thinking: notebook aberto apoiado no antebraço, outra mão no queixo, testa franzida olhando a tela.
- serious: mãos nos bolsos do moletom, ombros levemente erguidos, rosto virado de lado, olhar desconfiado.

**Ingrid Batista** — 34 anos aparentes, mulher branca de pele clara com sardas, estatura baixa e corpo largo, cabelo curto estilo pixie tingido de platinado com a raiz escura aparente, piercing pequeno na orelha, tatuagem de um sinal de check no pulso. Camisa xadrez azul-marinho e vinho aberta sobre camiseta cinza, calça jeans escura, coturno preto de cano baixo, crachá preso no bolso. Tablet com caneta stylus.
- neutral: segura o tablet virado para frente mostrando uma lista com marcas de check, sorriso aberto, pés firmes.
- thinking: stylus apoiada na têmpora, tablet apoiado no quadril, olhar para o alto.
- serious: tablet abraçado ao peito com os braços cruzados por cima, sobrancelhas franzidas, pés afastados.

**Rosângela Arruda** — 54 anos aparentes, mulher parda de pele morena média, cabelo castanho-escuro ondulado na altura dos ombros com mechas acobreadas, headset de call center apoiado no pescoço, relógio dourado grande no pulso. Blusa de seda verde-esmeralda, calça social cinza-chumbo, scarpin baixo preto. Relatório impresso dobrado na mão. Postura de comando, cordial.
- neutral: ereta, uma mão segura o relatório na altura da cintura, a outra apoiada no quadril, leve sorriso.
- thinking: braço erguido olhando o relógio de pulso, sobrancelha arqueada, relatório preso debaixo do braço.

**Edson Moura** — 42 anos aparentes, homem negro de pele escura, cabeça raspada, barba curta bem aparada. Colete refletivo laranja de campo sobre camisa polo azul-marinho sem logotipo legível, calça de brim, botina de segurança marrom, capacete branco. Celular na mão. Corpo forte, postura aberta.
- neutral: capacete debaixo do braço esquerdo, celular na mão direita, ombros soltos, sorriso largo.
- thinking: olha a tela do celular com a testa franzida, mão livre na cintura, capacete pendurado no cinto.

### Fundos reaproveitados
`empresa_exterior_manha`, `empresa_exterior_noite`, `escritorio_interior_manha/tarde/noite/festa`, `sala_reunioes_manha/tarde`, `empresa_cafe_tarde`, `refeitorio_tarde`, `transito_noite`, `quarto_noite`, `cozinha_noite`.

### Fundos novos (4)
| Arquivo | Define | Descrição | Cenas |
|---|---|---|---|
| `images/bg/central_atendimento_manha.png` | `bg central_atendimento_manha` | Andar aberto de central de atendimento corporativa: fileiras de baias com divisórias baixas azul-acinzentadas, monitores duplos, headsets nas mesas, atendentes figurantes de costas. Um painel de TV grande na parede com barras e números de fila (sem texto legível). Janelas altas com persianas, carpete cinza, plantas, quadro com post-its. Luz fria da manhã com feixes amarelados. | co_04 |
| `images/bg/central_atendimento_tarde.png` | `bg central_atendimento_tarde` | Mesmo ambiente no fim da tarde: luz laranja e magenta entrando pelas persianas, menos atendentes, monitores acesos. | co_17, co_18 |
| `images/bg/sala_servidores.png` | `bg sala_servidores` | Corredor de data center sem janelas: racks pretos com LEDs azuis e verdes, piso elevado de placas perfuradas, ar-condicionado de precisão. No canto, um rack bege antigo destoando, com etiqueta de papel amarelada (o servidor "Tia Neide"). Mesa dobrável com notebook aberto e copos de café. Luz azulada artificial; serve a qualquer hora. | co_02, co_18 |
| `images/bg/sala_arquivo_tarde.png` | `bg sala_arquivo_tarde` | Sala de arquivo de documentação: estantes de aço com pastas suspensas e caixas-arquivo, fichários de lombadas coloridas, pilha de documentos encadernados em espiral sobre uma mesa, monitor de tubo velho num canto. Luz de fim de tarde laranja por uma janela basculante alta, poeira visível no feixe. | co_04 |

### Telas e artefatos (4)
| Arquivo | Descrição | Cenas |
|---|---|---|
| `images/artifacts/co_sgc_legado.png` | Tela do SGC com visual de sistema web de 2008: janela cinza, abas com degradê azul, tabela densa de chamados com fonte pequena, botões em relevo. Detalhe do chamado 48213 com estado "Resolvido" e o campo "Solução" vazio destacado. Rótulos curtos em português. | co_01, co_04, co_09 |
| `images/artifacts/co_farol_consulta.png` | Tela do módulo Farol, limpa e atual: cartão do chamado 48213 com linha do tempo Aberto, Em atendimento, Resolvido; nome do atendente; caixa "Solução registrada" com texto; botão "Reabrir chamado"; selo de perfil "Solicitante" no topo. | co_09, co_16, co_18 |
| `images/artifacts/co_farol_arquitetura.png` | Diagrama limpo de arquitetura de transição: à esquerda o bloco "SGC (JSF + Oracle)"; no meio "Camada anticorrupção / API de chamados"; à direita "Módulo Farol"; embaixo a tabela "historico_chamado (somente inclusão)"; perfis solicitante, atendente, supervisor, admin; seta tracejada para "Aviso WhatsApp (próxima rodada)". Fundo branco, caixas com cantos arredondados. | co_13, co_15 |
| `images/artifacts/co_farol_auditoria.png` | Tela de trilha de auditoria para supervisão: tabela com data e hora, usuário, perfil, ação, valor anterior e valor novo; uma linha com usuário "sistema" e a ação "Encerrado automaticamente após 72 h"; cadeado indicando registro imutável; aba lateral "Perfis" com matriz de permissões por perfil. | co_17, co_18 |

## 9. Cena a cena

Meta total: cerca de 9.850 palavras (faixa pedida: 8.000 a 10.000).

| Cena | Meta | Cena | Meta | Cena | Meta |
|---|---|---|---|---|---|
| co_01 | 500 | co_07 | 400 | co_13 | 750 |
| co_02 | 600 | co_08 | 300 | co_14 | 450 |
| co_03 | 300 | co_09 | 650 | co_15 | 650 |
| co_04 | 550 | co_10 | 400 | co_16 | 600 |
| co_05 | 800 | co_11 | 800 | co_17 | 600 |
| co_06 | 450 | co_12 | 300 | co_18 | 750 |

Soma: 9.850.

---

### ATO 1 — Descoberta

#### co_01_chegada — Chegada ao Grupo Vértice
- **Quando**: semana 1, segunda, 8h50 às 11h30.
- **Fundos**: `empresa_exterior_manha`, `escritorio_interior_manha`. Artefato `co_sgc_legado`.
- **Música**: `music_office_motivated`.
- **Presentes**: co_mentora, co_legado, co_dev, co_qualidade. `set_available()` (ninguém da rota disponível).
- **Resumo**: O jogador chega à torre de vidro do Grupo Vértice e passa pela recepção: crachá provisório, foto e um termo de confidencialidade que cita a LGPD. Valéria busca o jogador no saguão e explica onde fica a Coordenação de Sistemas Corporativos. No andar, ela apresenta Jorge (no SGC desde 2008, com a caneca da época), Kauã (cuida do módulo novo) e Ingrid (qualidade, testes e "a pessoa do CAB"); cada um vira contato com 1 ponto de amizade. Valéria abre o SGC no monitor: tela cinza, abas em degradê, e o chamado 48213 marcado como Resolvido com a Solução vazia. Ela explica o Projeto Farol: deixar quem abre chamado ver o que foi feito sem precisar ligar para a central. O prazo é de oito semanas, com implantação numa janela de sábado. Jorge comenta que o SGC tem 16 anos e nenhum teste automatizado; Kauã diz que "um dia isso vai ter que ser reescrito"; Ingrid aponta o calendário de mudanças na parede. Antes do almoço, o jogador escolhe com quem puxar conversa.
- **Objetivos**: conhecer o contexto de manutenção de um sistema legado numa corporação; ligar o problema (chamado sem registro) às pessoas que sofrem com ele; conhecer os papéis da equipe.
- **Menu social** — "Antes do almoço, com quem você puxa conversa?"
  - "Jorge, como era o SGC quando nasceu?" → `add_friendship_point("co_legado", 1)`. Jorge conta do servidor Tia Neide e do lançamento em 2008.
  - "Kauã, o que já existe do Farol?" → `add_friendship_point("co_dev", 1)`. Um protótipo de tela e muita vontade de reescrever tudo.
  - "Ingrid, o que é esse calendário na parede?" → `add_friendship_point("co_qualidade", 1)`. As janelas de mudança: "Nada sobe sem passar por aqui."
- **Estado**: `add_contact` dos quatro; nenhuma variável nova.
- **Registros**: nenhum.
- **Meta**: 500 palavras.

#### co_02_ciclo_legado — O ciclo de vida de um sistema que já existe
- **Quando**: semana 1, segunda, 14h às 17h30.
- **Fundos**: `sala_reunioes_tarde`; no fim, `sala_servidores`.
- **Música**: `music_office_concentrated_1`.
- **Presentes**: os quatro da equipe. `set_available()`.
- **Resumo**: Valéria desenha no quadro o ciclo de vida adaptado a um sistema que já roda: entender o que existe, levantar, especificar, projetar a transição, implementar com testes de regressão, mudar com aprovação, operar e aprender. Ela apresenta os tipos de manutenção (corretiva, adaptativa, evolutiva, preventiva) e pergunta ao jogador onde o Farol se encaixa: evolutiva. Ingrid explica em poucas falas a parte de ITIL que a equipe usa: incidente, problema, mudança, RFC, CAB e janela. Kauã defende reescrever o SGC em microsserviços; Jorge responde que uma reescrita de 2016 foi cancelada depois de 14 meses. Valéria pergunta ao jogador qual é o primeiro passo (decisão 1). Depois, um menu social fecha a reunião. Jorge leva o grupo até a sala de servidores para mostrar o rack bege da Tia Neide, que ainda guarda uma réplica do banco. Valéria pede que o jogador anote o ciclo no notebook (registro 1).
- **Objetivos**: diferenciar os tipos de manutenção; entender por que a mudança em produção segue um processo (RFC, CAB, janela, rollback); reconhecer o risco de mudar sem conhecer o comportamento atual.
- **Decisão 1** (`co_ok_manutencao`) — "Antes de mexer no SGC, qual é o primeiro passo?"
  - "Reescrever o SGC do zero numa tecnologia nova, para não herdar problemas." → Jorge: "A gente herdaria o pior problema: não saber o que o velho fazia. Tem regra lá dentro que nenhum documento cita. Foi isso que matou a reescrita de 2016."
  - **Adequada**: "Entender o que o sistema faz hoje e combinar testes de regressão para o que o Farol vai tocar." → `co_ok_manutencao = True`, `co_score += 1`. Valéria: "Mudar sem saber o que existe é apostar. Primeiro a gente conhece, depois a gente protege, aí sim a gente muda."
  - "Alterar direto a tela de fechamento; é uma mudança pequena." → Ingrid: "Em 2019 uma mudança pequena no fechamento quebrou o relatório mensal da diretoria. Pequena no código não quer dizer pequena no efeito."
  - **Revisão**: "Como você reformula?" → "Primeiro descobrir o que o sistema faz hoje e como vamos perceber se algo parar de funcionar." Valéria confirma.
- **Menu social** — "No fim da reunião, você pergunta…"
  - a Jorge: "Como vocês descobrem o que o SGC faz sem documentação?" → +1 co_legado.
  - a Ingrid: "Qual mudança já deu mais errado aqui?" → +1 co_qualidade (história de 2019, contada sem culpados).
  - a Valéria: "Posso acompanhar você nas conversas com a central?" → +1 co_mentora.
- **Registros**: `co_reg_manutencao`.
- **Meta**: 600 palavras.

#### co_03_casa_sem1 — Fim da semana 1
- **Quando**: semana 1, sexta, 19h30 às 22h.
- **Fundos**: `transito_noite`, `cozinha_noite`, `quarto_noite`.
- **Música**: `music_streets_focused`, depois `music_home_reflecting`.
- **Presentes**: npc_roommate (cozinha). `set_available('all')` da rota.
- **Resumo**: No ônibus, o jogador repassa a semana: crachá, sala gelada dos servidores, um sistema mais velho que alguns colegas de faculdade. Na cozinha, o colega de república pergunta se empresa grande é "só reunião"; o jogador explica, com humor, que até mudança tem formulário, e que isso tem motivo. No quarto, revisa no notebook os tipos de manutenção, o caminho de uma mudança e quem é quem. Chega mensagem de Valéria: ela separou 30 chamados reais do mês passado, sem dados pessoais, para lerem juntos na segunda. O jogador responde. Depois, a tela de contatos abre para conversar com alguém. Fecha com o cartão "Fim da Semana 1: num sistema legado, o ciclo começa entendendo o que já existe."
- **Objetivos**: consolidar manutenção e mudança controlada; mostrar o uso do celular e da disponibilidade.
- **Menu social** — resposta à Valéria:
  - "Valeu! Vou dar uma olhada e anotar as dúvidas." → +1 co_mentora.
  - "Preciso ler tudo no fim de semana?" → Valéria: "Não. Segunda a gente lê junto. Fim de semana é descanso." (0)
  - Só curtir a mensagem. (0)
- **Estado**: `call screen contacts_screen`.
- **Registros**: nenhum.
- **Meta**: 300 palavras.

### ATO 2 — Levantamento

#### co_04_preparacao — Arqueologia do SGC
- **Quando**: semana 2, segunda, 9h às 17h30.
- **Fundos**: `escritorio_interior_manha`, `central_atendimento_manha`, `sala_arquivo_tarde`. Artefato `co_sgc_legado`.
- **Música**: `music_office_concentrated_2`.
- **Presentes**: co_mentora, co_legado. `set_available("co_dev", "co_qualidade")`.
- **Resumo**: Valéria e o jogador leem os 30 chamados e notam nove marcados como Resolvido com a Solução vazia. A entrevista com Rosângela e Edson é na quarta, e Valéria explica que, num legado, a preparação começa descobrindo o que o sistema faz de verdade. Ela pergunta onde buscar isso (decisão 2). No fim da manhã, os dois sentam uma hora ao lado da atendente Neusa na central: o jogador vê as ligações de "e meu chamado?" e a troca de abas para achar a resposta. À tarde, Jorge leva os dois à sala de arquivo e acha o manual de 2011, que ainda cita o estado Pendente, extinto em 2015. Cruzando os dados com o código, o jogador percebe que sete dos nove chamados vazios são de "Reset de senha" fechados exatamente 72 h depois de abertos. Jorge lembra: a rotina `TRG_FECHA_SENHA_72H` nasceu em 2013, depois de uma greve, quando a fila de senha passou de três mil. Ninguém tinha registrado isso. O dia termina com o roteiro da entrevista: perguntas abertas, pedido de episódio, atenção a palavras vagas e ao conflito que Valéria espera entre as duas pontas.
- **Objetivos**: praticar engenharia reversa cruzando dados, código e pessoas; perceber que documentação antiga engana; preparar um roteiro de entrevista.
- **Decisão 2** (`co_ok_fontes`) — "Onde buscar o comportamento real do SGC antes da entrevista?"
  - "No manual de 2011; é a documentação oficial." → Jorge: "O manual diz que existe o estado Pendente. Ele sumiu em 2015. Você ia perguntar à Rosângela sobre um estado que não existe."
  - "Perguntar só ao Jorge; ele fez o sistema." → Jorge: "Agradeço a confiança, mas eu lembro do que eu fiz, não do que os outros mudaram depois. E eu não vou estar aqui para sempre."
  - **Adequada**: "Cruzar fontes: chamados reais, o código e as rotinas do banco, e quem usa no dia a dia." → `co_ok_fontes = True`, `co_score += 1`. Valéria: "Cada fonte mostra um pedaço. Quando duas discordam, aí tem pergunta boa."
  - **Revisão**: "Como confirmar o que o sistema faz hoje?" → "Comparar o que os dados mostram com o código e com o relato de quem usa."
- **Menu social** — Jorge segura a pasta empoeirada.
  - "Me conta como essa regra das 72 h nasceu." → +1 co_legado.
  - "Vamos registrar isso no wiki agora, com a data e o motivo." → +1 co_mentora (Valéria aprova e cria a página).
  - "Anoto e sigo." (0)
- **Conquista**: `co_conq_arqueologia` se `co_ok_manutencao and co_ok_fontes`.
- **Registros**: `co_reg_legado`.
- **Meta**: 550 palavras.

#### co_05_entrevista — Duas pontas do mesmo chamado
- **Quando**: semana 2, quarta, 10h às 12h.
- **Fundos**: `sala_reunioes_manha`.
- **Música**: `music_office_relaxed`.
- **Presentes**: co_mentora, co_supervisora, co_solicitante. `set_available("co_legado", "co_dev", "co_qualidade")`.
- **Resumo**: Rosângela chega com o headset no pescoço e o relatório de SLA impresso; Edson chega de colete refletivo, direto de uma subestação. Valéria apresenta o jogador e passa a palavra. O jogador escolhe como abrir (decisão 3). Edson conta o episódio: o notebook do técnico Wellington ficou sem VPN, Edson ligou três vezes, cada atendente disse uma coisa, e o problema já tinha sido resolvido na véspera sem ninguém registrar; Wellington perdeu um dia de campo. Edson resume: "Eu só quero acompanhar fácil" (decisão 4). Rosângela reage: descrição obrigatória aumenta o TMA, a equipe dela já está no limite, e o que ela precisa é de relatório de SLA. O conflito fica claro (decisão 5). Quando a mediação funciona, Rosângela consulta o próprio relatório e descobre que 18% das ligações da central são cobrança de andamento; os dois concordam com descrição curta obrigatória, com modelos prontos para casos comuns. Ainda surgem outros requisitos, que o jogador anota: reabrir chamado quando a solução falha, trilha de auditoria (Rosângela lembra a auditoria interna de 2021), perfis diferentes para atendente, supervisor e admin, consulta rápida no pico das 9h, e o desejo de Edson de receber aviso por WhatsApp porque técnico de campo não abre a intranet. Valéria lembra que o SGC continua sendo o sistema de registro. No fim, os dois passam o contato.
- **Objetivos**: abrir entrevista pedindo episódio concreto; esclarecer palavra vaga; mediar conflito entre stakeholders com objetivo comum e dado; levantar requisitos funcionais, não funcionais e restrições.
- **Decisão 3** (`co_ok_episodio`) — "Como você abre a conversa?"
  - "Pergunto se preferem um aplicativo ou uma página web." → Valéria: "Isso já é solução. Ainda não sabemos o que precisa mudar para eles."
  - **Adequada**: "Peço que contem a última vez em que acompanhar um chamado deu errado." → `co_ok_episodio = True`, `co_score += 1`. Valéria: "Um episódio mostra quem sofre, o que acontece e quanto custa."
  - "Pergunto se um aviso automático de chamado resolvido já ajudaria." → Valéria: "A pergunta sugere a resposta. O Edson pode dizer sim e a gente nunca descobre o problema real."
  - **Revisão**: "Edson, quando foi a última vez que você precisou saber de um chamado e não conseguiu?"
- **Decisão 4** (`co_ok_ambiguidade`) — Edson: "Eu só quero acompanhar fácil." "O que fazer com 'fácil'?"
  - "Registro 'o acompanhamento deve ser fácil'." → Valéria: "A equipe vai entender 'fácil' de um jeito e o Edson de outro. Ninguém consegue testar isso."
  - "Troco por 'intuitivo e moderno'." → Valéria: "Trocamos um adjetivo por dois. O resultado esperado continua sem nome."
  - **Adequada**: "Pergunto o que ele precisa conseguir fazer nessa situação." → `co_ok_ambiguidade = True`, `co_score += 1`. Edson: "Abrir o chamado pelo número e ver o estado, quem pegou e o que foi feito."
  - **Revisão**: "O que precisava acontecer para você não ter ligado três vezes?" → mesma resposta de Edson.
  - Depois: Valéria lembra que a regra resolve uma parte; facilidade de uso se avalia observando pessoas usando.
- **Decisão 5** (`co_ok_conflito`) — "Rosângela e Edson puxam para lados opostos. Como você conduz?"
  - "A Rosângela é a gestora do processo; ela decide." → Edson se cala. Valéria: "A necessidade do Edson some do registro, as ligações continuam e o projeto perde o motivo de existir."
  - "Anoto os dois pedidos como estão e deixo a equipe decidir depois." → Valéria: "Aí uma regra contradiz a outra no documento, e quem decide é quem não conhece a central. Isso volta mais caro na inspeção."
  - **Adequada**: "Pergunto o que cada um quer evitar e busco um dado que os dois aceitem." → `co_ok_conflito = True`, `co_score += 1`. Rosângela confere o relatório: 18% das ligações são cobrança de andamento.
  - **Revisão**: "O que cada um de vocês quer evitar?" → Rosângela: "fila e retrabalho"; Edson: "ligação e dia perdido". Segue para o dado.
- **Menu social** — despedida:
  - Agradecer a Rosângela pelo dado e pedir para observar a central de novo → `add_friendship_point("co_supervisora", 1)`.
  - Pedir ao Edson que teste o protótipo com a equipe de campo → `add_friendship_point("co_solicitante", 1)`.
  - Agradecer aos dois juntos e encerrar. (0)
- **Estado**: `add_contact("co_supervisora")`, `add_contact("co_solicitante")` no fim.
- **Conquista**: `co_conq_escuta` se pelo menos 2 das decisões 3 a 5 forem adequadas de primeira.
- **Registros**: `co_reg_elicitacao`.
- **Meta**: 800 palavras.

#### co_06_avaliacao — Separando o que é o quê
- **Quando**: semana 2, quinta, 14h às 18h.
- **Fundos**: `escritorio_interior_tarde`, `escritorio_interior_noite`.
- **Música**: `music_office_focused`.
- **Presentes**: co_mentora, co_qualidade. `set_available("co_legado", "co_dev", "co_supervisora", "co_solicitante")`.
- **Resumo**: Valéria lê o resumo da entrevista e comenta o que o jogador fez, lendo `co_ok_episodio`, `co_ok_ambiguidade` e `co_ok_conflito` ("você começou pelo episódio" ou "com apoio, você chegou ao episódio"). Ingrid entra e propõe classificar os itens no quadro em quatro colunas: funcional, não funcional, restrição e desejo. O primeiro exemplo é narrado: "a consulta mostra estado, atendente e solução" vai para funcional. O jogador classifica o requisito de desempenho (decisão 6) e a regra sobre as tabelas do SGC (decisão 7). Ingrid mostra um item estranho que apareceu no grupo da equipe, "tema escuro com mascote", e o coloca em desejo, fora do problema. O aviso por WhatsApp também vai para desejo: registrado, sem data. Ingrid explica que cada tipo é verificado de um jeito: teste de função, teste de carga, revisão de arquitetura, conversa com stakeholder. O dia termina com o documento organizado.
- **Objetivos**: classificar requisitos em funcional, não funcional, restrição e desejo; entender que a classificação muda como o item é verificado.
- **Decisão 6** (`co_ok_class_nf`) — "A consulta do chamado deve responder em até 3 s para 95% dos acessos, com 1.500 usuários simultâneos no pico das 9h. Que tipo é?"
  - "Funcional: fala da consulta do chamado." → Ingrid: "A consulta é funcional. Este trecho fala de quão rápido ela responde e sob qual carga. Se entrar como funcional, ninguém planeja teste de carga."
  - **Adequada**: "Não funcional: define desempenho, com número, carga e momento." → `co_ok_class_nf = True`, `co_score += 1`.
  - "Desejo: seria bom, mas não é necessário." → Ingrid: "No pico das 9h, se a consulta pesar no Oracle, a tela do atendente trava junto. Isso não é enfeite."
  - **Revisão**: "Esse item descreve o que o sistema faz ou como ele deve se comportar?" → "Como ele deve se comportar: é não funcional."
- **Decisão 7** (`co_ok_class_restricao`) — "O Farol não pode alterar tabelas do SGC sem aprovação do CAB; os dados continuam no Oracle. Que tipo é?"
  - "Requisito funcional do Farol." → Ingrid: "Não descreve nada que o usuário faz. Limita como a gente pode construir."
  - "Desejo da equipe de qualidade." → Ingrid: "Se for desejo, alguém altera a tabela 'só um pouquinho' e a rotina das 72 h para de funcionar."
  - **Adequada**: "Restrição: limita a solução e vem do ambiente e da gestão de mudanças." → `co_ok_class_restricao = True`, `co_score += 1`.
  - **Revisão**: "Quem impôs essa regra e o que ela limita?" → "O ambiente e o CAB; limita a solução, então é restrição."
- **Menu social** — reação ao comentário de Ingrid:
  - "Quero entender onde acertei e onde errei." → +1 co_qualidade.
  - "Valéria, você lembra do seu primeiro requisito ruim?" → +1 co_mentora (ela mostra um de 2009: "o sistema deve ser ágil").
  - "Classificação parece burocracia." → Ingrid explica que cada coluna vira um tipo de teste. (0)
- **Registros**: `co_reg_classificacao`.
- **Meta**: 450 palavras.

#### co_07_cafe — Reescrever ou conviver?
- **Quando**: semana 2, sexta, 15h30 às 16h15.
- **Fundos**: `empresa_cafe_tarde`.
- **Música**: `music_coffee_break_energized`.
- **Presentes**: co_legado, co_dev. `set_available("co_mentora", "co_qualidade", "co_supervisora", "co_solicitante")`.
- **Resumo**: Na pausa do café, Kauã mostra no celular um trecho do SGC com o comentário "NAO MEXER - JT 2010"; Jorge ri e confessa que foi ele, numa sexta à noite. O jogador escolhe o assunto. Depois, Kauã diz que um dia o SGC vai ter que morrer; Jorge responde que sistema grande não morre, é substituído aos pedaços, "como a figueira mata-pau, que cresce em volta da árvore velha até ficar de pé sozinha". O jogador entra na conversa. A cena planta a ideia de estrangulamento sem dar o nome técnico, que aparece na co_13. Os três voltam para as mesas rindo do "patrimônio histórico".
- **Objetivos**: socializar; apresentar informalmente a tensão entre reescrever e evoluir.
- **Menu social 1** — "Sobre o que você puxa assunto?"
  - "Jorge, como era programar em 2008?" → +1 co_legado.
  - "Kauã, por que você escolheu trabalhar com legado?" → +1 co_dev ("Precisava do emprego. Fiquei porque descobri que gosto de mistério.").
  - "Qual o código mais estranho que vocês já viram aqui?" → +1 co_legado (a história da Tia Neide completa).
- **Menu social 2** — "Na discussão sobre reescrever…"
  - "Kauã, o que você trocaria primeiro, se pudesse?" → +1 co_dev.
  - "Jorge, o que você nunca deixaria mudar sem teste?" → +1 co_legado ("o fechamento e a rotina das 72 h").
  - "Prefiro ouvir mais antes de opinar." → Jorge: "Prudente." (0)
- **Registros**: nenhum.
- **Meta**: 400 palavras.

#### co_08_casa_sem2 — Fim da semana 2
- **Quando**: semana 2, sexta, 20h às 22h.
- **Fundos**: `transito_noite`, `quarto_noite`.
- **Música**: `music_streets_focused`, depois `music_home_dreamy`.
- **Presentes**: ninguém. `set_available('all')`.
- **Resumo**: No ônibus, o jogador pensa na rotina das 72 h, no manual errado e no dia perdido de Wellington. No quarto, revisa o notebook: o episódio, a regra confirmada com Edson, o dado de 18%, as quatro colunas da Ingrid. Chega uma mensagem de Kauã com a foto do comentário "NAO MEXER - JT 2010" emoldurada como meme: "patrimônio tombado". O jogador responde. A tela de contatos abre. Cartão: "Fim da Semana 2: antes de perguntar o que querem, pergunte o que aconteceu."
- **Objetivos**: consolidar elicitação e classificação.
- **Menu social** — resposta ao Kauã:
  - "Tombado pelo patrimônio. Ninguém mexe." → +1 co_dev.
  - Encaminhar ao Jorge pedindo a história completa → +1 co_legado (Jorge responde com um texto longo e uma piada no fim).
  - Não responder hoje. (0)
- **Estado**: `call screen contacts_screen`.
- **Registros**: nenhum.
- **Meta**: 300 palavras.

### ATO 3 — Especificação

#### co_09_historias — Do episódio à história de usuário
- **Quando**: semana 3, segunda, 9h às 17h.
- **Fundos**: `escritorio_interior_manha`, `escritorio_interior_tarde`. Artefatos `co_sgc_legado`, `co_farol_consulta`.
- **Música**: `music_office_concentrated_1`.
- **Presentes**: co_mentora, co_dev. `set_available("co_legado", "co_qualidade", "co_supervisora", "co_solicitante")`.
- **Resumo**: Valéria mostra como transformar o episódio de Edson numa história de usuário: "Como solicitante, quero consultar o estado e a solução registrada do meu chamado, para não precisar ligar para a central." Ela lista os casos de uso do Farol e os atores, que já desenham os perfis: UC01 Consultar chamado (solicitante), UC02 Registrar solução e resolver (atendente), UC03 Reabrir chamado (solicitante), UC04 Consultar trilha de auditoria (supervisor), UC05 Gerenciar perfis (admin). Para o UC01, anotam exceções: SGC fora do ar (mostrar o último estado sincronizado com data e hora) e chamado de outra pessoa (acesso negado). O jogador escolhe o critério de aceitação (decisão 8). Kauã levanta a dúvida: e se o atendente tentar resolver sem escrever nada? (decisão 9). Valéria anota que o caso limite precisa ser comparado com a rotina das 72 h, que fecha chamados sem descrição. À tarde, Kauã mostra um protótipo da tela de consulta, e Valéria lembra que protótipo serve para conversar, não para ir para produção. Kauã pergunta se já pode começar a codar.
- **Objetivos**: escrever história de usuário; identificar atores e casos de uso; escolher critério de aceitação verificável; tratar caso limite.
- **Decisão 8** (`co_ok_criterio`) — "Qual critério verifica a história?"
  - "A pessoa solicitante deve receber atendimento de qualidade." → Valéria: "É um objetivo importante, mas não diz o que observar no sistema."
  - "O atendente deve conseguir clicar no botão Resolver." → Valéria: "Conseguir clicar não garante o que o Edson vai ver do outro lado."
  - **Adequada**: "Dado um chamado Em atendimento, quando o suporte registra a solução e muda para Resolvido, a consulta do solicitante mostra Resolvido e o texto registrado." → `co_ok_criterio = True`, `co_score += 1`.
  - **Revisão**: "O que falta para verificar?" → "Registrar a situação inicial, a ação e o resultado que o solicitante confere."
- **Decisão 9** (`co_ok_caso_limite`) — "E se o atendente tentar resolver sem descrever a solução?"
  - "Preencho automaticamente com 'Resolvido', para não atrasar o atendimento." → Valéria: "Repetir o estado não explica nada. É o mesmo chamado 48213 de novo."
  - **Adequada**: "Proponho manter Em atendimento e orientar o preenchimento, e confirmo com a Rosângela." → `co_ok_caso_limite = True`, `co_score += 1`.
  - "Mudo o estado e o atendente explica depois por telefone." → Valéria: "Aí voltam as ligações que o Edson quer evitar."
  - **Revisão**: "Como registrar o caso e confirmar?" → "Descrição vazia mantém Em atendimento e mostra uma orientação; confirmar com a dona da regra."
- **Menu social** — "Posso começar a codar?", pergunta Kauã.
  - "Ainda não. Me ajuda a revisar os critérios? Assim você coda uma vez só." → +1 co_dev.
  - "Vamos perguntar à Valéria o que falta." → +1 co_mentora (ela explica a inspeção de quinta).
  - "Manda ver." → Valéria intervém com calma: protótipo sim, código de produção depois da inspeção. (0)
- **Registros**: `co_reg_criterio`.
- **Meta**: 650 palavras.

#### co_10_almoco — Mesa do refeitório
- **Quando**: semana 3, terça, 12h30 às 13h30.
- **Fundos**: `refeitorio_tarde`.
- **Música**: `music_coffee_break_friendly`.
- **Presentes**: os quatro da equipe. `set_available("co_supervisora", "co_solicitante")`.
- **Resumo**: No refeitório do prédio, a equipe se divide em duas mesas. O jogador escolhe onde sentar e puxa um assunto. Na mesa de Jorge e Ingrid, aparecem histórias de incidentes e uma pista de que Jorge vai sentir falta do lugar. Na mesa de Valéria e Kauã, Valéria conta que foi atendente com Rosângela em 2004, e Kauã fala do estudo de IA para prever picos de chamados. Na volta, há falas cruzadas que mudam com a amizade (≥4): Jorge oferece mostrar o PL/SQL da rotina das 72 h; Ingrid convida o jogador para assistir ao CAB de quinta como ouvinte.
- **Objetivos**: aprofundar laços; plantar a aposentadoria de Jorge e o CAB.
- **Menu social 1** — "Onde você senta?"
  - Com Jorge e Ingrid → +1 co_legado, +1 co_qualidade, `co_almoco_mesa = "jorge_ingrid"`.
  - Com Valéria e Kauã → +1 co_mentora, +1 co_dev, `co_almoco_mesa = "valeria_kaua"`.
- **Submenu A** (Jorge e Ingrid):
  - "Ingrid, qual foi o pior incidente que você viu?" → +1 co_qualidade (a sexta de 2019 e o post-mortem sem culpados).
  - "Jorge, você vai sentir falta daqui?" → +1 co_legado (ele desconversa; pista da aposentadoria).
  - "O que é um post-mortem sem culpados?" → explicação curta. (0)
- **Submenu B** (Valéria e Kauã):
  - "Valéria, como você saiu da central para a TI?" → +1 co_mentora.
  - "Kauã, o que você estuda fora do trabalho?" → +1 co_dev.
  - "Como vocês decidem o que entra numa versão?" → prévia da co_15. (0)
- **Registros**: nenhum.
- **Meta**: 400 palavras.

#### co_11_inspecao — Inspeção e escrita
- **Quando**: semana 3, quinta, 14h às 18h30.
- **Fundos**: `escritorio_interior_tarde`, `escritorio_interior_noite`.
- **Música**: `music_office_focused_2`.
- **Presentes**: co_mentora, co_qualidade. `set_available("co_legado", "co_dev", "co_supervisora", "co_solicitante")`.
- **Resumo**: Ingrid conduz uma inspeção formal com um checklist curto: falta algo? tem duas leituras? briga com outra regra? é estranho ao contexto? dá para testar? O jogador analisa três requisitos (decisões 10, 11 e 12). No terceiro, o conflito entre o bloqueio sem descrição e a rotina das 72 h vai para Rosângela pelo chat; ela decide que a rotina continua, mas grava a descrição padrão e registra a ação como "sistema" na trilha. Ingrid ainda mostra um requisito estranho que Kauã escreveu de brincadeira, "chatbot com avatar 3D", e o corta. Valéria propõe a escrita livre: Edson pediu para reabrir um chamado resolvido quando a solução falha, e o jogador escreve o requisito e o critério. Depois de revisar o texto, o jogador faz a autoavaliação com três perguntas (quem age e sob qual condição; dados iniciais e resultado observável; o que não pode mudar ou deve ser recusado) e escolhe entre reescrever, guardar como rascunho ou deixar pendente. O jogo diz com clareza que não corrige o texto. A cena termina com um menu de reação ao processo.
- **Objetivos**: identificar defeitos de requisito (ausente, ambíguo, inconsistente, estranho); resolver conflito de regra com a dona da regra; escrever requisito e critério e se autoavaliar.
- **Decisão 10** (`co_ok_insp_ausente`) — "RF-05: O solicitante pode reabrir um chamado resolvido." "O que você aponta?"
  - **Adequada**: "Faltam as condições: quem pode reabrir, até quando, se o motivo é obrigatório e o que acontece com a solução anterior." → `co_ok_insp_ausente = True`, `co_score += 1`.
  - "Está completo; o desenvolvedor decide os detalhes." → Ingrid: "O Kauã escolheria 30 dias, a Rosângela espera 7. A diferença aparece no teste de aceitação, com a tela pronta."
  - "O problema é o verbo: troque 'pode' por 'deve'." → Ingrid: "Obrigar a reabrir não faz sentido. Trocar o verbo não preenche a lacuna."
  - **Revisão**: "Que perguntas o requisito não responde?" → "Quem, até quando, com qual motivo e o que acontece com a solução anterior."
- **Decisão 11** (`co_ok_insp_ambiguo`) — "RNF-01: A consulta do chamado deve ser rápida mesmo nos horários de pico."
  - "Trocar por 'deve ser muito rápida e eficiente'." → Ingrid: "Continua sem número. Como alguém reprova esse teste?"
  - "Tirar o requisito; desempenho é problema da infraestrutura." → Ingrid: "O Farol lê o mesmo Oracle da central. Sem requisito, ninguém testa, e a tela do atendente trava no pico."
  - **Adequada**: "Definir tempo, percentual, carga e onde medir, como fizemos na classificação." → `co_ok_insp_ambiguo = True`, `co_score += 1`.
  - **Revisão**: "Quais palavras têm mais de uma leitura?" → "'Rápida' e 'pico': substituir por 3 s, 95%, 1.500 usuários, 9h."
- **Decisão 12** (`co_ok_insp_inconsistente`) — "RF-03: O sistema deve impedir que um chamado seja resolvido sem descrição. RN-07 (herdada do SGC): chamados de Reset de senha são resolvidos automaticamente após 72 h sem retorno."
  - "Apagar a RN-07; é regra velha do legado." → Ingrid: "Ela fecha uns 300 chamados de senha por semana. Sem ela, a fila da central volta a crescer. Regra velha tem motivo."
  - **Adequada**: "Apontar o conflito e levar a decisão à Rosângela, dona da regra, com uma proposta." → `co_ok_insp_inconsistente = True`, `co_score += 1`.
  - "Manter as duas; o código decide qual roda primeiro." → Ingrid: "Aí o comportamento depende da ordem de execução. Um teste aprova, outro reprova, e ninguém sabe qual está certo."
  - **Revisão**: "Quem pode decidir qual regra vale?" → "Quem é dona do processo: a Rosângela."
- **Escrita livre**: pedido — "A pessoa solicitante precisa reabrir um chamado resolvido quando a solução falhar. Ela deve informar o motivo; o chamado volta a Em atendimento e preserva a solução anterior no histórico." Grava `co_escrita_requisito`, `co_escrita_criterio`; autoavaliação define `co_escrita_status` ("rascunho" se os dois campos têm texto e o jogador confirma; "pendente" se segue sem registrar). "Reescrever" volta ao input com o texto anterior.
- **Menu social** — "Como você reage à inspeção?"
  - Agradece o olhar crítico → +1 co_qualidade.
  - Fica inseguro com tanto detalhe → Valéria: "Ninguém revisa sozinho. Por isso a gente inspeciona junto." +1 co_mentora.
  - Acha cansativo, mas entende → Ingrid: "Chato hoje, barato amanhã." (0)
- **Conquista**: `co_conq_inspetor` se pelo menos 2 das decisões 10 a 12 forem adequadas de primeira e `co_escrita_status == "rascunho"`.
- **Registros**: `co_reg_inspecao`.
- **Meta**: 800 palavras.

#### co_12_casa_sem3 — Fim da semana 3
- **Quando**: semana 3, sexta, 19h às 22h.
- **Fundos**: `transito_noite`, `quarto_noite`.
- **Música**: `music_streets_focused`, depois `music_home_reflecting`.
- **Presentes**: ninguém. `set_available('all')`.
- **Resumo**: No ônibus, o jogador relê o rascunho sobre reabrir chamado (se `co_escrita_status == "rascunho"`, mostrar o texto escapado; se pendente, lembrar que o exercício pode ser retomado). No quarto, anota as três perguntas da inspeção. Chega uma mensagem de Jorge com uma foto: a equipe do SGC no lançamento de 2008, ele com mais cabelo. O jogador responde. A tela de contatos abre. Cartão: "Fim da Semana 3: requisito bom é aquele que duas pessoas leem e entendem a mesma coisa."
- **Objetivos**: consolidar especificação e inspeção.
- **Menu social** — resposta ao Jorge:
  - "Quem são os outros da foto?" → +1 co_legado.
  - "Dá para colocar essa foto no wiki do SGC?" → Ingrid responde no grupo "Mais um ponto para a documentação." +1 co_qualidade.
  - Curtir a foto. (0)
- **Estado**: `call screen contacts_screen`.
- **Registros**: nenhum.
- **Meta**: 300 palavras.

### ATO 4 — Arquitetura e gestão

#### co_13_arquitetura — Trocar o motor com o avião voando
- **Quando**: semana 4, terça, 9h às 17h.
- **Fundos**: `sala_reunioes_manha`, `escritorio_interior_tarde`. Artefato `co_farol_arquitetura`.
- **Música**: `music_office_concentrated_2`.
- **Presentes**: co_legado, co_dev, co_qualidade, co_mentora (manhã); co_solicitante e co_dev (tarde). `set_available("co_supervisora")`.
- **Resumo**: Na reunião de arquitetura, Kauã apresenta a ideia de reescrever o SGC em microsserviços. Jorge lista o que depende do SGC: 14 relatórios, a rotina das 72 h, a integração com o RH. O jogador escolhe a estratégia (decisão 13); a adotada é sempre o estrangulamento com camada anticorrupção, e o diagrama aparece na tela. Em seguida modelam os dados: chamado (do SGC, só leitura), solicitante, atendente, perfil, usuario_perfil e a nova historico_chamado. O jogador decide como guardar quem mudou o quê (decisão 14). Kauã fica frustrado por ter perdido a reescrita, e o jogador fala com ele (menu social). À tarde, Edson passa na sede e pede para incluir o aviso por WhatsApp na primeira entrega. Kauã explica o impacto: contrato com provedor oficial da API, parecer do jurídico por usar telefone pessoal (LGPD), testes de segurança; incluir agora adia a consulta e o bloqueio. O jogador conduz a negociação até um acordo e confere o texto com os dois.
- **Objetivos**: escolher arquitetura de transição para legado; modelar trilha de auditoria; negociar mudança de escopo mostrando impacto e registrando o acordo.
- **Decisão 13** (`co_ok_arquitetura`) — "Qual estratégia para o Farol?"
  - "Reescrever tudo em microsserviços e desligar o SGC num grande dia de virada." → Jorge: "São 16 anos de regra, 14 relatórios e a rotina das 72 h. Num único dia de virada, qualquer esquecimento para a central inteira. E oito semanas não dão nem para listar tudo."
  - **Adequada**: "Construir o Farol ao lado do SGC, atrás de uma camada que traduz os dados, e assumir uma função por vez." → `co_ok_arquitetura = True`, `co_score += 1`. Jorge: "A figueira mata-pau. Agora tem nome técnico: estrangulamento."
  - "Construir o Farol dentro do SGC, acrescentando telas no JSF antigo." → Ingrid: "Sem testes automatizados, cada tela nova mexe em código que ninguém entende inteiro. E cada ajuste vira RFC no coração do sistema."
  - **Revisão**: "Como trocar uma parte sem parar o resto?" → "Uma parte por vez, ao lado do sistema velho, com um tradutor no meio."
- **Decisão 14** (`co_ok_auditoria`) — "Como guardar quem mudou o quê no chamado?"
  - "Uma coluna 'última alteração' na tabela de chamados." → Ingrid: "Guarda só a última. Se o chamado mudou cinco vezes, perdemos quatro. E a tabela é do SGC: precisaria de RFC."
  - "Gravar num arquivo de log no servidor." → Jorge: "Arquivo de log gira e some. Não dá para consultar por chamado, e qualquer administrador edita."
  - **Adequada**: "Uma tabela de histórico só de inclusão: quem, perfil, quando, ação, valor anterior e novo; ninguém altera nem apaga." → `co_ok_auditoria = True`, `co_score += 1`.
  - **Revisão**: "O que a Rosângela precisaria mostrar numa auditoria?" → "Cada mudança, com autor e horário, sem possibilidade de edição."
- **Menu social** — Kauã, desanimado com a reescrita:
  - "Sua ideia de serviços pode ser o destino. O estrangulamento é o caminho até lá." → +1 co_dev.
  - "Jorge, obrigado por mostrar as dependências." → +1 co_legado.
  - Deixar o assunto morrer. (0)
- **Negociação** (`co_negociacao_*`), ao abrir: `co_negociacao_sem_atalho = True`.
  - Ruim: "Incluir o WhatsApp e manter o prazo sem falar de capacidade." → Kauã: "Eu teria de cortar o bloqueio da descrição vazia." Edson: "Aí eu recebo aviso de um chamado que diz 'Resolvido' sem dizer nada." `co_negociacao_sem_atalho = False`, volta ao menu.
  - Ruim: "Recusar porque o escopo já foi escrito." → Edson: "Meu técnico continua sem abrir a intranet." Kauã: "O registro pode mudar; a gente precisa mostrar o efeito." `co_negociacao_sem_atalho = False`, volta ao menu.
  - Válida: "Entregar consulta e bloqueio primeiro; investigar o WhatsApp na próxima rodada, sem data." → `co_negociacao_opcao = "base_primeiro"`; acordo: "Entregar primeiro a consulta e o bloqueio sem descrição para todos. Edson e Kauã investigam o aviso por WhatsApp na próxima rodada, antes de estimar uma data."
  - Válida: "Investigar o WhatsApp agora e renegociar a data de liberação." → `co_negociacao_opcao = "investigar_agora"`; acordo: "Kauã investiga agora o aviso por WhatsApp. Na janela da semana 8, o Farol entra para a central e para o piloto da equipe do Edson; a liberação para todos fica para a janela seguinte, preservando a consulta e o bloqueio."
  - Conferência: "Rever o acordo" volta ao menu; "Confirmar com os dois" → `co_negociacao_completa = True`.
- **Conquistas**: `co_conq_acordo` ao confirmar, se `co_negociacao_sem_atalho`; `co_conq_transicao` se `co_ok_arquitetura and co_ok_auditoria`.
- **Registros**: `co_reg_transicao`.
- **Meta**: 750 palavras.

#### co_14_comemoracao — 25 anos de casa
- **Quando**: semana 4, sexta, 16h às 18h; casa às 21h.
- **Fundos**: `escritorio_interior_tarde`, `escritorio_interior_festa`, `quarto_noite`.
- **Música**: `music_office_relaxed`, depois `music_home_dreamy`.
- **Presentes**: os quatro da equipe. `set_available("co_supervisora", "co_solicitante")`.
- **Resumo**: Valéria vê na intranet que Jorge completa 25 anos de Grupo Vértice e propõe uma surpresa no fim do expediente. O jogador escolhe como ajudar. O escritório ganha bandeirinhas; Rosângela manda pelo chat um áudio da central inteira cantando parabéns (narrado). Jorge se emociona e conta que se aposenta em março. A sala fica em silêncio: quem vai saber das rotinas do SGC? O jogador propõe uma homenagem. A reação de Jorge muda com a amizade (≥5: ele aceita gravar os "Causos do SGC" e marca a primeira sessão). Em casa, o jogador pensa que um sistema legado também é a memória das pessoas que o mantêm. Cartão: "Fim da Semana 4: sistema legado é também memória de gente."
- **Objetivos**: cultura de equipe; risco de conhecimento concentrado numa pessoa (fator ônibus), tratado de forma humana.
- **Menu social 1** — "Como você ajuda na surpresa?"
  - Bolo com a tela do SGC em papel de arroz, desenhada pelo Kauã → +1 co_dev, `co_contribuicao_festa = "bolo"`.
  - Vaquinha para uma caneca nova, organizada pela Valéria → +1 co_mentora, `"vaquinha"`.
  - Cartão coletivo com assinaturas da central, circulado pela Ingrid → +1 co_qualidade, `"cartao"`.
- **Menu social 2** — "Que homenagem você propõe?"
  - "Um wiki 'Causos do SGC': o Jorge conta, a gente grava e registra." → +1 co_legado, `co_homenagem_jorge = "wiki"`; se `get_friendship_point("co_legado") >= 5`, `co_conq_memoria = True`.
  - "Um brinde e um agradecimento." → +1 co_legado, `"brinde"`.
  - "Agora a Tia Neide se aposenta junto?" → risadas. (0) `"piada"`.
- **Registros**: nenhum.
- **Meta**: 450 palavras.

#### co_15_gestao — Capacidade, CAB e riscos
- **Quando**: semana 5, segunda, 9h às 17h; resumo da quarta à noite e da sexta.
- **Fundos**: `sala_reunioes_manha`, `escritorio_interior_tarde`, `escritorio_interior_noite`. Artefato `co_farol_arquitetura`.
- **Música**: `music_office_focused`.
- **Presentes**: os quatro da equipe. `set_available("co_supervisora", "co_solicitante")`.
- **Resumo**: Valéria abre a reunião com o calendário: a janela aprovada é no sábado da semana 8, das 0h às 4h; o CAB se reúne às quintas e a RFC precisa entrar até a quinta da semana 7. Ela retoma o acordo da co_13 (texto muda com `co_negociacao_opcao`; em "investigar_agora", Kauã conta que o WhatsApp exige contrato e parecer do jurídico). A primeira entrega tem capacidade para mais dois itens, e o jogador monta o plano (2 de 4). Ingrid pergunta como levar a implantação ao CAB (decisão 15). Jorge levanta o maior risco: carregar 200 mil descrições históricas do SGC para a tabela nova (decisão 16). Ingrid pergunta quem fica para o ensaio da carga na quarta à noite. A cena fecha com um resumo: o ensaio (se `co_ok_risco`, desde o início; se não, depois da revisão) encontrou 2,7% de descrições com acentos de outro padrão, o script foi corrigido e o critério de parada ficou "zero registro corrompido". Cartão: "Fim da Semana 5: mudança boa tem plano de ida e plano de volta."
- **Objetivos**: planejar com capacidade limitada; preparar RFC normal; responder a risco de migração de dados com ensaio, critério de parada e reversão testada.
- **Planejamento** (mecanismo da demo, `co_plano_*`, 2 pontos):
  - 0 "Consulta do solicitante com estado, atendente e solução" (necessário).
  - 1 "Bloquear resolução sem descrição, com a exceção registrada da rotina das 72 h" (necessário).
  - 2 "Tema de cores personalizável no painel da supervisão" (extra).
  - 3 "Relatório mensal de chamados em PDF" (extra; o SGC já emite um parecido).
  - Feedback por cobertura 2/1/0, com Valéria citando o que Edson e Rosângela diriam. Se a cobertura for menor que 2, o menu oferece "Revisar os itens" ou "Manter este plano"; ao manter, Valéria explica que o comitê de produto fechou o recorte com os dois itens necessários, e a história segue com eles (`co_plano_cobertura` guarda a escolha do jogador para o resumo). Sem nota.
- **Decisão 15** (`co_ok_cab`) — "Como levar a implantação ao CAB?"
  - "Pedir como mudança emergencial, para não esperar a reunião de quinta." → Ingrid: "Emergencial é para restaurar serviço parado. Usar para furar fila faz o CAB desconfiar de todo pedido nosso. Depois de 2019, toda RFC da equipe passou seis meses sendo revisada duas vezes."
  - "Implantar numa terça às 15h e avisar por e-mail; é um módulo novo." → Ingrid: "O Farol lê o mesmo Oracle da central no meio do expediente, sem plano de volta combinado. Se travar, 140 atendentes param."
  - **Adequada**: "Registrar uma RFC normal: o que muda, impacto, janela de sábado, testes de regressão, plano de rollback e responsáveis." → `co_ok_cab = True`, `co_score += 1`.
  - **Revisão**: "O que o CAB precisa saber para aprovar?" → "O que muda, o impacto, quando, como testamos e como voltamos."
- **Decisão 16** (`co_ok_risco`) — "Como tratar o risco da carga do histórico?"
  - "Rodar a carga direto na janela; o script funcionou com 50 chamados de teste." → Jorge: "Os 50 de teste foram escritos ontem. Os de 2008 têm acento de outro padrão, texto colado do Word e campo com 4 mil caracteres."
  - **Adequada**: "Ensaiar a carga numa cópia de produção, definir um critério de parada e testar o script de reversão." → `co_ok_risco = True`, `co_score += 1`.
  - "Deixar o Jorge de sobreaviso; ele resolve se der problema." → Jorge: "Em março eu não estarei aqui. Risco com plano é risco gerenciado. Risco comigo de sobreaviso é sorte."
  - **Revisão**: "Como descobrir o problema antes da janela?" → "Ensaiar com dados reais e combinar quando parar e como voltar."
- **Menu social** — "Quem fica no ensaio de quarta à noite?"
  - "Eu fico com você no ensaio." → +1 co_qualidade.
  - "Reviso o roteiro de rollback com o Jorge." → +1 co_legado.
  - "Vou descansar; tenho prova na quinta." → Ingrid: "Descanso também é gestão de risco." (0)
- **Registros**: nenhum novo (aplica `co_reg_manutencao`).
- **Meta**: 650 palavras.

### ATO 5 — Implementação

#### co_16_codificacao — Código pequeno, rede grande
- **Quando**: semana 6, segunda a quarta; cena principal na segunda, 9h às 18h.
- **Fundos**: `escritorio_interior_manha`, `escritorio_interior_tarde`. Artefato `co_farol_consulta`.
- **Música**: `music_office_concentrated_1`, depois `music_office_relaxed`.
- **Presentes**: co_dev, co_legado. `set_available("co_mentora", "co_qualidade", "co_supervisora", "co_solicitante")`.
- **Resumo**: A tarefa do jogador é implementar, na camada anticorrupção, a regra de resolver com descrição e a exceção da rotina das 72 h. Ele escolhe a abordagem (decisão 17). Em pair com Kauã, os testes de caracterização revelam uma surpresa: a rotina das 72 h grava a data de fechamento no fuso de Brasília fixo, o que muda o relatório das filiais do Norte; o comportamento fica registrado e não é alterado agora. Kauã abre um pull request da tela de consulta e pede revisão ao jogador (decisão 18). Jorge revisa o pull request do jogador e deixa dois comentários: o nome do teste não diz o comportamento, e falta o caso de descrição só com espaços. O jogador reage. Na quarta, a consulta funciona em homologação com o chamado 48213 de exemplo. Cartão: "Fim da Semana 6: no legado, primeiro você prende uma rede, depois você mexe."
- **Objetivos**: escrever testes de caracterização antes de mudar; fazer mudança pequena; revisar pull request procurando o defeito que importa; receber revisão.
- **Decisão 17** (`co_ok_abordagem`) — "Como começar a mudança?"
  - "Aproveitar e refatorar a tela de fechamento do SGC, que é confusa." → Jorge: "São 4 mil linhas sem teste. Você mudaria o escopo da RFC e o risco de regressão sem ninguém pedir."
  - "Copiar a consulta SQL do relatório antigo para ganhar tempo." → Kauã: "Essa consulta varre a tabela inteira e tem o bug de fuso de 2014. Copiar é herdar os dois."
  - **Adequada**: "Escrever primeiro testes de caracterização do que o SGC faz hoje, inclusive a rotina das 72 h, e depois fazer a mudança pequena na camada." → `co_ok_abordagem = True`, `co_score += 1`.
  - **Revisão**: "O que você precisa ter antes de alterar?" → "Testes que mostram o comportamento atual."
- **Decisão 18** (`co_ok_review`) — PR do Kauã: "Exibir estado e solução; desabilitar Resolver com descrição vazia." "Que comentário você faz?"
  - "Comento nomes de variáveis e formatação." → Kauã: "Valeu, ajusto. Mas olha: passou batido que a API aceita descrição vazia vinda da integração."
  - **Adequada**: "A regra está só na tela. A API também precisa recusar descrição vazia, com um teste para isso." → `co_ok_review = True`, `co_score += 1`. Kauã: "Pegou. Os testes passavam porque nenhum chamava a API direto."
  - "Aprovo: os testes passaram e o Kauã tem mais experiência." → Valéria (pelo chat): "Revisão existe justamente para um segundo olhar. Os testes passaram porque nenhum chama a API."
  - **Revisão**: "Por onde mais um chamado pode ser resolvido além da tela?" → "Pela API da integração; a validação precisa estar no servidor."
- **Menu social** — reação à revisão de Jorge:
  - Agradecer e corrigir os dois pontos → +1 co_legado.
  - Pedir pair ao Kauã para o caso dos espaços → +1 co_dev.
  - "Mas funciona." → Jorge: "Funcionar hoje é o mínimo. O teste é para quem mexer aqui daqui a cinco anos." (0)
- **Registros**: nenhum.
- **Meta**: 600 palavras.

#### co_17_testes_seguranca — Quem pode o quê
- **Quando**: semana 7, segunda a quinta; manhã de segunda, tarde de quarta (aceitação), quinta (CAB).
- **Fundos**: `escritorio_interior_manha`, `central_atendimento_tarde`. Artefato `co_farol_auditoria`.
- **Música**: `music_office_focused_2`.
- **Presentes**: co_qualidade, co_dev; co_supervisora na tarde de quarta. `set_available("co_mentora", "co_legado", "co_solicitante")`.
- **Resumo**: Ingrid apresenta o plano de testes: unidade, integração com o SGC em homologação, perfis, trilha, carga do pico das 9h e regressão. O jogador decide como testar os perfis (decisão 19) e o que entra na regressão (decisão 20). Procurando a configuração da integração, Kauã encontra a senha do usuário de integração do SGC escrita num arquivo do repositório desde 2012. O jogador escolhe como relatar (menu social); em todos os caminhos a senha vai para o cofre de segredos, é trocada por mudança padrão e o caso é registrado sem procurar culpados. Na quarta à tarde, na central, Rosângela testa com dois atendentes: o bloqueio da descrição vazia, os modelos de descrição e a trilha mostrando "sistema" na rotina das 72 h. Ela diz que, na auditoria de 2021, teria economizado uma semana. Na quinta, a RFC vai ao CAB e é aprovada (se `co_ok_cab` foi de primeira, Ingrid comenta que a RFC passou sem nenhuma pergunta). Cartão: "Fim da Semana 7: teste de permissão se faz pelo lado do não."
- **Objetivos**: testar RBAC por casos negativos; definir escopo de regressão; tratar segredo exposto; conduzir teste de aceitação com usuários.
- **Decisão 19** (`co_ok_rbac`) — "Como verificar os perfis?"
  - "Testar com o usuário administrador, que acessa tudo." → Ingrid: "Prova que funciona para quem pode tudo. Não prova que alguém é impedido."
  - **Adequada**: "Testes negativos por perfil: o atendente tenta abrir a trilha, o solicitante tenta ver chamado de outra pessoa; os dois recebem acesso negado e a tentativa fica registrada." → `co_ok_rbac = True`, `co_score += 1`.
  - "Esconder os botões de quem não tem permissão." → Ingrid: "Botão escondido não é controle de acesso. Quem souber o endereço da API chama direto."
  - **Revisão**: "Como provar que alguém não consegue?" → "Entrar com cada perfil e tentar o que ele não pode."
- **Decisão 20** (`co_ok_regressao`) — "O que entra na suíte de regressão antes do CAB?"
  - "Só os testes do Farol; o SGC não foi alterado." → Kauã: "O Farol grava histórico e lê as mesmas tabelas, e a rotina das 72 h agora grava descrição. Se o relatório mensal quebrar, foi a gente."
  - **Adequada**: "Os fluxos do SGC que o Farol toca: abrir, resolver, a rotina das 72 h e o relatório mensal da diretoria, além dos testes novos." → `co_ok_regressao = True`, `co_score += 1`.
  - "Testar manualmente em produção depois da janela." → Ingrid: "Depois da janela, defeito vira incidente com a central aberta. Regressão serve para descobrir antes."
  - **Revisão**: "O que já funcionava e pode ser afetado?" → "Tudo que usa as mesmas tabelas ou a rotina das 72 h."
- **Menu social** — senha no repositório (`co_senha_relato`):
  - "Registro como vulnerabilidade e levo para Ingrid e Jorge, sem procurar culpados." → +1 co_qualidade, `"registro"`.
  - "Pergunto ao Jorge como a senha foi parar ali antes de registrar." → +1 co_legado, `"historia"` (2012, prazo apertado, ninguém voltou para corrigir; ele mesmo ajuda a registrar).
  - "Posto no grupo geral da TI para todo mundo ver." → Ingrid: "Expor um segredo para 300 pessoas aumenta o problema. Vamos trocar a senha agora." `"grupo"` (0)
- **Conquistas**: `co_conq_rede` se `co_ok_abordagem and co_ok_regressao`; `co_conq_trilha` se `co_ok_review and co_ok_rbac`.
- **Registros**: `co_reg_verificacao`.
- **Meta**: 600 palavras.

#### co_18_implantacao_avaliacao — Janela de sábado e avaliação
- **Quando**: semana 8, sábado 23h30 às 4h15; segunda, 15h às 17h; saída às 18h.
- **Fundos**: `escritorio_interior_noite`, `sala_servidores`, `central_atendimento_tarde`, `empresa_exterior_noite`. Artefatos `co_farol_consulta`, `co_farol_auditoria`.
- **Música**: `music_office_concentrated_2` na janela; `music_office_motivated` na avaliação.
- **Presentes**: os quatro da equipe na janela (Rosângela de plantão por telefone); na segunda, os quatro, co_supervisora e co_solicitante. `set_available()`.
- **Resumo**: A equipe se reúne na sala de guerra com o roteiro aprovado: (1) backup verificado; (2) publicar o Farol desligado; (3) ativar a camada e a regra; (4) carga do histórico; (5) testes de fumaça; (6) ligar o Farol para os usuários. Os passos 1 a 3 passam. Às 2h10, no passo 4, a validação acusa descrições com caracteres quebrados: 0,4% de uma filial com outro padrão de 2009 (se `co_ok_risco`), ou 3,1% dos registros (se não, com Jorge lembrando que o ensaio tardio pegou menos casos). O jogador decide (decisão 21). Kauã fica nervoso, e o jogador age (menu social). Às 4h15 os testes de fumaça passam e o Farol é ligado (para todos em "base_primeiro"; para a central e o piloto do Edson em "investigar_agora"). Na segunda, na central, Rosângela e Edson avaliam: as ligações de cobrança caíram de 18% para 11% em dois dias, e Edson reabriu um chamado do Wellington pelo celular. O jogo calcula `co_amizade_total`, `co_conq_total` e `co_final_grade`, e as falas finais variam (abaixo). A equipe sai junto do prédio à noite; segue o epílogo comum.
- **Objetivos**: executar implantação seguindo o plano e o critério de parada; separar incidente de problema; validar com os stakeholders; refletir sobre o ciclo inteiro.
- **Decisão 21** (`co_ok_janela`) — "Faltam menos de duas horas de janela. O que fazer?"
  - "Corrigir os registros na mão direto no banco de produção." → Ingrid: "Isso é mudança não autorizada, sem teste e sem trilha. Se um UPDATE errar, não temos como explicar o que mudou."
  - "Seguir assim; quase ninguém consulta chamado antigo." → Rosângela (telefone): "A auditoria interna consulta. E o critério que aprovamos no CAB diz zero registro corrompido."
  - **Adequada**: "Seguir o plano: reverter só a carga do histórico, que é um passo independente, ligar o Farol com o que passou nos testes, registrar um problema e reagendar a carga." → `co_ok_janela = True`, `co_score += 1`. Valéria: "Para isso serve o critério de parada. Ninguém precisa ser herói às 2h da manhã."
  - **Revisão**: "O que o plano aprovado diz para esse caso?" → "Passou do critério de parada: volta o passo 4, segue o resto, registra o problema."
- **Menu social** — Kauã, às 2h30:
  - "Seguimos o roteiro. Foi para isso que ensaiamos." → +1 co_dev.
  - Ajudar Valéria a escrever as atualizações para Rosângela e Edson → +1 co_mentora.
  - "Vou dar uma volta para esfriar a cabeça." (0)
- **Final** (após calcular):
  - **excelente**: Rosângela cita o bloqueio e a trilha ("pela primeira vez sei o que minha equipe fez sem perguntar"); Edson cita a reabertura pelo celular; Valéria diz que o jogador conduziu a conversa como alguém da equipe; Ingrid fala da RFC sem perguntas.
  - **bom**: os mesmos elogios, mais uma melhoria concreta de Rosângela (treinamento curto e mais modelos de descrição) e uma de Edson (o aviso que ainda falta).
  - **ok**: Rosângela e Edson reconhecem o avanço e listam o que faltou com honestidade (ouvir a central antes de propor, ensaiar antes da janela); Valéria transforma isso num plano para a próxima rodada.
  - Extras: com `co_conq_memoria`, Jorge conta que já gravou três "Causos do SGC" e passa a caneca de 2008 para o jogador guardar até março; com `co_amizade_total >= 28`, a equipe convida o jogador para a próxima rodada do Farol. Fala do acordo da co_13 conforme `co_negociacao_opcao` (próximo passo do WhatsApp).
- **Conquista**: `co_conq_janela` se `co_ok_janela and (co_ok_cab or co_ok_risco)`.
- **Registros**: nenhum novo. Ao fim, todos os registros descobertos ficam no notebook para o epílogo.
- **Meta**: 750 palavras.

## 10. Pontos de atenção para F2 e F4

- **Amizade pelo chat**: se `chat_amigo` continuar dando +1 a cada conversa, os limiares do final ficam fáceis de atingir. Vale aplicar a mesma regra que a F2 definir para a saúde.
- **Gênero do jogador**: os textos acima evitam flexão ("Boas-vindas", "Valeu!", "inseguro com tanto detalhe" pode virar "sente insegurança"). Onde não der, usar `player_gender`.
- **Conquistas e epílogo**: o resumo de aprendizagem do epílogo comum pode ler `co_score`, os `co_ok_*`, `co_negociacao_acordo` e `co_escrita_status`, como a demo faz.
- **Consistência**: chamado de exemplo é sempre 48213; a rotina é sempre "das 72 h"; o dado da entrevista é sempre 18%; a janela é sempre sábado, 0h às 4h, da semana 8.
- **Nomes**: nenhum nome repete a saúde ou a demo. Se a bíblia da Startup usar algum destes nomes, ajustar uma das rotas.
