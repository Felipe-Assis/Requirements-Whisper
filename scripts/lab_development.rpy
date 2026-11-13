default lab_dev_order = ["save", "validate", "rules"]
default lab_dev_selected = None
default lab_dev_revision = 0
default lab_dev_results = {}
default lab_dev_case = ""
default lab_dev_mode = ""
default lab_dev_feedback = ""

init python:
    LAB_DEV_STEPS = {"validate": "Validar horários", "rules": "Conferir regras do plano", "save": "Gravar reserva"}
    LAB_DEV_CASE_TITLES = {"invalid": "Fim antes do início · 15h30–15h", "overlap": "Sobreposição · 14h30–15h30", "preparation": "Cinco minutos de preparo · 15h05", "other": "Outro equipamento · centrífuga", "adjacent": "Limite adicional · começa às 15h"}

    def lab_dev_reset():
        store.lab_dev_order = ["save", "validate", "rules"]
        store.lab_dev_selected = None
        store.lab_dev_revision = store.lab_revision
        store.lab_dev_results = {}
        store.lab_dev_case = ""
        store.lab_dev_mode = ""
        store.lab_dev_feedback = "Teste a sequência atual antes de reorganizar. O ensaio usa uma cópia, sem alterar a agenda real."

    def lab_dev_execute(order, case_id, rules):
        if case_id == "invalid":
            existing, candidate = ("microscopio", 840, 900), ("microscopio", 930, 900)
        else:
            case = LAB_CASES[case_id]
            existing, candidate = tuple(case["existing"]), tuple(case["candidate"])
        reservations = [existing]
        result = "allowed"
        trace = []
        for step in order:
            if result != "allowed":
                trace.append(LAB_DEV_STEPS[step] + ": não executado após a recusa.")
            elif step == "validate":
                result = lab_reservation_result(existing, candidate, [])
                trace.append("Validar horários: " + ("formato válido." if result == "allowed" else "fim anterior ao início; tentativa recusada."))
            elif step == "rules":
                # Regras do plano não substituem a etapa de validar a entrada.
                if lab_reservation_result(existing, candidate, []) != "invalid":
                    result = lab_reservation_result(existing, candidate, rules)
                trace.append("Conferir regras do plano: " + {"allowed": "nenhuma regra deste plano recusa a tentativa.", "conflict": "sobreposição recusada.", "preparation_required": "preparo insuficiente; tentativa recusada."}[result])
            elif step == "save":
                reservations = reservations + [candidate]
                trace.append("Gravar reserva: a tentativa entrou na cópia da agenda.")
        expected = lab_reservation_result(existing, candidate, rules)
        dirty = expected != "allowed" and candidate in reservations
        return {"result": result, "expected": expected, "dirty": dirty, "reservations": reservations, "trace": trace, "order": list(order), "rules": list(rules)}

    def lab_dev_select(step):
        if step not in LAB_DEV_STEPS:
            return False
        store.lab_dev_selected = step
        store.lab_dev_feedback = LAB_DEV_STEPS[step] + " selecionado. Escolha a posição; os dois passos trocam de lugar."
        return True

    def lab_dev_place(position):
        if type(position) is not int or position not in range(3) or store.lab_dev_selected not in LAB_DEV_STEPS:
            return False
        order = list(store.lab_dev_order)
        origin = order.index(store.lab_dev_selected)
        if origin != position:
            order[origin], order[position] = order[position], order[origin]
            store.lab_dev_order = order
            store.lab_dev_results = {}
            store.lab_dev_case = ""
            store.lab_dev_feedback = "Sequência alterada. Repita os quatro casos: resultados da versão anterior não verificam esta mudança."
        return True

    def lab_dev_run(case_id):
        if case_id not in LAB_DEV_CASE_TITLES:
            return False
        report = lab_dev_execute(store.lab_dev_order, case_id, store.lab_plan)
        results = dict(store.lab_dev_results)
        results[case_id] = report
        store.lab_dev_results = results
        store.lab_dev_case = case_id
        if report["dirty"]:
            store.lab_dev_feedback = "Mutação indevida: a tentativa foi recusada, mas já tinha sido gravada. Mova a gravação para depois das conferências e teste de novo."
        elif report["result"] == "allowed" and case_id in ("overlap", "preparation", "adjacent"):
            store.lab_dev_feedback = "Aceito pelo plano atual. A sequência está em teste; ela não acrescenta a proteção que ficou fora do pacote."
        else:
            store.lab_dev_feedback = "Ensaio registrado. A reserva de Ana ficou intacta; confira a tentativa e a ordem dos passos no rastro."
        return True

    def lab_dev_review(mode):
        if mode not in ("solo", "pair"):
            return False
        store.lab_dev_mode = mode
        if mode == "pair":
            lab_dev_run("adjacent")
            if "preparation" in store.lab_plan:
                detail = "Às 15h a reserva anterior acabou, mas o microscópio ainda precisa dos dez minutos. O teste deve recusar antes de gravar."
            else:
                detail = "Às 15h não há sobreposição. Sem preparo no plano, este caso é aceito; a necessidade da técnica continua pendente."
            store.lab_dev_feedback = "Júlio trouxe um caso adicional: " + detail
        else:
            store.lab_dev_feedback = "Revisão individual: compare o rastro da tentativa inválida, da sobreposição, do preparo e do outro equipamento. Você pode chamar Júlio depois."
        return True

    def lab_dev_ready():
        for case_id in ("invalid", "overlap", "preparation", "other"):
            report = store.lab_dev_results.get(case_id)
            if not report or report["order"] != store.lab_dev_order or report["rules"] != store.lab_plan or report["dirty"] or report["result"] != report["expected"]:
                return False
        return True

label lab_development(fresh=False):
    if fresh or lab_dev_revision != lab_revision:
        $ lab_dev_reset()
    hide screen lab_hud
    hide carlos
    hide julio
    "Na bancada de desenvolvimento, a confirmação está dividida em três passos. A ordem também faz parte do comportamento."
    call screen lab_development_bench
    $ lab_record_event("development_verified_" + str(lab_revision))
    show screen lab_hud
    if lab_phase == "followup":
        show julio retorno at colleague_right
    else:
        show julio neutral at colleague_right
    return

screen lab_development_bench():
    modal True
    zorder 40
    use campaign_workspace("Antes de gravar a reserva", "Desenvolvimento · revisão " + str(lab_revision) + " · execute, reorganize e repita os testes numa cópia."):
        viewport:
            id "lab_dev_cases_scroll"
            ysize 645
            mousewheel True draggable True arrowkeys True pagekeys True
            scrollbars "vertical"
            frame:
                style "artifact_paper" xsize 1730
                vbox:
                    spacing 20
                    use artifact_bar("Confirmação de reserva", "Processo / Revisão " + str(lab_revision) + " / Execução em cópia")
                    hbox:
                        spacing 28
                        vbox:
                            xsize 485 spacing 14
                            text "Processo · passos disponíveis" style "artifact_heading" size 31
                            for step in ("validate", "rules", "save"):
                                textbutton (LAB_DEV_STEPS[step] + (" · selecionado" if lab_dev_selected == step else "")):
                                    style "artifact_button" text_size lab_ui_size(25) xfill True
                                    selected lab_dev_selected == step
                                    action Function(lab_ui_apply, lab_dev_select, step)
                                    id ("lab_dev_select_" + step)
                            text "Sequência de execução" style "artifact_heading" size 31
                            for position, step in enumerate(lab_dev_order):
                                textbutton (str(position + 1) + ". " + LAB_DEV_STEPS[step]):
                                    style "artifact_button" text_size lab_ui_size(25) xfill True
                                    sensitive lab_dev_selected is not None
                                    action Function(lab_ui_apply, lab_dev_place, position)
                                    id ("lab_dev_place_" + str(position))
                            text "Uma recusa deve acontecer antes de gravar. Trocar a ordem invalida os testes anteriores." style "artifact_muted" size lab_ui_size(24)
                        vbox:
                            xsize 500 spacing 14
                            text "Executar testes" style "artifact_heading" size 31
                            for case_id in ("invalid", "overlap", "preparation", "other"):
                                textbutton (LAB_DEV_CASE_TITLES[case_id] + (" · registrado" if case_id in lab_dev_results else "")):
                                    style "artifact_button" text_size lab_ui_size(25) xfill True
                                    selected lab_dev_case == case_id
                                    action Function(lab_ui_apply, lab_dev_run, case_id)
                                    id ("lab_dev_test_" + case_id)
                            text "Como revisar?" style "artifact_heading" size 30
                            textbutton ("Revisar com Júlio" + (" · escolhido" if lab_dev_mode == "pair" else "")):
                                style "artifact_button" text_size lab_ui_size(25) xfill True
                                selected lab_dev_mode == "pair"
                                action Function(lab_ui_apply, lab_dev_review, "pair")
                                id "lab_dev_review_pair"
                            textbutton ("Revisar individualmente" + (" · escolhido" if lab_dev_mode == "solo" else "")):
                                style "artifact_button" text_size lab_ui_size(25) xfill True
                                selected lab_dev_mode == "solo"
                                action Function(lab_ui_apply, lab_dev_review, "solo")
                                id "lab_dev_review_solo"
                        vbox:
                            xsize 620 spacing 18
                            text "Relatório de execução" style "artifact_heading" size 31
                            text "Ana · microscópio · 14h–15h" style "artifact_ink" size lab_ui_size(26)
                            text ("Regras do pacote: " + ", ".join(LAB_ITEMS[item]["title"] for item in lab_plan)) style "artifact_muted" size lab_ui_size(24)
                            if "conflict" not in lab_plan:
                                text "Limitação: este pacote aceita sobreposição." color "#8a5623" size lab_ui_size(25)
                            if "preparation" not in lab_plan:
                                text "Limitação: este pacote não protege o preparo." color "#8a5623" size lab_ui_size(25)
                            if lab_dev_case:
                                $ report = lab_dev_results[lab_dev_case]
                                text LAB_DEV_CASE_TITLES[lab_dev_case] style "artifact_heading" size 30
                                for index, line in enumerate(report["trace"], 1):
                                    text (str(index).zfill(2) + "  " + line) style "artifact_ink" size lab_ui_size(25)
                                frame:
                                    style "artifact_card" xfill True
                                    vbox:
                                        spacing 12
                                        text lab_ui_result(report["result"]) style "artifact_heading" size 29
                                        text ("Mutação indevida · tentativa recusada permanece gravada" if report["dirty"] else "Cópia coerente com as regras do plano") color ("#8a5623" if report["dirty"] else "#286b66") size lab_ui_size(26) id "lab_dev_outcome"
                                        text "Reserva de Ana: mantida" style "artifact_ink" size lab_ui_size(25)
                                        text ("Tentativa na agenda: " + ("gravada" if len(report["reservations"]) > 1 else "não gravada")) style "artifact_ink" size lab_ui_size(25)
                            else:
                                text "Execute um caso. O rastro mostra quando a tentativa entrou na agenda e se uma recusa chegou tarde." style "artifact_muted" size lab_ui_size(27)
                            text ("Quatro casos conferidos para esta sequência." if lab_dev_ready() else "Antes da demonstração: confira os quatro casos sem gravação indevida e escolha como revisar.") style "artifact_muted" size lab_ui_size(24)
    use campaign_footer(lab_dev_feedback)
    use lab_continue("Demonstrar esta versão", Return(True), lab_dev_ready() and bool(lab_dev_mode), "lab_dev_continue")
