# Mecânicas, exploração e consequências

Revisão de 09/11/2026, somente por leitura do código. Não houve nova partida observada nem teste com jogadores. As sugestões abaixo são propostas; não descrevem funcionalidades já implementadas ou diversão comprovada.

**Diagnóstico principal:** há uma demonstração didática funcional, mas a atividade dominante é escolher respostas e ler explicações. Exploração, descoberta e consequências ainda quase não participam do jogo.

## O que existe e onde está o limite

| Aspecto | Evidência no código | Avaliação |
|---|---|---|
| Point-click | `scripts/functions.rpy:40-82`: cada tela modal apresenta um objeto e uma ação que define um flag e avança | Ensina a clicar, mas não oferece investigação: não há escolha entre objetos, combinação de pistas ou caminhos. Cinco passos obrigatórios antes do conteúdo podem atrasar o primeiro momento interessante. |
| Inventário | `scripts/scene_1_quarto.rpy:20,30`: só entram notebook e mochila; `scripts/items.rpy:2-8` também define celular, bloco e caneta | O catálogo promete ferramentas, mas quase todas não integram o fluxo. Hoje funciona como apresentação de objetos. |
| Uso posterior do inventário | `scripts/inventory_screen.rpy:54-55` exige `notebook_available`; esse flag só liga em `scripts/scene_2_estagio.rpy:19`, após ocultar `inv_quick` em `scripts/scene_1_quarto.rpy:57-59` | A consulta de registros pelo inventário fica sem acesso pelo caminho normal quando seria útil. O notebook direto continua disponível. |
| Mapa e localidades | `scripts/backgrounds.rpy:3-14`; `scripts/scene_1_quarto.rpy:39,59`; `scripts/scene_2_estagio.rpy:45` | Existem cenários e transições lineares. Não encontrei mapa navegável, nós de localidade ou escolhas de deslocamento. |
| Missão de requisitos | `scripts/scene_2_estagio.rpy:78-129,180-232` | Bons exemplos concretos, casos limite e feedback. Entretanto, a revisão conduz à mesma descoberta, independentemente da escolha inicial. O jogador reconhece a resposta correta mais do que investiga. |
| Notebook | `scripts/notebook.rpy:4-12,38,60-64` | Boa base de memória e progresso. Atualmente recebe registros automaticamente; o jogador não compara fontes, monta requisitos ou anota dúvidas. |
| Planejamento | `scripts/scene_3_planejamento.rpy:14-18,22-25,64-65` | A seleção é reversível e ligada à necessidade. Mas os dois primeiros itens são sempre os necessários e todos custam um ponto; é principalmente identificação de escopo correto, sem decisões reais de capacidade ou dependências. |
| Negociação | `scripts/scene_4_negociacao.rpy:30-47,55-58` | Ponto forte: há dois acordos defensáveis. As alternativas inadequadas retornam ao menu; as válidas mudam o acordo textual, sem rodada seguinte que mostre entrega, atraso ou efeito no trabalho. |
| Aplicação final | `scripts/scene_5_sintese.rpy:24-39` | Produção livre é avanço relevante. A limitação da correção automática está explícita. Qualquer requisito e critério não vazios podem ser confirmados: concluir o exercício registra produção, sem comprovar qualidade. |
| Repetição | `scripts/scene_2_estagio.rpy:18-44`; `scripts/scene_5_sintese.rpy:66-73` | Troca de contexto é possível, mas reinicia o estado. Os três contextos variam os exemplos dentro da mesma estrutura; isso limita o interesse de repetir depois de aprender o padrão. |

## O ciclo que eu experimentaria primeiro

**Investigar uma situação → coletar evidências → formular uma regra → negociar uma entrega → experimentar o resultado → revisar.**

Uma missão de laboratório pode concretizar esse ciclo sem virar um simulador empresarial inteiro:

1. **Explorar três lugares úteis.** Bancada do laboratório, mesa da equipe e sala de conversa. Cada local responde a uma dúvida: o que aconteceu, o que restringe a solução e qual resultado importa. Um mapa simples com nomes e pendências basta; andar por corredores não acrescentaria decisão.
2. **Inspecionar objetos que contêm informação.** Duas planilhas mostram reservas sobrepostas; uma ficha do microscópio revela preparação de dez minutos; uma mensagem mostra que outra pessoa usa regra diferente. A pista relevante precisa ser legível e acessível por lista, além dos hotspots.
3. **Guardar evidências com origem.** “Planilha de Carlos — observação”; “dez minutos — confirmado pela técnica”; “todo equipamento exige intervalo — hipótese”. O inventário passa a ser uma pasta de trabalho, em vez de acumular objetos decorativos.
4. **Montar o requisito.** Arrastar ou selecionar cartões de ator, ação, condição e resultado. Vincular a condição à evidência correspondente. A mesma ação deve existir por teclado: selecionar cartão e escolher destino.
5. **Testar um pequeno protótipo.** Inserir duas reservas e observar a disputa do equipamento. Sem o intervalo confirmado, a segunda pessoa chega antes da preparação terminar. O feedback nasce de uma situação visível antes de Sabrina explicá-la.
6. **Rever com a equipe.** Júlio mostra a mudança necessária; Carlos relata o impacto; o jogador decide corrigir agora, reduzir a entrega ou negociar uma data. A consequência deve permanecer visível na rodada seguinte.

Arrastar cartões só vale se representar uma decisão. Mover a resposta evidentemente correta para uma caixa não resolve a falta de agência. Uma tarefa melhor apresenta duas fontes parcialmente conflitantes e permite manter uma dúvida aberta enquanto busca confirmação.

## Quests concretas

- **Por que duas pessoas chegaram às 14h?** Comparar planilhas e reconstruir a ocorrência. Entrega: problema com evidências, ainda sem solução presumida.
- **A reserva cabe no calendário, mas cabe no laboratório?** Descobrir o intervalo de preparação e perguntar se vale para todos os equipamentos. Entrega: regra confirmada e uma questão ainda aberta.
- **O que entra nesta rodada?** Escolher entre corrigir o conflito, investigar notificações ou melhorar informação do calendário, considerando objetivo e capacidade apresentados.
- **Você prometeu isso para quem?** Confirmar o mesmo acordo com usuário e desenvolvimento; detectar uma diferença de interpretação antes do compromisso.
- **Mostre funcionando.** Executar exemplos de aceitação em uma interface pequena e explicar uma falha. Entrega: evidência de teste e revisão do requisito.

As quests precisam de objetivo, pendência e resultado observável. Não precisam de níveis, moedas ou uma infraestrutura nova de missões no primeiro incremento.

## Consequências para produto, equipe e desenvolvimento

Usaria inicialmente três estados concretos: problema do usuário ainda presente ou resolvido; capacidade da rodada disponível ou comprometida; dúvida confirmada ou assumida. Evitaria medidores genéricos de confiança sem comportamento que os sustente.

- **Produto:** aceitar a integração pode reduzir consultas manuais, mas adiar a correção que evita reservas conflitantes. Se o contexto mudar, investigar a integração primeiro pode ser a escolha adequada.
- **Equipe:** um acordo não confirmado produz interpretações diferentes na próxima conversa. O conflito deve ser reparável por alinhamento, sem transformar discordância em falha moral.
- **Desenvolvimento:** critério incompleto gera comportamento que passa no exemplo inicial e falha no caso limite. Uma demonstração visível comunica melhor a consequência do que “você perdeu qualidade”.
- **Planejamento:** deixar uma dependência de fora bloqueia um item; incluir uma investigação consome capacidade, mas pode remover incerteza. Estimativas devem vir da equipe, evitando apresentar ponto como unidade universal de esforço.
- **Aprendizagem:** corrigir com ajuda deve continuar possível. Separar descoberta independente, revisão apoiada e aplicação em situação nova, preservando a distinção já existente na pontuação atual.

## Plano incremental sugerido

1. **Melhorar o início:** reduzir a preparação obrigatória e chegar mais cedo à primeira decisão de investigação. Medir abandono e compreensão antes de produzir mais cenários.
2. **Fazer uma missão investigativa completa:** apenas laboratório, três localidades, poucas evidências e uma dúvida de domínio. Critério: cada deslocamento revela informação útil ou permite confirmação.
3. **Dar função ao notebook:** fontes, hipóteses, regras confirmadas e vínculos com critérios; montagem por seleção antes de investir em arrastar.
4. **Mostrar entrega e consequência:** pequeno calendário testável, um erro recuperável e revisão. Só então ligar planejamento e negociação ao resultado.
5. **Ampliar decisões:** custos discutidos, uma dependência e duas prioridades defensáveis. Depois adaptar o ciclo para gastos e chamados, mudando o tipo de investigação, não apenas os textos.
6. **Expandir campanha conforme evidência de interesse:** novos personagens e lugares somente quando a missão curta demonstrar vontade de continuar.

## Métricas de diversão e aprendizagem

São propostas de avaliação, não resultados já demonstrados:

| Pergunta | Medida prática |
|---|---|
| O começo prende atenção? | Tempo até a primeira decisão significativa; ponto de abandono; desejo declarado de continuar após a primeira missão. |
| Explorar gera curiosidade? | Evidências opcionais procuradas espontaneamente; perguntas que o participante formula; cliques sem compreender o objetivo. |
| Há agência percebida? | Participante consegue explicar como uma escolha alterou a entrega e citar outra estratégia plausível. |
| O ciclo é divertido? | Escala curta após a missão para interesse, frustração e vontade de jogar outra; relato concreto do momento mais envolvente e do mais cansativo. |
| A pessoa quer repetir? | Escolha voluntária de experimentar outra estratégia ou outro contexto, distinguindo curiosidade de repetição por confusão. |
| A consequência ensina? | Previsão do resultado antes de executar o protótipo; explicação depois da falha; qualidade da revisão proposta. |
| Houve transferência? | Novo problema sem respostas prontas, avaliado com rubrica por pessoa: ator, comportamento, restrição, resultado observável e exceção relevante. |
| A interface atrapalha? | Pedidos de ajuda, erros de destino, uso de alternativa ao arrastar e sucesso por teclado. |

Começaria com sessões moderadas curtas com estudantes do público pretendido, comparando a missão atual e a missão investigativa. Mais tempo jogando não significa automaticamente mais diversão: pode revelar excesso de texto, dificuldade de navegação ou dúvida sobre o próximo passo.
