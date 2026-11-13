# Continuação da campanha

O encerramento anterior entregou apenas a campanha do laboratório. Esta rodada retoma o escopo restante autorizado. TodoWrite não está disponível; este registro mantém exatamente uma etapa em andamento.

- [completed] Revisar lacunas e definir os atos de desenvolvimento, equipe e produto nos três projetos.
- [completed] Implementar os projetos de gastos e chamados com mecânicas próprias, consequências e continuidade.
- [completed] Integrar seleção/progresso de projetos, feedback visual e arte.
- [completed] Executar revisão independente, testes e correções de jornada.
- [completed] Validar nove variações de iluminação, relógio de cenas e continuidade dos cenários.
- [completed] Refinar direção de arte: objetos separados com hover/foco, rótulos discretos e caixas de diálogo.
- [completed] Transformar minijogos em documentos, planilha, agenda e central de atendimento simulados; revisar e validar a nova UI.
- [completed] Integrar documentos e mensagens no notebook da mochila, com leitura persistente.
- [completed] Simplificar o menu: Novo jogo abre a campanha; demo anterior fica em Extras.
- [completed] Atualizar portfólio e preparar material de playtest humano.
- [completed] Integrar vida de estudante: dois locais opcionais e acordo de agenda, sem desviar os projetos.
- [completed] Criar e integrar ao menos uma roupa alternativa para cada um dos cinco NPCs com sprite.
- [in_progress] Recuperar nos commits a experiência original: abertura, preparação, mochila visual à esquerda e world map; integrar as novas atividades nessa jornada e corrigir nome/moldura.
- [pending] Conferir interface compacta, atualizar capturas, gerar e testar o pacote, integrar na main e limpar recursos próprios.

Decisão: manter Ren'Py e as ações determinísticas existentes. A expansão técnica está autorizada; não fingir que agentes substituem participantes humanos na avaliação de diversão, duração e aprendizagem.

Revisão após teste do autor: a entrada direta na mesa e a troca da mochila por texto prejudicaram a continuidade e a identidade do jogo original. As verificações técnicas anteriores não validavam essa preservação. A entrega foi reaberta antes do empacotamento: pesquisar a versão original nos commits e reaproveitar seus fluxos, sem tratar o jogo anterior como uma demo descartável. Nenhuma suíte de interface deve disputar a janela enquanto o autor joga.

Restrições: não alterar os arquivos preexistentes `II'` e `.playwright-mcp` da main; não apagar temporários da rodada anterior cuja exclusão foi bloqueada. Trabalho desta rodada em `X:/dev-tmp/Requirements-Whisper/campanha-completa/`. Sem Docker ou novo SDK.

## Decisão de design após revisão

Dois exploradores Sol/high verificaram código e conteúdo; Astra/high revisou o recorte. O hub guarda snapshots por projeto em `default campaign_results`, sem decisões em `persistent`. Cada projeto reinicia somente seu próprio estado; revisitar substitui somente sua conclusão, quando chegar ao novo final. Salvar/carregar permanece o mecanismo de retomar uma atividade.

- Laboratório: bancada para ordenar validação, conferência das regras escolhidas e gravação; ensaio reproduz gravação indevida e permite corrigir. Escopo escolhido continua valendo.
- Gastos: comprovante e lançamentos com identidade; total em centavos, confirmar/cancelar/desfazer, versão anterior comparável à nova. Igualdade de valor não prova duplicata.
- Chamados: triagem, perspectivas interna/pública, histórico, revisão ou publicação com acompanhamento e passagem de turno. Resolver não significa que o solicitante confirmou solução.
- Continuidade: objetos no escritório e lista acessível; resultados concretos, pendências e callbacks de Sabrina. Encerramento conjunto não é certificado de aprendizagem.

Contrato UI: `campaign_workspace(title, subtitle)` oferece painel transclude x40/y188/w1840/h700; `campaign_footer(feedback)` oferece feedback em y904. Estilos `lab_*` reutilizados. Ações editoras passam por `lab_ui_apply`; só navegação usa Return. Pasta própria `campaign_journal`, sem dados do laboratório indevidamente exibidos em outros projetos. Root integra hub/menu/arte/documentação; três implementadores possuem módulos separados de gastos, chamados e desenvolvimento do laboratório.

Aceite: cancelamento e repetição não corrompem total; outro chamado não muda junto; publicação pendente não aparece resolvida; montagem errada muda resultado do ensaio; decisões anteriores sobrevivem à troca de projeto/save/load; falas não inventam investigação; jornadas e interfaces revisadas no motor. A análise humana de ritmo/interesse/transferência fica registrada separadamente.

Feedback adicional incorporado: sem novas chamadas ao Superdesign. Interface de gastos montável por drag-and-drop e seleção equivalente; layout real aplicado e arquivado com os dados. Nova estudante Lia; Sabrina e atendimento em variação de chuva. Vida estudantil será opcional, com horários de campus/oficina e combinação explícita com a equipe; descanso não é falha. Revisão Astra encontrou recuperação insuficiente do ensaio, reparo inventado para texto livre, histórico incompleto e perda de compromisso no hub; todos entram na rodada de correções. Testes no motor encontraram necessidade de `renpy.retain_after_load` em ações editoras; a regressão mantém salvar/carregar dentro da atividade.
