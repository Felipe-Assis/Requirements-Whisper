"""Ajusta as imagens geradas ao padrão do jogo e grava em game/ (ou numa pasta de revisão).

Uso: python posproc.py saidas.json pasta_staging raiz_destino [--substituir]
saidas.json: lista [{"id", "kind": "sprite|bg|artifact|mapa|lugar|icone", "dest": "images/...png",
             "portrait": opcional, "largura" (lugar), "tamanho" (icone)}]
             ou {"saidas": [...]} (formato de estilo-c-saidas.json).
Sem --substituir, nunca sobrescreve um arquivo existente. Use --substituir só depois da aprovação visual.

Padrões (iguais aos da arte existente):
- sprite: RGBA 1024x1536, figura com ~1490 px de altura, pés a 22 px da base, centralizada;
- retrato: recorte de cabeça e ombros da pose âncora, 520x430;
- fundo: RGB 1536x1024, cobrindo (corte central);
- artefato: RGBA, no máximo 1600 px de largura.
Mapa da cidade (docs/design/mapa-cidade.md):
- mapa: base RGB 2560x1440, cobrindo (corte central);
- lugar: recorte RGBA justo no conteúdo, com a largura pedida em "largura" (px da base 2560x1440), sem normalizar
  a altura (uma torre fica mais alta que uma praça);
- icone: RGBA quadrado de "tamanho" px (padrão 192), conteúdo centralizado com margem de 8%.
"""
import json, os, sys
from PIL import Image

args = [a for a in sys.argv[1:] if not a.startswith("--")]
SUBSTITUIR = "--substituir" in sys.argv
dados = json.load(open(args[0], encoding="utf-8"))
mapa = dados["saidas"] if isinstance(dados, dict) else dados
staging, raiz = args[1], args[2]
SPRITE, FIG_ALTURA, MARGEM_BASE, BG, MAPA = (1024, 1536), 1490, 22, (1536, 1024), (2560, 1440)


def bbox_alpha(im, limiar=24):
    return im.getchannel("A").point(lambda a: 255 if a > limiar else 0).getbbox()


def recorte(src):
    """Abre a imagem, confere o fundo transparente e corta justo no conteúdo."""
    im = Image.open(src).convert("RGBA")
    transparentes = sum(im.getchannel("A").histogram()[:10]) / (im.width * im.height)
    if transparentes < 0.2:
        raise ValueError(f"sem fundo transparente ({transparentes:.0%} transparente)")
    return im.crop(bbox_alpha(im))


def sprite(src):
    fig = recorte(src)
    escala = min(FIG_ALTURA / fig.height, 1000 / fig.width)
    fig = fig.resize((round(fig.width * escala), round(fig.height * escala)), Image.LANCZOS)
    tela = Image.new("RGBA", SPRITE, (0, 0, 0, 0))
    tela.alpha_composite(fig, ((SPRITE[0] - fig.width) // 2, SPRITE[1] - MARGEM_BASE - fig.height))
    return tela


def retrato(img):
    x0, y0, x1, y1 = bbox_alpha(img)
    alt = (y1 - y0) * 0.27
    # Centraliza pelo rosto (faixa do queixo), não pelo cabelo.
    faixa = img.crop((0, int(y0 + alt * 0.55), img.width, int(y0 + alt * 0.7)))
    fb = bbox_alpha(faixa, 200) or (x0, 0, x1, 1)
    cx = (fb[0] + fb[2]) / 2
    larg = alt * 1.22
    return img.crop((int(cx - larg / 2), max(0, y0 - 12), int(cx + larg / 2), int(y0 + alt))).resize((520, 430), Image.LANCZOS)


def fundo(src, tam=BG):
    im = Image.open(src).convert("RGB")
    escala = max(tam[0] / im.width, tam[1] / im.height)
    im = im.resize((round(im.width * escala), round(im.height * escala)), Image.LANCZOS)
    x, y = (im.width - tam[0]) // 2, (im.height - tam[1]) // 2
    return im.crop((x, y, x + tam[0], y + tam[1]))


def lugar(src, largura):
    fig = recorte(src)
    return fig.resize((largura, round(fig.height * largura / fig.width)), Image.LANCZOS)


def icone(src, tamanho):
    fig = recorte(src)
    util = round(tamanho * 0.84)
    escala = util / max(fig.width, fig.height)
    fig = fig.resize((max(1, round(fig.width * escala)), max(1, round(fig.height * escala))), Image.LANCZOS)
    tela = Image.new("RGBA", (tamanho, tamanho), (0, 0, 0, 0))
    tela.alpha_composite(fig, ((tamanho - fig.width) // 2, (tamanho - fig.height) // 2))
    return tela


def artefato(src):
    im = Image.open(src).convert("RGBA")
    if im.width > 1600:
        im = im.resize((1600, round(im.height * 1600 / im.width)), Image.LANCZOS)
    return im


def salvar(img, rel):
    dest = os.path.join(raiz, rel)
    if os.path.exists(dest) and not SUBSTITUIR:
        raise FileExistsError(f"{rel} já existe; use --substituir depois da aprovação")
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    img.save(dest, optimize=True)


erros = 0
for item in mapa:
    src = os.path.join(staging, item["id"], "out.png")
    try:
        if not os.path.exists(src):
            raise FileNotFoundError("sem saída do Codex")
        if item["kind"] == "sprite":
            s = sprite(src)
            salvar(s, item["dest"])
            if item.get("portrait"):
                salvar(retrato(s), item["portrait"])
        elif item["kind"] == "bg":
            salvar(fundo(src), item["dest"])
        elif item["kind"] == "mapa":
            salvar(fundo(src, MAPA), item["dest"])
        elif item["kind"] == "lugar":
            salvar(lugar(src, item["largura"]), item["dest"])
        elif item["kind"] == "icone":
            salvar(icone(src, item.get("tamanho", 192)), item["dest"])
        else:
            salvar(artefato(src), item["dest"])
    except Exception as e:
        erros += 1
        print("ERRO", item["id"], e)
print("concluído;", len(mapa) - erros, "ok,", erros, "com erro")
