# Bíblia da rota Startup

Rota da vaga 2 de `scene_1_quarto` (`chosen_job == "startup"`): desenvolvimento mobile em uma startup de educação financeira. Esta bíblia é a fonte para as fases F2 (infraestrutura), F3 (arte) e F4 (cenas). A especificação de arte em formato de máquina está em `docs/rotas/startup-assets.json`.

## 1. Visão geral

**Empresa e produto.** A Trocado é uma startup de sete pessoas que funciona no segundo andar de um casarão reformado, hoje um coworking em Botafogo, no Rio. O produto, também chamado Trocado, é um app para universitários registrarem gastos, acompanharem o total do mês e entenderem para onde vai o dinheiro da bolsa, do estágio ou da mesada. O MVP está em beta com cerca de 800 estudantes e tem nota 3,4 nas lojas.

**O problema que move a rota.** As avaliações repetem duas queixas: "meu total está errado" e "lancei o almoço duas vezes e não consigo apagar". A retenção de 30 dias caiu de 40% para 22%. A causa aparece aos poucos: quando o 4G cai no ônibus, o app reenvia o lançamento e o servidor grava duas vezes. Não existe exclusão segura de gasto.

**Prazo.** Em 8 semanas a equipe precisa publicar a versão 1.0 nas lojas antes do início do semestre (quando os calouros chegam e os cadastros multiplicam) e apresentar o produto no demo day da Aceleradora Maré, para investidores. O CEO quer mostrar tração e importação bancária via Open Finance. A estudante usuária quer confiar no total e não quer entregar acesso ao banco para um app que erra a conta.

**Semente da demo.** O conteúdo do contexto Startup da demo curta (gasto lançado duas vezes, exclusão com confirmação e total atualizado, cancelar a exclusão, importar gastos do banco como mudança negociada, corrigir valor de gasto como escrita livre) é a espinha dos atos 2 a 4. A rota longa acrescenta a causa técnica (sincronização sem idempotência), LGPD, Open Finance, métricas, lojas e o pico do semestre.

**Temas da rota além do ciclo comum:** MVP; Kanban com rituais mínimos de Scrum; métricas de produto (retenção vs. métrica de vaidade); revisão e lançamento gradual nas lojas; LGPD de dados financeiros e exclusão de conta; Open Finance por consentimento; pico de uso no início do semestre; demo day com investidores.

**Arco de 8 semanas**

| Semana | Ato | Cenas | O que acontece |
|---|---|---|---|
| 1 | 1 Descoberta | 01, 02, 03 | Chegada, equipe, produto, ciclo de vida em ciclos curtos, MVP |
| 2 | 2 Levantamento | 04 a 08 | Preparação, entrevista com Vinícius e Bia, classificação, social |
| 3 | 3 Especificação | 09 a 12 | Histórias e critérios, almoço, inspeção e escrita livre |
| 4 | 4 Arquitetura e gestão | 13, 14 | Causa do duplicado, modelagem, mudança de escopo negociada, festa dos mil estudantes |
| 5 | 4 Arquitetura e gestão | 15 | Planejamento com capacidade, riscos e métricas |
| 6 | 5 Implementação | 16 | Testes primeiro, PR pequeno, code review |
| 7 | 5 Implementação | 17 | Testes, carga do semestre, segurança e LGPD |
| 8 | 5 Implementação | 18 | Lojas, rollout gradual, pico do semestre, demo day e avaliação |

**Tom.** O mesmo da versão longa: narração em itálico curta, falas naturais, humor leve, nenhum vilão. Vinícius pressiona, mas quer o bem dos estudantes. O jogador erra sem punição: cada distrator gera uma consequência concreta explicada por alguém da equipe e depois uma revisão orientada.

**Gênero do jogador.** Evitar adjetivos flexionados na narração ("você chega cedo" em vez de "você chega animado"). Quando inevitável, usar a flexão por `player_gender` definida na F2.

## 2. Elenco

Equipe da rota: `st_mentora`, `st_techlead`, `st_mobile`, `st_qualidade`. Stakeholders: `st_ceo`, `st_estudante`. A amizade que conta no final é a da equipe (4 pessoas). Nenhum nome repete a saúde ou a demo.

### 2.1 Tainá Duarte · `st_mentora`

- **Papel:** head de produto (PO) e responsável por requisitos. Guia do jogador, papel equivalente a Emily. Foi a terceira contratada da Trocado; antes trabalhou cinco anos no atendimento de um banco.
- **Personalidade:** calorosa e direta. Protege o tempo da equipe e pergunta "por quê?" até chegar na necessidade. Gosta de exemplos com dinheiro do dia a dia. Ri fácil e admite quando não sabe.
- **Jeito de falar:** frases curtas, "a gente", "me conta", "bora". Chama o jogador pelo nome. Usa valores concretos ("R$ 20 do almoço").
- **Cor do nome:** `#FF8A5B` (coral).
- **Descrição do contato:** "Head de produto. Te ajuda a transformar queixa em requisito."
- **Chat offline (8 respostas):**
  1. "Oi! Tô no meio de uma call, mas me conta: qual foi a última dúvida que apareceu?"
  2. "Quando alguém disser 'fácil', pergunta: fácil pra fazer o quê?"
  3. "Lembra: um exemplo com número vale mais que três adjetivos."
  4. "Hoje vi a Bia lançando gasto no bandejão. Observar ensina coisa que entrevista não pega."
  5. "Se o Vinícius pedir algo novo, não diga sim nem não ainda. Pergunta o que muda no prazo."
  6. "Tá cansado? Descansar também está no planejamento, viu."
  7. "Critério bom tem dado inicial, ação e resultado. O resto é desejo."
  8. "Valeu por hoje! Amanhã a gente continua, com café."

### 2.2 Otávio Ramos · `st_techlead`

- **Papel:** CTO e cofundador técnico. Cuida da API, arquitetura, infraestrutura, segurança e LGPD. Programa desde a época do internet banking por SMS.
- **Personalidade:** calmo, paciente, desconfiado de moda tecnológica. Conta "causos" de bugs antigos para ensinar. Leva dados pessoais muito a sério. Humor seco.
- **Jeito de falar:** pausado, faz perguntas em vez de dar a resposta ("e se o 4G cair aqui?"). Usa "veja bem" e comparações com obra e cozinha.
- **Cor do nome:** `#9ACD32` (verde-limão).
- **Descrição do contato:** "CTO e cofundador. Arquitetura, dados e segurança."
- **Chat offline (8 respostas):**
  1. "Veja bem: antes de escolher a ferramenta, desenha o caminho do dado."
  2. "Se der para repetir a mesma requisição sem estragar nada, você dormiu tranquilo."
  3. "Dinheiro em float é como medir farinha com régua. Centavo é inteiro."
  4. "Log não é diário. Não escreva nele o que você não mostraria para a Bia."
  5. "Estou revisando um PR. Respondo com calma daqui a pouco."
  6. "Em 2009 derrubei um banco de dados numa sexta. Desde então, não publico na sexta."
  7. "Dado que você não guarda não vaza."
  8. "Bom trabalho hoje. Vai pra casa, o servidor se vira até amanhã."

### 2.3 Davi Matsuda · `st_mobile`

- **Papel:** desenvolvedor mobile pleno (app em React Native). Parceiro de código do jogador e principal revisor de PRs.
- **Personalidade:** entusiasmado, rápido, adora ferramenta nova e às vezes atropela etapas. Generoso para ensinar. Gamer, faz trocadilhos ruins de propósito.
- **Jeito de falar:** gírias leves ("pô", "fechou", "mano"), termos em inglês do dia a dia de dev (PR, merge, build). No chat escreve "kkk".
- **Cor do nome:** `#5BC0EB` (azul-céu).
- **Descrição do contato:** "Dev mobile. Topa um pair programming a qualquer hora."
- **Chat offline (8 respostas):**
  1. "Fala! Tô esperando o build terminar, pode mandar kkk"
  2. "PR pequeno é PR revisado. PR gigante é PR aprovado sem ler."
  3. "Testei no celular mais barato da loja. Se roda nele, roda em qualquer um."
  4. "Mano, deploy de app não é site. Não dá pra dar F5 no celular de 800 pessoas."
  5. "Escreve o teste do cancelamento antes, confia."
  6. "Sábado tem partida online, se quiser entrar no time."
  7. "Trocadilho do dia: o app tá tão leve que nem pesa no bolso. Desculpa."
  8. "Fechou! Amanhã a gente pareia nisso."

### 2.4 Lorena Bezerra · `st_qualidade`

- **Papel:** qualidade e pesquisa com usuários. Planeja testes, lê todas as avaliações das lojas, faz testes de usabilidade e cuida da acessibilidade. Foi professora de Português em Campina Grande antes de migrar para tecnologia.
- **Personalidade:** meticulosa, empática com quem usa o app, cética com "achismo". Gentil, mas não aprova nada sem evidência.
- **Jeito de falar:** organiza em listas ("primeiro..., segundo..."), pergunta "cadê a evidência?", solta um "oxe" quando algo a surpreende.
- **Cor do nome:** `#E05FD0` (magenta).
- **Descrição do contato:** "Qualidade e pesquisa com usuários. Lê todas as avaliações da loja."
- **Chat offline (8 respostas):**
  1. "Oi! Tô lendo avaliação da loja. Hoje tem 3 novas, uma falando de total errado."
  2. "Primeiro: o que a pessoa tentou fazer. Segundo: o que aconteceu. Terceiro: o que esperava."
  3. "Oxe, 'confuso' não é defeito. Confuso onde, em qual passo?"
  4. "Teste o caminho de cancelar também. Usuário desiste o tempo todo."
  5. "O botão de excluir precisa ter nome para o leitor de tela, não só um ícone."
  6. "Cadê a evidência? Uma avaliação é um sinal; nove é um padrão."
  7. "Mês que vem tem teste de usabilidade com calouros. Quer assistir?"
  8. "Bom descanso! Amanhã eu te mostro o que achei."

### 2.5 Vinícius Prado · `st_ceo` (stakeholder)

- **Papel:** CEO e cofundador. Cuida de investidores, parcerias e da apresentação no demo day. Foi bolsista e conta que quase largou a faculdade por falta de dinheiro.
- **Personalidade:** carismático, otimista e ansioso com prazos. Fala em pitch, mas muda de ideia quando vê dados. Quer de verdade ajudar estudantes.
- **Jeito de falar:** jargão de startup ("tração", "escalar", "north star", "runway"), números redondos, exclamações.
- **Cor do nome:** `#F4D35E` (dourado).
- **Descrição do contato:** "CEO da Trocado. Sempre com um investidor na outra linha."
- **Chat offline (8 respostas):**
  1. "Fala! Saindo de uma reunião com fundo agora. O que manda?"
  2. "Investidor não quer só número grande. Quer ver gente voltando a usar."
  3. "Open Finance vai ser nosso diferencial. Mas só quando estiver redondo, prometo."
  4. "Se eu estiver pedindo coisa demais, me fala com o impacto. Eu escuto."
  5. "Demo day chegando! Tô ensaiando o pitch no espelho."
  6. "Mil estudantes cadastrados! Mas a Lorena me lembrou da retenção..."
  7. "Eu era bolsista. Esse app é o que eu queria ter tido."
  8. "Valeu, time! Agora vou ligar pro próximo investidor."

### 2.6 Beatriz Tavares, a Bia · `st_estudante` (stakeholder)

- **Papel:** estudante de Engenharia Ambiental, 20 anos, bolsista, de Manaus (povo Baré). Mora em república, é monitora de Cálculo e usa o beta desde o primeiro mês. Representa as pessoas usuárias.
- **Personalidade:** prática, sincera e desconfiada no começo. Conta histórias com detalhes e valores. Muito cuidadosa com privacidade.
- **Jeito de falar:** simples, cita valores exatos ("R$ 4,50 do bandejão"), usa "égua" quando se espanta e "tipo assim" para explicar.
- **Cor do nome:** `#8DD694` (verde-menta).
- **Descrição do contato:** "Estudante e beta tester. Anota tudo, até o cafezinho."
- **Chat offline (8 respostas):**
  1. "Oi! Tô entre uma aula e outra, pode falar."
  2. "Hoje lancei o bandejão, R$ 4,50. Apareceu uma vez só. Progresso, né?"
  3. "Égua, recebi um alerta estranho do app. Brincadeira, foi do banco mesmo."
  4. "Antes de pedir meu banco, me mostra que o total está certo."
  5. "Se eu desistir de excluir, o gasto tem que ficar lá. Simples assim."
  6. "Minhas amigas da república perguntaram do app. Disse que tá melhorando."
  7. "Tipo assim: eu só quero saber quanto sobra até a bolsa cair."
  8. "Obrigada por ouvir! Até a próxima."

## 3. Cenas

Convenções: "Disponíveis" lista quem está fora da cena e pode receber mensagem (argumentos de `set_available` da rota). Stakeholders só entram na lista depois de `add_contact` na cena 05. Toda decisão pedagógica tem 1 opção adequada (A) e 2 distratores (D1, D2); se o jogador escolhe um distrator, segue a revisão orientada (menu de uma opção) e a cena continua. `st_acertos += 1` só na primeira escolha adequada. Menus sociais usam `add_friendship_point(id, 1)`.

### Ato 1 · Descoberta

#### st_01_chegada · Bem-vindo à Trocado

- **Semana/horário:** semana 1, segunda, 9h00 a 11h30.
- **Fundos:** `bg transito_manha` → `bg startup_coworking_manha` (novo).
- **Artefatos:** `st_app_gastos.png` (versão beta atual), `st_painel_metricas.png`.
- **Música:** `music_office_motivated`.
- **Presentes:** Tainá, Otávio, Davi, Lorena. Disponíveis: nenhum (`set_available()`); os contatos ainda não existem.
- **Resumo:** O jogador chega de ônibus a Botafogo e sobe a escada do casarão até o coworking. Tainá recebe na porta, explica que a Trocado tem sete pessoas e que ali "todo mundo faz um pouco de tudo". Ela apresenta Otávio (CTO, entre duas reuniões), Davi (mobile, com três celulares de teste na mesa) e Lorena (qualidade, lendo avaliações da loja). Cada um vira contato. Davi mostra o app no celular: lançar gasto, lista do mês, total. Lorena lê duas avaliações reais do beta: "meu total está errado" e "lancei o almoço duas vezes e não consigo apagar". Tainá mostra o painel de métricas: 800 estudantes no beta, nota 3,4, retenção de 30 dias caindo de 40% para 22%. Ela apresenta o desafio: versão 1.0 nas lojas antes do início do semestre e demo day com investidores na mesma semana. O jogador recebe acesso ao repositório e instala o beta no próprio celular.
- **Objetivos de aprendizagem:** papéis acumulados em equipe pequena; o produto existe para resolver um problema de pessoas reais; primeira noção de métrica de produto (retenção).
- **Menus:**
  - Social, "O que mais chamou sua atenção até agora?":
    - "As avaliações dos estudantes. Quero entender o que está dando errado." → `add_friendship_point("st_mentora", 1)`. Tainá: "Começou pelo lugar certo."
    - "O app em si. Quero ver como ele é construído." → `add_friendship_point("st_mobile", 1)`. Davi já abre o projeto no notebook.
    - "Como vocês aguentam o ritmo com tão pouca gente?" → `add_friendship_point("st_techlead", 1)`. Otávio: "Fazendo menos coisas, mas direito."
- **Variáveis:** `add_contact` e `add_friendship_point(id, 1)` para os quatro da equipe (apresentação).
- **Notebook:** nenhum registro.
- **Meta de palavras:** 550.

#### st_02_reuniao_ciclo · Ciclo curto, não ciclo pulado

- **Semana/horário:** semana 1, quarta, 10h00 a 12h00.
- **Fundos:** `bg sala_reunioes_manha` (o "aquário" do coworking).
- **Artefatos:** `st_quadro_kanban.png`.
- **Música:** `music_office_concentrated_1`.
- **Presentes:** equipe completa; Vinícius abre a reunião e sai. Disponíveis: nenhum.
- **Resumo:** Vinícius entra com pressa, apresenta-se ao jogador ("seja bem-vindo à revolução do trocado!") e diz que o fundo quer ver tração no demo day; sai para uma ligação. Tainá desenha o ciclo de vida no quadro: descobrir, especificar, construir, testar, lançar, medir. Ela explica que numa startup o ciclo não some, ele encolhe: cada volta dura uma semana. Mostra o quadro Kanban com limite de duas tarefas em andamento por pessoa e os rituais mínimos que pegaram do Scrum: planejamento na segunda, conversa diária de dez minutos e revisão na sexta. Otávio diz que "MVP não é desculpa para pular etapa, é para fazer cada etapa menor". Davi lembra que app não é site: cada versão passa pela revisão das lojas e não dá para "dar F5 no celular de 800 pessoas". Lorena fecha: o ciclo só termina quando medimos se o estudante voltou a usar. O jogador responde o que entende por MVP.
- **Objetivos de aprendizagem:** ciclo de vida adaptado a ciclos curtos; MVP como teste de hipótese com usuários reais; Kanban com limite de WIP e rituais leves; particularidade do deploy mobile.
- **Menus:**
  - Pedagógico, "Para a equipe, o que é um MVP?" (`st_d02_mvp`):
    - A: "A menor versão que resolve um problema real e nos deixa aprender com estudantes de verdade." → `st_d02_mvp = True`, `st_acertos += 1`. Tainá: "Isso. O 'mínimo' é sobre escopo, não sobre qualidade."
    - D1: "O app completo, só que sem acabamento, para lançar logo." → Otávio: "Aí a gente entrega tudo meio quebrado e não sabe qual parte falhou. Foi assim que nasceu o total errado."
    - D2: "Um protótipo bonito para impressionar os investidores." → Lorena: "Protótipo sem usuário não mede nada. No demo day vão perguntar quem usa e quem voltou."
    - Revisão: "Então o MVP precisa resolver um problema e gerar aprendizado com gente real?" → Tainá confirma com o exemplo do total confiável.
  - Social, "Como você prefere aprender por aqui?":
    - "Fazendo junto, em par." → `st_mobile` +1.
    - "Observando e anotando primeiro." → `st_mentora` +1.
    - "Vendo os usuários usarem o app." → `st_qualidade` +1.
- **Variáveis:** `st_d02_mvp`.
- **Notebook:** registro 1, "MVP e ciclo curto".
- **Meta de palavras:** 550.

#### st_03_casa_sem1 · O almoço que apareceu duas vezes

- **Semana/horário:** semana 1, sexta, 19h30 a 22h00.
- **Fundos:** `bg transito_noite` → `bg quarto_noite` → `bg cozinha_noite`.
- **Música:** `music_streets_focused` → `music_home_reflecting`.
- **Presentes:** ninguém da equipe. Disponíveis: `set_available("all")` (equipe).
- **Resumo:** No ônibus, o jogador testa o beta e lança o lanche da tarde, R$ 7. O ônibus entra no túnel, o app fica carregando e o jogador toca de novo em Salvar. Quando o sinal volta, o lanche aparece duas vezes e o total sobe R$ 14. A sensação é exatamente a da avaliação que Lorena leu. Em casa, revisa as anotações da semana (ciclo curto, MVP, quadro Kanban, o desafio das 8 semanas) e anota o horário e o túnel. Chega mensagem de Tainá: segunda tem preparação para a entrevista com Bia, uma estudante do beta, e com Vinícius. O jogador abre os contatos. Na cozinha, o colega de república conta que controla tudo numa planilha "porque app nenhum acerta". Card de fim de semana.
- **Card:** "Fim da Semana 1. Um MVP é pequeno no escopo, não na qualidade. E o problema dos estudantes acabou de acontecer com você."
- **Menus:** nenhum. `call screen contacts_screen`.
- **Variáveis:** `st_viu_duplicado = True`; `add_friendship_point("st_mentora", 1)` pela mensagem.
- **Notebook:** nenhum registro novo.
- **Meta de palavras:** 300.

### Ato 2 · Levantamento

#### st_04_preparacao · Roteiro na mão

- **Semana/horário:** semana 2, segunda, 9h30 a 11h30.
- **Fundos:** `bg startup_coworking_manha`.
- **Música:** `music_office_relaxed`.
- **Presentes:** Tainá, Lorena. Disponíveis: `st_techlead`, `st_mobile`.
- **Resumo:** Lorena mostra as 37 avaliações e mensagens de suporte do beta agrupadas por assunto: 14 de total errado, 9 de "não consigo apagar", 6 pedindo para conectar o banco, 3 pedindo modo escuro. Tainá explica que a entrevista à tarde será conjunta: Bia, que usa o app todo dia, e Vinícius, que decide o que vai para o demo day. Ela avisa que eles vão discordar. Tainá lembra que entrevista é uma técnica entre várias: as avaliações, as métricas e a observação também contam. O jogador conta o duplicado do túnel e Lorena anota como mais uma evidência. Em seguida, monta o roteiro. Pausa para café na copa.
- **Objetivos de aprendizagem:** preparar elicitação com perguntas abertas; usar dados existentes (avaliações, suporte) sem trocar a conversa por eles; não levar solução pronta.
- **Menus:**
  - Pedagógico, "Como você prepara o roteiro?" (`st_d04_roteiro`):
    - A: "Perguntas abertas sobre situações recentes, com os dados das avaliações para confirmar o que ouvirmos." → `st_acertos += 1`. Tainá: "Os dados dizem onde cavar; a conversa diz por quê."
    - D1: "Levar o desenho da tela nova para eles aprovarem." → Lorena: "Eles vão opinar sobre o seu desenho, não sobre o problema deles. A conversa fica presa na sua ideia."
    - D2: "Um questionário de sim ou não com a lista de funcionalidades." → Tainá: "Todo mundo responde sim para tudo. Saímos com 20 prioridades e nenhuma razão."
    - Revisão: "Troco por perguntas sobre a última vez que o problema aconteceu e levo os números como apoio." → Tainá aprova.
  - Social, na copa:
    - "Ofereço um café para a Tainá antes da entrevista." → `st_mentora` +1.
    - "Pergunto à Lorena qual avaliação mais a marcou." → `st_qualidade` +1. Lorena conta de uma estudante que desinstalou porque "achou que tinha perdido dinheiro".
    - "Fico revisando o roteiro em silêncio." → sem efeito; Tainá: "Concentração também vale."
- **Variáveis:** `st_d04_roteiro`.
- **Notebook:** nenhum registro.
- **Meta de palavras:** 400.

#### st_05_entrevista · Duas vozes, um app

- **Semana/horário:** semana 2, segunda, 14h00 a 15h30.
- **Fundos:** `bg sala_reunioes_tarde`.
- **Música:** `music_office_relaxed`.
- **Presentes:** Tainá, Vinícius, Bia. Disponíveis: `st_techlead`, `st_mobile`, `st_qualidade`.
- **Resumo:** Bia chega do campus entre duas aulas, ainda de mochila. Vinícius abre com o pedido vago: "Precisamos de um jeito fácil de controlar os gastos, e que impressione no demo day." O jogador abre a conversa (decisão 1). Bia conta o episódio: lançou o almoço de R$ 20 no ônibus, a internet caiu, tocou de novo; o almoço apareceu duas vezes, o total ficou R$ 20 acima, ela achou que tinha perdido dinheiro, não conseguiu apagar e desinstalou por três dias. Ela diz "se fosse fácil, isso não acontecia" e o jogador trata a palavra "fácil" (decisão 2). A regra fica: a pessoa deve poder excluir um gasto lançado por engano, com uma confirmação antes, e ver o total atualizado. Vinícius rebate: fácil para ele é não precisar lançar nada, importando do banco via Open Finance, e com medalhas para engajar. Bia responde que não dá acesso ao banco para um app que erra o total, e que medalha não paga almoço. O jogador conduz o conflito (decisão 3). Vinícius revela a métrica que o preocupa: retenção de 30 dias em 22%. No fim, os dois passam o contato.
- **Objetivos de aprendizagem:** pedir episódio concreto; transformar adjetivo em tarefa e resultado; mediar conflito entre stakeholders ligando os pedidos a um objetivo comum e registrando os dois.
- **Menus:**
  - Pedagógico 1, "Como você começa?" (`st_d05_episodio`):
    - A: "Bia, você pode contar a última vez em que o app te atrapalhou?" → `st_d05_episodio = True`, `st_acertos += 1`, `add_friendship_point("st_estudante", 1)`. Tainá (baixo): "Agora a gente sabe quem, o quê e qual consequência."
    - D1: "Qual funcionalidade você mais quer: modo escuro ou medalhas?" → Tainá: "Essa pergunta oferece duas soluções prontas. A Bia escolhe uma e a gente não descobre o que dói."
    - D2: "Você usaria mais se a tela tivesse menos botões?" → Tainá: "Ela pode dizer sim por educação. Menos botões é uma hipótese nossa, não um relato dela."
    - Revisão: "Bia, me conta a última vez em que isso aconteceu?"
  - Pedagógico 2, "O que fazer com 'fácil'?" (`st_d05_ambiguidade`):
    - A: "Pergunto o que ela precisa conseguir fazer naquela situação." → `st_d05_ambiguidade = True`, `st_acertos += 1`.
    - D1: "Anoto 'o app deve ser fácil' e deixo o time decidir." → Tainá: "Davi vai entender uma coisa, Lorena outra e a Bia uma terceira. Ninguém consegue testar 'fácil'."
    - D2: "Troco por 'moderno e intuitivo', que soa mais profissional." → Tainá: "Trocou um adjetivo por dois. O resultado esperado continua sem nome."
    - Revisão: "O que precisa acontecer para o problema que você contou não se repetir?" Tainá lembra que a regra resolve uma parte; usabilidade se confirma observando pessoas.
  - Pedagógico 3, conflito (`st_d05_conflito`):
    - A: "Pergunto a cada um que resultado espera e proponho decidir pelo objetivo comum: estudantes que confiam no total e voltam a usar." → `st_d05_conflito = True`, `st_acertos += 1`, `st_ceo` +1, `st_estudante` +1. Vinícius: "Retenção é exatamente o que o fundo vai perguntar." Fica registrado: total confiável é prioridade; importação bancária é hipótese a investigar, que depende de consentimento.
    - D1: "Fico com o Vinícius: ele decide o que vai para o demo day." → `st_ceo` +1. Tainá: "Se a Bia sai daqui sem ser ouvida, os 800 do beta continuam desinstalando. E a métrica do Vinícius cai junto."
    - D2: "Fico com a Bia e descarto o Open Finance." → `st_estudante` +1. Tainá: "A vontade de não lançar tudo à mão é real, e o Vinícius vai trazer o pedido de volta mais forte. Descartar não resolve."
    - Revisão: "Peço que cada um diga o que quer ver acontecer e procuro o que os dois têm em comum." → resultado igual ao de A, sem pontos de acerto.
  - **Conquista:** `st_conq_escuta` se `st_d05_episodio and st_d05_ambiguidade`.
- **Variáveis:** `st_d05_episodio`, `st_d05_ambiguidade`, `st_d05_conflito`, `st_conq_escuta`; `add_contact("st_ceo")`, `add_contact("st_estudante")`.
- **Notebook:** registro 2, "Da queixa ao requisito".
- **Meta de palavras:** 700.

#### st_06_classificacao · Cada post-it no seu lugar

- **Semana/horário:** semana 2, terça, 10h00 a 16h00.
- **Fundos:** `bg startup_coworking_manha` → `bg startup_coworking_tarde`.
- **Música:** `music_office_focused`.
- **Presentes:** Tainá, Lorena. Disponíveis: `st_techlead`, `st_mobile`, `st_ceo`, `st_estudante`.
- **Resumo:** As anotações da entrevista viram post-its na parede de vidro. Tainá propõe quatro colunas: funcional, não funcional, restrição (lei, lojas, parceiros) e ideia a validar. Lorena explica que cada tipo vira um teste diferente: funcional se testa executando, não funcional se mede, restrição se confere com a regra externa, ideia se valida com usuários. O jogador classifica três post-its. Lorena revisa as anotações do jogador e encontra "Bia achou confuso"; pergunta "confuso onde, em qual passo?". O jogador decide como reagir ao feedback. No fim da tarde, a parede tem um mapa claro do que é necessidade confirmada e do que ainda é aposta.
- **Objetivos de aprendizagem:** distinguir requisito funcional, não funcional, restrição e ideia a validar; não funcional precisa de medida; LGPD e Open Finance como restrições; anotar fatos observáveis.
- **Menus:** (`st_classif_acertos` conta as escolhas adequadas, 0 a 3)
  - Pedagógico 1, "Excluir um gasto lançado por engano, com confirmação, e ver o total atualizado" (`st_d06_funcional`):
    - A: "Funcional: é um comportamento que o app executa." → acerto.
    - D1: "Não funcional, porque é sobre a qualidade do total." → Lorena: "Ele descreve uma ação e um resultado. Se fosse não funcional, eu mediria tempo ou carga, e não teria como testar a exclusão."
    - D2: "Ideia a validar." → Tainá: "Já temos um episódio e nove avaliações. Isso é necessidade confirmada."
  - Pedagógico 2, "A lista de gastos deve abrir rápido no 4G" (`st_d06_nao_funcional`):
    - A: "Não funcional, e precisa de número: abrir em até 2 segundos em 95% das vezes, num celular de entrada com 4G." → acerto.
    - D1: "Funcional, porque fala da lista." → Lorena: "A lista existir é funcional. A velocidade é uma qualidade, e qualidade se mede."
    - D2: "Não funcional, e 'rápido' já é suficiente." → Lorena: "Davi vai achar rápido no celular dele, de topo de linha. A Bia, com o celular de 2019, não."
  - Pedagógico 3, "Importar gastos do banco automaticamente" (`st_d06_ideia`):
    - A: "Ideia a validar, que depende de restrições: consentimento do Open Finance, parceiro autorizado e LGPD." → acerto.
    - D1: "Funcional obrigatório da 1.0, porque o CEO pediu." → Tainá: "Ninguém contou um episódio sobre isso ainda, e depende de um parceiro autorizado. Se virar obrigatório agora, ocupa o espaço da exclusão segura."
    - D2: "Descartar, porque a Bia não quer." → Tainá: "A Bia não quer agora, com o total errado. A vontade de digitar menos aparece em seis avaliações. Fica como hipótese."
  - Revisão de cada distrator: "Coloco o post-it na coluna que permite testar do jeito certo." → Lorena move junto e explica.
  - Social, reação ao feedback sobre "achou confuso":
    - "Me mostra como você anotaria?" → `st_qualidade` +1. Lorena reescreve: "Bia procurou o botão de apagar na lista e não achou."
    - "Posso mandar mensagem para a Bia confirmar onde foi?" → `st_mentora` +1. Tainá: "Voltar ao stakeholder é parte do trabalho."
    - "É só uma anotação, depois eu lembro." → sem efeito. Lorena: "Daqui a três semanas ninguém lembra. Anotação é memória da equipe."
- **Variáveis:** `st_d06_funcional`, `st_d06_nao_funcional`, `st_d06_ideia`, `st_classif_acertos`.
- **Notebook:** registro 3, "Tipos de requisito".
- **Meta de palavras:** 500.

#### st_07_social · Fim de tarde no café

- **Semana/horário:** semana 2, quinta, 17h30 a 19h00.
- **Fundos:** `bg empresa_cafe_tarde` (o café do térreo do coworking).
- **Música:** `music_coffee_break_energized`.
- **Presentes:** Davi, Lorena. Disponíveis: `st_mentora`, `st_techlead`, `st_ceo`, `st_estudante`.
- **Resumo:** Davi chama o jogador para um pão de queijo depois do expediente; Lorena desce junto. Davi conta que fez o primeiro app aos 17, uma calculadora de nota que três colegas usaram. Lorena conta que dava aula de Português e que corrigir redação a ensinou a ler requisito. A conversa toca em PR pequeno ("PR gigante é PR aprovado sem ler", diz Davi), em teste no celular mais barato e em descanso. Os dois fazem convites para o fim de semana e para o mês seguinte. O jogador volta para casa mais perto da equipe.
- **Objetivos de aprendizagem:** integração; pistas leves de code review e testes em aparelhos reais.
- **Menus:**
  - Social, "Sobre o que você puxa conversa?":
    - "Como foi seu primeiro app, Davi?" → `st_mobile` +1.
    - "Como foi sair da sala de aula para a tecnologia, Lorena?" → `st_qualidade` +1.
    - "Qual app de banco mais irrita vocês?" → `st_mobile` +1. Os dois riem juntos; Lorena lembra que reclamação é requisito disfarçado.
  - Social, convites:
    - "Topo assistir ao teste de usabilidade com os calouros." → `st_qualidade` +1.
    - "Topo a partida online de sábado." → `st_mobile` +1.
    - "Vou descansar no fim de semana." → sem efeito. Davi: "Justo. Descanso também entra na sprint."
- **Variáveis:** nenhuma nova.
- **Notebook:** nenhum registro.
- **Meta de palavras:** 400.

#### st_08_casa_sem2 · O caderno da Bia

- **Semana/horário:** semana 2, sexta, 20h00 a 22h00.
- **Fundos:** `bg transito_noite` → `bg quarto_noite`.
- **Música:** `music_streets_focused` → `music_home_dreamy`.
- **Presentes:** ninguém. Disponíveis: `set_available("all")` (equipe e stakeholders).
- **Resumo:** No ônibus, o jogador relê as anotações: episódio, regra, conflito, colunas de classificação. Em casa, chega mensagem de Bia com a foto do caderno de papel em que ela confere os gastos "quando o app erra": é a solução de contorno, evidência de que a necessidade é real. Em seguida, Otávio escreve: ficou curioso com o duplicado do túnel e pede o horário exato, se o jogador lembrar. O jogador manda. O jogador compara o que aprendeu na disciplina sobre elicitação com o que viu na sala. Abre os contatos para conversar.
- **Card:** "Fim da Semana 2. Pergunte pela última vez em que aconteceu. Adjetivo vira tarefa; conflito vira objetivo comum."
- **Menus:** nenhum. `call screen contacts_screen`.
- **Variáveis:** `add_friendship_point("st_techlead", 1)` pela troca de mensagens.
- **Notebook:** nenhum registro novo.
- **Meta de palavras:** 300.

### Ato 3 · Especificação

#### st_09_historias · Como, quero, para

- **Semana/horário:** semana 3, segunda, 9h00 a 12h00.
- **Fundos:** `bg startup_coworking_manha`.
- **Artefatos:** `st_app_gastos.png` (protótipo da confirmação).
- **Música:** `music_office_concentrated_1`.
- **Presentes:** Tainá, Davi. Disponíveis: `st_techlead`, `st_qualidade`, `st_ceo`, `st_estudante`.
- **Resumo:** Tainá explica que na Trocado cada cartão do Kanban é uma história de usuário com critérios de aceitação; caso de uso completo só quando o fluxo tem muitos desvios. O jogador escolhe a versão bem escrita da história da exclusão. Depois escolhe o critério que verifica a regra combinada com a Bia e trata o caso limite do cancelamento. Davi mostra um protótipo rápido da tela de confirmação ("Excluir Almoço, R$ 20? Cancelar / Excluir"). Ele pergunta: "e se ela estiver sem internet?". Tainá anota como pergunta aberta para a arquitetura. O cartão vai para a coluna "Pronto para desenvolver" só depois que Tainá manda o critério para Bia confirmar por mensagem.
- **Objetivos de aprendizagem:** história de usuário com quem, o quê e para quê; critério Dado/Quando/Então com dados; caso limite; Definition of Ready.
- **Menus:**
  - Pedagógico 1, "Qual história vai para o cartão?" (`st_d09_historia`):
    - A: "Como estudante que lançou um gasto por engano, quero excluí-lo com uma confirmação, para que o total do mês volte a ser confiável." → acerto.
    - D1: "Como sistema, quero um botão Excluir na lista de gastos." → Tainá: "Descreve uma tela, não uma pessoa. Sem o 'para quê', ninguém sabe dizer se ela vale mais que outra."
    - D2: "Como usuário, quero um app fácil de usar." → Tainá: "Isso é um épico do tamanho do app. Não cabe numa semana e não tem como testar."
    - Revisão: "Reescrevo dizendo quem é a pessoa, a ação e o benefício."
  - Pedagógico 2, "Qual critério verifica a regra?" (`st_d09_criterio`):
    - A: "Dado um total mensal de R$ 100 com um gasto de R$ 20, quando a estudante confirmar a exclusão, o gasto sai da lista e o total passa a R$ 80." → acerto.
    - D1: "O app deve ter um painel moderno de educação financeira." → Davi: "Eu entrego um painel lindo e o total continua errado. Esse critério passa."
    - D2: "O botão Excluir deve ficar visível na lista." → Davi: "Confere que o botão existe, não o que acontece com o gasto e com o total depois."
    - Revisão: "Escrevo situação inicial, ação e resultado com valores."
  - Pedagógico 3, "Bia pergunta: e se eu tocar em Excluir e depois cancelar?" (`st_d09_limite`):
    - A: "O gasto permanece e o total continua R$ 100; confirmo isso com a Bia." → acerto.
    - D1: "O gasto some, mas o total só atualiza quando ela reabrir a tela." → Tainá: "Cancelar é desistir. Se o gasto some mesmo assim, a confirmação vira enfeite."
    - D2: "A janela fecha; não precisa conferir lista nem total." → Davi: "Fechar a janela não prova nada. Já vi app que apagava no fundo e só mostrava depois."
    - Revisão: "Registro o caso do cancelamento e o resultado esperado, e confirmo com a Bia."
  - **Conquista:** `st_conq_criterio` se `st_d09_criterio and st_d09_limite`.
  - Social, Davi convida para parear no protótipo à tarde:
    - "Bora!" → `st_mobile` +1.
    - "Hoje prefiro revisar os critérios sozinho, mas amanhã topo." → sem efeito; Davi: "Fechou, amanhã."
- **Variáveis:** `st_d09_historia`, `st_d09_criterio`, `st_d09_limite`, `st_conq_criterio`.
- **Notebook:** registro 4, "História, critério e caso limite".
- **Meta de palavras:** 650.

#### st_10_almoco · Marmita coletiva

- **Semana/horário:** semana 3, terça, 12h30 a 13h30.
- **Fundos:** `bg refeitorio_tarde` (copa do coworking).
- **Música:** `music_coffee_break_friendly`.
- **Presentes:** equipe completa; Vinícius passa rapidamente. Disponíveis: `st_estudante`.
- **Resumo:** Terça é dia de marmita coletiva na copa. A mesa se divide em duas rodas e o jogador escolhe onde sentar. Na roda de Otávio e Davi, a conversa é sobre o internet banking por SMS que Otávio ajudou a construir em 2004, onde "a mensagem chegava duas vezes e o saldo também". Na roda de Tainá e Lorena, Tainá conta por que saiu do banco ("eu atendia gente que achava que tinha perdido dinheiro, igual a Bia") e Lorena fala do teste de usabilidade com calouros. Falas extras aparecem com amizade alta (4 ou mais). Vinícius passa com um prato na mão, anuncia que conseguiu reunião com um fundo e sai.
- **Objetivos de aprendizagem:** integração; pistas para a arquitetura (mensagem duplicada) e para usabilidade.
- **Menus:**
  - Social, "Onde você senta?":
    - "Com Otávio e Davi." → `st_techlead` +1, `st_mobile` +1.
    - "Com Tainá e Lorena." → `st_mentora` +1, `st_qualidade` +1.
  - Submenu Otávio e Davi:
    - "Como vocês resolviam a mensagem duplicada?" → `st_techlead` +1. Otávio: "Mal. Um dia te conto a versão certa."
    - "Davi, você usaria SMS banking hoje?" → `st_mobile` +1.
  - Submenu Tainá e Lorena:
    - "O que você aprendeu no atendimento do banco?" → `st_mentora` +1.
    - "Como é um teste de usabilidade na prática?" → `st_qualidade` +1.
  - Falas condicionais: `get_friendship_point("st_techlead") >= 4` libera Otávio dizendo que gostou de ensinar alguém que pergunta; o mesmo padrão para os outros três.
- **Variáveis:** nenhuma nova.
- **Notebook:** nenhum registro.
- **Meta de palavras:** 450.

#### st_11_inspecao · Lupa no documento

- **Semana/horário:** semana 3, quarta, 14h00 a 19h30.
- **Fundos:** `bg startup_coworking_tarde` → `bg startup_coworking_noite`.
- **Música:** `music_office_focused_2`.
- **Presentes:** Tainá, Lorena. Disponíveis: `st_techlead`, `st_mobile`, `st_ceo`, `st_estudante`.
- **Resumo:** Tainá juntou as histórias e regras no documento "Especificação Trocado 1.0". Antes de passar para o desenvolvimento, Lorena conduz uma inspeção com um checklist curto: falta algo? dá para entender de dois jeitos? contradiz outra regra? dá para testar? O jogador inspeciona três requisitos e aponta o defeito de cada um. Depois, Tainá traz um pedido novo da Bia, corrigir o valor de um gasto, e pede que o jogador escreva requisito e critério sozinho. O jogo mostra a tela de escrita livre, a revisão do texto e a autoavaliação em três perguntas. A noite chega com o documento revisado.
- **Objetivos de aprendizagem:** inspeção de requisitos; defeitos ausente, ambíguo e inconsistente; ligação entre requisito e LGPD; produzir um requisito e um critério verificáveis.
- **Menus:**
  - Pedagógico 1, "RF03: O app deve alertar o estudante quando ele gastar muito." (`st_d11_ambiguo`):
    - A: "Ambíguo: 'muito' precisa de referência, por exemplo, ao atingir 80% do orçamento do mês." → acerto.
    - D1: "Inconsistente com outro requisito." → Lorena: "Não contradiz nada. O problema é que cada um entende 'muito' de um jeito: a Bia recebe alerta todo dia ou nunca."
    - D2: "Está bom, o dev escolhe o limite." → Tainá: "Aí o limite muda a cada versão e ninguém consegue testar se o alerta está certo."
  - Pedagógico 2, "RF05: Ao excluir um gasto, ele é removido da lista." (`st_d11_ausente`):
    - A: "Ausente: falta a confirmação, o cancelamento e o recálculo do total que combinamos com a Bia." → acerto.
    - D1: "Redundante com o RF04, que fala de editar gasto." → Lorena: "Editar e excluir são ações diferentes, com riscos diferentes."
    - D2: "Está completo e dá para testar." → Lorena: "Dá para testar e passar com o total errado. É exatamente o problema que a Bia contou."
  - Pedagógico 3, "RF08: Gastos excluídos ficam guardados para sempre para métricas" e "RNF02: ao excluir a conta, os dados financeiros do estudante são apagados em até 15 dias" (`st_d11_inconsistente`):
    - A: "Inconsistentes: o RF08 contradiz o RNF02. Precisamos decidir finalidade e prazo com o Otávio." → acerto.
    - D1: "O RF08 é só ambíguo; falta dizer onde guarda." → Lorena: "O lugar não resolve. Os dois não podem ser verdade ao mesmo tempo."
    - D2: "Não é problema, métrica é importante para o demo day." → Tainá: "Guardar dado financeiro sem finalidade e sem prazo vai contra a LGPD e quebra a promessa feita a quem apaga a conta."
  - Revisão de cada distrator: "Releio com a pergunta do checklist que encaixa e corrijo a frase." → Lorena mostra a versão corrigida.
  - **Escrita livre** (mecânica da demo): pedido "A estudante precisa corrigir o valor de um gasto. O novo valor deve ser maior que zero; ao confirmar, a lista e o total do mês devem refletir a alteração." Dois `renpy.input` (requisito até 300 caracteres; critério até 400), tela de revisão, e a autoavaliação de Tainá: "Ficou claro quem age e qual condição restringe? O exemplo tem dados iniciais e resultado observável? Há algo que deve ser recusado, como valor zero ou negativo?" Opções:
    - "Reescrever para esclarecer uma condição ou o resultado" → volta aos inputs.
    - "Conferi os pontos; guardar como rascunho para discutir" (só se os dois campos têm texto) → `st_escrita_concluida = True`.
    - "Continuar sem registrar o exercício" → `st_escrita_concluida = False`; pode ser retomado na cena 12.
    - O jogo declara que não avalia o significado do texto. Texto exibido com escape de `{` e `[`.
  - **Conquistas:** `st_conq_inspetor` se pelo menos 2 dos 3 defeitos foram acertados antes do feedback; `st_conq_rascunho` se `st_escrita_concluida`.
  - Social, fim da tarde:
    - "Agradeço à Lorena pelo checklist." → `st_qualidade` +1.
    - "Comento que é cansativo, mas útil." → sem efeito. Lorena: "Cansa menos do que consertar em produção."
- **Variáveis:** `st_d11_ambiguo`, `st_d11_ausente`, `st_d11_inconsistente`, `st_inspecao_acertos`, `st_escrita_requisito`, `st_escrita_criterio`, `st_escrita_concluida`, `st_conq_inspetor`, `st_conq_rascunho`.
- **Notebook:** registro 5, "Inspeção de requisitos".
- **Meta de palavras:** 750.

#### st_12_casa_sem3 · Rascunho na mesa

- **Semana/horário:** semana 3, sexta, 20h30 a 22h30.
- **Fundos:** `bg transito_noite` → `bg quarto_noite`.
- **Música:** `music_streets_focused` → `music_home_reflecting`.
- **Presentes:** ninguém. Disponíveis: `set_available("all")`.
- **Resumo:** No ônibus, o jogador lembra da frase de Lorena: "dá para testar e passar com o total errado". Em casa, revisa a especificação. Se o rascunho foi guardado, relê o próprio requisito e anota uma dúvida para levar à Bia. Se ficou pendente, o jogo oferece retomar a escrita agora, sem penalidade. Lorena manda no grupo uma foto do checklist de inspeção colado no monitor. Contatos. Card.
- **Card:** "Fim da Semana 3. Requisito bom tem quem, condição e resultado. Inspecionar antes de codar custa uma tarde; depois, custa um lançamento."
- **Menus:** se `not st_escrita_concluida`: "Retomar o rascunho agora" (chama o mesmo bloco de escrita da cena 11) / "Deixar para depois". `call screen contacts_screen`.
- **Variáveis:** `add_friendship_point("st_qualidade", 1)` pela mensagem.
- **Notebook:** nenhum registro novo.
- **Meta de palavras:** 300.

### Ato 4 · Arquitetura e gestão

#### st_13_arquitetura · Por que apareceu duas vezes?

- **Semana/horário:** semana 4, segunda, 10h00 a 17h00.
- **Fundos:** `bg startup_coworking_manha` → `bg startup_coworking_tarde`.
- **Artefatos:** `st_diagrama_arquitetura.png`.
- **Música:** `music_office_concentrated_2`.
- **Presentes:** Otávio, Davi, Tainá; Vinícius entra à tarde. Disponíveis: `st_qualidade`, `st_estudante`.
- **Resumo:** Otávio desenha a arquitetura: app mobile que guarda os lançamentos no celular e funciona sem internet, uma fila de sincronização, funções serverless na nuvem e um banco relacional gerenciado. Com o horário que o jogador mandou na semana 2, ele reproduz o bug: o app sem sinal reenvia o mesmo lançamento e o servidor cria um gasto novo a cada tentativa. O jogador escolhe a correção. Depois modelam os dados: Estudante, Gasto (id gerado no celular, valor em centavos, data, categoria, origem manual ou banco, criado em, excluído em), Categoria e Consentimento (instituição, escopos, validade, revogado em). Otávio lembra que dado financeiro é dado pessoal: não está na lista de "sensíveis" da lei, mas um vazamento expõe renda e hábitos, então guardar só o necessário. À tarde, Vinícius chega da reunião com o fundo: quer a importação bancária via Open Finance na versão 1.0. Davi explica o impacto: parceria com instituição autorizada, tela de consentimento com prazo, tratamento de falhas; incluir agora empurra a exclusão segura e a correção do duplicado para depois do semestre. O jogador conduz a negociação até um acordo registrado.
- **Objetivos de aprendizagem:** arquitetura mobile offline com sincronização; idempotência; modelagem de dados (valor monetário em inteiros, exclusão lógica com prazo, consentimento); negociação de mudança de escopo com impacto explícito.
- **Menus:**
  - Pedagógico 1, "Como evitar o gasto duplicado?" (`st_d13_idempotencia`):
    - A: "O celular gera um identificador único no momento do lançamento; o servidor ignora repetições com o mesmo id." → acerto. Otávio: "Isso tem nome: idempotência. Pode repetir à vontade, o resultado é o mesmo."
    - D1: "Bloquear lançamentos sem internet." → Davi: "A Bia lança no ônibus e no bandejão, onde o sinal some. Ela vai esquecer o gasto e o total fica errado para menos."
    - D2: "O servidor apaga gastos com mesmo valor e mesma data." → Otávio: "E os dois cafés de R$ 5 que a Bia toma no mesmo dia? Viram um. Trocamos um erro por outro."
    - Revisão: "Faço cada lançamento ter uma identidade própria desde o celular."
  - Pedagógico 2, "Como guardar o valor do gasto?" (`st_d13_valor`):
    - A: "Número inteiro em centavos: R$ 20,00 vira 2000." → acerto.
    - D1: "Número decimal de ponto flutuante." → Otávio: "Some 0,10 com 0,20 no computador e veja o que dá. Em mil lançamentos, o centavo some."
    - D2: "Texto, do jeito que aparece na tela: 'R$ 20,00'." → Davi: "Aí para somar eu converto tudo, e a ordenação põe R$ 100 antes de R$ 20."
    - Revisão: "Guardo em centavos inteiros e formato só na tela."
  - As duas decisões de arquitetura contam só para `st_acertos`; não há conquista própria.
  - Negociação (mecânica da demo, menu em laço `st_13_negociacao`):
    - Ruim 1: "Incluir a importação e manter o prazo sem falar de capacidade." → Davi: "Para caber, eu corto o teste do cancelamento e a correção do duplicado. A Bia continua vendo o almoço duas vezes." Vinícius: "Então eu mostraria uma novidade em cima de um total errado." `st_acordo_ruins += 1`, volta ao menu.
    - Ruim 2: "Recusar, porque a especificação já está fechada." → Vinícius: "O documento não é contrato com o universo. O fundo vai perguntar." Tainá: "A necessidade continua. Precisamos decidir quando investigar." `st_acordo_ruins += 1`, volta ao menu.
    - Acordo válido A, `st_acordo_opcao = "base_primeiro"`: "Entregar na 1.0 a exclusão segura e a correção do duplicado. A importação vira investigação: no demo day, mostramos o protótipo do consentimento como próximo passo, sem dados reais e sem data prometida."
    - Acordo válido B, `st_acordo_opcao = "investigar_agora"`: "Otávio investiga a parceria por uma semana agora; a data da 1.0 é renegociada, preservando a exclusão segura, o caso limite e a correção do duplicado. Se não couber antes do semestre, a importação fica para depois."
    - Conferência: "Rever o acordo antes de confirmar" (volta ao laço) / "Confirmar o acordo com Vinícius, Davi e Tainá" → `st_acordo_confirmado = True`, texto em `st_acordo_texto`.
  - **Conquista:** `st_conq_acordo` se `st_acordo_confirmado and st_acordo_ruins == 0`.
  - Social, fim do dia:
    - "Agradeço ao Otávio pela paciência em reproduzir o bug." → `st_techlead` +1. Otávio conta a "versão certa" da história do SMS duplicado.
    - "Pergunto ao Davi como ele vai montar a fila de sincronização." → `st_mobile` +1.
    - "Vou direto registrar a decisão no documento." → sem efeito; Tainá: "Registro de decisão é ouro daqui a seis meses."
- **Variáveis:** `st_d13_idempotencia`, `st_d13_valor`, `st_acordo_opcao`, `st_acordo_texto`, `st_acordo_ruins`, `st_acordo_confirmado`, `st_conq_acordo`.
- **Notebook:** registro 6, "Mudança de escopo se negocia".
- **Meta de palavras:** 750.

#### st_14_comemoracao · Mil estudantes

- **Semana/horário:** semana 4, sexta, 18h00 a 21h30.
- **Fundos:** `bg startup_terraco_noite` (novo) → `bg quarto_noite`.
- **Música:** `music_coffee_break_energized` → `music_home_dreamy`.
- **Presentes:** equipe completa e Vinícius. Disponíveis: `st_estudante`.
- **Resumo:** O beta passou de mil estudantes cadastrados graças ao boca a boca nas repúblicas. Vinícius encomenda pizza e a equipe sobe para o terraço do coworking, com varal de lâmpadas e vista para o Pão de Açúcar. O jogador ajuda a preparar a comemoração. Lorena comemora, mas lembra baixinho que cadastro não é retenção; Otávio concorda e diz que segunda isso entra na pauta. Vinícius pede que o jogador faça o brinde. Otávio comenta, longe do barulho, que startup cansa e que ninguém precisa provar nada virando a noite. O jogador volta para casa.
- **Card:** "Fim da Semana 4. Comemorar é importante. Saber o que o número mede também."
- **Objetivos de aprendizagem:** cultura de equipe; semente da métrica de vaidade (cadastros) para a cena 15; ritmo sustentável.
- **Menus:**
  - Social, "Como você ajuda na festa?":
    - "Monto a playlist com o Davi." → `st_mobile` +1.
    - "Escrevo no quadro os nomes dos beta testers que mais mandaram feedback, com a Bia no topo." → `st_qualidade` +1. Lorena se emociona.
    - "Preparo o guaraná com gelo e os copos para todo mundo." → `st_mentora` +1.
  - Social, o brinde:
    - "Aos mil, e aos que vão continuar usando." → `st_techlead` +1. Otávio ergue o copo: "Essa é a métrica certa."
    - "Ao time que me recebeu tão bem." → `st_mentora` +1.
    - "Ao próximo bug que a gente vai achar antes do usuário." → `st_qualidade` +1.
- **Variáveis:** nenhuma nova.
- **Notebook:** nenhum registro.
- **Meta de palavras:** 450.

#### st_15_gestao · Duas fichas, quatro pedidos

- **Semana/horário:** semana 5, segunda, 9h30 a 16h00.
- **Fundos:** `bg sala_reunioes_manha` → `bg startup_coworking_tarde` → `bg quarto_noite`.
- **Artefatos:** `st_quadro_kanban.png`, `st_painel_metricas.png`.
- **Música:** `music_office_focused` → `music_home_reflecting`.
- **Presentes:** equipe completa; Vinícius entra na parte das métricas. Disponíveis: `st_estudante`.
- **Resumo:** Planejamento do último ciclo antes do lançamento: faltam três semanas. Tainá mostra a capacidade real: Davi sozinho no app, Otávio dividido entre a API e os investidores (e, se `st_acordo_opcao == "investigar_agora"`, com uma semana tomada pela investigação da parceria). A correção do duplicado já está em andamento; cabem mais dois itens. O jogador monta o plano com 2 de 4 itens. Depois a equipe registra riscos. Vinícius chega para combinar qual métrica mostrar no demo day; o painel mostra cadastros subindo e retenção parada. Lorena propõe que a definição de pronto inclua o teste do caso limite e o texto do botão revisado para leitor de tela. A semana termina com o quadro atualizado e o jogador em casa.
- **Card:** "Fim da Semana 5. Capacidade é finita: escolher é dizer não com motivo. E métrica boa mostra se a vida de alguém melhorou."
- **Objetivos de aprendizagem:** planejamento por capacidade; prioridade ligada à necessidade confirmada; gestão de riscos com dono e gatilho; métrica de produto vs. métrica de vaidade; definição de pronto.
- **Menus:**
  - Pedagógico, planejamento (mecânica da demo, 2 de 4, `st_plano_*`): itens "Confirmar a exclusão e manter o gasto se a pessoa cancelar" (necessário), "Atualizar a lista e recalcular o total após excluir ou sincronizar" (necessário), "Medalhas por frequência de uso" (extra), "Compartilhar resumo de gastos nas redes sociais" (extra). Adicionar e retirar em laço; "Conferir este plano" com 2 itens. Feedback por cobertura: 2 → Tainá e, por mensagem, Bia confirmam; 1 → fala de Bia sobre o que falta; 0 → "eu ainda veria o almoço duas vezes". Revisão livre. `st_plano_primeira_cobertura` guarda a cobertura da primeira conferência.
  - Pedagógico 2, "Como tratar os riscos destas três semanas?" (`st_d15_riscos`):
    - A: "Registrar cada risco com dono, gatilho e plano: pico de cadastros no semestre (teste de carga), revisão das lojas (enviar com uma semana de folga) e textos de consentimento e privacidade (revisão do Otávio)." → acerto.
    - D1: "Resolver os riscos quando aparecerem; somos rápidos." → Davi: "A revisão da loja pode levar dias. Se for rejeitada na véspera, lançamos depois que os calouros já escolheram outro app."
    - D2: "Uma planilha com todos os riscos possíveis, sem dono." → Lorena: "Sessenta linhas que ninguém abre. Risco sem dono é decoração."
    - Revisão: "Escolho os riscos que podem atrasar o lançamento e dou um dono e um gatilho para cada um."
  - Pedagógico 3, "Que métrica Vinícius deve mostrar no demo day?" (`st_d15_metrica`):
    - A: "Retenção semanal (estudantes que voltam a lançar gastos) e quantos fecharam o mês com o total conferido." → acerto. Vinícius: "Isso responde a pergunta que todo fundo faz."
    - D1: "Total de downloads." → Lorena: "Sobe com anúncio e com festa de mil cadastros. Não mostra se o app ajudou alguém."
    - D2: "Número de funcionalidades entregues." → Otávio: "Mede nosso esforço, não o resultado de quem usa."
    - Revisão: "Escolho um número que mostre se o estudante voltou e confiou no total."
  - **Conquista:** `st_conq_foco` se `st_plano_primeira_cobertura == 2 and st_d15_metrica`.
  - Social, no fim do dia Tainá pergunta como o jogador está com a pressão:
    - "Sendo honesto: um pouco ansioso, mas o plano ajudou." → `st_mentora` +1. Tainá: "Obrigada por falar. Ansiedade dita em voz alta vira ajuste."
    - "Tranquilo!" → sem efeito. Tainá: "Se mudar, me fala."
- **Variáveis:** `st_plano_selecionados`, `st_plano_cobertura`, `st_plano_primeira_cobertura`, `st_plano_completo`, `st_d15_riscos`, `st_d15_metrica`, `st_conq_foco`.
- **Notebook:** registro 7, "Capacidade, riscos e métricas".
- **Meta de palavras:** 650.

### Ato 5 · Implementação

#### st_16_codificacao · Um PR pequeno

- **Semana/horário:** semana 6, terça, 10h00 a 19h00.
- **Fundos:** `bg startup_coworking_manha` → `bg startup_coworking_tarde` → `bg startup_coworking_noite` → `bg quarto_noite`.
- **Artefatos:** `st_app_gastos.png`.
- **Música:** `music_office_concentrated_1` → `music_home_reflecting`.
- **Presentes:** Davi, Otávio; Lorena no fim da tarde. Disponíveis: `st_mentora`, `st_ceo`, `st_estudante` (e `st_qualidade` até ela chegar).
- **Resumo:** O jogador pega o cartão "Excluir gasto com confirmação". Escolhe a abordagem de implementação; se escolher um distrator, Otávio mostra a consequência e orienta o caminho com testes. Enquanto isso, Davi abre o PR da fila de sincronização com id único e pede revisão do jogador. O diff tem um log que grava o e-mail do estudante, a descrição e o valor do gasto, e falta o teste de enviar o mesmo id duas vezes. O jogador escolhe o comentário. Davi revisa o PR do jogador e sugere trocar o nome de uma função; o jogador responde. No fim da tarde, Lorena testa os dois PRs num Android de entrada com rede lenta e modo avião: a exclusão e o cancelamento passam.
- **Card:** "Fim da Semana 6. Teste primeiro, PR pequeno, revisão com motivo."
- **Objetivos de aprendizagem:** testes guiando a implementação; PR pequeno; code review que aponta problema, motivo e sugestão; dados pessoais em logs.
- **Menus:**
  - Pedagógico 1, "Como você implementa o cartão?" (`st_abordagem`):
    - A: "Escrevo primeiro os testes do critério e do caso limite (R$ 100 vira R$ 80; cancelar mantém R$ 100) e abro um PR pequeno." → `st_abordagem = "teste_pr"`, acerto.
    - D1: "Codifico rápido e testo depois no celular do Davi." → `st_abordagem = "rapida"`. Otávio: "Lorena vai achar que o total não recalcula depois da sincronização. São dois dias de volta, na semana mais apertada."
    - D2: "Aproveito para reescrever a tela de gastos com uma biblioteca nova de animações." → `st_abordagem = "reescrever"`. Davi: "Vira um PR de 40 arquivos. Ninguém revisa direito e o cancelamento se perde no meio."
    - Revisão: "Começo pelos dois testes da Bia e deixo o PR do tamanho do cartão." → `st_abordagem = "teste_pr"`; Otávio: "Perdemos meio dia, não dois." `st_abordagem_primeira` guarda a primeira escolha.
  - Pedagógico 2, "Que comentário você deixa no PR do Davi?" (`st_d16_review`):
    - A: "O log grava e-mail, descrição e valor do gasto, que são dados pessoais. Sugiro registrar só o id e o status, e incluir um teste enviando o mesmo id duas vezes." → acerto. Davi: "Pô, nem vi. Corrigindo."
    - D1: "Aprovo: o CI passou e o Davi tem mais experiência." → Otávio: "Esse log iria para o serviço de monitoramento, fora da nossa base. Dado financeiro de mil estudantes num lugar que ninguém controla."
    - D2: "Comento 'isso está estranho, refaz'." → Davi: "Estranho onde? Sem dizer o problema e o motivo, eu fico chutando."
    - Revisão: "Aponto a linha, explico o risco e sugiro a correção."
  - **Conquista:** `st_conq_revisor` se `st_abordagem == "teste_pr"` na primeira escolha e `st_d16_review`.
  - Social, resposta ao review do Davi:
    - "Valeu, ajustei o nome." → `st_mobile` +1.
    - "Explico por que escolhi o nome e pergunto o que ele acha." → `st_mobile` +1. Davi: "Discussão boa. Fica o seu, com um comentário."
    - "Ajusto sem responder." → sem efeito. Davi: "Tudo certo, mas um 'ok' ajuda a fechar a conversa."
- **Variáveis:** `st_abordagem`, `st_abordagem_primeira`, `st_d16_review`, `st_conq_revisor`.
- **Notebook:** nenhum registro novo.
- **Meta de palavras:** 650.

#### st_17_testes_seguranca · Dados que não são nossos

- **Semana/horário:** semana 7, quarta, 9h00 a 19h00.
- **Fundos:** `bg startup_coworking_manha` → `bg startup_coworking_tarde` → `bg quarto_noite`.
- **Música:** `music_office_concentrated_2` → `music_home_reflecting`.
- **Presentes:** Lorena, Otávio. Disponíveis: `st_mentora`, `st_mobile`, `st_ceo`, `st_estudante`.
- **Resumo:** Lorena apresenta o plano de testes: muitos testes de unidade, alguns de integração com a API, poucos de ponta a ponta no celular, teste exploratório com modo avião, leitor de tela no botão Excluir e um teste de carga. O jogador define o cenário de carga. Otávio entra com segurança: mesmo que a importação bancária ainda seja investigação ou protótipo, a equipe precisa decidir agora onde guardar o token de acesso. Ele explica Open Finance: o estudante autoriza o compartilhamento na própria instituição, por consentimento com finalidade, prazo e possibilidade de revogar; ninguém digita senha do banco no app. Chega mensagem da Bia: "se eu apagar minha conta, meus gastos somem mesmo?". O jogador decide a resposta e o comportamento. Os testes de tarde acham um bug: o total não atualiza ao sair do modo avião. O jogador escolhe como pedir ajuda e o bug é corrigido.
- **Card:** "Fim da Semana 7. Teste o pico antes que ele chegue. Dado financeiro é emprestado: guarde pouco, proteja bem e devolva quando pedirem."
- **Objetivos de aprendizagem:** pirâmide de testes; teste de carga representativo; armazenamento seguro de credenciais no celular; Open Finance por consentimento; LGPD: finalidade, necessidade e eliminação; exigência das lojas de oferecer exclusão de conta.
- **Menus:**
  - Pedagógico 1, "Como testar o pico do início do semestre?" (`st_d17_carga`):
    - A: "Simular dez vezes os cadastros e lançamentos de um dia normal, concentrados no horário do almoço, medindo se a lista abre em até 2 segundos." → acerto.
    - D1: "Pedir para cinco colegas abrirem o app ao mesmo tempo." → Lorena: "Cinco pessoas não são o pico de mil calouros. O teste passa e não diz nada."
    - D2: "Não precisa: serverless escala sozinho." → Otávio: "As funções escalam; o banco não. Mil funções abrindo conexão ao mesmo tempo derrubam o banco."
    - Revisão: "Reproduzo o volume e o horário do pico e meço contra a meta de 2 segundos."
  - Pedagógico 2, "Onde guardar o token de acesso da importação bancária?" (`st_d17_token`):
    - A: "No armazenamento seguro do sistema do celular (Keychain no iPhone, Keystore no Android), com validade curta; o app nunca pede senha do banco." → acerto.
    - D1: "No armazenamento comum do app, para facilitar." → Otávio: "Qualquer backup ou celular desbloqueado expõe o token. Com ele, alguém lê o extrato da Bia."
    - D2: "Pedir a senha do banco e guardá-la criptografada no servidor." → Otávio: "Open Finance existe justamente para ninguém precisar da senha. Guardar senha de banco é o pior risco que a gente poderia criar, e quebra a confiança que a Bia pediu."
    - Revisão: "Uso o cofre do sistema e o consentimento da instituição, sem senha."
  - Pedagógico 3, "O que acontece quando a Bia apaga a conta?" (`st_d17_exclusao`):
    - A: "Apagar conta e dados financeiros no prazo do RNF02, revogar consentimentos, manter só o que a lei obriga, e explicar isso a ela." → acerto.
    - D1: "Desativar a conta, mas manter os gastos para métricas." → Otávio: "Contradiz o RNF02 e a LGPD. E as lojas exigem que app com cadastro ofereça exclusão de conta de verdade."
    - D2: "Apagar só do celular dela." → Lorena: "No servidor continua tudo. Ela acha que apagou e não apagou."
    - Revisão: "Apago nos dois lugares, revogo o consentimento e confirmo para a Bia."
  - **Conquista:** `st_conq_guardiao` se `st_d17_token and st_d17_exclusao`.
  - Social, o bug do modo avião:
    - "Peço à Lorena para reproduzirmos juntos." → `st_qualidade` +1.
    - "Peço ao Otávio para olhar os logs da sincronização comigo." → `st_techlead` +1.
    - "Tento sozinho até tarde." → sem efeito. Lorena, às 20h: "Pedir ajuda cedo é técnica, não fraqueza." O bug é corrigido no dia seguinte.
- **Variáveis:** `st_d17_carga`, `st_d17_token`, `st_d17_exclusao`, `st_conq_guardiao`.
- **Notebook:** registro 8, "Dados financeiros: LGPD e Open Finance".
- **Meta de palavras:** 650.

#### st_18_lancamento · Demo day

- **Semana/horário:** semana 8, segunda 9h00 (lojas) → quarta 12h00 (pico) → quinta 15h00 (demo day) → quinta 22h00 (casa).
- **Fundos:** `bg startup_coworking_manha` → `bg startup_coworking_tarde` → `bg transito_tarde` → `bg demo_day_auditorio` (novo) → `bg quarto_noite`.
- **Artefatos:** `st_painel_metricas.png`.
- **Música:** `music_office_motivated` → `music_office_concentrated_2` → `music_home_reflecting`.
- **Presentes:** segunda e quarta: equipe completa, disponíveis `st_ceo`, `st_estudante`. Quinta: todos presentes, `set_available()`. Casa: `set_available("all")`.
- **Resumo:** Segunda: a versão 1.0 está pronta e o jogador escolhe como lançar. A loja da Apple aprova; a do Google pede o caminho de exclusão de conta dentro do app. Se `st_d17_exclusao` foi acerto de primeira, o caminho já está no menu e a aprovação sai no mesmo dia; senão, a revisão orientada da cena 17 já o tinha criado e só falta um ajuste de meio dia. Quarta: começa o semestre e os cadastros sobem oito vezes no almoço. Se `st_d17_carga` foi acerto de primeira, o teste já tinha mostrado o limite de conexões e o app aguenta; senão, a lista fica lenta por vinte minutos até Otávio aplicar o limite de conexões que saiu da revisão. Quinta: a equipe vai de ônibus para o auditório da Aceleradora Maré. Antes do pitch, o jogador ajuda alguém da equipe. Vinícius apresenta a métrica combinada na cena 15 e o próximo passo do Open Finance conforme o acordo da cena 13. Bia sobe ao palco e conta o episódio do almoço duplicado, agora resolvido. O jogo calcula o final e os stakeholders e a equipe dão retorno. O jogador volta para casa.
- **Card:** "Fim da Semana 8."
- **Objetivos de aprendizagem:** publicação nas lojas e suas revisões; lançamento gradual com feature flag e monitoramento; resposta a pico; validação com stakeholders; ligação entre decisões antigas e o resultado.
- **Menus:**
  - Pedagógico, "Como liberar a 1.0?" (`st_d18_rollout`):
    - A: "Enviar às lojas com antecedência, liberar aos poucos (10%, depois 50%, depois 100%), deixar o que é novo atrás de feature flag e acompanhar falhas e o tempo de abertura da lista." → acerto.
    - D1: "Liberar para 100% na sexta à noite, antes do demo day, para os números subirem." → Otávio: "Se der problema, atinge todo mundo no fim de semana e não tem ninguém de plantão. E não dá para desfazer uma versão instalada."
    - D2: "Esperar o demo day passar para lançar com calma." → Tainá: "O semestre começa na quarta. É quando o estudante decide como vai controlar o dinheiro. Perdemos a janela."
    - Revisão: "Libero em etapas, com a novidade desligável e o painel aberto."
  - **Conquista:** `st_conq_lancamento` se `st_d18_rollout`.
  - Social, antes do pitch, "Quem você ajuda?":
    - "Ensaio a fala da Bia com a Tainá." → `st_mentora` +1.
    - "Confiro o painel de métricas com o Otávio." → `st_techlead` +1.
    - "Testo o celular da demo com o Davi." → `st_mobile` +1.
    - "Reviso com a Lorena se os slides têm contraste e legenda." → `st_qualidade` +1.
  - **Final** (ver seção 6): falas de Bia e Vinícius variam por `st_final_grade`; cada pessoa da equipe com amizade 6 ou mais diz uma fala pessoal; com `st_conq_equipe`, a equipe convida o jogador a voltar nas férias.
  - **Conquista:** `st_conq_equipe` se as quatro amizades da equipe forem 5 ou mais.
- **Variáveis:** `st_d18_rollout`, `st_conq_lancamento`, `st_conq_equipe`, `st_amizade_equipe`, `st_total_conquistas`, `st_final_grade`.
- **Notebook:** nenhum registro novo.
- **Meta de palavras:** 750.

**Total das metas:** 9.750 palavras.

## 4. Notebook de aprendizagem

| # | Flag | Título | Conteúdo | Cena |
|---|---|---|---|---|
| 1 | `st_reg_mvp` | MVP e ciclo curto | O ciclo de vida continua inteiro: descobrir, especificar, construir, testar, lançar, medir. Numa startup cada volta dura pouco. MVP é a menor versão que resolve um problema real e gera aprendizado com usuários; é pequeno no escopo, não na qualidade. Em app, cada versão passa pela revisão das lojas. | st_02 |
| 2 | `st_reg_elicitacao` | Da queixa ao requisito | Peça um episódio recente: quem, o que aconteceu, qual a consequência. Pergunta que oferece solução esconde o problema. Troque adjetivos ("fácil", "moderno") por tarefa e resultado observável. Em conflito, pergunte o resultado esperado por cada pessoa e procure o objetivo comum. | st_05 |
| 3 | `st_reg_tipos` | Tipos de requisito | Funcional: o que o sistema faz (testa executando). Não funcional: qualidade com medida, como "até 2 s em 95% das vezes no 4G". Restrição: regra externa, como LGPD, lojas e Open Finance. Ideia a validar: hipótese que ainda precisa de evidência. | st_06 |
| 4 | `st_reg_criterio` | História, critério e caso limite | História: "Como [quem], quero [ação], para [benefício]". Critério: dado [situação com valores], quando [ação], então [resultado verificável]. Caso limite: o que muda fora do caminho principal, como cancelar a exclusão e manter o total em R$ 100. | st_09 |
| 5 | `st_reg_inspecao` | Inspeção de requisitos | Antes de codar, leia com um checklist: falta algo (ausente)? dá para entender de dois jeitos (ambíguo)? contradiz outra regra (inconsistente)? dá para testar? Corrigir no documento custa uma tarde; em produção, custa um lançamento. | st_11 |
| 6 | `st_reg_mudanca` | Mudança de escopo se negocia | Pedido novo no meio do caminho não se aceita nem se recusa no impulso. Explique o impacto no que já foi combinado, ofereça caminhos (base primeiro, ou investigar e renegociar a data) e registre o acordo com quem pediu. | st_13 |
| 7 | `st_reg_metricas` | Capacidade, riscos e métricas | Capacidade é finita: escolha o que atende a necessidade confirmada. Risco precisa de dono, gatilho e plano. Métrica de produto mostra se a vida de quem usa melhorou (retenção, total conferido); downloads e número de funcionalidades são métricas de vaidade. | st_15 |
| 8 | `st_reg_lgpd` | Dados financeiros: LGPD e Open Finance | Dado financeiro é dado pessoal de alto risco. Guarde só o necessário, com finalidade e prazo; apague quando a pessoa excluir a conta. Open Finance funciona por consentimento na instituição, com prazo e revogação; o app nunca pede senha do banco. Tokens ficam no cofre do sistema do celular. | st_17 |

## 5. Conquistas

As conquistas são booleanas (`default False`). As oito marcadas como pedagógicas contam para `st_total_conquistas`. "Antes do feedback" significa que a primeira escolha foi a adequada; a revisão orientada não conta, mas também não tira nada.

| Flag | Nome | Cena | Condição | Pedagógica |
|---|---|---|---|---|
| `st_conq_escuta` | Ouvido de produto | st_05 | episódio concreto e esclarecimento de "fácil" antes do feedback | sim |
| `st_conq_criterio` | Dado, quando, então | st_09 | critério e caso limite antes do feedback | sim |
| `st_conq_inspetor` | Lupa de requisitos | st_11 | pelo menos 2 dos 3 defeitos antes do feedback | sim |
| `st_conq_rascunho` | Primeiro rascunho | st_11 ou st_12 | escrita livre guardada como rascunho após a autoavaliação | sim |
| `st_conq_acordo` | Acordo possível | st_13 | acordo válido confirmado sem passar por opção ruim | sim |
| `st_conq_foco` | Foco no MVP | st_15 | primeira conferência do plano cobre os 2 itens necessários e métrica adequada antes do feedback | sim |
| `st_conq_revisor` | Revisão que protege | st_16 | abordagem com testes e PR pequeno e comentário de review adequado, antes do feedback | sim |
| `st_conq_guardiao` | Guardião dos dados | st_17 | armazenamento do token e exclusão de conta antes do feedback | sim |
| `st_conq_lancamento` | Lançamento gradual | st_18 | rollout em etapas antes do feedback | não (bônus) |
| `st_conq_equipe` | Time Trocado | st_18 | amizade 5 ou mais com Tainá, Otávio, Davi e Lorena | não (bônus) |

Todas são alcançáveis em uma única partida.

## 6. Regra do final

- `st_amizade_equipe` = soma de `amizade_st_mentora`, `amizade_st_techlead`, `amizade_st_mobile`, `amizade_st_qualidade` (0 a 40). Stakeholders não entram.
- `st_total_conquistas` = número de conquistas pedagógicas (0 a 8).
- `st_final_grade`:
  - `"excelente"`: `st_amizade_equipe >= 20` e `st_total_conquistas >= 5`.
  - `"bom"`: `st_amizade_equipe >= 15` ou `st_total_conquistas >= 5`.
  - `"ok"`: nos demais casos.
- Proporção: os limites 20 e 15 são metade e três oitavos do máximo (40), como os 40 e 30 de 80 na saúde.
- **Pontos de amizade disponíveis sem chat:** 4 na apresentação, 3 automáticos (cenas 03, 08, 12) e até 18 em menus sociais (01, 02, 04, 06, 07 ×2, 09, 10 com 3 pontos, 11, 13, 14 ×2, 15, 16, 17, 18), total de 25. Um jogador que escolhe as opções sociais quase sempre chega a 20 sem chat; com conversas no celular nas cenas de casa passa com folga.
- **`st_conq_equipe` é alcançável sem chat**, por exemplo: Davi 7 (apresentação, 01, 02, 07 ×2, 09, 16), Lorena 7 (apresentação, 04, 06, 10 com Tainá e Lorena, 11, 12, 14 primeiro menu), Tainá 6 (apresentação, 03, 10 mesa e submenu, 15, 18), Otávio 5 (apresentação, 08, 13, 14 brinde, 17).
- **Recomendação para a F2:** limitar o +1 do chat offline a uma vez por personagem por cena, para não permitir acumular pontos abrindo o mesmo contato várias vezes.
- **Falas por resultado:**
  - Excelente: Bia diz que voltou a confiar no total e indicou o app para a república inteira; Vinícius conta que um fundo pediu uma segunda reunião por causa da retenção; Tainá diz que o jogador "ouviu antes de construir".
  - Bom: Bia diz que o total está certo, mas ainda quer ver o modo offline mais claro; Vinícius fica satisfeito e pede que o jogador ajude no próximo ciclo; Lorena lista duas melhorias.
  - Ok: Bia agradece, mas diz que vai continuar conferindo no caderno por enquanto; Vinícius diz que o pitch foi bom, mas a retenção ainda não convence; Tainá lembra que o próximo ciclo começa segunda e que dá para fazer melhor.

## 7. Variáveis novas

Todas com prefixo `st_` e um único `default` (F2). Ids de personagem não precisam de prefixo nas variáveis por personagem: seguem o padrão existente (`contato_st_mentora`, `disponivel_st_mentora`, `amizade_st_mentora`).

| Variável | Default | Cena | Uso |
|---|---|---|---|
| `st_acertos` | 0 | todas | escolhas adequadas antes do feedback (máximo 24: 02, 04, 05 ×3, 06 ×3, 09 ×3, 11 ×3, 13 ×2, 15 ×2, 16 ×2, 17 ×3, 18) |
| `st_viu_duplicado` | False | 03 | o jogador viu o duplicado no túnel; lido na 13 |
| `st_d02_mvp`, `st_d04_roteiro` | False | 02, 04 | decisões |
| `st_d05_episodio`, `st_d05_ambiguidade`, `st_d05_conflito` | False | 05 | decisões |
| `st_d06_funcional`, `st_d06_nao_funcional`, `st_d06_ideia` | False | 06 | decisões |
| `st_classif_acertos` | 0 | 06 | 0 a 3 |
| `st_d09_historia`, `st_d09_criterio`, `st_d09_limite` | False | 09 | decisões |
| `st_d11_ambiguo`, `st_d11_ausente`, `st_d11_inconsistente` | False | 11 | decisões |
| `st_inspecao_acertos` | 0 | 11 | 0 a 3 |
| `st_escrita_requisito`, `st_escrita_criterio` | "" | 11, 12 | texto do jogador |
| `st_escrita_concluida` | False | 11, 12 | rascunho guardado |
| `st_d13_idempotencia`, `st_d13_valor` | False | 13 | decisões |
| `st_acordo_opcao` | "" | 13 | "base_primeiro" ou "investigar_agora"; lido na 15 e 18 |
| `st_acordo_texto` | "" | 13 | texto do acordo |
| `st_acordo_ruins` | 0 | 13 | opções ruins escolhidas |
| `st_acordo_confirmado` | False | 13 | acordo confirmado |
| `st_plano_itens` | [] | 15 | os 4 itens |
| `st_plano_selecionados` | [] | 15 | índices escolhidos |
| `st_plano_cobertura`, `st_plano_primeira_cobertura` | 0, -1 | 15 | cobertura atual e da primeira conferência |
| `st_plano_completo` | False | 15 | plano conferido |
| `st_d15_riscos`, `st_d15_metrica` | False | 15 | decisões |
| `st_abordagem`, `st_abordagem_primeira` | "" | 16 | abordagem final e primeira escolha |
| `st_d16_review` | False | 16 | decisão |
| `st_d17_carga`, `st_d17_token`, `st_d17_exclusao` | False | 17 | decisões; carga e exclusão lidas na 18 |
| `st_d18_rollout` | False | 18 | decisão |
| `st_reg_mvp` … `st_reg_lgpd` | False | ver seção 4 | registros descobertos |
| `st_conq_*` (10) | False | ver seção 5 | conquistas |
| `st_amizade_equipe`, `st_total_conquistas` | 0 | 18 | cálculo do final |
| `st_final_grade` | "" | 18 | "excelente", "bom" ou "ok" |

Para o resumo de aprendizagem no epílogo: "Você fez X de 24 escolhas adequadas antes do feedback", mais o acordo (`st_acordo_texto`) e o estado do rascunho.

## 8. Arte

Estilo igual ao existente: sprites PNG RGBA 1024x1536, corpo inteiro em pé, figura do topo (y≈30) até perto da base (y≈1500), contorno fino escuro, cel shading com 1 a 2 tons de sombra, olhos grandes escuros com brilho, nariz mínimo, paleta natural levemente dessaturada, fundo transparente com halo suave. A expressão vem da pose. Retratos saem por recorte da pose neutra. Fundos PNG 1536x1024 na família `escritorio_interior` (ilustração anime com contorno de tinta, grão leve, figurantes de costas, sem texto legível), com variantes de horário: manhã azul-petróleo frio com luz amarelada, tarde laranja e magenta, noite azul-marinho quase monocromático.

### 8.1 Personagens

**Tainá Duarte (`st_mentora`).** Mulher de 33 anos, parda, pele morena média tom caramelo, rosto oval, sorriso largo. Cabelo cacheado volumoso castanho-escuro preso num coque alto (puff), com cachos soltos na testa. Brincos de argola dourados médios. Camisa jeans clara de manga dobrada, aberta sobre camiseta branca com um pequeno símbolo de moeda coral no peito (sem texto); calça de alfaiataria verde-oliva cropped; tênis brancos; cordão de crachá coral no pescoço. Carrega um caderno de capa laranja com post-its saindo das páginas. Altura média, postura aberta e firme.
- `neutral`: em pé, sorriso aberto, mão direita estendida à frente em gesto de boas-vindas, palma para cima; mão esquerda segura o caderno junto ao quadril.
- `thinking`: cabeça levemente inclinada, olhar para cima e para o lado, a ponta de uma caneta encostada no queixo com a mão direita; o caderno aberto apoiado no antebraço esquerdo.
- `serious`: braços cruzados prendendo o caderno contra o peito, peso numa perna só, sobrancelhas retas e boca fechada, olhar direto.

**Otávio Ramos (`st_techlead`).** Homem negro de 50 anos, pele escura, alto e robusto. Cabeça raspada, barba curta grisalha bem aparada, óculos de armação redonda de metal fino. Camisa polo azul-marinho sob cardigã cinza-chumbo aberto; calça chino cáqui; sapatênis marrom; relógio analógico de pulseira de couro no pulso esquerdo. Segura uma caneca esmaltada branca com borda azul. Postura calma, ombros relaxados.
- `neutral`: segura a caneca com a mão direita na altura do peito, mão esquerda no bolso da calça, leve sorriso de canto.
- `thinking`: ajusta os óculos com polegar e indicador da mão esquerda, braço direito cruzado na frente do corpo apoiando o cotovelo esquerdo, olhar para baixo, caneca na mão direita.
- `serious`: ereto, as duas mãos atrás das costas, queixo levemente abaixado, olhar firme por cima dos óculos, boca reta.

**Davi Matsuda (`st_mobile`).** Homem nipo-brasileiro de 24 anos, pele clara amarelada, magro, altura média. Cabelo preto liso com franja longa repartida ao meio e laterais curtas; sem barba. Moletom oversized cinza-mescla com capuz e um pequeno robô estampado no peito; camiseta preta por baixo aparecendo na barra; calça cargo preta; tênis de cano alto vermelhos. Fones de ouvido grandes pretos pendurados no pescoço. Celular Android em capinha transparente com adesivos. Postura animada, um pouco curvada.
- `neutral`: acenando com a mão direita aberta na altura do ombro, celular na mão esquerda, sorriso largo mostrando os dentes.
- `thinking`: olha para a tela do celular segurado com as duas mãos na altura do peito, polegar sobre a tela, cabeça inclinada, boca de lado.
- `serious`: mãos enfiadas no bolso canguru do moletom, ombros levemente erguidos, olhar de lado, boca reta, concentrado e sem graça.

**Lorena Bezerra (`st_qualidade`).** Mulher branca de 30 anos, pele clara com sardas no nariz e nas bochechas, cabelo ruivo-acobreado curto em corte pixie com a lateral esquerda raspada. Óculos de armação grossa verde-água, piercing pequeno de argola na narina direita, tatuagem fina de ramo de flores no antebraço esquerdo. Jardineira jeans escura sobre camiseta listrada branca e azul-marinho; tênis de lona amarelo-mostarda; bolsa transversal pequena marrom. Segura um tablet com capa laranja. Postura ereta e atenta.
- `neutral`: tablet seguro junto ao quadril pela mão esquerda, mão direita fazendo sinal de positivo, sorriso tranquilo.
- `thinking`: tablet apoiado no antebraço esquerdo, indicador direito tocando a tela, olhar concentrado para o tablet, lábios contraídos.
- `serious`: tablet abraçado contra o peito com os dois braços, sobrancelhas levemente franzidas, olhar direto para a frente.

**Vinícius Prado (`st_ceo`).** Homem branco de 36 anos, altura média-alta, magro atlético. Cabelo castanho-claro ondulado penteado para trás com volume, barba por fazer, olhos castanhos. Colete acolchoado sem mangas azul-petróleo sobre camisa social branca de manga dobrada até o cotovelo; calça jeans escura justa; tênis brancos de couro; smartwatch preto. Postura de palco, peito aberto.
- `neutral`: braços abertos à frente na altura da cintura, palmas para cima, como quem apresenta algo; sorriso confiante.
- `thinking`: mão direita no queixo, cotovelo apoiado no braço esquerdo cruzado à frente do corpo, sobrancelha erguida, olhar para cima.

**Beatriz Tavares, Bia (`st_estudante`).** Mulher indígena de 20 anos (povo Baré), pele morena acobreada, rosto arredondado, olhos escuros amendoados. Cabelo preto liso e longo até a cintura com franja reta. Brincos de sementes de açaí e pulseira de miçangas coloridas. Camiseta larga amarela com um brasão genérico sem texto, calça jeans clara, tênis gastos. Mochila de uma alça pendurada no ombro direito com chaveiro de boto-cor-de-rosa; garrafa d'água presa na lateral. Postura simples, um pouco reservada.
- `neutral`: segura a alça da mochila com a mão esquerda e mostra a tela do celular para a frente com a mão direita, sorriso tímido.
- `thinking`: braços cruzados frouxos, celular numa das mãos, olhar de lado, lábios apertados, expressão desconfiada.

### 8.2 Fundos

**Reaproveitados:** `transito_manha`, `transito_tarde`, `transito_noite`, `quarto_noite`, `cozinha_noite`, `sala_reunioes_manha`, `sala_reunioes_tarde`, `empresa_cafe_tarde`, `refeitorio_tarde`.

**Novos (5 de no máximo 6):**

| Arquivo | Define | Descrição | Cenas |
|---|---|---|---|
| `images/bg/startup_coworking_manha.png` | `bg startup_coworking_manha` | Coworking no segundo andar de um casarão antigo reformado: pé-direito alto, piso de taco, paredes de tijolo aparente pintadas de branco, janelas altas em arco com venezianas verdes abertas para árvores. Uma mesa longa compartilhada de madeira clara com notebooks, celulares de teste num suporte, canecas e plantas em vasos. À esquerda, uma parede de vidro com um quadro Kanban de post-its coloridos (sem texto legível). Ao fundo, sofá verde e uma bicicleta encostada. Luz da manhã fria azul-petróleo entrando pelas janelas com faixas amareladas no piso. Dois figurantes de costas. | 01, 04, 06, 09, 13, 16, 17, 18 |
| `images/bg/startup_coworking_tarde.png` | `bg startup_coworking_tarde` | Mesmo enquadramento, luz de fim de tarde laranja e magenta entrando pelas janelas em arco, sombras longas, post-its mais saturados, um figurante guardando o notebook. | 06, 11, 13, 15, 16, 17, 18 |
| `images/bg/startup_coworking_noite.png` | `bg startup_coworking_noite` | Mesmo enquadramento à noite: azul-marinho quase monocromático, janelas escuras com reflexo, luminárias pendentes amarelas acesas só sobre a mesa, monitores com brilho frio, cadeiras vazias. | 11, 16 |
| `images/bg/startup_terraco_noite.png` | `bg startup_terraco_noite` | Terraço do casarão à noite: deck de madeira, varal de lâmpadas amarelas, mesas baixas com caixas de pizza e copos, puffs, plantas em vasos, guarda-corpo de ferro. Ao fundo, silhueta do Pão de Açúcar e prédios iluminados de Botafogo sob céu azul-marinho. Figurantes de costas conversando. | 14 |
| `images/bg/demo_day_auditorio.png` | `bg demo_day_auditorio` | Auditório pequeno de uma aceleradora: palco baixo com púlpito, telão grande atrás exibindo um gráfico genérico de linha subindo (sem texto), plateia de cadeiras pretas com figurantes de costas, holofotes, faixa lateral com padrão geométrico azul e laranja sem palavras. Luz de tarde quente misturada com o brilho frio do telão. | 18 |

### 8.3 Telas e artefatos (4 de no máximo 4)

| Arquivo | Descrição | Cenas |
|---|---|---|
| `images/artifacts/st_app_gastos.png` | Duas telas de celular lado a lado, estilo mockup limpo. À esquerda, a lista de gastos do mês: cabeçalho "Outubro", total "R$ 100,00" em destaque, itens "Almoço R$ 20,00", "Bandejão R$ 4,50", "Ônibus R$ 4,30", "Café R$ 5,00", cada um com ícone de categoria e ícone de lixeira. À direita, a mesma tela escurecida com uma caixa de confirmação "Excluir Almoço, R$ 20,00?" e botões "Cancelar" (contorno) e "Excluir" (coral). Paleta coral, branco e verde-menta; fonte sem serifa; textos em português. | 01, 09, 16 |
| `images/artifacts/st_quadro_kanban.png` | Quadro Kanban digital com cinco colunas: "Descoberta", "Pronto para desenvolver", "Fazendo (limite 2)", "Revisão", "Pronto". Cartões com títulos curtos em português: "Excluir gasto com confirmação", "Total recalculado após sincronizar", "Gasto duplicado no offline", "Importação bancária (investigar)", "Medalhas", "Revisar textos de privacidade". Avatares circulares pequenos com as cores dos personagens. | 02, 15 |
| `images/artifacts/st_diagrama_arquitetura.png` | Diagrama de arquitetura em estilo quadro branco limpo: celular com "Banco local" e "Fila de sincronização" → seta "HTTPS + id único" → nuvem "Funções da API" → cilindro "Banco relacional". Caixa lateral tracejada "Instituição parceira (Open Finance)" ligada por seta pontilhada "consentimento". Ao lado, quatro entidades: "Estudante", "Gasto (id, valor_centavos, data, categoria, origem, excluido_em)", "Categoria", "Consentimento (escopos, validade, revogado_em)". | 13 |
| `images/artifacts/st_painel_metricas.png` | Painel de métricas de produto: cartões "Cadastros 1.000", "Retenção 30 dias 22%", "Nota na loja 3,4", "Sessões sem falha 98,7%"; gráfico de linha de cadastros subindo e gráfico de retenção caindo e depois subindo levemente; destaque de um pico marcado "Início do semestre". | 01, 15, 18 |
