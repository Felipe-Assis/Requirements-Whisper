# rota_corporativo.rpy
# Cadeia de cenas da rota Corporativo (chamada por label start em script.rpy
# quando chosen_job == "corporativo"). Uma label por arquivo, em ordem.
# Tempo livre (docs/design/intermissoes-corporativo.md, seção 2.0): as semanas
# 1 a 4 e 8 entram aqui na cadeia; as semanas 5, 6 e 7 entram dentro de
# co_15, co_16 e co_17, antes do cartão "Fim da Semana". O ponto de parada vem
# logo depois da cena que mostra o cartão de cada semana (1 a 7).

label rota_corporativo:
    call co_01_chegada from _co_01_chegada
    call co_02_ciclo_legado from _co_02_ciclo_legado
    call im_intermissao(1) from _im_corporativo_s1
    call co_03_casa_sem1 from _co_03_casa_sem1
    call im_ponto_parada(1) from _pp_corporativo_s1
    call co_04_preparacao from _co_04_preparacao
    call co_05_entrevista from _co_05_entrevista
    call co_06_avaliacao from _co_06_avaliacao
    call co_07_cafe from _co_07_cafe
    call im_intermissao(2) from _im_corporativo_s2
    call co_08_casa_sem2 from _co_08_casa_sem2
    call im_ponto_parada(2) from _pp_corporativo_s2
    call co_09_historias from _co_09_historias
    call co_10_almoco from _co_10_almoco
    call co_11_inspecao from _co_11_inspecao
    call im_intermissao(3) from _im_corporativo_s3
    call co_12_casa_sem3 from _co_12_casa_sem3
    call im_ponto_parada(3) from _pp_corporativo_s3
    call co_13_arquitetura from _co_13_arquitetura
    call im_intermissao(4) from _im_corporativo_s4
    call co_14_comemoracao from _co_14_comemoracao
    call im_ponto_parada(4) from _pp_corporativo_s4
    call co_15_gestao from _co_15_gestao
    call im_ponto_parada(5) from _pp_corporativo_s5
    call co_16_codificacao from _co_16_codificacao
    call im_ponto_parada(6) from _pp_corporativo_s6
    call co_17_testes_seguranca from _co_17_testes_seguranca
    call im_ponto_parada(7) from _pp_corporativo_s7
    call im_intermissao(8) from _im_corporativo_s8
    call co_18_implantacao_avaliacao from _co_18_implantacao_avaliacao
    return
