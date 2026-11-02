# Intermissões da rota Saúde: conteúdo

Data: 2026-11-02. Branch `evolucao`. Etapa E1 (design de conteúdo, rota Saúde).
Segue `docs/design/sistemas-intermissoes.md` (aqui chamado **Sistemas**) em formatos, nomes, custos e regras. Este
documento não altera nenhum `.rpy`. Quem implementa é a E5 (conteúdo) e a E6 (ambiguidade e rastreabilidade).

Escopo do usuário: jogo educacional que serve para aula e para jogar sozinho, completo do início ao fim. Estilo de
arte C. Live2D fora.

---

## 0. Resumo e ajustes registrados

**O que este documento entrega para a Saúde:** 7 locais com descrição para a arte do mapa, as 8 intermissões
(gancho, horário, agenda, ações, pistas, extras), os fios de conversa de cada personagem, o arco de mentoria "Um dia
de ambulatório", os dados completos da caça à ambiguidade (`scene_10`) e da rastreabilidade (`scene_17`, bug na
`scene_19`), os efeitos de energia, as mudanças exatas em cada cena e a estimativa de palavras e minutos.

**Ajustes em relação ao Sistemas (com motivo):**

| # | Ajuste | Motivo |
|---|---|---|
| A1 | 7 locais, não 5 ou 6 | O Sistemas §2.1 fixa 5 locais desde a semana 1 e 2 que abrem depois (ambulatório na S2, servidores na S6). Mantido. |
| A2 | Rótulo do dia na S1: "Primeiro dia" (não "Sexta") | A `scene_4` diz "Parabéns pelo seu primeiro dia" e "Amanhã começamos a preparar as entrevistas". O horário (16h–18h) fica. |
| A3 | Rótulos de dia S6–S8: "Dia da codificação", "Dia dos testes", "Último dia" | Na `scene_18` a semana pode terminar na mesma noite ou na manhã seguinte (`scene_18_2`); nomear o dia da semana criaria contradição. A `scene_21` já diz "O último dia começa". |
| A4 | Na ambiguidade, o trecho clicável é "de forma rápida" (não só "rápida") e a reescrita de "sempre que necessário" ganhou outra ordem | Para que a troca pela reescrita adequada deixe a frase gramatical. O conteúdo é o mesmo do Sistemas §5.1 (mesmo pedido da escrita livre da `scene_12`). |
| A5 | A pista `saude_p_papeis` entra no menu da tarde da `scene_19` ("Enfrenta dificuldade para corrigir uma falha crítica"), não no ramo "Validação de permissões" | O laço da manhã escolhe 4 de 8 testes; o ramo de permissões pode não acontecer. O menu da tarde sempre acontece e vem logo depois da revelação da falha de acesso (seção 7.4). |
| A6 | Depois do gancho B da S6 a cena redesenha fundo e música | Na `scene_18`, as falas que vêm depois do gancho não têm `scene`; ficariam sobre o fundo do último local visitado. Ver 10.1. |
| A7 | Conversas em "fios": o label genérico `im_saude_conversar_<cid>` despacha para a próxima conversa da série | São 74 presenças na agenda; escrever uma conversa por pessoa por semana daria 13 mil palavras. Com fios de 3 conversas por pessoa e conversas próprias só onde a semana importa, o jogador nunca vê a mesma conversa duas vezes nas primeiras 3 visitas. Usa a convenção do Sistemas §1.6 sem mudar o motor. |
| A8 | Proposta para E4: `im_abertura(N)` chama `im_<rota>_abertura_<N>` quando existir | O Sistemas §1.5 define o tutorial da S1 com falas da guia, mas não diz onde a rota escreve as aberturas. A convenção segue o §1.6. |

Nada aqui muda `final_saude`, a conta da `scene_21`, `registrar`, `decisao` nem as conquistas da rota.

---

## 1. Locais (POI) da rota Saúde

### 1.1 Lista

Ids, nomes, fundos e semana de abertura iguais ao Sistemas §2.1.

| id | Nome | Fundo da ação | Abre | Ações do local | `pos` (imagem 1920x1080) |
|---|---|---|---|---|---|
| `mesa` | Mesa da equipe | `escritorio_interior_tarde` | 1 | — | (760, 270) |
| `sala_reunioes` | Sala de reuniões | `sala_reunioes_tarde` | 1 | estudar | (430, 250) |
| `cafe` | Café | `empresa_cafe_tarde` | 1 | descansar | (450, 470) |
| `refeitorio` | Refeitório | `refeitorio_tarde` | 1 | — | (780, 520) |
| `praca` | Praça em frente | `empresa_exterior_manha` | 1 | descansar | (1150, 640) |
| `ambulatorio` | Ambulatório do Instituto | `escritorio_medica` | 2 (depois da entrevista) | observar | (1560, 380) |
| `servidores` | Sala de servidores | `sala_servidores` | 6 | — | (600, 760) |

Estado escrito no mapa antes de abrir: ambulatório "Abre na semana 2"; servidores "Abre na semana 6".
O ambulatório fica no Instituto, do outro lado da praça: os 90 min de observar e de mentoria já incluem o trajeto.

### 1.2 Arte do mapa (E3)

**Uso nos dois formatos.** Se a E3 seguir o mapa único da cidade (plano de evolução, "Mapa da cidade"), estes
sprites ficam no bairro do campus. Se seguir o mapa por rota (Sistemas §2.3, `images/mapas/saude.png`), eles
compõem a imagem da rota. As posições acima valem para o segundo caso.

**Base do polo Saúde (`images/mapas/saude.png` ou recorte do mapa da cidade).** Estilo C dos fundos: paleta suave e
levemente dessaturada, leve textura de papel, linhas limpas, perspectiva precisa, luz de tarde vinda da esquerda,
sombras curtas e contidas, sem texto legível. Vista de cima em 3/4, leve. À esquerda, o prédio da equipe; no centro, uma
praça; à direita, o Instituto. Ao fundo, morros verdes e um pedaço da baía com uma ponte ao longe; ruas com faixa de
ônibus e um ponto coberto. Palmeiras-imperiais ao longo da calçada. Sem pessoas em primeiro plano; figurantes só ao
longe, de costas.

**Prédio da equipe em corte.** Um prédio de vidro azul-esverdeado e concreto claro, como em `empresa_exterior_manha`,
desenhado como casa de bonecas: a fachada que olha para o jogador foi retirada e mostra três andares e o subsolo.
Cada sala é um sprite recortado próprio, para poder "saltar" ao focar.

| Local | Descrição visual do sprite | Ícone (64 px, contorno escuro com leve textura de lápis, preenchimento suave, legível em 32 px) |
|---|---|---|
| `mesa` | 3º andar, à direita. Sala aberta com quatro mesas de madeira clara em L, monitores com gráficos abstratos azuis, cadeiras azul-marinho, estante escura com fichários, quadro de cortiça com papéis sem texto, cafeteira sobre um gaveteiro. Janelas grandes com luz de fim de tarde laranja-rosada (mesma família de `escritorio_interior_tarde`). | Monitor de frente com uma caneca ao lado direito. |
| `sala_reunioes` | 3º andar, à esquerda. Mesa oval clara com seis cadeiras, quadro branco com caixas e setas rabiscadas (sem letras), post-its amarelos e verdes, projetor no teto, uma planta num canto. | Quadro branco com dois post-its colados. |
| `cafe` | 2º andar. Copa com balcão de madeira e três banquetas redondas, armários cinza-azulados, cafeteira de vidro, quatro xícaras brancas, micro-ondas, poltrona marrom no canto, janela com o pôr do sol (como `empresa_cafe_tarde`). | Xícara com três fios de vapor. |
| `refeitorio` | Térreo. Mesas com toalha creme, cadeiras de madeira com assento vermelho, luminárias pendentes em cúpula, balcão de madeira ao fundo com prateleiras de potes e garrafas de suco, tapete vermelho desbotado, uma planta grande (como `refeitorio_tarde`). | Bandeja com prato, garfo e faca. |
| `servidores` | Subsolo, visível por uma faixa de corte no chão. Corredor estreito de racks azul-escuros com luzes verdes e azuis, piso elevado perfurado, duas máquinas de ar-condicionado ao fundo, mesa dobrável com notebook e copo de café (como `sala_servidores`). Antes da S6, o sprite aparece com a porta fechada e mais escuro. | Rack de servidor com três luzes em fila. |

**Praça e Instituto.**

| Local | Descrição visual do sprite | Ícone |
|---|---|---|
| `praca` | Praça pequena entre o prédio e o Instituto: calçada de pedras portuguesas em ondas pretas e brancas, três palmeiras-imperiais, dois bancos de madeira, um bebedouro, canteiro com flores baixas, um bem-te-vi num galho. Sombra das palmeiras no chão. | Banco de praça sob uma palmeira. |
| `ambulatorio` | Ala de dois andares do Instituto, fachada creme com janelas azul-esverdeadas e entrada lateral com toldo verde-água; uma placa com um ícone de folha e pulmão no lugar de texto. Uma janela grande em corte mostra a sala das médicas como em `escritorio_medica`: estantes de madeira com pastas, duas mesas com papéis espalhados, quadros com caduceu e coração, planta, cortina creme. Ao lado, a sala de espera com cadeiras azuis e um balcão de recepção. Sem cruz vermelha e sem a palavra "HOSPITAL". | Prancheta com um estetoscópio por cima. |

Os 7 ícones têm silhuetas diferentes entre si, para que a ação e o local não dependam de cor (Sistemas §2.5).
Observação para a E3: `empresa_exterior_manha` (fundo da praça) ainda está em pintura pastel e destoa do estilo C; o
plano de evolução já o lista para regerar.

---

## 2. As 8 intermissões

Legenda das ações (custos do Sistemas §1.2): conversar 30 min, 0 energia, amizade +0,5 · observar 90 min, −1, pista
de uso (se houver) e +0,5 com quem é observado · estudar 60 min, −1, registro extra · descansar 60 min, +2 · ajudar
90 min, −2, +1,0 e pista técnica (se houver) · mentoria 90 min, −1, +1,0 com a Dra. Nathalia e um passo do arco.
Teto de amizade: +1,0 por pessoa e +2,0 por intermissão.

"Fio" = próxima conversa da série da pessoa (seção 3). Metas de tamanho: conversar 8–14 falas (~170 palavras),
observar e ajudar 15–25 falas (~350), estudar 6–10 (~150), mentoria 20–30 (~470), descansar 3–6 (~70).

Aberturas: label `im_saude_abertura_<N>` (A8). Cada uma tem 1–2 falas e, se `energia_cansaco()`, uma fala a mais.

### S1 · Primeiro dia, 16h–18h · 120 min (tutorial)

- **Gancho A** em `game/script.rpy`, entre `call scene_3_reuniao_inicial from _scene_3_reuniao_inicial` e
  `call scene_4_retorno_casa from _scene_4_retorno_casa`: `call im_intermissao(1) from _im_saude_s1`.
- `mesmo_dia: False` (faz `set_time(16, 0)`). Ajuste do Sistemas: `scene_4` troca `$ advance_minutes(150)` por
  `$ advance_minutes(50)`.
- **Abertura (tutorial, Emily, 6 falas)**:
  1. "Hoje ninguém vai te passar tarefa até as seis. Primeiro dia é para conhecer a casa."
  2. "Esse é o mapa do prédio e do campus. Em cada lugar aparece quem está lá e o que dá para fazer."
  3. "Cada coisa custa tempo: conversar, meia hora; estudar, uma hora. Não cabe tudo, e tudo bem. Escolher é deixar
     algo para outro dia."
  4. "Fica de olho na sua energia, embaixo do relógio. Ajudar alguém cansa; descansar recupera."
  5. "Às vezes você vai ver um detalhe que vira pista e ajuda numa decisão lá na frente."
  6. "E o mais importante: nada aqui é obrigatório para aprender. O que o projeto precisa, a gente faz junto no
     expediente. Esse tempo é seu."

| Local | Quem | Ações | Conteúdo |
|---|---|---|---|
| mesa | Emily, Joseph | conversar Emily, conversar Joseph | fio 1 de cada |
| sala_reunioes | Robert | **estudar** `saude_extra_glossario`; conversar Robert | `im_saude_s1_estudar_sala_reunioes`: o Robert mostra a página "Glossário" do wiki, com três termos e dois anos sem mudança. Você completa com o que ouviu na reunião: carga tabágica, escala HAD, retorno, histórico de saúde. Robert: "Se você mantiver isso vivo, vira a página mais lida do wiki." (~150) |
| cafe | Lucas, César | descansar; conversar Lucas, César | `im_saude_descansar_cafe` (seção 3.4) |
| refeitorio | Daiana, Heitor | conversar Daiana, Heitor | fio 1 |
| praca | Mateus | descansar; conversar Mateus | `im_saude_descansar_praca` |
| ambulatorio | — | "Abre na semana 2" | — |
| servidores | — | "Abre na semana 6" | — |

Sem ajudar, sem observar, sem pistas. Exemplo de uso: duas conversas e estudar (120 min).

### S2 · Sexta (dia da entrevista), 16h–19h · 180 min

- **Gancho A** em `script.rpy`, entre `call scene_8_cafe_informal from _scene_8_cafe_informal` e
  `call scene_9_retorno_casa_sem2 from _scene_9_retorno_casa_sem2`: `call im_intermissao(2) from _im_saude_s2`.
- `mesmo_dia: True`.
- **Abertura:** narrador: "Fim da tarde do dia da entrevista. Antes de você sair do Instituto, a [NOME_DOUTORA_2]
  disse que o ambulatório fica aberto até as sete, se você quiser ver a rotina de perto." (O ambulatório aparece
  aceso no mapa pela primeira vez.)

| Local | Quem | Ações | Conteúdo |
|---|---|---|---|
| mesa | **Joseph**, Mateus | **ajudar Joseph** (sem pista); conversar Joseph, Mateus | `im_saude_s2_ajudar_developer_coding` "O README": Joseph está montando o repositório no GitLab (lint, modelo de commit). Você escreve a seção "Como rodar". Ele devolve: "'Rode o projeto' não é instrução. Qual comando? Em qual pasta? O que aparece quando dá certo?" Você reescreve com passos e resultado esperado e percebe que é a mesma lição da entrevista: o que não dá para conferir não está pronto. (~350) |
| sala_reunioes | Robert, Heitor | **estudar** `saude_extra_fluxos`; conversar Robert, Heitor | `im_saude_s2_estudar_sala_reunioes`: Heitor desenha num canto do quadro um caminho principal e dois desvios. "Um desvio ainda chega lá. O outro não chega, e o sistema tem que dizer o que fazer." (~150) |
| cafe | Emily | descansar; conversar Emily | fio |
| refeitorio | Daiana, César | conversar Daiana, César | fio |
| praca | Lucas | descansar; conversar Lucas | fio |
| ambulatorio | Nathalia ★, Michelle | **observar** (`saude_p_cpf`); mentoria; conversar Nathalia, Michelle | observar: `im_saude_s2_observar_ambulatorio`. Mentoria: `im_saude_mentoria_1` (seção 5). Michelle: `im_saude_s2_conversar_doutora_1` (seção 3.3) |
| servidores | — | "Abre na semana 6" | — |

**Observar S2 "A recepção às quatro" (~350, +0,5 Nathalia, pista `saude_p_cpf`):** você se senta perto do balcão da
recepção. A recepcionista Sônia (sem sprite) cadastra quem chega. Um paciente chega sem documento; Sônia anota o
nome num papel com "cadastrar depois" e prende com um clipe no monitor. Há três papéis assim. A [NOME_DOUTORA_2]
passa e comenta: "Esses papéis somem. Aí o paciente volta e é como se fosse a primeira vez." Fecho do narrador: "Na
entrevista, ninguém falou desses papéis. Eles só aparecem para quem fica olhando."

Pistas desta semana: `saude_p_cpf` (observar) e `saude_p_had` (mentoria 1). As duas valem só até a S2. Fazer
observar e mentoria ocupa os 180 min no ambulatório; a amizade com a Nathalia para em +1,0 (o aviso diz isso).

### S3 · Sexta, 15h–18h · 180 min

- **Gancho A** em `script.rpy`, entre `call scene_12_especificacao_requisitos from _scene_12_especificacao_requisitos`
  e `call scene_13_retorno_casa_sem3 from _scene_13_retorno_casa_sem3`: `call im_intermissao(3) from _im_saude_s3`.
- `mesmo_dia: False` (`set_time(15, 0)`). A especificação foi no dia anterior.
- **Abertura:** "Sexta. A especificação foi revisada ontem à noite, e a tarde de hoje está mais leve." Cansaço:
  "Ontem você saiu tarde. O corpo lembra."

| Local | Quem | Ações | Conteúdo |
|---|---|---|---|
| mesa | Daiana, Lucas | conversar Daiana, Lucas | fio |
| sala_reunioes | Emily, **Robert** | **ajudar Robert** (sem pista); **estudar** `saude_extra_acoplamento`; conversar Emily, Robert | ajudar: `im_saude_s3_ajudar_developer_management`. estudar: `im_saude_s3_estudar_sala_reunioes` |
| cafe | Joseph, César | descansar; conversar Joseph, César | fio |
| refeitorio | Heitor, Mateus | conversar Heitor, Mateus | fio |
| praca | ninguém | descansar | `im_saude_descansar_praca` |
| ambulatorio | Nathalia ★ | **observar** (`saude_p_autosave`); mentoria; conversar Nathalia | `im_saude_s3_observar_ambulatorio` |

**Ajudar Robert S3 "Do caso de uso ao cartão" (~350, +1,0 Robert):** vocês passam o UC1 e o UC5 para o quadro do
Trello. O cartão "Fazer o cadastro" é grande demais; Robert pergunta como dividir. Você propõe um cartão por fluxo:
principal, alternativo (paciente sem CPF), exceção (conexão cai). Robert: "Cartão que ninguém consegue terminar numa
semana é só uma preocupação com nome bonito." Fecho: ele avisa que na semana que vem vão estimar esses cartões juntos.

**Estudar S3 (~150):** Emily mostra a mensagem do Heitor da `scene_10` ("separar a persistência da lógica de
negócios") e pergunta por quê. Você lê sobre coesão e acoplamento e responde com o exemplo das escalas: o cálculo da
HAD não deveria saber em que tabela a resposta está guardada.

**Observar S3 "O formulário que sumiu" (~350, +0,5 Nathalia, pista `saude_p_autosave`):** com a permissão do
paciente, você assiste do canto a uma consulta. A [NOME_DOUTORA_2] digita rápido e só clica em Salvar no fim. A ala
antiga tem Wi-Fi fraco; a rede cai, a tela recarrega e o formulário volta em branco. Ela respira fundo e refaz as
perguntas com o paciente esperando. Depois, baixinho: "Viu? É disso que eu falava." Você anota sem nome do paciente
("paciente A"), e ela aprova: "Boa. Nome de paciente não sai daqui."

### S4 · Sexta, 12h–15h (almoço estendido) · 180 min

- **Gancho A** em `script.rpy`, entre `call scene_14_discussao_arquitetura from _scene_14_discussao_arquitetura` e
  `call scene_15_aniversario_surpresa from _scene_15_aniversario_surpresa`: `call im_intermissao(4) from _im_saude_s4`.
- `mesmo_dia: False` (`set_time(12, 0)`). Ajuste do Sistemas: na `scene_15`, `"{i}Já no dia seguinte...{/i}"` vira
  `"{i}Depois do almoço...{/i}"`.
- **Abertura:** "Sexta. O [NOME_DEVELOPER_MANAGEMENT] liberou um almoço estendido até as três: a reunião de
  arquitetura de ontem rendeu." Cansaço: "Ainda dá para sentir a reunião de ontem até as sete."

| Local | Quem | Ações | Conteúdo |
|---|---|---|---|
| mesa | Mateus (não sabe da festa) | conversar Mateus | `im_saude_s4_conversar_developer_security` (abaixo) |
| sala_reunioes | Robert, Heitor | **estudar** `saude_extra_estimativa`; conversar Robert, Heitor | `im_saude_s4_estudar_sala_reunioes`: Robert e Heitor discutem quanto vale o cartão do autosave; um diz 3, o outro 8. Você lê sobre planning poker e entende que a diferença é a conversa: Heitor via o risco da conexão cair no meio da gravação. (~150) |
| cafe | Emily, Daiana | descansar; conversar Emily, Daiana | fio |
| refeitorio | Joseph, **César**, Lucas | **ajudar César** (sem pista); conversar Joseph, César, Lucas | `im_saude_s4_ajudar_developer_test` (abaixo) |
| praca | ninguém | descansar | — |
| ambulatorio | Nathalia ★, Michelle | **observar** (`saude_p_autosave`); mentoria; conversar Nathalia, Michelle | `im_saude_s4_observar_ambulatorio`; Michelle: `im_saude_s4_conversar_doutora_1` |

**Conversar Mateus S4 "Um dia comum" (~200, +0,5 Mateus):** Mateus almoça na mesa, marmita e o bonsai ao lado. Diz
que hoje é "um dia comum". O celular vibra; ele vira a tela para baixo rápido, mas você leu: "Parabéns, filho. Vem
jantar?". Ele muda de assunto para o log de acesso. Você não comenta. (Retorno na `scene_15`, seção 10.)

**Ajudar César S4 "A massa de testes da HAD" (~350, +1,0 César):** num guardanapo, vocês montam os casos de teste do
cálculo da HAD: cada subescala vai de 0 a 21; faixas 0–7, 8–10 e 11–21. César: "Onde testar?" Você aponta as bordas: 7
e 8, 10 e 11, 0 e 21; e os inválidos: 22, número negativo, resposta faltando. César: "Teste bom não confirma que
funciona. Procura onde não funciona." Fecha com ele guardando o guardanapo no bolso "para virar código hoje".

**Observar S4 "Papel de garantia" (~350, +0,5 Michelle, pista `saude_p_autosave` se ainda não tem):** a
[NOME_DOUTORA_1] preenche a escala de um paciente no sistema antigo e, ao mesmo tempo, num formulário de papel.
"Já perdi tanta coisa que agora faço duas vezes." A rede cai na metade; o sistema perde, o papel fica. À noite ela vai
digitar tudo de novo. Se o jogador já tem a pista (S3), o conteúdo roda igual e o fecho muda: "É a segunda vez que
você vê a mesma perda, com outra médica. Já não é azar: é padrão."

### S5 · Sexta, 16h–19h · 180 min

- **Gancho B** em `game/story/act4_arquitetura/scene_17_tarde_estudos_tecnicos.rpy`, logo depois de
  `"Você salva suas anotações, fecha o notebook e sente que tem base para os desafios dos próximos dias."` e antes
  de `$ set_available('all')`: `call im_intermissao(5) from _im_saude_s5`.
- `mesmo_dia: True`. Antes do gancho, a cena já tem o quadro de rastreabilidade (seção 7).
- **Abertura:** "A tarde de estudos rendeu. Ainda falta um pedaço do expediente, e ninguém está cobrando nada."

| Local | Quem | Ações | Conteúdo |
|---|---|---|---|
| mesa | **Joseph** (`saude_p_memoria`), César | **ajudar Joseph**; conversar Joseph, César | `im_saude_ajudar_developer_coding` (abaixo; vale para S5 e S6) |
| sala_reunioes | Robert, Emily | **estudar** `saude_extra_revisao`; conversar Robert, Emily | `im_saude_s5_estudar_sala_reunioes`: Emily te pede para revisar o PR de um colega de outra equipe. Você lê o roteiro do wiki e comenta o comportamento antes do estilo. (~150) |
| cafe | Lucas | descansar; conversar Lucas | fio |
| refeitorio | Daiana, Heitor | conversar Daiana, Heitor | fio |
| praca | **Mateus** (`saude_p_papeis`) | **ajudar Mateus**; descansar; conversar Mateus | `im_saude_s5_ajudar_developer_security` (abaixo) |
| ambulatorio | Nathalia ★ | observar (só cena); mentoria; conversar Nathalia | `im_saude_s5_observar_ambulatorio` |

**Ajudar Joseph "O servidor que melhora de manhã" (`im_saude_ajudar_developer_coding`, ~350, +1,0 Joseph, pista
`saude_p_memoria`):** Joseph reclama que o servidor de testes é rápido de manhã e lento à tarde. Vocês olham juntos
e você acha uma rotina agendada que reinicia o servidor às 3h, criada anos atrás "para limpar". Joseph: "Então
qualquer coisa que cresce devagar nunca passa de um dia." Ele anota para depois do deploy; agora o módulo de cadastro é
a prioridade. Variação S6 (`im_semana_atual == 6`): a primeira fala vira "Hoje, com todo mundo subindo código, ele
está pior ainda."

**Ajudar Mateus S5 "A médica em dois lugares" (`im_saude_s5_ajudar_developer_security`, ~350, +1,0 Mateus, pista
`saude_p_papeis`):** Mateus caminha na praça para pensar e pede ajuda com algo que viu no log de acesso do sistema
antigo (ele descreve de memória, sem nome de paciente): às 7h02 a [NOME_DOUTORA_2] abriu a agenda na recepção; às
7h05 ela estava num plantão em outro prédio. Você junta as peças: alguém usa a senha dela. Mateus, devagar: "Senha
emprestada não é maldade. É sinal de que o perfil de alguém não deixa trabalhar." Se o jogador já tem a pista
(mentoria 3), o fecho muda: "Você já tinha visto isso de perto, então. Agora tem o log também."

**Observar S5 "A fila da tarde" (só cena, ~350, +0,5 Nathalia):** a recepção decide a ordem de atendimento por um
cartão plastificado: gestantes, recaída na última semana, primeira consulta, retorno. Nathalia: "Critério escrito é
para ninguém decidir no humor do dia." Fecho: você lembra do plano da manhã (`scene_16`): duas vagas, critério antes da
vontade.

### S6 · Dia da codificação, 16h30–19h30 · 180 min

- **Gancho B** em `game/story/act5_implementacao/scene_18_codificacao_implementacao.rpy`, depois de
  `hide tela_ui_final` / `pause 0.7` e antes do comentário `# Decisão: se não finalizou no escritório, ramifica...`:
  `call im_intermissao(6) from _im_saude_s6`, seguido de `scene bg escritorio_interior_noite` com `dissolve` e
  `play music music_office_relaxed fadein 1.0` (A6).
- `mesmo_dia: True`. A sala de servidores abre nesta semana.
- **Abertura:** se `finalizou_no_escritorio`: "O módulo está entregue para o [NOME_DEVELOPER_TEST] testar. Até o fim
  do expediente, o tempo é seu." Se não: "O módulo não fechou, e o [NOME_DEVELOPER_TEST] está rodando a bateria de
  testes, que vai até o fim do dia. Nada a fazer nele agora; o resto você decide depois."

| Local | Quem | Ações | Conteúdo |
|---|---|---|---|
| mesa | **Joseph** (`saude_p_memoria`), Lucas | **ajudar Joseph**; conversar Joseph, Lucas | `im_saude_ajudar_developer_coding` (variação S6) |
| sala_reunioes | Heitor | **estudar** `saude_extra_piramide`; conversar Heitor | `im_saude_s6_estudar_sala_reunioes`: Heitor desenha um triângulo no quadro e não diz nada; você completa as camadas e ele só acena. (~150) |
| cafe | Emily, Daiana | descansar; conversar Emily, Daiana | fio |
| refeitorio | Robert | conversar Robert | fio |
| praca | César | descansar; conversar César | fio |
| ambulatorio | Nathalia ★ | observar (só cena); mentoria; conversar Nathalia | `im_saude_s6_observar_ambulatorio` |
| servidores | **Mateus** (`saude_p_backup`) | **ajudar Mateus**; conversar Mateus | `im_saude_ajudar_developer_security` (abaixo; vale para S6 e S7) |

**Ajudar Mateus "O backup verde" (`im_saude_ajudar_developer_security`, ~350, +1,0 Mateus, pista `saude_p_backup`):**
Mateus arruma a sala para o servidor novo. O painel mostra a rotina de backup verde todos os dias há dois anos. Você
pergunta quando foi a última restauração. Ele procura no wiki e não acha. "Backup que nunca foi restaurado é um
arquivo que a gente torce para estar certo." Ele anota para "depois do deploy". Variação S7: ele já está mais
cansado e a frase final é "Semana que vem, sem falta."

**Observar S6 "Erro 0x80004005" (só cena, ~350, +0,5 Nathalia):** o sistema antigo mostra "Erro 0x80004005" e um
botão OK. Nathalia não sabe se salvou, liga para a TI e espera dez minutos com o paciente na sala. Fecho: você anota
que uma mensagem de erro é requisito: dizer o que aconteceu, se algo se perdeu e o que fazer agora.

### S7 · Dia dos testes, 15h30–18h30 · 180 min

- **Gancho B** em `game/story/act5_implementacao/scene_19_testes_seguranca.rpy`, depois do menu
  "Enfrenta dificuldade para corrigir uma falha crítica. O que faz?" e da linha de energia (seção 8), antes de
  `# Fechamento: Reflexão e estatísticas`: `call im_intermissao(7) from _im_saude_s7`, seguido de
  `play music music_office_relaxed fadein 1.0` (a linha seguinte da cena já faz `scene`).
- `mesmo_dia: True`. Se o jogador virou a noite na `scene_18`, o bloco perde 60 min de hora extra.
- **Abertura:** "Os bugs do dia estão anotados e as correções, divididas. Até o fim do expediente, o tempo é seu."
  Se `im_hora_extra` foi descontado: "A noite em claro da semana passada ainda cobra: hoje o tempo livre é mais
  curto."

| Local | Quem | Ações | Conteúdo |
|---|---|---|---|
| mesa | **César** (`saude_p_memoria`), Daiana | **ajudar César**; conversar César, Daiana | `im_saude_s7_ajudar_developer_test` (abaixo) |
| sala_reunioes | Robert, Heitor | **estudar** `saude_extra_rollback`; conversar Robert, Heitor | `im_saude_s7_estudar_sala_reunioes`: Robert pergunta "se der errado amanhã, quem decide voltar, e em quanto tempo?". Ninguém sabe. Você escreve o rascunho do plano. (~150) |
| cafe | Joseph | descansar; conversar Joseph | fio |
| refeitorio | Lucas, Emily | conversar Lucas, Emily | fio |
| praca | ninguém | descansar | — |
| ambulatorio | Nathalia ★, Michelle | observar (só cena); mentoria; conversar Nathalia, Michelle | `im_saude_s7_observar_ambulatorio`; Michelle: `im_saude_s7_conversar_doutora_1` |
| servidores | **Mateus** (`saude_p_backup`) | **ajudar Mateus**; conversar Mateus | `im_saude_ajudar_developer_security` (variação S7) |

**Ajudar César S7 "O teste das 3h" (`im_saude_s7_ajudar_developer_test`, ~350, +1,0 César, pista
`saude_p_memoria`):** César quer um teste de resistência de 48 horas no cadastro, mas o teste morre sempre às 3h.
Vocês acham a rotina de reinício. César: "Então a gente nunca testou o sistema por mais de um dia." Desligar a rotina
depende da infraestrutura; fica pedido para a semana do deploy. Se já tem a pista (S5/S6), o fecho muda: "É a mesma
rotina que o [NOME_DEVELOPER_CODING] achou. Ninguém desligou."

**Observar S7 "A planilha da pesquisa" (só cena, ~350, +0,5 Michelle):** a [NOME_DOUTORA_1] prepara a planilha da
pesquisa apagando à mão a coluna de nomes. Ficam a coluna de telefone e um campo "observações" onde aparece "Seu
Ivo". Você comenta com cuidado; ela agradece e conta que nunca ninguém explicou o que "anonimizar" quer dizer na
prática. Fecho: a pergunta da manhã (exportar com ou sem identificação) agora tem rosto.

### S8 · Último dia, 9h30–12h30 · 180 min

- **Gancho B** em `game/story/act5_implementacao/scene_21_avaliacao_final.rpy`, depois de
  `"Você confere os slides, o protótipo rodando e revisa as anotações no notebook."` e antes de
  `# Transição: trajeto até o instituto`: `call im_intermissao(8) from _im_saude_s8`, seguido de
  `play music music_home_reflecting fadein 1.0` (a linha seguinte já faz `scene bg transito_tarde`).
- `mesmo_dia: True`. Sem estudar (os extras vão da S1 à S7). Sem pistas (nenhuma cena depois usaria).
- **Abertura:** Robert: "A apresentação está pronta. Até o almoço, cada um faz o que precisa." Cansaço: "E quem
  estiver no limite: hoje não precisa provar nada."

| Local | Quem | Ações | Conteúdo |
|---|---|---|---|
| mesa | Emily, Robert | conversar Emily, Robert | Emily: `im_saude_s8_conversar_developer_requirements` (abaixo); Robert: fio |
| sala_reunioes | Heitor, Daiana | conversar Heitor, Daiana | fio |
| cafe | Lucas, Joseph | descansar; conversar Lucas, Joseph | fio |
| refeitorio | ninguém | — | "Ninguém agora" |
| praca | César | descansar; conversar César | fio |
| ambulatorio | Nathalia ★ | observar (só cena); mentoria (última chance); conversar Nathalia | `im_saude_s8_observar_ambulatorio` |
| servidores | Mateus | conversar Mateus | fio |

**Conversar Emily S8 "O caderno" (~250, +0,5 Emily):** Emily pergunta o que você leva destas oito semanas. Menu
`(tipo="conversa")` com três respostas (ouvir casos reais / escrever o que dá para conferir / não fazer nada sozinho),
cada uma com uma resposta dela, sem efeito além da fala. No fim ela te dá um caderno pequeno: "Anota do jeito que a
pessoa falou. Resumo você faz depois." Não vira item; é só fala.

**Observar S8 "O sistema novo no ambulatório" (só cena, ~350, +0,5 Nathalia):** a [NOME_DOUTORA_2] usa o ByeByeFumo
com um paciente de verdade. No canto da tela, "Salvo às 10:42". A HAD avisa "Faltam 2 respostas"; ela sorri. Um
atrito: o botão Cancelar fica colado no Salvar e ela quase clica errado. Você anota para a avaliação da tarde (é a
mesma sugestão que aparece na `scene_21`). Fecho: "Na primeira semana você ouviu como deveria ser. Hoje viu como é."

---

## 3. Conteúdo reutilizável

### 3.1 Despacho dos fios (A7)

O label genérico de cada pessoa chama a próxima conversa da série. Funções de conteúdo ficam no arquivo de dados da
rota (`game/data/intermissoes/saude.rpy`), sem estado novo: elas só leem `im_feitas`.

```python
init 3 python:
    def saude_im_fez(semana, acao, alvo=None, poi=None):
        """True se a ação foi feita na intermissão da semana (rota saúde)."""
        sem = store.im_feitas.get("saude", {}).get(semana, {})
        for p, a, t in sem.get("acoes", []):
            if a == acao and (alvo is None or t == alvo) and (poi is None or p == poi):
                return True
        return False

    def saude_conversas(cid):
        """Quantas conversas já terminadas com cid em todas as intermissões."""
        total = 0
        for sem in store.im_feitas.get("saude", {}).values():
            total += sum(1 for p, a, t in sem.get("acoes", []) if a == "conversar" and t == cid)
        return total

    def saude_fio(cid):
        """Label da próxima conversa: fio 1..3, depois o papo rápido."""
        n = saude_conversas(cid) + 1
        if n <= 3 and renpy.has_label("im_saude_fio_%s_%d" % (cid, n)):
            return "im_saude_fio_%s_%d" % (cid, n)
        return "im_saude_papo_%s" % cid
```

```renpy
label im_saude_conversar_developer_coding:
    call expression saude_fio("developer_coding")
    return
```

Um label assim por pessoa (8 developers e `doutora_2`). A Dra. Michelle só aparece na S2, S4 e S7 e tem conversas
próprias por semana (3.3). Como `im_executar` grava em `im_feitas` depois do conteúdo, a contagem durante a conversa é
a das anteriores.

**Papo rápido** (`im_saude_papo_<cid>`, 3–4 falas, ~60 palavras): a pessoa comenta a semana em uma frase (o tema vem
do cartão da semana), e o jogador responde com uma fala fixa. Uma variante por semana par/ímpar.

### 3.2 Fios dos developers (3 conversas cada, ~170 palavras, 8–12 falas)

Os fios não dependem da semana e não citam eventos futuros. Cada um pode ter um menu curto `(tipo="conversa")` sem
efeito além da fala.

| Pessoa | Fio | Resumo | Fala-chave |
|---|---|---|---|
| Emily `developer_requirements` | 1 O caderno de frases | Ela anota as frases dos usuários palavra por palavra, porque a paráfrase perde a dor. Mostra uma: "eu perdi tudo". | "Eu anoto do jeito que a pessoa falou. Resumo eu faço depois." |
| | 2 Antes dos requisitos | Trabalhou três anos num suporte por telefone e aprendeu a perguntar "o que você estava tentando fazer?". | "Quem liga para o suporte nunca diz o requisito. Diz o que deu errado." |
| | 3 Dizer não com cuidado | Como ela recusa pedidos: mostrando a troca, nunca só "não dá". | "'Não dá' fecha a conversa. 'Se entrar isso, sai aquilo' abre." |
| Lucas `developer_ai` | 1 O modelo de recaída | Ele quer prever recaídas com IA. Você pergunta de onde viriam os dados; ele percebe que precisa de consentimento e de dados que ainda não existem. | "Sem dado bom, IA só erra mais rápido." |
| | 2 IA e palavra vaga | Testou um assistente para revisar requisitos; ele aprovou "o sistema deve ser rápido". | "Ela concorda com tudo. Parece eu no primeiro mês." |
| | 3 O hackathon | Conta do hackathon do fim de semana: o time da Daiana ganhou de novo. | "Eles ensaiaram a apresentação. A gente ensaiou o código." |
| Joseph `developer_coding` | 1 Risoto e revisão | Risoto pede atenção contínua; revisão de código pede pedaços pequenos. | "Ninguém revisa duas mil linhas. Revisa vinte, com atenção." |
| | 2 A sexta-feira | O deploy de sexta à noite que derrubou o sistema de uma farmácia o fim de semana todo. | "Desde então, sexta à noite eu só faço risoto." |
| | 3 Por que eu sou chato | Perdeu um estagiário por criticar sem explicar; hoje explica o motivo de cada comentário. | "Crítica sem motivo é só barulho. Eu aprendi tarde." |
| Robert `developer_management` | 1 Gerente aos 28 | Fala da insegurança de gerenciar gente mais experiente; decide perguntando. | "Eu não sei mais que eles. Eu só sei quem sabe o quê." |
| | 2 O quadro | Explica o limite de dois cartões "Fazendo" por pessoa. | "Se tudo está em andamento, nada está pronto." |
| | 3 O guarda-chuva | Segura a pressão da diretoria do Instituto para o time não sentir. | "Prazo apertado eu negocio. Gente esgotada eu não consigo consertar." |
| Daiana `developer_quality` | 1 Professora | Foi professora de matemática antes de QA; checklist é o jeito dela de ensinar. | "Checklist é aula para quem está com pressa." |
| | 2 O pudim | Conta o melhor bug para ganhar o pudim: um sistema aceitou 30 de fevereiro por dois anos. | "Ninguém tinha escrito que não podia." |
| | 3 Qualidade não é fase | Por que ela entra nas reuniões desde a entrevista. | "Qualidade não é a última etapa. É o jeito de fazer todas." |
| Heitor `developer_project` | 1 O guardanapo | Desenha o modelo de dados num guardanapo, quase sem falar. | "Paciente tem muitos atendimentos. Atendimento tem um paciente. O resto é detalhe." |
| | 2 Versionar o histórico | Por que prontuário não se sobrescreve: cada mudança é uma versão nova. | "Em prontuário, apagar é mentir sobre o passado." |
| | 3 Falar pouco | Jogava xadrez; pensa antes de mexer. | "Cada palavra que eu digo numa reunião vira tarefa de alguém." |
| Mateus `developer_security` | 1 Devagar | Fala devagar porque, em incidente, pressa destrói evidência. | "Em incidente, quem corre apaga a prova." |
| | 2 O bonsai | Cuida de um bonsai na mesa; compara poda com permissão mínima. | "Permissão é igual galho: se ninguém poda, cresce para onde não devia." |
| | 3 A planilha no e-mail | Num emprego antigo, uma planilha de pacientes foi para o e-mail errado. | "Do outro lado de cada linha tem alguém que confiou na gente." |
| César `developer_test` | 1 Corrida | Corre toda manhã e pensa nos testes correndo. | "Correndo eu penso: e se o usuário fizer o contrário?" |
| | 2 A base apagada | O dia em que apagou a base de testes achando que era produção (a história do café, `scene_8`), contado pelo lado do susto. | "Hoje produção tem fundo vermelho no meu terminal. Aprendi do pior jeito." |
| | 3 Quem quebra | Por que gosta de dados absurdos: idade 200, CPF com letras. | "Usuário não lê manual. Usuário aperta tudo." |

### 3.3 Fios das médicas

| Pessoa | Label | Resumo | Fala-chave |
|---|---|---|---|
| Nathalia `doutora_2` | fio 1 Por que o tabagismo | O avô parou de fumar sete vezes; a última deu certo porque alguém acompanhou. | "Parar de fumar é a coisa mais difícil que eu já vi alguém tentar." |
| | fio 2 O café do plantão | O plantão de 24 horas, o café, e por que pediu notificações. | "No plantão eu esqueço até de almoçar. O sistema não pode depender da minha memória." |
| | fio 3 A tela verdinha | Ela volta à piada da tela verde e fala sério: um colega é daltônico; alerta só em vermelho ele não vê. | "Se o aviso for só cor, o Dr. Paulo não vê. Escreve o que é." |
| Michelle `doutora_1` | `im_saude_s2_conversar_doutora_1` | Os dois dias conferindo fichas de papel por causa de um dado alterado sem registro. | "Não quero saber quem errou. Quero saber o que mudou, quando e de onde veio." |
| | `im_saude_s4_conversar_doutora_1` | O pedido do Adeus Cigarro, ontem. Lê `s14_acordo_escopo`: `"base_primeiro"` → "Fiquei chateada, mas o autosave é mais urgente mesmo."; `"investigar_agora"` → "Obrigada por não prometer o que ninguém sabia se dava." | "Prefiro ouvir 'ainda não sei' a ouvir 'sim' e esperar um ano." |
| | `im_saude_s7_conversar_doutora_1` | Ela vai apresentar o sistema às colegas do Instituto e pede que você explique em uma frase o que mudou. | "Se eu não consigo explicar em uma frase, as minhas colegas não vão usar." |

Depois do fio 3 da Nathalia, o papo rápido. A amizade com as médicas não entra no final (soma só os 8 developers).

### 3.4 Descansar (`im_saude_descansar_cafe` e `im_saude_descansar_praca`, ~70 palavras)

- **Café:** café passado, a janela com o fim de tarde, o barulho da cafeteira. Se `energia_cansaco()`: "Você quase
  cochila na banqueta. Alguém deixa uma xícara do seu lado e não diz nada."
- **Praça:** banco à sombra da palmeira, vento, um bem-te-vi. Se `energia_cansaco()`: "Você fecha os olhos por dez
  minutos e acorda com o celular vibrando no bolso. Era só o grupo da equipe mandando meme."
- Na S4 a praça e o café ficam cheios do almoço: uma fala a mais sobre o movimento.

---

## 4. Pistas: onde nascem e onde são usadas

### 4.1 Dados

| id | Título | Texto (o que o jogador viu) | Onde ganha | Até | Uso |
|---|---|---|---|---|---|
| `saude_p_cpf` | O paciente sem CPF | "Na recepção do ambulatório, um paciente chegou sem documento. A recepcionista anotou o nome num papel para cadastrar depois, e a ficha ficou sem CPF." | S2 observar ambulatório | 2 | Semana 3: um fluxo alternativo do cadastro. |
| `saude_p_had` | A escala pela metade | "Na triagem, um paciente pulou duas perguntas da escala HAD no papel. A Dra. Nathalia não conseguiu fechar o escore e escreveu 'incompleta' na margem." | S2 mentoria 1 | 2 | Semana 3: a inspeção do requisito da HAD. |
| `saude_p_autosave` | O formulário que sumiu | "No ambulatório, a internet caiu no meio de uma consulta e o formulário quase pronto se perdeu. A médica refez as perguntas com o paciente esperando." | S3 ou S4 observar ambulatório | 4 | Semana 5: o plano da primeira entrega. |
| `saude_p_papeis` | A senha emprestada | "A recepção entra no sistema com a senha da Dra. Nathalia, porque o perfil da recepção não abre a agenda. Tudo o que a recepção faz fica registrado como se fosse a médica." | S4+ mentoria 3 ou S5 ajudar Mateus | 6 | Semana 7: a revisão de papéis de acesso. |
| `saude_p_memoria` | O servidor que reinicia | "O servidor de testes é reiniciado toda madrugada por uma rotina automática. Nenhum teste roda mais de um dia seguido." | S5–S6 ajudar Joseph, S7 ajudar César | 7 | Semana 8: o bug crítico antes do deploy. |
| `saude_p_backup` | O backup nunca restaurado | "A rotina de backup aparece verde todo dia há dois anos, mas ninguém nunca tentou restaurar uma cópia." | S6–S7 ajudar Mateus | 7 | Semana 8: o checklist de deploy. |

Os textos descrevem o que foi visto, não a resposta do menu.

### 4.2 Usos exatos

**`saude_p_cpf` — formato 2.** `game/story/act3_especificacao/scene_10_criacao_casos_uso.rpy`, label
`scene_10_criacao_casos_uso`, menu "Durante a pausa, sobre o que você quer conversar com
[NOME_DEVELOPER_REQUIREMENTS]?". As três opções atuais ficam; o menu ganha `(tipo="conversa")` e uma quarta opção:

```renpy
        "Contar o que vi na recepção do ambulatório: um paciente sem CPF, anotado num papel" (tipo="pista") if pista_tem("saude_p_cpf"):
            $ pista_usar("saude_p_cpf")
            show developer_requirements serious at left_zoom
            developer_requirements "Num papel? Então o paciente existe para a recepção e não existe para o sistema. Foi esse buraco que eu já vi travar um cadastro inteiro."
            developer_requirements "Vamos escrever agora: fluxo alternativo do UC1, paciente sem documento. Cadastro provisório com nome, data de nascimento e nome da mãe; o CPF fica pendente e o sistema lembra na próxima visita."
            "{i}O UC1 ganha o fluxo alternativo FA1, com o passo onde começa e como termina. Ao lado, você anota a origem: observação na recepção.{/i}"
            $ add_friendship_point("developer_requirements", 0.5)
```

**`saude_p_had` — formato 1.** `scene_12_especificacao_requisitos.rpy`, label `scene_12_especificacao_requisitos`:
depois de `developer_requirements "Está claro? O que pode faltar aqui?"` e antes do `menu:` com
`"1 de 4 · Qual problema pesa mais neste requisito?"`:

```renpy
    call pista_lembrar("saude_p_had") from _pl_s12_had
```

**`saude_p_autosave` — formato 1.** `game/story/act4_arquitetura/scene_16_reuniao_gerenciamento.rpy`, label
`scene_16_reuniao_gerenciamento`: depois de `developer_management "[player_name], monte o plano. Quais itens entram?"`
e antes de `call atividade_planejamento("saude_plano", ...)`:

```renpy
    call pista_lembrar("saude_p_autosave") from _pl_s16_plano
```

**`saude_p_papeis` — formato 2 (A5).** `scene_19_testes_seguranca.rpy`, label `scene_19_testes_seguranca`, menu
"Enfrenta dificuldade para corrigir uma falha crítica. O que faz?" (vem logo depois do bloco da rastreabilidade, 7.4).
Opções atuais ficam; o menu ganha `(tipo="trabalho")` e uma quarta opção:

```renpy
        "Contar ao [NOME_DEVELOPER_SECURITY] o que você viu: a recepção entra com a senha da médica" (tipo="pista") if pista_tem("saude_p_papeis"):
            $ pista_usar("saude_p_papeis")
            show developer_security thinking at right_zoom
            if rast_lacuna_achada("saude_rast_acesso"):
                developer_security "O teste garante que o perfil recepção não abre o histórico. Mas, se a recepção entra com a senha da doutora, o teste passa e o problema continua."
            else:
                developer_security "Então corrigir o perfil não basta. Se a recepção continuar com a senha da doutora, o histórico abre para a pessoa errada e a trilha registra a médica."
            developer_security "A correção tem duas partes: um login para cada pessoa da recepção, com agenda e cadastro, e uma conversa com a [NOME_DOUTORA_2] sobre senha emprestada."
            "{i}Vocês escrevem juntos a mensagem para a [NOME_DOUTORA_2]: sem culpa, com o motivo. A correção passa a cobrir a causa, não só o sintoma.{/i}"
            $ add_friendship_point("developer_security", 0.5)
            hide developer_security
```

**`saude_p_backup` — formato 2.** `game/story/act5_implementacao/scene_20_deploy_final.rpy`, label
`scene_20_deploy_final`, menu "Backup do banco e dos arquivos realizado?". Opções atuais ficam; nova opção:

```renpy
        "Contar o que você viu na sala de servidores: ninguém nunca restaurou esse backup. Pedir um teste de restauração antes" (tipo="pista") if pista_tem("saude_p_backup"):
            $ pista_usar("saude_p_backup")
            show developer_security serious at right_zoom
            developer_security "Eu tinha deixado isso para depois do deploy. Depois seria tarde."
            "{i}Em vinte minutos, [NOME_DEVELOPER_PROJECT] e [NOME_DEVELOPER_SECURITY] restauram a cópia em homologação. O banco volta inteiro, mas a pasta dos exames digitalizados não estava no backup.{/i}"
            show developer_project serious at left_zoom
            developer_project "Se o servidor caísse amanhã, os exames anexados sumiam. Incluí a pasta e agendei um teste de restauração por mês."
            $ add_friendship_point("developer_security", 0.5)
            hide developer_security
            hide developer_project
```

**`saude_p_memoria` — formato 2.** Mesmo arquivo, menu "Como você resolve o bug crítico?". Opções atuais ficam;
nova opção:

```renpy
        "Contar o que você viu: o servidor de testes reinicia toda madrugada, e nenhum teste rodou mais de um dia" (tipo="pista") if pista_tem("saude_p_memoria"):
            $ pista_usar("saude_p_memoria")
            show developer_coding serious at left_zoom
            developer_coding "Então tem algo crescendo devagar, e o reinício escondia. Vazamento de memória."
            show developer_test enthusiastic at right_zoom
            developer_test "Perfil de memória na listagem de pacientes... achei. Cada busca guarda a lista inteira num cache que nunca é limpo."
            "{i}A correção leva vinte minutos. O servidor de testes deixa de reiniciar de madrugada e ganha um alerta de memória.{/i}"
            hide developer_coding
            hide developer_test
            "{i}Você ganhou o selo 'Bug Crítico Resolvido' no inventário.{/i}"
            $ inventario.append("badge_bug_buster")
```

O selo é o mesmo da primeira opção atual (que também acha o vazamento), então o caminho sem pista chega ao mesmo
fim. A opção é um atalho na história, não uma conquista nova.

---

## 5. Mentoria: "Um dia de ambulatório" (Dra. Nathalia)

Arco opcional sobre ouvir quem usa o sistema. Os encontros acontecem no ambulatório, com a permissão de cada paciente,
e o jogador aprende a anotar sem identificar ninguém. Pacientes e a recepcionista não têm sprite: falam por
`Character` simples definidos no arquivo de dados (`saude_npc_recepcao` "Sônia", `saude_npc_ivo` "Seu Ivo",
`saude_npc_celia` "Dona Célia"), fora de `FALA_TAGS`.

| k | Label | Semana mín. | Título | O que acontece (resumo) | O que se aprende | Pista |
|---|---|---|---|---|---|---|
| 1 | `im_saude_mentoria_1` | 2 | Triagem e escala no papel | Nathalia faz a triagem de um paciente novo: Fagerström e HAD no papel. Ele pula duas perguntas da HAD ("me sinto lento", "perdi o interesse pela aparência"), por vergonha. Ela não insiste e escreve "incompleta". | Observar o trabalho real mostra o que a entrevista não conta: o usuário pula, hesita, contorna. Anotar sem nome. | `saude_p_had` (só na S2) |
| 2 | `im_saude_mentoria_2` | 3 | O retorno de um paciente | Seu Ivo, terceiro retorno, recaiu depois de um enterro. Nathalia folheia três fichas para comparar cigarros por dia e o estágio de motivação. Ela não julga. | A necessidade real é "ver o que mudou desde a última consulta", não "um gráfico". E o maior risco é o paciente que some (liga com o aviso de falta da `scene_12`). | — |
| 3 | `im_saude_mentoria_3` | 4 | Quem vê o quê | Ela leva você pelo caminho do prontuário: recepção (agenda, cadastro), enfermagem (sinais vitais), médica (histórico), pesquisa (dados sem identificação). Na recepção, Sônia entra com a senha da Nathalia: "o meu perfil não abre a agenda". Nathalia, sem graça: "Eu sei, eu sei." | Papéis de acesso nascem do trabalho de cada um; um contorno é sinal de requisito mal atendido; mínimo necessário (LGPD). | `saude_p_papeis` (até a S6) |
| 4 | `im_saude_mentoria_4` | 5 | A consulta de 15 minutos | Com permissão, você cronometra uma consulta: 15 min, dos quais 6 olhando a tela e digitando, de costas para o paciente. | Usabilidade em número: tempo de tarefa, medido antes e depois. Liga com a reescrita "um retorno em até 3 minutos" da `scene_10`. | — |
| 5 | `im_saude_mentoria_5` | 6 | A paciente testa o protótipo | Dona Célia, 62 anos, aceita responder a HAD no protótipo clicável do César, num tablet na sala de espera. Ela pensa em voz alta; você não pode ajudar. A letra é pequena e ela não acha o "Próximo". Pula uma pergunta e a tela diz "Faltam 2 respostas. Você pode voltar ou salvar e continuar depois"; ela sorri. | Teste de usabilidade com usuário real: tarefa clara, pensar em voz alta, não ajudar, anotar onde trava. Achados: fonte maior, botão fixo embaixo. | — |

Falas-chave (Nathalia): 1 "Na entrevista eu te contei como deveria ser. Aqui você vê como é." · 2 "Recaída não é
fracasso, é dado. O sistema precisa me mostrar a história, não só a última foto." · 3 "Ninguém aqui quer burlar
nada. A senha emprestada é o jeito que a gente achou de trabalhar." · 4 "Cada minuto que eu olho a tela é um minuto
que eu não olho para ele." · 5 (Dona Célia) "Se até eu consegui, qualquer um consegue." e (Nathalia, conclusão)
"Agora você sabe olhar um ambulatório."

Variações: no encontro 4, se `energia_cansaco()`: "Você está com cara de fim de plantão. Senta aí; hoje você só
cronometra." No encontro 5 na S8, o sistema já está no ar: "protótipo" vira "a versão nova no tablet".

Tamanho: 20–30 falas por encontro (~470 palavras).

**Dados:**

```python
ROUTES["saude"]["mentoria"] = {
    "id": "saude_mentoria_ambulatorio",
    "titulo": _("Um dia de ambulatório"),
    "mentor": "doutora_2",
    "passos": [
        {"n": 1, "semana_min": 2, "pista": "saude_p_had",    "resumo": _("Triagem e escala no papel")},
        {"n": 2, "semana_min": 3, "pista": None,             "resumo": _("O retorno de um paciente")},
        {"n": 3, "semana_min": 4, "pista": "saude_p_papeis", "resumo": _("Quem vê o quê")},
        {"n": 4, "semana_min": 5, "pista": None,             "resumo": _("A consulta de 15 minutos")},
        {"n": 5, "semana_min": 6, "pista": None,             "resumo": _("A paciente testa o protótipo")},
    ],
}
ROUTES["saude"]["conquistas_extra"] = [
    {"id": "mentoria_conq_saude", "var": "mentoria_conq_saude",
     "title": _("Olhar de Ambulatório"),
     "desc": _("Concluiu os cinco encontros com a Dra. Nathalia.")},
]
```

**Conquista:** `mentoria_conq_saude` "Olhar de Ambulatório", concedida por `mentoria_avancar()` no 5º encontro
(`mentoria_passos["saude"] == 5`). Não entra em `route_achievements()` nem em `final_saude()`.

**Retorno na `scene_21`** (só fala, nada muda na nota): depois de
`doutora_2 "Eu senti que nossas opiniões foram levadas a sério. Isso faz a gente se sentir parte do projeto também!"`:

```renpy
    if mentoria_conq_saude:
        doutora_2 "E a Dona Célia, que testou a escala no tablet, perguntou de você. Disse que agora responde sozinha, com a letra grande."
    elif mentoria_passos.get("saude", 0) >= 2:
        doutora_2 "E obrigada pelas tardes no ambulatório, [player_name]. Deu para ver que você entendeu a nossa rotina."
```

---

## 6. Caça à ambiguidade (`scene_10`, semana 3)

**Onde:** `scene_10_criacao_casos_uso.rpy`, label `scene_10_criacao_casos_uso`, depois de
`developer_requirements "Bom dia, [player_name]! Que tal começarmos pelos fluxos mais comuns do usuário? ..."` e do
`$ advance_minutes(3)` seguinte, antes de `"{i}Você senta ao lado de [NOME_DEVELOPER_REQUIREMENTS] e abre o notebook..."`.

```renpy
    developer_requirements "Antes, olha esse rascunho que saiu das anotações da entrevista. Se o caso de uso nascer de palavra vaga, ele herda o problema."
    call amb_atividade("saude_amb_historico") from _amb_s10
    show developer_requirements positive at left_zoom
    developer_requirements "Agora dá para testar cada pedaço. E os 3 minutos são uma proposta nossa: a gente confirma com a [NOME_DOUTORA_2] antes de fechar."
    $ advance_minutes(7)
```

**Dados:**

```python
ROUTES["saude"]["ambiguidades"] = {
    "saude_amb_historico": {
        "contexto": _("Rascunho de requisito montado a partir das anotações da entrevista com as médicas."),
        "segmentos": [
            _("O sistema deve permitir que a médica registre o "),
            ("isca", "historico", _("histórico")),
            _(" do paciente "),
            ("vaga", "rapida", _("de forma rápida")),
            _(" e "),
            ("vaga", "simples", _("simples")),
            _(", e emitir "),
            ("isca", "alertas", _("alertas")),
            _(" "),
            ("vaga", "necessario", _("sempre que necessário")),
            _("."),
        ],
        "iscas": {
            "historico": _("'Histórico de saúde' está definido no UC2: tratamentos em andamento, medicamentos, gravidez, comorbidades. A equipe sabe o que entra."),
            "alertas": _("'Alerta' já tem forma combinada com as médicas: um aviso na tela inicial de quem acompanha o caso. O vago aqui é quando ele aparece, não o que ele é."),
        },
        "vagas": {
            "rapida": {
                "porque": _("Rápida para quem? Num plantão cheio, 'rápido' muda de sentido. Sem número, o teste não passa nem falha."),
                "opcoes": [
                    {"texto": _("com a tela abrindo em até 2 s e um retorno sem mudanças registrado em até 3 minutos"), "adequada": True},
                    {"texto": _("o mais rápido possível"), "adequada": False,
                     "feedback": _("Continua sem número. Cada pessoa da equipe para num ponto diferente, e o teste não tem como passar ou falhar.")},
                    {"texto": _("mais rápido que no sistema atual"), "adequada": False,
                     "feedback": _("Ninguém mediu o sistema atual. Sem a medida de antes, a comparação vira opinião na hora da entrega.")},
                ],
            },
            "simples": {
                "porque": _("'Simples' é opinião. A Dra. Nathalia já disse o que atrapalha; é isso que precisa estar escrito."),
                "opcoes": [
                    {"texto": _("com os campos obrigatórios marcados antes de salvar e os dados da visita anterior já preenchidos"), "adequada": True},
                    {"texto": _("com uma interface intuitiva e amigável"), "adequada": False,
                     "feedback": _("Troca uma palavra vaga por duas. Ainda não dá para conferir nada.")},
                    {"texto": _("com no máximo uma tela e poucos campos"), "adequada": False,
                     "feedback": _("Isso já é solução, e pode cortar campos que o atendimento exige, como as escalas. O problema dela não era o número de telas.")},
                ],
            },
            "necessario": {
                "porque": _("Necessário segundo quem? Sem dizer o evento e quem recebe, o sistema avisa de tudo ou de nada."),
                "opcoes": [
                    {"texto": _("para a profissional que acompanha o caso, no mesmo dia em que o paciente faltar à consulta de retorno"), "adequada": True},
                    {"texto": _("a cada alteração no prontuário"), "adequada": False,
                     "feedback": _("Seriam dezenas de avisos por plantão. Aviso demais vira ruído, e a médica passa a ignorar até o importante.")},
                    {"texto": _("quando a médica achar importante"), "adequada": False,
                     "feedback": _("Devolve a decisão para a médica em cada caso. O sistema continua sem saber quando avisar.")},
                ],
            },
        },
    },
}
```

Resultado esperado (o jogo monta): "O sistema deve permitir que a médica registre o histórico do paciente **[com a
tela abrindo em até 2 s e um retorno sem mudanças registrado em até 3 minutos]** e **[com os campos obrigatórios
marcados antes de salvar e os dados da visita anterior já preenchidos]**, e emitir alertas **[para a profissional
que acompanha o caso, no mesmo dia em que o paciente faltar à consulta de retorno]**."

Coerência com a rota: os 2 s vêm do DR01 (`scene_12`); campos obrigatórios e dados da visita anterior são a resposta
da Nathalia sobre "prático" (`scene_6`); o aviso de falta é o pedido da escrita livre da `scene_12`. Decisões
registradas: `saude_amb_historico_marcar`, `saude_amb_historico_rapida`, `saude_amb_historico_simples`,
`saude_amb_historico_necessario` (só a primeira tentativa, Sistemas §5.1).

**Fala nova na `scene_12`** (não muda menu nem decisão): depois de
`developer_requirements "Pedido novo, e chegou na hora certa. Que tal você escrever esse? ..."`:

```renpy
    if amb_resultados.get("saude_amb_historico", {}).get("concluido"):
        developer_requirements "É o alerta que a gente destrinchou na caça à ambiguidade. Agora ela contou o motivo. Escreve inteiro, com critério."
```

---

## 7. Rastreabilidade (`scene_17`, semana 5) e o bug (`scene_19`, semana 7)

### 7.1 Onde entra

`scene_17_tarde_estudos_tecnicos.rpy`, label `scene_17_tarde_estudos_tecnicos`, depois de
`developer_test "Se quiser revisar algum teste, me chama! Nada como aprender praticando."` e antes de `hide developer_test`:

```renpy
    developer_test "Aliás, já que você está aqui: monta comigo o quadro de rastreabilidade da primeira entrega? Cada critério ligado ao requisito de onde veio e ao teste que cobre."
    call rast_atividade("saude_rast_acesso") from _rast_s17
    if rast_lacuna_achada("saude_rast_acesso"):
        developer_test "C3 sem teste... bem visto. Escrevo hoje: teste_recepcao_nao_abre_historico. Entra na pipeline amanhã."
    else:
        developer_test "Quadro conferido. Semana que vem essa bateria roda inteira na pipeline."
```

A fala do "else" não revela a lacuna (Sistemas §5.2).

### 7.2 Dados

Os requisitos e critérios vêm da primeira entrega combinada na `scene_16` (autosave e HAD) e da segurança da
`scene_6`/`scene_14` (quem alterou, LGPD).

```python
ROUTES["saude"]["rastreabilidade"] = {
    "saude_rast_acesso": {
        "requisitos": [
            {"id": "R1", "texto": _("RF02: O sistema salva o histórico de saúde durante o preenchimento e recupera o rascunho se a conexão cair.")},
            {"id": "R2", "texto": _("RF05A: O sistema calcula os escores da escala HAD e, quando falta resposta, avisa e salva o preenchimento parcial.")},
            {"id": "R3", "texto": _("SEG01: Cada perfil vê só o que precisa: a recepção cuida de agenda e cadastro; o histórico de saúde é da equipe clínica. Toda alteração no histórico registra quem, quando e o valor anterior.")},
        ],
        "criterios": [
            {"id": "C1", "de": "R1", "teste": "T1", "texto": _("Dado um histórico com três campos preenchidos, quando a conexão cai e volta, então os três campos continuam lá.")},
            {"id": "C2", "de": "R2", "teste": "T2", "texto": _("Dadas as 14 respostas da HAD, quando a médica conclui, então o sistema mostra os escores de ansiedade e de depressão, de 0 a 21 cada.")},
            {"id": "C3", "de": "R3", "teste": None, "texto": _("Dado o perfil recepção, quando abre o histórico de saúde de um paciente, então o acesso é negado.")},
            {"id": "C4", "de": "R2", "teste": "T3", "texto": _("Dadas 12 das 14 respostas, quando a médica tenta concluir, então o sistema mostra quais faltam e salva como parcial.")},
            {"id": "C5", "de": "R3", "teste": "T4", "texto": _("Dada uma médica que altera a carga tabágica, então a trilha registra quem alterou, a hora e o valor anterior.")},
        ],
        "testes": [
            {"id": "T1", "texto": _("teste_autosave_queda_conexao")},
            {"id": "T2", "texto": _("teste_had_escore_completo")},
            {"id": "T3", "texto": _("teste_had_resposta_faltando")},
            {"id": "T4", "texto": _("teste_trilha_alteracao_historico")},
        ],
        "lacuna": "C3",
        "explica_lacuna": _("Nenhum teste confere que a recepção não abre o histórico de saúde. O teste da trilha registra quem alterou; não impede quem não devia ver."),
    },
}
```

A armadilha é ligar C3 a T4: os dois são do R3 e falam de acesso, mas T4 confere registro, não permissão. A lacuna
fica no meio da lista (C3), para não ser "a última linha".

### 7.3 Ligações certas e cobertura

| Critério | Requisito | Teste |
|---|---|---|
| C1 | R1 | T1 |
| C2 | R2 | T2 |
| C3 | R3 | nenhum (lacuna) |
| C4 | R2 | T3 |
| C5 | R3 | T4 |

Cobertura esperada: R1 1 critério, 1 teste · R2 2 critérios, 2 testes · R3 2 critérios, 1 teste.
Decisões: `saude_rast_acesso_ligacoes`, `saude_rast_acesso_lacuna` (Sistemas §5.2).

### 7.4 O bug na semana 7 (`scene_19`)

Só narrativa: `bugs_encontrados`, `vulnerabilidades` e `s19_pontos_maturidade` não mudam.

**(a) Ramo "Validação de permissões" do laço da manhã.** A fala do Mateus passa a depender do quadro:

```renpy
                show developer_security thinking at right_zoom
                if rast_lacuna_achada("saude_rast_acesso"):
                    developer_security "Ótimo! A recepção abrindo o histórico, o teste do quadro já tinha pegado. Sobrou outro: o perfil administrativo vê relatório clínico sem precisar. Corrija isso logo!"
                else:
                    developer_security "Ótimo! Papéis mal definidos são porta de entrada para problemas sérios. Detectou um acesso indevido de usuário comum. Corrija isso logo!"
                $ vulnerabilidades += 1
```

**(b) Bloco da tarde**, depois de `"{i}À tarde, o time se reúne para debater as vulnerabilidades e bugs encontrados,
...{/i}"` e antes do comentário `# Pequena ramificação: pedir ajuda`:

```renpy
    if rast_lacuna_achada("saude_rast_acesso"):
        show developer_test confident at right_zoom2
        developer_test "Uma boa notícia no meio dos bugs: a recepção abrindo o histórico de saúde nem chegou até hoje. O teste do quadro falhou na pipeline semana passada e o [NOME_DEVELOPER_CODING] corrigiu no mesmo dia."
        hide developer_test
    else:
        show developer_security serious at right_zoom
        show developer_test thinking at right_zoom2
        developer_security "Rodei a revisão de papéis antes do almoço. A falha mais séria: o perfil recepção abre o histórico de saúde inteiro. Diagnóstico, escalas, tudo."
        developer_test "Voltei ao quadro de rastreabilidade da semana passada. O critério estava lá, C3: recepção abre o histórico, acesso negado. Mas nenhum teste cobria. Foi esse o elo que faltou."
        developer_test "Já escrevi o teste que faltava. Agora ele roda em todo commit, e a correção só entra com ele passando."
        hide developer_security
        hide developer_test
```

O menu seguinte ("falha crítica") recebe a opção da pista `saude_p_papeis` (4.2), que vale nos dois casos.

**Ponto para a E6:** na linha da lacuna, escolher qualquer teste deve contar como "não achou a lacuna", sem a marca
"(confira)" de ligação errada; senão a marca entrega a lacuna. O mesmo vale para C4 do exemplo da Startup.

---

## 8. Energia nesta rota

### 8.1 Eventos nas cenas (Sistemas §4.2)

| Cena | Ponto exato | Linha | Efeito |
|---|---|---|---|
| `scene_12` | no bloco final, depois de `$ advance_minutes(18)` e antes de `"{i}Fim de tarde, sensação de dever cumprido...{/i}"` | `$ energia_gastar(1, _("especificação até a noite"))` | −1 |
| `scene_18` | ao lado de `$ energia_diaria = 1` (opção "Virar a noite e entregar tudo ainda hoje.") | `$ energia_gastar(3, _("virou a noite"))` e `$ im_hora_extra_somar(60)` | −3 e −60 min na S7 |
| `scene_19` | depois do menu "Enfrenta dificuldade para corrigir uma falha crítica", antes do gancho da S7 | `$ energia_gastar(1, _("dia inteiro caçando bugs"))` | −1 |
| `scene_20` | no bloco final, depois de `$ advance_minutes(29)` e antes de `"{i}Ao cair da noite, a equipe celebra...{/i}"` | `$ energia_gastar(2, _("dia de deploy"))` | −2 |

A lição aparece sozinha: quem vira a noite na S6 entrega o módulo, mas chega à S7 com o bloco de 180 min reduzido a
120 (ou 90, se estiver em Cansaço) e com menos ações de ajuda possíveis.

### 8.2 Falas com energia baixa (`if energia_cansaco():`, uma fala a mais, sem `else`)

| Cena | Depois de | Fala |
|---|---|---|
| `scene_14` | `developer_test "E do ponto de vista de testes, quanto mais modular e desacoplado..."` | `developer_test "(baixinho) Tá com cara de sono, [player_name]. Pega um café; essa discussão vai longe."` |
| `scene_16` | `developer_management "Vamos revisar nosso cronograma e discutir riscos do projeto..."` | `developer_management "[player_name], se a semana pesou, fala. Planejar também é planejar o descanso de quem faz."` |
| `scene_19` | `developer_security "E qualquer brecha de segurança pode virar dor de cabeça..."` | `developer_quality "Vamos devagar no checklist hoje. Teste feito com sono vira teste pulado."` |
| `scene_20` | `developer_management "Atenção, equipe! Chegou o grande momento..."` | `developer_management "Quem estiver no limite me avisa antes. Deploy cansado é deploy com erro."` |
| `scene_21` | `developer_management "Pessoal, caprichem na apresentação..."` | `developer_management "E, [player_name]: ontem foi puxado. Hoje você só precisa contar o que fizemos, do jeito que viveu."` |

Dentro das intermissões: fala de cansaço em cada abertura (seção 2), nos dois descansos (3.4) e no encontro 4 da
mentoria (5). Nenhuma muda decisão, registro, conquista ou final.

---

## 9. Registros extras do notebook (estudar)

| Sem. | id | Título | Texto |
|---|---|---|---|
| 1 | `saude_extra_glossario` | Glossário do projeto | Um glossário dá um sentido só a cada termo do domínio: histórico de saúde, carga tabágica (maços por dia vezes anos de fumo), retorno, escala HAD. Quando equipe e médicas usam a mesma palavra para a mesma coisa, o requisito não muda de sentido no caminho. |
| 2 | `saude_extra_fluxos` | Fluxo alternativo e exceção | Fluxo alternativo é outro caminho que ainda chega ao objetivo, como o cadastro provisório do paciente sem CPF. Exceção é quando o objetivo não é alcançado e o sistema precisa reagir, como guardar o rascunho quando a conexão cai. Os dois entram no caso de uso, com o passo onde começam. |
| 3 | `saude_extra_acoplamento` | Coesão e acoplamento | Um módulo coeso faz uma coisa só, como calcular as escalas. Acoplamento baixo quer dizer que mudar um módulo não obriga a mexer nos outros. Separar a gravação dos dados da regra de negócio reduz o acoplamento e facilita os testes. |
| 4 | `saude_extra_estimativa` | Estimativa em equipe | No planning poker, todos mostram a estimativa ao mesmo tempo, e as diferenças grandes viram conversa: quem estimou alto costuma ver um risco que os outros não viram. Estime em tamanho relativo e compare com a capacidade real da equipe. |
| 5 | `saude_extra_revisao` | O que olhar numa revisão de código | Comece pelo comportamento: o código faz o que o requisito pede, inclusive nas exceções? Depois, nomes claros, entradas validadas, dado sensível fora do log e testes junto da mudança. Comente o código, não a pessoa, e prefira revisões pequenas. |
| 6 | `saude_extra_piramide` | Pirâmide de testes | Muitos testes de unidade (rápidos e baratos), menos testes de integração e poucos testes de ponta a ponta (lentos e frágeis). Com a pirâmide invertida, a pipeline demora e as falhas aparecem tarde. |
| 7 | `saude_extra_rollback` | Plano de rollback | Antes do deploy, escreva como voltar: para qual versão, quem decide, em quanto tempo e o que acontece com os dados gravados na versão nova. Ensaie a volta em homologação. Rollback nunca testado é só uma esperança. |

Cada extra prepara a semana seguinte (glossário → entrevista; fluxos → casos de uso; acoplamento → arquitetura;
estimativa → planejamento; revisão → codificação; pirâmide → testes; rollback → deploy). Nenhum é pré-requisito: o
conteúdo de cada um também aparece, mais curto, nas cenas da semana seguinte.

---

## 10. Mudanças nas cenas existentes (lista para a E5)

Toda linha nova de `call` leva `from`. Nenhum label ou variável existente muda de nome.

| Arquivo | Mudança | Seção |
|---|---|---|
| `game/script.rpy` | 4 ganchos A: `_im_saude_s1` (antes de `scene_4`), `_im_saude_s2` (antes de `scene_9`), `_im_saude_s3` (antes de `scene_13`), `_im_saude_s4` (antes de `scene_15`) | 2 |
| `scene_4_retorno_casa.rpy` | `$ advance_minutes(150)` → `$ advance_minutes(50)` | 2 (S1) |
| `scene_10_criacao_casos_uso.rpy` | caça à ambiguidade (`_amb_s10`); quarta opção da pista `saude_p_cpf` no menu da pausa | 6, 4.2 |
| `scene_12_especificacao_requisitos.rpy` | `pista_lembrar` (`_pl_s12_had`); fala condicional da ambiguidade; energia −1 | 4.2, 6, 8.1 |
| `scene_14_discussao_arquitetura.rpy` | fala de cansaço (César) | 8.2 |
| `scene_15_aniversario_surpresa.rpy` | "Já no dia seguinte..." → "Depois do almoço..."; fala do segredo do Mateus (abaixo) | 2 (S4) |
| `scene_16_reuniao_gerenciamento.rpy` | `pista_lembrar` (`_pl_s16_plano`); fala de cansaço (Robert) | 4.2, 8.2 |
| `scene_17_tarde_estudos_tecnicos.rpy` | rastreabilidade (`_rast_s17`); gancho B da S5 (`_im_saude_s5`) | 7.1, 2 |
| `scene_18_codificacao_implementacao.rpy` | gancho B da S6 (`_im_saude_s6`) + `scene`/`music` depois dele; energia −3 e hora extra 60 | 2, 8.1 |
| `scene_19_testes_seguranca.rpy` | fala condicional no ramo de permissões; bloco do bug; opção da pista `saude_p_papeis`; energia −1; gancho B da S7 (`_im_saude_s7`) + música; fala de cansaço (Daiana) | 7.4, 4.2, 8 |
| `scene_20_deploy_final.rpy` | opções das pistas `saude_p_backup` e `saude_p_memoria`; energia −2; fala de cansaço (Robert) | 4.2, 8 |
| `scene_21_avaliacao_final.rpy` | gancho B da S8 (`_im_saude_s8`) + música; falas da mentoria; fala de cansaço (Robert) | 2, 5, 8.2 |

**Segredo do Mateus na `scene_15`** (só fala): depois de
`developer_security "Nossa, gente... Nem sei o que dizer. Vocês são demais!"`:

```renpy
    if saude_im_fez(4, "conversar", "developer_security"):
        "{i}Você lembra da mensagem que ele escondeu no almoço: \"Parabéns, filho. Vem jantar?\". Agora o \"dia comum\" faz sentido.{/i}"
```

**Tipos de menu** (Sistemas §6.3) nos menus citados aqui: `scene_10` pausa → `conversa`; `scene_19` falha crítica →
`trabalho`; `scene_20` backup e bug crítico → `trabalho`. Opções de pista → `pista`.

### 10.1 Fundo e música depois dos ganchos B

| Gancho | Linha seguinte na cena | Precisa |
|---|---|---|
| S5 (`scene_17`) | `$ set_available('all')`, `play music`, `scene bg quarto_noite` | nada |
| S6 (`scene_18`) | `if not finalizou_no_escritorio:` (o caminho "terminou" fala sem `scene`) | `scene bg escritorio_interior_noite` com `dissolve` e `play music music_office_relaxed fadein 1.0` |
| S7 (`scene_19`) | `scene bg escritorio_interior_noite` (sem música) | `play music music_office_relaxed fadein 1.0` |
| S8 (`scene_21`) | `scene bg transito_tarde` (sem música) | `play music music_home_reflecting fadein 1.0` |

Se a E4 decidir que `im_intermissao` restaura fundo e música sozinha, estas linhas saem.

---

## 11. Dados da rota (`game/data/intermissoes/saude.rpy`, `init 3 python`)

```python
init 3 python:
    ROUTES["saude"]["mapa"] = {
        "imagem": "images/mapas/saude.png",
        "musica": "music_office_relaxed",
        "pois": [
            {"id": "mesa", "nome": _("Mesa da equipe"), "bg": "escritorio_interior_tarde", "pos": (760, 270), "abre": 1, "acoes": []},
            {"id": "sala_reunioes", "nome": _("Sala de reuniões"), "bg": "sala_reunioes_tarde", "pos": (430, 250), "abre": 1, "acoes": ["estudar"]},
            {"id": "cafe", "nome": _("Café"), "bg": "empresa_cafe_tarde", "pos": (450, 470), "abre": 1, "acoes": ["descansar"]},
            {"id": "refeitorio", "nome": _("Refeitório"), "bg": "refeitorio_tarde", "pos": (780, 520), "abre": 1, "acoes": []},
            {"id": "praca", "nome": _("Praça em frente"), "bg": "empresa_exterior_manha", "pos": (1150, 640), "abre": 1, "acoes": ["descansar"]},
            {"id": "ambulatorio", "nome": _("Ambulatório do Instituto"), "bg": "escritorio_medica", "pos": (1560, 380), "abre": 2, "acoes": ["observar"]},
            {"id": "servidores", "nome": _("Sala de servidores"), "bg": "sala_servidores", "pos": (600, 760), "abre": 6, "acoes": []},
        ],
    }

    ROUTES["saude"]["intermissoes"] = {
        1: {"dia": _("Primeiro dia"), "inicio": (16, 0), "bloco": 120, "mesmo_dia": False,
            "agenda": {"mesa": ["developer_requirements", "developer_coding"],
                       "sala_reunioes": ["developer_management"],
                       "cafe": ["developer_ai", "developer_test"],
                       "refeitorio": ["developer_quality", "developer_project"],
                       "praca": ["developer_security"]},
            "fechados": {}, "ajudar": {}, "observar": {}, "estudar": "saude_extra_glossario"},
        2: {"dia": _("Sexta"), "inicio": (16, 0), "bloco": 180, "mesmo_dia": True,
            "agenda": {"mesa": ["developer_coding", "developer_security"],
                       "sala_reunioes": ["developer_management", "developer_project"],
                       "cafe": ["developer_requirements"],
                       "refeitorio": ["developer_quality", "developer_test"],
                       "praca": ["developer_ai"],
                       "ambulatorio": ["doutora_2", "doutora_1"]},
            "fechados": {}, "ajudar": {"developer_coding": None},
            "observar": {"ambulatorio": "saude_p_cpf"}, "estudar": "saude_extra_fluxos"},
        3: {"dia": _("Sexta"), "inicio": (15, 0), "bloco": 180, "mesmo_dia": False,
            "agenda": {"mesa": ["developer_quality", "developer_ai"],
                       "sala_reunioes": ["developer_requirements", "developer_management"],
                       "cafe": ["developer_coding", "developer_test"],
                       "refeitorio": ["developer_project", "developer_security"],
                       "ambulatorio": ["doutora_2"]},
            "fechados": {}, "ajudar": {"developer_management": None},
            "observar": {"ambulatorio": "saude_p_autosave"}, "estudar": "saude_extra_acoplamento"},
        4: {"dia": _("Sexta"), "inicio": (12, 0), "bloco": 180, "mesmo_dia": False,
            "agenda": {"mesa": ["developer_security"],
                       "sala_reunioes": ["developer_management", "developer_project"],
                       "cafe": ["developer_requirements", "developer_quality"],
                       "refeitorio": ["developer_coding", "developer_test", "developer_ai"],
                       "ambulatorio": ["doutora_2", "doutora_1"]},
            "fechados": {}, "ajudar": {"developer_test": None},
            "observar": {"ambulatorio": "saude_p_autosave"}, "estudar": "saude_extra_estimativa"},
        5: {"dia": _("Sexta"), "inicio": (16, 0), "bloco": 180, "mesmo_dia": True,
            "agenda": {"mesa": ["developer_coding", "developer_test"],
                       "sala_reunioes": ["developer_management", "developer_requirements"],
                       "cafe": ["developer_ai"],
                       "refeitorio": ["developer_quality", "developer_project"],
                       "praca": ["developer_security"],
                       "ambulatorio": ["doutora_2"]},
            "fechados": {},
            "ajudar": {"developer_coding": "saude_p_memoria", "developer_security": "saude_p_papeis"},
            "observar": {"ambulatorio": None}, "estudar": "saude_extra_revisao"},
        6: {"dia": _("Dia da codificação"), "inicio": (16, 30), "bloco": 180, "mesmo_dia": True,
            "agenda": {"mesa": ["developer_coding", "developer_ai"],
                       "sala_reunioes": ["developer_project"],
                       "cafe": ["developer_requirements", "developer_quality"],
                       "refeitorio": ["developer_management"],
                       "praca": ["developer_test"],
                       "ambulatorio": ["doutora_2"],
                       "servidores": ["developer_security"]},
            "fechados": {},
            "ajudar": {"developer_coding": "saude_p_memoria", "developer_security": "saude_p_backup"},
            "observar": {"ambulatorio": None}, "estudar": "saude_extra_piramide"},
        7: {"dia": _("Dia dos testes"), "inicio": (15, 30), "bloco": 180, "mesmo_dia": True,
            "agenda": {"mesa": ["developer_test", "developer_quality"],
                       "sala_reunioes": ["developer_management", "developer_project"],
                       "cafe": ["developer_coding"],
                       "refeitorio": ["developer_ai", "developer_requirements"],
                       "ambulatorio": ["doutora_2", "doutora_1"],
                       "servidores": ["developer_security"]},
            "fechados": {},
            "ajudar": {"developer_test": "saude_p_memoria", "developer_security": "saude_p_backup"},
            "observar": {"ambulatorio": None}, "estudar": "saude_extra_rollback"},
        8: {"dia": _("Último dia"), "inicio": (9, 30), "bloco": 180, "mesmo_dia": True,
            "agenda": {"mesa": ["developer_requirements", "developer_management"],
                       "sala_reunioes": ["developer_project", "developer_quality"],
                       "cafe": ["developer_ai", "developer_coding"],
                       "praca": ["developer_test"],
                       "ambulatorio": ["doutora_2"],
                       "servidores": ["developer_security"]},
            "fechados": {}, "ajudar": {},
            "observar": {"ambulatorio": None}, "estudar": None},
    }

    ROUTES["saude"]["pistas"] = {
        "saude_p_cpf": {"titulo": _("O paciente sem CPF"),
            "texto": _("Na recepção do ambulatório, um paciente chegou sem documento. A recepcionista anotou o nome num papel para cadastrar depois, e a ficha ficou sem CPF."),
            "ate_semana": 2, "uso": _("Semana 3: um fluxo alternativo do cadastro.")},
        "saude_p_had": {"titulo": _("A escala pela metade"),
            "texto": _("Na triagem, um paciente pulou duas perguntas da escala HAD no papel. A Dra. Nathalia não conseguiu fechar o escore e escreveu 'incompleta' na margem."),
            "ate_semana": 2, "uso": _("Semana 3: a inspeção do requisito da HAD.")},
        "saude_p_autosave": {"titulo": _("O formulário que sumiu"),
            "texto": _("No ambulatório, a internet caiu no meio de uma consulta e o formulário quase pronto se perdeu. A médica refez as perguntas com o paciente esperando."),
            "ate_semana": 4, "uso": _("Semana 5: o plano da primeira entrega.")},
        "saude_p_papeis": {"titulo": _("A senha emprestada"),
            "texto": _("A recepção entra no sistema com a senha da Dra. Nathalia, porque o perfil da recepção não abre a agenda. Tudo o que a recepção faz fica registrado como se fosse a médica."),
            "ate_semana": 6, "uso": _("Semana 7: a revisão de papéis de acesso.")},
        "saude_p_memoria": {"titulo": _("O servidor que reinicia"),
            "texto": _("O servidor de testes é reiniciado toda madrugada por uma rotina automática. Nenhum teste roda mais de um dia seguido."),
            "ate_semana": 7, "uso": _("Semana 8: o bug crítico antes do deploy.")},
        "saude_p_backup": {"titulo": _("O backup nunca restaurado"),
            "texto": _("A rotina de backup aparece verde todo dia há dois anos, mas ninguém nunca tentou restaurar uma cópia."),
            "ate_semana": 7, "uso": _("Semana 8: o checklist de deploy.")},
    }

    ROUTES["saude"]["extras"] = [
        {"id": "saude_extra_glossario", "title": _("Glossário do projeto"), "text": _("...")},   # textos da seção 9
        # ... os 7 da seção 9, na ordem das semanas
    ]
    # ROUTES["saude"]["mentoria"], ["conquistas_extra"]: seção 5
    # ROUTES["saude"]["ambiguidades"]: seção 6 · ROUTES["saude"]["rastreabilidade"]: seção 7.2

define saude_npc_recepcao = Character(_("Sônia"), color="#A89A84")
define saude_npc_ivo = Character(_("Seu Ivo"), color="#9FB3A5")
define saude_npc_celia = Character(_("Dona Célia"), color="#C7A6B5")
```

Conferências do `im_validar_dados("saude")`: a Nathalia (mentora) está na agenda das semanas 2 a 8 (7 de 7); todo
`ajudar` aponta para alguém presente no local daquela semana; `ate_semana` ≥ semana de origem em todas as pistas;
`inicio + bloco` termina antes da meia-noite em todas as semanas (a mais tarde, S6, termina 19h30).

---

## 12. Para a aula: o que o tempo livre aprofunda

| Sem. | Aprofunda (opcional) | Onde o caminho principal já ensina |
|---|---|---|
| 1 | glossário | ciclo de vida (`scene_3`) |
| 2 | observação como técnica de elicitação; anotar sem identificar | entrevista (`scene_6`), classificação (`scene_7`) |
| 3 | perda de dados vista de perto; quebrar caso de uso em tarefas | casos de uso, ambiguidade (`scene_10`), inspeção (`scene_12`) |
| 4 | fronteiras da HAD; papéis de acesso no trabalho real | arquitetura e negociação (`scene_14`) |
| 5 | critério escrito de prioridade; tempo de tarefa | planejamento (`scene_16`), rastreabilidade (`scene_17`) |
| 6 | mensagem de erro como requisito; backup que nunca foi restaurado | codificação (`scene_18`) |
| 7 | anonimização na prática; teste de resistência | testes e segurança (`scene_19`) |
| 8 | o sistema em uso real | deploy e avaliação (`scene_20`, `scene_21`) |

Com "Tempo livre: pular", as pistas não aparecem e as cenas seguem pelas opções de sempre; os 8 registros, as decisões,
a escrita, o planejamento, a ambiguidade e a rastreabilidade continuam todos no caminho principal.

---

## 13. Estimativa de palavras e minutos

**Palavras escritas (conteúdo novo da rota):**

| Bloco | Itens | Palavras |
|---|---|---|
| Aberturas (S1 tutorial + S2–S8 + falas de cansaço) | 8 | ~600 |
| Fios dos developers | 24 conversas | ~4.100 |
| Fios e conversas das médicas | 6 | ~1.050 |
| Conversas próprias (Mateus S4, Emily S8) | 2 | ~450 |
| Papo rápido | 9 pessoas | ~550 |
| Observar | 7 | ~2.450 |
| Ajudar | 7 labels | ~2.450 |
| Estudar + textos dos extras | 7 + 7 | ~1.350 |
| Descansar | 2 | ~220 |
| Mentoria | 5 | ~2.350 |
| Dados (pistas, ambiguidade, rastreabilidade) | — | ~900 |
| Mudanças nas cenas (pistas, bug, energia, mentoria, segredo) | — | ~1.300 |
| **Total escrito** | | **≈ 17.800** |

**Lido por partida** (caminho típico: 2 a 4 ações por semana, ~24 ações): aberturas ~400; ~10 conversas ~1.750;
3 observações ~1.050; 3 ajudas ~1.050; 3 estudos ~450; 3 mentorias ~1.400; 2 descansos ~140; mudanças nas cenas e
mecânicas ~1.300. **Total ≈ 7.500 palavras** (a rota hoje tem ~13 mil por partida).

**Minutos adicionados:**

| Item | Minutos |
|---|---|
| Leitura das intermissões (~6.200 palavras) | ~35 |
| Mapa, escolhas e resumos (8 semanas) | ~10 |
| Caça à ambiguidade | ~7 |
| Rastreabilidade | ~9 |
| Falas novas nas cenas e pontos de parada | ~3 |
| **Total** | **≈ +64** (rota de ~80–90 para **≈ 145–155 min**) |
| Com "Tempo livre: pular" | ≈ +19 (**≈ 100–110 min**) |

Bate com o Sistemas §8.1. Para 4 aulas de 50 min: duas semanas de jogo por aula (~37 min) e 10–15 min de conversa.
