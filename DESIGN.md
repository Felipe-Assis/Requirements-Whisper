# Direção visual

## Campanha conectada

Os minijogos devem parecer as ferramentas que o personagem está usando. A moldura externa é do jogo; por dentro, requisitos usam papel claro com ID/regra/fonte, planejamento usa backlog, gastos usa planilha/aplicativo e chamados usa fila com histórico e visão do solicitante. A bancada de desenvolvimento apresenta sequência e resultados como editor e relatório. Não são imagens decorativas de interfaces: os campos e registros exibem o estado real da atividade. Controles sem função não são acrescentados para imitar software.

Paleta interna: papel `#f4f0e6`, superfície `#ffffff`, tinta `#23343b`, texto secundário `#52656b`, barra `#dce6e5`, ação `#286b66`. Cor não indica automaticamente a resposta correta. `artifact_*` mantém os mesmos alvos de teclado e a preferência de texto ampliado. Barras e cabeçalhos entram na área rolável quando necessário, sem encobrir ações essenciais.

A interação nos cenários usa PNGs transparentes separados: caderno, prancheta, celular e laptop. `scene_object` aplica brilho ao hover ou foco de teclado; não anima nem pulsa continuamente. Os rótulos são discretos e a lista equivalente continua disponível. Conversas e destinos usam marcadores pequenos. As caixas de diálogo têm margens laterais, carvão esverdeado `#192c32` e texto quente `#f5f0e7`; o tamanho normal é 34, nomes 32 e leitura ampliada 42. As atividades conservam painéis próprios para dados densos.

`campaign_clock` guarda local, marco, hora e variante de iluminação; salvar/carregar preserva esse conjunto. O relógio é narrativo por cena e por caso, sem cronômetro nem calendário global. Cada NPC com sprite tem roupa alternativa nos retornos. Variantes de clima preservam a arquitetura e o mapa de objetos.

O hub usa objetos do escritório como entradas para Universidade, Startup e Central de atendimento, com lista equivalente. Os três casos compartilham estilos `lab_*`; `campaign_workspace` cuida da navegação/pasta/salvar e `campaign_footer` do feedback. Estado do projeto permanece nos respectivos módulos; snapshots do retorno ficam em `campaign_results`, nunca em preferências globais. A pasta de campanha usa overlay próprio e Esc fecha somente esse overlay.

A montagem do aplicativo troca posições de Total, Lançamentos e Ações; arrastar e selecionar/posicionar chamam a mesma operação. A ordem é usada pela tela funcional de gastos e arquivada no retorno. O feedback tem texto além de cor. Novos fundos preservam o traço ilustrado e diferenciam os locais por objetos e luz; chuva é passagem de tempo, não uma regra que conserta o software.

## Campanha 1.2 — pasta de trabalho

A campanha mantém azul-petróleo e teal, com âmbar `#e1b66b` nas ações de avanço e nos marcos. Cenário e personagens ocupam as conversas; atividades têm uma bancada própria, sem sobreposição da HUD. A pasta reúne fontes, projeto e compromissos. Hotspots sempre têm ação equivalente numa lista, e estado é escrito além da cor. Uma hipótese pode ser revista; uma entrega pendente nunca recebe rótulo de concluída.

O quarto e laboratório usam artes próprias. Sabrina muda de roupa no retorno explicitamente situado uma semana depois. Transições seguem a preferência do motor. Não há cronômetro de leitura. O portfólio em `docs/portfolio/index.html` usa abas de caderno, paleta do jogo e imagens locais; mantém foco visível, diálogo acessível e respeita movimento reduzido.

Uma visual novel educacional em português para estudantes iniciando a prática de engenharia de software. O jogador precisa ler, comparar decisões e consultar o que descobriu sem pressa.

## Padrões preservados

- Cenas e personagens ilustrados já disponíveis no projeto; sem acrescentar estilos de arte conflitantes.
- Painéis azul-petróleo `#142b38`, texto claro `#eaf3f7`, destaque azul `#99ccff` e verde `#51c8b6` nas ações do perfil/inventário.
- Fonte DejaVu Sans fornecida pelo Ren'Py; hierarquia por tamanho e espaço.
- Fundos opacos atrás de texto, foco visível e estado selecionado escrito quando relevante.
- Emblemas do perfil são símbolos simples com rótulo, sem mudar oportunidades ou desempenho.
- Texto maior preserva conteúdo; rolagem permite acessar opções que não cabem acima do diálogo.
- Notebook mostra registros à medida que são descobertos. Informação pendente não é uma resposta escondida atrás de um controle.

## Verificação visual

Revisar menu, perfil, notebook parcial/completo, escolhas longas, histórico e encerramento nas fontes normal/maior. Verificar variante compacta no motor separadamente de testes em dispositivos reais. Nenhuma informação essencial pode depender apenas de cor, som ou animação.
