# characters.rpy
# -------------------------------
# DEFINIÇÃO DOS PERSONAGENS + MAPEAMENTO DAS IMAGENS
# -------------------------------
# NOME_*/COR_* defines live in data/character_names.rpy.
# Sprite-position transforms live in ui/styles/sprite_transforms.rpy.
# image="<id>" liga o personagem à tag do sprite: o destaque de quem fala
# (ui/styles/fala_destaque.rpy) usa renpy.get_say_image_tag(). Não existe
# imagem "side <id>", então a tela say continua sem side image.

define developer_test = Character(NOME_DEVELOPER_TEST, color=COR_DEVELOPER_TEST, image="developer_test")
define developer_coding = Character(NOME_DEVELOPER_CODING, color=COR_DEVELOPER_CODING, image="developer_coding")
define developer_management = Character(NOME_DEVELOPER_MANAGEMENT, color=COR_DEVELOPER_MANAGEMENT, image="developer_management")
define developer_requirements = Character(NOME_DEVELOPER_REQUIREMENTS, color=COR_DEVELOPER_REQUIREMENTS, image="developer_requirements")

define developer_ai = Character(NOME_DEVELOPER_AI, color=COR_DEVELOPER_AI, image="developer_ai")
define developer_quality = Character(NOME_DEVELOPER_QUALITY, color=COR_DEVELOPER_QUALITY, image="developer_quality")
define developer_project = Character(NOME_DEVELOPER_PROJECT, color=COR_DEVELOPER_PROJECT, image="developer_project")
define developer_security = Character(NOME_DEVELOPER_SECURITY, color=COR_DEVELOPER_SECURITY, image="developer_security")


define npc_roommate = Character(_("Colega de República"), color="#8EC07C", image="npc_roommate")

define doutora_1 = Character(NOME_DOUTORA_1, color="#B45F06", image="doutora_1")
define doutora_2 = Character(NOME_DOUTORA_2, color="#4CAF50", image="doutora_2")

# -------------------------------
# MAPEAMENTO DAS IMAGENS
# -------------------------------

image npc_roommate neutral = "images/characters/amigo/base.png"

# --- doutora ---
image doutora_1 portrait = "images/characters/doutora_1/portrait.png"
image doutora_1 neutral = "images/characters/doutora_1/neutral.png"
image doutora_1 serious = "images/characters/doutora_1/serious.png"
image doutora_1 thinking = "images/characters/doutora_1/thinking.png"
image doutora_1 positive = "images/characters/doutora_1/positive.png"

# --- doutora_2 ---
image doutora_2 portrait = "images/characters/doutora_2/portrait.png"
image doutora_2 neutral = "images/characters/doutora_2/neutral.png"
image doutora_2 serious = "images/characters/doutora_2/serious.png"
image doutora_2 thinking = "images/characters/doutora_2/thinking.png"
image doutora_2 positive = "images/characters/doutora_2/positive.png"



# --- developer_ai ---
image developer_ai portrait = "images/characters/developer_ai/portrait.png"
image developer_ai concentrated = "images/characters/developer_ai/concentrated.png"
image developer_ai positive = "images/characters/developer_ai/positive.png"
image developer_ai thinking = "images/characters/developer_ai/thinking.png"
# alias (atributo sem arte própria)
image developer_ai enthusiastic = "images/characters/developer_ai/positive.png"

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
# alias (atributo sem arte própria)
image developer_management positive = "images/characters/developer_management/thinking.png"
image developer_management enthusiastic = "images/characters/developer_management/thinking.png"

# --- developer_project---
image developer_project portrait = "images/characters/developer_project/portrait.png"
image developer_project confident = "images/characters/developer_project/confident.png"
image developer_project neutral = "images/characters/developer_project/confident.png"
image developer_project serious = "images/characters/developer_project/serious.png"
image developer_project thinking = "images/characters/developer_project/thinking.png"
# alias (atributo sem arte própria)
image developer_project positive = "images/characters/developer_project/confident.png"

# --- developer_quality ---
image developer_quality portrait = "images/characters/developer_quality/portrait.png"
image developer_quality positive = "images/characters/developer_quality/positive.png"
image developer_quality serious = "images/characters/developer_quality/serious.png"
image developer_quality thinking = "images/characters/developer_quality/thinking.png"
# alias (atributo sem arte própria)
image developer_quality enthusiastic = "images/characters/developer_quality/positive.png"

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
# alias (atributo sem arte própria)
image developer_security enthusiastic = "images/characters/developer_security/thinking.png"

# --- developer_test --
image developer_test portrait = "images/characters/developer_test/portrait.png"
image developer_test confident = "images/characters/developer_test/confident.png"
image developer_test positive = "images/characters/developer_test/confident.png"
image developer_test enthusiastic = "images/characters/developer_test/enthusiastic.png"
image developer_test serious = "images/characters/developer_test/serious.png"
image developer_test thinking = "images/characters/developer_test/thinking.png"

# -------------------------------
# PERSONAGENS DAS ROTAS STARTUP (st_*) E CORPORATIVO (co_*)
# -------------------------------
# A arte final ainda não chegou: os PNGs atuais são placeholders listados em
# docs/rotas/placeholders.txt. Equipe tem neutral/thinking/serious; stakeholders
# têm neutral/thinking. Os atributos extras são aliases para as cenas poderem
# usar o mesmo vocabulário da rota saúde.

define st_mentora = Character(NOME_ST_MENTORA, color=COR_ST_MENTORA, image="st_mentora")
define st_techlead = Character(NOME_ST_TECHLEAD, color=COR_ST_TECHLEAD, image="st_techlead")
define st_mobile = Character(NOME_ST_MOBILE, color=COR_ST_MOBILE, image="st_mobile")
define st_qualidade = Character(NOME_ST_QUALIDADE, color=COR_ST_QUALIDADE, image="st_qualidade")
define st_ceo = Character(NOME_ST_CEO, color=COR_ST_CEO, image="st_ceo")
define st_estudante = Character(NOME_ST_ESTUDANTE, color=COR_ST_ESTUDANTE, image="st_estudante")
define co_mentora = Character(NOME_CO_MENTORA, color=COR_CO_MENTORA, image="co_mentora")
define co_legado = Character(NOME_CO_LEGADO, color=COR_CO_LEGADO, image="co_legado")
define co_dev = Character(NOME_CO_DEV, color=COR_CO_DEV, image="co_dev")
define co_qualidade = Character(NOME_CO_QUALIDADE, color=COR_CO_QUALIDADE, image="co_qualidade")
define co_supervisora = Character(NOME_CO_SUPERVISORA, color=COR_CO_SUPERVISORA, image="co_supervisora")
define co_solicitante = Character(NOME_CO_SOLICITANTE, color=COR_CO_SOLICITANTE, image="co_solicitante")

# --- st_mentora ---
image st_mentora portrait = "images/characters/st_mentora/portrait.png"
image st_mentora neutral = "images/characters/st_mentora/neutral.png"
image st_mentora thinking = "images/characters/st_mentora/thinking.png"
image st_mentora serious = "images/characters/st_mentora/serious.png"
# aliases (atributos sem arte própria)
image st_mentora positive = "images/characters/st_mentora/neutral.png"
image st_mentora enthusiastic = "images/characters/st_mentora/neutral.png"
image st_mentora confident = "images/characters/st_mentora/neutral.png"
image st_mentora concentrated = "images/characters/st_mentora/neutral.png"

# --- st_techlead ---
image st_techlead portrait = "images/characters/st_techlead/portrait.png"
image st_techlead neutral = "images/characters/st_techlead/neutral.png"
image st_techlead thinking = "images/characters/st_techlead/thinking.png"
image st_techlead serious = "images/characters/st_techlead/serious.png"
# aliases (atributos sem arte própria)
image st_techlead positive = "images/characters/st_techlead/neutral.png"
image st_techlead enthusiastic = "images/characters/st_techlead/neutral.png"
image st_techlead confident = "images/characters/st_techlead/neutral.png"
image st_techlead concentrated = "images/characters/st_techlead/neutral.png"

# --- st_mobile ---
image st_mobile portrait = "images/characters/st_mobile/portrait.png"
image st_mobile neutral = "images/characters/st_mobile/neutral.png"
image st_mobile thinking = "images/characters/st_mobile/thinking.png"
image st_mobile serious = "images/characters/st_mobile/serious.png"
# aliases (atributos sem arte própria)
image st_mobile positive = "images/characters/st_mobile/neutral.png"
image st_mobile enthusiastic = "images/characters/st_mobile/neutral.png"
image st_mobile confident = "images/characters/st_mobile/neutral.png"
image st_mobile concentrated = "images/characters/st_mobile/neutral.png"

# --- st_qualidade ---
image st_qualidade portrait = "images/characters/st_qualidade/portrait.png"
image st_qualidade neutral = "images/characters/st_qualidade/neutral.png"
image st_qualidade thinking = "images/characters/st_qualidade/thinking.png"
image st_qualidade serious = "images/characters/st_qualidade/serious.png"
# aliases (atributos sem arte própria)
image st_qualidade positive = "images/characters/st_qualidade/neutral.png"
image st_qualidade enthusiastic = "images/characters/st_qualidade/neutral.png"
image st_qualidade confident = "images/characters/st_qualidade/neutral.png"
image st_qualidade concentrated = "images/characters/st_qualidade/neutral.png"

# --- st_ceo ---
image st_ceo portrait = "images/characters/st_ceo/portrait.png"
image st_ceo neutral = "images/characters/st_ceo/neutral.png"
image st_ceo thinking = "images/characters/st_ceo/thinking.png"
# aliases (atributos sem arte própria)
image st_ceo positive = "images/characters/st_ceo/neutral.png"
image st_ceo enthusiastic = "images/characters/st_ceo/neutral.png"
image st_ceo confident = "images/characters/st_ceo/neutral.png"
image st_ceo concentrated = "images/characters/st_ceo/neutral.png"
image st_ceo serious = "images/characters/st_ceo/thinking.png"

# --- st_estudante ---
image st_estudante portrait = "images/characters/st_estudante/portrait.png"
image st_estudante neutral = "images/characters/st_estudante/neutral.png"
image st_estudante thinking = "images/characters/st_estudante/thinking.png"
# aliases (atributos sem arte própria)
image st_estudante positive = "images/characters/st_estudante/neutral.png"
image st_estudante enthusiastic = "images/characters/st_estudante/neutral.png"
image st_estudante confident = "images/characters/st_estudante/neutral.png"
image st_estudante concentrated = "images/characters/st_estudante/neutral.png"
image st_estudante serious = "images/characters/st_estudante/thinking.png"

# --- co_mentora ---
image co_mentora portrait = "images/characters/co_mentora/portrait.png"
image co_mentora neutral = "images/characters/co_mentora/neutral.png"
image co_mentora thinking = "images/characters/co_mentora/thinking.png"
image co_mentora serious = "images/characters/co_mentora/serious.png"
# aliases (atributos sem arte própria)
image co_mentora positive = "images/characters/co_mentora/neutral.png"
image co_mentora enthusiastic = "images/characters/co_mentora/neutral.png"
image co_mentora confident = "images/characters/co_mentora/neutral.png"
image co_mentora concentrated = "images/characters/co_mentora/neutral.png"

# --- co_legado ---
image co_legado portrait = "images/characters/co_legado/portrait.png"
image co_legado neutral = "images/characters/co_legado/neutral.png"
image co_legado thinking = "images/characters/co_legado/thinking.png"
image co_legado serious = "images/characters/co_legado/serious.png"
# aliases (atributos sem arte própria)
image co_legado positive = "images/characters/co_legado/neutral.png"
image co_legado enthusiastic = "images/characters/co_legado/neutral.png"
image co_legado confident = "images/characters/co_legado/neutral.png"
image co_legado concentrated = "images/characters/co_legado/neutral.png"

# --- co_dev ---
image co_dev portrait = "images/characters/co_dev/portrait.png"
image co_dev neutral = "images/characters/co_dev/neutral.png"
image co_dev thinking = "images/characters/co_dev/thinking.png"
image co_dev serious = "images/characters/co_dev/serious.png"
# aliases (atributos sem arte própria)
image co_dev positive = "images/characters/co_dev/neutral.png"
image co_dev enthusiastic = "images/characters/co_dev/neutral.png"
image co_dev confident = "images/characters/co_dev/neutral.png"
image co_dev concentrated = "images/characters/co_dev/neutral.png"

# --- co_qualidade ---
image co_qualidade portrait = "images/characters/co_qualidade/portrait.png"
image co_qualidade neutral = "images/characters/co_qualidade/neutral.png"
image co_qualidade thinking = "images/characters/co_qualidade/thinking.png"
image co_qualidade serious = "images/characters/co_qualidade/serious.png"
# aliases (atributos sem arte própria)
image co_qualidade positive = "images/characters/co_qualidade/neutral.png"
image co_qualidade enthusiastic = "images/characters/co_qualidade/neutral.png"
image co_qualidade confident = "images/characters/co_qualidade/neutral.png"
image co_qualidade concentrated = "images/characters/co_qualidade/neutral.png"

# --- co_supervisora ---
image co_supervisora portrait = "images/characters/co_supervisora/portrait.png"
image co_supervisora neutral = "images/characters/co_supervisora/neutral.png"
image co_supervisora thinking = "images/characters/co_supervisora/thinking.png"
# aliases (atributos sem arte própria)
image co_supervisora positive = "images/characters/co_supervisora/neutral.png"
image co_supervisora enthusiastic = "images/characters/co_supervisora/neutral.png"
image co_supervisora confident = "images/characters/co_supervisora/neutral.png"
image co_supervisora concentrated = "images/characters/co_supervisora/neutral.png"
image co_supervisora serious = "images/characters/co_supervisora/thinking.png"

# --- co_solicitante ---
image co_solicitante portrait = "images/characters/co_solicitante/portrait.png"
image co_solicitante neutral = "images/characters/co_solicitante/neutral.png"
image co_solicitante thinking = "images/characters/co_solicitante/thinking.png"
# aliases (atributos sem arte própria)
image co_solicitante positive = "images/characters/co_solicitante/neutral.png"
image co_solicitante enthusiastic = "images/characters/co_solicitante/neutral.png"
image co_solicitante confident = "images/characters/co_solicitante/neutral.png"
image co_solicitante concentrated = "images/characters/co_solicitante/neutral.png"
image co_solicitante serious = "images/characters/co_solicitante/thinking.png"
