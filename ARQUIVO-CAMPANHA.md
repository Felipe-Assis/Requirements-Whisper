# Campanha alternativa preservada

Snapshot de 13/11/2026 das alterações locais sobre `c934289`, preservado na branch
`archive/campanha-completa-20261113`. Este é um arquivo de referência e não a versão
canônica do jogo. O checkout de trabalho pode ser removido depois de confirmar o push.

O jogo atual está em `C:/Users/Felipe/Documents/GitHub/Renpy Projects/Requirements-Whisper`.
Não mesclar esta branch inteira na principal: entrada, personagens, estado, relógio e
organização dos arquivos são diferentes. A versão atual já adaptou notebook, gastos,
chamados e agenda semanal. A agenda atual preserva reservas, renegociação, acordo e
presença por rota/semana; o diagnóstico anterior de que ela faltava ficou desatualizado.

Esta versão conserva o caso do microscópio, a passagem de turno com responsável disponível,
o gesto de arrastar módulos da interface, o hub que reúne três projetos e as artes próprias.
Esses elementos continuam úteis como referência, mas não são correções pendentes que
devam substituir as rotas atuais.

Foram preservados todos os fontes e recursos não ignorados: 285 arquivos existentes,
cerca de 223 MiB, mais este registro. A revisão encontrou 14 arquivos rastreados alterados
e 98 novos. Cinco artes e um documento já existem idênticos no canônico; os outros arquivos
podem ter equivalentes adaptados, sem identidade byte a byte.

Verificação deste snapshot: 73 testes Python de estado passaram. Não foi executada uma
nova validação visual ou suíte no motor Ren'Py; o arquivo não declara uma nova entrega.
Não foram encontrados arquivos acima de 100 MiB nem credenciais nos nomes/padrões
verificados, o que não equivale a uma auditoria completa de segurança.

Os saves locais e compilados, que não devem ir ao Git, ficam preservados separadamente
em `E:/dev-archives/requirements-whisper/campanha-completa-20261113/local-state.zip`,
com manifesto SHA-256 ao lado. O relatório de comparação está em
`X:/dev-tmp/docker/auditoria-global-20261113/campanha-deep-review.json`.

Para recuperar esta evolução, faça checkout da branch de arquivo em outra pasta. Se precisar
retomar saves antigos, restaure o ZIP local nessa cópia antes de abrir o motor, preservando
os compilados originais. Nunca extraia esse estado sobre o jogo canônico.
