# Arquivo: backgrounds.rpy
# Os fundos são 1536x1024 (3:2). Antes eram esticados para 1920x1080 (cerca de
# 18% na horizontal). bg_cobrir recorta a faixa central 16:9 e só então escala,
# como um fit "cover" centralizado, sem distorcer. O recorte é explícito para
# não depender de como a scene posiciona uma imagem maior que a tela.

init -1 python:
    def bg_cobrir(arquivo, foco_y=0.5, largura=1536, altura=1024):
        # foco_y escolhe a faixa vertical que fica: 0 = topo, 0.5 = centro, 1 = base.
        alt_16x9 = int(largura * 9 / 16)
        if alt_16x9 <= altura:
            crop = (0, int((altura - alt_16x9) * foco_y), largura, alt_16x9)
        else:
            larg_16x9 = int(altura * 16 / 9)
            crop = (int((largura - larg_16x9) / 2), 0, larg_16x9, altura)
        return Transform(arquivo, crop=crop, xysize=(config.screen_width, config.screen_height))

image bg tela_conquistas = bg_cobrir("images/bg/tela_conquistas.png")
image bg creditos = bg_cobrir("images/bg/tela_conquistas.png")

image bg fachada_instituto_tarde = bg_cobrir("images/bg/fachada_instituto_tarde.png")

image bg escritorio_medica = bg_cobrir("images/bg/escritorio_medica.png")

image bg empresa_cafe_manha = bg_cobrir("images/bg/empresa_cafe_manha.png")
image bg empresa_cafe_tarde = bg_cobrir("images/bg/empresa_cafe_tarde.png")


image bg refeitorio_tarde = bg_cobrir("images/bg/refeitorio_tarde.png")

image bg cozinha_noite = bg_cobrir("images/bg/cozinha_noite.png")

image bg transito_manha = bg_cobrir("images/bg/transito_manha.png")
image bg transito_tarde = bg_cobrir("images/bg/transito_tarde.png")
image bg transito_noite = bg_cobrir("images/bg/transito_noite.png")

image bg sala_reunioes_manha = bg_cobrir("images/bg/sala_reunioes_manha.png")
image bg sala_reunioes_tarde = bg_cobrir("images/bg/sala_reunioes_tarde.png")

# Quartos
image bg quarto_manha = bg_cobrir("images/bg/quarto_manha.png")
image bg quarto_noite = bg_cobrir("images/bg/quarto_noite.png")

# Empresa/Escritório - Exterior
image bg empresa_exterior_manha = bg_cobrir("images/bg/empresa_exterior_manha.png")
image bg empresa_exterior_noite = bg_cobrir("images/bg/empresa_exterior_noite.png")

# Escritório - Interior
image bg escritorio_interior_festa = bg_cobrir("images/bg/escritorio_interior_festa.png")
image bg escritorio_interior_manha = bg_cobrir("images/bg/escritorio_interior_manha.png")
image bg escritorio_interior_tarde = bg_cobrir("images/bg/escritorio_interior_tarde.png")
image bg escritorio_interior_noite = bg_cobrir("images/bg/escritorio_interior_noite.png")
image bg escritorio_interior_vazio = bg_cobrir("images/bg/escritorio_interior_vazio.png")
# Rotas Startup e Corporativo (arte gerada com o Codex em 2026-11-02; ver docs/rotas/*-assets.json)
image bg startup_coworking_manha = bg_cobrir("images/bg/startup_coworking_manha.png")
image bg startup_coworking_tarde = bg_cobrir("images/bg/startup_coworking_tarde.png")
image bg startup_coworking_noite = bg_cobrir("images/bg/startup_coworking_noite.png")
image bg startup_terraco_noite = bg_cobrir("images/bg/startup_terraco_noite.png")
image bg demo_day_auditorio = bg_cobrir("images/bg/demo_day_auditorio.png")
image bg central_atendimento_manha = bg_cobrir("images/bg/central_atendimento_manha.png")
image bg central_atendimento_tarde = bg_cobrir("images/bg/central_atendimento_tarde.png")
image bg sala_servidores = bg_cobrir("images/bg/sala_servidores.png")
image bg sala_arquivo_tarde = bg_cobrir("images/bg/sala_arquivo_tarde.png")
