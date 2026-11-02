# Arte: prompts, referências e como regerar

Toda a arte gerada com IA neste projeto passou pelo Codex (skill `imagegen`, ferramenta `image_gen` embutida, sem
chave de API). Esta pasta guarda o necessário para regerar ou modificar qualquer imagem.

## Estilo atual: C (mescla aprovada em 2026-11-02)

Escolhido na página de comparação (Emily, Tainá e o escritório em três estilos):
https://claude.ai/artifact/4wNJSGy4HhqwEEcpALx8X1

- **Personagens:** contorno escuro com leve textura de lápis/carvão, cores suaves e levemente dessaturadas, formas
  simples, sombra mínima, rosto simples com olhos discretos; anatomia, mãos e roupas corretas; nada de anime genérico.
- **Fundos:** paleta suave, leve textura de papel, clima de ilustração feita à mão, perspectiva precisa, luz contida,
  figurantes de costas e sem rosto, sem texto.
- **Referências de estilo** (as imagens aprovadas) em `referencias/`: `estilo-c-emily.png`, `estilo-c-taina.png`,
  `estilo-c-escritorio.png`. Toda geração nova anexa uma delas.

## Referência padrão: a Emily

Decisão do usuário em 2026-11-02, depois de quatro rodadas de revisão do elenco da Saúde: **o traço da Emily
(`developer_requirements`) é o padrão de todo personagem**, novo ou refeito. Os personagens das rotas novas
(Tainá, Kauã etc.) seguem o mesmo traço e servem de apoio.

O texto e as referências ficam em `tools/arte/estilo_padrao.py` (`CORPO`, `ROSTO`, `SPRITE`, `ESTILO`, `REF_EMILY`,
`REF_ROSTOS`). Um script de lote novo importa de lá em vez de escrever o próprio estilo:

```python
from estilo_padrao import ESTILO, REF_EMILY, REF_ROSTOS
```

O que as revisões ensinaram (cada item foi um problema real apontado pelo usuário):

- **Rosto simples é o que mais pesa.** Pele chapada de um tom, íris escura simples com um brilho, nariz em traço,
  boca em forma simples, sobrancelha grossa. Sardas, cílios desenhados, batom, sombra no nariz, rugas e textura de
  barba deixam o personagem "detalhado demais" ao lado da Emily. Pedir "maçãs do rosto e mandíbula definidas" puxou
  o rosto para esse lado; a idade deve vir do formato do rosto, do cabelo e da roupa.
- **Proporção de adulto (~7,5 cabeças).** Sem isso, o gerador volta à cabeça grande e ao corpo de criança
  (aconteceu com o colega de república).
- **Expressão está nas sobrancelhas e nos olhos.** Em cada pose, descreva sobrancelhas, olhos, direção do olhar e
  boca, e anexe como referência de expressão a mesma pose de um personagem das rotas novas. Pedir só "a pose da
  imagem X" fez o gerador copiar o rosto da âncora em todas as poses.
- **Um acessório de personalidade** (crachá, relógio, caneca, mochila, pasta, brinco) ajuda a não ficar genérico.
- **Objeto na mão precisa caber na pose.** Com braços cruzados, o objeto vai para o bolso.

`referencias/estilo-c-rostos.png` mostra cabeça e ombros de Emily, Tainá, Kauã e Dra. Michelle lado a lado. É a
referência para o rosto. Para refazer o close-up com outros personagens:
`python tools/arte/rostos.py saida.png img1.png img2.png ...`.

## Lotes e prompts (`prompts/`)

| Arquivo | O que gerou | Situação |
|---|---|---|
| `rotas-novas-2026-11-02.json` | 12 personagens, 9 fundos e 8 telas das rotas Startup e Corporativo | prompts reconstruídos de forma exata a partir de `docs/rotas/*-assets.json` por `tools/arte/montar_rotas_novas.py`; personagens e fundos depois substituídos pelo estilo C; as 8 telas (`images/artifacts/st_*`, `co_*`) continuam em uso |
| `comparacao-estilos-2026-11-02.json` | as 6 variações da página de comparação | registro da escolha do estilo |
| `estilo-c.json` | regeração de todos os personagens (23) e fundos (27) no estilo C | lote atual; montado por `tools/arte/montar_estilo_c.py` |
| `estilo-c-regeracoes.json` | 5 imagens refeitas do lote acima (2 com reforço de identidade/transparência, 3 que tinham nascido de uma âncora trocada) | aplicado junto com o lote |
| `estilo-c-saude-v2.json` | elenco da Saúde refeito na proporção e no detalhe da Emily e das rotas novas, com um acessório de personalidade por personagem (1ª revisão do usuário) | aplicado; montado por `tools/arte/montar_saude_v2.py`; refeitas em `estilo-c-saude-v2-regeracoes.json` |
| `estilo-c-saude-v3-expressoes.json` | todas as poses não âncora da Saúde com o rosto descrito por partes e referência de expressão das rotas novas (2ª revisão: "olhos quase não mudam") | aplicado; montado por `tools/arte/montar_saude_v3_expressoes.py`; Joseph e Mateus refeitos em `estilo-c-saude-v3-regeracoes.json` |
| `estilo-c-saude-v4.json` | colega de república e Dra. Nathalia refeitos como adultos com traços próprios; poses serious, thinking e positive novas para as duas doutoras; César sério com o celular no bolso (3ª revisão) | aplicado; montado por `tools/arte/montar_saude_v4.py`; colega e Nathalia substituídos pelo lote seguinte |
| `estilo-c-saude-v5-rostos.json` | rosto do colega e das 4 poses da Nathalia simplificado no traço da Emily (4ª revisão: "detalhados demais no rosto e olhos"); originou o padrão da seção "Referência padrão: a Emily" | aplicado; montado por `tools/arte/montar_saude_v5_rostos.py`; saídas em `estilo-c-saude-v5-rostos-saidas.json` |
| `mapa.json` | mapa da cidade (E3b): base 16:9 sem os prédios, 12 lugares recortados (dependem da base), 8 ícones de atividade, o marcador "Você" e 6 telas de transição (28 tarefas) | aplicado (refeitas em `mapa-regeracoes.json`; posições finais em `mapa-coordenadas-ajustadas.json`); montado por `tools/arte/montar_mapa.py`; design em `docs/design/mapa-cidade.md`; saídas com os kinds novos `mapa`, `lugar` e `icone` de `posproc.py` |

## Cuidado com execuções em paralelo

O Codex grava cada imagem em `$CODEX_HOME/generated_images/<session id>/`. Nas primeiras rodadas, o prompt pedia
ao próprio Codex para copiar "a imagem gerada", e com 4 execuções em paralelo ele às vezes copiou a imagem de
outra sessão (ex.: o Vinícius saiu com o rosto do Jorge; o coworking saiu como o consultório). Desde 2026-11-02,
`gerar_codex.py` lê o `session id` no log de cada execução e copia ele mesmo a imagem daquela sessão
(`gerar_codex_util.py`). Para um staging antigo, `reparar_staging.py <staging>` recopia cada imagem da sua sessão e
lista as que estavam trocadas; poses e variantes geradas a partir de uma âncora trocada precisam ser regeradas.
Mesmo assim, toda imagem passa pela folha de contato antes de entrar no jogo.

Cada tarefa tem `id`, `prompt`, `refs` (imagens anexadas, na ordem citada no prompt) e, quando depende de outra,
`depends`: a saída dessa outra tarefa entra como **primeira** referência (identidade do personagem nas demais poses;
ambiente base nas variantes de horário). Os arquivos `*-saidas.json` dizem onde cada saída é gravada no jogo.

A arte original da rota Saúde (antes de 2026-11-02) foi feita fora deste repositório; os prompts dela não existem.
Ela serviu de referência de identidade e pose para o lote do estilo C.

## Como regerar ou modificar

Ferramentas em `tools/arte/` (Python 3 com Pillow; Codex CLI autenticado):

1. Copie as tarefas que quer refazer para um JSON novo (ou edite o prompt). Para mudar só uma pose, mantenha o
   `depends` da âncora do personagem: a âncora já gerada garante o mesmo rosto e a mesma roupa.
2. Gere fora do repositório:
   `python tools/arte/gerar_codex.py tarefas.json X:/dev-tmp/requirements-whisper/<tarefa>/staging 4`
   Cada imagem leva de 1,5 a 2 minutos; tarefas já geradas são puladas, então dá para retomar.
3. Ajuste ao padrão do jogo numa pasta de revisão:
   `python tools/arte/posproc.py prompts/estilo-c-saidas.json <staging> <pasta-revisao>`
4. Revise numa folha de contato (`python tools/arte/folha.py folha.png 600 img1.png img2.png ...`): mesma pessoa
   entre poses, mesma roupa, fundo transparente, estilo C. Regere o que destoar com um reforço no início do prompt
   (exemplos em `montar_rotas_novas.py`, `REFORCOS`).
5. Depois de aprovado, grave no jogo: `python tools/arte/posproc.py <saidas.json> <staging> game --substituir`.
   Os nomes de arquivo não mudam, então nenhum script precisa ser alterado.

Padrões de saída: sprite RGBA 1024x1536 com a figura de ~1490 px de altura e os pés a 22 px da base; retrato
520x430 recortado da pose âncora; fundo RGB 1536x1024; tela de produto RGBA com até 1600 px de largura. Mapa:
base RGB 2560x1440; lugar RGBA recortado justo, na largura definida em `mapa-saidas.json` (sem normalizar a altura);
ícone e marcador RGBA 192x192 com margem.
