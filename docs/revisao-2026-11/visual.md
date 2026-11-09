# Revisão de interface, arte e viabilidade visual

Revisão de 09/11/2026 da versão 1.1-demo. Foram lidos `DESIGN.md`, README, avaliação anterior, telas, estados e testes. Foram inspecionadas as imagens históricas de menu, diálogo, notebook, planejamento, perfil e preferências compactas em `docs/capturas/`, além de artes de Sabrina, escritório e objetos. **Não houve nova partida, execução de testes, captura do estado atual ou pesquisa com jogadores nesta revisão.** Resultados de motor registrados em `docs/AVALIACAO.md` pertencem à validação anterior. A inspeção estática não certifica acessibilidade, suporte móvel ou diversão.

## Diagnóstico

A base visual é coerente e legível para uma demo educacional. Painéis opacos azul-petróleo, texto claro e verde nas ações funcionam bem com o escritório ilustrado. O maior ganho viria de tornar visíveis a etapa atual, o objetivo imediato, as descobertas e as consequências das decisões.

| Evidência | Constatação | Prioridade |
|---|---|---|
| `scripts/notebook.rpy:67` | `learning_hud` só registra a tecla N. Não desenha HUD nem progresso. O contador 0–6 está dentro do notebook, em `:38`. | Alta para orientação |
| `scripts/backgrounds.rpy:3` | O quarto é uma composição de retângulos, janela e chão; o escritório é arte ilustrada. A abertura tem acabamento inferior ao restante. | Alta para arte |
| `scripts/backgrounds.rpy:12` | A seleção de vagas usa fundo sólido, embora seja uma escolha importante de contexto. | Média |
| `screens.rpy:210` | Planejamento e escolhas de conversa usam o mesmo menu vertical. Opções longas cobrem quase toda a área dos personagens na captura de planejamento. | Média |
| `scripts/characters.rpy:36` e `:42` | Personagens usam posições fixas esquerda/direita, com altura 940. Os retratos funcionam, mas a encenação tem pouca variação. | Média |
| `scripts/characters.rpy:4` | O avatar é um emblema textual com nome. A prévia é clara, mas não há personalização visual do personagem. | Média, se fizer parte da proposta |
| `images/items/notebook_fechado.png` | O selo UFRJ tem letras deformadas no contorno. É um detalhe visível que prejudica o acabamento. | Alta para correção de asset |

A primeira opção cortada em `docs/capturas/planejamento.png` **não é evidência de bug**: a avaliação anterior identifica essa imagem como planejamento após rolagem. O código tem viewport e testes de PgDn. O problema observado é densidade visual e competição com personagens, sobretudo com fonte ampliada.

## Forças a preservar

- Menu principal com ilustração relevante e promessa do jogo em linguagem concreta.
- Diálogo que distingue nome e papel, como “Sabrina · mentora”.
- Notebook com estados escritos “registrado” e “pendente”, descoberta gradual e rolagem (`scripts/notebook.rpy:7` e `:40`).
- Nome opcional, seleção do emblema por escrito e prévia (`scripts/functions.rpy:84`; `scripts/characters.rpy:4`).
- Inventário com estado vazio e descrição do objeto, sem depender apenas da imagem (`scripts/inventory_screen.rpy:22`).
- Cores, tipografia DejaVu e superfícies coerentes entre telas. Não há motivo observado para trocar toda a identidade.

## HUD e mapa vivo

O código já contém estados suficientes para uma primeira versão de orientação: `mission_stage`, `planning_complete`, `negotiation_complete` e `transfer_complete`.

Um HUD discreto pode mostrar “Investigação · critério de aceitação”, “Próximo: confirmar um exemplo com Carlos” e “Registros 2/6”, junto ao botão Notebook. O contador representa registros descobertos, sem sugerir competência ou nota. A ação mais útil precisa continuar acessível em teclado e telas menores, sem disputar a área dos rostos.

Para a demo atual, a primeira versão viável do mapa vivo é um **mapa das descobertas** no notebook: problema → regra → critério → caso limite → acordo → rascunho final. Cada nó abre seu conteúdo e mostra “pendente”, “em conversa” ou “registrado”. O planejamento entra como ramo opcional entre investigação e acordo. Contexto escolhido e resumo do compromisso tornam as consequências consultáveis.

Essa visão pode ser feita com frames, texto, linhas e botões Ren’Py. Não exige biblioteca, animação complexa ou seis ilustrações novas. Planejamento opcional e aplicação pendente não podem ser apresentados como etapas obrigatórias concluídas. Rollback, troca de contexto e save precisam manter o mapa coerente.

Para a expansão em aventura proposta na [síntese](LEIA-ME.md), o mapa espacial tem outra função: uma lista ilustrada de destinos úteis, mostrando objetivo, pessoas presentes e mudanças recentes. Ele deve complementar o mapa das descobertas. A simples mudança entre cenários não comprova avanço; a interface deve derivar novidades de fatos da partida.

## Menus e atividades

- Dar ao planejamento uma tela própria: capacidade 2/2 fixa, candidatos, seleção atual e “Revisar plano”. Montar escopo pede comparação simultânea, além da lista de respostas de uma conversa.
- Na escolha de vagas, mostrar contexto, pessoa interessada e problema inicial em três cartões. O conteúdo já existe no roteiro; não é necessário inventar outro fluxo.
- Oferecer um índice curto do notebook antes dos textos completos. A captura atual mostra apenas dois registros e parte do terceiro.
- Preservar atalhos e ações visíveis. No compacto há uma alternativa de menu rápido em `screens.rpy:1561`, mas aparelho real ainda precisa de verificação.
- Bancadas de evidências e protótipos devem reservar instruções, ação principal, seleção atual e alternativa por teclado antes de acrescentar arrastar e soltar.

## Assets concretos

1. **Quarto ilustrado 1920×1080**, com paleta e tratamento próximos ao escritório, espaço central para controles e janela na posição aproximada da composição atual. Os objetos continuam separados.
2. **Mesa/notebook aberto** para candidatura. Vagas, textos e controles são renderizados pelo motor; evitar letras rasterizadas na ilustração.
3. **Notebook fechado corrigido**, sem o selo deformado. Um decalque simples e legível basta.
4. **Expressões padronizadas para Sabrina, Carlos e Júlio**, com mesma referência de olhos, pés e enquadramento, mantendo roupas e proporções. `sabrina/serious.png` tem 1464×2208, enquanto as demais expressões dela têm 1024×1536. Essa expressão não está declarada em `characters.rpy`; deve ser normalizada antes de integração.
5. **Imagem de encerramento mostrando o resultado do trabalho da equipe**, para dar peso à entrega. Requisito escrito pelo jogador permanece como texto do motor.
6. **Símbolos simples para problema, regra, exemplo, exceção, acordo e rascunho**, produzidos em código ou vetores quando adequado, com rótulos textuais.

Se a expansão do laboratório for escolhida, cenário investigável e estados de antes/depois passam à frente do quarto: a prioridade acompanha o ciclo de jogo validado. Usar o mesmo enquadramento permite trocar camadas de evidência e consequência sem produzir salas inteiras para cada combinação de decisões.

As artes existentes oferecem referência de estilo. `docs/AVALIACAO.md:33` registra que origem e créditos ainda não estão documentados; essa pendência permanece para distribuição externa. Nenhuma arte foi gerada ou alterada nesta subtarefa.

## Acessibilidade e validação

O código oferece texto maior, instantâneo, transições configuráveis, histórico, foco e instruções de teclado (`screens.rpy:1668`). `tests/accessibility.rpy` cobre preferências, escolhas longas, PgDn e seleção após rolagem. A suite visual está desativada por padrão e produz capturas para revisão humana (`tests/visual.rpy:1`); não compara automaticamente com baseline aprovado.

Verificações necessárias na próxima implementação:

- HUD correto antes/depois de cada descoberta, após rollback, salvar/carregar e trocar contexto.
- Mapas acessíveis por teclado, com estados escritos e sem antecipar respostas pendentes.
- Planejamento com 0/1/2 itens, fontes normal/maior e ação final alcançável.
- Notebook com 0/4/6 registros, texto longo e fonte maior.
- Atalhos sem interceptar digitação; a tecla N já recebeu tratamento no exercício.
- Voz PT-BR, ordem de leitura e foco ao fechar modais, em inspeção manual.
- Aparelho pequeno real antes de afirmar suporte móvel: variante compacta no motor não comprova alvos de toque, legibilidade ou interação com teclado virtual.
- Se houver destinos e hotspots, verificar lista acessível equivalente, rótulos, ordem de foco e distinção entre decoração e ação.

Nenhum bloqueador de execução foi confirmado por esta inspeção. Isso não substitui lint, testes no motor ou observação de uso. O maior ganho visual e funcional seria orientar a jornada, permitir comparação no planejamento e alinhar o acabamento dos cenários ao núcleo da experiência escolhido.
