# The Requirements Whisperer

Versão **1.1-demo**. Jogo educacional em Ren'Py, em português, sobre engenharia de requisitos. Você procura um estágio, investiga um pedido com Sabrina e Carlos, negocia uma mudança com Júlio e produz um rascunho de requisito e critério de aceitação.

## Jogar

Para jogar o pacote Windows local, extraia `dist/TheRequirementsWhisperer-1.1-demo-win.zip` e abra `TheRequirementsWhisperer.exe` na pasta extraída. O pacote inclui o motor; não exige instalar o SDK.

Para executar ou editar o código-fonte:

Use o [SDK oficial Ren'Py 8.5.3](https://www.renpy.org/release/8.5.3) ou uma versão compatível. Este repositório contém diretamente os arquivos do jogo, sem uma pasta `game/` intermediária.

No PowerShell, ajuste os dois caminhos e execute:

```powershell
$sdk = 'C:/caminho/renpy-8.5.3-sdk'
$jogo = 'C:/caminho/Requirements-Whisper'
& "$sdk/lib/py3-windows-x86_64/python.exe" "$sdk/renpy.py" $jogo
```

Para usar um projeto criado pelo launcher, coloque o conteúdo deste repositório na pasta `game/` desse projeto, substituindo os scripts de exemplo.

## O que há nesta versão

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

Use o mouse ou as setas e Enter para escolher. Espaço avança falas; Esc abre o menu; I abre ou fecha o inventário durante a preparação. N abre e fecha o notebook durante o estágio; o botão Notebook também permite consultá-lo. Durante a digitação do exercício, N funciona como letra e o atalho do notebook fica indisponível. Enter conclui cada campo. Na revisão, use a roda do mouse ou Page Up / Page Down para percorrer o texto e o botão Continuar para avançar.

O botão Histórico permite reler diálogos. Shift+A abre os ajustes nativos de acessibilidade; V solicita leitura em voz alta, conforme as vozes disponíveis no sistema. A leitura por voz e o uso em aparelhos físicos ainda precisam de validação própria.

## Verificar

```powershell
& "$sdk/lib/py3-windows-x86_64/python.exe" "$sdk/renpy.py" $jogo lint
& "$sdk/lib/py3-windows-x86_64/python.exe" "$sdk/renpy.py" $jogo test --savedir "$jogo/.test-saves" --report-detailed
```

Os testes executam o jogo no próprio motor, incluindo três contextos, inventário, revisão, negociação, aplicação final, repetição e persistência. O diretório de saves separado evita misturar testes e partidas pessoais. Para gerar capturas de inspeção:

```powershell
& "$sdk/lib/py3-windows-x86_64/python.exe" "$sdk/renpy.py" $jogo test --savedir "$jogo/.test-saves" --enable-all --overwrite-screenshots --report-detailed
```

As capturas ficam em `tests/screenshots/review/`. A opção de sobrescrita serve à inspeção manual; essas imagens não são baselines de regressão aprovadas automaticamente.

## Gerar o pacote Windows local

Na raiz do repositório, execute:

```powershell
./tools/build-windows.ps1 -SdkPath 'C:/caminho/renpy-8.5.3-sdk'
```

O script prepara um projeto temporário, executa lint e solicita o pacote Windows ao distribuidor do SDK. O ZIP local e seu arquivo SHA256 são gravados em `dist/`. Para escolher outra pasta, use `-OutputDirectory 'C:/caminho/saida'`. O pacote exclui testes, saves, metadados Git e músicas não utilizadas; o diretório temporário é removido ao terminar. A geração não publica o jogo nem envia arquivos a um serviço externo.

Os resultados de validação e as limitações estão na [avaliação](docs/AVALIACAO.md). A jornada é uma demonstração curta, não um curso completo de engenharia de software.
