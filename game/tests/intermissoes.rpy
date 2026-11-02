# Tempo livre: dados, tempo e energia, opções e deslocamento, teto de
# amizade, pistas, mentoria, telas do mapa e as 8 intermissões de cada rota
# chamadas direto (as cenas ainda não chamam im_intermissao).

# Temporários dos testes abaixo.
default rw_avisos = 0
default rw_telas = 0
default rw_antes = None

# Labels auxiliares (só existem com a pasta de testes).
label rw_teste_intermissoes(rota, modo="primeira", mapa=None):
    # Roda as 8 intermissões e os 7 pontos de parada da rota com o autopiloto.
    $ chosen_job = rota
    $ autopiloto.ligar(rota, modo, mapa=mapa)
    $ renpy.dynamic("rw_n")
    $ rw_n = 1
    while rw_n <= 8:
        # Sem as cenas no meio, o relógio vai para o início do bloco.
        $ set_time(*im_dados(rw_n)["inicio"])
        call im_intermissao(rw_n) from _rw_teste_im
        if rw_n < 8:
            call im_ponto_parada(rw_n) from _rw_teste_pp
        $ rw_n += 1
    $ autopiloto.concluir("ok")
    "Fim do teste das intermissões."
    return

label rw_teste_pista(pid):
    call pista_lembrar(pid) from _rw_teste_pista
    "Fim do teste de pista."
    return


testsuite intermissoes:
    before testcase:
        if not screen "main_menu":
            run MainMenu(confirm=False)
        pause until screen "main_menu"
        run Start()
        pause until screen "say"

    after testcase:
        $ autopiloto.desligar()
        $ persistent.im_pular = False
        $ persistent.im_mapa_lista = False

    testcase dados_validos:
        parameter rota = ["saude", "startup", "corporativo"]
        assert eval im_validar_dados(rota) == []
        assert eval len(ROUTES[rota]["extras"]) == 7
        assert eval len(ROUTES[rota]["mentoria"]["passos"]) == 5
        assert eval all(p["lugar"] in MAPA_LUGARES for p in ROUTES[rota]["mapa"]["pois"])

    testcase deslocamento_por_distancia:
        $ chosen_job = "startup"
        assert eval im_trajeto("mesa", "sala_vidro") == {"minutos": 0, "meio": "escada", "de": "casarao", "para": "casarao"}
        assert eval im_trajeto("mesa", "cafe")["minutos"] == 0 and im_trajeto("mesa", "cafe")["meio"] == "escada"
        assert eval im_trajeto("mesa", "ponto")["minutos"] == 10
        assert eval (im_trajeto("mesa", "bandejao")["minutos"], im_trajeto("mesa", "bandejao")["meio"]) == (30, "onibus")
        assert eval (im_trajeto("bandejao", "aceleradora")["minutos"], im_trajeto("bandejao", "aceleradora")["meio"]) == (25, "onibus")
        assert eval im_trajeto("mesa", "mesa")["meio"] is None
        $ chosen_job = "saude"
        assert eval (im_trajeto("mesa", "cafe")["minutos"], im_trajeto("mesa", "cafe")["meio"]) == (0, None)
        assert eval (im_trajeto("mesa", "ambulatorio")["minutos"], im_trajeto("mesa", "ambulatorio")["meio"]) == (10, "campus")
        $ chosen_job = "corporativo"
        assert eval (im_trajeto("baia", "arquivo")["minutos"], im_trajeto("baia", "arquivo")["meio"]) == (0, "elevador")

    testcase opcoes_tempo_e_energia:
        $ chosen_job = "startup"
        $ im_iniciar(2)
        assert eval im_minutos == 210 and im_local == "mesa" and (game_hour, game_minute) == (15, 0)
        # O deslocamento entra no custo: observar no bandejão = 30 + 90.
        assert eval [o["minutos"] for o in im_opcoes(2) if o["acao"] == "observar"] == [120]
        # Com 30 min sobrando, só conversar no mesmo prédio cabe.
        $ im_minutos = 30
        assert eval im_opcoes(2) and all(o["acao"] == "conversar" and o["min_desloc"] == 0 for o in im_opcoes(2))
        $ im_minutos = 210
        # Com energia 1, ajudar (−2) fica fora, com o motivo escrito.
        $ energia_semana = 1
        assert eval not any(o["acao"] == "ajudar" for o in im_opcoes(2))
        assert eval any(o["acao"] == "ajudar" and o["motivo"] == "Precisa de 2 de energia" for o in im_opcoes(2, todas=True))
        # Cansaço: descansar vem primeiro e recomendado.
        assert eval im_opcoes(2)[0]["acao"] == "descansar" and im_opcoes(2)[0]["recomendado"]
        $ energia_semana = 8
        # Ação feita não volta.
        $ im_registro_semana(2)["acoes"].append(["mesa", "conversar", "st_mobile"])
        assert eval not any(o["acao"] == "conversar" and o["alvo"] == "st_mobile" for o in im_opcoes(2))
        assert eval any(o["alvo"] == "st_mobile" and o["acao"] == "conversar" and o["motivo"] == "Já feito hoje" for o in im_opcoes(2, todas=True))
        # Falta de tempo com trajeto: o motivo soma as partes.
        $ im_minutos = 100
        assert eval any(o["acao"] == "observar" and o["motivo"] == "Falta tempo (precisa de 120 min: 90 + 30 de trajeto)" for o in im_opcoes(2, todas=True))

    testcase energia_e_bloco:
        $ energia_gastar(20)
        assert eval energia_semana == 0 and energia_estado() == "Exaustão"
        $ energia_ganhar(50)
        assert eval energia_semana == 10 and energia_estado() == "Alta"
        assert eval [energia_estado(v) for v in (7, 4, 3, 2, 1)] == ["Boa", "Boa", "Cansaço", "Cansaço", "Exaustão"]
        $ chosen_job = "startup"
        $ energia_semana = 3
        $ im_iniciar(3)
        assert eval im_minutos == 180 and energia_cansaco()
        $ energia_semana = 1
        $ im_iniciar(3)
        assert eval im_minutos == 150
        $ energia_semana = 8
        $ im_hora_extra_somar(45)
        $ im_hora_extra_somar(45)
        assert eval im_hora_extra == 60
        $ im_iniciar(3)
        assert eval im_minutos == 150 and im_hora_extra == 0
        # mesmo_dia: começa no relógio atual e mantém o fim; mínimo de 90.
        $ set_time(17, 0)
        $ im_iniciar(5)
        assert eval im_minutos == 150 and im_fim == (19, 30)
        $ rw_avisos = len(IM_DIAG.relogio_volta)
        $ set_time(19, 0)
        $ im_iniciar(5)
        assert eval im_minutos == 90 and len(IM_DIAG.relogio_volta) == rw_avisos + 1
        $ del IM_DIAG.relogio_volta[rw_avisos:]
        # Fim de semana: +3, teto 10, estado zerado, HUD ligado.
        $ energia_semana = 9
        $ im_encerrar(5)
        assert eval energia_semana == 10 and im_semana_atual == 0 and energia_mostrar

    testcase teto_de_amizade:
        $ chosen_job = "startup"
        $ im_iniciar(6)
        $ im_amizade("st_mobile", 1.0)
        $ im_amizade("st_techlead", 1.0)
        $ im_amizade("st_ceo", 1.0)
        assert eval (amizade_st_mobile, amizade_st_techlead, amizade_st_ceo) == (1.0, 1.0, 0.0)
        assert eval any(o["aviso"] == "Teto de amizade atingido" for o in im_opcoes(6, todas=True))
        $ im_iniciar(5)
        $ im_amizade("st_mobile", 1.0)
        $ im_amizade("st_mobile", 0.5)
        assert eval amizade_st_mobile == 2.0

    testcase pistas_janela_e_lembrar:
        $ chosen_job = "startup"
        # (As chamadas ficam fora do assert: ele pode ser avaliado mais de uma vez.)
        $ rw_antes = pista_ganhar("st_p_tunel", semana=4)
        assert eval rw_antes is False and not pista_tem("st_p_tunel")
        $ rw_antes = pista_ganhar("st_p_tunel", semana=3)
        assert eval rw_antes is True and pista_tem("st_p_tunel")
        $ rw_antes = pista_ganhar("st_p_inexistente")
        assert eval rw_antes is False and "st_p_inexistente" not in pistas
        # Sem a pista: pista_lembrar não mostra nada.
        run Call("rw_teste_pista", "st_p_bolsa")
        advance until "Fim do teste de pista"
        assert eval "st_p_bolsa" not in pistas_usadas
        # Com a pista: menu de lembrar, e ela fica usada.
        run Call("rw_teste_pista", "st_p_tunel")
        advance until screen "choice"
        click "Lembrar: Salvar duas vezes no subsolo"
        advance until "Fim do teste de pista"
        assert eval "st_p_tunel" in pistas_usadas and not pista_disponivel("st_p_tunel")

    testcase mentoria_em_ordem:
        $ chosen_job = "startup"
        $ rw_antes = (st_conquistas(), st_final_grade(), route_final_grade(), len(route_achievements()))
        assert eval mentoria_proximo() == 1 and mentoria_disponivel(1) is None
        $ im_iniciar(3)
        assert eval [o["rotulo"] for o in im_opcoes(3) if o["acao"] == "mentoria"] == ["Mentoria com Lorena (1 de 5)"]
        $ [mentoria_avancar() for _i in range(4)]
        assert eval mentoria_passos["startup"] == 4 and not mentoria_conq_startup
        assert eval "st_p_leitor" in pistas
        $ mentoria_avancar()
        assert eval mentoria_conq_startup and mentoria_proximo() is None
        assert eval [a["id"] for a in conquistas_extra_obtidas()] == ["mentoria_conq_startup"]
        assert eval (st_conquistas(), st_final_grade(), route_final_grade(), len(route_achievements())) == rw_antes

    testcase mapa_deslocamento_e_transicao:
        $ chosen_job = "startup"
        $ _preferences.transitions = 2
        # Tempos longos: só o clique fecha as telas a tempo.
        $ MAPA_TEMPO_MARCADOR = 30.0
        $ MAPA_TEMPO_TRANSICAO = [(999, 30.0)]
        $ MAPA_TEMPO_CARTAO = 30.0
        $ rw_telas = len(IM_DIAG.telas)
        run Call("im_intermissao", 2)
        pause until screen "im_abertura_cartao"
        click id "im_abrir_mapa"
        pause until screen "im_mapa"
        click "Bandejão da universidade"
        pause until "Conversar com Bia"
        click "Conversar com Bia"
        pause until screen "im_deslocamento"
        click pos (960, 540)
        pause until screen "im_transicao" timeout 5
        click pos (960, 540)
        pause until screen "say" timeout 5
        assert eval IM_DIAG.telas[rw_telas:] == ["deslocamento", "transicao"]
        assert eval im_local == "bandejao" and (game_hour, game_minute) == (15, 30)
        advance until screen "im_mapa"
        assert eval (game_hour, game_minute) == (16, 0) and im_minutos == 150
        # Transições desligadas: só o cartão de texto, também pulável.
        $ _preferences.transitions = 0
        click "Casarão amarelo"
        pause until "Conversar com Davi"
        click "Conversar com Davi"
        pause until screen "im_transicao" timeout 5
        assert eval IM_DIAG.telas[-1] == "cartao"
        click pos (960, 540)
        advance until screen "im_mapa"
        assert eval im_local == "mesa" and im_minutos == 90
        click id "im_encerrar"
        pause until screen "im_resumo"
        click id "im_resumo_continuar"
        pause until eval im_semana_atual == 0
        assert eval im_feitas["startup"][2]["encerrou_cedo"] and im_feitas["startup"][2]["trajetos"] == 2
        assert eval im_feitas["startup"][2]["acoes"] == [["bandejao", "conversar", "st_estudante"], ["mesa", "conversar", "st_mobile"]]

    testcase mapa_como_lista:
        $ chosen_job = "corporativo"
        $ persistent.im_mapa_lista = True
        run Call("im_intermissao", 1)
        pause until screen "im_abertura_cartao"
        click id "im_abrir_mapa"
        advance until screen "im_mapa"
        assert eval renpy.get_screen("im_mapa").scope["lista"]
        click "Conversar com Kauã"
        advance until screen "im_mapa"
        assert eval im_feitas["corporativo"][1]["acoes"] == [["baia", "conversar", "co_dev"]]
        click id "im_encerrar"
        pause until screen "im_resumo"
        click id "im_resumo_continuar"
        pause until eval im_semana_atual == 0

    testcase pular_pela_preferencia:
        $ chosen_job = "corporativo"
        $ persistent.im_pular = True
        run Call("im_intermissao", 1)
        pause until eval im_feitas.get("corporativo", {}).get(1, {}).get("concluida")
        assert eval im_feitas["corporativo"][1]["pulada"] and im_fim == (17, 0)
        assert eval im_feitas["corporativo"][1]["acoes"] == [] and energia_mostrar

    testcase ponto_de_parada:
        $ chosen_job = "startup"
        run Call("im_ponto_parada", 2)
        pause until screen "im_parada"
        assert eval save_name == "Semana 3 · Trocado"
        click id "im_parada_continuar"
        pause until eval not renpy.get_screen("im_parada")

    # As 8 intermissões de cada rota, chamadas direto, com o autopiloto na
    # prioridade (mentoria > observar > ajudar > ...).
    testcase intermissoes_diretas:
        parameter rota = ["saude", "startup", "corporativo"]
        run Call("rw_teste_intermissoes", rota)
        pause until eval autopiloto.terminou() timeout 180
        assert eval autopiloto.relatorio()["motivo"] == "ok"
        assert eval autopiloto.relatorio()["erros"] == []
        assert eval autopiloto.relatorio()["intermissoes"] == 8
        assert eval autopiloto.relatorio()["relogio_volta"] == []
        assert eval autopiloto.relatorio()["imagens_nao_encontradas"] == []
        # Isolamento: nada do caminho principal muda.
        assert eval registros_contagem()[0] == 0 and aprendizagem == {}
        assert eval 0 <= energia_semana <= 10
        assert eval mentoria_passos[rota] == 5 and all(achievement_unlocked(a) for a in conquistas_extra())
        assert eval not any(a["id"].startswith("mentoria_conq") for a in route_achievements())
        assert eval len(pistas) > 0
        assert eval tempo_livre_resumo()["intermissoes"] == 8 and tempo_livre_resumo()["mentoria"] == (5, 5)

    testcase intermissoes_puladas:
        parameter rota = ["saude", "startup", "corporativo"]
        run Call("rw_teste_intermissoes", rota, "primeira", "pular")
        pause until eval autopiloto.terminou() timeout 120
        assert eval autopiloto.relatorio()["motivo"] == "ok" and autopiloto.relatorio()["erros"] == []
        assert eval len(im_feitas[rota]) == 8 and all(r["pulada"] for r in im_feitas[rota].values())
        assert eval mentoria_passos.get(rota, 0) == 0 and pistas == set()

    testcase intermissoes_aleatorias:
        parameter rota = ["saude", "startup", "corporativo"]
        run Call("rw_teste_intermissoes", rota, "aleatorio:5")
        pause until eval autopiloto.terminou() timeout 180
        assert eval autopiloto.relatorio()["motivo"] == "ok" and autopiloto.relatorio()["erros"] == []
        assert eval autopiloto.relatorio()["intermissoes"] == 8
        assert eval registros_contagem()[0] == 0 and aprendizagem == {}
