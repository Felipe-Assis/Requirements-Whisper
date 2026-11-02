# estado_startup.rpy
# Estado da rota Startup (Trocado). Fonte: docs/rotas/startup.md.
#
# API para as cenas st_01..st_18:
# - Decisão pedagógica (seções 3 e 7 da bíblia): na opção escolhida chame
#   $ st_decidir("st_dXX_nome", True|False). Só a primeira tentativa conta:
#   seta a flag st_dXX_nome (se adequada), soma st_acertos e chama decisao().
#   A revisão orientada depois de um distrator não chama st_decidir de novo
#   (se chamar, é ignorada).
# - st_06: no fim, $ st_classif_acertos = st_contar("st_d06_funcional",
#   "st_d06_nao_funcional", "st_d06_ideia").
# - st_11: $ st_inspecao_acertos = st_contar("st_d11_ambiguo", "st_d11_ausente",
#   "st_d11_inconsistente"); escrita livre com
#   call exercicio_escrita(ST_ESCRITA_ID, ST_ESCRITA_PEDIDO) e depois
#   $ st_sincronizar_escrita(). A st_12 retoma com a mesma chamada.
# - st_03: $ st_viu_duplicado = True.
# - st_13: cada opção ruim faz $ st_acordo_ruins += 1; ao confirmar,
#   $ st_confirmar_acordo("base_primeiro" | "investigar_agora").
#   Textos dos acordos em ST_ACORDOS.
# - st_15: call atividade_planejamento("st_plano", ST_PLANO_ITENS,
#   ST_PLANO_NECESSARIOS, 2) e depois $ st_registrar_plano(_return).
# - st_16: $ st_escolher_abordagem("teste_pr" | "rapida" | "reescrever")
#   (também na revisão, com "teste_pr").
# - Conquistas: no fim de cada cena com conquista (05, 09, 11, 12, 13, 15, 16,
#   17), $ st_checar_conquistas(). Na st_18, depois do rollout e do menu
#   social, $ st_checar_conquistas(final=True) (avalia st_conq_equipe).
#   As regras ficam todas aqui.
# - Notebook: $ registrar("st_reg_mvp") etc. (ids em ROUTES["startup"]["records"]).
# - Final (st_18): st_amizade_equipe(), st_conquistas() e st_final_grade()
#   ("excelente" | "bom" | "ok"). São funções, não variáveis.
# - Epílogo: st_acertos de ST_ACERTOS_MAX, st_acordo_texto, st_escrita_concluida.

# Escolhas adequadas na primeira tentativa (máximo ST_ACERTOS_MAX).
default st_acertos = 0
# Ids já decididos por st_decidir (garante "só a primeira tentativa conta").
default st_decisoes = set()

default st_viu_duplicado = False

default st_d02_mvp = False
default st_d04_roteiro = False
default st_d05_episodio = False
default st_d05_ambiguidade = False
default st_d05_conflito = False
default st_d06_funcional = False
default st_d06_nao_funcional = False
default st_d06_ideia = False
default st_classif_acertos = 0
default st_d09_historia = False
default st_d09_criterio = False
default st_d09_limite = False
default st_d11_ambiguo = False
default st_d11_ausente = False
default st_d11_inconsistente = False
default st_inspecao_acertos = 0
default st_escrita_requisito = ""
default st_escrita_criterio = ""
default st_escrita_concluida = False
default st_d13_idempotencia = False
default st_d13_valor = False
default st_acordo_opcao = ""
default st_acordo_texto = ""
default st_acordo_ruins = 0
default st_acordo_confirmado = False
default st_plano_selecionados = []
default st_plano_cobertura = 0
default st_plano_primeira_cobertura = -1
default st_plano_completo = False
default st_d15_riscos = False
default st_d15_metrica = False
default st_abordagem = ""
default st_abordagem_primeira = ""
default st_d16_review = False
default st_d17_carga = False
default st_d17_token = False
default st_d17_exclusao = False
default st_d18_rollout = False

default st_conq_escuta = False
default st_conq_criterio = False
default st_conq_inspetor = False
default st_conq_rascunho = False
default st_conq_acordo = False
default st_conq_foco = False
default st_conq_revisor = False
default st_conq_guardiao = False
default st_conq_lancamento = False
default st_conq_equipe = False


# init 2: ROUTES é criado em init 1 (data/routes.rpy).
init 2 python:
    ST_ACERTOS_MAX = 24

    ROUTES["startup"]["records"] = [
        {
            "id": "st_reg_mvp",
            "title": _("MVP e ciclo curto"),
            "text": _("O ciclo de vida continua inteiro: descobrir, especificar, construir, testar, lançar, medir. Numa startup cada volta dura pouco. MVP é a menor versão que resolve um problema real e gera aprendizado com usuários; é pequeno no escopo, não na qualidade. Em app, cada versão passa pela revisão das lojas."),
        },
        {
            "id": "st_reg_elicitacao",
            "title": _("Da queixa ao requisito"),
            "text": _("Peça um episódio recente: quem, o que aconteceu, qual a consequência. Pergunta que oferece solução esconde o problema. Troque adjetivos (\"fácil\", \"moderno\") por tarefa e resultado observável. Em conflito, pergunte o resultado esperado por cada pessoa e procure o objetivo comum."),
        },
        {
            "id": "st_reg_tipos",
            "title": _("Tipos de requisito"),
            "text": _("Funcional: o que o sistema faz (testa executando). Não funcional: qualidade com medida, como \"até 2 s em 95% das vezes no 4G\". Restrição: regra externa, como LGPD, lojas e Open Finance. Ideia a validar: hipótese que ainda precisa de evidência."),
        },
        {
            "id": "st_reg_criterio",
            "title": _("História, critério e caso limite"),
            "text": _("História: \"Como (quem), quero (ação), para (benefício)\". Critério: dado (situação com valores), quando (ação), então (resultado verificável). Caso limite: o que muda fora do caminho principal, como cancelar a exclusão e manter o total em R$ 100."),
        },
        {
            "id": "st_reg_inspecao",
            "title": _("Inspeção de requisitos"),
            "text": _("Antes de codar, leia com um checklist: falta algo (ausente)? dá para entender de dois jeitos (ambíguo)? contradiz outra regra (inconsistente)? dá para testar? Corrigir no documento custa uma tarde; em produção, custa um lançamento."),
        },
        {
            "id": "st_reg_mudanca",
            "title": _("Mudança de escopo se negocia"),
            "text": _("Pedido novo no meio do caminho não se aceita nem se recusa no impulso. Explique o impacto no que já foi combinado, ofereça caminhos (base primeiro, ou investigar e renegociar a data) e registre o acordo com quem pediu."),
        },
        {
            "id": "st_reg_metricas",
            "title": _("Capacidade, riscos e métricas"),
            "text": _("Capacidade é finita: escolha o que atende a necessidade confirmada. Risco precisa de dono, gatilho e plano. Métrica de produto mostra se a vida de quem usa melhorou (retenção, total conferido); downloads e número de funcionalidades são métricas de vaidade."),
        },
        {
            "id": "st_reg_lgpd",
            "title": _("Dados financeiros: LGPD e Open Finance"),
            "text": _("Dado financeiro é dado pessoal de alto risco. Guarde só o necessário, com finalidade e prazo; apague quando a pessoa excluir a conta. Open Finance funciona por consentimento na instituição, com prazo e revogação; o app nunca pede senha do banco. Tokens ficam no cofre do sistema do celular."),
        },
    ]

    # "pedagogica" é extra ao contrato: só as pedagógicas contam no final.
    ROUTES["startup"]["achievements"] = [
        {"id": "st_conq_escuta", "var": "st_conq_escuta", "pedagogica": True,
         "title": _("Ouvido de produto"),
         "desc": _("Pediu um episódio concreto e esclareceu \"fácil\" antes do feedback.")},
        {"id": "st_conq_criterio", "var": "st_conq_criterio", "pedagogica": True,
         "title": _("Dado, quando, então"),
         "desc": _("Escolheu o critério e o caso limite antes do feedback.")},
        {"id": "st_conq_inspetor", "var": "st_conq_inspetor", "pedagogica": True,
         "title": _("Lupa de requisitos"),
         "desc": _("Achou pelo menos 2 dos 3 defeitos antes do feedback.")},
        {"id": "st_conq_rascunho", "var": "st_conq_rascunho", "pedagogica": True,
         "title": _("Primeiro rascunho"),
         "desc": _("Guardou a escrita livre como rascunho depois da autoavaliação.")},
        {"id": "st_conq_acordo", "var": "st_conq_acordo", "pedagogica": True,
         "title": _("Acordo possível"),
         "desc": _("Confirmou um acordo válido sem passar por opção ruim.")},
        {"id": "st_conq_foco", "var": "st_conq_foco", "pedagogica": True,
         "title": _("Foco no MVP"),
         "desc": _("O primeiro plano cobriu os 2 itens necessários e a métrica foi adequada antes do feedback.")},
        {"id": "st_conq_revisor", "var": "st_conq_revisor", "pedagogica": True,
         "title": _("Revisão que protege"),
         "desc": _("Começou pelos testes com PR pequeno e deixou um review adequado, antes do feedback.")},
        {"id": "st_conq_guardiao", "var": "st_conq_guardiao", "pedagogica": True,
         "title": _("Guardião dos dados"),
         "desc": _("Acertou o armazenamento do token e a exclusão de conta antes do feedback.")},
        {"id": "st_conq_lancamento", "var": "st_conq_lancamento", "pedagogica": False,
         "title": _("Lançamento gradual"),
         "desc": _("Liberou a 1.0 em etapas antes do feedback.")},
        {"id": "st_conq_equipe", "var": "st_conq_equipe", "pedagogica": False,
         "title": _("Time Trocado"),
         "desc": _("Amizade 5 ou mais com Tainá, Otávio, Davi e Lorena.")},
    ]

    ROUTES["startup"]["final"] = "st_final_grade"

    # Escrita livre (st_11, retomada na st_12).
    ST_ESCRITA_ID = "st_escrita_valor"
    ST_ESCRITA_PEDIDO = _("A estudante precisa corrigir o valor de um gasto. O novo valor deve ser maior que zero; ao confirmar, a lista e o total do mês devem refletir a alteração.")

    # Planejamento da st_15: 2 de 4 itens; ST_PLANO_NECESSARIOS são índices.
    ST_PLANO_ITENS = [
        _("Confirmar a exclusão e manter o gasto se a pessoa cancelar"),
        _("Atualizar a lista e recalcular o total após excluir ou sincronizar"),
        _("Medalhas por frequência de uso"),
        _("Compartilhar resumo de gastos nas redes sociais"),
    ]
    ST_PLANO_NECESSARIOS = [0, 1]

    # Acordos válidos da negociação da st_13.
    ST_ACORDOS = {
        "base_primeiro": _("Entregar na 1.0 a exclusão segura e a correção do duplicado. A importação vira investigação: no demo day, mostramos o protótipo do consentimento como próximo passo, sem dados reais e sem data prometida."),
        "investigar_agora": _("Otávio investiga a parceria por uma semana agora; a data da 1.0 é renegociada, preservando a exclusão segura, o caso limite e a correção do duplicado. Se não couber antes do semestre, a importação fica para depois."),
    }

    def st_decidir(did, adequada):
        """Registra a primeira tentativa da decisão did; devolve adequada."""
        if did in store.st_decisoes:
            return adequada
        store.st_decisoes.add(did)
        if adequada:
            if hasattr(store, did):
                setattr(store, did, True)
            store.st_acertos += 1
        decisao(did, adequada)
        return adequada

    def st_contar(*flags):
        """Quantas das flags (nomes de variáveis) estão True."""
        return sum(1 for f in flags if getattr(store, f, False))

    def st_escolher_abordagem(valor):
        """st_16: guarda a abordagem atual e a primeira escolha."""
        store.st_abordagem = valor
        if not store.st_abordagem_primeira:
            store.st_abordagem_primeira = valor
        st_decidir("st_d16_abordagem", valor == "teste_pr")

    def st_confirmar_acordo(opcao):
        """st_13: confirma um dos acordos de ST_ACORDOS."""
        store.st_acordo_opcao = opcao
        store.st_acordo_texto = ST_ACORDOS[opcao]
        store.st_acordo_confirmado = True
        # Registro de aprendizagem; não entra em st_acertos (bíblia, seção 7).
        decisao("st_d13_acordo", store.st_acordo_ruins == 0)

    def st_registrar_plano(cobertura):
        """st_15: guarda a cobertura do plano (a primeira fica registrada)."""
        store.st_plano_cobertura = cobertura
        if store.st_plano_primeira_cobertura < 0:
            store.st_plano_primeira_cobertura = cobertura
        store.st_plano_completo = True
        decisao("st_d15_plano", cobertura == len(ST_PLANO_NECESSARIOS))

    def st_sincronizar_escrita():
        """st_11/st_12: copia o exercício de escrita para as variáveis st_escrita_*."""
        e = store.escritas.get(ST_ESCRITA_ID)
        if not e:
            return
        store.st_escrita_requisito = e.get("req", "")
        store.st_escrita_criterio = e.get("crit", "")
        store.st_escrita_concluida = e.get("status") == "confirmado"

    def st_amizade_equipe():
        """Soma da amizade da equipe da Startup (0 a 40); stakeholders não entram."""
        return sum(get_friendship_point(cid) for cid in route_team("startup"))

    def st_conquistas():
        """Quantas conquistas pedagógicas da Startup foram obtidas (0 a 8)."""
        return sum(1 for a in ROUTES["startup"]["achievements"]
                   if a["pedagogica"] and getattr(store, a["var"]))

    def st_final_grade():
        """Resultado da rota: "excelente", "bom" ou "ok" (bíblia, seção 6)."""
        amizade = st_amizade_equipe()
        conquistas = st_conquistas()
        if amizade >= 20 and conquistas >= 5:
            return "excelente"
        if amizade >= 15 or conquistas >= 5:
            return "bom"
        return "ok"

    def st_checar_conquistas(final=False):
        """Libera as conquistas cujas condições já valem e avisa o jogador.
        st_conq_equipe só é avaliada com final=True (st_18)."""
        s = store
        regras = {
            "st_conq_escuta": s.st_d05_episodio and s.st_d05_ambiguidade,
            "st_conq_criterio": s.st_d09_criterio and s.st_d09_limite,
            "st_conq_inspetor": st_contar("st_d11_ambiguo", "st_d11_ausente", "st_d11_inconsistente") >= 2,
            "st_conq_rascunho": s.st_escrita_concluida,
            "st_conq_acordo": s.st_acordo_confirmado and s.st_acordo_ruins == 0,
            "st_conq_foco": s.st_plano_primeira_cobertura == 2 and s.st_d15_metrica,
            "st_conq_revisor": s.st_abordagem_primeira == "teste_pr" and s.st_d16_review,
            "st_conq_guardiao": s.st_d17_token and s.st_d17_exclusao,
            "st_conq_lancamento": s.st_d18_rollout,
            "st_conq_equipe": final and all(get_friendship_point(cid) >= 5 for cid in route_team("startup")),
        }
        for a in ROUTES["startup"]["achievements"]:
            if regras[a["var"]] and not getattr(s, a["var"]):
                setattr(s, a["var"], True)
                renpy.notify(__("Conquista: {titulo}").format(titulo=__(a["title"])))
