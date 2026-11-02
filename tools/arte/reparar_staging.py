"""Repara um staging gerado antes da correção de sessão em gerar_codex.py.

Para cada tarefa, recopia a imagem da pasta da própria sessão do Codex (lida no log) e lista as que estavam
trocadas. Uso: python reparar_staging.py pasta_staging
"""
import filecmp, glob, os, shutil, sys

sys.path.insert(0, os.path.dirname(__file__))
from gerar_codex_util import imagem_da_sessao  # noqa: E402

staging = sys.argv[1]
trocadas, sem_log = [], []
for pasta in sorted(glob.glob(os.path.join(staging, "*"))):
    logs = sorted(glob.glob(os.path.join(pasta, "run*.log")))
    out = os.path.join(pasta, "out.png")
    if not logs:
        sem_log.append(os.path.basename(pasta))
        continue
    propria = imagem_da_sessao(logs[-1])
    if propria and (not os.path.exists(out) or not filecmp.cmp(propria, out, shallow=False)):
        shutil.copyfile(propria, out)
        trocadas.append(os.path.basename(pasta))
print("trocadas e corrigidas:", trocadas or "nenhuma")
print("sem log (prontas de antes, não verificadas):", sem_log or "nenhuma")
