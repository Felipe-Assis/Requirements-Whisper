# friends_data.rpy
# -------------------------------
# DICIONÁRIO DE AMIGOS E ASSISTANT_IDS
# -------------------------------
# AMIGOS_DATA mapeia cada id de contato -> {name, portrait, assistant_id}.
# Fica em `init python` prio 0 porque referencia os defines NOME_* (também
# prio 0, em data/character_names.rpy) — NÃO usar `python early`.

init python:
    AMIGOS_DATA = {
        "developer_ai": {
            "name": NOME_DEVELOPER_AI,
            "portrait": "images/characters/developer_ai/portrait.png",
            "assistant_id": "asst_fbVtwWljzUZhHtmllEphxkYn",
            "desc": "Especialista em IA e ML. Animado, detalhista, sempre com ideias inovadoras."
        },
        "developer_requirements": {
            "name": NOME_DEVELOPER_REQUIREMENTS,
            "portrait": "images/characters/developer_requirements/portrait.png",
            "assistant_id": "asst_t5wjZ9SCpAbHNCg7utEcY2et",
            "desc": "Especialista em requisitos, comunicativa, detalhista e proativa."
        },
        "developer_coding": {
            "name": NOME_DEVELOPER_CODING,
            "portrait": "images/characters/developer_coding/portrait.png",
            "assistant_id": "asst_d8n3ntyqOsHfdBkJA2LqrZFh",
            "desc": "Desenvolvedor sênior, crítico e experiente, já liderou vários projetos."
        },
        "developer_management": {
            "name": NOME_DEVELOPER_MANAGEMENT,
            "portrait": "images/characters/developer_management/portrait.png",
            "assistant_id": "asst_DzfYAhfiHWBPKborojHC50lZ",
            "desc": "Gerente jovem, organizado, querido pela equipe."
        },
        "developer_quality": {
            "name": NOME_DEVELOPER_QUALITY,
            "portrait": "images/characters/developer_quality/portrait.png",
            "assistant_id": "asst_YkbAOJa4eudUqFL1NMTLkEAA",
            "desc": "Apaixonada por ensinar e qualidade de software."
        },
        "developer_project": {
            "name": NOME_DEVELOPER_PROJECT,
            "portrait": "images/characters/developer_project/portrait.png",
            "assistant_id": "asst_UrbLbKIjf7i5bBzDpvwTkAWn",
            "desc": "Arquiteto de software e bancos, fala pouco, mas certeiro."
        },
        "developer_security": {
            "name": NOME_DEVELOPER_SECURITY,
            "portrait": "images/characters/developer_security/portrait.png",
            "assistant_id": "asst_FylyYRTtZVHXYpVpqCxVk6AX",
            "desc": "Senior, fala devagar e preza segurança dos sistemas."
        },
        "developer_test": {
            "name": NOME_DEVELOPER_TEST,
            "portrait": "images/characters/developer_test/portrait.png",
            "assistant_id": "asst_r5MMYuijOxJHRmqdynMewgWA",
            "desc": "Jovem prodígio dos testes, faz tudo com eficiência."
        },
        "doutora_1": {
            "name": NOME_DOUTORA_1,
            "portrait": "images/characters/doutora_1/portrait.png",
            "assistant_id": "asst_nUAGJlGDbfdxhxpADXSRdLwC",
            "desc": "Experiente médica."
        },
        "doutora_2": {
            "name": NOME_DOUTORA_2,
            "portrait": "images/characters/doutora_2/portrait.png",
            "assistant_id": "asst_0RVJbliiBedg7ADSndhb1BnS",
            "desc": "Jovem médica."
        },
        # Adicione outros se necessário...
    }

    # Ordem de exibição dos contatos na grade (espelha a ordem de AMIGOS_DATA).
    CONTACTS_ORDER = [
        "developer_ai",
        "developer_requirements",
        "developer_coding",
        "developer_management",
        "developer_quality",
        "developer_project",
        "developer_security",
        "developer_test",
        "doutora_1",
        "doutora_2",
    ]

    # Inicializa o assistant_id global para uso no backend
    if not hasattr(renpy.store, "current_assistant_id"):
        renpy.store.current_assistant_id = "asst_default"
