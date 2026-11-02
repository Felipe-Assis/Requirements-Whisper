# rota_corporativo.rpy
# Cadeia de cenas da rota Corporativo (chamada por label start em script.rpy
# quando chosen_job == "corporativo"). Uma label por arquivo, em ordem.

label rota_corporativo:
    call co_01_chegada from _co_01_chegada
    call co_02_ciclo_legado from _co_02_ciclo_legado
    call co_03_casa_sem1 from _co_03_casa_sem1
    call co_04_preparacao from _co_04_preparacao
    call co_05_entrevista from _co_05_entrevista
    call co_06_avaliacao from _co_06_avaliacao
    call co_07_cafe from _co_07_cafe
    call co_08_casa_sem2 from _co_08_casa_sem2
    call co_09_historias from _co_09_historias
    call co_10_almoco from _co_10_almoco
    call co_11_inspecao from _co_11_inspecao
    call co_12_casa_sem3 from _co_12_casa_sem3
    call co_13_arquitetura from _co_13_arquitetura
    call co_14_comemoracao from _co_14_comemoracao
    call co_15_gestao from _co_15_gestao
    call co_16_codificacao from _co_16_codificacao
    call co_17_testes_seguranca from _co_17_testes_seguranca
    call co_18_implantacao_avaliacao from _co_18_implantacao_avaliacao
    return
