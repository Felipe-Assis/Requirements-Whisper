"""Lote de revisão do elenco da Saúde no estilo C (feedback do usuário em 2026-11-02).

Feedback: "Na parte da saúde, Joseph parece muito realista e os outros ainda muito cartoonescos. Devem se aproximar
mais do estilo de Emily ou dos outros da parte de Startup e/ou Corporativo em relação à proporção do corpo e ao nível
de detalhes. Pode revisar algum aspecto da roupa mantendo a base, para dar mais personalidade (brinco, relógio,
segurando algo, mochila, pasta, crachá etc.)."

Gera docs/arte/prompts/estilo-c-saude-v2.json e estilo-c-saude-v2-saidas.json. Rode a partir da raiz:
    python tools/arte/montar_saude_v2.py
"""
import json, os

RAIZ = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
IMG = os.path.join(RAIZ, "game", "images").replace("\\", "/")
REF = os.path.join(RAIZ, "docs", "arte", "referencias").replace("\\", "/")
# Referências de estilo e proporção: a Emily aprovada e dois personagens das rotas novas.
REFS_ESTILO = [f"{REF}/estilo-c-emily.png", f"{IMG}/characters/st_mentora/neutral.png", f"{IMG}/characters/co_dev/neutral.png"]

ESTILO = (
    "Estilo C, IGUAL ao das imagens de referência de estilo: mesmas proporções de corpo (adulto com ~7,5 cabeças, "
    "cabeça proporcional, ombros e mãos naturais), o mesmo nível de detalhe nas roupas (costuras, dobras, sombras "
    "suaves de 1 tom), contorno escuro com leve textura de lápis, cores suaves e levemente dessaturadas, rosto simples "
    "com olhos discretos. Nem realista demais (sem pele com textura de foto, sem rugas detalhadas) nem cartunesco "
    "demais (sem cabeça grande, sem olhos enormes). Sprite de visual novel: corpo inteiro em pé, do topo da cabeça "
    "aos pés, centralizado, fundo totalmente transparente (PNG com alfa), sem sombra no chão, sem texto, retrato 2:3."
)

# id: (nome, papel, pose âncora, acréscimo de personalidade, pose do retrato)
ELENCO = {
    "developer_test": ("César", "jovem prodígio dos testes, rápido e eficiente", "enthusiastic",
                       "crachá azul num cordão no pescoço, smartwatch no pulso e um celular de testes com capinha "
                       "colorida na mão ou no bolso da camisa", "serious"),
    "developer_coding": ("Joseph", "desenvolvedor sênior de backend, sério e crítico", "neutral",
                         "menos realista que hoje, no mesmo traço das referências; relógio analógico de pulseira de "
                         "couro e uma caneca de café escura", None),
    "developer_management": ("Robert", "gerente de projeto jovem, organizado, querido pela equipe", "thinking",
                             "crachá preso no bolso e uma prancheta com o cronograma impresso (sem texto legível)", None),
    "developer_ai": ("Lucas", "pesquisador jovem de IA, animado, fala rápido", "positive",
                     "mochila de uma alça com adesivos de tecnologia e uma pulseira de tecido", None),
    "developer_quality": ("Daiana", "especialista em qualidade, didática, adora ensinar", "positive",
                          "brincos pequenos de argola e uma pasta com post-its coloridos saindo das páginas", None),
    "developer_project": ("Heitor", "arquiteto de software e banco de dados, veio do mercado financeiro, fala pouco", "confident",
                          "relógio de pulso discreto e um notebook fechado debaixo do braço", None),
    "developer_security": ("Mateus", "desenvolvedor sênior de segurança, sério, fala devagar, organizado", "serious",
                           "sobrecamisa aberta cinza-escura por cima da camiseta preta e crachá de acesso com chip "
                           "preso no cinto", None),
    "doutora_1": ("Dra. Michelle", "médica pneumologista experiente, stakeholder do projeto", "neutral",
                  "crachá do Instituto no jaleco e uma prancheta com ficha de paciente (sem texto legível)", None),
    "doutora_2": ("Dra. Nathalia", "médica jovem, stakeholder do projeto", "neutral",
                  "a máscara cirúrgica ABAIXADA no pescoço, deixando o rosto inteiro à mostra, e um tablet na mão", None),
    "amigo": ("colega de república", "colega que divide o apartamento com o jogador", "base",
              "mantenha o pijama e o bocejo; acrescente uma caneca de café na outra mão", None),
}

tarefas, saidas = [], []
for cid, (nome, papel, ancora, extra, pose_retrato) in ELENCO.items():
    pasta = f"{IMG}/characters/{cid}"
    poses = sorted(f[:-4] for f in os.listdir(pasta) if f.endswith(".png") and f != "portrait.png")
    base_id = f"{cid}__{ancora}"
    for pose in [ancora] + [p for p in poses if p != ancora]:
        tid = f"{cid}__{pose}"
        if pose == ancora:
            prompt = (f"A PRIMEIRA imagem é {nome} ({papel}). Redesenhe essa pessoa mantendo o rosto, o cabelo, o tom "
                      f"de pele, a roupa base, as cores e a pose. As imagens seguintes são só referência de ESTILO e "
                      f"PROPORÇÃO (não copie as pessoas delas). Acréscimo de personalidade: {extra}.\n\n{ESTILO}")
            refs = [f"{pasta}/{pose}.png"] + REFS_ESTILO
            tarefas.append({"id": tid, "prompt": prompt, "refs": refs})
        else:
            prompt = (f"A PRIMEIRA imagem é {nome} já no estilo e na roupa finais (inclusive: {extra}): mantenha a "
                      f"identidade, o rosto, o cabelo, a roupa, os acessórios e as cores. A SEGUNDA imagem mostra a POSE "
                      f"e a expressão desejadas. Desenhe a pessoa da primeira imagem na pose da segunda. A TERCEIRA é "
                      f"referência de estilo e proporção.\n\n{ESTILO}")
            tarefas.append({"id": tid, "prompt": prompt, "refs": [f"{pasta}/{pose}.png", REFS_ESTILO[0]],
                            "depends": base_id})
        item = {"id": tid, "kind": "sprite", "dest": f"images/characters/{cid}/{pose}.png"}
        if pose == (pose_retrato or ancora):
            item["portrait"] = f"images/characters/{cid}/portrait.png"
        saidas.append(item)

d = os.path.join(RAIZ, "docs", "arte", "prompts")
json.dump(tarefas, open(os.path.join(d, "estilo-c-saude-v2.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
json.dump({"saidas": saidas}, open(os.path.join(d, "estilo-c-saude-v2-saidas.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(len(tarefas), "tarefas")
