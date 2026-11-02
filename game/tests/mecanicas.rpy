# Caça à ambiguidade e rastreabilidade nas três rotas, tipos de menu,
# destaque de quem fala, respiração/câmera e as preferências novas.
# As cenas ainda não chamam as duas mecânicas: os labels abaixo chamam.

init python:
    def rw_focado(tela):
        # id do widget da tela com o foco agora, ou None.
        foco = renpy.display.focus.get_focused()
        scr = renpy.get_screen(tela)
        if foco is None or scr is None:
            return None
        for wid, w in scr.widgets.items():
            if w is foco:
                return wid
        return None

    def rw_seletor():
        # Seletor do quadro de rastreabilidade em foco: (critério, 0 ou 1) ou None.
        scr = renpy.get_screen("rast_quadro")
        return scr.scope.get("foco") if scr is not None else None

    def rw_termo_focado(tela):
        # Termo (id "amb_termo_<termo>") com o foco agora, ou None.
        wid = rw_focado(tela) or ""
        return wid[len("amb_termo_"):] if wid.startswith("amb_termo_") else None

label rw_amb_saude:
    call amb_atividade("saude_amb_historico")
    "Fim do teste de ambiguidade."
    return

label rw_amb_startup:
    call amb_atividade("st_amb_total")
    "Fim do teste de ambiguidade."
    return

label rw_amb_corporativo:
    call amb_atividade("co_amb_termo")
    "Fim do teste de ambiguidade."
    return

label rw_rast_saude:
    call rast_atividade("saude_rast_acesso")
    "Fim do teste de rastreabilidade."
    return

label rw_rast_startup:
    call rast_atividade("st_rast_exclusao")
    "Fim do teste de rastreabilidade."
    call rast_lembrar("st_rast_exclusao")
    "Fim do lembrete."
    call rast_lembrar("st_rast_exclusao")
    "Fim do segundo lembrete."
    return

label rw_rast_corporativo:
    call rast_atividade("co_rast_farol")
    "Fim do teste de rastreabilidade."
    call rast_lembrar("co_rast_farol")
    "Fim do lembrete."
    return

label rw_teste_menu_tipos:
    menu (tipo="trabalho"):
        "Opção de trabalho":
            pass
        "Opção de pista" (tipo="pista"):
            pass
    "Primeiro menu respondido."
    menu:
        "Opção sem tipo":
            pass
    "Fim do teste de menu."
    return

label rw_teste_fala:
    scene bg escritorio_interior_tarde
    show developer_ai positive at left_zoom
    show developer_test confident at right_zoom
    show expression "images/artifacts/cadastro_screen.png" as tela at artefato_tela
    developer_test "Fala de teste do César."
    hide tela
    "Fala do narrador."
    return

testsuite mecanicas:
    before testcase:
        python hide:
            renpy._rw_prefs_mec = (persistent.texto_maior, persistent.fala_destaque, persistent.vida_movimento)
        if not screen "main_menu":
            run MainMenu(confirm=False)
        pause until screen "main_menu"
        run Start()
        pause until screen "say"

    after testcase:
        python hide:
            persistent.texto_maior, persistent.fala_destaque, persistent.vida_movimento = renpy._rw_prefs_mec
            del renpy._rw_prefs_mec

    testcase dados_das_tres_rotas:
        assert eval sorted(a for r in ROUTES for a in ROUTES[r].get("ambiguidades", {})) == ["co_amb_termo", "saude_amb_historico", "st_amb_total"]
        assert eval sorted(q for r in ROUTES for q in ROUTES[r].get("rastreabilidade", {})) == ["co_rast_farol", "saude_rast_acesso", "st_rast_exclusao"]
        assert eval [e for r in ROUTES for a in ROUTES[r].get("ambiguidades", {}) for e in amb_validar(a)] == []
        assert eval [e for r in ROUTES for q in ROUTES[r].get("rastreabilidade", {}) for e in rast_validar(q)] == []
        # Ordem das reescritas: fixa por id, igual em toda partida.
        assert eval amb_ordem("st_amb_total", "rapido") == amb_ordem("st_amb_total", "rapido")

    # Saúde, pelo mouse: isca marcada, vaga faltando, revisão orientada e distrator.
    testcase ambiguidade_saude_revisao:
        run Jump("rw_amb_saude")
        pause until screen "amb_marcar"
        assert eval renpy.get_screen("amb_marcar").scope["fase"] == "marcar"
        click id "amb_termo_rapida"
        click id "amb_termo_historico"
        assert eval amb_atual["marcadas"] == ["rapida", "historico"]
        click id "amb_conferir"
        pause until eval amb_atual["conferencias"] == 1
        pause 0.2
        assert eval amb_atual["retorno"]["fase"] == "rever" and amb_atual["retorno"]["faltam"] == ["simples", "necessario"]
        assert eval aprendizagem["saude_amb_historico_marcar"] is False
        assert eval amb_resultados["saude_amb_historico"]["iscas_primeira"] == ["historico"]
        assert eval amb_resumo(amb_atual["retorno"]) == "Você achou 1 de 3 palavras vagas e marcou 1 termo que não é vago."
        # Desmarca a isca, marca mais uma vaga e confere de novo: a que falta é indicada.
        click id "amb_termo_historico"
        click id "amb_termo_simples"
        click id "amb_conferir"
        pause until eval renpy.get_screen("amb_marcar") is not None and renpy.get_screen("amb_marcar").scope["fase"] == "conferido"
        assert eval amb_resultados["saude_amb_historico"]["faltaram"] == ["necessario"]
        assert eval aprendizagem["saude_amb_historico_marcar"] is False
        click id "amb_continuar"
        pause until screen "choice"
        assert "TRABALHO"
        click "o mais rápido possível"
        advance until screen "choice"
        click "com a tela abrindo em até 2 s"
        advance until screen "choice"
        click "com os campos obrigatórios marcados"
        advance until screen "choice"
        click "para a profissional que acompanha o caso"
        pause until eval renpy.get_screen("amb_marcar") is not None and renpy.get_screen("amb_marcar").scope["fase"] == "resultado"
        assert eval "{b}[[com a tela abrindo em até 2 s" in amb_resultado("saude_amb_historico")
        click id "amb_continuar"
        advance until "Fim do teste de ambiguidade"
        assert eval aprendizagem["saude_amb_historico_rapida"] is False
        assert eval aprendizagem["saude_amb_historico_simples"] is True and aprendizagem["saude_amb_historico_necessario"] is True
        assert eval amb_resultados["saude_amb_historico"]["concluido"] and amb_resultados["saude_amb_historico"]["primeira_ok"] == {"rapida": False, "simples": True, "necessario": True}

    # Startup: teclado na marcação, tudo certo de primeira e retomada sem sobrescrever.
    testcase ambiguidade_startup_teclado_e_retomada:
        run Jump("rw_amb_startup")
        pause until screen "amb_marcar"
        pause 0.3
        # Teclado: a seta leva o foco a um termo; Enter marca e desmarca.
        keysym "K_RIGHT" until eval rw_termo_focado("amb_marcar") is not None timeout 3
        $ renpy._rw_termo = rw_termo_focado("amb_marcar")
        keysym "K_RETURN"
        pause until eval amb_atual["marcadas"] == [renpy._rw_termo]
        keysym "K_RETURN"
        pause until eval amb_atual["marcadas"] == []
        click id "amb_termo_rapido"
        click id "amb_termo_facil"
        click id "amb_termo_sem_perder"
        click id "amb_conferir"
        pause until eval renpy.get_screen("amb_marcar") is not None and renpy.get_screen("amb_marcar").scope["fase"] == "conferido"
        assert eval aprendizagem["st_amb_total_marcar"] is True and amb_resultados["st_amb_total"]["faltaram"] == []
        click id "amb_continuar"
        pause until screen "choice"
        click "em até 2 segundos depois de salvar"
        advance until screen "choice"
        click "a partir do próprio gasto na lista"
        advance until screen "choice"
        click "um gasto salvo sem internet fica guardado"
        pause until eval renpy.get_screen("amb_marcar") is not None and renpy.get_screen("amb_marcar").scope["fase"] == "resultado"
        click id "amb_continuar"
        advance until "Fim do teste de ambiguidade"
        assert eval all(aprendizagem["st_amb_total_" + t] for t in ("marcar", "rapido", "facil", "sem_perder"))
        # Retomada: errar tudo agora não muda a primeira tentativa.
        run Jump("rw_amb_startup")
        pause until screen "amb_marcar"
        assert eval amb_atual["marcadas"] == [] and amb_atual["conferencias"] == 0
        click id "amb_termo_gastos"
        click id "amb_conferir"
        pause until eval amb_atual["conferencias"] == 1
        click id "amb_termo_gastos"
        click id "amb_conferir"
        pause until eval amb_atual["conferencias"] == 2
        assert eval amb_atual["retorno"]["fase"] == "fechado"
        click id "amb_continuar"
        pause until screen "choice"
        click "instantaneamente"
        advance until screen "choice"
        click "em até 2 segundos depois de salvar"
        advance until screen "choice"
        click "de forma intuitiva"
        advance until screen "choice"
        click "a partir do próprio gasto na lista"
        advance until screen "choice"
        click "um gasto salvo sem internet fica guardado"
        pause until eval renpy.get_screen("amb_marcar") is not None and renpy.get_screen("amb_marcar").scope["fase"] == "resultado"
        click id "amb_continuar"
        advance until "Fim do teste de ambiguidade"
        assert eval all(aprendizagem["st_amb_total_" + t] for t in ("marcar", "rapido", "facil", "sem_perder"))
        assert eval amb_resultados["st_amb_total"]["marcadas_primeira"] == ["rapido", "facil", "sem_perder"]
        assert eval amb_resultados["st_amb_total"]["faltaram"] == []

    # Corporativo, como o autopiloto responde (valores de retorno da tela).
    testcase ambiguidade_corporativo_por_retorno:
        $ persistent.texto_maior = True
        run Jump("rw_amb_corporativo")
        pause until screen "amb_marcar"
        python hide:
            amb_atual["marcadas"][:] = ["rapida", "completas", "adequadamente", "chamado"]
            renpy.restart_interaction()
        pause 0.2
        click id "amb_conferir"
        pause until eval renpy.get_screen("amb_marcar") is not None and renpy.get_screen("amb_marcar").scope["fase"] == "conferido"
        assert eval aprendizagem["co_amb_termo_marcar"] is False and amb_resultados["co_amb_termo"]["iscas_primeira"] == ["chamado"]
        click id "amb_continuar"
        pause until screen "choice"
        click "responder em até 3 s"
        advance until screen "choice"
        click "mostrar o estado, o atendente"
        advance until screen "choice"
        click "em texto curto que diga o que foi feito"
        pause until eval renpy.get_screen("amb_marcar") is not None and renpy.get_screen("amb_marcar").scope["fase"] == "resultado"
        assert eval amb_resultado("co_amb_termo").startswith("A consulta deve {b}[[responder")
        click id "amb_continuar"
        advance until "Fim do teste de ambiguidade"
        assert eval [aprendizagem["co_amb_termo_" + t] for t in ("rapida", "completas", "adequadamente")] == [True, True, True]

    # Saúde, pelo mouse: armadilha C3 -> T4 (não ganha "confira"), requisito
    # errado no C5, correção e fechamento na segunda conferência sem revelar a lacuna.
    testcase rastreabilidade_saude_mouse:
        run Jump("rw_rast_saude")
        pause until screen "rast_quadro"
        assert eval renpy.get_screen("rast_quadro").scope["fase"] == "quadro" and not rast_completo()
        python hide:
            renpy._rw_resp = {"C1": ["R1", "T1"], "C2": ["R2", "T2"], "C3": ["R3", "T4"], "C4": ["R2", "T3"], "C5": ["R2", "T4"]}
        click id "rast_req_C1"
        pause until screen "rast_escolher"
        click id "rast_opcao_R1"
        pause until not screen "rast_escolher"
        click id "rast_teste_C1"
        pause until screen "rast_escolher"
        click id "rast_opcao_T1"
        pause until not screen "rast_escolher"
        assert eval rast_atual["ligacoes"]["C1"] == ["R1", "T1"]
        # Esc fecha a escolha sem mudar nada.
        click id "rast_teste_C2"
        pause until screen "rast_escolher"
        keysym "K_ESCAPE"
        pause until not screen "rast_escolher"
        assert eval rast_atual["ligacoes"]["C2"] == ["", ""]
        $ rast_atual["ligacoes"].update({k: list(v) for k, v in renpy._rw_resp.items() if k != "C1"})
        $ renpy.restart_interaction()
        pause 0.2
        click id "rast_conferir"
        pause until eval rast_atual["conferencias"] == 1
        pause 0.2
        assert eval sorted(rast_atual["confira"]) == ["C5"] and rast_atual["confira"]["C5"] == [True, False]
        assert eval "Todo critério tem teste?" in rast_atual["msgs"] and not rast_atual["fechado"]
        assert eval aprendizagem["saude_rast_acesso_ligacoes"] is False and aprendizagem["saude_rast_acesso_lacuna"] is False
        # C5 fica fora da área visível do quadro: corrige pelo estado.
        $ rast_atual["ligacoes"]["C5"][0] = "R3"
        $ renpy.restart_interaction()
        pause 0.2
        click id "rast_conferir"
        pause until eval renpy.get_screen("rast_quadro") is not None and renpy.get_screen("rast_quadro").scope["fase"] == "fechado"
        assert eval rast_atual["msgs"][-1] == "Quadro conferido." and "Todo critério tem teste?" not in rast_atual["msgs"]
        assert eval rast_cobertura("saude_rast_acesso") == ["R1: 1 critério, 1 teste", "R2: 2 critérios, 2 testes", "R3: 2 critérios, 1 teste"]
        click id "rast_continuar"
        advance until "Fim do teste de rastreabilidade"
        assert eval not rast_lacuna_achada("saude_rast_acesso") and rast_quadros["saude_rast_acesso"]["concluido"]
        assert eval rast_quadros["saude_rast_acesso"]["primeira"] == {"ligacoes_ok": False, "lacuna_ok": False}

    # Startup: setas trocam o valor do seletor em foco; tudo certo de primeira; rast_lembrar.
    testcase rastreabilidade_startup_lacuna_e_lembrete:
        run Jump("rw_rast_startup")
        pause until screen "rast_quadro"
        pause 0.3
        # Com o seletor em foco, direita e esquerda trocam o valor.
        keysym "K_UP" until eval rw_seletor() == ("C1", 0) timeout 5
        keysym "K_RIGHT"
        pause until eval rast_atual["ligacoes"]["C1"][0] == "R1"
        # Para baixo: o seletor de teste da mesma linha.
        keysym "K_DOWN"
        pause until eval rw_seletor() == ("C1", 1)
        keysym "K_LEFT"
        pause until eval rast_atual["ligacoes"]["C1"][1] is None
        keysym "K_UP"
        pause until eval rw_seletor() == ("C1", 0)
        keysym "K_RIGHT"
        pause until eval rast_atual["ligacoes"]["C1"][0] == "R2"
        keysym "K_LEFT"
        pause until eval rast_atual["ligacoes"]["C1"][0] == "R1"
        $ rast_atual["ligacoes"].update(rast_respostas("st_rast_exclusao"))
        $ renpy.restart_interaction()
        pause 0.2
        click id "rast_conferir"
        pause until eval renpy.get_screen("rast_quadro") is not None and renpy.get_screen("rast_quadro").scope["fase"] == "fechado"
        assert eval aprendizagem["st_rast_exclusao_ligacoes"] is True and aprendizagem["st_rast_exclusao_lacuna"] is True
        assert eval rast_cobertura("st_rast_exclusao") == ["R1: 2 critérios, 2 testes", "R2: 2 critérios, 1 teste", "R3: 1 critério, 1 teste"]
        click id "rast_continuar"
        advance until screen "choice"
        assert "PISTA"
        click "Lembrar: o critério sem teste"
        advance until "Fim do lembrete"
        assert eval rast_quadros["st_rast_exclusao"]["lembrado"] and rast_lacuna_achada("st_rast_exclusao")
        advance until "Fim do segundo lembrete"

    # Corporativo: ligações certas com um teste na lacuna (a isca T6). Não fecha
    # na primeira; fecha na segunda sem apontar a lacuna; rast_lembrar não aparece.
    testcase rastreabilidade_corporativo_sem_lacuna:
        $ persistent.texto_maior = True
        run Jump("rw_rast_corporativo")
        pause until screen "rast_quadro"
        $ renpy._rw_resp = rast_respostas("co_rast_farol", lacuna=False)
        $ renpy._rw_resp["C6"] = ["RF-06", "T6"]
        $ rast_atual["ligacoes"].update(renpy._rw_resp)
        $ renpy.restart_interaction()
        pause 0.2
        click id "rast_conferir"
        pause until eval rast_atual["conferencias"] == 1
        assert eval rast_atual["confira"] == {} and rast_atual["msgs"] == ["Todas as ligações de requisito e de teste conferem.", "Todo critério tem teste?"]
        assert eval not rast_atual["fechado"]
        $ rast_atual["ligacoes"].update(renpy._rw_resp)
        $ renpy.restart_interaction()
        pause 0.2
        click id "rast_conferir"
        pause until eval renpy.get_screen("rast_quadro") is not None and renpy.get_screen("rast_quadro").scope["fase"] == "fechado"
        assert eval aprendizagem["co_rast_farol_ligacoes"] is True and aprendizagem["co_rast_farol_lacuna"] is False
        click id "rast_continuar"
        advance until "Fim do lembrete"
        assert eval not rast_lacuna_achada("co_rast_farol")

    testcase menu_com_selos:
        run Jump("rw_teste_menu_tipos")
        advance until screen "choice"
        assert "TRABALHO"
        assert "PISTA"
        click "Opção de pista"
        advance until screen "choice"
        assert "Opção sem tipo"
        assert not "TRABALHO"
        $ persistent.texto_maior = True
        click "Opção sem tipo"
        advance until "Fim do teste de menu"

    testcase destaque_de_quem_fala:
        $ persistent.fala_destaque = True
        $ persistent.vida_movimento = True
        run Jump("rw_teste_fala")
        # Só durante a fala o Ren'Py aponta quem fala.
        pause until eval renpy.get_say_image_tag() == "developer_test"
        # Sprite de personagem: posição + foco + respiração; artefato e fundo passam direto.
        assert eval len(renpy.get_at_list("developer_ai")) == 3 and len(renpy.get_at_list("developer_test")) == 3
        assert eval len(renpy.get_at_list("tela")) == 1
        python hide:
            t = Transform()
            f = FalaFoco("developer_ai")
            f(t, 0.0, 0.0)
            assert f.n == 1.0 and t.matrixcolor is not None
            g = FalaFoco("developer_test")
            g(t, 0.0, 0.0)
            assert g.n == 0.0
            persistent.fala_destaque = False
            f(t, 0.05, 0.05)
            assert 0.0 < f.n < 1.0
            f(t, 1.0, 1.0)
            assert f.n == 0.0 and t.matrixcolor is None
            persistent.fala_destaque = True
        # O foco vai para o save junto com a lista de cenas: salvar e carregar.
        run FileSave("rw_fala", confirm=False)
        pause 0.3
        run FileLoad("rw_fala", confirm=False)
        pause until eval renpy.get_say_image_tag() == "developer_test"
        assert eval len(renpy.get_at_list("developer_ai")) == 3
        advance until "Fala do narrador"
        pause until eval not renpy.showing("tela")
        assert eval renpy.get_say_image_tag() is None
        python hide:
            f = FalaFoco("developer_ai")
            t = Transform()
            f(t, 0.0, 0.0)
            assert f.n == 0.0
        # Voltar (rollback) para a fala do César restaura quem fala e o artefato.
        run Rollback()
        pause until eval renpy.get_say_image_tag() == "developer_test"
        assert eval renpy.showing("tela")
        advance until "Fala do narrador"
        # Sem movimento: só posição + foco.
        $ persistent.vida_movimento = False
        $ config.show("developer_ai", at_list=[left_zoom])
        assert eval len(renpy.get_at_list("developer_ai")) == 2

    testcase camera_e_preferencias:
        $ persistent.vida_movimento = True
        $ cam_foco(0.3)
        assert eval cam_ativo
        $ cam_reset()
        assert eval not cam_ativo
        $ persistent.vida_movimento = False
        $ cam_foco(0.3)
        assert eval not cam_ativo
        $ cam_reset()
        run ShowMenu("preferences")
        pause until screen "preferences"
        pause until "Português"
        run SetField(persistent, "fala_destaque", True)
        click id "pref_fala_destaque"
        assert eval persistent.fala_destaque is False
        click id "pref_vida_movimento"
        assert eval persistent.vida_movimento is True
        keysym "K_ESCAPE"
        pause 0.2
        assert not screen "preferences"
