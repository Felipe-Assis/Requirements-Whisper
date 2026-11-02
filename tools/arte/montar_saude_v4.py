"""Lote 4 da Saúde (feedback do usuário em 2026-11-02, segunda revisão da galeria).

Feedback: "amigo e doutora [Nathalia] ainda parecem muito jovens e genéricos e não combinam muito bem com o estilo.
A outra doutora está boa, mas talvez as 2 doutoras devessem ter mais alguma variação de expressão além da neutra.
Developer [César] serious está segurando o celular de forma estranha; com os braços cruzados, pode assumir que o
celular está no bolso."

- amigo e doutora_2: redesenho com rosto e corpo adultos e traços próprios (não genéricos);
- doutora_1 e doutora_2: poses novas serious, thinking e positive, com o rosto descrito por partes e uma referência
  de expressão das rotas novas (mesma técnica do lote v3);
- developer_test serious: braços cruzados, celular no bolso.

Gera docs/arte/prompts/estilo-c-saude-v4.json e estilo-c-saude-v4-saidas.json. Rode a partir da raiz:
    python tools/arte/montar_saude_v4.py
"""
import json, os

RAIZ = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
IMG = os.path.join(RAIZ, "game", "images").replace("\\", "/")
REF = os.path.join(RAIZ, "docs", "arte", "referencias").replace("\\", "/")
CH = f"{IMG}/characters"

ESTILO = (
    "Estilo C, IGUAL ao das imagens de referência de estilo: proporção de ADULTO com ~7,5 cabeças, ombros e mãos "
    "naturais, o mesmo nível de detalhe nas roupas (costuras, dobras, sombras suaves de 1 tom), contorno escuro com "
    "leve textura de lápis, cores suaves e levemente dessaturadas. Rosto de adulto: olhos de tamanho natural (não "
    "olhos grandes de anime), maçãs do rosto e mandíbula definidas, sobrancelhas marcadas e expressivas. Nem realista "
    "demais nem cartunesco. Sprite de visual novel: corpo inteiro em pé, do topo da cabeça aos pés, centralizado, "
    "fundo totalmente transparente (PNG com alfa), sem sombra no chão, sem texto, retrato 2:3."
)

# Redesenhos: (id, imagem atual, prompt de identidade, referências de estilo/proporção)
REDESENHOS = [
    ("amigo__base", f"{CH}/amigo/base.png",
     "A PRIMEIRA imagem é o colega de república do protagonista, mas ele está com cara de criança. Redesenhe-o como "
     "um ADULTO de uns 26 anos, que faz mestrado e divide o apartamento: altura e ombros de adulto, rosto mais longo, "
     "barba por fazer, cabelo castanho bagunçado de quem acabou de acordar, olheiras leves. Mantenha a cena: ele "
     "boceja cobrindo a boca com uma mão e segura uma caneca de café na outra. Roupa com personalidade: calça de "
     "pijama listrada azul (a base de hoje), camiseta larga e desbotada de um time de futebol de bairro (estampa sem "
     "texto legível), chinelo de dedo, fone de ouvido grande pendurado no pescoço. As imagens seguintes são só "
     "referência de ESTILO e PROPORÇÃO (não copie as pessoas delas).",
     [f"{REF}/estilo-c-emily.png", f"{CH}/co_dev/neutral.png", f"{CH}/st_techlead/neutral.png"]),
    ("doutora_2__neutral", f"{CH}/doutora_2/neutral.png",
     "A PRIMEIRA imagem é a Dra. Nathalia, mas ela está jovem demais e genérica. Redesenhe-a como uma médica "
     "pneumologista de uns 32 anos, prática e direta, que atende muitos pacientes por dia: rosto adulto com maçãs do "
     "rosto definidas, olhos de tamanho natural, sardas leves, cabelo loiro-escuro preso num coque baixo com mechas "
     "soltas e uma caneta enfiada no coque, brincos pequenos de pérola. Roupa: pijama cirúrgico verde-água por baixo "
     "do jaleco branco aberto, estetoscópio no pescoço, máscara cirúrgica ABAIXADA no pescoço (rosto inteiro à "
     "mostra), crachá do Instituto no jaleco, tênis brancos confortáveis e um tablet na mão. Pose: em pé, relaxada, "
     "olhar direto, leve sorriso de canto. As imagens seguintes são só referência de ESTILO e PROPORÇÃO (não copie "
     "as pessoas delas).",
     [f"{REF}/estilo-c-emily.png", f"{CH}/doutora_1/neutral.png", f"{CH}/co_mentora/neutral.png"]),
]

# Poses novas das doutoras: corpo, rosto descrito por partes, referência de expressão (outra pessoa).
POSES = {
    "serious": ("braços cruzados ou segurando o objeto dela junto ao peito, peso numa perna, postura firme",
                "sobrancelhas BAIXAS e franzidas, inclinadas para o centro (preocupação); olhar firme direto para a "
                "frente; boca fechada em linha reta, cantos levemente para baixo", f"{CH}/st_qualidade/serious.png"),
    "thinking": ("uma mão no queixo, a outra segurando o objeto dela, cabeça levemente inclinada",
                 "uma sobrancelha erguida e a outra franzida (assimétricas); olhos semicerrados olhando para CIMA e "
                 "para o LADO, não para a frente; lábios comprimidos e puxados para um canto", f"{CH}/st_mentora/thinking.png"),
    "positive": ("explicando algo com uma mão aberta estendida à frente, a outra segurando o objeto dela",
                 "sobrancelhas erguidas; olhos apertados de sorriso; sorriso aberto e caloroso mostrando os dentes",
                 f"{CH}/st_mentora/neutral.png"),
}
DOUTORAS = {
    "doutora_1": ("Dra. Michelle", "cabelo cacheado grisalho, jaleco branco, camisa lilás, calça bege, crachá do "
                  "Instituto e prancheta", f"{CH}/doutora_1/neutral.png", None),
    "doutora_2": ("Dra. Nathalia", "coque baixo loiro-escuro com caneta, sardas, pijama cirúrgico verde-água, jaleco, "
                  "estetoscópio, máscara abaixada no pescoço e tablet", None, "doutora_2__neutral"),
}

tarefas, saidas = [], []
for tid, atual, identidade, refs in REDESENHOS:
    tarefas.append({"id": tid, "prompt": f"{identidade}\n\n{ESTILO}", "refs": [atual] + refs})
    cid, pose = tid.split("__")
    saidas.append({"id": tid, "kind": "sprite", "dest": f"images/characters/{cid}/{pose}.png",
                   "portrait": f"images/characters/{cid}/portrait.png"})

for cid, (nome, objetos, ancora_arquivo, ancora_tarefa) in DOUTORAS.items():
    for pose, (corpo, rosto, ref_expr) in POSES.items():
        tid = f"{cid}__{pose}"
        prompt = (f"A PRIMEIRA imagem é {nome} na versão final: mantenha exatamente a identidade, o rosto, o cabelo, "
                  f"a roupa, as cores e os acessórios ({objetos}). A SEGUNDA imagem é referência de EXPRESSÃO e "
                  f"atitude (outra pessoa: não copie rosto nem roupa dela).\n\n"
                  f"POSE: {corpo}.\nROSTO (obrigatório, bem diferente da primeira imagem): {rosto}.\n\n{ESTILO}")
        t = {"id": tid, "prompt": prompt, "refs": [ref_expr]}
        if ancora_tarefa:
            t["depends"] = ancora_tarefa
        else:
            t["refs"].insert(0, ancora_arquivo)
        tarefas.append(t)
        saidas.append({"id": tid, "kind": "sprite", "dest": f"images/characters/{cid}/{pose}.png"})

# César sério: a âncora (enthusiastic) já está aprovada e entra como primeira referência.
tarefas.append({
    "id": "developer_test__serious",
    "prompt": ("A PRIMEIRA imagem é César na versão final: mantenha exatamente a identidade, o rosto, o boné, os "
               "óculos, a barba, a roupa, o crachá e o smartwatch. A SEGUNDA imagem é a pose séria atual, que tem um "
               "erro: ele segura o celular de um jeito estranho com os braços cruzados. Corrija: braços cruzados "
               "sobre o peito com as DUAS mãos vazias e o celular de capinha colorida guardado no bolso da calça, só "
               "a pontinha aparecendo. ROSTO: sobrancelhas BAIXAS, retas e aproximadas; olhar firme direto para a "
               f"frente; boca fechada em linha reta, sem sorriso.\n\n{ESTILO}"),
    "refs": [f"{CH}/developer_test/enthusiastic.png", f"{CH}/developer_test/serious.png"],
})
saidas.append({"id": "developer_test__serious", "kind": "sprite", "dest": "images/characters/developer_test/serious.png",
               "portrait": "images/characters/developer_test/portrait.png"})

d = os.path.join(RAIZ, "docs", "arte", "prompts")
json.dump(tarefas, open(os.path.join(d, "estilo-c-saude-v4.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
json.dump({"saidas": saidas}, open(os.path.join(d, "estilo-c-saude-v4-saidas.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(len(tarefas), "tarefas:", [t["id"] for t in tarefas])
