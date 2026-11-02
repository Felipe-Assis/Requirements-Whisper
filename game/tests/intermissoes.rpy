# Tempo livre: dados, tempo e energia, opções e deslocamento, teto de
# amizade, pistas, mentoria, telas do mapa e as 8 intermissões de cada rota
# chamadas direto (as cenas ainda não chamam im_intermissao).

# Temporários dos testes abaixo.
default rw_avisos = 0
default rw_telas = 0
default rw_antes = None

init python:
    # Destinos do lote de arte (docs/arte/prompts/mapa-saidas.json): os
    # caminhos que o motor monta têm de ser exatamente estes.
    RW_MAPA_SAIDAS = set([
        "images/mapa/cidade_base.png", "images/mapa/voce.png",
        "images/mapa/lugares/republica.png", "images/mapa/lugares/predio_projeto.png",
        "images/mapa/lugares/praca_campus.png", "images/mapa/lugares/instituto.png",
        "images/mapa/lugares/bandejao.png", "images/mapa/lugares/casarao.png",
        "images/mapa/lugares/cafe_esquina.png", "images/mapa/lugares/orla.png",
        "images/mapa/lugares/aterro.png", "images/mapa/lugares/torre_vertice.png",
        "images/mapa/lugares/aceleradora.png", "images/mapa/lugares/subestacao.png",
        "images/mapa/icones/conversando.png", "images/mapa/icones/estudando.png",
        "images/mapa/icones/reuniao.png", "images/mapa/icones/celular.png",
        "images/mapa/icones/descansando.png", "images/mapa/icones/observando.png",
        "images/mapa/icones/programando.png", "images/mapa/icones/cafe.png",
        "images/bg/transicao_onibus.png", "images/bg/transicao_metro.png",
        "images/bg/transicao_calcada.png", "images/bg/transicao_elevador.png",
        "images/bg/transicao_campus.png", "images/bg/transicao_escada.png",
    ])
    # Larguras ajustadas na montagem do mapa (docs/arte/prompts/mapa-coordenadas-ajustadas.json).
    RW_MAPA_LARGURAS = {"republica": 220, "predio_projeto": 300, "praca_campus": 220, "instituto": 270,
                        "bandejao": 230, "casarao": 330, "cafe_esquina": 170, "orla": 280, "aterro": 300,
                        "torre_vertice": 270, "aceleradora": 320, "subestacao": 260}

    def rw_mapa_caminhos():
        """Todos os caminhos de imagem que o motor do mapa usa."""
        c = MAPA_CIDADE
        r = set([c["base"], c["voce"]])
        r |= set(c["pasta_lugares"] + lid + ".png" for lid in MAPA_LUGARES)
        r |= set(c["pasta_icones"] + i + ".png" for i in MAPA_ICONES)
        r |= set(c["pasta_icones"] + v[1] + ".png" for v in MAPA_ATIVIDADES.values())
        r |= set(c["pasta_transicoes"] + m + ".png" for m in MAPA_MEIOS)
        return r

    def rw_desl(poi):
        """(meio, minutos, imagem, som, volume, som de chegada) para ir até o poi."""
        d = im_deslocamento_info({"poi": poi})
        return (d["meio"], d["minutos"], d["imagem"], d["som"], d["volume"], d["som_chegada"])

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

    # Dados da cidade alinhados a docs/design/mapa-cidade.md e ao lote de arte.
    testcase mapa_cidade_alinhado:
        assert eval im_validar_mapa() == []
        assert eval MAPA_CIDADE["tamanho"] == (2560, 1440) and _im_escala() == 0.75
        assert eval rw_mapa_caminhos() == RW_MAPA_SAIDAS
        assert eval dict((l, L["largura"]) for l, L in MAPA_LUGARES.items()) == RW_MAPA_LARGURAS
        assert eval sorted(MAPA_ICONES) == sorted(["conversando", "estudando", "reuniao", "celular", "descansando", "observando", "programando", "cafe"])
        assert eval MAPA_CASA == "republica" and _im_caixa("bandejao")["x"] == 1777 and _im_caixa("bandejao")["y"] == 525
        # Painel do lado oposto: x > 1280 na base vai para a esquerda.
        assert eval MAPA_LUGARES["instituto"]["ancora"][0] > 1280 > MAPA_LUGARES["casarao"]["ancora"][0]

    # Folga de 30 min nas semanas 2-8 da Saúde e da Startup (§5); o
    # Corporativo e a semana 1 não mudam.
    testcase folga_de_trajeto:
        assert eval [(ROUTES["saude"]["intermissoes"][n]["inicio"], ROUTES["saude"]["intermissoes"][n]["bloco"]) for n in range(1, 9)] == [((16, 0), 120), ((16, 0), 210), ((15, 0), 210), ((11, 30), 210), ((16, 0), 210), ((16, 0), 210), ((15, 30), 210), ((9, 30), 210)]
        assert eval [(ROUTES["startup"]["intermissoes"][n]["inicio"], ROUTES["startup"]["intermissoes"][n]["bloco"]) for n in range(1, 9)] == [((15, 0), 120), ((15, 0), 210), ((15, 0), 210), ((14, 30), 210), ((16, 0), 210), ((18, 0), 180), ((11, 30), 180), ((13, 30), 210)]
        assert eval [ROUTES["corporativo"]["intermissoes"][n]["bloco"] for n in range(1, 9)] == [120] + [180] * 7

    testcase aterro_no_corporativo:
        $ chosen_job = "corporativo"
        assert eval [p["estado"] for p in im_pois(1) if p["id"] == "aterro"] == ["futuro"]
        assert eval [p["estado"] for p in im_pois(2) if p["id"] == "aterro"] == ["aberto"]
        assert eval (im_trajeto("baia", "aterro")["minutos"], im_trajeto("baia", "aterro")["meio"]) == (15, "calcada")
        $ im_iniciar(2)
        assert eval [(o["acao"], o["minutos"]) for o in im_opcoes(2) if o["poi"] == "aterro"] == [("descansar", 75)]
        # Na semana 1 o parque fica fora; a subestação segue fechada.
        $ im_iniciar(1)
        assert eval not any(o["poi"] == "aterro" for o in im_opcoes(1, todas=True))
        assert eval im_mapa_estado(1)["lugares"]["aterro"]["estado_lugar"] == "fechado"
        assert eval im_mapa_estado(1)["lugares"]["subestacao"]["estado_lugar"] == "fechado"

    # Tela e sons por trajeto (§4.3).
    testcase transicoes_e_sons:
        $ chosen_job = "saude"
        $ im_iniciar(2)
        assert eval rw_desl("cafe") == (None, 0, None, None, 1.0, MAPA_SOM_CAFE)
        assert eval im_deslocamento_info({"poi": "cafe"})["tela"] is False
        assert eval rw_desl("ambulatorio") == ("campus", 10, "images/bg/transicao_campus.png", "audio/effects/steps.ogg", 1.0, MAPA_SOM_PORTA)
        assert eval rw_desl("praca")[5] is None
        $ chosen_job = "startup"
        $ im_iniciar(6)
        assert eval rw_desl("cafe") == ("escada", 0, "images/bg/transicao_escada.png", "audio/effects/passos.ogg", 1.0, MAPA_SOM_CAFE)
        assert eval rw_desl("terraco") == ("escada", 0, "images/bg/transicao_escada.png", "audio/effects/passos.ogg", 1.0, None)
        assert eval rw_desl("ponto")[:3] == ("calcada", 10, "images/bg/transicao_calcada.png")
        assert eval rw_desl("aceleradora") == ("metro", 25, "images/bg/transicao_metro.png", "audio/effects/bus.ogg", 0.6, MAPA_SOM_PORTA)
        assert eval rw_desl("bandejao")[:4] == ("onibus", 30, "images/bg/transicao_onibus.png", "audio/effects/bus.ogg")
        assert eval [d for lim, d in MAPA_TEMPO_TRANSICAO] == [1.0, 1.5, 1.8, 2.0]
        assert eval im_deslocamento_info({"poi": "bandejao"})["duracao"] == 2.0 and im_deslocamento_info({"poi": "aceleradora"})["duracao"] == 1.8
        assert eval im_deslocamento_info({"poi": "bandejao"})["texto"] == "Ônibus · Casarão amarelo (Trocado) → Bandejão da universidade · 30 min"
        $ chosen_job = "corporativo"
        $ im_iniciar(2)
        assert eval rw_desl("cafe") == ("elevador", 0, "images/bg/transicao_elevador.png", "audio/effects/ambiente_reuniao.ogg", 1.0, MAPA_SOM_CAFE)
        assert eval rw_desl("aterro") == ("calcada", 15, "images/bg/transicao_calcada.png", "audio/effects/passos.ogg", 1.0, None)

    # Ir para casa: mesma tela do meio, sem cobrar minutos; porta no fim.
    testcase volta_para_casa:
        $ chosen_job = "startup"
        $ im_iniciar(2)
        $ rw_antes = im_deslocamento_casa_info()
        assert eval (rw_antes["de"], rw_antes["para"], rw_antes["meio"], rw_antes["minutos"], rw_antes["relogio"]) == ("casarao", "republica", "onibus", 0, False)
        assert eval rw_antes["texto"] == "Ônibus · Casarão amarelo (Trocado) → República das Amendoeiras · 15 min"
        assert eval rw_antes["som_chegada"] == MAPA_SOM_PORTA and rw_antes["hora_fim"] == rw_antes["hora_ini"]
        $ chosen_job = "corporativo"
        $ im_iniciar(2)
        assert eval im_deslocamento_casa_info()["meio"] == "metro"
        assert eval "sem gastar tempo livre" in im_mapa_estado(2)["lugares"]["republica"]["trajeto"]
        $ im_local = ""
        assert eval im_deslocamento_casa_info() is None

    # Linha "No caminho" do fechamento.
    testcase resumo_no_caminho:
        $ chosen_job = "saude"
        $ set_time(9, 0)
        $ im_iniciar(2)
        $ im_pagar_deslocamento({"poi": "ambulatorio"}, im_deslocamento_info({"poi": "ambulatorio"}))
        assert eval im_local == "ambulatorio" and im_minutos == 200 and (game_hour, game_minute) == (16, 10)
        assert eval im_resumo_caminho(im_resumo_dados(2)) == "No caminho: 10 min (1 trajeto)"
        $ im_pagar_deslocamento({"poi": "mesa"}, im_deslocamento_info({"poi": "mesa"}))
        assert eval im_resumo_caminho(im_resumo_dados(2)) == "No caminho: 20 min (2 trajetos)"

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
        # A abertura da semana (conteúdo da E5) pode ter falas antes do mapa.
        advance until screen "im_mapa"
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
        # Encerrar = ir para casa: cartão do trajeto, sem gastar tempo livre.
        click id "im_encerrar"
        pause until screen "im_transicao" timeout 5
        assert eval IM_DIAG.telas[-1] == "cartao" and (game_hour, game_minute) == (17, 0)
        click pos (960, 540)
        pause until screen "im_resumo" timeout 5
        assert eval (game_hour, game_minute) == (17, 0)
        click id "im_resumo_continuar"
        pause until eval im_semana_atual == 0
        assert eval im_feitas["startup"][2]["encerrou_cedo"] and im_feitas["startup"][2]["trajetos"] == 2
        assert eval im_feitas["startup"][2]["trajeto_min"] == 60 and im_feitas["startup"][2]["minutos_usados"] == 120
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
        # A volta para casa (marcador + metrô) fecha sozinha em ~3 s.
        click id "im_encerrar"
        pause until screen "im_resumo" timeout 10
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
