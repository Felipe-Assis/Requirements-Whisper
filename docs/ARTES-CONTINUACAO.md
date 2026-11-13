# Artes da continuação

Produzidas em 09/11/2026 com a ferramenta nativa `image_gen`, seguindo a skill imagegen. Não foi usado gerador por CLI. Os PNGs finais foram copiados para o repositório; as referências existentes foram preservadas.

| Arquivo | Uso narrativo | Formato | Inspeção |
|---|---|---|---|
| `images/characters/lia/neutral.png` | Lia, estudante adulta que participa da investigação dos gastos | 1024 × 1536, RGBA | Identidade própria, óculos redondos, cabelo cacheado curto, roupa prática oliva/branca/escura; corpo e pés completos |
| `images/characters/sabrina/rain.png` | Retorno de Sabrina ao suporte, uma semana depois, em dia chuvoso | 1024 × 1536, RGBA | Mesma identidade, gesto e tênis das referências; casaco leve com capuz abaixado e cabelo seco |
| `images/bg/suporte_chuva.png` | Atendimento no suporte durante a chuva | 1672 × 941, RGB | Mesma câmera e organização do suporte; chuva nos vidros, luz fria e luminárias quentes |

## Continuidade e validação

Lia usa a linguagem visual de contornos escuros finos, proporções de animação 2D e sombreamento pintado dos demais personagens. Ela tem rosto e cabelo próprios, sem reaproveitar a identidade de Sabrina.

A variante de Sabrina foi editada a partir de `images/characters/sabrina/neutral.png` e `images/characters/sabrina/return.png`. A face, o rabo de cavalo e o gesto continuam reconhecíveis. A roupa acompanha a mudança de semana e de clima: casaco impermeável leve aberto, camiseta clara, calça escura e os mesmos tênis. Ela está dentro da sala, com o cabelo seco, sem guarda-chuva cobrindo o sprite.

O cenário foi editado a partir de `images/bg/suporte.png`. A comparação visual confirmou porta, corredor, relógio, estantes, plantas, cadeiras, computadores, telefone, caderno e headset nas mesmas posições. A chuva fica no exterior; o piso interno continua seco. A luz direta alaranjada foi substituída pela luz difusa fria do tempo fechado, preservando a luz quente das lâmpadas.

Os dois sprites têm canal alpha real, cantos completamente transparentes e cobertura da personagem predominantemente acima de 240/255. O gerador entregou alpha máximo de 254, também observado na referência `return.png`; o canal foi preservado sem pós-processamento. Não foram adicionados fundos opacos nem sombras de chão. Os PNGs finais foram abertos e inspecionados visualmente antes da entrega.

## Proveniência

- Lia: geração nova, sem imagem de entrada; fonte `exec-e2184ff3-605c-4b35-bbed-c80e228a06a9.png`.
- Sabrina chuva: edição das duas referências locais indicadas acima; fonte `exec-80f29b87-05a0-45cf-925c-173503fb7e50.png`.
- Suporte chuva: edição do cenário local indicado acima; fonte `exec-101e8231-4465-46e2-bc22-034afa02dd9b.png`.
- Os três arquivos de origem foram entregues pelo gerador em `C:/Users/Felipe/.codex/generated_images/01a1c072-0cb9-7581-8359-b9d8a49a8f42/`; cópias finais ficam nos caminhos versionados da tabela. As referências anteriores permanecem sem substituição.
- Esta geração não altera os registros de origem ou licenciamento das artes preexistentes.

## Prompts enviados

### Lia

> Use case: illustration-story. Asset type: full-body transparent character sprite for a hand-drawn 2D visual novel set in a Brazilian university. Create Lia, a new and distinct adult Brazilian student in her twenties: medium-brown skin, short naturally curly dark-brown hair, round thin-frame glasses, warm attentive brown eyes, friendly thoughtful expression. Practical casual outfit: muted olive-green open overshirt, plain white T-shirt, dark charcoal trousers, comfortable off-white sneakers. Relaxed standing conversational pose, one hand making a small open gesture, the other loosely at her side. Coherent fine dark ink outlines, anime-inspired but grounded 2D animation character design, subtle painted texture, restrained highlights and warm skin shading. Single character centered on a tall 2:3 canvas, head and both feet completely visible with margin, proportions of an adult, no props. Genuine transparent RGBA background, clean alpha edges, no ground shadow, no haze or background glow, no scenery, no text, no logos, no watermark. This is an original character; do not copy another character's face or hairstyle.

### Sabrina com roupa de chuva

> Use case: identity-preserve. Asset type: transparent full-body visual novel sprite. Input image 1 is Sabrina neutral, the exact identity reference; input image 2 is Sabrina return, the outfit/polish reference. Create Sabrina visiting support one week later on a rainy day. Preserve Sabrina's exact identity, brown skin, black high ponytail, dark eyes, face proportions, friendly open smile, standing full-body proportions, same conversational palm-up gesture, fine dark ink contours and softly painted 2D shading. Change ONLY outfit to a lightweight muted blue-gray rain jacket, open over a plain cream T-shirt, dark navy trousers, same pale-blue sneakers. Hood lowered behind neck, hair dry and neatly tied, indoors after arriving from rain. Keep both hands visible, no umbrella, no bag. Full head and both shoes completely visible, same tall 2:3 framing. Genuine transparent RGBA background with clean alpha; remove all background, glow and ground shadow. No text, logos, scenery, watermark. This must read immediately as the SAME Sabrina, just appropriately dressed for rain.

### Suporte em dia chuvoso

> Use case: lighting-weather. Asset type: 16:9 hand-painted visual novel background. Edit the input support office into a rainy daytime version of the SAME room. Change only weather outside the right windows and the resulting lighting: overcast cool blue-gray sky, clearly visible fine rain streaks/droplets on the window glass, wet exterior building and foliage, cool soft diffuse daylight. Remove the orange sunset shafts and sunlit patches from floor and wall. Keep existing desk and ceiling lamps gently warm and switched on. Preserve exact room geometry, camera, door, corridor, clock, shelves, files, plants, all chairs, computers, phone, notebook, cables, headset and every prop position. Keep painterly 2D ink-and-color style, object outlines and perspective. Indoor floor remains dry; rain is outside only. Single edge-to-edge scene, no added people or objects, no text, labels, UI, logos, border or watermark. Match original landscape composition and aspect ratio.

