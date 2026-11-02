# rota_startup.rpy
# Cadeia de cenas da rota Startup (chamada por label start em script.rpy
# quando chosen_job == "startup"). Uma label por arquivo, em ordem.

label rota_startup:
    call st_01_chegada from _st_01_chegada
    call st_02_reuniao_ciclo from _st_02_reuniao_ciclo
    call st_03_casa_sem1 from _st_03_casa_sem1
    call st_04_preparacao from _st_04_preparacao
    call st_05_entrevista from _st_05_entrevista
    call st_06_classificacao from _st_06_classificacao
    call st_07_social from _st_07_social
    call st_08_casa_sem2 from _st_08_casa_sem2
    call st_09_historias from _st_09_historias
    call st_10_almoco from _st_10_almoco
    call st_11_inspecao from _st_11_inspecao
    call st_12_casa_sem3 from _st_12_casa_sem3
    call st_13_arquitetura from _st_13_arquitetura
    call st_14_comemoracao from _st_14_comemoracao
    call st_15_gestao from _st_15_gestao
    call st_16_codificacao from _st_16_codificacao
    call st_17_testes_seguranca from _st_17_testes_seguranca
    call st_18_lancamento from _st_18_lancamento
    return
