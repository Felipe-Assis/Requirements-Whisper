"""Monta o lote de regeração no estilo C (mescla aprovada em 2026-11-02).

Gera docs/arte/prompts/estilo-c.json (tarefas para gerar_codex.py) e docs/arte/prompts/estilo-c-saidas.json
(destinos para posproc.py). Rode a partir da raiz do repositório:
    python tools/arte/montar_estilo_c.py
"""
import json, os

RAIZ = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
IMG = os.path.join(RAIZ, "game", "images").replace("\\", "/")
REF = os.path.join(RAIZ, "docs", "arte", "referencias").replace("\\", "/")
REF_PERSONAGEM = [f"{REF}/estilo-c-emily.png", f"{REF}/estilo-c-taina.png"]
REF_FUNDO = f"{REF}/estilo-c-escritorio.png"

ESTILO_PERSONAGEM = (
    "Estilo C (aprovado): contorno escuro com leve textura de lápis/carvão, cores suaves e levemente "
    "dessaturadas, formas simples com poucos detalhes, sombra mínima, rosto simples com olhos discretos e sem "
    "brilho exagerado; anatomia e proporções corretas, mãos e pés bem desenhados, dobras de roupa coerentes, "
    "acabamento limpo. Evite o visual de anime genérico. Sprite de visual novel: corpo inteiro em pé, do topo da "
    "cabeça aos pés, centralizado, fundo totalmente transparente (PNG com alfa), sem sombra no chão, sem texto, "
    "retrato 2:3."
)
ESTILO_FUNDO = (
    "Estilo C dos fundos (aprovado): paleta suave e levemente dessaturada, leve textura de papel, clima de "
    "ilustração feita à mão, perspectiva precisa, linhas limpas, objetos bem definidos, luz clara porém contida. "
    "Figurantes só ao longe, de costas e sem rosto. Sem texto legível. Fundo de visual novel em paisagem 3:2."
)

# id -> (nome, pose âncora). A âncora é regerada primeiro; as outras poses usam a âncora regerada como identidade.
PERSONAGENS = {
    "developer_requirements": ("Emily", "neutral"),
    "developer_test": ("César", "enthusiastic"),
    "developer_coding": ("Joseph", "neutral"),
    "developer_management": ("Robert", "thinking"),
    "developer_ai": ("Lucas", "positive"),
    "developer_quality": ("Daiana", "positive"),
    "developer_project": ("Heitor", "confident"),
    "developer_security": ("Mateus", "serious"),
    "doutora_1": ("Dra. Michelle", "neutral"),
    "doutora_2": ("Dra. Nathalia", "neutral"),
    "amigo": ("colega de república", "base"),
    "st_mentora": ("Tainá", "neutral"), "st_techlead": ("Otávio", "neutral"), "st_mobile": ("Davi", "neutral"),
    "st_qualidade": ("Lorena", "neutral"), "st_ceo": ("Vinícius", "neutral"), "st_estudante": ("Bia", "neutral"),
    "co_mentora": ("Valéria", "neutral"), "co_legado": ("Jorge", "neutral"), "co_dev": ("Kauã", "neutral"),
    "co_qualidade": ("Ingrid", "neutral"), "co_supervisora": ("Rosângela", "neutral"),
    "co_solicitante": ("Edson", "neutral"),
}
# Âncoras já aprovadas na página de comparação: entram como saída pronta, sem nova geração.
APROVADAS = {"developer_requirements__neutral": "estilo-c-emily.png", "st_mentora__neutral": "estilo-c-taina.png",
             "bg__escritorio_interior_manha": "estilo-c-escritorio.png"}

# Fundos: base -> variantes que herdam ambiente e enquadramento da base regerada.
FUNDOS = {
    "escritorio_interior_manha": ["escritorio_interior_tarde", "escritorio_interior_noite",
                                  "escritorio_interior_festa", "escritorio_interior_vazio"],
    "quarto_manha": ["quarto_noite"],
    "transito_manha": ["transito_tarde", "transito_noite"],
    "sala_reunioes_manha": ["sala_reunioes_tarde"],
    "empresa_cafe_manha": ["empresa_cafe_tarde"],
    "empresa_exterior_manha": ["empresa_exterior_noite"],
    "startup_coworking_manha": ["startup_coworking_tarde", "startup_coworking_noite"],
    "central_atendimento_manha": ["central_atendimento_tarde"],
    "cozinha_noite": [], "refeitorio_tarde": [], "escritorio_medica": [], "fachada_instituto_tarde": [],
    "demo_day_auditorio": [], "sala_arquivo_tarde": [], "sala_servidores": [], "startup_terraco_noite": [],
}

tarefas, saidas = [], []
for cid, (nome, ancora) in PERSONAGENS.items():
    pasta = f"{IMG}/characters/{cid}"
    poses = sorted(os.path.splitext(f)[0] for f in os.listdir(pasta) if f.endswith(".png") and f != "portrait.png")
    base_id = f"{cid}__{ancora}"
    for pose in [ancora] + [p for p in poses if p != ancora]:
        tid = f"{cid}__{pose}"
        if tid not in APROVADAS:
            if pose == ancora:
                prompt = (f"A PRIMEIRA imagem é {nome}. Redesenhe EXATAMENTE essa pessoa, com o mesmo rosto, "
                          f"cabelo, tom de pele, roupa, acessórios, cores e pose, no estilo das imagens seguintes, "
                          f"que são só referência de estilo (não copie as pessoas delas).\n\n{ESTILO_PERSONAGEM}")
                tarefas.append({"id": tid, "prompt": prompt, "refs": [f"{pasta}/{pose}.png"] + REF_PERSONAGEM})
            else:
                prompt = (f"A PRIMEIRA imagem é {nome} já no estilo final: mantenha a identidade, o rosto, o "
                          f"cabelo, a roupa, as cores e o estilo de desenho dela. A SEGUNDA imagem mostra a POSE e "
                          f"a expressão desejadas (a mesma pessoa, desenhada em outro estilo). Desenhe a pessoa da "
                          f"primeira imagem na pose da segunda.\n\n{ESTILO_PERSONAGEM}")
                tarefas.append({"id": tid, "prompt": prompt, "refs": [f"{pasta}/{pose}.png", REF_PERSONAGEM[0]],
                                "depends": base_id})
        item = {"id": tid, "kind": "sprite", "dest": f"images/characters/{cid}/{pose}.png"}
        if pose == ancora:
            item["portrait"] = f"images/characters/{cid}/portrait.png"
        saidas.append(item)

for base, variantes in FUNDOS.items():
    for nome in [base] + variantes:
        tid = f"bg__{nome}"
        atual = f"{IMG}/bg/{nome}.png"
        if tid not in APROVADAS:
            if nome == base:
                prompt = (f"A PRIMEIRA imagem é o fundo atual '{nome}'. Redesenhe o MESMO ambiente, com a mesma "
                          f"composição, móveis, objetos, horário e enquadramento, no estilo da SEGUNDA imagem "
                          f"(só referência de estilo).\n\n{ESTILO_FUNDO}")
                tarefas.append({"id": tid, "prompt": prompt, "refs": [atual, REF_FUNDO]})
            else:
                prompt = (f"A PRIMEIRA imagem é o ambiente já no estilo final. A SEGUNDA é a variante atual "
                          f"'{nome}' (outro horário ou situação). Desenhe o MESMO ambiente da primeira, com o mesmo "
                          f"enquadramento e móveis, mas com a iluminação, o horário e os elementos da segunda, no "
                          f"estilo da primeira.\n\n{ESTILO_FUNDO}")
                tarefas.append({"id": tid, "prompt": prompt, "refs": [atual], "depends": f"bg__{base}"})
        saidas.append({"id": tid, "kind": "bg", "dest": f"images/bg/{nome}.png"})

os.makedirs(os.path.join(RAIZ, "docs", "arte", "prompts"), exist_ok=True)
with open(os.path.join(RAIZ, "docs", "arte", "prompts", "estilo-c.json"), "w", encoding="utf-8") as f:
    json.dump(tarefas, f, ensure_ascii=False, indent=1)
with open(os.path.join(RAIZ, "docs", "arte", "prompts", "estilo-c-saidas.json"), "w", encoding="utf-8") as f:
    json.dump({"aprovadas": APROVADAS, "saidas": saidas}, f, ensure_ascii=False, indent=1)
print(len(tarefas), "tarefas de geração;", len(saidas), "saídas;", len(APROVADAS), "aprovadas sem nova geração")
