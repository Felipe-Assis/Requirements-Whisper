# state_time.rpy
#
# In-game clock state and helpers.
# The `default`s stay at init -1 (same priority as before the split); the
# helper functions are de-nested to plain `init python` (prio 0).

init -1:
    default game_hour = 7      # Horas (inteiro, 0-23)
    default game_minute = 0    # Minutos (inteiro, 0-59)
    default show_clock = False  # Se quiser poder ocultar facilmente

# Função para atualizar o horário, se preferir
init python:
    def set_time(hour, minute):
        store.game_hour = hour
        store.game_minute = minute

    def advance_minutes(minutes):
        total = store.game_hour * 60 + store.game_minute + minutes
        store.game_hour = (total // 60) % 24
        store.game_minute = total % 60
