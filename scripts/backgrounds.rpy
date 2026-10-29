# O quarto não tinha ilustração no projeto. A composição mantém a cena legível
# sem depender de um arquivo ausente; os objetos usam as artes disponíveis.
image bg quarto_manha = Composite(
    (1920, 1080),
    (0, 0), Solid("#243c47", xysize=(1920, 1080)),
    (1030, 120), Solid("#42616a", xysize=(650, 550)),
    (1060, 150), Solid("#9ab9b4", xysize=(590, 490)),
    (1345, 150), Solid("#42616a", xysize=(20, 490)),
    (1060, 380), Solid("#42616a", xysize=(590, 20)),
    (0, 780), Solid("#192d36", xysize=(1920, 300)))

image bg notebook_vagas = Solid("#122532")
image bg escritorio = Transform("images/bg/escritorio_interior_manha.png", xysize=(1920, 1080), fit="cover")
image bg empresa = Transform("images/bg/empresa_exterior_manha.png", xysize=(1920, 1080), fit="cover")
