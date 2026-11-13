# Mesa do campus sem caderno pintado

Em 09/11/2026, o image_gen integrado produziu duas edições precise-object-edit. As referências foram abertas com view_image antes da geração e enviadas por referenced_image_paths.

Estas variantes preparam a mesa para receber um sprite interativo de caderno. O caderno pintado no centro inferior do fundo provocava duplicação visual quando o jogo acrescentava esse sprite.

| Alvo de edição | Arquivo final | Remoção |
| --- | --- | --- |
| images/bg/campus.png | images/bg/campus_mesa.png | Caderno espiral inteiro no centro inferior: páginas, espiral, capa e os dois post-its sobre suas páginas. |
| images/bg/campus_noite.png | images/bg/campus_noite_mesa.png | A mesma remoção na variante de noite. |

A região foi preenchida com madeira de continuidade visual coerente com o tampo. Não houve mudança de horário: a imagem diurna mantém sol e sombras das folhas; a noturna mantém exterior azul e luz artificial interna confortável.

## Inspeção visual

As saídas foram comparadas visualmente com as duas bases. O centro inferior mostra somente madeira, sem contorno residual do caderno. O livro aberto separado à direita permanece, assim como lápis, caneta, bloco de notas, post-its avulsos à direita, estojo, garrafa, pilha de livros, porta-lápis e canecas. Cadeiras, mochila, quadro, janelas e plantas mantêm sua disposição. O enquadramento continua 1672×941.

As bases originais e a documentação das gerações anteriores não foram alteradas. Esta entrega não muda scripts, hotspots ou regras do jogo.

## Prompt diurno

```text
Use case: precise-object-edit. Asset type: visual novel background clean plate for an interactive notebook overlay.
Input image is the EDIT TARGET: this exact daylight classroom.
Remove ONLY the entire large open SPIRAL NOTEBOOK in the CENTER BOTTOM FOREGROUND, including both lined pages, spiral rings, teal cover/binding, and the two lavender sticky notes sitting ON those pages. Reconstruct the uncovered warm wooden tabletop underneath it, matching this exact table's perspective, continuous wood grain, texture and daylight/leaf-shadow illumination. The restored area must contain only natural wood, no notebook residue, no rectangle outline and no replacement object.
Preserve ALL OTHER pixels/objects as closely as possible: the separate open book at right MUST STAY, the pencil and pen at lower right MUST STAY, the sticky-note pad and separate pink/lavender notes at far right MUST STAY, the pencil case and bottle at left MUST STAY, the stacked books and pencil cup MUST STAY. Preserve all mugs, chairs, backpack, desks, windows, plants, board, wall, background geometry and original camera exactly. Keep the original sunny afternoon colors and shadows; do not change time of day or style. Do not crop, zoom, move objects, add people, text, UI, logos or watermark. Preserve exact wide framing and original illustrated painterly style. Return one opaque wide image.
```

## Prompt noturno

```text
Use case: precise-object-edit. Asset type: visual novel background clean plate for an interactive notebook overlay.
Input image is the EDIT TARGET: this exact nighttime classroom.
Remove ONLY the entire large open SPIRAL NOTEBOOK in the CENTER BOTTOM FOREGROUND, including both lined pages, spiral rings, teal cover/binding, and the two lavender sticky notes sitting ON those pages. Reconstruct the uncovered warm wooden tabletop underneath it, matching this exact table's perspective, continuous wood grain, texture and warm artificial interior lighting. The restored area must contain only natural wood, no notebook residue, no rectangle outline and no replacement object.
Preserve ALL OTHER pixels/objects as closely as possible: the separate open book at right MUST STAY, the pencil and pen at lower right MUST STAY, the sticky-note pad and separate pink/lavender notes at far right MUST STAY, the pencil case and bottle at left MUST STAY, the stacked books and pencil cup MUST STAY. Preserve all mugs, chairs, backpack, desks, windows, plants, board, wall, background geometry and original camera exactly. Keep the same deep-blue night outside, warm and comfortably bright artificial lighting inside and soft shadows. Do not introduce sunlight or leaf-shaped sun patches, change time of day or change style. Do not crop, zoom, move objects, add people, text, UI, logos or watermark. Preserve exact wide framing and original illustrated painterly style. Return one opaque wide image.
```

## Origem das cópias

Pasta padrão do image_gen: C:/Users/Felipe/.codex/generated_images/01a1c08b-0e1f-75e1-9dcb-dffc15bf06b1/

- Diurna: exec-8993fd80-62a8-42e0-9db8-5f47aad0be92.png
- Noturna: exec-906733f3-239d-4d47-adca-49761e6a0304.png

As cópias que devem ser consumidas pelo jogo estão em images/bg/.

