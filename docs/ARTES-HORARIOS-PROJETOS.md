# Artes dos projetos por horário

As quatro imagens abaixo são edições dos fundos existentes feitas com a ferramenta integrada `image_gen` em 9 de novembro de 2026. Não foi usado Superdesign nem CLI/API de geração. Os originais foram preservados.

| Arquivo final | Referência editada | Horário | Diferença visual |
| --- | --- | --- | --- |
| `images/bg/laboratorio_manha.png` | `images/bg/laboratorio.png` | 9h | Luz difusa neutra, folhas verdes e piso sem as faixas alaranjadas do fim da tarde. |
| `images/bg/startup_manha.png` | `images/bg/startup.png` | 9h | Manhã clara, luz suave e quadro branco sem o banho dourado do fundo original. |
| `images/bg/suporte_dia.png` | `images/bg/suporte.png` | 14h30 | Exterior diurno, sombras de tarde claras e relógio com minutos em 6 e horas entre 2 e 3. |
| `images/bg/suporte_manha.png` | `images/bg/suporte.png` | 9h | Luz difusa suave, exterior diurno e relógio com ponteiros em 9h. |

## Preservação e conferência

As referências foram abertas antes das edições. A comparação visual preserva o enquadramento, as posições dos móveis, janelas, plantas e objetos, a perspectiva e o estilo ilustrado. Laboratório e as duas variantes de suporte têm as mesmas dimensões dos originais (1672 × 941 pixels). A ferramenta retornou startup manhã com 1671 × 941 pixels, um pixel a menos de largura; o enquadramento foi preservado. Nenhum personagem ou elemento de interface foi acrescentado. Como são edições generativas, pequenos traços de textura podem variar.

A primeira saída de suporte diurno mostrou o ponteiro curto em 3; uma segunda edição corrigiu apenas esse ponteiro para a posição entre 2 e 3. As imagens finais foram inspecionadas junto aos originais. O fundo de chuva já existente não foi alterado.

## Proveniência

Diretório da sessão de geração: `C:/Users/Felipe/.codex/generated_images/01a1c08a-ce62-7a93-aadc-04301f80a350/`.

| Entrega | Saída integrada selecionada |
| --- | --- |
| Laboratório manhã | `exec-4a96e547-ba44-4ab0-9b52-f5423576fdfb.png` |
| Startup manhã | `exec-910e5521-f4a4-4c1a-9b69-9bd9c9fe4a70.png` |
| Suporte dia | `exec-10ad1b17-f645-49ed-90fb-3fed56416fb9.png` |
| Suporte manhã | `exec-02d02fcb-edb4-4ece-87db-78c26ffe983e.png` |

A saída intermediária `exec-26a1543b-aa16-44bc-84eb-87e17de1fc9e.png` serviu de alvo para a correção do relógio de suporte diurno e não foi incorporada ao jogo. As saídas selecionadas foram copiadas para o projeto; os arquivos da sessão de geração permanecem no local padrão da ferramenta.

## Prompts usados

### Laboratório manhã

```text
Use case: lighting-weather.
Asset type: 16:9 visual novel background, empty Brazilian university laboratory.
Input image 1 is the EDIT TARGET, not a style suggestion. Edit this exact room.
Primary request: change ONLY the time-of-day lighting to 09:00 in the morning: soft diffuse neutral daylight, fresh pale-blue sky outside, naturally green leaves, gentle broad shadows and soft highlights. Remove the strong golden-orange late-afternoon/sunset cast and long bright orange sunlight stripes. Keep the room readable and calm.
Invariants: preserve the exact camera, perspective, framing, aspect ratio, layout, geometry, linework and painterly illustrated style. Preserve every piece of furniture and every object in precisely the same position and size: microscope, benches, shelves, test tubes, clipboards, plants, Brazilian flag, computer, chair with lab coat, stool, backpack, windows and exterior architecture. Keep the flag as in reference without adding lettering.
Avoid: redesign, moving/replacing objects, new objects, people, logos, text, interface, watermarks, photorealism. Produce a single full-frame background, same landscape 16:9 composition, ideally 1672x941 matching input.
```

### Startup manhã

```text
Use case: lighting-weather.
Asset type: full-frame 16:9 visual novel background.
Input image 1 is the EDIT TARGET. Modify this exact startup office only.
Primary request: same room at 09:00 on a clear bright morning. Replace the orange golden-hour/sunset illumination with fresh soft neutral morning daylight through the windows, pale-blue morning sky, natural green foliage, a balanced brighter interior with gentle soft shadows. The sunlight should be subtle, pale and diffuse; remove long orange shadows and the strong orange wash across desk and floor.
Invariants: retain exact camera perspective, framing, room dimensions, all furniture and objects at their precise original coordinates and sizes, the same illustrated painterly linework. Preserve foreground laptop, phone, papers, mug, notebooks, backpack and corkboard; preserve sofa, cushions, shelves, plants, whiteboard and sticky-note arrangement, meeting chairs and table, desks, monitors, windows, outdoor buildings and trees.
Avoid: redesign, new objects, removing or relocating objects, people, logos, readable text, UI, watermark. Output a single landscape full-frame 16:9 background, ideally 1672x941 to match input.
```

### Suporte dia

```text
Use case: lighting-weather.
Asset type: 16:9 visual novel background of an empty university IT support office.
Input image 1 is the EDIT TARGET, preserve this exact room.
Primary request: change ONLY lighting and time of day to 14:30, early afternoon. Through the windows, replace twilight and sunset with clear pale-blue daylight and naturally green trees, keeping exact buildings/trees geometry. The interior should receive broad neutral daylight and some soft, short afternoon shadows; remove orange sunset streaks and purple/dark-blue twilight outside. Existing desk/ceiling lamps may keep their understated light.
Clock synchronization: preserve the exact existing round wall clock face, rim, position and size, but set its hands to 14:30 (minute hand straight down at 6, short hour hand halfway between 2 and 3). Make these two hands visibly accurate and simple.
Invariants: exact camera, perspective, framing, aspect ratio and illustrated painterly style; every furniture piece and object at precisely the same coordinates and sizes. Preserve two foreground monitors, chairs, notebook, headset, telephone, note papers, trays, plants, shelving/binders, open door and corridor, repair workbench with computer, tools, cable coils, corkboard, row of waiting chairs, windows/blinds and exterior architecture.
Avoid: room redesign, objects moved/added/removed, people, readable text, logos, UI, watermarks, night or sunset sky. Single full-frame landscape composition, ideally 1672x941 matching input.
```

### Correção do relógio de suporte dia

Alvo: a primeira saída de suporte diurno.

```text
Use case: precise-object-edit.
Input image 1 is the edit target. Edit ONLY the small black hour hand inside the existing round wall clock centered around x635 y132. Everything else must be pixel visually identical: same camera, geometry, daylight, objects, textures, scene, framing, illustration, colors.
The intended time is 14:30 / two thirty. Keep the long black minute hand pointing straight DOWN toward the bottom six o'clock tick. Move ONLY the SHORT black hour hand: from its current horizontal-right direction toward a diagonal UP-RIGHT direction, halfway between the two and three o'clock ticks, approximately 15 degrees above horizontal right (75 degrees clockwise from straight up). Short hand tip must be above the center. Make it clearly 2:30, NOT 3:30. Preserve all existing tick marks and rim. No other change, no text, no people, no logo, no watermark. Preserve exact input dimensions 1672x941.
```

### Suporte manhã

```text
Use case: lighting-weather.
Asset type: 16:9 visual novel background of an empty university IT support office.
Input image 1 is the EDIT TARGET. Preserve this exact room.
Primary request: change ONLY lighting and time of day to 09:00, soft morning. Replace twilight through the windows with pale-blue daytime sky, naturally green trees and the same exterior buildings. Broad soft diffuse neutral morning daylight fills the room. Remove orange sunset stripes, long dramatic light bands and purple/dark-blue sky. Gentle low-contrast shadows, fresh calm morning atmosphere.
Clock synchronization: keep existing round wall clock face, rim, location and size; set exactly 09:00 with long minute hand pointing vertically UP to twelve, and short hour hand pointing horizontally LEFT to nine. Clearly show those two simple black hands. No other clock changes.
Invariants: exact camera, perspective, framing, aspect ratio and illustrated painterly style; every furniture piece and object at precisely the same coordinates and sizes. Preserve two foreground monitors, chairs, notebook, headset, telephone, note papers, trays, plants, shelving/binders, open door and corridor, repair workbench with computer, tools, cable coils, corkboard, row of waiting chairs, windows/blinds and exterior architecture. Preserve existing lamps, reduce their visual dominance under daylight.
Avoid: redesign, objects moved/added/removed, people, readable text, logos, UI, watermarks, sunset, night. Single full-frame landscape composition, ideally 1672x941 matching input.
```

