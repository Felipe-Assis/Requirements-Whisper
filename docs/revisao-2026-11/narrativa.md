# Revisão de narrativa, escolhas e continuidade

Data: 09/11/2026. Escopo: leitura dos roteiros e da documentação; não foi executada uma partida nesta avaliação. Este relatório distingue comportamento demonstrado pelo código de interpretações e propostas.

## Diagnóstico

A versão atual entrega uma atividade educacional com começo, meio e encerramento. Como narrativa interativa, porém, ainda oferece pouca transformação do mundo: o jogador aprende a conduzir uma conversa, mas não presencia o resultado do trabalho nem modifica de forma duradoura as relações ou práticas da equipe.

## O que já funciona

- A insegurança inicial de quem começa um estágio aproxima a história da experiência do público. A passagem de tempo evita que a candidatura vire contratação instantânea: `scripts/scene_1_quarto.rpy:17`, `scripts/scene_1_quarto.rpy:27`.
- Os exemplos têm problemas identificáveis: reservas duplicadas, gasto duplicado e divergência no atendimento. Não são apenas definições abstratas: `scripts/scene_2_estagio.rpy:51`.
- O feedback explica o efeito de uma abordagem inadequada e permite rever sem punição acumulada. A distinção entre desempenho inicial e revisão apoiada é clara: `scripts/scene_2_estagio.rpy:78`, `scripts/scene_2_estagio.rpy:239`.
- Carlos e Júlio possuem interesses diferentes na negociação. O texto aceita dois acordos razoáveis e explicita que investigar não garante viabilidade: `scripts/scene_4_negociacao.rpy:23`, `scripts/scene_4_negociacao.rpy:38`.
- A escrita final sai do reconhecimento de alternativas e pede produção própria. O jogo informa corretamente que não verifica o significado do texto: `scripts/scene_5_sintese.rpy:24`, `scripts/scene_5_sintese.rpy:28`.

## Problemas prioritários

### 1. Escolhas iniciais alteram pouco a cena

**Fato:** respostas inadequadas conduzem a uma reformulação com uma única alternativa ou ao mesmo conteúdo dado por Carlos. O problema, a regra e os critérios são previamente definidos. Ver `scripts/scene_2_estagio.rpy:51`, `scripts/scene_2_estagio.rpy:92`, `scripts/scene_2_estagio.rpy:118`, `scripts/scene_2_estagio.rpy:167`, `scripts/scene_2_estagio.rpy:225`.

**Interpretação:** isso é apropriado para uma primeira atividade guiada, mas o padrão repetido faz o jogador antecipar a resposta pedagogicamente correta. Os distratores frequentemente opõem uma pergunta sensata a erros muito evidentes, como trocar “fácil” por “moderno” (`scripts/scene_2_estagio.rpy:111`). A dificuldade principal fica em reconhecer a frase certa, com pouco espaço para conduzir uma investigação.

**Proposta:** manter uma decisão guiada e transformar a seguinte em escolha entre investigações igualmente defensáveis. Exemplo: ouvir a pessoa prejudicada pela reserva duplicada ou observar a preparação do equipamento. Cada caminho revela uma evidência diferente; depois o jogador precisa procurar a evidência ausente. A ordem pode mudar a conversa sem exigir campanhas inteiramente separadas.

### 2. Planejamento não produz consequências posteriores

**Fato:** `planning_coverage` altera o feedback local (`scripts/scene_3_planejamento.rpy:64`). A negociação e o encerramento não consultam o plano. Mesmo um plano sem os dois itens essenciais pode ser concluído (`scripts/scene_3_planejamento.rpy:90`, `scripts/scene_3_planejamento.rpy:103`) e seguido pela mesma negociação, que pressupõe preservar regra e caso limite (`scripts/scene_4_negociacao.rpy:40`).

**Interpretação:** a decisão é lembrada pelo sistema da atividade, mas esquecida pela história. Surge uma descontinuidade entre o plano escolhido e o compromisso discutido depois.

**Proposta:** Júlio abre a negociação mostrando os dois itens efetivamente escolhidos. Se falta uma proteção, apresenta a situação que continua sem cobertura e pede uma decisão de escopo. A revisão modifica o plano existente, em vez de criar outra atividade desconectada. Quando o planejamento opcional não tiver sido feito, a cena pode apresentar explicitamente a proposta inicial da equipe.

### 3. Os dois acordos não têm dois desdobramentos

**Fato:** `negotiation_option` recebe `base_primeiro` ou `investigar_agora` (`scripts/scene_4_negociacao.rpy:39`, `scripts/scene_4_negociacao.rpy:44`), mas não gera cenas posteriores. O final apenas reapresenta `negotiation_agreement`: `scripts/scene_5_sintese.rpy:50`.

**Interpretação:** existe escolha de compromisso, mas falta a experiência de conviver com ele. O conflito fica resolvido no registro.

**Proposta:** acrescentar uma cena curta “uma semana depois”. Em `base_primeiro`, o problema principal foi resolvido, mas Carlos ainda precisa consultar o sistema; o jogador deve cobrar a investigação prometida. Em `investigar_agora`, surge uma dependência real e o jogador comunica o adiamento, organiza uma alternativa temporária e renegocia o próximo passo. Ambos podem terminar bem, com custos diferentes. Nenhum caminho precisa funcionar como punição por uma preferência legítima.

### 4. Há memória de aprendizagem, mas não memória social dos NPCs

**Fato:** o notebook acompanha descobertas e acordo (`scripts/notebook.rpy:4`). As quatro respostas mudam o resumo (`scripts/scene_2_estagio.rpy:240`). Não há variáveis de relação ou falas futuras que recordem uma promessa específica descumprida, uma pergunta anterior ou o plano adotado. Refazer a missão limpa o estado (`scripts/scene_2_estagio.rpy:21`). Os testes cobrem restauração do acordo por salvar/carregar (`tests/journey.rpy:44`).

**Interpretação:** Sabrina, Carlos e Júlio funcionam principalmente como papéis pedagógicos. Isso não significa que salvar/carregar esteja ausente; persistência técnica e memória narrativa são coisas diferentes.

**Proposta:** começar com dois ou três fatos lembrados, sem barra genérica de confiança: “prometeu investigar a integração”, “confirmou a necessidade com a técnica do laboratório”, “comunicou o atraso antes da reunião”. NPCs retomam esses acontecimentos e ajustam pedidos e autonomia. “Você disse que voltaria com a resposta hoje” é mais expressivo que “confiança −10”. Os fatos podem ser pequenos estados ligados a decisões concretas, sem um sistema complexo de relacionamento.

### 5. Sabrina domina a interpretação do que acontece

**Fato:** ela anuncia as quatro decisões, explica os conceitos e avalia praticamente todas as respostas (`scripts/scene_2_estagio.rpy:75`, `scripts/scene_2_estagio.rpy:82`, `scripts/scene_2_estagio.rpy:102`, `scripts/scene_2_estagio.rpy:126`, `scripts/scene_2_estagio.rpy:173`, `scripts/scene_2_estagio.rpy:232`).

**Interpretação:** o diálogo se aproxima de uma aula comentada. Carlos frequentemente confirma; Júlio entra apenas na negociação. As vozes são distinguíveis pelos papéis, mas ainda têm pouca experiência pessoal ou iniciativa fora da função didática.

**Proposta:** Sabrina faz uma pergunta e se afasta em uma segunda missão. Carlos precisa escolher entre duas necessidades próprias conflitantes; Júlio expõe uma incerteza real. A avaliação aparece depois da ação.

Exemplos de voz, apresentados como sugestões de escrita:

- Carlos: “Na terça perdi a preparação inteira. Não preciso de mais uma tela; preciso saber se posso contar com o horário.”
- Júlio: “Consigo bloquear o conflito. O e-mail depende de uma autorização que ainda não temos.”
- Sabrina: “O que você ainda precisa descobrir antes de prometer isso?”

### 6. O final reconhece participação, mas não mostra mudança

**Fato:** todos recebem o agradecimento “Você ouviu o problema…” (`scripts/scene_5_sintese.rpy:47`) e o mesmo encerramento, variando nota, acordo e existência de rascunho (`scripts/scene_5_sintese.rpy:49`). Não há cena de implantação ou uso posterior da entrega.

**Interpretação:** a conclusão fecha uma ficha de atividade, sem uma resolução dramática para a insegurança inicial. O jogador influencia um acordo, mas não vê alguém trabalhar de outra maneira por causa dele.

**Proposta:** terminar com uma situação observável: Carlos usa a entrega, encontra uma exceção e chama o jogador diretamente para discutir. Sabrina comenta uma ação específica; a autonomia adquirida substitui a dúvida “preciso saber tudo?” pela capacidade de reconhecer e investigar o que falta. Um erro anterior pode ser lembrado pela forma como foi reparado.

## Continuação proposta

Recomendo aprofundar primeiro o laboratório, usando as outras vagas como variações posteriores. Isso permite demonstrar continuidade com menos conteúdo disperso. Esta é uma proposta criativa para discussão, não uma decisão de implementação já aprovada.

| Momento | Conflito e ação | Transformação observável |
| --- | --- | --- |
| Dia 1 — Ouvir | Conflito de reserva; jogador escolhe fontes, registra evidências e negocia a primeira entrega. | Pessoas com perspectivas diferentes passam a compartilhar um problema e critérios verificáveis. |
| Dia 8 — Verificar | A equipe testa o comportamento e descobre que aplicar dez minutos a todos os equipamentos cria indisponibilidade desnecessária. | O jogador identifica a generalização, revisa o requisito e melhora como a equipe confirma regras de domínio. |
| Dia 15 — Mudar a prática | Uma pessoa com necessidade urgente entra em conflito com uma reserva confirmada. O jogador reúne perspectivas e propõe uma política transparente de exceção, com autorização e aviso. | A equipe muda como decide e comunica exceções; a transformação vai além de produzir uma tela. |

A regra existente diz “esse microscópio” (`scripts/scene_2_estagio.rpy:193`), portanto a continuação pode cobrar precisão e rastreabilidade sem contradizer o conteúdo. Para não imputar automaticamente o erro ao jogador, a generalização pode surgir na implementação de um protótipo, ou resultar de uma escolha explícita dele sobre o alcance da regra.

O encerramento combina consequências de entrega, tratamento das pessoas e cumprimento dos compromissos. Evitaria um único “final perfeito” calculado por nota: entregar cedo, investigar antes e renegociar uma regra podem ser bons caminhos quando seus custos foram discutidos. O que diferencia os finais é a prática estabelecida e a maneira como a equipe assume os próximos problemas.

Para manter o escopo pequeno, bastam inicialmente: uma cena de retorno após o acordo; duas variantes ligadas ao compromisso; poucas lembranças específicas dos NPCs; um encerramento que mostre uso e mudança de prática. Não é necessário começar com árvores narrativas grandes ou simulação geral de confiança.

## Duração

Não há medição de tempo de jogadores nos materiais inspecionados. A documentação descreve a jornada como demonstração curta, e o fluxo confirma uma única conversa principal, negociação e rascunho final.

Estimo **10–20 minutos por contexto**, dependendo da leitura, revisões e escrita. É uma hipótese para planejamento, não resultado de teste ou tempo observado. As três vagas repetem a estrutura, portanto somar três partidas não equivale a uma campanha com três capítulos.

Para uma experiência de aproximadamente 30–45 minutos, a prioridade deveria ser acrescentar consequências, retorno ao problema e autonomia gradual. Alongar a preparação ou multiplicar explicações aumentaria o tempo sem resolver a falta de continuidade. Uma rodada com estudantes deve medir separadamente leitura, decisões, planejamento opcional e escrita, além de pedir que relatem quais decisões perceberam como relevantes.

## Ordem recomendada

1. Fazer o planejamento escolhido chegar à negociação, resolvendo a descontinuidade já existente.
2. Acrescentar a cena posterior ao acordo, mostrando efeitos das duas opções.
3. Dar aos NPCs poucas lembranças concretas e falas próprias sobre esses efeitos.
4. Criar um segundo conflito com investigação menos guiada e encerrar com mudança observável da prática da equipe.
5. Medir compreensão, agência percebida e duração com jogadores antes de multiplicar contextos ou finais.

## Limites da revisão

Esta revisão não comprova o comportamento em execução, a qualidade visual, a duração real ou a eficácia pedagógica. As propostas procuram preservar Ren'Py, os personagens e os exemplos existentes. A leitura não encontrou AGENTS.md ou CLAUDE.md locais; foram consideradas as instruções fornecidas na conversa. Nenhum código do jogo foi alterado por esta avaliação.
