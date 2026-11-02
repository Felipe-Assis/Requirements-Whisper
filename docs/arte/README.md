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

## Lotes e prompts (`prompts/`)

| Arquivo | O que gerou | Situação |
|---|---|---|
| `rotas-novas-2026-11-02.json` | 12 personagens, 9 fundos e 8 telas das rotas Startup e Corporativo | prompts reconstruídos de forma exata a partir de `docs/rotas/*-assets.json` por `tools/arte/montar_rotas_novas.py`; personagens e fundos depois substituídos pelo estilo C; as 8 telas (`images/artifacts/st_*`, `co_*`) continuam em uso |
| `comparacao-estilos-2026-11-02.json` | as 6 variações da página de comparação | registro da escolha do estilo |
| `estilo-c.json` | regeração de todos os personagens (23) e fundos (27) no estilo C | lote atual; montado por `tools/arte/montar_estilo_c.py` |
| `estilo-c-regeracoes.json` | 5 imagens refeitas do lote acima (2 com reforço de identidade/transparência, 3 que tinham nascido de uma âncora trocada) | aplicado junto com o lote |
| `mapa.json` | mapa da cidade (E3b): base 16:9 sem os prédios, 12 lugares recortados (dependem da base), 8 ícones de atividade, o marcador "Você" e 6 telas de transição (28 tarefas) | a gerar; montado por `tools/arte/montar_mapa.py`; design em `docs/design/mapa-cidade.md`; saídas com os kinds novos `mapa`, `lugar` e `icone` de `posproc.py` |

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
