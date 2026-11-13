# Arte da interface de diálogo

A moldura foi produzida em 09/11/2026 com o gerador integrado `image_gen`. É uma borda editorial transparente em verde petróleo e cobre, separada da fala e do fundo de leitura. Não houve nova chamada ao Superdesign para esta arte.

| Campo | Registro |
|---|---|
| Arquivo no jogo | `images/ui/dialogue_frame.png` |
| Saída do gerador | `C:/Users/Felipe/.codex/generated_images/01a1becc-0f40-7151-9f0a-a2b044f2d1c3/exec-a49e6b7f-6060-4ac7-9ea1-cffa8bd84f10.png` |
| Dimensões | 2172 × 724 pixels |
| Formato | PNG RGBA; canal alpha de 0 a 255 |
| SHA256 da cópia integrada | `d91e0f2e2602eb9b34c514ddf7bd852af3423d138129e649d9ff7fc46f550502` |
| Uso | Contorno da caixa de diálogo, como camada sobre o fundo e sob o texto nativo |

## Direção e integração

A direção visual registrada é uma borda fina em verde petróleo com detalhes de cobre, sem texto, retratos ou controles incorporados. Essa descrição resume a direção da imagem; não é uma transcrição literal do prompt de geração.

O motor usa o arquivo original com recorte e bordas redimensionáveis:

```python
Frame(Crop((18, 77, 2138, 571), "images/ui/dialogue_frame.png"), 38, 38)
```

O recorte remove a margem transparente externa na composição. `Frame` conserva os cantos enquanto adapta as bordas à caixa de diálogo. O PNG não recebeu um recorte destrutivo no arquivo. Texto e nomes continuam sendo renderizados pelo motor; a moldura não contém palavras nem números.

O fundo de leitura usa carvão esverdeado `#192c32` e texto marfim `#f5f0e7`. No modo normal, o diálogo tem altura 300, fala em tamanho 34 e nome em 32; a preferência de texto maior mantém tamanho 42 e espaço próprio. A moldura não elimina essa preferência.

## Inspeção e limites

A cópia integrada foi aberta para inspeção visual e suas dimensões e transparência foram lidas diretamente do PNG. O interior permanece transparente; o fundo de leitura é uma camada do jogo. Essa inspeção do arquivo não substitui verificar fala longa, texto maior, nomes, escolhas, histórico e variantes de tela no fluxo integrado. A verificação final da interface e o playtest humano continuam pendentes de registro.

O total desta expansão é de 29 novos arquivos de arte: 18 fundos e variantes, seis sprites, quatro objetos e esta moldura. A origem das artes anteriores permanece nos seus registros próprios.
