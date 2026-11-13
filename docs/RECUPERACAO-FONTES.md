# Fontes recuperáveis do jogo

Verificação em 09/11/2026. A inspeção foi somente de leitura: não abriu o jogo, não executou o SDK, não alterou saves nem os backups. Este documento é o único arquivo criado por esta investigação.

## Resultado

Foi localizado outro checkout com o jogo completo e seu histórico: `C:/Users/Felipe/Documents/GitHub/Renpy Projects/Requirements-Whisper`, branch `main`, commit `d6b9403`. O diretório `game/` está sem alterações locais. Esse é o candidato mais completo para retomar a campanha com mapa, ônibus, metrô, introdução e mochila.

Há ainda fontes anteriores à reescrita de outubro de 2026 nos backups automáticos do Ren'Py e pacotes de 02/11/2026. Não é necessário decompilar `.rpyc` para recuperar essas partes.

As datas abaixo são datas dos arquivos, não uma garantia de lançamento público ou de que cada versão funcionava. Os hashes SHA-256 identificam o conteúdo inspecionado.

## Comparação das fontes

| Fonte | Histórico/versão observada | Conteúdo comprovado | Confiança e uso |
| --- | --- | --- | --- |
| Checkout curto: `C:/Users/Felipe/Documents/GitHub/Requirements-Whisper` | 11 commits alcançáveis; `main` em `c934289`; 18 módulos de jogo `.rpy`, excluindo testes/traduções | Família simplificada de cinco cenas, notebook e laboratório; campanha atual criada a partir dela | Alta para identificar o estado atual; não contém a versão do mapa neste histórico |
| Checkout completo: `C:/Users/Felipe/Documents/GitHub/Renpy Projects/Requirements-Whisper` | 67 commits alcançáveis; `main` em `d6b9403`, de 02/11/2026 20:37:35 −03:00; 134 módulos de jogo `.rpy` | Introdução extensa, três rotas, intermissões, mapa, relógio, energia, inventário e recursos correspondentes | Alta: `git status --porcelain -- game` vazio; melhor base recuperada com histórico. Existem alterações locais fora de `game/`, que devem ser preservadas |
| ZIP `evolucao` no X: | Pacote de 02/11/2026 23:38:40 UTC; 134 fontes | Mesmo conteúdo dos 134 módulos do checkout completo | Alta: 85 arquivos idênticos em bytes e 49 diferindo somente em CRLF/LF; nenhum módulo ausente ou com outro conteúdo |
| ZIP `integracao-rotas` no X: | Pacote de 02/11/2026 15:39:38 UTC; 92 fontes | Campanha com três rotas e a mesma introdução extensa; ainda sem o conjunto do mapa/intermissões | Alta para essa etapa anterior; não substitui a evolução com mapa |
| Backup Ren'Py `Requirements-Whisper` | 757 arquivos de revisões, de 2025 a outubro de 2026 | Introduções e inventários originais, além de revisões posteriores | Alta para recuperar versões específicas identificadas por hash; conjunto de versões, não snapshot único |
| Backups Ren'Py `Requirements-Whisper-evolucao` e `Requirements-Whisper-integracao` | Respectivamente 355 e 301 arquivos de revisões de 02/11/2026 | Etapas intermediárias e confirmação independente de módulos dos ZIPs | Alta para comparação de conteúdo; não escolher tudo pelo maior timestamp |

Os dois checkouts compartilham dois commits, inclusive a raiz `90f4607` de 22/07/2025. Seus históricos locais seguiram caminhos diferentes depois dessa base. O checkout curto não possui os 67 commits da campanha completa: isso explica por que consultar apenas seu Git não revelou o mapa. A conclusão decorre dos históricos disponíveis; não indica quem fez essa separação nem por quê.

A comparação com o pacote não prova que todo o jogo foi jogado e validado agora. Ela prova que as fontes completas continuam disponíveis e que o pacote e o checkout completo preservam o mesmo conteúdo.

## Introdução e mochila anteriores à reescrita

Diretório base: `C:/Users/Felipe/AppData/Roaming/RenPy/backups/Requirements-Whisper/`.

| Fonte, relativa à base | Tamanho | Data do arquivo em UTC | SHA-256 |
| --- | ---: | --- | --- |
| `story/act1_descoberta/scene_1_quarto.2861d4a5740babf7.rpy` | 7.387 B | 2026-06-06 22:34:24 | `c86857b9b1d0ecd2b579886b653a192a9161582174559b3acb1586811309f9c9` |
| `scripts/scene_1_quarto.f81852436d5cfe89.rpy` | 7.408 B | 2025-07-28 01:44:39 | `710c7ced502f9bf1590e41956ffea55bc32228230c123359a4b872b54dfdf21c` |
| `scripts/mechanics/inventory_screen.ec72c0740287adba.rpy` | 2.911 B | 2026-06-06 22:34:24 | `e8c4a54843d066e239653ecc8d694d183aca2bdce48ef680e8376d34a6045934` |
| `data/items.0e10a1e92e442d23.rpy` | 4.512 B | 2026-06-06 22:34:24 | `6abd8be4f19f08318d8f80da3a5d3cc274d43c569781eda3396c64cf42a156b5` |

A introdução de junho tem 170 linhas: alarme; recolhimento do notebook, celular, bloco e caneta; currículo com nome, gênero e idade; escolha das três vagas; tutorial de mochila, contatos e amizade; garrafinha; saída para `scene_2_escritorio`. Linhas 139–144 contêm o tutorial. Isso é evidência direta de conteúdo anterior à alteração de outubro.

O botão da mochila está nas linhas 69–78 do backup `inventory_screen.ec72c0740287adba.rpy`: estado normal `item mochila_idle`, estado de foco `item mochila_aberta_vazia_idle`, ação `ShowMenu("inventory_screen")`, posição `(30, 30)`, tamanho `(120, 120)` e `focus_mask True`. As descrições dos itens usam `hovered` e `unhovered` nas linhas 23–24.

A pasta contém 757 arquivos de backup, incluindo várias versões do mesmo módulo, traduções e revisões de outubro. Não se deve escolher automaticamente o arquivo mais recente sem comparar o conteúdo. Há ainda uma pasta `C:/Users/Felipe/AppData/Roaming/RenPy/backups/The Requirements Whisperer/`, com 14 arquivos de 2025, principalmente a estrutura inicial e módulos vazios. Ela não é a fonte mais completa.

## Pacote com mapa, ônibus e metrô

Arquivo: `X:/dev-tmp/Requirements-Whisper/evolucao/dist/TheRequirementsWhisperer-1.1-win.zip`.

- Tamanho: 304.948.066 bytes.
- Data do arquivo em UTC: 2026-11-02 23:38:40.
- SHA-256: `cc4b41edb1dd7e7bcf10721a45ebd66165fd81bba5bfc695391704a77c57f8de`.
- Prefixo dos módulos no ZIP: `TheRequirementsWhisperer-1.1-win/game/`.
- 134 fontes `.rpy`, somando 1.411.411 bytes, além dos `.rpyc` correspondentes. Fontes do backend não foram inspecionadas.

| Módulo relativo ao prefixo | Tamanho | SHA-256 |
| --- | ---: | --- |
| `script.rpy` | 2.419 B | `aec5d9829817f3ce45ee80c7b4d3e1c65fbb8b868b53d7b92093f8132fee71dc` |
| `story/act1_descoberta/scene_1_quarto.rpy` | 7.539 B | `d23da9227cdf2a1c8ab112a9113844e51cfbd9813f947d7e009341d398396e75` |
| `data/mapa_cidade.rpy` | 9.627 B | `8b423ea6812a0b384a2cbeac71d70dcf3fd95f4c9cfe9084a6cb12d36a8050f5` |
| `scripts/mechanics/mapa_screen.rpy` | 42.678 B | `3673092deee68dad51b8e119bbdfefce9fa804858884eb76f2d2dce464573a85` |
| `scripts/mechanics/inventory_screen.rpy` | 4.914 B | `b262beb071929747d7952d145f57abd8e1bd109d1ca708d1f30eab37afb3f0b1` |
| `data/items.rpy` | 4.512 B | `6abd8be4f19f08318d8f80da3a5d3cc274d43c569781eda3396c64cf42a156b5` |
| `logic/inventory.rpy` | 504 B | `99b7e63d3d5dddc52660d1407cf086848586164128d12d7a6dd25ed43437dd59` |
| `logic/state_flags.rpy` | 4.115 B | `79a6c8818bab82850cfeffc8c308368161dc01cbd8a36b85fa9d9a2da1836510` |
| `ui/styles/vida_transforms.rpy` | 2.703 B | `d9599cdf94d3ceb0f40bca81ac96662f1b80841938c0f87b3f062a661425ce74` |

O pacote também contém `logic/intermissao.rpy`, `logic/energia.rpy`, `scripts/mechanics/intermissao_fluxo.rpy`, dados e cenas das intermissões de saúde, startup e corporativo. O mapa depende desse conjunto, portanto copiar somente a tela não recompõe o fluxo.

Recursos presentes no ZIP:

- `images/mapa/cidade_base.png`, `images/mapa/voce.png`, 12 imagens em `images/mapa/lugares/` e oito ícones em `images/mapa/icones/`.
- `images/bg/transicao_metro.png` (2.404.555 bytes) e `images/bg/transicao_onibus.png` (2.470.825 bytes).
- `images/bg/transito_dia.png`, `transito_manha.png`, `transito_tarde.png` e `transito_noite.png`.
- `images/items/mochila.png`, `mochila_aberta_vazia.png`, `mochila_com_agua.png` e `mochila_com_notebook.png`.

O backup automático confirma dois módulos do mapa byte a byte, em `C:/Users/Felipe/AppData/Roaming/RenPy/backups/Requirements-Whisper-evolucao/`:

- `data/mapa_cidade.dc92a41c5ef8da4e.rpy` tem o mesmo SHA-256 do módulo do ZIP.
- `scripts/mechanics/mapa_screen.0602bf8d44c7a732.rpy` tem o mesmo SHA-256 do módulo do ZIP.

Há versões intermediárias nessa pasta, todas observadas em 02/11/2026. O histórico do checkout completo registra a introdução desses módulos em `a11bd39`, de 02/11/2026 15:59:38 −03:00, e ajustes em `d6b9403`. Não foi encontrada evidência de que esse mapa já existia em 2025 ou junho de 2026. Sua origem comprovada nesta investigação é a evolução de novembro.

Os hashes desta tabela são os bytes do ZIP. No checkout completo, os três módulos `script.rpy`, `data/mapa_cidade.rpy` e `scripts/mechanics/mapa_screen.rpy` têm CRLF; ao normalizar somente `\r\n` para `\n`, seus tamanhos e hashes coincidem com os registrados acima. Essa normalização foi feita em memória, sem alterar arquivos.

## Segundo pacote para comparação

Arquivo: `X:/dev-tmp/Requirements-Whisper/integracao-rotas/dist/TheRequirementsWhisperer-1.1-win.zip`.

- Data do arquivo em UTC: 2026-11-02 15:39:38.
- SHA-256: `1052315c1f0f337e27b64a7efdddac781c6180bb112da9a4572c1ab2d8522797`.
- 92 fontes `.rpy`; todas também existem no pacote `evolucao`, mas 75 têm conteúdo diferente.
- A introdução de 7.539 bytes e `data/items.rpy` são idênticos nos dois pacotes.
- Não contém `data/mapa_cidade.rpy`, `scripts/mechanics/mapa_screen.rpy`, as imagens do mapa nem as transições próprias de ônibus e metrô. O pacote `evolucao` acrescenta 42 módulos, principalmente mapa e intermissões.

Os ZIPs atuais do repositório (`dist/TheRequirementsWhisperer-1.1-demo-win.zip` e `dist/TheRequirementsWhisperer-1.2-campanha-win.zip`) contêm a família simplificada de 15 e 18 fontes `.rpy`, respectivamente. Eles não recuperam o mapa de novembro.

## Histórico Git e outros candidatos

O histórico do checkout curto possui 11 commits alcançáveis. `7c194a4` versiona recursos visuais e áudio, mas não os roteiros. `dee2fa5` já inclui a família de roteiros reescrita. Portanto, voltar somente a um commit desse checkout não recupera os roteiros originais. O checkout completo contém o histórico que faltava à primeira investigação.

Não há stash. `git fsck --full --no-reflogs --unreachable` encontrou um commit anterior ao amend, duas árvores e três blobs. Os blobs não vazios são um registro de revisão de novembro e um teste de notebook; não são as fontes originais. Nenhum objeto foi recuperado, removido ou alterado.

`X:/dev-tmp/Requirements-Whisper/evolucao/backup-migracao/` contém capturas e um patch de outro conjunto de ferramentas; os cabeçalhos do patch não correspondem aos roteiros do jogo. Essa pasta foi preservada. Os `.rpyc` ignorados do checkout e dos pacotes observados acompanham fontes `.rpy`; não foi necessário executar desserialização ou decompilação.

## Como recuperar sem substituir o trabalho atual

1. Preserve os backups e confira o SHA-256 antes de usá-los. Leia os módulos com `pathlib` ou `zipfile` sem executar seu conteúdo.
2. Antes de mudar a base do trabalho, confirme a escolha do usuário entre continuar a campanha atual e retomar a campanha completa. Preserve as alterações locais de ambos os checkouts. Compare o roteiro de junho, a versão do checkout completo/ZIP de novembro e o checkout atual: o backup de junho mostra a introdução antiga; o checkout completo permite retomar sua evolução com histórico.
3. Extraia somente arquivos selecionados para uma pasta de comparação no X:. Não use `extractall` sobre o checkout nem copie saves, backend ou configurações indiscriminadamente.
4. Reaproveite o botão e os estados de imagem da mochila com suas dependências. Para mapa e transporte, reconcilie dados, fluxo das intermissões, relógio/energia, telas, imagens e destinos antes de conectar a navegação atual.
5. Registre separadamente o que foi restaurado de uma fonte histórica e o que precisou ser adaptado para a campanha atual. A existência dos arquivos comprova recuperabilidade; execução e compatibilidade precisam de validação própria.
