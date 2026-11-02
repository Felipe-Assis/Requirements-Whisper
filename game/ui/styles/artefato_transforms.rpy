# artefato_transforms.rpy
# -------------------------------
# TRANSFORMS DE ARTEFATOS (telas de produto, quadros, diagramas)
# -------------------------------
# Usado pelas três rotas em
#   show expression "images/artifacts/<arquivo>.png" as <tag> at artefato_tela
# center_zoom (sprites) alinha pela base e deixava metade do artefato atrás
# da caixa de diálogo. Aqui a imagem cabe inteira acima da caixa, inclusive
# com "texto maior" (caixa de 390 px): até 1500x640, proporção mantida.

transform artefato_tela:
    fit "contain"
    xysize (1500, 640)
    xalign 0.5
    yanchor 0.0
    ypos 20
