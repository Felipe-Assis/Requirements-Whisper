label scene_1_quarto:
    $ alarm_off = False
    $ notebook_taken = False
    $ mochila_taken = False
    $ notebook_in_bag = False
    $ clothes_changed = False
    $ inventory = []
    $ selected_item = None

    scene bg quarto_manha
    show screen inv_quick

    "BIP BIP BIP... O despertador disputa sua atenção com a vontade de dormir mais cinco minutos."
    "Hoje você vai procurar seu primeiro estágio em desenvolvimento de software. Primeiro, desligue o alarme."
    call screen pointclick_quarto_1

    "No silêncio, uma dúvida aparece: será que vão esperar que você já saiba tudo?"
    "Você abre o notebook para procurar uma oportunidade de aprender trabalhando."
    call screen pointclick_quarto_2
    $ inventory.append("notebook")

    "Antes de continuar, como você quer aparecer nesta história?"
    call screen player_formulario
    call escolher_vaga

    scene bg quarto_manha
    "Alguns dias e uma entrevista depois, chega a confirmação: a vaga é sua."
    "Na manhã do primeiro dia, você confere o que vai levar. Pegue a mochila."
    call screen pointclick_quarto_3
    $ inventory.append("mochila")

    "O notebook vai ajudar a registrar o que você descobrir. Guarde-o na mochila."
    call screen pointclick_guardar_notebook

    "Falta escolher uma roupa confortável para conhecer a equipe."
    call screen pointclick_guarda_roupa

    "Tudo pronto. Você respira fundo e sai para o primeiro dia."
    jump proxima_cena

label escolher_vaga(explorar=False):
    scene bg notebook_vagas
    "Três vagas chamam sua atenção. Cada uma traz um problema diferente para investigar."
    menu:
        "Em qual contexto você quer começar?"
        "IDT-UFRJ — organizar reservas de equipamentos":
            $ chosen_job = "IDT-UFRJ"
        "Startup — ajudar estudantes a acompanhar gastos":
            $ chosen_job = "Startup"
        "Empresa — melhorar o atendimento em um sistema legado":
            $ chosen_job = "Empresa legada"
    if not explorar:
        "Você envia sua candidatura para [chosen_job]. Agora é esperar a resposta."
    return

label proxima_cena:
    hide screen inv_quick
    hide screen inventory_screen
    jump scene_2_estagio
