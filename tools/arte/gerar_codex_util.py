"""Funções comuns às ferramentas de geração com o Codex."""
import glob, os, re

# O Codex grava cada imagem em $CODEX_HOME/generated_images/<session id>/. Com várias execuções em paralelo,
# pedir ao Codex "copie a imagem gerada" às vezes copia a de outra sessão. Por isso as ferramentas leem o
# session id no log da execução e copiam elas mesmas a imagem dessa sessão.
CODEX_HOME = os.environ.get("CODEX_HOME") or os.path.join(os.path.expanduser("~"), ".codex")


def imagem_da_sessao(log_path):
    """Caminho da imagem mais recente gerada pela sessão registrada no log, ou None."""
    try:
        texto = open(log_path, encoding="utf-8", errors="replace").read()
    except OSError:
        return None
    m = re.search(r"session id:\s*([0-9a-f-]{36})", texto)
    if not m:
        return None
    pngs = glob.glob(os.path.join(CODEX_HOME, "generated_images", m.group(1), "*.png"))
    return max(pngs, key=os.path.getmtime) if pngs else None
