# learning.rpy
# -------------------------------
# REGISTROS, DECISÕES, ESCRITAS E PLANEJAMENTOS (mecânicas trazidas da demo)
# -------------------------------
# Estado que o notebook, as atividades e o resumo do epílogo leem. Os dados
# de cada rota (records, achievements, final) ficam em ROUTES:
#   ROUTES[rota]["records"]      = [{"id", "title", "text"}, ...]  (8 por rota)
#   ROUTES[rota]["achievements"] = [{"id", "title", "desc", "var"}] ou
#                                  [{"id", "title", "desc", "inv"}] (saúde)
#   ROUTES[rota]["final"]        = nome de uma função que devolve
#                                  "excelente" / "bom" / "ok"
# A saúde define os seus em data/routes.rpy; Startup e Corporativo, em
# init 2 python nos próprios arquivos de estado.
# Telas: scripts/mechanics/notebook_screen.rpy. Labels exercicio_escrita e
# atividade_planejamento: scripts/mechanics/learning_activities.rpy.

# Ids de registros descobertos (de qualquer rota; a contagem filtra pela rota).
default registros = set()

# did -> True (escolha adequada na primeira tentativa, sem apoio) ou
# False (precisou de revisão orientada). Só a primeira tentativa conta.
default aprendizagem = {}

# eid -> {"req", "crit", "checks": 0-4, "status": "confirmado"|"pendente"}.
# req e crit ficam guardados com { e [ escapados (ver escapar_texto).
default escritas = {}

# pid -> {"selecionados": [índices], "cobertura": int, "total": int,
#         "primeira_cobertura": int}
default planejamentos = {}


init python:

    def route_records(route=None):
        """
        Lista de registros da rota (dicts com "id", "title", "text").
        Lista vazia se a rota ainda não definiu os seus.
        """
        return list(route_data(route).get("records", []))

    def _record_by_id(rid, route=None):
        for rec in route_records(route):
            if rec["id"] == rid:
                return rec
        return None

    def registrar(rid):
        """
        Marca o registro `rid` da rota atual como descoberto e avisa:
        "Anotado no notebook: <título>". Ids repetidos são ignorados em
        silêncio. Ids que não existem na rota atual não são gravados (o erro
        vai para o log). Devolve True se o registro foi gravado agora.
        Exemplo: $ registrar("saude_reg_ciclo")
        """
        if rid in store.registros:
            return False
        rec = _record_by_id(rid)
        if rec is None:
            renpy.log("registrar: id desconhecido na rota %s: %s" % (current_route(), rid))
            return False
        store.registros.add(rid)
        renpy.notify(__("Anotado no notebook: {titulo}").format(titulo=__(rec["title"])))
        return True

    def registro_descoberto(rid):
        """True se o registro `rid` já foi descoberto."""
        return rid in store.registros

    def registros_rota(route=None):
        """Lista de (registro, descoberto) da rota, na ordem definida."""
        return [(rec, rec["id"] in store.registros) for rec in route_records(route)]

    def registros_contagem(route=None):
        """(descobertos, total) da rota."""
        dados = registros_rota(route)
        return (sum(1 for rec, ok in dados if ok), len(dados))

    def route_achievements(route=None):
        """Lista de conquistas da rota (vazia se a rota não definiu)."""
        return list(route_data(route).get("achievements", []))

    def achievement_unlocked(a):
        """
        True se a conquista `a` foi obtida: lê a variável booleana do store
        ("var") ou procura o item na lista inventario ("inv", rota saúde).
        """
        if "var" in a:
            return bool(getattr(store, a["var"], False))
        if "inv" in a:
            return a["inv"] in store.inventario
        return False

    def route_final_grade(route=None):
        """
        "excelente" / "bom" / "ok" segundo a função indicada em
        ROUTES[rota]["final"]; None se a rota ainda não definiu.
        """
        nome = route_data(route).get("final")
        if not nome:
            return None
        return getattr(store, nome)()

    def decisao(did, adequada):
        """
        Registra a PRIMEIRA tentativa da decisão `did`: True = escolha
        adequada sem apoio; False = precisou de revisão orientada. Chamadas
        seguintes com o mesmo did não sobrescrevem. Devolve True se gravou.
        Exemplo: $ decisao("st_entrevista_abertura", False)
        """
        if did in store.aprendizagem:
            return False
        store.aprendizagem[did] = bool(adequada)
        return True

    def resumo_decisoes():
        """(adequadas sem apoio, com apoio) entre as decisões registradas."""
        valores = list(store.aprendizagem.values())
        adequadas = sum(1 for v in valores if v)
        return (adequadas, len(valores) - adequadas)

    def resumo_escritas():
        """(confirmadas, pendentes) entre os exercícios de escrita."""
        status = [e.get("status") for e in store.escritas.values()]
        confirmadas = status.count("confirmado")
        return (confirmadas, len(status) - confirmadas)

    def escapar_texto(texto):
        """
        Prepara texto livre do jogador para exibição: tira espaços das pontas
        e dobra { e [ para que não virem tags nem interpolação do Ren'Py.
        """
        return (texto or "").strip().replace("{", "{{").replace("[", "[[")

    def desescapar_texto(texto):
        """Inverso de escapar_texto, para devolver o rascunho a um input."""
        return (texto or "").replace("{{", "{").replace("[[", "[")
