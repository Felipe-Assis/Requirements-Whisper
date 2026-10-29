# Avaliação do jogo — 29/10/2026

O protótipo disponível terminava na escolha de uma vaga. A preparação chamava cinco telas inexistentes; os cenários do quarto e do notebook não estavam definidos. O inventário referenciava imagens ausentes e trocava o identificador do notebook ao guardá-lo, o que poderia causar erro ao consultar o item. Apenas README e .gitignore estavam versionados.

A intervenção preserva o motor e as artes existentes e entrega uma primeira missão completa de engenharia de requisitos. A avaliação foi dividida entre três agentes Astra: narrativa e aprendizagem, interface e acessibilidade, mecânicas e personagens.

| Aspecto | Avaliação e melhoria implementada | Próximo passo útil |
| --- | --- | --- |
| Diálogos | Abertura com uma insegurança plausível de quem inicia um estágio; perguntas abertas e feedback que explica consequências. | Testar compreensão e duração com estudantes; reduzir trechos que pareçam expositivos demais. |
| História | Candidatura antes de guardar o notebook, passagem de dias explícita e chegada ao estágio. As três vagas mudam o problema e os exemplos. | Criar uma missão de negociação entre pessoas com necessidades conflitantes. |
| Aprendizagem | Quatro decisões: investigar o problema, esclarecer uma ambiguidade, verificar a entrega e explorar um caso limite. Resumo distingue autonomia de revisão com apoio. | Exercício de transferência com uma necessidade nova e justificativa do estudante, além de escolhas fechadas. |
| Personagens | Sabrina acompanha o estágio; Carlos relata uma necessidade concreta. Sprites e expressões existentes aparecem na missão. | Dar a cada personagem objetivos próprios e decisões com consequências em capítulos posteriores. |
| Avatar | Nome fictício opcional e escolha de emblema textual do perfil, sem idade obrigatória. | Avatar visual com prévia e alternativas de aparência, se houver arte consistente disponível. O emblema atual não é um editor de retratos. |
| Gráficos | Escritório ilustrado no menu e missão; quarto composto com elementos nativos; objetos existentes apresentados com alvos nomeados. | Produzir um cenário de quarto coerente com o escritório e revisar consistência de escala entre expressões. |
| Acessibilidade | Botões por teclado, foco visível, texto maior, texto instantâneo, transições configuráveis, histórico sem altura fixa e estados escritos nas opções. | Testar com pessoas usuárias de tecnologia assistiva, vozes PT-BR e aparelhos menores. |
| Mecânicas | Preparação funcional, inventário com IDs estáveis, revisão do requisito, repetição e troca de contexto sem acumular pontuação. Atividade opcional de montar e revisar um escopo de dois itens, com feedback ligado à necessidade. | Integrar o notebook a futuras atividades de registrar e comparar requisitos. |
| Efeitos e áudio | Transições discretas e desativáveis; nenhuma informação depende de áudio. Indicadores não piscam. | Selecionar efeitos e trilha adequados após registrar origem e permissões dos arquivos existentes; áudio de fala não foi produzido. |

## Limites pedagógicos

O exemplo de uma regra funcional não demonstra que o sistema inteiro será fácil de usar; o diálogo deixa essa diferença explícita. Os critérios são exemplos verificáveis, não uma especificação exaustiva. O caso limite acrescenta uma regra discutida com a pessoa interessada, em vez de presumir uma resposta universal.

A nota representa quatro escolhas iniciais em uma atividade curta. Ela não deve ser apresentada como avaliação completa de competência em engenharia de software. Repetir permite experimentar outra abordagem; não há punição por precisar de feedback.

A atividade de planejamento usa uma capacidade fictícia de dois itens e não atribui nota. O feedback compara o plano ao objetivo confirmado para aquela rodada; não afirma que relatórios, personalização ou outros extras sejam sempre menos importantes. O roteiro explica que estimativas, dependências e riscos precisam ser discutidos em projetos reais.

## Escopo da verificação

Os testes usam Ren'Py 8.5.3 no Windows e percorrem a interface real. Capturas do motor permitem revisar menu, preparação, perfil, acessibilidade e escolhas com fonte ampliada. A execução de testes e o lint são registrados na entrega; voz, Android, iOS e navegador precisam de validação própria.

As artes e músicas já estavam no diretório antes desta intervenção. Não foi criada nova arte para o jogo nem ativadas as faixas musicais. A origem e os créditos desses recursos ainda precisam ser documentados antes de uma distribuição pública.

## Resultado da verificação

- Ren'Py 8.5.3: lint sem erros; 116 blocos de diálogo e 17 menus.
- Suite completa com capturas opcionais: 15 casos, 131 verificações, nenhum erro.
- Cópia limpa criada por `git archive`: 14 testes funcionais e 131 verificações passaram sem depender de arquivos ignorados; a captura opcional ficou desativada nessa rodada.
- Caminhos exercitados: três contextos, respostas adequadas e distratores, revisão orientada, repetição, troca de vaga, planejamento com cobertura 0/1/2, inventário, navegação inicial por teclado e menu de acessibilidade.
- Salvar/carregar restaura pontuação e escolhas; rollback até a decisão anterior permite mudar a resposta sem acumular pontos.
- Capturas revisadas com fonte maior. O menu de planejamento ganhou rolagem para não se sobrepor ao diálogo; PgDn e retorno foram exercitados no motor.
- Revisão adicional por agente não encontrou bloqueadores no estado e nos retornos da atividade de planejamento.

Capturas da versão verificada: [menu inicial](capturas/menu.png), [diálogo com fonte maior](capturas/dialogo.png) e [planejamento após rolagem](capturas/planejamento.png).

Não foram usados containers Docker. O SDK oficial foi conferido pelo SHA256 e permanece no cache local de ferramentas para repetir as verificações; ele não faz parte do repositório.
