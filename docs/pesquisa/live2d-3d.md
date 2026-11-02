# Pesquisa: personagens "vivos", Live2D, 3D Stage e 3D no Ren'Py 8.5.3

Projeto: Requirements-Whisper (Ren'Py 8.5.3, Windows). Pesquisa técnica, sem nenhuma alteração no projeto.
Data: 2026-11-02.

## Resumo

- **Dá para ter "vida" já, sem refazer a arte:** ATL puro (respiração, balanço, entrada suave) sobre os PNGs atuais funciona hoje, custa poucas horas e não tem risco de licença. Um shader de balanço com `mesh` (deformação simples, topo mexe e pés ficam parados) também funciona com o PNG inteiro.
- **Piscar e boca:** não precisa recortar o personagem todo. Basta gerar por inpainting (IA) uma versão "olhos fechados" e 1 ou 2 bocas, recortar só esse retângulo e usar `layeredimage` com ATL. É o melhor ganho por esforço depois do ATL.
- **Live2D:** tem suporte nativo no Ren'Py 8.5.3 e funciona na web desde o 8.5.0. Mas exige arte em camadas (PSD com partes separadas e áreas escondidas pintadas) e rigging no Cubism Editor, por personagem. Com 11 personagens e arte gerada por IA, sem fonte em camadas, é o caminho mais caro. Licença: indivíduo ou empresa com faturamento anual abaixo de 10 milhões de ienes não precisa assinar nem pagar a licença de publicação do SDK.
- **Spine:** não há runtime oficial para Ren'Py. Não recomendo.
- **3D Stage:** existe desde o 7.4.5 (câmera via `camera` desde o 7.4.6). Permite paralaxe, câmera que anda entre personagens e profundidade real. Ativa-se com `camera: perspective True`. Para paralaxe de verdade, os fundos precisam estar separados em planos (fundo, meio, frente).
- **3D de verdade:** o 8.4.0 trouxe `GLTFModel`, mas é mínimo: só malha e textura, **sem animação**, sem shader padrão. Serve para fundo ou objeto 3D estático, não para personagem animado. Para personagem 3D, o caminho prático é renderizar fora (Blender etc.) e importar como PNG ou vídeo WebM com máscara.

## Contexto conferido no projeto

- `game/options.rpy:30-31`: `config.zoom_zaxis = False` e `config.old_show_expression = True`.
- `game/ui/styles/sprite_transforms.rpy`: `left_zoom`, `center_zoom`, `right_zoom` etc. usam `xalign`, `yalign 1.0` e `zoom 0.6`. Como `yalign 1.0` ancora os pés na base da tela, um `yzoom` de respiração mantém os pés parados e mexe só o topo (bom para respiração).
- `game/data/backgrounds.rpy`: fundos declarados como `Transform("...png", xysize=(config.screen_width, config.screen_height))`. O PNG 1536x1024 (3:2) é esticado para 16:9, com distorção de cerca de 18% na horizontal. Para mover câmera ou fazer paralaxe, vai faltar margem e resolução (ver seção 2).
- `game/images/characters/`: 11 personagens, 3 a 4 PNGs cada, além de `portrait.png` (avatar).
- O SDK local **não tem Live2D instalado** (não há `Live2DCubismCore.dll` em `lib/py3-windows-x86_64`).
- O projeto considera build web (`progressive_download.txt`, ramo web no chat).

---

## 1. Personagens e avatar que se mexem em loop

### Comparativo rápido

| Caminho | Precisa | Esforço (estimativa minha) | Qualidade visual | Risco | Encaixe com a arte de IA |
|---|---|---|---|---|---|
| (a) ATL sobre o PNG | Só código | Muito baixo: 2-4 h para todos | Sutil: dá "presença", não expressão | Muito baixo | Total, usa os PNGs atuais |
| (b-lite) piscar/boca por inpainting + `layeredimage` | 2-3 recortes pequenos por pose, gerados por inpainting | Baixo a médio: cerca de 1-2 h por pose | Boa: piscar e boca fazem muita diferença | Baixo; precisa alinhar pixel a pixel | Bom: só muda a região dos olhos e da boca |
| (b) `layeredimage` completo | Personagem recortado em camadas | Médio a alto | Boa, com troca de expressão sem novo PNG | Médio | Ruim: exige recortar e pintar áreas escondidas |
| (c) Live2D | Cubism SDK + Cubism Editor + PSD em camadas + rigging | Alto: dias a semanas por personagem | Excelente (cabeça, olhos, cabelo com física) | Alto: arte, licença, plataformas | Ruim sem PSD: precisa decompor a arte |
| (d) Spine | Runtime de terceiros (não existe oficial) + licença Spine | Muito alto | Excelente (esqueleto) | Muito alto | Ruim, também exige camadas |
| (e) Shader + `mesh` | `renpy.register_shader` + GLSL | Baixo a médio: 4-8 h para o primeiro | Média: balanço e ondulação, sem expressão | Médio: GLSL ES na web, testes em GPUs | Total, usa o PNG inteiro |
| (f) Vídeo em loop (WebM com máscara) | Gerar o loop fora (IA de vídeo, After Effects, render 3D) | Médio por clipe | Pode ser muito boa | Médio: tamanho, decodificação, consistência | Bom, se a IA de vídeo mantiver o rosto |

### (a) ATL puro sobre o PNG atual

O que é: transforms ATL com `ease`, `parallel`, `repeat` e `choice` alterando `yzoom`, `xoffset`, `rotate` etc. `xzoom`/`yzoom` estão documentados em https://www.renpy.org/doc/html/transform_properties.html. A instrução `choice` (sorteio de ramos com peso) está em https://www.renpy.org/doc/html/transforms.html.

Exemplo (não executado; validar no jogo):

```renpy
# Respiração + leve balanço. Amplitudes pequenas para não deformar o rosto.
transform vivo(resp=0.006, dx=2, t1=2.4, t2=3.7):
    parallel:
        ease t1 yzoom 1.0 + resp
        ease t1 yzoom 1.0
        repeat
    parallel:
        ease t2 xoffset dx
        ease t2 xoffset -dx
        repeat

# Mesmas posições de hoje, com vida. Incluir um transform dentro de outro
# em ATL executa o primeiro (instantâneo) e depois o segundo.
transform right_zoom_vivo:
    right_zoom
    vivo
```

- Respiração com `yzoom` a 0,5-1% estica o corpo inteiro, inclusive o rosto. Nessa amplitude não se nota a deformação, mas acima de 1,5% a cabeça parece "esticar".
- Sombra no chão: um `Solid` ou PNG de elipse escura com `alpha` e `blur` abaixo do sprite, mexendo junto. `blur` achata o filho e pode ter artefatos (https://www.renpy.org/doc/html/transform_properties.html#transform-property-blur).
- Fases diferentes por personagem (`t1`, `t2` diferentes) evitam que todos respirem juntos.
- Custo: transforms com `repeat` pedem redesenho contínuo. Para 2D isso é barato no desktop.
- Avatar (`portrait.png`): mesma técnica, com amplitudes ainda menores.

### (b) `layeredimage` com piscar e boca animados

O `layeredimage` aceita, em `always`, `attribute` e `group`, qualquer displayable, inclusive uma imagem com bloco ATL, além de `at` com transform (https://www.renpy.org/doc/html/layeredimage.html). Isso permite um olho que pisca sozinho:

```renpy
image dev_req_olhos:
    "images/characters/developer_requirements/olhos_abertos.png"
    choice 3:
        pause 3.5
    choice 2:
        pause 5.0
    choice 1:
        pause 1.8
    "images/characters/developer_requirements/olhos_fechados.png"
    pause 0.12
    repeat

layeredimage developer_requirements:
    group pose:
        attribute neutral default "images/characters/developer_requirements/neutral.png"
        attribute enthusiastic "images/characters/developer_requirements/enthusiastic.png"
    always "dev_req_olhos"   # na prática, um olho por pose (usar if_any/condições)
```

Boca falando: `config.speaking_attribute` adiciona um atributo de imagem ao personagem enquanto ele fala e o remove quando para (https://www.renpy.org/doc/html/config.html#var-config.speaking_attribute). Com um atributo `falando` ligado a uma boca em ATL (aberta/fechada alternando), a boca mexe durante a fala sem código extra no roteiro. Exige que o `Character` tenha `image=` ligado à tag do sprite.

**Versão "lite" para arte de IA (recomendada):** não recortar o corpo. Para cada pose:
1. Gerar com inpainting (mesma imagem, máscara só nos olhos) uma variante "olhos fechados"; idem para 1-2 bocas.
2. Recortar só o retângulo dos olhos e da boca, em PNGs pequenos com transparência, no mesmo enquadramento do original (mesmo tamanho de tela 1024x1536, ou com `pos` em pixels).
3. Montar o `layeredimage` com o PNG inteiro como base e os recortes por cima.

Risco: diferença de cor ou borda entre o recorte e a base. Mitigação: recortar com borda suave e conferir com zoom 0.6 na tela real. Precisa ser feito para cada uma das cerca de 35 poses, ou só para as mais usadas.

### (c) Live2D (suporte nativo no Ren'Py)

**Como o Ren'Py integra** (https://www.renpy.org/doc/html/live2d.html e doc local `doc/live2d.html` do SDK):
- O Ren'Py lê os arquivos exportados pelo Live2D, calcula parâmetros a partir de motions e expressions e passa ao **Cubism SDK for Native**, que devolve as malhas para o Ren'Py desenhar.
- Suporta formatos Cubism 3, 4 e 5, além de expressions e motions.
- Arquivo de entrada: `.model3.json` (ou a pasta que o contém). O `.model3.json` aponta para o `.moc3`, as texturas, os `.motion3.json` e os `.exp3.json`.

**Versão exigida pelo 8.5.3:** o changelog do 8.5.3 diz: "Ren'Py now supports and requires Live2D 5.3" (https://www.renpy.org/doc/html/changelog.html, seção 8.5.3). O código do SDK reforça: `renpy/gl2/live2d.py` anexa ao erro de carga a nota "Live2D Cubism 5.3 or later is required.". Pela Live2D, "5.3 SDK" significa Cubism 5 SDK **R5 beta1 ou posterior** (https://docs.live2d.com/en/cubism-sdk-manual/compatibility-with-cubism-5-3/). Arquivos `.moc3` exportados com recursos do 5.3 não abrem em cores antigos.
- Atenção: a página de instalação ainda cita `CubismSdkForNative-5-r.1.zip`, que é anterior ao 5.3. O instalador do launcher aceita qualquer arquivo com o padrão `CubismSdkForNative-[45]-*.zip` (`launcher/game/install.rpy:97`). Use o SDK mais recente da série 5 (R5 ou posterior). Não confirmei o nome exato do zip atual porque a página de download não mostra a versão sem login/aceite.

**Instalação** (doc + `launcher/game/install.rpy`):
1. Baixar o Cubism SDK for Native em https://www.live2d.com/en/sdk/download/native/. É preciso aceitar o Proprietary Software License e o Open Software License.
2. Colocar o zip na pasta do SDK do Ren'Py (`C:\Program Files (x86)\renpy-8.5.3-sdk`).
3. No launcher, abrir Preferences, depois Install libraries, depois "Install Live2D Cubism SDK for Native". O instalador copia `Live2DCubismCore.dll` para `lib/` (Windows x86_64, Linux, macOS, Raspberry Pi e Android armv7/arm64).
4. Web: zip `CubismSdkForWeb-5-*.zip` e botão "Install Live2D Cubism SDK for Web" (suporte web desde o 8.5.0, conforme o changelog).
5. O texto do launcher avisa: "Live2D doesn't support Android x86_64 (including emulators and Chrome OS) and must be added to iOS projects manually. Live2D must be reinstalled after upgrading Ren'Py or installing Android support."

**Declaração e uso** (doc oficial):

```renpy
init python:
    # A doc recomenda um fallback: se o Live2D não iniciar, uma chamada
    # a Live2D() impede o jogo inteiro de carregar.
    def RWLive2D(*args, fallback=None, **kwargs):
        if renpy.has_live2d():
            return Live2D(*args, **kwargs)
        return fallback

image mentora = RWLive2D("live2d/Mentora", base=0.6, loop=True,
                         fallback="images/characters/doutora_1/base.png")

label exemplo:
    show mentora idle exp_feliz      # motion + expression viram atributos
    show mentora -exp_feliz           # remove expressão não exclusiva
```

- Assinatura: `Live2D(filename, zoom=None, top=0.0, base=1.0, height=1.0, alias={}, loop=False, fade=None, seamless=None, attribute_function=None, attribute_filter=None, update_function=None, **properties)`. Também aceita `nonexclusive` e `default_fade`.
- Os nomes de motions e expressions vêm dos arquivos, em minúsculas e sem o prefixo do modelo (`Hiyori_Motion01` vira `motion01`). Atributos especiais: `null` (sem expressão) e `still` (para as motions).
- `update_function` + `blend_parameter()`/`blend_opacity()` permitem mexer parâmetros por código (ex.: olhar seguir algo).
- Em loop, a doc recomenda pausas acima de 0,2 s nas motions para o Ren'Py fazer predição de imagens.
- Observação de código (não testada): no 8.5.3, `onetime_init()` em `renpy/gl2/live2d.py` captura a exceção de carga da DLL e só anexa uma nota, sem relançar. Por isso, teste o build final numa máquina limpa e não confie só em `renpy.has_live2d()`.

**Licença e custo (Live2D):**
- Licença de publicação do SDK (SDK Release License): exigida de empresas que publicam conteúdo com o SDK. "Individuals and small-scale businesses are exempt from the license agreement and payment (excluding Expandable Application)" (https://www.live2d.com/en/sdk/license/). Pequena empresa ou usuário geral significa faturamento anual **abaixo de 10 milhões de ienes** (https://help.live2d.com/en/?p=2181 e https://www.live2d.com/en/cubism/comparison/).
- Quando aplicável, o contrato é por obra e precisa ser feito pelo menos um mês antes do lançamento. Para jogos há planos D (sem fins lucrativos, distribuído), F/E (compra única) e G (royalty) (https://www.live2d.com/en/sdk/license/).
- Uma VN não é "Expandable Application", categoria pensada para sistemas de avatar e software de VTuber.
- **Ponto a decidir:** quem publica? Se for o aluno ou o grupo do curso (UFRJ), cai na isenção. Se uma empresa acima de 10 milhões de ienes publicar ou comercializar, precisa de contrato.
- **Cubism Editor** (a ferramenta de rigging), conforme https://www.live2d.com/en/cubism/comparison/:
  - FREE: 1 textura de até 2048 px, até 100 ArtMeshes, 30 parâmetros, 50 deformers e 30 partes. Uso comercial permitido para quem fatura abaixo de 10 milhões de ienes.
  - PRO: sem esses limites, com teste grátis de 42 dias (https://www.live2d.com/en/cubism/download/editor/) e desconto de 76% para estudantes e professores (plano de 3 anos).
  - Preço do PRO: **não confirmei** em fonte oficial; consultar https://store.live2d.com.
  - Um rig simples de idle (respirar, piscar, boca, ângulo da cabeça, cabelo com física) costuma caber em cerca de 20-30 parâmetros. Pode caber no FREE, mas a textura única de 2048 px é apertada para corpo inteiro (estimativa minha, não confirmada).

**Trabalho de rigging a partir da arte de IA:**
- O Live2D deforma camadas separadas. A doc do Ren'Py cita como exemplo uma camada para pupilas e íris, outra para o branco dos olhos, outra para as sobrancelhas etc.
- A arte de IA é uma imagem única. Seria preciso, por personagem:
  1. Separar em PSD: cabelo frente, lados e trás; rosto; olhos (branco, íris, pálpebras, cílios); sobrancelhas; boca (lábios, interior); pescoço; tronco; braços.
  2. **Pintar as áreas escondidas**: testa sob a franja, olho sob a pálpebra, pescoço sob o queixo.
  3. Criar malhas, deformers e parâmetros, além de motions de idle e expressions.
- As 3 poses de corpo atuais (braços diferentes) não viram expressões: seriam rigs separados ou braços trocáveis.
- Estimativa minha: dias a semanas por personagem para quem já sabe rigar. Para 11 personagens, inviável sem um artista dedicado.

**Plataformas:** Windows, Mac e Linux pelo instalador. Web desde o 8.5.0 (SDK for Web separado). Android só ARM. iOS manual. Mais memória e tempo de carga, porque o Ren'Py gera mipmaps para texturas Live2D (changelog 8.4.0). Usar recursos do 5.3 (blend modes, offscreen) aumenta o custo de desenho (https://docs.live2d.com/en/cubism-sdk-manual/compatibility-with-cubism-5-3/).

### (d) Spine e outras alternativas de terceiros

- Spine: não existe runtime oficial para Ren'Py. A lista de runtimes oficiais (C, C++, C#, TS, Godot, Unity, Unreal, SDL etc.) não inclui Python nem Ren'Py (https://github.com/EsotericSoftware/spine-runtimes). No fórum da Esoteric, a resposta foi que não há runtime para Ren'Py e que portar ou envolver o runtime em C seria o caminho (https://de.esotericsoftware.com/forum/d/27841-has-anybody-tried-use-spine-in-renpy-with-python-runtime).
- Licença Spine: "users of your software must have their own Spine license", e para distribuir é preciso licença Spine no momento da integração (README do repositório acima).
- Conclusão: exigiria escrever uma integração própria (Cython/C + `Model` do Ren'Py) e manter a cada versão. Custo muito alto, sem ganho sobre Live2D para VN. Não recomendo.
- Alternativa prática de terceiros: **vídeo em loop**. O Ren'Py não decodifica alfa em vídeo, mas o `Movie(play=..., side_mask=True)` aceita vídeo com cor e máscara lado a lado. A doc mostra o comando ffmpeg para gerar o arquivo. Movies em `Movie` repetem automaticamente e há ressalvas de codec na web (https://www.renpy.org/doc/html/movie.html). O loop pode vir de IA de vídeo (image-to-video a partir do PNG atual), After Effects, Live2D (export de vídeo) ou render 3D. Riscos: consistência do rosto, tamanho dos arquivos, 1 canal de vídeo por sprite e custo de decodificação com vários personagens na tela.

### (e) Shaders / Model-Based Rendering (deformação simples)

- `mesh` (True ou tupla com o número de pontos) faz o transform virar um modelo com grade de vértices. `shader` aplica partes de shader registradas com `renpy.register_shader(name, variables=..., vertex_NNN=..., fragment_NNN=...)`. Uniforms `u_*` viram propriedades de transform. `u_time` está disponível para animar (https://www.renpy.org/doc/html/model.html).
- Ordem dos shaders padrão: `renpy.geometry` faz `gl_Position = a_position` na prioridade 0 e aplica `u_transform` na prioridade 100 (https://www.renpy.org/doc/html/shader_parts.html). Um vertex shader na prioridade 50 pode deslocar vértices em pixels do modelo.
- A doc avisa que shaders com `u_time` podem "travar" se nada pedir redesenho; a solução documentada é `pause 0` + `repeat` no transform.
- GLSL da web e do mobile é GLSL ES 1.00, mais restrito.

Exemplo (não executado; validar):

```renpy
init python:
    renpy.register_shader("rw.balanco", variables="""
        uniform float u_time;
        uniform vec2 u_model_size;
        uniform float u_rw_amp;
        attribute vec4 a_position;
    """, vertex_50="""
        // 0 nos pés, 1 no topo: só a parte de cima balança.
        float altura = 1.0 - a_position.y / u_model_size.y;
        gl_Position.x += sin(u_time * 1.3) * u_rw_amp * altura * altura;
    """)

transform balanco_mesh(amp=4.0):
    mesh (4, 12)
    shader "rw.balanco"
    u_rw_amp amp
    pause 0
    repeat
```

- Não confirmei se `u_model_size` vem preenchido quando `mesh` é uma tupla (a doc diz que vale para "2D models that supply a size"). Se vier (0, 0), passe a altura como uniform próprio.
- Dá para limitar a deformação a uma faixa (ex.: só o tronco, para respiração sem esticar o rosto) usando a coordenada y. Cabelo "solto" não dá sem camadas, porque o shader não sabe o que é cabelo.
- Qualidade: melhor que ATL para balanço orgânico (curvatura), mas não faz piscar nem expressão.

---

## 2. 3D Stage

Fontes: https://www.renpy.org/doc/html/3dstage.html (online, 8.5.4) e `doc/3dstage.html` do SDK 8.5.3 (mesmo conteúdo nas seções conferidas).

**O que é:** posiciona displayables em 3 dimensões e renderiza com perspectiva. O eixo z aponta para o espectador: z positivo aproxima e aumenta, z negativo afasta e diminui.

**Desde quando:**
- 7.4.5: renderizador por modelos vira padrão e surge o 3D Stage.
- 7.4.6: instrução `camera`.
- 8.1 / 7.6: `point_to`, `xrotate`/`yrotate`/`zrotate`, `orientation`.
- Fonte: https://www.renpy.org/doc/html/changelog.html, seções 7.4.5, 7.4.6 e "New 3D Stage Properties".

**Ativação:**

```renpy
camera:
    perspective True
```

`camera` sem nome usa a camada `master`. Diferente de `show layer`, não é limpa por `scene`.

**Peças principais:**
- `zpos`: profundidade do sprite.
- `zzoom True`: compensa o encolhimento de um fundo com z negativo, para continuar 1:1.
- `perspective`: na câmera, pode ser True ou uma tupla (near, z 1:1, far). Com `gui.init(1920, 1080)` e fov 75, a distância 1:1 é de cerca de 1251.
- `xpos`/`ypos`/`zpos`/`rotate` na câmera: movem a câmera; o sentido é invertido em relação a um sprite.
- `matrixtransform` com `RotateMatrix`/`OffsetMatrix`/`ScaleMatrix`: animável em ATL se a estrutura for igual.
- `point_to Camera()`: faz o sprite olhar para a câmera.
- `gl_depth True`: ordenação por profundidade na GPU.

**Cuidado com `gl_depth`:** a doc de GL properties avisa que pixels transparentes também escrevem no buffer de profundidade e sugere usar `zorder`/`behind` (https://www.renpy.org/doc/html/model.html, seção GL Properties). Para sprites PNG com fundo transparente, **não use `gl_depth`**: mantenha a ordem normal de `show`.

**O que permite:**
- Paralaxe: planos em zpos diferentes andam em velocidades diferentes quando a câmera se move.
- Câmera que vai de um personagem a outro (`ease` no `xpos` da câmera) e aproximação (zpos da câmera).
- Leve rotação de câmera.
- Efeito de foco: não há profundidade de campo automática. Faz-se com `blur` nos planos fora de foco, mudando por ATL. `blur` tem custo e pode ter artefatos.

Exemplo (não executado; sinais e valores precisam de ajuste no jogo):

```renpy
transform plano_fundo:
    xalign 0.5 yalign 0.5
    zpos -600 zzoom True
transform plano_meio:
    xalign 0.5 yalign 1.0
    zpos -250 zzoom True
transform plano_frente:
    xalign 0.5 yalign 1.0
    zpos 150

label cena_reuniao:
    camera:
        perspective True
    scene sala_fundo at plano_fundo
    show sala_mesa at plano_meio
    show developer_test enthusiastic at right_zoom
    show sala_vaso at plano_frente
    # A câmera vai até o lado direito; os planos andam em velocidades diferentes.
    camera:
        perspective True
        ease 1.5 xpos 250
    # Foco: desfoca o fundo enquanto alguém fala.
    show sala_fundo at plano_fundo:
        ease 0.6 blur 6
```

Ao passar um bloco ATL no `show`, o transform padrão deixa de valer, por isso a doc pede `xalign`/`yalign` explícitos. A doc também avisa que `zpos` pode interagir de forma estranha com `left`/`right`/`xalign`, porque a perspectiva pode empurrar partes para fora da tela.

**Interação com `config.zoom_zaxis = False`:**
- No 8.4, `zoom` passou a escalar também o eixo z. `config.zoom_zaxis = False` volta ao comportamento antigo (https://www.renpy.org/doc/html/incompatible.html, seção 8.4).
- No código, `renpy/config.py:1599` define o padrão `zoom_zaxis = True` ("zooms will apply to the z-axis as well"). Em `RenderTransform.size_zoom_rotate` (`renpy/display/accelerator.pyx`, conferido no GitHub `master`, não no tag 8.5.3), quando `zoom != 1` e `zoom_zaxis` é True, o fator vai para o componente z da matriz do filho.
- Na prática, para PNGs planos (z = 0) não há diferença visível. `zoom 0.6` nos sprites continua igual, e o `zpos` do próprio transform não é escalado pelo `zoom`.
- A diferença aparece quando há conteúdo com profundidade dentro de um transform com `zoom`: `GLTFModel`, grupos com `zpos` internos, ou `zoom` aplicado a uma camada inteira.
- Com False, a profundidade não encolhe junto, então um modelo 3D reduzido por `zoom` fica "achatado" errado. Nesse caso, use `GLTFModel(..., zoom=...)`, que escala o modelo em si.
- Recomendação: manter False (protege as cenas atuais), usar `zpos` para profundidade e nunca usar `zoom` para escalar modelos 3D.

**Custo de performance:**
- Para quads 2D, a perspectiva é só uma matriz na GPU; a doc não cita custo.
- O que pesa: `blur` (renderiza para textura), fundos muito grandes (memória de textura) e `gl_depth`.
- Não encontrei números oficiais.

**Arte necessária para tirar proveito:**
- Fundos **separados em planos**: (1) fundo (paredes, janela, céu); (2) meio (mesa, estantes); (3) frente opcional (vaso, borda de monitor, desfocado). Cada plano é um PNG com transparência, e as áreas que o plano da frente cobre precisam estar pintadas no plano de trás.
- A arte gerada por IA não vem assim. É preciso recortar o primeiro plano e reconstruir por inpainting o que estava atrás dele. Com 3 planos por cena e cerca de 20 fundos, é um trabalho grande. Dá para fazer só nas cenas principais.
- **Proporção e margem:** gerar ou reamostrar em 16:9 e com sobra (ex.: 2304x1296 ou 2560x1440) para a câmera andar sem mostrar bordas. Hoje os fundos são 1536x1024 esticados para 1920x1080, então ampliar mais vai deixar a imagem macia.
- Um ganho imediato e independente: trocar `xysize` por `fit "cover"` (propriedade `fit`, https://www.renpy.org/doc/html/transform_properties.html) elimina a distorção, cortando as bordas em vez de esticar.
- **Sem separar planos**, ainda dá para fazer "câmera viva": um leve `ease` de `xpos`/zoom da câmera, ou um *Ken Burns* lento no fundo, com sprites e fundo em zpos diferentes. A paralaxe fica só entre fundo e personagens, e já ajuda.

---

## 3. Personagens 3D de verdade

**Suporte nativo existe, mas é mínimo.** Desde o 8.4.0 há o `GLTFModel(filename, shader=(), tangents=False, zoom=1.0, report=False)`, que usa a biblioteca Open Asset Importer (assimp). Fontes: https://www.renpy.org/doc/html/model.html#gltfmodel-displayable, `doc/model.html` local e `renpy/defaultstore.py:187` (`GLTFModel = renpy.gl2.assimp.GLTFModel`).

Limitações, conforme o changelog 8.4.0 e a doc:
- "only supports loading the mesh and textures of a model. There's no support for animation". Ou seja, **sem esqueleto e sem animação**.
- Sem shader padrão: é preciso registrar um shader de iluminação (a doc traz um exemplo de iluminação difusa e especular).
- Transparência ruim (artefatos de ordem).
- Sem *culling*: o modelo precisa ser simples.
- Tamanho zero para o layout 2D. Com vários modelos, é preciso `gl_depth True` na câmera.
- O próprio changelog diz que o recurso serve para fundos 3D e para experimentação.
- Conclusão: **personagem 3D animado não é viável nativamente no 8.5.3.** Objeto ou cenário 3D estático é possível, mas exige alguém com prática em GLSL.

**Caminhos para usar personagens feitos em 3D:**
1. **Pré-renderizar poses como PNG** (Blender, VRoid etc., com shader toon) e usar como os sprites de hoje, mais ATL ou camadas para piscar. Mantém o fluxo atual.
2. **Pré-renderizar loops como vídeo** WebM com `side_mask=True` (`Movie`), por exemplo idle de 2-4 s em loop. Dá movimento 3D real (cabelo, respiração). Custo: arquivos e decodificação. Na web, codecs diferentes (https://www.renpy.org/doc/html/movie.html).
3. **Sequência de quadros (spritesheet)** em ATL: muitos PNGs. Pesado em memória para sprites de 1024x1536, mas só vale para loops curtos.
4. Integração 3D própria (animar o `GLTFModel` por código, trocar malhas por quadro): não recomendo; é pesquisa e não um caminho de produção.

Para este projeto, 3D só faria sentido se a arte inteira fosse refeita em 3D. Não combina com a arte de IA atual.

---

## 4. Recomendação em etapas

### Etapa 1: "vida" já, sem refazer arte (esforço: muito baixo, cerca de 1 dia)
- ATL de respiração e balanço em todos os sprites e no avatar, com amplitude baixa e fase diferente por personagem.
- Entradas e saídas mais suaves (`ease` em `xoffset` e `alpha`) e um leve "pulo" de quem começa a falar.
- Sombra simples no chão.
- Fundos: `fit "cover"` no lugar de `xysize` para tirar a distorção, e Ken Burns muito lento em cenas longas.
- 3D Stage leve, sem separar planos: `camera: perspective True`, fundo com `zpos` negativo e `zzoom True`, e pequenas movimentações de câmera em momentos-chave.
- **Funciona com a arte atual. Nada a comprar.** Validar: `lint` limpo, cenas principais, desempenho no build web.

### Etapa 2: rostos vivos (esforço: médio, cerca de 1-2 h por pose; começar pelos 3-4 personagens mais presentes)
- `layeredimage` "lite": base = PNG atual; olhos fechados e 1-2 bocas gerados por inpainting e recortados em retângulo.
- Piscar aleatório com `choice` e boca ligada a `config.speaking_attribute`.
- Opcional: shader `mesh` de balanço ou respiração restrito ao tronco.
- Opcional: separar 2-3 planos nos fundos das cenas mais importantes, para paralaxe real e foco com `blur`.
- **Decisão:** qual ferramenta de inpainting usar e quem garante a consistência (cor e alinhamento). Nada a comprar além do que já é usado para gerar a arte.

### Etapa 3: ambiciosa (esforço: alto, dias a semanas por personagem)
- **Opção A, Live2D para 1-2 personagens-chave** (ex.: a mentora ou o avatar do jogador), não para os 11.
  - Exige PSD em camadas: refazer a arte com um ilustrador, ou decompor e pintar a arte de IA.
  - Exige rigging no Cubism Editor (FREE pode bastar para um rig simples; PRO em teste de 42 dias, ou com desconto de estudante).
  - Instalar o Cubism SDK for Native da série 5.3 (R5+) e, se houver build web, o SDK for Web.
  - Usar wrapper com fallback para o PNG.
  - **Decisões:** quem publica (isenção de licença abaixo de 10 milhões de ienes por ano), plataformas-alvo (Android x86_64 e iOS têm restrições) e se vale o custo de manter dois estilos de personagem.
- **Opção B, loops em vídeo** (IA de vídeo ou render): idle de 3 s em WebM com `side_mask` para poucos personagens ou momentos especiais.
  - Menos técnico que Live2D, mas pesa em tamanho e na web.
  - **Decisão:** ferramenta de vídeo e direitos de uso do material gerado.
- **Não recomendo:** Spine (sem runtime oficial) e personagens 3D em tempo real (o `GLTFModel` não anima).

### O que precisaria ser decidido ou comprado
| Item | Quando | Custo |
|---|---|---|
| Nenhum | Etapas 1 e 2 | Só tempo |
| Ferramenta de inpainting consistente | Etapa 2 | Depende da ferramenta já usada |
| Cubism Editor PRO (opcional) | Etapa 3A | Preço não confirmado; teste de 42 dias; 76% de desconto para estudantes |
| Contrato de publicação Live2D | Etapa 3A, só se o publicador faturar 10 milhões de ienes ou mais por ano | Por obra; planos D/E/F/G |
| Artista para PSD em camadas e rigging | Etapa 3A | Maior custo real |
| Ferramenta de vídeo por IA ou render | Etapa 3B | Depende |

---

## O que não confirmei
- Nome e versão exata do zip atual do Cubism SDK for Native (a página não mostra sem o fluxo de download). Também não confirmei se modelos `.moc3` antigos (pré-5.3) abrem no core 5.3; a página da Live2D não afirma isso.
- Preço atual do Cubism Editor PRO.
- Se `u_model_size` vem preenchido com `mesh (x, y)`.
- O trecho de `zoom_zaxis` foi lido no código do `master` no GitHub, não no tag exato 8.5.3. O `.pyx` não vem no SDK, e no SDK só achei a definição em `renpy/config.py`.
- Nenhum exemplo de código deste relatório foi executado.

## Fontes consultadas
- Ren'Py, Live2D: https://www.renpy.org/doc/html/live2d.html (e `C:\Program Files (x86)\renpy-8.5.3-sdk\doc\live2d.html`)
- Ren'Py, 3D Stage: https://www.renpy.org/doc/html/3dstage.html (e `doc\3dstage.html`)
- Ren'Py, Model-Based Rendering (shaders, `mesh`, `GLTFModel`, GL properties): https://www.renpy.org/doc/html/model.html
- Ren'Py, Default Shader Parts: https://www.renpy.org/doc/html/shader_parts.html
- Ren'Py, Transform Properties (`zoom`, `blur`, `fit`): https://www.renpy.org/doc/html/transform_properties.html
- Ren'Py, ATL (`choice`, `parallel`): https://www.renpy.org/doc/html/transforms.html
- Ren'Py, Layered Images: https://www.renpy.org/doc/html/layeredimage.html
- Ren'Py, `config.speaking_attribute`: https://www.renpy.org/doc/html/config.html
- Ren'Py, Movie (`side_mask`): https://www.renpy.org/doc/html/movie.html
- Ren'Py, Changelog (8.5.3, 8.5.0, 8.4.0, 8.1, 7.4.6, 7.4.5): https://www.renpy.org/doc/html/changelog.html
- Ren'Py, Incompatible Changes (`zoom_zaxis`): https://www.renpy.org/doc/html/incompatible.html
- Código do SDK 8.5.3: `renpy/gl2/live2d.py`, `renpy/config.py:1599`, `renpy/defaultstore.py:187`, `launcher/game/install.rpy`
- Código-fonte Ren'Py (GitHub master): https://raw.githubusercontent.com/renpy/renpy/master/renpy/display/accelerator.pyx
- Live2D, SDK Release License: https://www.live2d.com/en/sdk/license/
- Live2D, Help (limite de 10 milhões de ienes): https://help.live2d.com/en/?p=2181
- Live2D, FREE vs PRO: https://www.live2d.com/en/cubism/comparison/
- Live2D, download do Editor: https://www.live2d.com/en/cubism/download/editor/
- Live2D, download do SDK for Native: https://www.live2d.com/en/sdk/download/native/
- Live2D, compatibilidade 5.3: https://docs.live2d.com/en/cubism-sdk-manual/compatibility-with-cubism-5-3/
- Spine runtimes: https://github.com/EsotericSoftware/spine-runtimes
- Fórum Spine sobre Ren'Py: https://de.esotericsoftware.com/forum/d/27841-has-anybody-tried-use-spine-in-renpy-with-python-runtime
