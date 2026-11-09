# Plano de evolução — investigar, entregar e transformar

> Para execução por agentes: usar `superpowers:subagent-driven-development` ou `superpowers:executing-plans`, seguindo uma tarefa por vez. Este plano ainda não representa funcionalidades implementadas.

**Objetivo:** tornar a jornada uma aventura em que evidências e escolhas modificam um produto, as práticas da equipe e os desfechos observados.

**Arquitetura:** preservar Ren'Py, telas nativas e estado serializável declarado com `default`. Usar poucos fatos de campanha e funções determinísticas, compartilhados por diálogos, notebook, protótipo e epílogo. Nenhum backend ou serviço de IA é necessário durante a partida.

**Tecnologia:** Ren'Py 8.5.3, Python embutido, imagens raster existentes e novas artes revisadas.

**Especificação:** [revisão e direção de design](../../revisao-2026-11/LEIA-ME.md). Ler também os três pareceres vinculados. Escala de 60–90 minutos é hipótese, não compromisso validado; a primeira entrega testável tem 20–30 minutos.

## Restrições gerais

- Diversão antes de exposição: cada bloco explicativo deve sustentar uma ação ou uma descoberta, com aprofundamento opcional.
- Toda escolha anunciada como relevante tem uma consequência identificável. Não transformar hipótese em regra confirmada por correção silenciosa.
- Arrastar tem alternativa equivalente por seleção e teclado. Informação não depende apenas de cor, posição, som ou animação.
- A regra de dez minutos se refere ao microscópio confirmado, nunca automaticamente a todos os equipamentos.
- Preservar revisão apoiada e escrita livre sem alegar avaliação automática de significado.
- Preparação e side quests opcionais não bloqueiam a história por pistas essenciais exclusivas.
- Dados de campanha pertencem ao save; `persistent` fica reservado às preferências e metadados realmente globais.
- Manter as três demos acessíveis até seus casos ganharem evolução própria. Não apagar partidas pessoais nem validar sobre saves reais.
- Temporários e resultados de testes em `X:/dev-tmp/Requirements-Whisper/evolucao/`; sem Docker necessário. Se X: estiver ausente, informar antes de escolher alternativa.
- Commits simples, sem trailers; integrar na main local após verificação e remover worktree criado para a tarefa conforme instruções globais.

## Pontos de revisão transversal

1. Carregar save antigo sem fatos novos: inicializar valores seguros e oferecer retomada coerente, sem inventar entrega realizada.
2. Rollback e repetir escolhas: desfazer evidência, promessa e consequência juntas, sem contar cliques repetidos como progresso.
3. Fonte maior e teclado: abrir, operar e fechar cada modal, devolvendo foco ao ponto adequado; atalhos não interceptam escrita.
4. Caminhos opcionais ou incompletos: história continua com pendência explícita; epílogo nunca atribui investigação não realizada.
5. Divergência entre plano e fala: negociação, protótipo e epílogo consultam o mesmo plano confirmado, inclusive quando falta proteção.

## Entregas e ordem

Não produzir cinco capítulos em paralelo. Primeiro provar a cadeia inteira com poucas escolhas. Depois ampliar conteúdo sobre o contrato verificado. Um responsável integra estado e testes; narrativa e arte podem trabalhar em arquivos separados após o contrato estar estável.

| Ciclo | Resultado jogável | Depende de | Porta de saída |
|---|---|---|---|
| A | Plano e acordo aparecem no teste de uma entrega e numa cena posterior | Demo existente | Dois caminhos têm consequência real e coerente |
| B | Laboratório investigável, evidências e mapa de três destinos | A | Missão inteira operável por teclado; fonte e hipótese distinguíveis |
| C | Projeto manipulável, planejamento e memória social | B | Jogador explica o que mudou por uma escolha |
| D | Side quest, recuperação de incidente e epílogos | C validado com pessoas | Há vontade de continuar e nenhuma rota sem saída |
| E | Campanha e casos de gastos/chamados com desafios próprios | D | Revisão por ato e evidência de transferência |

## Contrato mínimo do primeiro caso

Criar `scripts/project_state.rpy` apenas para o caso do laboratório, sem framework genérico de quests. Estrutura proposta, que o executor pode simplificar preservando os comportamentos:

- `default campaign_version = 1`.
- `default lab_evidence = []`: IDs conhecidos, sem duplicatas; usar estruturas compatíveis com rollback do motor.
- `default lab_rule_status = "hypothesis"`: valores `hypothesis`, `confirmed`, `revised`.
- `default lab_plan = []`: IDs dos itens confirmados, sem derivar a entrega da nota.
- `default lab_commitment = ""`: `base_primeiro` ou `investigar_agora` quando confirmado.
- `default lab_commitment_owner = ""` e `default lab_return_milestone = ""`: responsável e marco de retorno da investigação, sem prometer a entrega da integração.
- `default lab_commitment_participants = []` e `default lab_commitment_status = "open"`: pessoas que confirmaram e estado `open`, `fulfilled` ou `renegotiated`. No primeiro caso há um compromisso de investigação ativo; não criar sistema genérico de contratos.
- `default lab_events = []`: fatos narrativos explícitos, com ocorrência única quando aplicável; sem timestamp real.
- `default lab_delivery = "not_delivered"`: `not_delivered`, `base_delivered`, `repaired`.
- `default lab_visit = "first"`: `first` ou `followup`, para controlar o momento, não o resultado.
- `lab_project_view()` retorna dados derivados de estado para o protótipo, objetivo e epílogo; não altera estado durante renderização.
- `lab_reservation_result(existing, candidate, rules)` retorna `allowed`, `conflict` ou `preparation_required`. Entradas usam equipamento e minutos inteiros; intervalos semiabertos: fim igual ao início não sobrepõe. Preparação confirmada do microscópio pode impedir esse encaixe. Explicar a convenção no teste, não assumir implicitamente.

O executor deve mapear IDs de `planning_selected` atuais para `lab_plan`, e `negotiation_option` para `lab_commitment`, em um ponto de confirmação. Não manter duas versões editáveis independentes. Uma alteração posterior de escopo passa pela mesma confirmação. O protótipo nunca escolhe regras com base em `mission_score`.

## Tarefa 1 — Fechar o ciclo de uma decisão existente

**Arquivos:** modificar `scripts/scene_3_planejamento.rpy`, `scripts/scene_4_negociacao.rpy`, `scripts/scene_5_sintese.rpy`; criar `scripts/project_state.rpy`, `scripts/scene_6_retorno.rpy` e `tests/consequences.rpy`.

**Entrada:** seleção e acordo existentes. **Saída:** plano confirmado, fato de entrega e cena de retorno que os consulta.

- [ ] Escrever teste que escolhe plano sem proteção, confirma acordo e verifica que o retorno não declara proteção entregue. Confirmar falha no estado atual.
- [ ] Escrever testes para os dois acordos: base primeiro resolve conflito somente se a proteção estiver no plano entregue, deixando consulta manual; sem proteção o conflito permanece. Investigação primeiro mantém entrega pendente e registra dependência descoberta, sem alegar integração pronta.
- [ ] Criar demonstração mínima reaproveitável: dois horários predefinidos e botão “Tentar reservar”, usando `lab_reservation_result`. Mostrar aceitação ou rejeição da tentativa e reserva preservada. A Tarefa 3 amplia essa mesma tela e função; o ciclo A não pode ser aceito com apenas diálogo sobre o resultado.
- [ ] Implementar confirmação de escopo real. Se o planejamento foi pulado, mostrar proposta de plano antes do acordo; não fabricar uma escolha atribuída ao jogador.
- [ ] Implementar retorno com Carlos e Júlio, retomando promessa específica e oferecendo uma reparação coerente.
- [ ] Na rota de investigação, distinguir protótipo de produto entregue e permitir experimentar confirmação centralizada temporária. Registrar responsável e reunião de retorno antes de cobrar o compromisso.
- [ ] Testar salvar/carregar, rollback antes do acordo, mudança de opção e repetição da missão; não duplicar fatos. Cobrir save antigo.
- [ ] Rodar lint e suíte existente; revisar duas rotas completas e integrar commit.

Aceite: pelo menos uma mudança de plano altera comportamento mostrado, uma fala posterior e registro. Apenas repetir o texto do acordo não passa.

## Tarefa 2 — Exploração e evidências com origem

**Arquivos:** criar `scripts/lab_exploration.rpy`, `tests/exploration.rpy`; modificar `scripts/scene_1_quarto.rpy`, `scripts/scene_2_estagio.rpy`, `scripts/notebook.rpy`, `scripts/backgrounds.rpy`.

**Entrada:** estado do caso e assets revisados. **Saída:** `lab_evidence` e fonte de confirmação de cada regra.

- [ ] Testar visita a laboratório, mesa e sala em ordens diferentes; inspecionar a mesma pista duas vezes não duplica registro nem bloqueia saída.
- [ ] Criar três evidências essenciais: duas reservas incompatíveis, preparação do microscópio, relato da pessoa afetada. Distinguir observado, relatado e hipótese.
- [ ] Criar mapa simples com destino e pendência, incluindo sem novidade, indisponível com motivo e retorno ao objetivo. Hotspots e lista de objetos usam as mesmas ações.
- [ ] Reduzir prólogo obrigatório; permitir conhecer perfil e mochila depois, sem perder escolhas anteriores.
- [ ] Adicionar mecanismo de confirmação quando fonte é insuficiente. Pista opcional não deve ser único caminho para concluir a missão.
- [ ] Testar exploração incompleta, retorno ao mapa, fonte maior, mouse e teclado; confirmar ausência de resposta escondida por hover.
- [ ] Validar screenshots no motor e integrar commit.

Aceite: o jogador escolhe a ordem de investigação e distingue fonte de inferência; nenhum deslocamento obrigatório existe apenas para aumentar duração.

## Tarefa 3 — Ligar requisito, evidência e teste

**Arquivos:** criar `scripts/requirements_board.rpy`, `scripts/lab_prototype.rpy`, `tests/lab_prototype.rpy`; modificar `scripts/notebook.rpy`, `scripts/project_state.rpy`.

**Entrada:** evidências e plano confirmado. **Saída:** vínculo justificado, configuração da entrega e resultado visível de teste.

- [ ] Testar reservas sobrepostas, adjacentes, em equipamentos diferentes, com preparação específica e entrada inválida (fim anterior ao início).
- [ ] Testar vínculo de hipótese não confirmada: manter estado explícito e permitir buscar fonte, sem marcar resposta correta automaticamente.
- [ ] Implementar primeiro seleção de cartão + destino. Só adicionar drag-and-drop depois que seleção estiver funcional; ambas chamam a mesma ação.
- [ ] Implementar calendário de demonstração com poucas regras e exemplos. Uma regra ausente deve produzir a falha correspondente, recuperável na revisão. Pular um teste não cria uma falha numa regra já implementada; testar essa independência.
- [ ] Mostrar tentativa conflitante rejeitada, reserva anterior preservada e motivo textual. Mostrar a mesma disponibilidade em duas consultas, sem usar apenas alerta vermelho como prova de sucesso.
- [ ] Dar feedback por pessoa afetada e comportamento do produto antes da explicação conceitual opcional.
- [ ] Testar teclado completo, desfazer vínculo, modal, texto longo, rollback após teste e salvar/carregar antes da revisão.
- [ ] Rodar regressão, inspecionar capturas e integrar commit.

Aceite: uma pessoa consegue demonstrar a falha e propor a mudança; arrastar o cartão “certo” sem efeito no protótipo não basta.

## Tarefa 4 — Planejamento com custo e memória dos NPCs

**Arquivos:** modificar `scripts/scene_3_planejamento.rpy`, `scripts/scene_4_negociacao.rpy`, `scripts/scene_6_retorno.rpy`, `scripts/project_state.rpy`; ampliar `tests/planning.rpy`, `tests/consequences.rpy`.

**Entrada:** evidência e comportamento demonstrado. **Saída:** plano coerente, dependência explícita e fatos lembrados.

- [ ] Escrever testes de compromisso cumprido, renegociado e pendente; comentário do NPC deve corresponder ao evento correto.
- [ ] Trocar “dois itens equivalentes” por três ou quatro itens com estimativas contextualizadas e uma dependência real. Explicar incerteza; não ensinar ponto como unidade universal de tempo.
- [ ] Criar tela própria com plano atual, capacidade e consequência da mudança simultaneamente visíveis.
- [ ] Dar duas prioridades defensáveis. Preservar opção de investigar antes e custo de manter processo atual.
- [ ] Inserir callbacks curtos em Carlos, Júlio e Sabrina; evitar reexplicar toda a decisão.
- [ ] Testar mudança de ideia antes/depois da confirmação, ausência de planejamento e fala sem fatos ainda não descobertos.
- [ ] Revisar narrativa e integrar commit após testes.

Aceite: NPC lembra uma ação concreta; o jogador consegue reconhecer a causa da reação sem consultar uma pontuação invisível.

## Tarefa 5 — HUD, notebook e arte de continuidade

**Arquivos:** modificar `scripts/notebook.rpy`, `screens.rpy`, `scripts/backgrounds.rpy`, `DESIGN.md`; criar imagens finais em `images/bg/` e `images/items/`; ampliar `tests/notebook.rpy`, `tests/accessibility.rpy`, `tests/visual.rpy`.

**Entrada:** estado derivado comum. **Saída:** próximo passo, compromisso pendente e antes/depois coerentes.

- [ ] Testar HUD em cada marco, no retorno, após rollback e ao trocar de contexto; planejamento opcional não aparece como bloqueio.
- [ ] Implementar Evidências / Projeto / Compromissos e aviso reabrível do que mudou. Distinguir pendência de conclusão. Usar etapa, sem inventar contagem de dias não definida no roteiro.
- [ ] Gerar background final usando referências existentes, separar estados por camadas e documentar prompts. O conceito desta revisão não é asset final: contém duas cenas numa imagem e variações de geometria.
- [ ] Corrigir notebook com selo deformado e criar quarto consistente, se continuar visível no fluxo. Texto e ícones funcionais permanecem no motor.
- [ ] Inspecionar normal/maior/compacto, contraste, sobreposição, foco e leitura. Testar voz PT-BR separadamente antes de alegar suporte verificado.
- [ ] Conferir consumo das imagens e build para não distribuir conceitos/documentos desnecessários; integrar commit.

Aceite: progresso corresponde ao que aconteceu; sem “100%” por apenas ter passado pelos diálogos.

## Tarefa 6 — Uma side quest e finais distintos

**Arquivos:** criar `scripts/lab_sidequest.rpy`, `scripts/lab_endings.rpy`, `tests/endings.rpy`; modificar `scripts/scene_5_sintese.rpy`, `scripts/project_state.rpy`.

- [ ] Escrever matriz de epílogos com prioridade explícita para combinações, evitando finais contraditórios. “Não entregue” não pode mostrar calendário funcionando em produção.
- [ ] Implementar primeiro “A planilha que ninguém aposenta”: opcional, curta e com consequência na adoção; caminho principal continua completo sem ela.
- [ ] Implementar as quatro famílias propostas e variantes pequenas para compromissos, sem explosão de árvores de diálogo.
- [ ] Testar cada final e pares de condições concorrentes, quest ignorada/concluída, reparação e replay sem vazamento de fatos.
- [ ] Revisar resultado e causa com participantes antes de ampliar localidades; integrar commit técnico, registrando avaliação humana ainda pendente se for o caso.

Aceite: epílogo mostra transformação, custo e próximo passo. Escolher investigação primeiro nunca equivale automaticamente a fracasso.

## Tarefa 7 — Ampliar após validar a missão

**Arquivos:** criar atos de incidente e acompanhamento em `scripts/`; novos testes por ato. Definir nomes finais só após estabilizar os atos anteriores.

- [ ] Ato de desenvolvimento: transformar critério em mudança pequena no protótipo; comparar versão anterior e nova, reproduzir bug e verificar regressão.
- [ ] Ato de equipe: tornar dependência, revisão e comunicação parte do conflito; sem simular pessoas como barras de produtividade.
- [ ] Ato de produto: verificar adoção e objetivo depois da entrega; distinguir saída produzida de resultado para usuário.
- [ ] Adaptar gastos e chamados com fontes, riscos e tipos de teste próprios, evitando simples troca de substantivos.
- [ ] Medir duração real por ato; cortar exposição antes de acrescentar minutos.
- [ ] Rodar ciclo técnico e com participantes para cada ato, revisar plano e integrar incrementos pequenos.

## Execução técnica e evidência

Antes de implementar, localizar SDK existente e verificar versão; não instalar outro por padrão. Usar worktree isolado se houver mudanças concorrentes, mantendo temporários no X:. Não remover o arquivo não rastreado `II'`, preexistente à revisão.

Com caminhos locais confirmados, executar lint e testes do motor em área de resultados temporária. O parâmetro `--savedir` isola saves, mas não garante que relatórios e capturas saiam do checkout: ajustar a execução ou usar cópia de teste no X: para esses arquivos. Não afirmar que só mudar `--savedir` atende a toda a regra de temporários.

```powershell
# $sdk e $testProject apontam para caminhos verificados; $testProject fica no X:.
& "$sdk/lib/py3-windows-x86_64/python.exe" "$sdk/renpy.py" $testProject lint
& "$sdk/lib/py3-windows-x86_64/python.exe" "$sdk/renpy.py" $testProject test --savedir 'X:/dev-tmp/Requirements-Whisper/evolucao/saves' --report-detailed
```

Para cada tarefa: teste que falha pelo comportamento ausente → implementação → teste passando → regressão proporcional → inspeção de UI quando aplicável → revisão independente → commit/main → limpeza dos recursos próprios. Não recalcular baseline visual automaticamente para ocultar diferença.

## Loop para avaliar diversão e aprendizagem

Realizar rodadas exploratórias com 5–8 participantes do público, número proposto para detectar problemas qualitativos, sem inferência estatística. Não há participantes recrutados nesta entrega. Sessões consentidas e notas locais bastam; não criar telemetria obrigatória.

1. Jogar sem explicação prévia dos conceitos, observando ajuda necessária e momentos de interesse.
2. Perguntar o que tentava fazer, qual decisão teve efeito e o que faria diferente; evitar induzir a resposta.
3. Oferecer continuar ou explorar outra estratégia, sem obrigação de replay. Registrar aceitação espontânea, motivo de recusa e sinais observados de curiosidade, cansaço ou aborrecimento; distinguir falta de tempo de desinteresse.
4. Apresentar problema novo curto: pedir evidência que buscaria, regra proposta, teste e limitação. Revisão humana por rubrica.
5. Registrar achados com frequência, gravidade, evidência e mudança proposta. Selecionar os três problemas de maior efeito.
6. Corrigir, executar testes e repetir com pessoas novas; incluir algumas anteriores para verificar o problema específico, distinguindo familiaridade.

Metas iniciais de decisão, a calibrar depois da primeira rodada:

| Critério | Sinal esperado | Se falhar |
|---|---|---|
| Primeiro interesse | Primeira decisão significativa em até 2 min para a maioria | Cortar preparação e antecipar conflito |
| Orientação | Pelo menos 80% concluem missão sem intervenção sobre navegação | Corrigir objetivo, foco e pistas antes de ampliar conteúdo |
| Agência | Pelo menos 80% citam uma consequência específica da própria escolha | Tornar causa, retorno e mudança do produto explícitos |
| Interesse | Pelo menos 70% dizem querer outro capítulo e explicam por quê; cruzar com continuação voluntária e observação, sem concluir por intenção isolada | Rever ritmo e desafio; não adicionar recompensas arbitrárias |
| Fricção | Nenhum bloqueio recorrente por interface; teclado completa o ciclo | Corrigir interação antes de novas quests |
| Transferência | Maioria liga necessidade, evidência e teste num caso novo | Rever a atividade que exercita o conceito, não acrescentar aula por padrão |

Com amostras pequenas, registrar contagens brutas (ex.: 4/5), justificativas e exceções, sem falsa precisão. Tempo alto pode indicar confusão, não engajamento. Rubrica de transferência: 0 ausente, 1 parcial/com apoio, 2 justificado autonomamente para necessidade/evidência, regra/alcance e teste observável; não usar total como certificação profissional.

Saída do ciclo de demo: duas rodadas sem bloqueadores recorrentes e evidências consistentes de agência e vontade de continuar. Saída da campanha: cada ato validado, consequências integradas, finais coerentes e transferência observada. Se o resultado não atingir as metas, continuar revisão; não afirmar que a campanha está pronta porque testes automatizados passaram.

## Estado desta entrega

Concluídos: revisão do repositório, brainstorming, conceito visual, plano e revisão cruzada documental. Pendentes: implementação dos ciclos A–E, novas execuções no motor, recrutamento de participantes e validação de diversão/aprendizagem. O plano oferece um caminho executável; não substitui esses resultados.
