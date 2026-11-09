# De responder perguntas a transformar um projeto

Revisão de 09/11/2026, baseada no código da versão 1.1-demo, nas artes e nas capturas locais da validação anterior. Três revisores independentes: GPT-6.1 Sol, esforço alto, divididos entre narrativa, mecânicas e visual. Não houve nova partida observada nem pesquisa com jogadores nesta revisão. Os testes documentados em `docs/AVALIACAO.md` são históricos; não comprovam diversão.

**Diagnóstico:** existe uma boa atividade guiada de requisitos, mas ainda pouca experiência de ser responsável por um projeto. A principal oportunidade não é aumentar a quantidade de conteúdo: é fazer cada investigação mudar uma decisão, a decisão mudar a entrega e a entrega mudar a vida de alguém.

## O que preservar e o que mudar

| Aspecto | Força existente | Limite atual | Direção |
|---|---|---|---|
| História | Insegurança plausível no início do estágio; passagem de dias | Arco termina em agradecimento, sem mostrar o uso do produto | Voltar ao laboratório depois da entrega e acompanhar quem foi afetado |
| Diálogos | Exemplos concretos e feedback respeitoso | Sabrina explica e valida quase tudo; distratores frequentemente óbvios | NPCs com interesses, dúvidas e vozes próprias; mentor gradualmente se afasta |
| Escolhas | Dois acordos defensáveis na negociação | Planejamento e acordo quase não mudam cenas posteriores | Planos executáveis, compromissos lembrados e custos visíveis |
| Mecânicas | Seleção reversível, notebook e escrita livre | Predomínio de leitura e reconhecimento da alternativa correta | Investigar, relacionar fontes, testar protótipo, corrigir uma falha |
| Mapa | Escritório e exterior já ilustrados | Não existe mapa navegável; são transições lineares | Pequeno mapa com três destinos úteis, sem caminhadas de preenchimento |
| Inventário | Objetos e interface existentes | Perde acesso normal no estágio; quase nada é usado | Pasta de evidências e ferramentas com uma função concreta |
| Arte | Escritório acolhedor, paleta consistente | Quarto geométrico; objetos e sprites variam em acabamento | Acertar consistência e criar cenário investigável antes de multiplicar NPCs |
| Interface | Contraste, texto maior, foco e rolagem | Notebook é arquivo de textos; `learning_hud` só oferece atalho | Próximo objetivo, promessa pendente e mudança recente visíveis |
| Finais | Encerramento e repetição funcionais | Um encerramento estrutural, sem desfechos dramatizados | Epílogos combinados por resultado, compromisso e autonomia |
| Duração | Demo permite uma sessão curta | Sem tempo medido; vagas repetem estrutura | Hipótese atual: 10–20 min/contexto. Validar uma missão de 20–30 min antes de ampliar |
| Ensino | Problema, ambiguidade, aceitação, caso limite e transferência | Não cobre ciclo de software, produto e equipe em profundidade | Ampliar pelo problema vivido: priorizar, desenvolver, verificar, entregar e aprender |

As referências detalhadas estão em [narrativa](narrativa.md), [mecânicas](mecanicas.md) e [visual](visual.md). Persistência técnica existe; a lacuna é a memória narrativa. A tela de planejamento parcialmente cortada em captura foi rolada: não foi classificada como defeito sem reprodução.

## Três caminhos considerados

1. **Expandir a visual novel:** novos capítulos, mais diálogos e finais. Menor custo, mas mantém a passividade se o jogador só escolhe falas.
2. **Aventura de investigação com um produto manipulável — recomendação:** poucos cenários, evidências, conversas e um calendário funcional dentro da ficção. Dá propósito ao point-and-click e torna consequências demonstráveis.
3. **Simulador completo de estúdio:** contratar, alocar equipe, orçamento e vários projetos. Pode ser interessante mais tarde, mas agora dilui a narrativa e exige sistemas sem evidência de necessidade.

Decisão proposta pelo coordenador: manter Ren'Py e a arte existente, aprofundar primeiro o laboratório. As vagas de gastos e chamados continuam disponíveis como demo; não serão vendidas como capítulos novos por simples troca de textos. Escala provisória da campanha: 60–90 minutos, condicionada ao teste da missão curta e à preferência do usuário.

## O jogador como agente de transformação

O problema inicial é humano: duas pessoas perderam a preparação de um experimento porque receberam a mesma reserva. A promessa da campanha é poder mudar como aquele laboratório trabalha. O jogador não precisa ser um desenvolvedor que resolve tudo sozinho: articula evidência, implementação e compromisso com a equipe.

O ciclo central será **observar → investigar → propor → negociar → experimentar → acompanhar → revisar**. Uma escolha importante deve deixar três marcas: uma mudança no produto ou no trabalho, uma reação específica de alguém e um registro consultável da causa. Feedback textual sozinho não encerra esse ciclo.

### Uma missão de 20–30 minutos

- Abertura de até dois minutos: Carlos encontra duas pessoas para o mesmo microscópio. Preparação do quarto vira prólogo opcional, revisável depois.
- O jogador escolhe por onde investigar: duas planilhas, equipamento ou conversa com quem perdeu a reserva. Cada entrada oferece informação diferente; nenhuma fonte contém toda a resposta.
- Na pasta de evidências, separa o que observou do que alguém relatou e do que ainda supõe. Uma ficha sobre preparação sugere dez minutos para aquele microscópio, não para todo o laboratório.
- Na mesa da equipe, liga a reserva conflitante a uma regra e a um exemplo de aceitação. Pode arrastar cartões ou selecionar origem e destino por teclado. O significado da ligação importa mais que o gesto.
- Júlio mostra capacidade e dependências. O plano escolhido vira a configuração da entrega; omissões não são consertadas silenciosamente pelo roteiro.
- O jogador usa um calendário de demonstração: cria duas reservas e tenta iniciar uma imediatamente após outra. O comportamento depende das regras que a equipe implementou. Na rota de investigação primeiro, o calendário é explicitamente um protótipo ainda não entregue; o jogador experimenta também um procedimento temporário de confirmação centralizada, enquanto o processo anterior continua em uso.
- Uma semana depois, Carlos mostra o resultado e lembra o acordo. O jogador pode reparar uma omissão, comunicar um adiamento ou cobrar uma investigação prometida. O epílogo mostra trabalho que deixou de ser necessário e o que ainda exige atenção.

### Estrutura de campanha

| Ato | Tensão dramática | Ação do jogador | Aprendizagem decorrente |
|---|---|---|---|
| 1. Duas pessoas, um horário | Quem está com a informação certa? | Reconstruir a ocorrência e reunir fontes | Elicitação, domínio, evidência e hipótese |
| 2. Cabe na tela, não no laboratório | Regra aparentemente correta falha na preparação | Construir exemplos e testar limites | Requisito, aceitação, escopo e precisão |
| 3. A promessa de sexta-feira | Novidade útil compete com correção urgente | Planejar, negociar dependência e comunicar custo | Produto, capacidade, risco e gestão de equipe |
| 4. Funcionou ontem | Mudança ou exceção desafia a entrega | Reproduzir incidente, rever regra e testar regressão | Desenvolvimento, verificação, manutenção e versionamento |
| 5. O laboratório continua | Quem mantém o acordo depois que você sai? | Entregar, ouvir retorno e organizar responsabilidade | Adoção, acompanhamento e melhoria contínua |

Isso é uma introdução aplicada ao ciclo, não formação profissional completa. Evitar quizzes separados ao fim de cada ato: o desafio deve exigir o conceito dentro da ação. Termos técnicos podem aparecer depois da descoberta, em notas opcionais.

## Mapa, cenário e side quests

Começar com **laboratório, mesa da equipe e sala de conversa**. O mapa é uma lista ilustrada de destinos com objetivo, pessoas presentes e novidades. Mover-se não consome tempo arbitrário. Não há ruas ou corredores vazios para aumentar duração.

| Local | Interações | Evidência ou consequência |
|---|---|---|
| Laboratório | Planilhas, microscópio, ficha de preparação, terminal | Conflito observado, restrição do equipamento, antes/depois do processo |
| Mesa da equipe | Quadro de trabalho, protótipo, mensagem sobre integração | Plano efetivo, dependência e resultado dos testes |
| Sala de conversa | Pessoas e acordos sobrepostos no quadro | Conflito de prioridades, confirmação e promessa |
| Copa, em fase posterior | Conversa informal opcional | Trabalho invisível e contexto pessoal, sem esconder pista obrigatória |
| Recepção/atendimento, em outro caso | Fila e histórico de chamados | Segundo projeto com dinâmica própria, após validar o primeiro |

Cada objeto clicável precisa oferecer evidência, reação ou uma pequena recompensa de caracterização. Mostrar alvos com um comando e oferecer lista acessível evita caça a pixels. Objetos decorativos não podem parecer objetivos obrigatórios.

Side quests propostas:

- **O intervalo invisível:** acompanhar a técnica preparando o microscópio; confirmar o alcance da regra. No primeiro caso, a regra essencial também precisa de um caminho obrigatório: a missão opcional aprofunda outros equipamentos.
- **A planilha que ninguém aposenta:** descobrir por que alguém mantém cópia local. Pode revelar necessidade de acesso temporário; permite entregar um procedimento de transição, alterando a adoção no epílogo.
- **A promessa no café:** NPC lembra que o jogador prometeu retorno. Resolver produz uma fala posterior e acesso a uma observação complementar; não compra simpatia com itens.
- **Quem fica de fora do calendário?** Observar uma pessoa usando teclado ou precisando de texto maior. Rever a interface do produto e ver essa pessoa conseguir reservar. Acessibilidade básica do jogo nunca é recompensa desbloqueável.

Uma side quest só entra se mudar uma cena, artefato ou relação. Sem tarefas de buscar cinco objetos, experiência artificial ou corrida contra relógio para ler.

## Mecânicas que merecem protótipo

| Ideia | Decisão real | Retorno visível | Prioridade |
|---|---|---|---|
| Ligar evidência a requisito | Qual fonte sustenta esta regra? | Fonte e alcance aparecem ao lado da regra; hipótese continua marcada | Primeira missão |
| Montar critérios por cartões | Qual condição distingue sucesso de falha? | Executar o exemplo altera o calendário | Primeira missão |
| Arrastar tarefas para a entrega | O que cabe, o que depende de quê? | Item bloqueado explica a dependência; adiamento tem destinatário | Depois da seleção por teclado funcionar |
| Comparar versões do documento | Qual mudança atende ao acordo? | Trecho alterado e motivo aparecem juntos | Segundo ciclo |
| Reproduzir bug com passos | Que sequência causa a falha? | Caso reproduzível vira teste de regressão | Ato 4 |
| Vincular teste a requisito | O que esta verificação realmente cobre? | Lacuna aparece no cenário demonstrado | Ato 4 |
| Revisão com a equipe | Quem precisa confirmar uma hipótese? | NPC confirma, contesta ou limita o alcance | Todos os atos |

Não criar um editor livre de código ou um corretor semântico automático nesta fase. O protótipo usa um conjunto pequeno de regras representáveis e resultados determinísticos. A escrita livre continua como extensão reflexiva, com revisão humana ou autoavaliação explicitamente identificada.

## NPCs que lembram e escolhas que persistem

Memória por acontecimentos concretos, sem uma barra universal de confiança. Exemplos: `prometeu_investigar_email`, `confirmou_intervalo`, `comunicou_adiamento`, `entregou_protecao_conflito`. O registro precisa guardar quem participou, responsável, marco combinado para retorno (por exemplo, próxima reunião) e qual compromisso continua aberto. Retorno da investigação não é promessa de entrega da integração.

| Decisão | Próxima cena | Produto/cenário | Retorno posterior |
|---|---|---|---|
| Entregar base primeiro | Júlio testa a proteção; Carlos aceita consulta manual | Reservas sobrepostas bloqueadas; aviso automático ainda ausente | Carlos cobra investigação no prazo combinado |
| Investigar integração primeiro | Dependência é verificada e atraso comunicado | Processo antigo continua com alternativa temporária | Equipe conhece a limitação; pesquisa não significa integração pronta |
| Generalizar intervalo sem confirmar | Técnica contesta equipamento que não exige preparação | Calendário bloqueia tempo desnecessário | Jogador corrige alcance e demonstra uso recuperado |
| Deixar a proteção contra sobreposição fora do plano | Demonstração permite conflito | Duas reservas persistem | Incidente reparável; revisão altera entrega seguinte |
| Revisar após ouvir outra pessoa | NPC reconhece especificamente a mudança | Regra e documento mudam juntos | Mais autonomia em conversa posterior |

Uma discordância legítima não reduz automaticamente a relação. Confiança deve ser expressa por ações coerentes: avisar cedo, mostrar evidência, cumprir ou renegociar. NPCs podem estar enganados e mudar de ideia; não são gabaritos ambulantes.

Separar regra ausente, implementação defeituosa e teste não executado: pular um teste não cria um bug. A falta de teste deixa uma falha existente sem detecção; o estado do protótipo determina se a falha existe.

Exemplo de continuidade: Carlos diz “Você combinou que eu ainda consultaria o sistema esta semana. Funcionou, mas preciso saber quando retomamos o aviso.” Júlio responde olhando o plano real: “A proteção entrou; a pesquisa continua pendente. Vamos marcar a verificação da autorização antes de prometer a data.” Sabrina pergunta “O que mudou para ele?” em vez de dar outra aula.

## Finais e replay

Quatro famílias de epílogo propostas, com pequenas variações de compromissos e relações:

1. **Uma rotina confiável:** proteção entregue, limitações comunicadas e responsabilidade definida; há trabalho futuro, mas o usuário consegue confiar no horário.
2. **Uma espera com propósito:** investigação e alternativa temporária acordadas; dependência descoberta e próximo passo concreto. Não fingir que pesquisa já é entrega.
3. **Aprender com o incidente:** falha ocorreu, jogador ouviu as pessoas, corrigiu e mostrou regressão. Recuperação é um arco válido.
4. **Uma promessa sem dono:** pendências e impactos continuam visíveis; equipe propõe reparação. Não é humilhação nem tela “você é um mau profissional”.

Os finais derivam de fatos da campanha, não da soma das quatro perguntas iniciais. Exibir “O que você mudou”, “Quem percebeu” e “O que ficou pendente”, com links para decisões. Replay permite outra estratégia a partir de um marco; nova campanha limpa estado, carregar preserva estado e rollback desfaz consequência sem duplicação.

## Direção visual

![Conceito do laboratório antes e depois](arte/laboratorio-antes-depois.png)

Imagem gerada nesta revisão pelo gerador integrado do Codex. É **arte conceitual**, não cenário integrado nem screenshot. Ela explora continuidade espacial e mudança operacional: papéis conflitantes dão lugar a uma agenda compartilhada. A versão final deve manter o mesmo enquadramento entre estados; nesta imagem há diferenças de câmera e objetos, aceitáveis apenas para conceito. O alerta no calendário deve representar conflito evitado, com explicação textual na interface real.

HUD proposta: canto superior com “Etapa 2 · Verificar a entrega”; abaixo, um objetivo acionável (“Testar duas reservas seguidas”); no outro canto, acesso a mapa, evidências e projeto. Aviso discreto “Acordo atualizado: investigar e-mail depois da entrega” pode ser reaberto. Sem números decorativos de produtividade, chuva de conquistas ou interface cobrindo rostos durante conversas. Dias só serão mostrados quando o roteiro definir a passagem de tempo.

O mapa distingue destino inicial, novidade disponível, sem novidade e ação indisponível com motivo; sempre permite retornar ao objetivo. No calendário, a tentativa conflitante é rejeitada, a reserva anterior permanece e o motivo é escrito. Mostrar disponibilidade sincronizada entre consultas demonstra a melhoria; comprar um monitor não é a transformação desejada.

Notebook dividido em **Evidências / Projeto / Compromissos**. Cada entrada tem origem, estado por escrito e ligação com o que mudou. Mostrar diferenças de versão em trechos curtos; manter leitura completa e histórico. Fluxos de manipulação ocupam uma bancada própria, preservando espaço para instruções e alternativa por teclado.

Menu principal: continuar a jornada em destaque quando houver save, novo projeto e preferências claros. A arte pode refletir o capítulo somente sem spoilers e com estado derivado do save selecionado; não usar estado global de outra partida. Mochila deixa de competir com o notebook: uma entrada “Pasta de trabalho” reúne artefatos úteis.

Produção de arte em ordem: laboratório e seus estados; cartões/objetos de evidência; quarto coerente; expressões consistentes dos três NPCs; apenas então técnica do laboratório e local opcional. Textos, selos, alertas e dados do projeto são renderizados pelo motor, não embutidos na imagem gerada. A decoração não pode simular progresso que o estado do jogo não confirma.

## Como saber se ficou bom

“Bom o suficiente” requer jogadores. Revisores de código podem encontrar inconsistências, mas não demonstrar diversão. O [plano executável](../superpowers/plans/2026-11-09-evolucao-jogo.md) organiza implementação, testes técnicos e ciclos com participantes. Uma rodada de avaliação que falha gera alterações e nova rodada; não uma declaração automática de sucesso.

Primeiro objetivo de produto: a pessoa quer descobrir o que aconteceu, consegue explicar uma consequência da própria escolha e quer experimentar outra estratégia. Objetivo de aprendizagem: diante de um caso novo, consegue buscar evidência, justificar uma regra e propor um teste observável. Os dois são avaliados separadamente.
