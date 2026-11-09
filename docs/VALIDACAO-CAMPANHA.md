# Verificação da campanha 1.2

Esta versão implementa a campanha do laboratório, preserva as três demos guiadas e acrescenta um portfólio HTML local. O plano original permanece como histórico; a expansão em campanhas próprias de gastos e chamados e a avaliação com participantes continuam pendentes.

## Escopo entregue

- Exploração por três destinos e evidências com origem, incluindo missão opcional da planilha local.
- Vínculos revisáveis de evidência e requisito, planejamento com capacidade e dependência.
- Duas prioridades negociáveis; protótipo, entrega e investigação possuem estados diferentes.
- Calendário com quatro casos, consulta diferente conforme o item escolhido e reserva anterior preservada.
- Retorno, promessa cumprida ou renegociada, incidente, reparação, regressão e quatro famílias de epílogo.
- Memória de fatos, plano original preservado e estado compatível com salvar/carregar e rollback.
- HUD, pasta de trabalho, feedback visual de seleção e resultado; transição de resultado desativável.
- Quatro artes novas integradas; Sabrina muda de roupa no retorno. Técnica participa por diálogo, sem novo sprite.
- Portfólio HTML offline com abas por teclado, simulador causal e galeria ampliável.

## Revisão e correções

Três implementadores GPT-6.1 Sol/high trabalharam em estado, UI e narrativa. GPT-6 Astra/high revisou o conjunto e as correções. A coordenação executou testes no SDK existente e inspecionou capturas.

As rodadas encontraram e corrigiram:

1. Valores de retorno de ações `Function` encerravam telas de atividade. Ações agora descartam retorno; testes verificam permanência da atividade.
2. HUD sobreposta a telas usadas por composição; modal e ordem de desenho explícitos nas telas públicas.
3. Reparação apagava escopo anterior; snapshot preservado e itens anteriores mantidos na rodada adicional.
4. Pesquisa simultaneamente incluída no pacote e adiada na conversa; pesquisa virou rodada alternativa, com custo explícito de atraso.
5. Calendário legível custava capacidade sem efeito; agora altera a consulta do produto demonstrado.
6. Entrega marcada cedo demais; primeira entrega só na chegada à bancada, revisão só após os dois testes de regressão corretos.
7. Memória e marcos vagos; falas condicionadas às fontes, responsável e retorno explícitos.
8. Testes com ações dentro de asserções executavam efeitos duas vezes; asserções agora apenas observam. Textos estáticos são conferidos pelo widget correto, junto da inspeção visual.
9. Imagem de mapa ultrapassava a coluna; enquadramento contido e controles desabilitados identificados por texto.

## Evidência técnica

- Ren'Py 8.5.3, Windows: lint sem erros; 253 blocos de diálogo, 29 menus e 52 telas.
- Suíte completa com capturas opcionais: 53 casos, 388 asserções e 86 hooks passaram, sem falhas.
- Regras de estado em Python: 15 testes passaram.
- Interface na variante `small touch` do motor: 15 casos e 77 asserções passaram. Isso não substitui avaliação em aparelho físico.
- Capturas inspecionadas: menu, mapa, fontes, quadro, planejamento, consulta separada/unificada, diário, roupa no retorno e finais com texto maior. Cópias selecionadas estão no portfólio.
- A revisão final Astra confirmou o fechamento dos achados, incluindo entrega da revisão somente após regressão.

O pacote Windows `TheRequirementsWhisperer-1.2-campanha-win.zip` foi gerado com 105.996.176 bytes. SHA-256: `8fe73772863c9e02d15f2e6d45f1a502dcf20e3626cadf831489b68ece9679af`. O runtime Python/Ren'Py incluído no pacote executou os testes contra o código extraído: 50 casos e 387 asserções passaram; três casos de captura visual, opcionais, ficaram desativados. Apenas os testes foram copiados para a extração; o código distribuído foi preservado.

O SDK existente foi reutilizado; nenhum recurso Docker foi criado. A integração e a limpeza são acompanhadas em `IMPLEMENTACAO.md`.

O portfólio foi aberto no navegador e exercitado em 1440px e 390px: abas por clique e setas, mudanças de consequência, ampliação de imagem e fechamento por Esc. Nenhuma imagem de conteúdo ausente ou overflow horizontal na verificação. Não usa CDN, fontes remotas ou scripts externos. As fontes de sistema têm fallback; o HTML pode ser aberto diretamente do disco.

## Limites

Não houve playtest com estudantes nesta sessão. Duração, vontade de continuar, compreensão e transferência para problemas novos não foram medidas. A campanha exercita requisitos, escopo, priorização, dependências, comunicação, verificação e acompanhamento; não equivale a curso completo ou certificação profissional.

Arrastar cartões não foi implementado: seleção por clique e teclado atende ao vínculo entre fonte e requisito. O calendário trabalha com exemplos delimitados, não com edição livre de código. Não há avaliação semântica automática de texto livre. Voz e uso em aparelhos físicos ainda precisam de validação própria.

Os testes de nova partida da demo conferem defaults antigos convivendo com os novos; não foi carregado save pessoal do usuário nem uma coleção histórica de saves. Artes preexistentes continuam com a pendência de origem/créditos já documentada antes desta sessão.
