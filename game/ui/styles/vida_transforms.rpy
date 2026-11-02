# vida_transforms.rpy
# -------------------------------
# VIDA NOS SPRITES (respiração) E CÂMERA LEVE
# -------------------------------
# vida_respira entra sozinho em todo sprite de personagem pelo wrapper de
# config.show (fala_destaque.rpy); as cenas não precisam escrever nada. As
# posições (left_zoom, center_zoom...) não mudam: o transform externo herda a
# posição do filho, então yalign 1.0 segura os pés e só o topo respira.
# Sem zoom aqui (config.zoom_zaxis = False não interfere). Amplitude máxima
# de 0,6%: acima de 1,5% a cabeça parece esticar (docs/pesquisa/live2d-3d.md).
#
# Câmera: para as cenas usarem depois, só em momentos marcantes e nunca com
# artefato na tela (artefato_tela também está na camada master):
#     $ cam_foco(0.3)      # aproxima 4% em direção a x = 0.3
#     ...
#     $ cam_reset()        # obrigatório na mesma cena
# Com "Movimento dos personagens: não", cam_foco não faz nada; com
# "Transições: desligadas", o movimento é instantâneo.

# True enquanto a câmera está fora do neutro (o autopiloto confere).
default cam_ativo = False

transform vida_respira(t1=2.6, t2=3.9, amp=0.006, dx=1.5):
    subpixel True
    parallel:
        ease t1 yzoom 1.0 + amp
        ease t1 yzoom 1.0
        repeat
    parallel:
        ease t2 xoffset dx
        ease t2 xoffset -dx
        repeat

# Zoom em torno do centro, com xoffset para manter o ponto x parado na tela.
transform cam_aproxima(x=0.5, z=1.04, t=0.8):
    subpixel True
    xanchor 0.5 xpos 0.5 yanchor 0.35 ypos 0.35
    ease t zoom z xoffset ((x - 0.5) * config.screen_width * (1.0 - z))

transform cam_neutra(t=0.6):
    subpixel True
    xanchor 0.5 xpos 0.5 yanchor 0.35 ypos 0.35
    ease t zoom 1.0 xoffset 0

init python:

    def vida_respira_para(tag):
        # Períodos estáveis por personagem, para não respirarem em sincronia.
        # sum(ord) em vez de hash(): hash() muda a cada execução.
        k = sum(map(ord, tag)) % 5
        return vida_respira(t1=2.4 + 0.12 * k, t2=3.5 + 0.15 * k)

    def cam_tempo(t):
        return 0 if _preferences.transitions == 0 else t

    def cam_foco(x=0.5, z=1.04, t=0.8):
        """Aproxima a câmera (camada master) em direção a x. Par de cam_reset()."""
        if not persistent.vida_movimento:
            return
        renpy.show_layer_at([cam_aproxima(x=x, z=z, t=cam_tempo(t))], layer="master", camera=True)
        store.cam_ativo = True

    def cam_reset(t=0.6):
        """Volta a câmera ao neutro. Pode ser chamada mesmo sem cam_foco antes."""
        if store.cam_ativo:
            renpy.show_layer_at([cam_neutra(t=cam_tempo(t))], layer="master", camera=True)
        store.cam_ativo = False
