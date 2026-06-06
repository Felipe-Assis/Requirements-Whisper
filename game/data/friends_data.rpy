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
            "assistant_id": "asst_fbVtwWljzUZhHtmllEphxkYn"
        },
        "developer_requirements": {
            "name": NOME_DEVELOPER_REQUIREMENTS,
            "portrait": "images/characters/developer_requirements/portrait.png",
            "assistant_id": "asst_t5wjZ9SCpAbHNCg7utEcY2et"
        },
        "developer_coding": {
            "name": NOME_DEVELOPER_CODING,
            "portrait": "images/characters/developer_coding/portrait.png",
            "assistant_id": "asst_d8n3ntyqOsHfdBkJA2LqrZFh"
        },
        "developer_management": {
            "name": NOME_DEVELOPER_MANAGEMENT,
            "portrait": "images/characters/developer_management/portrait.png",
            "assistant_id": "asst_DzfYAhfiHWBPKborojHC50lZ"
        },
        "developer_quality": {
            "name": NOME_DEVELOPER_QUALITY,
            "portrait": "images/characters/developer_quality/portrait.png",
            "assistant_id": "asst_YkbAOJa4eudUqFL1NMTLkEAA"
        },
        "developer_project": {
            "name": NOME_DEVELOPER_PROJECT,
            "portrait": "images/characters/developer_project/portrait.png",
            "assistant_id": "asst_UrbLbKIjf7i5bBzDpvwTkAWn"
        },
        "developer_security": {
            "name": NOME_DEVELOPER_SECURITY,
            "portrait": "images/characters/developer_security/portrait.png",
            "assistant_id": "asst_FylyYRTtZVHXYpVpqCxVk6AX"
        },
        "developer_test": {
            "name": NOME_DEVELOPER_TEST,
            "portrait": "images/characters/developer_test/portrait.png",
            "assistant_id": "asst_r5MMYuijOxJHRmqdynMewgWA"
        },
        "doutora_1": {
            "name": NOME_DOUTORA_1,
            "portrait": "images/characters/doutora_1/portrait.png",
            "assistant_id": "asst_nUAGJlGDbfdxhxpADXSRdLwC"
        },
        "doutora_2": {
            "name": NOME_DOUTORA_2,
            "portrait": "images/characters/doutora_2/portrait.png",
            "assistant_id": "asst_0RVJbliiBedg7ADSndhb1BnS"
        },
        # Adicione outros se necessário...
    }

    # Inicializa o assistant_id global para uso no backend
    if not hasattr(renpy.store, "current_assistant_id"):
        renpy.store.current_assistant_id = "asst_default"
