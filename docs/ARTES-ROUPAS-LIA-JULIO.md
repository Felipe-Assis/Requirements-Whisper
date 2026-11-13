# Roupa alternativa de Lia e Júlio

Geradas em 09/11/2026 pelo image_gen integrado, com edição identity-preserve e transparent_background=true. Nenhuma CLI ou Superdesign foi usada. Os sprites originais foram abertos com view_image antes da geração; permanecem intactos.

| Personagem | Referências locais | Entrega | Alteração |
| --- | --- | --- | --- |
| Lia | images/characters/lia/neutral.png | images/characters/lia/return.png | Camiseta ocre claro e cardigan azul escuro no lugar da camiseta branca e sobrecamisa oliva. Calça, tênis, óculos e brincos mantidos. |
| Júlio | images/characters/julio/neutral.png como alvo; images/characters/julio/thinking.png como apoio de identidade | images/characters/julio/return.png | Sobrecamisa azul petróleo e camiseta areia no lugar do blazer marrom e camiseta escura. Jeans e sapatos mantidos. |

As roupas se destinam ao retorno na semana seguinte. Lia só tinha uma referência disponível. A pose de Júlio é a neutral; a segunda referência serviu para preservar o mesmo rosto, sem importar a pose de reflexão.

## Verificação

Inspeção visual comparou os sprites antes/depois: cabelo, óculos, rosto e tom de pele de Lia preservados; cabeça, barba, traços e expressão de Júlio preservados. As mãos, o gesto e o corpo inteiro continuam visíveis, incluindo ambos os calçados. A roupa muda; o personagem permanece reconhecível no estilo da referência.

Os dois arquivos finais são PNG RGBA 1024×1536. Leitura do canal alpha confirmou pixels totalmente transparentes: 70,81% em Lia e 75,29% em Júlio, incluindo o canto superior esquerdo. Não foi feita remoção de fundo por código; a transparência foi produzida pelo image_gen. O intervalo alpha de ambos é 0–254, com bordas suavizadas. As cores escondidas em pixels transparentes podem aparecer no preview bruto da ferramenta, mas não formam um fundo opaco no jogo.

Nenhum script foi alterado nesta entrega.

## Prompt de Lia

```text
Use case: identity-preserve. Asset type: transparent full-body visual-novel character sprite.
Input image 1 is the EDIT TARGET, Lia's original neutral sprite. This is an outfit change for the SAME person at a return meeting one week later, not a new character.
Keep Lia's exact face shape, brown skin tone, large round thin metal glasses, brown eyes, short voluminous dark curly hair with the exact silhouette, eyebrows, nose, mouth and friendly neutral speaking expression; retain gold hoop earrings. Preserve her exact full-body pose, hand positions (one arm hanging, other forearm extended palm up), body proportions, height, full-body framing, camera, dark charcoal high-waisted wide trousers and off-white sneakers. Preserve original detailed ink-lined painterly illustration style.
Change ONLY her clothing from olive overshirt and white tee to a LIGHT OCHRE crew-neck T-shirt tucked into the same trousers, under an OPEN lightweight DARK NAVY BLUE cardigan with sleeves pushed to the same forearm height. Clothes have plausible soft folds, no logos, no patterns. Do not change limbs or hide hands.
Remove the original dark blurred background and warm halo completely. Output a genuinely TRANSPARENT background with alpha all around the clean silhouette and between the limbs; no halo, no ground shadow, no gradient, no checkerboard printed into image. Entire character including all hair, hands and both shoes visible, same framing and silhouette placement, no cropping. No text, no UI, no watermark. One sprite only.
```

## Prompt de Júlio

```text
Use case: identity-preserve. Asset type: transparent full-body visual-novel character sprite.
Input image 1 (neutral.png) is the EDIT TARGET and controls exact pose/framing/expression. Input image 2 (thinking.png) is a SUPPORTING IDENTITY reference of the SAME man; do not copy its thinking pose.
Create ONLY an outfit change of Júlio for a return meeting one week later. Keep his exact bald head shape, skin tone, dark eyebrows, dark eyes, nose and ear shapes, solid gray beard shape, open friendly speaking mouth and facial proportions. Do NOT create a different man. Preserve his original simple clean anime linework and shading, not a photoreal redesign. Preserve the full body framing and exact neutral pose: screen-left arm extended with open palm, other hand in trouser pocket, same stance and body proportions.
Change ONLY the brown blazer and black T-shirt to an OPEN dark TEAL-BLUE cotton overshirt with simple collar over a plain LIGHT SAND crew-neck T-shirt. The return outfit should read as practical neat casual work clothing. Preserve his same dark blue straight jeans and brown leather shoes unchanged. No patterns or logos, no accessories added.
Remove the original blurred warm dark background/halo completely. Output a genuinely TRANSPARENT alpha background outside the clean character silhouette and in gaps between limbs, no gradient, no colored halo, no printed checkerboard and no ground shadow. Entire head, both hands and both shoes visible, same placement and scale as image 1, no cropping. No text, UI, watermark or extra figure. One sprite only.
```

## Origem das cópias

Pasta padrão do image_gen: C:/Users/Felipe/.codex/generated_images/01a1c08b-0e1f-75e1-9dcb-dffc15bf06b1/

- Lia: exec-3557e634-0e05-4d5b-8884-6fdeac136bc1.png
- Júlio: exec-93024e28-5ab7-4628-ac6a-a87c460575c2.png

Os arquivos usados pelo jogo são as cópias finais em images/characters/, não os caminhos da pasta de geração.

