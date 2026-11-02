"""Lote 5 da Saúde: rosto simplificado do colega de república e da Dra. Nathalia (feedback de 2026-11-02).

Feedback: "Ficaram bons, mas acho que um pouco detalhados demais, especialmente na parte do rosto e olhos. Veja a
Emily como exemplo a ser seguido ou outros personagens dos outros arcos."

Diferença observada no close-up: Emily, Tainá, Kauã e Dra. Michelle têm pele chapada de 1 tom, olhos com íris
escura simples e um brilho, nariz em traço curto e boca em forma simples. A versão do lote 4 tinha íris detalhada,
cílios, sardas, batom, sombra no nariz e, no colega, rugas e textura de barba.

Refaz as duas âncoras (a imagem do lote 4 entra como identidade e roupa; docs/arte/referencias/estilo-c-rostos.png,
com os 4 rostos de exemplo, entra como referência do rosto) e as 3 poses da Nathalia sobre a âncora nova, com os
mesmos prompts de pose do lote 4. Gera docs/arte/prompts/estilo-c-saude-v5-rostos.json; as saídas são as do lote 4
(estilo-c-saude-v4-saidas.json, filtradas pelos ids deste lote). Rode a partir da raiz:
    python tools/arte/montar_saude_v5_rostos.py
"""
import json, os

RAIZ = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
CH = os.path.join(RAIZ, "game", "images", "characters").replace("\\", "/")
REF = os.path.join(RAIZ, "docs", "arte", "referencias").replace("\\", "/")
PROMPTS = os.path.join(RAIZ, "docs", "arte", "prompts")

ROSTO = (
    "ROSTO NO TRAÇO DA EMILY E DOS OUTROS ROSTOS DA IMAGEM DE REFERÊNCIA DE ROSTO: pele chapada de um tom só com no "
    "máximo uma sombra simples, sem textura, sem sardas, sem rugas, sem marcas de expressão; olhos com íris escura "
    "simples e um único brilho branco, cílios só como um traço grosso na pálpebra de cima, sem maquiagem desenhada; "
    "nariz como um traço curto; boca em forma simples, sem batom nem lábios detalhados; sobrancelhas como uma faixa "
    "escura grossa. Barba, quando houver, como uma mancha lisa de um tom, sem fios. "
)

v4 = {t["id"]: t for t in json.load(open(os.path.join(PROMPTS, "estilo-c-saude-v4.json"), encoding="utf-8"))}
# O ESTILO do lote 4 pedia "maçãs do rosto e mandíbula definidas", o que puxou o rosto para o detalhado.
ROSTO_V4 = ("Rosto de adulto: olhos de tamanho natural (não olhos grandes de anime), maçãs do rosto e mandíbula "
            "definidas, sobrancelhas marcadas e expressivas.")
ROSTO_V5 = "Rosto de adulto no traço simples da Emily: a idade aparece no formato do rosto e no cabelo, não em detalhes."
for t in v4.values():
    assert ROSTO_V4 in t["prompt"], t["id"]
    t["prompt"] = t["prompt"].replace(ROSTO_V4, ROSTO_V5)
ROSTOS = f"{REF}/estilo-c-rostos.png"

tarefas = []
for tid in ("amigo__base", "doutora_2__neutral"):
    cid, pose = tid.split("__")
    prompt = (f"{ROSTO}A PRIMEIRA imagem é a versão atual: mantenha a identidade, o cabelo, o corpo adulto, a roupa, "
              f"os acessórios, as cores e a pose; mude SÓ o traço do rosto (e deixe-o tão simples quanto o da segunda "
              f"imagem). A SEGUNDA imagem mostra rostos de outros personagens do jogo, como referência de traço (não "
              f"copie as pessoas).\n\n" + v4[tid]["prompt"].split("\n\n", 1)[1])
    tarefas.append({"id": tid, "prompt": prompt, "refs": [f"{CH}/{cid}/{pose}.png", ROSTOS]})

for pose in ("serious", "thinking", "positive"):
    t = dict(v4[f"doutora_2__{pose}"])
    t["prompt"] = ROSTO + t["prompt"].replace("sardas, ", "")
    tarefas.append(t)

json.dump(tarefas, open(os.path.join(PROMPTS, "estilo-c-saude-v5-rostos.json"), "w", encoding="utf-8"),
          ensure_ascii=False, indent=1)
print(len(tarefas), "tarefas:", [t["id"] for t in tarefas])
