"""Folha de contato sobre fundo cinza. Uso: python folha.py saida.png altura img1 img2 ..."""
import sys
from PIL import Image, ImageDraw

saida, altura, imgs = sys.argv[1], int(sys.argv[2]), sys.argv[3:]
cols = []
for p in imgs:
    im = Image.open(p).convert("RGBA")
    cols.append((p, im.resize((round(im.width * altura / im.height), altura), Image.LANCZOS)))
larg = sum(im.width for _, im in cols) + 10 * (len(cols) + 1)
folha = Image.new("RGBA", (larg, altura + 40), (128, 128, 128, 255))
d = ImageDraw.Draw(folha)
x = 10
for p, im in cols:
    folha.alpha_composite(im, (x, 30))
    d.text((x, 8), p.replace("\\", "/").split("/")[-1], fill=(0, 0, 0, 255))
    x += im.width + 10
folha.convert("RGB").save(saida)
