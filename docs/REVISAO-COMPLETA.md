# Revisão da campanha conectada — 1.3

O encerramento da versão 1.2 foi prematuro em relação ao pedido: só o laboratório tinha uma campanha própria. Esta continuação transforma os casos de gastos e chamados em atividades diferentes, conecta os retornos e acrescenta a vida de estudante. O relato abaixo separa implementação de avaliação humana; não declara qualidade profissional comprovada por testes automatizados.

## Cada ponto do pedido

| Aspecto | O que mudou no jogo | Limite ou próximo teste |
|---|---|---|
| Mecânicas | Laboratório executa passos ordenáveis; gastos manipula lista/total; chamados compara perspectivas, publicação e histórico | São modelos pequenos e deliberados, não programação livre |
| Criar coisas | Montagem de interface por arrastar ou selecionar/posicionar três módulos; a tela funcional usa a ordem escolhida | O jogador reorganiza componentes; não desenha qualquer aplicativo |
| Point and click | Objetos de investigação com fonte e registro; mapas oferecem hotspots e listas equivalentes | Não há exploração por caminhada ou física |
| Mapa | Hub conecta universidade, startup e atendimento; cidade opcional leva ao campus e à oficina | Alguns deslocamentos são transições de cena |
| Side quests | Cópia offline, edição de gasto, escala do turno, oficina e agenda estudantil | Nenhuma pista essencial depende de pagar tempo num curso opcional |
| Agência | Plano altera calendário, interface muda ordem real, publicação muda quem vê o quê, acordo registra responsável | Parte das correções ainda é orientada; testar se a ajuda chega cedo demais |
| Memória | Resultados por projeto, fontes, escopo, promessa e layout arquivados no save; callbacks retomam fatos | Nova partida reinicia; preferências globais não guardam decisões da história |
| Continuidade | Hub entre capítulos; retornos, versões de teste e entregas distinguidos; revisitar substitui só o resultado desse projeto ao concluir | A ordem dos projetos é livre; não há calendário global simulando todas as semanas |
| Progresso | Registro de projetos e próximos cuidados, ensaios observáveis, antes/depois, fim conjunto | Contagem de retornos não representa competência ou sucesso de todas as entregas |
| Narrativa e diálogos | Lia tem identidade própria; Rodrigo participa do atendimento; Sabrina acompanha decisões e limites de agenda | Naturalidade e ritmo precisam de leitura/jogo com pessoas; revisão editorial não basta |
| Escolhas e finais | Laboratório tem quatro famílias; gastos distingue pesquisa, ensaio pendente, correção e recuperação; chamados preserva revisão, acompanhamento, reabertura e repasse pendente | Não somar combinações como se fossem capítulos inteiramente escritos |
| Arte e tempo | 29 novos arquivos: 18 fundos/variantes, seis sprites, quatro objetos e uma moldura de diálogo. Os cinco NPCs têm roupa alternativa; relógio das cenas seleciona luz/clima coerentes | Variações cobrem os horários usados no roteiro, não todas as combinações possíveis de clima/local. Artes antigas mantêm os registros de origem anteriores |
| Feedback | Seleção visível, posição dos módulos, estados públicos/internos, total e histórico; documentos claros, moldura de diálogo e transições que respeitam preferências | Não há nova trilha ou sistema de efeitos sonoros nesta rodada |
| Vida de estudante | Duas noites, disponibilidade da oficina, conflito preserva agenda, acordo com Sabrina e colega; curso concluído ocupa sua noite | É uma semana opcional, não simulador de semestres, notas ou produtividade |
| Documentos e mensagens | Mochila e notebook com dossiês e caixa de entrada simulada; mensagens derivadas dos projetos iniciados, retornos e acordos reais da partida | Acessos integrados e testes dirigidos do notebook aprovados; a consolidação da suíte final continua pendente. Não há e-mail externo |
| Duração e engajamento | Mais ações e rotas para experimentar, com fontes e curso opcionais | Duração por ato, abandono, interesse e vontade de repetir não foram medidos |
| Aprendizagem | Evidência→regra→teste, transação, regressão, escopo, dependência, revisão, comunicação e adoção são praticados | Não cobre toda engenharia de software nem comprova transferência para trabalho real |

## Forças e fragilidades após a expansão

O ponto forte agora é a cadeia observável entre decisão e comportamento. O jogador pode mostrar uma gravação indevida, ver o total mudar, cancelar uma operação, comparar o que suporte e solicitante enxergam e rever sua própria interface. Erro tem recuperação e não depende de pontuação escondida.

A maior fragilidade de design é a orientação intensa em partes das bancadas: instruções já sugerem a correção. Isso pode ajudar iniciantes e reduzir a descoberta. Uma rodada com participantes deve observar se eles formulam hipóteses ou apenas seguem controles. Reduzir explicações antes de aumentar o número de enigmas será a primeira intervenção se o fluxo parecer um exercício escolar.

O jogo não foi validado como “divertido” por agentes. Também não há evidência de uma duração de 60–90 minutos. Contar palavras, menus ou casos de teste não responde essas perguntas. As sugestões de avaliação abaixo tornam a próxima revisão verificável.

## Revisões e correções concretas

Exploradores e implementadores Sol/high trabalharam em módulos separados; Astra/high revisou domínio, narrativa e continuidade. A coordenação integrou código, arte, testes e inspeção visual.

- Repor amostra recupera várias exclusões e reinicia os critérios, sem apagar fontes ou escolhas.
- Motivo livre de reabertura continua em investigação. Só um caso simulado identificado recebe a correção prevista para ele.
- Confirmação de uso entra no histórico e não duplica eventos.
- Arquivo do laboratório preserva responsável e marco, incluindo correção sem dono.
- Retorno de chamados distingue publicação, revisão, recuperação e acompanhamento, sem confundir ontem/hoje.
- Edições em telas longas usam retenção do estado ao carregar; testes incluem save durante atividade, além de save em diálogo.
- Curso concluído ocupa quinta e não permite reutilizar a mesma noite para plantão.
- Campus e oficina ganharam cenários próprios; objetos clicáveis correspondem à arte.
- Painéis receberam correções de navegação e rolagem após testes no motor.
- Horário, relógios desenhados e iluminação foram comparados. O despertador foi corrigido para 08h/20h; suporte usa 14h30, 09h e 10h10 na chuva.
- Os cinco NPCs têm uma roupa alternativa integrada aos retornos. Após renegociar o projeto de gastos, Lia e Júlio conservam a roupa do novo encontro durante a revisão.
- Objetos clicáveis são sprites transparentes separados, com brilho ao hover/foco e rótulos pequenos. A lista equivalente permanece; a interação não depende de enxergar apenas uma diferença de cor.
- A primeira composição duplicava laptop, celular e caderno já pintados. Foram produzidas bases da mesa sem esses objetos, preservando os originais e a geometria da sala.
- Caixas de diálogo ganharam margens e altura menor; nomes deixaram de competir com a fala. Texto maior conserva espaço próprio.
- O próximo marco do laboratório agora muda para a reunião da coordenação após o retorno realizado, sem arquivar a reunião corrente como compromisso futuro.

Referências técnicas consultadas: [drag-and-drop do Ren'Py](https://www.renpy.org/doc/html/drag_drop.html) e [salvar, carregar e rollback](https://www.renpy.org/doc/html/save_load_rollback.html). A execução usa o SDK local 8.5.3.

## Documentos e interfaces das atividades

O menu principal passa a usar **Novo jogo** para a campanha. A jornada anterior permanece em **Extras → Demo guiada anterior**. Essa mudança evita duas entradas concorrentes para começar a história; o legado continua disponível para comparação.

A revisão visual mantém a moldura externa do jogo e dá identidade ao artefato usado em cada atividade:

- Requisitos: ficha com ID, fonte vinculada, regra e registros de ensaio. Uma hipótese sem apoio continua identificada como hipótese.
- Planejamento: quadro em formato Kanban, com o escopo escolhido e os limites da rodada. A aparência do quadro não acrescenta capacidade à equipe.
- Agenda: equipamento, horário, reserva anterior e tentativa são campos da interface; resultado e regra permanecem ligados ao plano.
- Gastos: recibo em papel e planilha com colunas, linhas numeradas, identificadores, descrição, valor e ação. Confirmar, cancelar e desfazer continuam usando os dados do caso.
- Chamados: fila com as três pessoas e impactos, bancada de revisão, perspectiva interna, portal da solicitante e histórico em cartões de mensagem.
- Montagem: módulos claros e prévia de aplicativo; os três slots continuam operáveis por arrastar ou seleção e posição.

As células, textos e ações são desenhados pelo Ren'Py. Não foram geradas imagens contendo telas de software ou controles fictícios. As pastas de consulta usam papel claro e seções para comparar fontes, escopo e compromisso sem editar o plano.

A mochila abre o notebook. Documentos levam aos dossiês; a caixa de entrada simula convites, demandas, retornos e acordos a partir do estado existente. Um retorno só aparece se houver resultado arquivado; mudanças de resultado ou acordo produzem uma versão correspondente da mensagem. Ler uma mensagem não equivale a entregar o projeto. Os acessos estão integrados. Três casos dirigidos do notebook passaram, incluindo consulta e mensagens vinculadas ao estado da partida. A suíte completa e o pacote continuam sujeitos à verificação final da rodada.

A moldura editorial em verde petróleo e cobre é um PNG transparente separado do texto e do fundo de leitura. Origem, dimensões e recorte estão em [ARTES-UI.md](ARTES-UI.md). Sua inclusão leva o pacote a 29 arquivos novos de arte: 18 fundos, seis sprites, quatro objetos e uma moldura.

O portfólio reúne capturas reais de menu, mochila, documentos, caixa de entrada, mensagem, dossiê, requisitos, Kanban e agenda. Alguns estados são preparados para inspeção. As capturas anteriores continuam identificadas; nenhuma captura isolada comprova o fluxo completo ou a aprendizagem.

## Próxima revisão com jogadores

Usar sessões consentidas, sem telemetria obrigatória e sem explicar a solução antes da atividade. Registrar em papel ou arquivo local: tempo por ato, pedidos de ajuda, ações tentadas, momentos de interesse e vontade espontânea de continuar. Preservar observação separada da interpretação.

1. Pedir uma partida de um projeto; observar a primeira decisão significativa e se a pessoa encontra objetos, próximo passo, salvar e voltar.
2. Perguntar qual decisão mudou o produto, quem percebeu e o que continua pendente. Pedir para mostrar a prova na tela.
3. Oferecer outro projeto ou estratégia sem obrigação. Registrar aceitação e motivo; recusa por falta de tempo não é desinteresse.
4. Apresentar caso novo: duas inscrições simultâneas na última vaga de um curso. Pedir uma fonte, regra, teste e limitação. Não premiar repetição literal do exemplo do laboratório.
5. Comparar se a pessoa distingue publicação de resultado, recuperação de desfazer e responsabilidade de “mandar para a equipe”.
6. Priorizar três problemas observados, corrigir e repetir com participantes novos; algumas pessoas anteriores ajudam a conferir a correção.

Relatar contagens brutas e exemplos, sem tratar uma pequena amostra qualitativa como certificação. O objetivo é encontrar fricção e oportunidades de diversão, não aprovar o jogo por simpatia.

## Evidência técnica

Em 09/11/2026, no SDK Ren'Py 8.5.3 para Windows:

- Suíte completa, incluindo capturas de inspeção: 90 casos e 627 asserções passaram.
- Regras e regressões em Python: 73 testes passaram.
- Notebook: abrir/fechar documentos sem sair da atividade, leitura idempotente, salvar/carregar e novas versões de retorno estão cobertos no motor.
- Texto livre dos chamados: chaves e colchetes aparecem literalmente no histórico, encerramento e email; o estado conserva o texto original.
- Portfólio local: conferido em 1440×1000 e 390×844, sem transbordamento horizontal ou imagens ausentes. Ampliação de imagem e fechamento por Esc funcionaram.

A conferência compacta e do pacote Windows está em conclusão. As capturas foram inspecionadas; não são baselines de comparação aprovadas automaticamente. Nenhum desses resultados mede diversão ou aprendizagem humana. O estado de execução está em [CONTINUACAO-CAMPANHA.md](CONTINUACAO-CAMPANHA.md); o portfólio está em [portfolio/index.html](portfolio/index.html).
