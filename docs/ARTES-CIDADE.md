# Cidade: dia e noite

Artes produzidas em 09/11/2026 com `image_gen` nativo, sem CLI ou Superdesign. O dia foi criado com referências locais de estilo; a noite é uma edição da mesma imagem, preservando a arquitetura e o enquadramento.

| Arquivo | Uso | Formato |
|---|---|---|
| `images/bg/cidade_dia.png` | Mapa opcional da cidade, aproximadamente 16h | 1672 × 941, RGB |
| `images/bg/cidade_noite.png` | Deslocamento para o curso, aproximadamente 20h | 1672 × 941, RGB |

## Direção e continuidade

A rua reúne a entrada do campus à esquerda, um ponto de ônibus no centro e a oficina comunitária à direita. Portão, portas e banco ficam visíveis, com calçada contínua e faixa de pedestres no primeiro plano. Não há pessoas grandes, texto legível ou controles desenhados na arte.

A pintura usa contornos finos, materiais com textura, paredes claras, tons verde-azulados e vegetação brasileira, em continuidade com `campus.png`, `oficina.png` e `startup.png`. A oficina vista pela porta retoma o mural, as mesas e os papéis do ambiente interno.

A noite mantém as entradas abertas, construções, árvores, ponto de ônibus, poste, fios e marcações da rua nas mesmas posições. A luz solar foi substituída por iluminação ambiente azul e luz quente na oficina, nas janelas do campus e sob o abrigo. O piso permanece seco. Uma luminária extra que apareceu no poste durante a primeira edição noturna foi removida numa revisão pontual para preservar a silhueta do poste diurno.

As duas imagens finais foram abertas e comparadas visualmente. As áreas de destino são legíveis também à noite. No arquivo original, os centros aproximados são campus em (300, 500), ponto em (850, 540) e oficina em (1400, 520). São referências para posicionamento; os controles devem ser conferidos no recorte real do jogo, pois o quadro lateral usa `fit cover` e não tem proporção 16:9.

## Proveniência

Diretório de saída nativo: `C:/Users/Felipe/.codex/generated_images/01a1c072-0cb9-7581-8359-b9d8a49a8f42/`.

- Dia: `exec-7faeb3a6-0b6f-4fe6-8ae3-4c83e3c364d4.png`. Entradas: `images/bg/campus.png`, `images/bg/oficina.png` e `images/bg/startup.png`, apenas como referências de estilo.
- Primeira edição noturna: `exec-93bfd64c-96d9-4858-8716-ca36f3fd5566.png`, não usada no jogo por acrescentar luminária no poste.
- Noite final: `exec-cbc2012c-fc3f-4625-909d-454f6b58ff4d.png`. Entradas: primeira edição noturna como alvo e dia como referência da silhueta do poste.
- As referências existentes foram preservadas. Os arquivos finais estão copiados nos caminhos versionados da tabela; os controles e horários continuam sob responsabilidade do motor.

## Prompts enviados

### Dia, 16h

> Use case: illustration-story. Asset type: production landscape 16:9 background for the SAME hand-painted 2D Brazilian university visual novel as the three reference images. References are STYLE ONLY: delicate dark ink outlines, painted textured shading, warm honey light against muted teal-blue shadows, natural Brazilian trees and lived-in buildings. Create one coherent Brazilian university-neighborhood street at 16:00 in clear weather, no people. Wide eye-level view from opposite sidewalk, showing three easily identifiable destinations in a single shared scene: at LEFT a modest university campus entrance with pale ochre academic building, low brick-tile roof, courtyard gate and leafy trees; at RIGHT a small community workshop/center, warm cream plaster walls with faded teal lower paint, broad open doorway showing craft tables, colored paper and a noticeboard, red tile roof. BETWEEN them near the street center is a simple covered city bus stop with bench and an empty plain route sign, clearly recognizable, no bus. Their distinct doors must be fully visible and reasonably large for game hotspots. A continuous sidewalk and quiet asphalt road connect them, a crosswalk in the near foreground. Brazilian neighborhood scale, plausible utility poles, tropical foliage, no luxury architecture. Late-afternoon sunlight from upper left, soft long shadows but sky still blue. Entire canvas is actual scene, no border or empty strip; avoid deep foreground objects blocking entrances. Keep the room-background level of detailed painted materials, not photographic or oil-impressionist. Single scene, no collage, no characters, no large people, no text or legible lettering, no logos, no UI, no watermark.

### Noite, 20h

> Use case: lighting-weather. Asset type: production 16:9 background for a 2D visual novel. EDIT this exact daytime Brazilian neighborhood into the SAME view at 20:00, after sunset. Change ONLY time-of-day lighting: deep natural blue evening sky with a few faint stars, cool blue ambient shadows, warm practical light spilling from the community workshop doorway on the right, warm light through a few university windows on the left, soft practical light under the bus shelter and from an existing street light source. Remove all direct sunlight, golden sun shafts and sharp sunlit patches; keep the ground dry and the atmosphere calm. Keep every building, door, gate, tree, wall, bench, bus shelter, sign, utility pole, overhead wire, plant, pavement marking and crosswalk in exactly the SAME place, with the same geometry, viewpoint, scale and crop. Campus gate remains open as in reference, workshop doorway remains open; no new objects or people. Preserve the fine ink lines and painterly textured 2D materials of the input. Retain enough shadow detail to see all three destinations clearly, avoid crushed blacks, no fog or rain, no glowing fantasy elements, no text or legible lettering, no logos, UI, border or watermark.

### Correção pontual da silhueta do poste

> Use case: precise-object-edit. Edit target image 1 is the completed NIGHT street. Supporting image 2 is the DAY version and is a reference ONLY for the original utility pole silhouette. Make exactly ONE small correction: remove the curved streetlamp arm, lamp shade and visible bulb that were newly added to the tall utility pole in the upper-right sky. Restore that pole to the plain DAY pole silhouette with its original overhead cables, no projecting lamp arm. Preserve the NIGHT time of day, exact camera, every building, door, open gate, bus shelter, lit shelter lamp, bench, foliage, pavement markings, stars and all other details. The workshop and shelter still cast warm light; retain readable cool-blue night ambient light, keep the image otherwise unchanged. Do NOT revert to daylight. Do not add anything. Same dimensions and crop, no text or watermark.

