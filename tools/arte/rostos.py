"""Close-up dos rostos (topo de cada sprite) lado a lado. Uso: python rostos.py saida.png img1 img2 ..."""
import sys
from PIL import Image

crops = []
for f in sys.argv[2:]:
    im = Image.open(f).convert("RGBA")
    x0, y0, x1, _ = im.getchannel("A").point(lambda a: 255 if a > 24 else 0).getbbox()
    cx = (x0 + x1) // 2
    c = im.crop((cx - 160, y0 - 10, cx + 160, y0 + 330)).resize((480, 510), Image.LANCZOS)
    crops.append(c)
s = Image.new("RGBA", (sum(c.width + 10 for c in crops) + 10, 530), (128, 128, 128, 255))
x = 10
for c in crops:
    s.alpha_composite(c, (x, 10))
    x += c.width + 10
s.convert("RGB").save(sys.argv[1])
