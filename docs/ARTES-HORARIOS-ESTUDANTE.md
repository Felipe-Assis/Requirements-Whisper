# Horários dos cenários do estudante

Revisão de integração: a arte do quarto recebeu uma correção posterior dos ponteiros para 20h, documentada em [ARTES-CENARIOS.md](ARTES-CENARIOS.md). O roteiro final usa 08h na abertura e 20h no planejamento. O prompt abaixo conserva o pedido original da primeira geração, antes dessa correção.

As três variantes foram produzidas pelo image_gen integrado em 09/11/2026, no modo de edição lighting-weather. Cada base foi aberta com view_image antes da edição e fornecida como referenced_image_paths. Os originais permanecem intactos. Não houve CLI nem Superdesign.

## Entregas e inspeção visual

| Base | Variante final | Horário | Inspeção antes/depois |
| --- | --- | --- | --- |
| images/bg/campus.png | images/bg/campus_noite.png | 20h, grupo de estudo | A base tinha sol e sombras de folhas. A variante remove essas sombras, troca o exterior por azul noturno e mantém a sala clara com iluminação artificial quente suave. Quadro, caderno aberto, livros, cadeiras, mochila e plantas mantêm posição e escala. |
| images/bg/oficina.png | images/bg/oficina_dia.png | 16h, visita ao mural | A base tinha exterior azul de fim de dia e janelas/poste acesos. A variante tem céu diurno, casas sem brilho artificial e luz solar entrando pela janela, com sombras de folhas no piso. Mural, protótipos, materiais, bancos e mesa permanecem no lugar. Madeira quente e paredes azuis continuam reconhecíveis. |
| images/bg/quarto_ilustrado.png | images/bg/quarto_noite.png | 20h, organização da semana após a revisão | A base tinha exterior diurno e manchas solares fortes. A variante mostra céu azul profundo, janelas urbanas acesas e luz âmbar do abajur; piso e paredes têm sombras suaves. Notebook continua fechado e na mesma posição; mesa, cadeira, mochila, cama, fotos e plantas preservadas. |

As três imagens finais mantêm enquadramento 16:9, estilo ilustrado, mapa de objetos e áreas de interação. Não foram acrescentados personagens, texto legível, UI ou cenas extras. A avaliação foi visual, comparando as imagens abertas antes e depois; não se afirma igualdade pixel a pixel.

## Prompts finais

### Campus, 20h

```text
Use case: lighting-weather. Asset type: visual novel 16:9 illustrated background, no characters.
Input image: EDIT TARGET, the campus classroom in the supplied local image.
Primary request: Change ONLY time of day and illumination to 20:00 at night for a comfortable evening study group. Preserve the exact image composition, camera, perspective, architecture, every desk/chair, whiteboard, plants, bookshelf, bag, bottle, books, open foreground notebook, stationery and their exact positions and scale. Do not draw people.
Lighting: The exterior through the existing windows must clearly be night, deep blue sky and dim blue courtyard with gentle warm light in the distant building. Remove all sunlight beams and leaf-shaped sunlight shadows inside. Interior remains comfortably BRIGHT and easy to read under soft, warm-neutral overhead artificial light from outside the framing: warm wood highlights, softly lit pale board, blue chairs, natural indoor green plants. Keep every corner sufficiently legible; avoid dramatic darkness and avoid a flat blue overall filter. Shadows should be soft and consistent with interior overhead lighting.
Preserve the original painterly anime illustration texture and the exact 16:9 full framing. Add no new objects, no fixtures, no text, no UI, no labels, no watermark. This is a lighting edit of this exact room, not a redesign. Produce one finished wide image only.
```

### Oficina, 16h

```text
Use case: lighting-weather. Asset type: visual novel 16:9 illustrated background.
Input image: EDIT TARGET, the workshop room supplied.
Primary request: Change ONLY time of day and illumination to 16:00 in the afternoon for visiting the community workshop's corkboard. Preserve the exact camera, perspective, room layout, corkboard papers and diagram, teal walls and beams, plants, window, shelves, wooden bench, stools, foreground table with paper phone prototypes, scissors, ruler, markers, cups and bottle, all their positions and scale.
Lighting: Through the existing right window show a bright late-afternoon pale blue sky and the SAME nearby hillside homes in natural daylight, with streetlight and home windows no longer glowing. Afternoon sunlight enters from that existing window, casts physically consistent directional highlights on the floor and tabletop, and gently warms the interior. Existing hanging lamps may have a subtle weak warm glow; sunlight is the dominant light. Board and paper mockups must remain clearly readable as blank graphical shapes. Teal remains teal, warm wood remains warm, white papers remain cream. Not dusk and not night.
Preserve the painterly anime illustration style and exact 16:9 full framing. Add no people, new objects, writing, UI, labels or watermark. This is a time-of-day edit of this exact workshop, not a redesign. Produce one finished wide image only.
```

### Quarto, 21h

```text
Use case: lighting-weather. Asset type: visual novel 16:9 illustrated background.
Input image: EDIT TARGET, supplied student's bedroom.
Primary request: Change ONLY time of day and lighting to 21:00 at night while the student organizes the week. Preserve the exact camera/perspective, wardrobe, bed, desk, chair, backpack, bottle, shelves, plants, photo grid, curtains, notebook and pen, alarm clock, and the CLOSED dark-blue laptop on the desk with their exact positions and scale. Laptop stays closed. Keep the same entire window with same distant Rio hills and buildings.
Lighting: Outside that existing window is clearly late evening/night, deep navy-blue sky, dark green foliage, distant city windows with subtle warm illuminated dots. NO sunset, NO sunlight streaks or leaf-shaped sun patches anywhere indoors. Existing desk lamp is on and casts a warm amber pool on the desk, closed laptop, notebook and wall nearby. Soft warm indoor ambient light keeps the entire bedroom gently readable, including bed, backpack, floor and wardrobe; floor has soft low-contrast shadows rather than sunlight patches. Overall comfortable calm mood, with warm-neutral interior contrasting with blue nighttime window, retaining teal walls and wood colors. Do not make the room gloomy, do not blue-tint the entire interior, do not add any lamps/fixtures.
Preserve the original detailed painterly anime illustration texture and exact full 16:9 framing. Add no people, objects, text, UI, labels or watermark. This is a lighting edit of this exact room, not a redesign. Produce one finished wide image only.
```

## Arquivos da geração

Pasta padrão do image_gen: C:/Users/Felipe/.codex/generated_images/01a1c08b-0e1f-75e1-9dcb-dffc15bf06b1/

- Campus: exec-a19fc0b5-2eef-47a9-82a1-2d1361f0f3c8.png
- Oficina: exec-492919a3-10c8-46fb-9458-a87dc675a92f.png
- Quarto: exec-5d5ee1fb-085a-448e-b567-63117f5f7b83.png

As cópias finais estão em images/bg/ no checkout do projeto e são os arquivos que devem ser usados pelo jogo.

