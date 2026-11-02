# The Requirements Whisperer

Visual novel educacional (Ren'Py, PT-BR) desenvolvida na disciplina de Projeto de Jogos (UFRJ).
Você é estagiário e passa 8 semanas vivendo o ciclo de vida de um software: requisitos, especificação,
arquitetura, codificação, testes e implantação. As escolhas mexem nas amizades, nos registros do
notebook, nas conquistas e no final.

## Três rotas

A vaga escolhida no início define a empresa, a equipe e a história:

- **Saúde**: sistema web clínico ByeByeFumo, em parceria com uma universidade (22 cenas).
- **Startup**: Trocado, app de controle de gastos para universitários, até o demo day (18 cenas).
- **Corporativo**: Grupo Vértice, manutenção do sistema legado de chamados SGC e o novo módulo Farol (18 cenas).

Em todas as rotas há decisões com feedback e revisão orientada (errar não é punido), planejamento
de entrega, negociação de mudança de escopo, escrita livre de requisito e critério de aceitação com
autoavaliação e um notebook com o que você aprendeu. O resumo final não certifica domínio do conteúdo.

## Como jogar

Requisitos: Ren'Py 8.5.3 (mínimo 8.2+).

1. Clone este repositório.
2. Abra o **Ren'Py Launcher** e adicione a pasta do projeto (a raiz que contém `game/`).
3. Clique em **Launch Project**.

O chat dos colegas da rota Saúde usa um serviço remoto. Os personagens das rotas Startup e
Corporativo respondem com mensagens roteirizadas, sem rede.

## Desenvolvimento

- Lint: `& "<sdk>\lib\py3-windows-x86_64\python.exe" "<sdk>\renpy.py" "<projeto>" lint`
- Testes no motor: `... "<projeto>" test --savedir "<projeto>\.test-saves"`
- Partidas automáticas das três rotas: `powershell -File game/tests/autopiloto.ps1`
- Pacote Windows: `./tools/build-windows.ps1 -SdkPath '<sdk>'` (ZIP e SHA256 em `dist/`)

Detalhes de arquitetura em `CLAUDE.md`; planos e bíblias das rotas em `docs/`.
