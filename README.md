# The Requirements Whisperer

A [revisão criativa](docs/revisao-2026-11/LEIA-ME.md) originou a campanha **O horário de todo mundo**. Veja o [portfólio interativo](docs/portfolio/index.html), com artes, mecânicas e um simulador das consequências. Abra o HTML em um navegador; não exige servidor nem conexão.

Versão **1.3-cidade**. A campanha reúne três projetos: reservas de laboratório, controle de gastos e atendimento de chamados. Investigue objetos e relatos, defina o escopo, monte e teste mudanças e volte às pessoas afetadas. A mesa da equipe conserva resultados, compromissos, pendências e a interface criada, mesmo quando você troca de projeto.

No menu, **Novo jogo** abre a campanha. A demo guiada anterior fica em **Extras → Demo guiada anterior**, com os três contextos e escrita livre. As duas jornadas têm estado separado; preferências de leitura continuam compartilhadas.

No laboratório, ordenar validações e gravação muda o resultado do ensaio. Em gastos, você monta a interface arrastando módulos ou selecionando posições, confere comprovantes e testa excluir, cancelar e desfazer. Em chamados, acompanha as perspectivas interna e pública, verifica o histórico e negocia a passagem de responsabilidade. As escolhas alteram entregas e retornos; concluir uma investigação não equivale a entregar uma correção.

A cidade oferece faculdade e oficina comunitária. Organize duas noites entre estudo, curso, plantão e descanso e combine a disponibilidade com Sabrina. O relógio acompanha as cenas de cada caso, com versões de manhã, tarde, noite e chuva dos mesmos locais. Não é um calendário contínuo nem um simulador livre de cidade. Há 29 novos arquivos de arte nesta expansão: 18 fundos e variantes, seis sprites de personagens, quatro objetos transparentes e uma moldura de diálogo. Os objetos têm destaque no mouse/foco; os cinco NPCs têm roupa alternativa. A [revisão completa](docs/REVISAO-COMPLETA.md) registra as mudanças e o roteiro de playtest; duração, diversão e aprendizagem ainda precisam de avaliação com jogadores.

As atividades agora usam documentos e interfaces claras dentro da moldura do jogo: ficha de requisitos com fontes, quadro de planejamento no formato Kanban, agenda de reservas, planilha de gastos com células e central de atendimento com fila, mensagens e histórico. Os textos e controles são nativos do motor, com ações ligadas ao estado da partida; não são imagens de software.

A mochila e o notebook reúnem documentos dos projetos e uma caixa de entrada simulada. Convites, demandas, retornos, acordos e registros de chamados são derivados dos fatos da partida. Não há conta de e-mail nem envio externo. Os acessos do menu, da mochila e do notebook estão integrados. Os testes dirigidos do notebook passaram; a consolidação da suíte final e do pacote ainda precisa ser registrada.

A [procedência da moldura de diálogo](docs/ARTES-UI.md) registra o arquivo, a origem e o recorte usado no motor. O portfólio reúne capturas reais do notebook e dos documentos. Capturas e testes técnicos não substituem o playtest humano.

## Jogar

Para jogar o pacote Windows local, extraia `dist/TheRequirementsWhisperer-1.3-cidade-win.zip` e abra `TheRequirementsWhisperer.exe` na pasta extraída. O pacote inclui o motor; não exige instalar o SDK.

Para executar ou editar o código-fonte:

Use o [SDK oficial Ren'Py 8.5.3](https://www.renpy.org/release/8.5.3) ou uma versão compatível. Este repositório contém diretamente os arquivos do jogo, sem uma pasta `game/` intermediária.

No PowerShell, ajuste os dois caminhos e execute:

```powershell
$sdk = 'C:/caminho/renpy-8.5.3-sdk'
$jogo = 'C:/caminho/Requirements-Whisper'
& "$sdk/lib/py3-windows-x86_64/python.exe" "$sdk/renpy.py" $jogo
```

Para usar um projeto criado pelo launcher, coloque o conteúdo deste repositório na pasta `game/` desse projeto, substituindo os scripts de exemplo.

## Demo guiada preservada

- Preparação interativa com inventário, nome opcional e prévia visual do emblema do perfil. Não é preciso informar idade ou nome real.
- Três contextos: reservas de laboratório, controle de gastos e atendimento de chamados.
- Quatro decisões sobre elicitação, ambiguidade, critérios de aceitação e casos limite, com feedback e revisão orientada.
- Atividade opcional de planejamento: monte uma entrega com dois itens e compare o escopo com a necessidade confirmada.
- Negociação de uma mudança: Carlos quer reduzir consultas manuais; Júlio precisa preservar uma entrega confiável. Escolha entre investigar a integração agora e adiar a entrega, ou entregar a regra primeiro e investigar depois.
- Aplicação final com um pedido novo, produção curta de requisito e critério, revisão do rascunho e autoavaliação guiada. É possível deixar o exercício pendente e retomá-lo no encerramento.
- Notebook com os registros descobertos, acordo e rascunho; encerramento com repetição ou troca de contexto.
- Texto maior, texto instantâneo, controle de transições, histórico e menus com rolagem e foco por teclado.

A pontuação conta somente as quatro escolhas adequadas antes do feedback da primeira missão. Revisões com apoio não somam pontos. Planejamento, negociação e aplicação final não recebem nota. O jogo não avalia automaticamente o significado do texto livre: o rascunho ainda precisa ser discutido com as pessoas envolvidas. Concluir a história não certifica domínio do conteúdo.

## Controles

Use o mouse ou as setas e Enter para escolher. Espaço avança falas; Esc abre o menu; I abre ou fecha o inventário durante a preparação. Na demo guiada, N abre e fecha o notebook durante o estágio; o botão Notebook também permite consultá-lo. Na campanha, mochila, notebook e pastas permitem consultar documentos e mensagens sem abandonar a atividade atual. Durante a digitação do exercício, N funciona como letra e o atalho do notebook fica indisponível. Enter conclui cada campo. Na revisão, use a roda do mouse ou Page Up / Page Down para percorrer o texto e o botão Continuar para avançar.

O botão Histórico permite reler diálogos. Shift+A abre os ajustes nativos de acessibilidade; V solicita leitura em voz alta, conforme as vozes disponíveis no sistema. A leitura por voz e o uso em aparelhos físicos ainda precisam de validação própria.

## Verificar

```powershell
& "$sdk/lib/py3-windows-x86_64/python.exe" "$sdk/renpy.py" $jogo lint
& "$sdk/lib/py3-windows-x86_64/python.exe" "$sdk/renpy.py" $jogo test --savedir 'X:/dev-tmp/Requirements-Whisper/verificacao/saves' --report-detailed
```

Os testes executam o jogo no próprio motor, incluindo três contextos, inventário, revisão, negociação, aplicação final, repetição e persistência. O diretório de saves separado evita misturar testes e partidas pessoais. Para gerar capturas de inspeção:

```powershell
& "$sdk/lib/py3-windows-x86_64/python.exe" "$sdk/renpy.py" $jogo test --savedir 'X:/dev-tmp/Requirements-Whisper/verificacao/saves' --enable-all --overwrite-screenshots --report-detailed
```

As capturas ficam em `tests/screenshots/review/`. A opção de sobrescrita serve à inspeção manual; essas imagens não são baselines de regressão aprovadas automaticamente.

## Gerar o pacote Windows local

Na raiz do repositório, execute:

```powershell
./tools/build-windows.ps1 -SdkPath 'C:/caminho/renpy-8.5.3-sdk'
```

O script prepara um projeto temporário, executa lint e solicita o pacote Windows ao distribuidor do SDK. O ZIP local e seu arquivo SHA256 são gravados em `dist/`. Para escolher outra pasta, use `-OutputDirectory 'C:/caminho/saida'`. O pacote exclui testes, saves, metadados Git e músicas não utilizadas; o diretório temporário é removido ao terminar. A geração não publica o jogo nem envia arquivos a um serviço externo.

Os resultados de validação e as limitações da expansão estão na [revisão completa](docs/REVISAO-COMPLETA.md); a [avaliação anterior](docs/AVALIACAO.md) descreve a demo. A campanha pratica situações de requisitos, produto, implementação e colaboração; não substitui um curso completo de engenharia de software.
