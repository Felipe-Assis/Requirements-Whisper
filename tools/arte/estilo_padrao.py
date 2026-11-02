"""Padrão de personagem do jogo: o traço da Emily (developer_requirements). Decisão do usuário em 2026-11-02.

Todo lote novo de personagens importa daqui o texto de estilo e as referências, em vez de reescrever o seu.
Explicação e histórico em docs/arte/README.md, seção "Referência padrão: a Emily".
"""
import os

RAIZ = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
REF = os.path.join(RAIZ, "docs", "arte", "referencias").replace("\\", "/")

# Anexe sempre REF_EMILY como referência de estilo; anexe REF_ROSTOS quando o rosto importar (personagem novo,
# redesenho, expressões). As duas são só de traço: o prompt deve dizer "não copie as pessoas".
REF_EMILY = f"{REF}/estilo-c-emily.png"
REF_ROSTOS = f"{REF}/estilo-c-rostos.png"  # Emily, Tainá, Kauã e Dra. Michelle, cabeça e ombros

CORPO = (
    "Estilo C, IGUAL ao da Emily: proporção de ADULTO com ~7,5 cabeças, cabeça proporcional, ombros e mãos naturais; "
    "roupas com costuras, dobras e sombras suaves de 1 tom; contorno escuro com leve textura de lápis; cores suaves e "
    "levemente dessaturadas. Nem realista (sem textura de foto, sem anatomia detalhada) nem cartunesco (sem cabeça "
    "grande, sem olhos enormes)."
)

ROSTO = (
    "ROSTO NO TRAÇO DA EMILY: pele chapada de um tom só com no máximo uma sombra simples, sem textura, sem sardas, "
    "sem rugas, sem marcas de expressão; olhos com íris escura simples e um único brilho branco, cílios só como um "
    "traço grosso na pálpebra de cima, sem maquiagem desenhada; nariz como um traço curto; boca em forma simples, "
    "sem batom nem lábios detalhados; sobrancelhas como uma faixa escura grossa, que carrega a expressão. Barba, "
    "quando houver, como uma mancha lisa de um tom, sem fios. A idade aparece no formato do rosto, no cabelo e na "
    "roupa, não em detalhes do rosto."
)

SPRITE = (
    "Sprite de visual novel: corpo inteiro em pé, do topo da cabeça aos pés, centralizado, fundo totalmente "
    "transparente (PNG com alfa), sem sombra no chão, sem texto, retrato 2:3."
)

ESTILO = f"{CORPO} {ROSTO} {SPRITE}"
