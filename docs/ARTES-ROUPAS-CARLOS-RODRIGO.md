# Roupas alternativas de Carlos e Rodrigo

Produzidas em 09/11/2026 com a ferramenta nativa `image_gen`, seguindo a skill imagegen no modo `identity-preserve`. As quatro referências foram abertas com `view_image` antes das edições. Não foi usado gerador por CLI nem Superdesign.

| Arquivo final | Referências | Uso | Formato |
| --- | --- | --- | --- |
| `images/characters/carlos/return.png` | Carlos `thinking.png` como alvo; `confident.png` como referência de identidade | Retorno ao laboratório na semana seguinte: camisa verde-sálvia de mangas dobradas, mantendo boné, calça e tênis | 1024 × 1536, RGBA |
| `images/characters/rodrigo/rain.png` | Rodrigo `thinking.png` como alvo; `serious.png` como referência de identidade | Retorno ao suporte na manhã chuvosa: casaco oliva aberto, capuz abaixado, camiseta listrada, calça e sapatos preservados | 1024 × 1536, RGBA |

## Conferência

A inspeção visual comparou rosto, cabelo, barba/bigode, óculos e boné quando presentes, proporções, gesto de mão no queixo, outra mão no bolso e posição dos pés. Ambos continuam reconhecíveis como os personagens das referências, com corpo inteiro e sem objetos novos. As roupas são diferentes e adequadas aos retornos previstos. Rodrigo não leva guarda-chuva e está seco dentro da sala.

Os PNGs têm transparência real: os quatro cantos têm alpha zero, assim como as amostras de fundo laterais. Carlos tem 1.131.645 pixels totalmente transparentes e 421.838 acima de 240/255; Rodrigo tem 1.096.792 pixels totalmente transparentes e 454.829 acima de 240/255. O alpha máximo gerado é 254, como em outras artes desta campanha. O canal original foi preservado, sem pós-processamento. As cores residuais dos pixels transparentes não constituem um fundo opaco.

Os arquivos foram copiados sem alteração para os destinos acima. Nenhum sprite preexistente foi substituído. A integração das declarações e cenas fica com o coordenador da campanha.

## Origem

Diretório de saída do gerador: `C:/Users/Felipe/.codex/generated_images/01a1c075-9dad-70a0-ad6a-916e24aaa5c4/`.

- Carlos: `exec-c71c4faa-6bb1-40e5-8a42-5a82dce704c0.png`.
- Rodrigo: `exec-378f15ed-7a55-48bf-aa72-e2affffaefa9.png`.

As saídas originais permanecem no diretório padrão do gerador; as cópias versionadas são as usadas pelo projeto. Esta edição não muda a procedência das referências preexistentes.

## Prompts enviados

### Carlos

> Use case: identity-preserve. Asset type: full-body transparent 2D visual novel character sprite, 1024x1536 portrait. Input image 1 (Carlos thinking) is the EDIT TARGET. Input image 2 (Carlos confident) is a supporting identity reference only. Edit Carlos for a laboratory follow-up meeting one week later. Preserve EXACT identity, face proportions, black hair, full black beard, glasses, navy baseball cap, skin tone, body proportions, head position, thoughtful closed-mouth expression and entire thinking pose from image 1: one hand at chin and the other in trouser pocket, legs and gray sneakers unchanged. Change ONLY clothing below the neck: replace the navy short-sleeve polo with a muted sage-green long-sleeve casual work shirt, sleeves neatly rolled to the elbows, plain buttons and collar, worn untucked with the same charcoal trousers and gray sneakers. This is the SAME Carlos in another practical working outfit, not a new character. Preserve fine dark outlines and original anime-inspired hand-painted 2D shading, character scale and full-body framing, head and both shoes entirely visible. Background must be genuinely transparent RGBA with clean alpha edges. Remove any smoky background, glow, vignette and ground shadow in the input; retain only the character. No new props, no text, no logos, no watermark, no scenery, no umbrella. Keep face/body/pose and cap unchanged.

### Rodrigo

> Use case: identity-preserve. Asset type: full-body transparent 2D visual novel character sprite, 1024x1536 portrait. Input image 1 (Rodrigo thinking) is the EDIT TARGET. Input image 2 (Rodrigo serious) is a supporting identity reference only. Edit Rodrigo arriving inside the support office during a rainy morning at 10:10, one week later. Preserve EXACT identity, medium-brown skin, short black hair with the same hairline, thick dark eyebrows, black moustache, short jaw stubble, dark eyes, face proportions, body proportions and thoughtful expression. Preserve the ENTIRE thinking pose from image 1: one hand at chin, other hand in trouser pocket, same leg stance, same full-body scale and framing. Change ONLY outfit by adding a practical lightweight dark olive rain jacket, open over the same cream/navy horizontally striped T-shirt. Rain jacket has a hood lowered behind the neck, no hood covering the head; sleeves go to wrists, carefully preserve hand-at-chin gesture and pocket-hand pose. Preserve the existing tan trousers and brown loafers. He is indoors after arriving, hair dry, no dripping water or rain around the sprite. Match exact fine ink contour and softly textured 2D illustrated style. Genuine transparent RGBA background, clean alpha edges; remove any smoky background, glow, vignette and ground shadow from the input. Show complete head and both shoes with margins. SAME Rodrigo, never a replacement face. No umbrella, bag, props, text, logo, watermark, scenery or added person.

