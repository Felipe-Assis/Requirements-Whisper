# Capturas para inspeção visual das telas e das cenas das rotas. Desligada
# por padrão: só roda quando chamada pelo nome, e as imagens vão para fora do
# repositório (RW_INSPECAO_DIR; subpasta RW_INSPECAO_FASE, ex.: antes/depois).
#   $env:RW_INSPECAO_FASE = "depois"
#   & "<sdk>\lib\py3-windows-x86_64\python.exe" "<sdk>\renpy.py" "<projeto>" test inspecao --savedir "<projeto>/.test-saves" --overwrite-screenshots

init python in rw_insp:
    import os

    def cap(nome, maior=False):
        pasta = os.environ.get("RW_INSPECAO_DIR", "X:/dev-tmp/requirements-whisper/integracao-rotas/capturas")
        fase = os.environ.get("RW_INSPECAO_FASE", "atual")
        return "%s/%s/%s%s.png" % (pasta, fase, nome, "_maior" if maior else "")

    TEXTO_LONGO_REQ = ("A estudante cadastrada pode corrigir o valor de um gasto já lançado no mês atual, "
        "desde que o novo valor seja maior que zero e que o gasto não tenha sido exportado para o relatório "
        "mensal; se o aparelho estiver sem sinal, a correção fica guardada e é enviada quando a conexão voltar, "
        "sem duplicar o lançamento nem perder a categoria escolhida.")
    TEXTO_LONGO_CRIT = ("Dado um gasto de R$ 20 em Alimentação no mês atual, quando a estudante muda o valor "
        "para R$ 15 e confirma, então a lista mostra R$ 15, o total do mês diminui R$ 5 e o histórico guarda o "
        "valor anterior; se ela digitar zero ou um valor negativo, o app recusa e explica por quê, sem salvar.")


label rw_insp_escrita(eid):
    call exercicio_escrita(eid, ST_ESCRITA_PEDIDO)
    "Fim da inspeção de escrita."
    return

label rw_insp_plano:
    call atividade_planejamento("rw_insp_plano", ST_PLANO_ITENS, ST_PLANO_NECESSARIOS, 2)
    "Fim da inspeção de planejamento."
    return


testsuite inspecao:
    enabled False

    before testcase:
        python hide:
            import renpy.test.testsettings as ts
            renpy._rw_insp_prefs = (persistent.texto_maior, _preferences.text_cps, _preferences.transitions)
            # Capturas são lentas e o laço do planejamento volta à mesma
            # linha do script: o limite padrão (5 s na mesma linha) é curto.
            # Não volta ao padrão no after: a suíte só roda sozinha.
            ts._test.timeout = 60
            _preferences.text_cps = 0
            _preferences.transitions = 0
        if not screen "main_menu":
            run MainMenu(confirm=False)
        pause until screen "main_menu"
        run Start()
        pause until screen "say"
        $ player_name = "Ana"
        $ player_gender = "Feminino"

    after testcase:
        python hide:
            persistent.texto_maior, _preferences.text_cps, _preferences.transitions = renpy._rw_insp_prefs
            del renpy._rw_insp_prefs

    testcase notebook:
        parameter maior = [False, True]
        $ persistent.texto_maior = maior
        $ chosen_job = "startup"
        run Show("notebook_registros")
        pause until screen "notebook_registros"
        pause 0.3
        screenshot rw_insp.cap("notebook_0", maior)
        $ [registrar(r["id"]) for r in route_records()[:4]]
        pause 0.3
        screenshot rw_insp.cap("notebook_4", maior)
        $ [registrar(r["id"]) for r in route_records()]
        pause 0.3
        screenshot rw_insp.cap("notebook_8", maior)
        keysym "K_PAGEDOWN"
        pause 0.3
        screenshot rw_insp.cap("notebook_8_rolado", maior)

    testcase escrita:
        parameter maior = [False, True]
        $ persistent.texto_maior = maior
        $ chosen_job = "startup"
        run Call("rw_insp_escrita", "rw_insp_vazio")
        advance until screen "escrita_input"
        pause 0.3
        screenshot rw_insp.cap("escrita_campo1_vazio", maior)
        type "A estudante pode corrigir o valor de um gasto."
        keysym "K_RETURN"
        pause until eval escrita_atual.get("req")
        pause 0.3
        screenshot rw_insp.cap("escrita_campo2_vazio", maior)
        keysym "K_RETURN"
        pause until screen "escrita_revisao"
        pause 0.3
        screenshot rw_insp.cap("escrita_revisao_curta", maior)
        click id "escrita_pendente"
        advance until "Fim da inspeção"
        $ escritas["rw_insp_longo"] = {"req": rw_insp.TEXTO_LONGO_REQ, "crit": rw_insp.TEXTO_LONGO_CRIT, "checks": 0, "status": "pendente"}
        run Call("rw_insp_escrita", "rw_insp_longo")
        advance until screen "escrita_input"
        pause 0.3
        screenshot rw_insp.cap("escrita_campo1_longo", maior)
        keysym "K_RETURN"
        pause until eval renpy.get_widget("escrita_input", "input") is not None and renpy.get_widget("escrita_input", "input").content.startswith("Dado")
        pause 0.3
        screenshot rw_insp.cap("escrita_campo2_longo", maior)
        keysym "K_RETURN"
        pause until screen "escrita_revisao"
        click id "escrita_marca_0"
        click id "escrita_marca_1"
        pause 0.3
        screenshot rw_insp.cap("escrita_revisao_longa", maior)
        keysym "K_DOWN"
        pause 0.3
        screenshot rw_insp.cap("escrita_revisao_foco", maior)

    testcase planejamento:
        parameter maior = [False, True]
        $ persistent.texto_maior = maior
        $ chosen_job = "startup"
        run Jump("rw_insp_plano")
        advance until screen "choice"
        pause 0.3
        screenshot rw_insp.cap("plano_inicio", maior)
        click "Adicionar: Medalhas"
        pause until "Retirar: Medalhas"
        click "Adicionar: Confirmar"
        pause until "Conferir este plano"
        pause 0.3
        screenshot rw_insp.cap("plano_cheio", maior)
        click "Conferir este plano"
        pause until screen "say"
        pause 0.3
        screenshot rw_insp.cap("plano_resultado", maior)

    testcase resumo:
        parameter maior = [False, True]
        $ persistent.texto_maior = maior
        $ chosen_job = "startup"
        $ [registrar(r["id"]) for r in route_records()[:5]]
        $ [setattr(store, a["var"], True) for a in route_achievements()[:3]]
        $ decisao("rw_insp_d1", True)
        $ decisao("rw_insp_d2", False)
        $ escritas["rw_insp"] = {"req": "x", "crit": "y", "checks": 4, "status": "confirmado"}
        run Jump("scene_epilogo_conquistas_final")
        advance until screen "resumo_rota"
        pause 0.3
        screenshot rw_insp.cap("resumo", maior)
        keysym "K_PAGEDOWN"
        pause 0.3
        screenshot rw_insp.cap("resumo_rolado", maior)

    testcase preferencias:
        parameter maior = [False, True]
        $ persistent.texto_maior = maior
        run ShowMenu("preferences")
        pause until screen "preferences"
        pause 0.5
        screenshot rw_insp.cap("preferencias", maior)

    testcase mochila:
        parameter maior = [False, True]
        $ persistent.texto_maior = maior
        $ item_notebook = item_celular = item_bloco_de_notas = item_caneta = item_garrafinha = True
        run ShowMenu("inventory_screen")
        pause until screen "inventory_screen"
        pause 0.3
        screenshot rw_insp.cap("mochila", maior)
        keysym "K_RIGHT"
        pause 0.3
        screenshot rw_insp.cap("mochila_foco", maior)

    testcase contatos:
        parameter rota = ["startup", "corporativo"]
        $ chosen_job = rota
        python:
            for _c in route_contacts_order():
                setattr(store, "contato_" + _c, True)
            set_available(*route_contacts_order()[:3])
        run Show("contacts_screen")
        pause until screen "contacts_screen"
        pause 0.3
        screenshot rw_insp.cap("contatos_" + rota)
        keysym "K_RIGHT"
        pause 0.3
        screenshot rw_insp.cap("contatos_%s_foco" % rota)

    testcase chat:
        parameter maior = [False, True]
        $ persistent.texto_maior = maior
        $ chosen_job = "startup"
        $ amigo_selecionado = "st_mentora"
        run Jump("chat_amigo")
        advance until screen "chat_with_backend"
        type "Oi, tudo bem? Como foi seu dia hoje no escritorio?"
        keysym "K_RETURN"
        pause 0.3
        type "Queria entender melhor o que a Bia quis dizer com facil no app."
        keysym "K_RETURN"
        pause 0.3
        type "Valeu!"
        keysym "K_RETURN"
        pause 0.5
        screenshot rw_insp.cap("chat_offline", maior)

    # Composição das cenas: quadros antes do primeiro menu de cada cena.
    testcase cena_st_01:
        parameter maior = [False, True]
        $ persistent.texto_maior = maior
        $ chosen_job = "startup"
        run Jump("st_01_chegada")
        advance until "Perto da janela"
        pause 0.5
        screenshot rw_insp.cap("st_01_equipe", maior)
        advance until "Na tela da esquerda"
        pause 0.5
        screenshot rw_insp.cap("st_01_artefato_app", maior)
        advance until "Agora a parte menos bonita"
        pause 0.5
        screenshot rw_insp.cap("st_01_mobile_qualidade", maior)
        advance until "800 estudantes"
        pause 0.5
        screenshot rw_insp.cap("st_01_artefato_painel", maior)

    testcase cena_st_02:
        $ chosen_job = "startup"
        run Jump("st_02_reuniao_ciclo")
        advance until "Esse é o nosso quadro"
        pause 0.5
        screenshot rw_insp.cap("st_02_kanban")

    testcase cena_st_05:
        $ chosen_job = "startup"
        run Jump("st_05_entrevista")
        advance until "Fundo de investimento"
        pause 0.5
        screenshot rw_insp.cap("st_05_entrevista_tres")

    testcase cena_st_13:
        parameter maior = [False, True]
        $ persistent.texto_maior = maior
        $ chosen_job = "startup"
        run Jump("st_13_arquitetura")
        advance until "Eu vim de ouvinte"
        pause 0.5
        screenshot rw_insp.cap("st_13_tres", maior)
        advance until "Começa no celular"
        pause 0.5
        screenshot rw_insp.cap("st_13_diagrama", maior)

    testcase cena_co_01:
        $ chosen_job = "corporativo"
        run Jump("co_01_chegada")
        advance until "Desde 2008"
        pause 0.5
        screenshot rw_insp.cap("co_01_equipe")
        advance until "chamado 48213"
        pause 0.5
        screenshot rw_insp.cap("co_01_artefato_sgc")
        advance until "dezesseis anos"
        pause 0.5
        screenshot rw_insp.cap("co_01_tres")

    testcase cena_co_05:
        $ chosen_job = "corporativo"
        run Jump("co_05_entrevista")
        advance until "subestação"
        pause 0.5
        screenshot rw_insp.cap("co_05_entrevista_tres")

    testcase cena_co_17:
        $ chosen_job = "corporativo"
        run Jump("co_17_testes_seguranca")
        advance until "Plano de testes"
        pause 0.5
        screenshot rw_insp.cap("co_17_dupla")
        advance until "abre a tela da trilha"
        pause 0.5
        screenshot rw_insp.cap("co_17_artefato_auditoria")

    testcase cena_co_18:
        $ chosen_job = "corporativo"
        run Jump("co_18_implantacao_avaliacao")
        advance until "Backup sem restauração"
        pause 0.5
        screenshot rw_insp.cap("co_18_servidores")

    # Referência da saúde (artefato e dupla de sprites originais).
    testcase cena_saude_18:
        $ chosen_job = "saude"
        run Jump("scene_18_codificacao_implementacao")
        advance until "Vamos direto ao ponto"
        pause 0.5
        screenshot rw_insp.cap("saude_18_dupla")
        advance until "layout da tela de cadastro"
        pause 0.5
        screenshot rw_insp.cap("saude_18_artefato")
