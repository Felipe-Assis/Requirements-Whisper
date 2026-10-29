# The Requirements Whisperer

Jogo educacional em Ren'Py, em português, sobre engenharia de requisitos. Você procura um estágio, conhece Sabrina e Carlos e transforma um pedido vago em regras e critérios que podem ser verificados.

## Jogar

Use o [SDK oficial Ren'Py 8.5.3](https://www.renpy.org/release/8.5.3) ou uma versão compatível. Este repositório contém diretamente os arquivos do jogo, sem uma pasta `game/` intermediária.

No PowerShell, ajuste os dois caminhos e execute:

```powershell
$sdk = 'C:/caminho/renpy-8.5.3-sdk'
$jogo = 'C:/caminho/Requirements-Whisper'
& "$sdk/lib/py3-windows-x86_64/python.exe" "$sdk/renpy.py" $jogo
```

Para usar um projeto criado pelo launcher, coloque o conteúdo deste repositório na pasta `game/` desse projeto, substituindo os scripts de exemplo.

## O que há nesta versão

- Preparação interativa com inventário e perfil opcional. Não é preciso informar idade ou nome real.
- Três contextos: reservas de laboratório, controle de gastos e atendimento de chamados.
- Quatro decisões sobre elicitação, ambiguidade, critérios de aceitação e casos limite.
- Feedback específico, revisão orientada, resumo por competência e repetição da missão.
- Atividade opcional de planejamento: monte uma entrega com dois itens e compare o escopo com a necessidade confirmada.
- Texto maior, texto instantâneo, controle de transições, histórico e menus em português.

A pontuação conta as escolhas adequadas antes do feedback. Uma revisão com apoio permite continuar, mas não soma pontos. Ela é um recurso formativo, não uma certificação de domínio do conteúdo.

## Controles

Use o mouse ou as setas e Enter para escolher. Espaço avança falas; Esc abre o menu; I abre ou fecha o inventário durante a preparação. O botão Histórico permite reler diálogos. Shift+A abre os ajustes nativos de acessibilidade; V solicita leitura em voz alta, conforme as vozes disponíveis no sistema.

## Verificar

```powershell
& "$sdk/lib/py3-windows-x86_64/python.exe" "$sdk/renpy.py" $jogo lint
& "$sdk/lib/py3-windows-x86_64/python.exe" "$sdk/renpy.py" $jogo test --savedir "$jogo/.test-saves" --report-detailed
```

Os testes executam o jogo no próprio motor, com escolhas, inventário, revisão, repetição e persistência. O diretório de saves separado evita misturar testes e partidas pessoais. Capturas opcionais para inspeção visual:

```powershell
& "$sdk/lib/py3-windows-x86_64/python.exe" "$sdk/renpy.py" $jogo test --savedir "$jogo/.test-saves" --enable-all --overwrite-screenshots --report-detailed
```

As capturas ficam em `tests/screenshots/review/`. A opção de sobrescrita serve à inspeção manual; essas imagens não são baselines de regressão aprovadas automaticamente.

Veja a [avaliação e os próximos passos](docs/AVALIACAO.md). O conteúdo ainda é uma primeira missão, não um curso completo de engenharia de software.
