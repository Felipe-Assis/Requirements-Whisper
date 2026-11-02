# fala_destaque.rpy
# -------------------------------
# DESTAQUE DE QUEM FALA (escurece levemente quem não está falando)
# -------------------------------
# Técnica (docs/design/sistemas-intermissoes.md, 6.1):
# 1. Character(..., image="<id>") em data/characters.rpy: assim
#    renpy.get_say_image_tag() devolve a tag de quem fala.
# 2. config.show passa por fala_show, que acrescenta ao at_list dos sprites
#    de personagem o fala_foco (e a respiração, vida_transforms.rpy). show
#    expression (artefatos, itens), scene/fundos e telas passam direto.
# 3. fala_foco chama um FalaFoco a cada ~0,05 s: se quem fala está na tela e
#    não é esta tag, escurece em 0,15 s (brilho x0,72 e saturação x0,75);
#    senão, volta ao normal. Só durante a fala: depois dela (num menu, por
#    exemplo) o Ren'Py devolve get_say_image_tag() ao valor anterior.
# Narrador, jogador e personagens sem sprite na tela: ninguém escurece.
# show <id> <pose> sem "at" mantém os transforms anteriores (e o foco).
#
# A classe FalaFoco vai para o save junto com a lista de cenas: não remover
# nem renomear depois de publicada. Para desligar, use a preferência
# "Destacar quem fala" (persistent.fala_destaque), que vale na hora.

init -1 python:

    class FalaFoco(object):
        """Estado do escurecimento de um sprite (0 = normal, 1 = escurecido)."""

        TICK = 0.05
        DURACAO = 0.15

        def __init__(self, tag):
            self.tag = tag
            self.n = 0.0
            self.ultimo = None

        def alvo(self):
            if not persistent.fala_destaque:
                return 0.0
            falante = renpy.get_say_image_tag()
            if falante and falante != self.tag and renpy.showing(falante):
                return 1.0
            return 0.0

        def __call__(self, trans, st, at):
            alvo = self.alvo()
            if self.ultimo is None or st < self.ultimo:
                # Primeiro quadro (ou transform reiniciado): vai direto ao alvo.
                self.n = alvo
            else:
                passo = (st - self.ultimo) / self.DURACAO
                if self.n < alvo:
                    self.n = min(alvo, self.n + passo)
                else:
                    self.n = max(alvo, self.n - passo)
            self.ultimo = st
            n = self.n
            if n > 0:
                # Escurece multiplicando (TintMatrix), não subtraindo: com
                # BrightnessMatrix(-0.22) as roupas escuras viravam preto chapado.
                f = 1.0 - 0.28 * n
                trans.matrixcolor = TintMatrix(Color(rgb=(f, f, f))) * SaturationMatrix(1.0 - 0.25 * n)
            else:
                trans.matrixcolor = None
            return 0 if n != alvo else self.TICK

    # Tags de personagem com sprite: preenchido em init 3 com todo Character
    # que tem image= (8 developers, doutoras, npc_roommate e as rotas novas).
    FALA_TAGS = set()

    def fala_tag(name, tag=None):
        if tag:
            return tag
        if isinstance(name, tuple):
            return name[0]
        return name.split()[0]

    _fala_show_original = config.show or renpy.show

    def fala_show(name, at_list=[], layer=None, what=None, zorder=None, tag=None, behind=[], atl=None, **kwargs):
        t = fala_tag(name, tag)
        # Só sprites de personagem com posição explícita ("at"). Sem "at", o
        # Ren'Py mantém os transforms de antes, inclusive o foco.
        if what is None and at_list and t in FALA_TAGS:
            extra = [fala_foco(t)]
            if persistent.vida_movimento:
                extra.append(vida_respira_para(t))
            at_list = list(at_list) + extra
        return _fala_show_original(name, at_list=at_list, layer=layer, what=what, zorder=zorder,
                                   tag=tag, behind=behind, atl=atl, **kwargs)

    config.show = fala_show

    def fala_prever(*args, **kwargs):
        # Previsão da fala igual à padrão, mas sem prever a imagem
        # "side <tag> <pose>": o jogo não tem side images, e com image= a
        # previsão padrão a procurava e gerava ImageNotFound (inofensivo,
        # porém ruído nos relatórios do autopiloto).
        anterior = store._side_image_attributes
        store._side_image_attributes = None
        try:
            return renpy.character.predict_show_display_say(*args, **kwargs)
        finally:
            store._side_image_attributes = anterior

init 3 python:
    for _fala_nome, _fala_obj in list(store.__dict__.items()):
        if isinstance(_fala_obj, ADVCharacter) and getattr(_fala_obj, "image_tag", None):
            FALA_TAGS.add(_fala_obj.image_tag)
            _fala_obj.predict_function = fala_prever
    del _fala_nome, _fala_obj

transform fala_foco(tag):
    function FalaFoco(tag)
