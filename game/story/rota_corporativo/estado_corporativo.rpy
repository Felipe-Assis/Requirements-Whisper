# estado_corporativo.rpy
# Estado da rota Corporativo (Grupo Vértice / Projeto Farol). Fonte: docs/rotas/corporativo.md.
#
# API para as cenas co_01..co_18:
# - Decisão pedagógica (bíblia §3 e §4), sempre dentro do bloco do menu:
#     opção adequada:  $ co_acerto("co_ok_<x>")   (co_ok_<x> = True, co_score += 1, decisao(..., True))
#     cada distrator:  $ co_erro("co_ok_<x>")     (decisao(..., False); não mexe em score nem amizade)
#     depois do menu:  if not co_ok_<x>: menu de revisão (sem ponto).
# - Registro do notebook: $ co_registrar("co_reg_<x>") na cena indicada (co_02, co_04, co_05,
#   co_06, co_09, co_11, co_13, co_17). Marca co_reg_<x> e chama registrar() da F2b.
# - Conquista: $ co_conceder("co_conq_<x>") no ponto da bíblia §6; só concede se a condição
#   valer (co_condicao_conquista) e avisa "Conquista: <título>". Chamadas repetidas não fazem nada.
# - Escrita livre (co_11): call exercicio_escrita("co_reabrir", pedido), depois
#   $ co_sincronizar_escrita() para preencher co_escrita_requisito/criterio/status.
# - Planejamento (co_15): call atividade_planejamento("co_plano", ...); depois
#   $ co_plano_cobertura = _return e $ co_plano_completo = True.
# - Negociação (co_13): co_negociacao_sem_atalho = True ao abrir; False numa opção ruim;
#   co_negociacao_opcao ("base_primeiro"/"investigar_agora"), co_negociacao_acordo (texto),
#   co_negociacao_completa = True ao confirmar.
# - Escolhas sociais: co_almoco_mesa (co_10), co_contribuicao_festa e co_homenagem_jorge (co_14),
#   co_senha_relato (co_17).
# - Final (co_18): $ co_calcular_final() preenche co_amizade_total, co_conq_total e
#   co_final_resultado. co_final_grade() é a função de ROUTES["corporativo"]["final"]; por isso o
#   resultado não usa o nome co_final_grade da bíblia (o nome já é da função).

# Decisões pedagógicas: acertos de primeira (0 a 21) e uma flag por decisão.
default co_score = 0
default co_ok_manutencao = False
default co_ok_fontes = False
default co_ok_episodio = False
default co_ok_ambiguidade = False
default co_ok_conflito = False
default co_ok_class_nf = False
default co_ok_class_restricao = False
default co_ok_criterio = False
default co_ok_caso_limite = False
default co_ok_insp_ausente = False
default co_ok_insp_ambiguo = False
default co_ok_insp_inconsistente = False
default co_ok_arquitetura = False
default co_ok_auditoria = False
default co_ok_cab = False
default co_ok_risco = False
default co_ok_abordagem = False
default co_ok_review = False
default co_ok_rbac = False
default co_ok_regressao = False
default co_ok_janela = False

# Registros do notebook descobertos.
default co_reg_manutencao = False
default co_reg_legado = False
default co_reg_elicitacao = False
default co_reg_classificacao = False
default co_reg_criterio = False
default co_reg_inspecao = False
default co_reg_transicao = False
default co_reg_verificacao = False

# Conquistas (as 8 primeiras são de aprendizagem; co_conq_memoria é social).
default co_conq_arqueologia = False
default co_conq_escuta = False
default co_conq_inspetor = False
default co_conq_acordo = False
default co_conq_transicao = False
default co_conq_rede = False
default co_conq_trilha = False
default co_conq_janela = False
default co_conq_memoria = False

# Negociação (co_13).
default co_negociacao_opcao = ""
default co_negociacao_acordo = ""
default co_negociacao_sem_atalho = False
default co_negociacao_completa = False

# Planejamento (co_15).
default co_plano_selecionados = []
default co_plano_cobertura = 0
default co_plano_completo = False

# Escrita livre (co_11).
default co_escrita_requisito = ""
default co_escrita_criterio = ""
default co_escrita_status = ""

# Escolhas sociais.
default co_almoco_mesa = ""
default co_contribuicao_festa = ""
default co_homenagem_jorge = ""
default co_senha_relato = ""

# Final (co_18).
default co_amizade_total = 0
default co_conq_total = 0
default co_final_resultado = ""


init 2 python:
    ROUTES["corporativo"]["records"] = [
        {
            "id": "co_reg_manutencao",
            "title": _("Manutenção e mudança controlada"),
            "text": _("Manutenção corretiva conserta defeito; adaptativa acompanha mudança de ambiente; evolutiva acrescenta ou melhora uma função; preventiva reduz risco futuro. O Farol é evolutiva. Em produção, toda mudança segue um caminho: RFC, avaliação do CAB, janela combinada, plano de volta e revisão depois da implantação. Incidente restaura o serviço; problema investiga a causa."),
        },
        {
            "id": "co_reg_legado",
            "title": _("Ler o legado antes de mudar"),
            "text": _("Documentação antiga mostra o que alguém planejou, não o que roda hoje. Cruze três fontes: dados reais, código (inclusive rotinas do banco) e quem usa. Quando duas fontes discordam, há uma pergunta para a entrevista. Achado: a rotina das 72 h resolve chamados de senha sem descrição."),
        },
        {
            "id": "co_reg_elicitacao",
            "title": _("Episódio, palavra vaga e conflito"),
            "text": _("Comece pedindo a última vez que o problema aconteceu. Troque \"fácil\" pelo que a pessoa precisa conseguir fazer. Em conflito entre stakeholders, pergunte o que cada um quer evitar e procure um dado que os dois aceitem: 18% das ligações da central eram cobrança de andamento."),
        },
        {
            "id": "co_reg_classificacao",
            "title": _("O que é o quê"),
            "text": _("Funcional: o que o sistema faz (consultar estado e solução). Não funcional: como ele deve se comportar, com número (3 s para 95% das consultas com 1.500 usuários no pico). Restrição: limite imposto à solução (não alterar tabelas do SGC sem CAB). Desejo: ideia sem necessidade confirmada (tema escuro com mascote). Cada tipo é verificado de um jeito."),
        },
        {
            "id": "co_reg_criterio",
            "title": _("História, critério e caso limite"),
            "text": _("Como solicitante, quero consultar o estado e a solução do meu chamado, para não precisar ligar para a central. Critério: dado um chamado Em atendimento, quando o suporte registra a solução e muda para Resolvido, a consulta mostra Resolvido e o texto registrado. Caso limite: descrição vazia mantém Em atendimento e orienta o preenchimento."),
        },
        {
            "id": "co_reg_inspecao",
            "title": _("Inspeção de requisitos"),
            "text": _("Procure o que falta (quem, quando, condição), o que tem duas leituras (\"rápida\") e o que briga com outra regra (bloqueio sem descrição x rotina das 72 h). Conflito se resolve com quem é dono da regra. Autoavaliação: quem age e sob qual condição; dados iniciais e resultado observável; o que não pode mudar ou deve ser recusado."),
        },
        {
            "id": "co_reg_transicao",
            "title": _("Trocar o motor com o avião voando"),
            "text": _("O Farol cresce ao lado do SGC, atrás de uma camada que traduz os dados, e assume uma função por vez. A trilha de auditoria é uma tabela só de inclusão: quem, perfil, quando, ação, valor anterior e novo. Pedido novo no meio do caminho: mostrar o impacto, combinar a prioridade e registrar o acordo."),
        },
        {
            "id": "co_reg_verificacao",
            "title": _("Regressão, perfis e trilha"),
            "text": _("Regressão confirma que o que já funcionava continua funcionando, inclusive o que o Farol só toca de leve. Perfil se testa pelo \"não\": cada um tenta o que não pode e recebe acesso negado, registrado na trilha. Botão escondido não é controle de acesso. Senha não fica em arquivo do repositório: vai para o cofre, é trocada e o caso é registrado sem procurar culpados."),
        },
    ]

    ROUTES["corporativo"]["achievements"] = [
        {"id": "co_conq_arqueologia", "var": "co_conq_arqueologia",
         "title": _("Arqueologia do Legado"),
         "desc": _("Entendeu o SGC antes de mudar e cruzou dados, código e pessoas de primeira.")},
        {"id": "co_conq_escuta", "var": "co_conq_escuta",
         "title": _("Escuta que Pergunta"),
         "desc": _("Acertou de primeira pelo menos 2 das 3 decisões da entrevista: episódio, palavra vaga e conflito.")},
        {"id": "co_conq_inspetor", "var": "co_conq_inspetor",
         "title": _("Inspeção em Dia"),
         "desc": _("Achou de primeira pelo menos 2 dos 3 defeitos da inspeção e guardou o rascunho do requisito de reabertura.")},
        {"id": "co_conq_acordo", "var": "co_conq_acordo",
         "title": _("Acordo Registrado"),
         "desc": _("Negociou o pedido do WhatsApp até um acordo sem escolher atalho.")},
        {"id": "co_conq_transicao", "var": "co_conq_transicao",
         "title": _("Troca com o Avião Voando"),
         "desc": _("Escolheu de primeira o estrangulamento e a trilha de auditoria só de inclusão.")},
        {"id": "co_conq_rede", "var": "co_conq_rede",
         "title": _("Rede de Regressão"),
         "desc": _("Começou pelos testes de caracterização e montou a regressão certa de primeira.")},
        {"id": "co_conq_trilha", "var": "co_conq_trilha",
         "title": _("Guardião da Trilha"),
         "desc": _("Achou o defeito real no pull request e testou os perfis pelo lado do não.")},
        {"id": "co_conq_janela", "var": "co_conq_janela",
         "title": _("Janela Cumprida"),
         "desc": _("Seguiu o critério de parada na janela de sábado, com a RFC ou o ensaio da carga bem preparados.")},
        {"id": "co_conq_memoria", "var": "co_conq_memoria",
         "title": _("Memória Viva"),
         "desc": _("Propôs o wiki \"Causos do SGC\" e o Jorge aceitou gravar a memória do sistema.")},
    ]

    ROUTES["corporativo"]["final"] = "co_final_grade"

    # Conquista social: fica fora da contagem do final.
    CO_CONQ_SOCIAL = "co_conq_memoria"

    def co_ok_contagem(*nomes):
        """Quantas das decisões co_ok_* informadas foram adequadas de primeira."""
        return sum(1 for n in nomes if getattr(store, n))

    def co_acerto(var):
        """Opção adequada de primeira: marca co_ok_*, soma co_score uma vez e registra a decisão."""
        if not getattr(store, var):
            setattr(store, var, True)
            store.co_score += 1
        decisao(var, True)

    def co_erro(var):
        """Distrator escolhido: registra que a decisão precisou de revisão orientada."""
        decisao(var, False)

    def co_registrar(rid):
        """Descobre o registro co_reg_* (flag da rota + notebook da F2b)."""
        setattr(store, rid, True)
        registrar(rid)

    def co_condicao_conquista(var):
        """Condição da bíblia (§6) para a conquista co_conq_*."""
        s = store
        if var == "co_conq_arqueologia":
            return s.co_ok_manutencao and s.co_ok_fontes
        if var == "co_conq_escuta":
            return co_ok_contagem("co_ok_episodio", "co_ok_ambiguidade", "co_ok_conflito") >= 2
        if var == "co_conq_inspetor":
            return (co_ok_contagem("co_ok_insp_ausente", "co_ok_insp_ambiguo", "co_ok_insp_inconsistente") >= 2
                    and s.co_escrita_status == "rascunho")
        if var == "co_conq_acordo":
            return s.co_negociacao_sem_atalho
        if var == "co_conq_transicao":
            return s.co_ok_arquitetura and s.co_ok_auditoria
        if var == "co_conq_rede":
            return s.co_ok_abordagem and s.co_ok_regressao
        if var == "co_conq_trilha":
            return s.co_ok_review and s.co_ok_rbac
        if var == "co_conq_janela":
            return s.co_ok_janela and (s.co_ok_cab or s.co_ok_risco)
        if var == "co_conq_memoria":
            # Chamar depois do +1 do menu da homenagem.
            return s.co_homenagem_jorge == "wiki" and get_friendship_point("co_legado") >= 5
        return False

    def co_conceder(var):
        """Concede a conquista se a condição valer e avisa; devolve True se ela está ganha."""
        if getattr(store, var):
            return True
        if not co_condicao_conquista(var):
            return False
        setattr(store, var, True)
        for a in ROUTES["corporativo"]["achievements"]:
            if a["var"] == var:
                renpy.notify(_("Conquista: {titulo}").format(titulo=__(a["title"])))
        return True

    def co_sincronizar_escrita(eid="co_reabrir"):
        """Copia escritas[eid] (F2b) para co_escrita_*; "confirmado" vira "rascunho", como na bíblia."""
        e = store.escritas.get(eid)
        if not e:
            store.co_escrita_status = "pendente"
            return
        store.co_escrita_requisito = e.get("req", "")
        store.co_escrita_criterio = e.get("crit", "")
        store.co_escrita_status = "rascunho" if e.get("status") == "confirmado" else "pendente"

    def co_amizade_equipe():
        """Soma das amizades da equipe da rota (0 a 40)."""
        return sum(get_friendship_point(cid) for cid in route_team("corporativo"))

    def co_conquistas():
        """Quantas das 8 conquistas de aprendizagem foram ganhas (sem a social)."""
        return sum(1 for a in ROUTES["corporativo"]["achievements"]
                   if a["var"] != CO_CONQ_SOCIAL and getattr(store, a["var"]))

    def co_final_grade():
        """Regra do final da bíblia: "excelente", "bom" ou "ok"."""
        amizade = co_amizade_equipe()
        conquistas = co_conquistas()
        if amizade >= 20 and conquistas >= 4:
            return "excelente"
        if amizade >= 15 or conquistas >= 5:
            return "bom"
        return "ok"

    def co_calcular_final():
        """Guarda co_amizade_total, co_conq_total e co_final_resultado (co_18) e devolve o final."""
        store.co_amizade_total = co_amizade_equipe()
        store.co_conq_total = co_conquistas()
        store.co_final_resultado = co_final_grade()
        return store.co_final_resultado
