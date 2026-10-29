# Conclusão da versão demonstrável

> Execução com agentes: usar `superpowers:subagent-driven-development`, com revisão independente antes da integração.

**Objetivo:** entregar uma jornada curta completa de engenharia de requisitos, do primeiro estágio ao acordo de uma entrega verificável.

**Arquitetura:** manter labels, screens e variáveis `default` do Ren'Py. Novos capítulos consomem o contexto da vaga e os requisitos já descobertos. Notebook consulta o estado da partida sem duplicar a fonte das informações.

**Tecnologia:** Ren'Py 8.5.3 e recursos existentes; sem serviço externo ou dependência adicional de runtime.

**Referência:** pedido de continuação do usuário e `docs/AVALIACAO.md`.

## Restrições e revisão

- Português claro, feedback formativo e possibilidade de revisar escolhas.
- Sem pontuar texto livre como correto por regras superficiais; aplicação final tem autoavaliação orientada.
- Salvar/carregar, rollback, repetição e troca de vaga devem manter estado coerente.
- Conteúdo no notebook aparece quando descoberto, não antes da atividade.
- Teclado, texto maior e menus longos precisam continuar utilizáveis.
- Voz e dispositivos físicos não serão declarados validados apenas por simulação.
- Publicação externa não faz parte da entrega. Empacotamento local deve excluir material de testes e músicas não utilizadas.

## 1. Jornada educacional

Arquivos: `scripts/scene_2_estagio.rpy`, novos `scripts/scene_4_negociacao.rpy`, `scripts/scene_5_sintese.rpy`, `tests/journey.rpy`.

- [ ] Acrescentar continuação no resumo, com labels `scene_4_negociacao` e `scene_5_sintese` chamadas em sequência.
- [ ] Negociar uma mudança com objetivos distintos de Carlos e Júlio, derivada do contexto escolhido; escolhas têm consequências e um acordo registrado.
- [ ] Aplicar o que foi aprendido a um novo pedido, com produção curta e autoavaliação guiada; concluir com resumo e próximos passos.
- [ ] Usar defaults `negotiation_complete`, `negotiation_agreement`, `transfer_complete`, `transfer_requirement`, `transfer_criterion`, `journey_complete`; limpar na repetição da primeira missão.
- [ ] Testar os três contextos, revisão, saída, repetição, estado e encerramento.

## 2. Notebook e apresentação do perfil

Arquivos: novo `scripts/notebook.rpy`, `scripts/inventory_screen.rpy`, `scripts/functions.rpy`, `scripts/characters.rpy`, `tests/notebook.rpy`.

- [ ] Notebook modal com problema, regra, critério, caso limite e acordo; progresso visível e textos ainda não descobertos indicados como pendentes.
- [ ] Expor `screen learning_notebook()` e `screen learning_hud()`; root conecta a missão e o menu rápido.
- [ ] Perfil com prévia visual simples do emblema escolhido, nome opcional e estados explícitos; reaproveitar estilo existente.
- [ ] Testar abertura/fechamento por teclado, conteúdo parcial/completo, nome vazio e troca/reinício.

## 3. Interface e acessibilidade

Arquivos: `screens.rpy`, `gui.rpy`, `tests/accessibility.rpy`.

- [ ] Revisar escolhas com rolagem e foco, fonte maior, menus e variante compacta; corrigir apenas problemas demonstrados.
- [ ] Ligar notebook ao menu rápido consumindo a screen e a disponibilidade definida no passo 2.
- [ ] Validar estados de preferências e capturar telas com conteúdo longo.

## 4. Integração e entrega

Arquivos: `options.rpy`, `script.rpy`, scripts de execução/build se necessários, documentação.

- [ ] Rodar testes no motor com saves isolados e lint, revisar capturas e executar revisão independente.
- [ ] Preparar pacote local Windows ou launcher reproduzível, verificando a inicialização do artefato.
- [ ] Atualizar avaliação com resultados reais e limitações; limpar temporários próprios.
- [ ] Commitar e integrar na main local, sem push automático.
