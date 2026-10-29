# Avaliação do jogo — 29/10/2026

## Histórico da primeira rodada

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

## Conclusão da jornada — versão 1.1-demo

A segunda rodada, realizada com agentes Sol, amplia a primeira missão até um encerramento. A tabela e os resultados anteriores registram a rodada inicial; os próximos passos daquela tabela que tratavam de negociação, transferência e notebook foram implementados nesta continuação.

Carlos e Júlio agora têm objetivos distintos. Carlos pede uma integração para reduzir consultas manuais; Júlio explica dependências e o efeito de assumir essa mudança na entrega. As três vagas mudam o pedido e o impacto discutido. Há dois acordos possíveis: preservar a entrega da regra e do caso limite e investigar a integração na próxima rodada, ou investigar agora e renegociar a data. Prometer tudo no mesmo prazo ou recusar a conversa recebe feedback com uma consequência concreta e permite rever a escolha. O acordo confirmado fica no notebook, sem nota adicional.

A aplicação final apresenta uma necessidade nova em cada contexto. A pessoa escreve um requisito e um critério de aceitação, confere o rascunho em uma tela com rolagem e decide se precisa reescrever. A autoavaliação pergunta sobre quem age, condições, resultado observável e exceções. O jogo não atribui correção semântica ou nota ao texto livre. A confirmação registra um rascunho revisado pela própria pessoa, ainda sujeito à discussão com a equipe. Também é possível concluir a história com o exercício pendente e retomá-lo pelo menu final.

O notebook mostra problema, regra, critério e caso limite apenas depois de descobertos na conversa, incluindo revisões orientadas. Acordo e aplicação aparecem após sua confirmação. O atalho N e o botão Notebook permitem consultar os registros durante o estágio. Durante a digitação, o atalho N fica indisponível para não interceptar a letra; a entrada e a revisão usam áreas amplas com rolagem. O reinício limpa o estado das atividades e a troca de vaga oculta o notebook até o novo contexto começar.

O perfil ganhou prévia visual dos emblemas existentes, com nome opcional e indicação da escolha atual. Isso não constitui um editor de retratos. A navegação e as preferências continuam em português, com foco visível, fonte maior, opções explícitas, menus e histórico roláveis. Os testes de variante compacta usam o motor; eles não substituem uso em aparelhos físicos nem avaliação com pessoas usuárias de tecnologia assistiva.

### Verificações da continuação

As verificações desta rodada cobrem negociação e revisão dos dois acordos, três contextos, rascunho e exercício pendente, encerramento, repetição, descoberta gradual no notebook, perfil e acessibilidade. A jornada exercita salvar/carregar o acordo e entrada de texto com a tecla N. O caso de texto longo usa fonte maior, registros próximos aos limites de 300/400 caracteres e marcação literal; as capturas da entrada e da revisão com rolagem foram inspecionadas.

- Ren'Py 8.5.3 no Windows: lint sem erros; 145 blocos de diálogo, 21 menus e 39 telas.
- Suíte completa: 27 casos e 210 verificações passaram, incluindo capturas opcionais.
- Acessibilidade: quatro casos passaram em desktop (10 verificações) e na variante compacta/touch do motor (6 verificações).
- Revisão independente de fluxo, estado, texto livre e build sem bloqueadores. A revisão encontrou a tecla N interceptando a escrita e textos longos excedendo a caixa de diálogo; ambos foram corrigidos e cobertos por testes.
- Capturas inspecionadas: [perfil](capturas/perfil.png), [notebook com fonte maior](capturas/notebook.png), [revisão de texto longo](capturas/revisao-rascunho.png) e [preferências compactas](capturas/preferencias-compactas.png).

Os números da seção anterior pertencem à primeira rodada.

### Pacote local

O comando `./tools/build-windows.ps1 -SdkPath 'C:/caminho/renpy-8.5.3-sdk'` prepara o projeto para o distribuidor do SDK e grava o ZIP Windows e seu SHA256 em `dist/`. O script exclui testes, saves, metadados Git e músicas não utilizadas e limpa a área temporária. Os módulos de áudio do próprio motor permanecem no pacote.

Artefato gerado: `TheRequirementsWhisperer-1.1-demo-win.zip`, 97.289.694 bytes. SHA256: `7d00bb394be6adac5aafc50140caf0608833ac5244b2cf48646d467730e08175`.

O ZIP foi extraído em uma pasta separada. Somente os roteiros de teste foram acrescentados à cópia extraída; fontes e recursos do jogo vieram do pacote. O executável distribuído iniciou o jogo e passou nos 26 casos funcionais e nas 210 verificações, sem usar o SDK. O caso opcional de capturas ficou desativado nessa rodada. Os diretórios temporários do build foram removidos pelo script; o ZIP e seu SHA256 permanecem em `dist/` para uso local. Docker não foi utilizado.

A política de execução bloqueou a limpeza posterior, inclusive com caminhos literais conferidos. Permaneceram localmente, fora do Git: `dist/validacao/`, logs em `dist/`, `.test-saves/`, `tests/screenshots/`, `.build-windows.log` e `premium-audit.json`. São resultados desta sessão, não dependências do jogo. A cópia em `dist/validacao/` contém testes acrescentados; o ZIP de entrega não contém esses testes.

A distribuição externa continua fora do escopo desta rodada. As limitações sobre origem das artes, vozes, aparelhos físicos e plataformas adicionais permanecem aplicáveis.
