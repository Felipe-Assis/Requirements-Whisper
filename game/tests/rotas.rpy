# Despacho por rota em label start, contrato de ROUTES e set_available.
testsuite rotas:
    before testcase:
        if not screen "main_menu":
            run MainMenu(confirm=False)
        pause until screen "main_menu"
        run Start()
        pause until screen "say"

    # Pula scene_1_quarto: tira o frame da chamada e salta para o ponto de
    # retorno (_scene_1_quarto), onde label start escolhe a cadeia da rota.
    # A chegada é conferida pelo ponto de retorno (from) na pilha de chamadas.
    testcase despacho_saude:
        $ chosen_job = "saude"
        $ renpy.pop_call()
        run Jump("_scene_1_quarto")
        advance until eval "_scene_3_reuniao_inicial" in renpy.get_return_stack()

    testcase despacho_startup:
        $ chosen_job = "startup"
        $ renpy.pop_call()
        run Jump("_scene_1_quarto")
        advance until eval "_st_01_chegada" in renpy.get_return_stack()

    testcase despacho_corporativo:
        $ chosen_job = "corporativo"
        $ renpy.pop_call()
        run Jump("_scene_1_quarto")
        advance until eval "_co_01_chegada" in renpy.get_return_stack()

    testcase contrato_das_rotas:
        parameter rota = ["saude", "startup", "corporativo"]
        assert eval len(route_records(rota)) == 8
        assert eval len(set(r["id"] for r in route_records(rota))) == 8
        assert eval all(r["title"] and r["text"] for r in route_records(rota))
        assert eval len(route_achievements(rota)) > 0
        assert eval all(("var" in a) != ("inv" in a) for a in route_achievements(rota))
        assert eval all(hasattr(store, a["var"]) for a in route_achievements(rota) if "var" in a)
        assert eval route_final_grade(rota) in ("excelente", "bom", "ok")

    testcase final_saude_segue_scene_21:
        $ chosen_job = "saude"
        assert eval route_final_grade() == "ok"
        python:
            for cid in DEVELOPERS:
                setattr(store, "amizade_" + cid, 5.0)
        assert eval route_final_grade() == "bom"
        $ inventario.extend(["selo_codigo_sem_bugs", "conquista_bug_vuln"])
        assert eval route_final_grade() == "excelente"

    testcase set_available_por_rota:
        $ chosen_job = "saude"
        $ disponivel_doutora_1 = True
        $ set_available("developer_ai")
        assert eval disponivel_developer_ai and not disponivel_developer_coding
        assert eval disponivel_doutora_1 and not disponivel_st_mentora
        $ chosen_job = "startup"
        $ set_available("st_mentora", "st_ceo")
        assert eval disponivel_st_mentora and disponivel_st_ceo and not disponivel_st_techlead
        assert eval disponivel_developer_ai
        $ chosen_job = "corporativo"
        $ set_available("all")
        assert eval all(getattr(store, "disponivel_" + c) for c in route_contact_ids("corporativo"))
        assert eval disponivel_st_mentora and disponivel_co_mentora
