# energia.rpy
# -------------------------------
# ENERGIA SEMANAL (0 a 10, sempre inteira)
# -------------------------------
# Recurso visível (HUD abaixo do relógio, número e texto). Energia baixa nunca
# dá game over nem mexe em decisões, registros, conquistas ou final: só tira
# tempo da próxima intermissão e muda algumas falas (energia_cansaco()).
# energia_diaria e nivel_estresse (state_progress.rpy) continuam no save e não
# são lidos. Tabela de ganhos e gastos: docs/design/sistemas-intermissoes.md §4.
#
# Uso nas cenas:
#   $ energia_gastar(3, _("virou a noite"))
#   $ im_hora_extra_somar(60)          # tira até 60 min da próxima intermissão
#   if energia_cansaco():
#       developer_requirements "Você parece cansado. Café?"

default energia_semana = 8
# O HUD aparece a partir da primeira intermissão (im_encerrar liga).
default energia_mostrar = False

init python:

    ENERGIA_MAX = 10

    # (mínimo, texto do estado), do maior para o menor.
    ENERGIA_ESTADOS = [
        (8, _("Alta")),
        (4, _("Boa")),
        (2, _("Cansaço")),
        (0, _("Exaustão")),
    ]

    def _energia_limitar(valor):
        return max(0, min(ENERGIA_MAX, int(valor)))

    def energia_estado(valor=None):
        """Texto do estado: Alta (8-10), Boa (4-7), Cansaço (2-3), Exaustão (0-1)."""
        v = store.energia_semana if valor is None else valor
        for minimo, texto in ENERGIA_ESTADOS:
            if v >= minimo:
                return __(texto)
        return __(ENERGIA_ESTADOS[-1][1])

    def energia_cansaco():
        """True com 3 ou menos (Cansaço ou Exaustão). Para falas alternativas."""
        return store.energia_semana <= 3

    def energia_exaustao():
        """True com 1 ou menos."""
        return store.energia_semana <= 1

    def energia_desconto_bloco():
        """Minutos que a energia baixa tira do próximo bloco de tempo livre."""
        if store.energia_semana <= 1:
            return 60
        if store.energia_semana <= 3:
            return 30
        return 0

    def _energia_mudar(delta, motivo):
        antes = store.energia_semana
        depois = _energia_limitar(antes + delta)
        store.energia_semana = depois
        if depois != antes:
            sinal = "+" if delta >= 0 else "−"
            msg = __("Energia {sinal}{n}").format(sinal=sinal, n=abs(int(delta)))
            if motivo:
                msg += ": " + __(motivo)
            msg += " ({a} → {d})".format(a=antes, d=depois)
            renpy.notify(msg)
        return depois - antes

    def energia_gastar(n, motivo=None):
        """Tira n de energia (limita a 0) e avisa. Devolve a variação real (<= 0)."""
        return _energia_mudar(-abs(int(n)), motivo)

    def energia_ganhar(n, motivo=None):
        """Soma n de energia (limita a 10) e avisa. Devolve a variação real (>= 0)."""
        return _energia_mudar(abs(int(n)), motivo)

    def energia_hud_texto():
        return __("Energia {v}/{m} · {estado}").format(v=store.energia_semana, m=ENERGIA_MAX,
                                                         estado=energia_estado())
