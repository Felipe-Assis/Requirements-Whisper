"""Lote de expressões do elenco da Saúde (feedback do usuário em 2026-11-02).

Feedback: "os personagens [da Saúde] estão bem menos expressivos que os outros, principalmente na região dos olhos,
que quase não mudam de uma pose para a outra". Causa: o prompt das poses pedia a mesma pessoa na pose da segunda
imagem sem descrever a expressão, e o gerador copiava o rosto da âncora. Este lote refaz todas as poses que não são
âncora, descrevendo sobrancelhas, olhos, olhar e boca, e anexando como referência de EXPRESSÃO a mesma pose de um
personagem das rotas novas (que o usuário considera expressivos).

Identidade: a âncora já revisada (lote estilo-c-saude-v2), passada por "depends".
Gera docs/arte/prompts/estilo-c-saude-v3-expressoes.json. Rode a partir da raiz:
    python tools/arte/montar_saude_v3_expressoes.py
"""
import json, os

RAIZ = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
IMG = os.path.join(RAIZ, "game", "images").replace("\\", "/")
REF = os.path.join(RAIZ, "docs", "arte", "referencias").replace("\\", "/")
CH = f"{IMG}/characters"

# Corpo e rosto de cada pose. O rosto é descrito por partes para o gerador não repetir o da âncora.
POSES = {
    "serious": ("braços cruzados sobre o peito, peso numa perna, postura firme",
                "sobrancelhas BAIXAS, retas e aproximadas; pálpebras de cima um pouco caídas; olhar firme direto "
                "para a frente; boca fechada em linha reta, sem sorriso", f"{CH}/st_qualidade/serious.png"),
    "thinking": ("uma mão no queixo, a outra no bolso ou segurando o objeto do personagem, cabeça levemente inclinada",
                 "uma sobrancelha erguida e a outra franzida (assimétricas); olhos semicerrados olhando para CIMA e "
                 "para o LADO, não para a frente; lábios comprimidos e puxados para um canto", f"{CH}/st_mentora/thinking.png"),
    "confident": ("uma mão no bolso, a outra segurando o objeto do personagem à altura do peito, ombros abertos",
                  "uma sobrancelha levemente arqueada; olhos bem abertos com um brilho de ironia; olhar direto; meio "
                  "sorriso torto de um lado só", f"{CH}/co_dev/neutral.png"),
    "concentrated": ("escrevendo num bloco de notas ou caderno segurado à frente do peito",
                     "cabeça um pouco baixa; olhos voltados PARA BAIXO, para o caderno; sobrancelhas levemente "
                     "franzidas e unidas no centro; boca entreaberta ou mordendo de leve o lábio", f"{CH}/co_qualidade/thinking.png"),
}

ESTILO = (
    "Estilo C, igual ao das referências: proporção adulta de ~7,5 cabeças, mesmo nível de detalhe nas roupas, "
    "contorno escuro com leve textura de lápis, cores suaves. O ROSTO deve ser tão expressivo quanto o da imagem de "
    "referência de expressão: sobrancelhas e olhos mudam bastante de uma emoção para outra. Sprite de visual novel, "
    "corpo inteiro, do topo da cabeça aos pés, centralizado, fundo totalmente transparente (PNG com alfa), sem texto, "
    "retrato 2:3."
)

# Personagens da Saúde: (nome, pose âncora já revisada, objeto/acessórios que precisam aparecer)
ELENCO = {
    "developer_test": ("César", "enthusiastic", "óculos redondos, boné azul-marinho, barba, crachá azul no cordão, smartwatch, celular de testes"),
    "developer_coding": ("Joseph", "neutral", "careca, barba grisalha curta, blazer marrom, relógio analógico, caneca de café"),
    "developer_management": ("Robert", "thinking", "camiseta de listras horizontais azul-marinho e branco, bigode, crachá no bolso, prancheta"),
    "developer_ai": ("Lucas", "positive", "óculos pretos, cabelo loiro, camisa de flores, mochila com adesivos, pulseira"),
    "developer_quality": ("Daiana", "positive", "óculos redondos, cabelo cacheado preto, camiseta verde-clara, brincos de argola, pasta com post-its"),
    "developer_project": ("Heitor", "confident", "óculos, suéter creme sobre camisa branca, relógio, notebook debaixo do braço"),
    "developer_security": ("Mateus", "serious", "camiseta preta, sobrecamisa cinza-escura aberta, crachá de acesso no cinto"),
}

tarefas = []
for cid, (nome, ancora, objetos) in ELENCO.items():
    poses = sorted(f[:-4] for f in os.listdir(f"{CH}/{cid}") if f.endswith(".png") and f != "portrait.png")
    for pose in poses:
        if pose == ancora or pose not in POSES:
            continue
        corpo, rosto, ref_expr = POSES[pose]
        prompt = (f"A PRIMEIRA imagem é {nome} na versão final: mantenha exatamente a identidade, o rosto, o cabelo, "
                  f"a roupa, as cores e os acessórios ({objetos}). A SEGUNDA imagem é referência de EXPRESSÃO e "
                  f"atitude (outra pessoa: não copie rosto nem roupa dela).\n\n"
                  f"POSE: {corpo}.\nROSTO (obrigatório, bem diferente da primeira imagem): {rosto}.\n\n{ESTILO}")
        tarefas.append({"id": f"{cid}__{pose}", "prompt": prompt, "refs": [ref_expr], "depends": f"{cid}__{ancora}"})

d = os.path.join(RAIZ, "docs", "arte", "prompts")
json.dump(tarefas, open(os.path.join(d, "estilo-c-saude-v3-expressoes.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(len(tarefas), "tarefas:", [t["id"] for t in tarefas])
