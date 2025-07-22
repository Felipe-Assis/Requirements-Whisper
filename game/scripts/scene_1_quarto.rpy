# scene_1_quarto.rpy
label scene_1_quarto:
    # Inicia variáveis locais
    $ alarm_off = False
    $ notebook_taken = False
    $ mochila_taken = False
    $ notebook_in_bag = False
    $ clothes_changed = False
    $ player_gender = ""
    $ player_name = ""
    $ player_age = 18
    $ inventory = []

    # Background do quarto
    scene bg quarto_manha

    show screen inv_quick # Mostra inventário rápido (caso já implementado)

    "BIP BIP BIP... O alarme toca alto logo cedo."

    show screen pointclick_quarto_1

    "Você deve desligar o despertador..."

    # Espera o jogador clicar no despertador
    while not alarm_off:
        $ renpy.pause(0.5)

    "Você desliga o alarme e sente o silêncio no quarto."

    "Hora de checar o notebook para procurar vagas de estágio."

    show screen pointclick_quarto_2

    while not notebook_taken:
        $ renpy.pause(0.5)

    "Antes de acessar as vagas, preencha seu cadastro:"

    call screen player_formulario

    $ inventory.append("notebook")
    "Você pegou seu notebook."

    "Agora, pegue sua mochila antes de sair."
    show screen pointclick_quarto_3

    while not mochila_taken:
        $ renpy.pause(0.5)

    $ inventory.append("mochila")
    "Você pegou sua mochila."

    "Guarde seu notebook na mochila antes de sair."
    show screen pointclick_guardar_notebook

    while not notebook_in_bag:
        $ renpy.pause(0.5)

    $ inventory.remove("notebook")
    $ inventory.append("notebook (na mochila)")

    "Tudo pronto, mas talvez seja uma boa trocar de roupa antes de sair."

    show screen pointclick_guarda_roupa

    while not clothes_changed:
        $ renpy.pause(0.5)

    "Você trocou de roupa. Agora está pronto para começar o dia!"

    jump escolher_vaga

label escolher_vaga:
    scene bg notebook_vagas
    "Você abre o notebook e encontra três oportunidades de estágio:"
    menu:
        "Qual vaga deseja se candidatar?"
        "Projeto de software para o IDT-UFRJ":
            $ chosen_job = "IDT-UFRJ"
            jump proxima_cena
        "Desenvolvimento mobile para startup de educação financeira":
            $ chosen_job = "Startup"
            jump proxima_cena
        "Estágio em manutenção de sistemas legados numa grande empresa":
            $ chosen_job = "Empresa legada"
            jump proxima_cena

label proxima_cena:
    # Continuação do roteiro...
    "Você se prepara para uma nova etapa da sua jornada..."
    return
