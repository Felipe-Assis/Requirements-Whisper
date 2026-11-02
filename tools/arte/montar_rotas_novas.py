"""Reconstrói o lote de 2026-11-02 que gerou a arte das rotas Startup e Corporativo.

Os prompts saem de docs/rotas/*-assets.json com os mesmos modelos de texto usados na geração original.
Grava docs/arte/prompts/rotas-novas-2026-11-02.json (tarefas para gerar_codex.py) e
docs/arte/prompts/rotas-novas-2026-11-02-saidas.json (destinos para posproc.py). Rode a partir da raiz:
    python tools/arte/montar_rotas_novas.py
Observação: essa arte foi depois substituída pelo estilo C (ver estilo-c.json); este lote fica como registro e para
regerar no estilo antigo, se preciso. As referências de estilo eram dois sprites e dois fundos da rota Saúde no
estado anterior ao estilo C (commit 7066ed1).
"""
import json, os, re

RAIZ = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
IMG = os.path.join(RAIZ, "game", "images").replace("\\", "/")
REF_SPRITES = [IMG + "/characters/developer_quality/positive.png", IMG + "/characters/developer_coding/serious.png"]
REF_BG = [IMG + "/bg/escritorio_interior_manha.png", IMG + "/bg/sala_reunioes_manha.png"]

ESTILO_SPRITE = (
    "Sprite de personagem para visual novel. Corpo inteiro em pé, do topo da cabeça aos pés visíveis, "
    "centralizado, de frente ou levemente 3/4, fundo totalmente transparente (PNG com canal alfa), sem "
    "sombra no chão, sem cenário, sem texto, formato retrato 2:3. Siga o estilo das imagens de referência: "
    "ilustração anime/cartoon ocidentalizada SIMPLES e limpa, traço fino escuro, cores chapadas com no "
    "máximo 1-2 tons de sombra suave, poucos detalhes de textura, olhos grandes escuros com brilho branco, "
    "nariz mínimo, boca simples, paleta natural levemente dessaturada, proporção realista (~7 cabeças). "
    "A expressão é transmitida principalmente pela pose."
)
ESTILO_BG = (
    "Fundo de visual novel em paisagem 3:2, sem texto legível, sem personagens em primeiro plano "
    "(figurantes só ao longe, de costas e sem rosto). Siga o estilo das imagens de referência: ilustração "
    "anime/cel com contorno fino de tinta escura, sombreamento suave, leve textura de papel, perspectiva "
    "na altura dos olhos, cores conforme o horário (manhã: azul-petróleo frio com luz amarelada; tarde: "
    "laranja e magenta de pôr do sol; noite: azul-marinho quase monocromático)."
)
ESTILO_ART = (
    "Ilustração de uma tela/artefato de software para aparecer dentro de uma visual novel: plana, limpa, "
    "contorno leve, textos curtos em português do Brasil escritos corretamente e legíveis, sem marcas reais. "
    "Fundo transparente ao redor do quadro (PNG com alfa)."
)
# Três sprites saíram inconsistentes e foram regerados com um reforço no início do prompt.
REFORCOS = {
    "co_legado__serious": (
        "A ÚNICA imagem anexada é o Jorge, um senhor de uns 60 anos. Desenhe ESSE MESMO homem (não uma mulher, não "
        "outra pessoa). ATENÇÃO À CONSISTÊNCIA: o colete é CINZA (o mesmo da imagem anexada), a camisa é "
        "azul-clara de manga curta, calça cáqui, sapatos marrons, cabelo grisalho, bigode, óculos pendurados na "
        "camisa. Não troque a cor de nenhuma peça.", True),
    "st_mobile__serious": (
        "ATENÇÃO À CONSISTÊNCIA: é o MESMO rapaz da imagem anexada: cabelo preto CURTO e liso com franja (não é "
        "cabelo comprido nem chanel), moletom cinza com o pequeno robô no peito, fone de ouvido preto no pescoço, "
        "calça cargo preta, tênis vermelho-escuro. Rosto masculino idêntico.", False),
}

tarefas, saidas = [], []
for rota in ("startup", "corporativo"):
    spec = json.load(open(f"{RAIZ}/docs/rotas/{rota}-assets.json", encoding="utf-8"))
    for c in spec["characters"]:
        cid = c["id"]
        visual = re.sub(r"Estilo do jogo:.*", "", c["visual"]).strip()
        base = f"{cid}__neutral"
        for pose, desc in c["poses"].items():
            tid = f"{cid}__{pose}"
            if pose == "neutral":
                t = {"id": tid, "prompt": f"{ESTILO_SPRITE}\n\nPersonagem: {c['name']}. {visual}\n\nPose: {desc}",
                     "refs": REF_SPRITES}
            else:
                t = {"id": tid, "refs": REF_SPRITES[:1], "depends": base,
                     "prompt": (f"A PRIMEIRA imagem anexada é o personagem {c['name']}. Gere a MESMA pessoa, com o "
                                f"mesmo rosto, cabelo, roupa, acessórios, cores e estilo de desenho, mudando só a pose "
                                f"e a expressão.\n\nNova pose: {desc}\n\n{ESTILO_SPRITE}")}
            if tid in REFORCOS:
                texto, so_identidade = REFORCOS[tid]
                t["prompt"] = texto + "\n\n" + t["prompt"]
                if so_identidade:
                    t["refs"] = []
                t["observacao"] = "regerado com reforço de consistência"
            tarefas.append(t)
            item = {"id": tid, "kind": "sprite", "dest": f"images/characters/{cid}/{pose}.png"}
            if pose == "neutral":
                item["portrait"] = f"images/characters/{cid}/portrait.png"
            saidas.append(item)
    bases = {}
    for b in spec["backgrounds"]:
        nome = os.path.splitext(os.path.basename(b["file"]))[0]
        raiz = re.sub(r"_(manha|tarde|noite)$", "", nome)
        tid = f"bg__{nome}"
        if raiz in bases and raiz != nome:
            tarefas.append({"id": tid, "refs": REF_BG[:1], "depends": bases[raiz],
                            "prompt": (f"A PRIMEIRA imagem anexada é o ambiente base. Gere o MESMO ambiente, com o "
                                       f"mesmo enquadramento, móveis e composição, mudando só a iluminação e os "
                                       f"detalhes descritos.\n\n{b['desc']}\n\n{ESTILO_BG}")})
        else:
            if raiz != nome:
                bases[raiz] = tid
            tarefas.append({"id": tid, "prompt": f"{ESTILO_BG}\n\n{b['desc']}", "refs": REF_BG})
        saidas.append({"id": tid, "kind": "bg", "dest": b["file"]})
    for a in spec["artifacts"]:
        nome = os.path.splitext(os.path.basename(a["file"]))[0]
        tarefas.append({"id": f"art__{nome}", "prompt": f"{ESTILO_ART}\n\n{a['desc']}", "refs": []})
        saidas.append({"id": f"art__{nome}", "kind": "artifact", "dest": a["file"]})

d = os.path.join(RAIZ, "docs", "arte", "prompts")
os.makedirs(d, exist_ok=True)
json.dump(tarefas, open(os.path.join(d, "rotas-novas-2026-11-02.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
json.dump(saidas, open(os.path.join(d, "rotas-novas-2026-11-02-saidas.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(len(tarefas), "tarefas reconstruídas")
