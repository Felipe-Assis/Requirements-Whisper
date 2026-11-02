"""Gera a galeria de validação de assets (miniaturas WebP + dados JSON embutidos no HTML)."""
import json, os
from PIL import Image

E = "C:/Users/Felipe/Documents/GitHub/Renpy Projects/Requirements-Whisper-evolucao/game/images"
AQUI = os.path.dirname(os.path.abspath(__file__))
IMG = os.path.join(AQUI, "img")
os.makedirs(IMG, exist_ok=True)

ROTAS = [
    {"id": "saude", "nome": "Saúde", "empresa": "ByeByeFumo, com o Instituto",
     "pessoas": [("developer_requirements", "Emily", "requisitos · mentora"), ("developer_test", "César", "testes"),
                 ("developer_coding", "Joseph", "backend sênior"), ("developer_management", "Robert", "gerente de projeto"),
                 ("developer_ai", "Lucas", "IA e dados"), ("developer_quality", "Daiana", "qualidade"),
                 ("developer_project", "Heitor", "arquitetura e banco"), ("developer_security", "Mateus", "segurança"),
                 ("doutora_1", "Dra. Michelle", "stakeholder"), ("doutora_2", "Dra. Nathalia", "stakeholder"),
                 ("amigo", "Colega de república", "casa, cena 4")],
     "fundos": "cozinha_noite empresa_cafe_tarde empresa_exterior_manha escritorio_interior_festa escritorio_interior_manha escritorio_interior_noite escritorio_interior_tarde escritorio_medica fachada_instituto_tarde quarto_manha quarto_noite refeitorio_tarde sala_reunioes_tarde transito_manha transito_noite transito_tarde",
     "telas": "cadastro_screen main_screen main_screen_old"},
    {"id": "startup", "nome": "Startup", "empresa": "Trocado",
     "pessoas": [("st_mentora", "Tainá", "produto · mentora"), ("st_techlead", "Otávio", "CTO"),
                 ("st_mobile", "Davi", "dev mobile"), ("st_qualidade", "Lorena", "qualidade e pesquisa"),
                 ("st_ceo", "Vinícius", "CEO · stakeholder"), ("st_estudante", "Bia", "estudante · stakeholder")],
     "fundos": "quarto_manha cozinha_noite demo_day_auditorio empresa_cafe_tarde quarto_noite refeitorio_tarde sala_reunioes_manha sala_reunioes_tarde startup_coworking_manha startup_coworking_tarde startup_coworking_noite startup_terraco_noite transito_manha transito_tarde transito_noite",
     "telas": "st_app_gastos st_diagrama_arquitetura st_painel_metricas st_quadro_kanban"},
    {"id": "corporativo", "nome": "Corporativo", "empresa": "Grupo Vértice · SGC e Farol",
     "pessoas": [("co_mentora", "Valéria", "analista sênior · mentora"), ("co_legado", "Jorge", "dev do legado"),
                 ("co_dev", "Kauã", "dev pleno"), ("co_qualidade", "Ingrid", "qualidade e segurança"),
                 ("co_supervisora", "Rosângela", "supervisora · stakeholder"), ("co_solicitante", "Edson", "campo · stakeholder")],
     "fundos": "quarto_manha central_atendimento_manha central_atendimento_tarde cozinha_noite empresa_cafe_tarde empresa_exterior_manha empresa_exterior_noite escritorio_interior_festa escritorio_interior_manha escritorio_interior_noite escritorio_interior_tarde quarto_noite refeitorio_tarde sala_arquivo_tarde sala_reunioes_manha sala_reunioes_tarde sala_servidores transito_noite",
     "telas": "co_farol_arquitetura co_farol_auditoria co_farol_consulta co_sgc_legado"},
]
SEM_USO = ["escritorio_interior_vazio", "empresa_cafe_manha"]
NOTAS = {
    "co_supervisora": "Traço um pouco mais fino que o resto do elenco (a métrica de contorno ficou abaixo da média).",
    "doutora_2": "Máscara cobre parte do rosto, como no desenho original.",
    "co_solicitante": "Saturação alta por causa do colete laranja, não do estilo.",
    "developer_management": "Saturação alta por causa do blazer marrom, não do estilo.",
}
CONTA = {}
usados = {}


def salvar(src, nome, caixa, alfa=True):
    if nome in usados:
        return usados[nome]
    im = Image.open(src)
    im = im.convert("RGBA" if alfa else "RGB")
    if alfa:
        bb = im.getchannel("A").point(lambda a: 255 if a > 24 else 0).getbbox()
        if bb:
            im = im.crop(bb)
    im.thumbnail(caixa, Image.LANCZOS)
    rel = f"img/{nome}.webp"
    im.save(os.path.join(AQUI, rel), "WEBP", quality=84, method=6)
    usados[nome] = {"src": rel, "w": im.width, "h": im.height}
    return usados[nome]


dados = []
for r in ROTAS:
    pessoas = []
    for cid, nome, papel in r["pessoas"]:
        pasta = f"{E}/characters/{cid}"
        poses = sorted(f[:-4] for f in os.listdir(pasta) if f.endswith(".png") and f != "portrait.png")
        pessoas.append({"id": cid, "nome": nome, "papel": papel, "nota": NOTAS.get(cid, ""),
                        "retrato": salvar(f"{pasta}/portrait.png", f"{cid}__portrait", (260, 216)),
                        "poses": [{"pose": p, **salvar(f"{pasta}/{p}.png", f"{cid}__{p}", (420, 640))} for p in poses]})
    fundos = [{"id": b, **salvar(f"{E}/bg/{b}.png", f"bg__{b}", (960, 640), alfa=False)} for b in r["fundos"].split()]
    telas = [{"id": t, **salvar(f"{E}/artifacts/{t}.png", f"art__{t}", (900, 600))} for t in r["telas"].split()]
    dados.append({"id": r["id"], "nome": r["nome"], "empresa": r["empresa"], "pessoas": pessoas, "fundos": fundos, "telas": telas})
extras = [{"id": b, **salvar(f"{E}/bg/{b}.png", f"bg__{b}", (960, 640), alfa=False)} for b in SEM_USO]

modelo = open(os.path.join(AQUI, "modelo.html"), encoding="utf-8").read()
html = modelo.replace("/*DADOS*/null", json.dumps({"rotas": dados, "semUso": extras}, ensure_ascii=False))
open(os.path.join(AQUI, "galeria-assets.html"), "w", encoding="utf-8").write(html)
total = sum(os.path.getsize(os.path.join(IMG, f)) for f in os.listdir(IMG))
print(len(usados), "imagens,", round(total / 1e6, 1), "MB")
print("\n".join(sorted("img/" + os.path.basename(v["src"]) for v in usados.values())))
