# characters.rpy
# -------------------------------
# DEFINIÇÃO DOS PERSONAGENS + MAPEAMENTO DAS IMAGENS
# -------------------------------
# NOME_*/COR_* defines live in data/character_names.rpy.
# Sprite-position transforms live in ui/styles/sprite_transforms.rpy.

define developer_test = Character(NOME_DEVELOPER_TEST, color=COR_DEVELOPER_TEST)
define developer_coding = Character(NOME_DEVELOPER_CODING, color=COR_DEVELOPER_CODING)
define developer_management = Character(NOME_DEVELOPER_MANAGEMENT, color=COR_DEVELOPER_MANAGEMENT)
define developer_requirements = Character(NOME_DEVELOPER_REQUIREMENTS, color=COR_DEVELOPER_REQUIREMENTS)

define developer_ai = Character(NOME_DEVELOPER_AI, color=COR_DEVELOPER_AI)
define developer_quality = Character(NOME_DEVELOPER_QUALITY, color=COR_DEVELOPER_QUALITY)
define developer_project = Character(NOME_DEVELOPER_PROJECT, color=COR_DEVELOPER_PROJECT)
define developer_security = Character(NOME_DEVELOPER_SECURITY, color=COR_DEVELOPER_SECURITY)


define npc_roommate = Character("Colega de República", color="#8EC07C")

define doutora_1 = Character(NOME_DOUTORA_1, color="#B45F06")
define doutora_2 = Character(NOME_DOUTORA_2, color="#4CAF50")

# -------------------------------
# MAPEAMENTO DAS IMAGENS
# -------------------------------

image npc_roommate neutral = "images/characters/amigo/base.png"

# --- doutora ---
image doutora_1 portrait = "images/characters/doutora_1/portrait.png"
image doutora_1 neutral = "images/characters/doutora_1/neutral.png"

# --- enfermeira ---
image doutora_2 portrait = "images/characters/doutora_2/portrait.png"
image doutora_2 neutral = "images/characters/doutora_2/neutral.png"



# --- developer_ai ---
image developer_ai portrait = "images/characters/developer_ai/portrait.png"
image developer_ai concentrated = "images/characters/developer_ai/concentrated.png"
image developer_ai positive = "images/characters/developer_ai/positive.png"
image developer_ai thinking = "images/characters/developer_ai/thinking.png"

# --- developer_coding---
image developer_coding portrait = "images/characters/developer_coding/portrait.png"
image developer_coding neutral = "images/characters/developer_coding/neutral.png"
image developer_coding positive = "images/characters/developer_coding/neutral.png"
image developer_coding serious = "images/characters/developer_coding/serious.png"
image developer_coding thinking = "images/characters/developer_coding/thinking.png"

# --- developer_management---
image developer_management portrait = "images/characters/developer_management/portrait.png"
image developer_management serious = "images/characters/developer_management/serious.png"
image developer_management thinking = "images/characters/developer_management/thinking.png"

# --- developer_project---
image developer_project portrait = "images/characters/developer_project/portrait.png"
image developer_project confident = "images/characters/developer_project/confident.png"
image developer_project neutral = "images/characters/developer_project/confident.png"
image developer_project serious = "images/characters/developer_project/serious.png"
image developer_project thinking = "images/characters/developer_project/thinking.png"

# --- developer_quality ---
image developer_quality portrait = "images/characters/developer_quality/portrait.png"
image developer_quality positive = "images/characters/developer_quality/positive.png"
image developer_quality serious = "images/characters/developer_quality/serious.png"
image developer_quality thinking = "images/characters/developer_quality/thinking.png"

# --- developer_requirements---
image developer_requirements portrait = "images/characters/developer_requirements/portrait.png"
image developer_requirements enthusiastic = "images/characters/developer_requirements/enthusiastic.png"
image developer_requirements positive = "images/characters/developer_requirements/enthusiastic.png"
image developer_requirements neutral = "images/characters/developer_requirements/neutral.png"
image developer_requirements serious = "images/characters/developer_requirements/serious.png"
image developer_requirements thinking = "images/characters/developer_requirements/thinking.png"

# --- developer_security ---
image developer_security portrait = "images/characters/developer_security/portrait.png"
image developer_security serious = "images/characters/developer_security/serious.png"
image developer_security thinking = "images/characters/developer_security/thinking.png"

# --- developer_test --
image developer_test portrait = "images/characters/developer_test/portrait.png"
image developer_test confident = "images/characters/developer_test/confident.png"
image developer_test positive = "images/characters/developer_test/confident.png"
image developer_test enthusiastic = "images/characters/developer_test/enthusiastic.png"
image developer_test serious = "images/characters/developer_test/serious.png"
image developer_test thinking = "images/characters/developer_test/thinking.png"
