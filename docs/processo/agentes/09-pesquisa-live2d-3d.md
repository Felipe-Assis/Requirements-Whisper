# Pesquisa — Live2D, 3D Stage e personagens que se mexem

Executor: agente Claude (general-purpose) com WebSearch/WebFetch, 2026-11-02. Resultado: `docs/pesquisa/live2d-3d.md`.
Prompt usado:

---

Pesquisa técnica (sem implementar nada, sem editar arquivos de projeto). Responda em português do Brasil, linguagem simples e objetiva.

Contexto: visual novel educacional em Ren'Py 8.5.3 (Windows; SDK em `C:\Program Files (x86)\renpy-8.5.3-sdk`; projeto em `C:\Users\Felipe\Documents\GitHub\Renpy Projects\Requirements-Whisper`, branch main, com `config.zoom_zaxis = False` e `config.old_show_expression = True` em options.rpy). Os personagens hoje são sprites PNG estáticos 1024x1536 (corpo inteiro, 3 poses por personagem, sem camadas) exibidos com transforms `left_zoom`/`center_zoom`/`right_zoom` (zoom 0.6). Os fundos são PNG 1536x1024 esticados para 1920x1080. A arte foi gerada por IA de imagem (não há arquivos fonte em camadas/PSD).

Perguntas que o usuário quer respondidas, com base na documentação oficial do Ren'Py (renpy.org/doc/html, use WebFetch/WebSearch; leia também a pasta `doc` do SDK local se existir, e o código em `renpy/` do SDK quando a documentação for vaga) e nas páginas oficiais da Live2D (licenciamento, Cubism SDK):
1. Personagens e avatar "semi-3D" que ficam se mexendo em loop (respiração, piscar, leve balanço, cabelo): quais caminhos existem no Ren'Py 8.5.3? Compare pelo menos: (a) ATL puro sobre o PNG atual (respiração com zoom/yzoom sutil, balanço, sombra), (b) layeredimage com piscar/boca animados (exige recortar camadas), (c) Live2D (suporte nativo do Ren'Py: o que precisa — Cubism SDK for Native, onde colocar, versão suportada pelo 8.5, formatos .model3.json/.moc3, motions/expressions, como declarar `Live2D(...)`, limitações na web/mobile, custo/licença da Live2D para uso educacional/indie/comercial, ferramenta Cubism Editor e o trabalho de "rigging" a partir de uma arte em camadas), (d) Spine ou outras alternativas via terceiros, (e) shaders/Model-based rendering do Ren'Py (ex.: mesh warp, `renpy.register_shader`) para deformação simples. Para cada um: o que precisa, esforço, qualidade visual, risco e como encaixa com a arte gerada por IA.
2. "3D Stage" do Ren'Py: o que é (camera, zpos, perspective, layer 3D, zzoom, matrixtransform etc.), em que versão entrou, como ativar, o que permite (parallax, profundidade, câmera que se move entre personagens, efeito de foco), interação com `config.zoom_zaxis = False` que o projeto fixa, custo de performance, e exemplos curtos de código ATL/camera. Diga o que seria necessário preparar na arte (ex.: fundos separados em planos: fundo, meio, frente) para tirar proveito.
3. Personagens 3D de verdade (modelos 3D): o Ren'Py suporta? Se não, quais caminhos (renderizar spritesheets/vídeo a partir de modelos 3D, etc.).
4. Recomendação: um caminho em etapas (o mais barato que já dá "vida" agora → intermediário → ambicioso), com estimativa de esforço relativo e o que precisaria ser decidido/comprado. Destaque o que funciona com a arte atual sem refazer.
Cite as URLs consultadas ao lado de cada afirmação relevante. Não invente versões ou APIs: se não confirmar algo na documentação ou no código do SDK, diga que não confirmou.

Entregue também um arquivo markdown com o relatório em `X:/dev-tmp/requirements-whisper/evolucao/pesquisa-live2d-3d.md` (crie a pasta). Sua resposta final deve ser o mesmo relatório.
