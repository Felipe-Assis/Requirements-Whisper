# Objetos clicáveis separados

Artes produzidas em 09/11/2026 com `image_gen` nativo, seguindo a skill imagegen. Foram feitas quatro gerações individuais, sem atlas, CLI, Superdesign ou alteração dos fundos.

| Arquivo | Objeto | Dimensões | Referência |
|---|---|---|---|
| `images/objects/clipboard.png` | Prancheta com ficha, papéis e clip metálico | 1254 × 1254, RGBA | `images/bg/laboratorio.png` |
| `images/objects/phone.png` | Smartphone vertical levemente inclinado, tela escura e suporte discreto | 1254 × 1254, RGBA | `images/bg/startup.png` |
| `images/objects/laptop.png` | Computador portátil aberto em vista 3/4, tela escura | 1254 × 1254, RGBA | `images/bg/startup.png` |
| `images/objects/notebook.png` | Caderno de papel aberto, espiral central e marcadores lilás | 1536 × 1024, RGBA | `images/bg/campus.png` |

## Direção e verificação

Os objetos usam contornos escuros finos, textura pintada e iluminação neutra quente para acompanhar os cenários existentes. As referências serviram para material, perspectiva e estilo; nenhuma sala foi incorporada ao arquivo de objeto. Todos os objetos estão inteiros, sem texto legível, logotipo, controle ou etiqueta embutida. As teclas do laptop, a tela do celular e as folhas ficam sem informação funcional.

As quatro saídas foram inspecionadas visualmente e tiveram o canal alpha verificado por leitura do PNG. Prancheta, telefone e laptop apresentam alpha de 0 a 255; caderno de 0 a 254, padrão também observado em sprites anteriores do gerador. A transparência foi preservada sem remoção de fundo por cor nem pós-processamento. A área transparente permite sobrepor o objeto ao cenário; nome discreto, foco, hover e ação devem ser desenhados pelo motor.

O prompt pediu tela quadrada de 1024 pixels, mas o gerador integrado entregou as dimensões da tabela. Os originais foram preservados para que o jogo determine o tamanho de exibição. Não foi feito redimensionamento destrutivo apenas para impor 1024.

Para conferir escala e posição, estes são os limites aproximados da silhueta principal (alpha >= 128), em pixels do arquivo original; coordenadas no formato esquerda, topo, direita, base:

- Prancheta: `(114, 92, 1138, 1172)`.
- Telefone: `(310, 64, 961, 1205)`.
- Laptop: `(21, 111, 1236, 1127)`.
- Caderno: `(6, 133, 1534, 892)`.

Esses limites documentam o conteúdo; não são hotspots fixos. A área clicável precisa acompanhar a imagem redimensionada no jogo e sua silhueta. O hover deve destacar o mesmo objeto, preservando posição e proporção.

## Proveniência

Saídas originais em `C:/Users/Felipe/.codex/generated_images/01a1c072-0cb9-7581-8359-b9d8a49a8f42/`, copiadas para os caminhos locais da tabela:

- Prancheta: `exec-b4f2528d-e4a8-48a6-956f-bf3957c23ccf.png`.
- Telefone: `exec-be638d73-d3dd-4d24-b6cc-56f2c4398722.png`.
- Laptop: `exec-7bc4ac55-cc7c-4eaa-9c5a-551f73480dcd.png`.
- Caderno: `exec-2819354c-1c86-4834-898a-bbc7e4c5b41e.png`.

## Prompts enviados

### Prancheta

> Use case: illustration-story. Asset type: single transparent inventory/point-and-click object overlay for a hand-painted 2D visual novel. Input reference is a STYLE and MATERIAL reference only, not a scene to reproduce. Create one complete clipboard for an equipment preparation sheet: modest brown hardboard with silver metal clip, a short stack of cream paper firmly clipped to it, one preparation sheet on top with a few drawn empty checkboxes and faint neutral horizontal rules, NO legible text or letters. Match the clipboard/materials in the laboratory reference, thin dark ink contours and softly painted textured shading, warm-neutral studio illumination. Slight three-quarter overhead view as if resting on a tabletop, top points gently toward upper-right. Show the entire object with all corners and clip visible, centered in a square 1024x1024 canvas with a small clean transparent margin. Standalone single object only; do not depict any tabletop, scenery, hands, person, border, UI, logo or watermark. Actual transparent RGBA background, clean alpha silhouette, no drop shadow, no glow, no background haze. Production usable object sprite.

### Telefone

> Use case: illustration-story. Asset type: single transparent object overlay for a hand-painted 2D visual novel. Input reference is STYLE and MATERIAL reference only, not a scene to reproduce. Create a single unbranded modern smartphone with dark graphite-blue case, blank dark glass screen with a restrained soft warm reflection, no UI or text. Phone in portrait orientation, standing upright with a gentle backward lean like the foreground phone in the startup reference, seen in a natural slight three-quarter view; a very small plain folding support behind it is allowed only if needed to make the standing pose physically plausible. Thin dark ink contours and softly painted textured shading, matching the reference's objects; neutral-warm illumination. Entire phone visible, top and bottom uncropped, centered with small transparent margin in a square 1024x1024 canvas. Standalone object sprite only, actual transparent RGBA background with clean alpha silhouette; no tabletop, room, hands, scenery, ground shadow, glow, background haze, text, logo, letters, symbols, UI, watermark or border.

### Laptop

> Use case: illustration-story. Asset type: single transparent object overlay for a hand-painted 2D visual novel. Input reference is STYLE and OBJECT reference only, do not recreate the room. Create one open unbranded laptop matching the foreground laptop in the startup reference: graphite/dark slate housing, screen open at about 105 degrees, visible keyboard and broad trackpad, blank dark glass display with soft restrained warm reflections. No letters or logos on the keys or display. Natural three-quarter frontal elevated view as if on a desk, the whole laptop seen clearly, slightly turned so its right side recedes, screen and base both intact. Thin dark ink contours, softly painted textured shading, neutral-warm illumination, consistent with the illustrated reference. Center on a square 1024x1024 canvas, laptop uses most of available width with clean small margin; entire object and all corners visible. Actual transparent RGBA background, clean silhouette and no attached shadows outside laptop. No tabletop, other objects, scenery, hand, person, background haze, glow, cast shadow, UI, text, symbols, brand, watermark or border. Single production object sprite only.

### Caderno

> Use case: illustration-story. Asset type: single transparent object overlay for a hand-painted 2D visual novel. Input reference is STYLE and OBJECT reference only, do not recreate the classroom. Create one open spiral-bound paper notebook matching the foreground study notebook in the campus reference, plain muted teal cover visible underneath, cream paper pages with delicate pale blue-gray rules, metal central spiral binding, one or two small pastel lavender sticky tabs on the pages. NO written words, numbers, letters or legible text. A paper notebook, NOT a laptop computer. Natural three-quarter overhead view as if resting flat on a study table, both left and right pages fully visible and mostly open flat; slightly angled but not extreme. Thin dark ink contours and softly painted textured shading, warm-neutral illumination, consistent with reference's materials. Entire object centered and all corners visible, uses most of square 1024x1024 canvas with a small clean transparent margin. Standalone notebook only, no pens or extra loose items. Actual transparent RGBA background and clean silhouette, no tabletop, room, person, hand, floor, background haze, glow, cast shadow, UI, logo, brand, symbols, watermark or border.

## Base da mesa sem objetos repetidos

`images/bg/startup_mesa.png` é uma edição de `images/bg/startup.png` para receber os objetos clicáveis separados, mantendo 1672 × 941 pixels RGB. Foram removidos apenas o laptop aberto, o celular com base e os cadernos do primeiro plano; as áreas foram preenchidas com a madeira da mesa. Isso evita que a imagem de objeto apareça sobre outra cópia já pintada no fundo.

A inspeção do original e da saída antes da cópia confirmou os recibos, plantas, mural, caneca com descanso, mochila, cadeiras, móveis, câmera e direção de luz preservados. O arquivo original não foi substituído. O resultado não representa outro horário: é a base interativa da mesma cena.

Origem: `exec-135e2925-0047-462a-9029-29fefa9826b0.png`, no mesmo diretório nativo das demais gerações. Ferramenta: `image_gen` nativo, com `startup.png` como alvo de edição.

### Prompt da base da mesa

> Use case: precise-object-edit. Asset type: clean plate background for a 2D visual novel with separately clickable object sprites. Edit this exact startup room image. Remove ONLY these THREE groups of objects from the FOREGROUND desk: (1) the entire open laptop in the lower center, including screen, keyboard, base and its own cast shadow; (2) the entire upright smartphone and its little stand at lower left; (3) the closed teal/navy spiral notebooks stacked at lower right next to the backpack. Fill only those removed object areas with continuous wooden tabletop that matches the existing grain, perspective, painted texture, reflections, and warm sunlight. The desk must appear convincingly empty at these three former object positions so separate interactive sprite images can be overlaid there. Everything else is a strict invariant: keep exact camera, geometry, scene dimensions and crop; all plants and their pots, the loose paper receipts on the foreground desk, the coffee mug and coaster, the cork noticeboard with its pinned papers behind the mug, the backpack at the far right, every chair, sofa, shelf, meeting table, background computer monitors, window frame, trees, lamps, light direction and color grading must stay unchanged. Do not remove the corkboard or papers; do not remove the mug, backpack or receipts. Do not introduce a new object, rearrange furnishings, change time of day or restyle the painting. Entire canvas remains the scene. No people, text, labels, logos, UI, border or watermark.


