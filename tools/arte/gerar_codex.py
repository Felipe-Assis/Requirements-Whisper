"""Gera imagens com o Codex (skill imagegen, ferramenta image_gen embutida) a partir de uma lista de tarefas.

Uso: python gerar_codex.py tarefas.json pasta_staging [paralelo]
Cada tarefa: {"id", "prompt", "refs": [caminhos de imagens de referência], "depends": "id opcional"}
A saída de "depends" entra como PRIMEIRA referência (identidade do personagem, ambiente base).
Saída: pasta_staging/<id>/out.png. Tarefas com out.png existente são puladas, o que permite retomar.
"""
import json, os, shutil, subprocess, sys, threading, time
from concurrent.futures import ThreadPoolExecutor

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gerar_codex_util import imagem_da_sessao  # noqa: E402

tarefas = json.load(open(sys.argv[1], encoding="utf-8"))
staging = os.path.abspath(sys.argv[2])
paralelo = int(sys.argv[3]) if len(sys.argv) > 3 else 3
por_id = {t["id"]: t for t in tarefas}
feitos = {}
trava = threading.Lock()

INSTRUCAO = (
    "Use a skill imagegen com a ferramenta embutida image_gen (nao use o CLI nem OPENAI_API_KEY). "
    "Gere exatamente UMA imagem final para o pedido abaixo. As imagens anexadas sao referencias, "
    "na ordem e com o papel descrito no pedido. Depois copie o arquivo gerado de "
    "$CODEX_HOME/generated_images para {saida} (sobrescreva se existir). Nao crie outros arquivos. "
    "Responda apenas com o caminho final.\n\nPEDIDO:\n{prompt}"
)


def saida(tid):
    return os.path.join(staging, tid, "out.png")


def rodar(t):
    tid = t["id"]
    pasta = os.path.join(staging, tid)
    os.makedirs(pasta, exist_ok=True)
    if os.path.exists(saida(tid)):
        return tid, "ja existia"
    dep = t.get("depends")
    if dep:
        while not feitos.get(dep):
            if feitos.get(dep) is False:
                return tid, f"pulado: dependencia {dep} falhou"
            time.sleep(5)
    refs = list(t.get("refs", []))
    if dep:
        refs.insert(0, saida(dep))
    # O prompt vai por stdin ("-") antes dos -i, porque -i aceita vários valores.
    cmd = [shutil.which("codex"), "exec", "--skip-git-repo-check", "-s", "workspace-write", "-C", pasta,
           "-o", os.path.join(pasta, "ultima.txt"), "-"]
    for r in refs:
        cmd += ["-i", r]
    texto = INSTRUCAO.format(saida=saida(tid).replace("\\", "/"), prompt=t["prompt"])
    for tentativa in (1, 2):
        log_path = os.path.join(pasta, f"run{tentativa}.log")
        with open(log_path, "w", encoding="utf-8") as log:
            try:
                subprocess.run(cmd, input=texto, text=True, encoding="utf-8", stdout=log,
                               stderr=subprocess.STDOUT, timeout=1200)
            except subprocess.TimeoutExpired:
                log.write("\nTIMEOUT\n")
        propria = imagem_da_sessao(log_path)
        if propria:
            shutil.copyfile(propria, saida(tid))
            return tid, f"ok (tentativa {tentativa}, imagem da sessão)"
        if os.path.exists(saida(tid)):
            return tid, f"ok (tentativa {tentativa}, cópia do Codex: confira)"
    return tid, "FALHOU"


def tarefa(t):
    tid, status = rodar(t)
    with trava:
        feitos[tid] = os.path.exists(saida(tid))
        print(time.strftime("%H:%M:%S"), tid, status, flush=True)
    return tid, status


# Bases primeiro, para as dependentes não ocuparem todos os workers esperando.
ordem = sorted(tarefas, key=lambda t: 1 if t.get("depends") else 0)
for t in ordem:
    if os.path.exists(saida(t["id"])):
        feitos[t["id"]] = True
    dep = t.get("depends")
    # Dependência fora desta lista: vale o arquivo já gerado; sem ele, não há o que esperar.
    if dep and dep not in por_id:
        feitos[dep] = os.path.exists(saida(dep))
with ThreadPoolExecutor(max_workers=paralelo) as ex:
    resultados = list(ex.map(tarefa, ordem))
falhas = [tid for tid, s in resultados if "FALHOU" in s or "pulado" in s]
print("FIM", len(resultados), "tarefas;", "falhas:", falhas or "nenhuma", flush=True)
