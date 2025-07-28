default selected_contact_description = ""

transform grayscale_icon:
    matrixcolor Matrix([
        0.3, 0.6, 0.1,
        0.3, 0.6, 0.1,
        0.3, 0.6, 0.1
    ])
    alpha 0.8

transform contact_icon:
    xysize (140, 140)


screen contacts_screen():
    tag contacts
    modal True
    zorder 110

    frame:
        background "#000a"
        xalign 0.5
        yalign 0.5
        xsize 840
        ysize 650

        vbox:
            spacing 15

            text "Contatos" size 40 color "#fff"

            hbox:
                spacing 50

                grid 5 2 spacing 30:  # Aumente a grid se quiser mais linhas/colunas

                    # AI (Lucas)
                    if contato_developer_ai:
                        vbox:
                            spacing 3
                            xalign 0.5
                            if disponivel_developer_ai:
                                imagebutton:
                                    idle "developer_ai portrait"
                                    hover "developer_ai portrait"
                                    at contact_icon
                                    hovered [SetVariable("selected_contact_description", "{b}%s{/b}\nEspecialista em IA e ML. Animado, detalhista, sempre com ideias inovadoras." % NOME_DEVELOPER_AI)]
                                    unhovered [SetVariable("selected_contact_description", "")]
                                    action [SetVariable("amigo_selecionado", "developer_ai"), Hide("contacts_screen"), Jump("chat_amigo")]
                            else:
                                imagebutton:
                                    idle "developer_ai portrait"
                                    at contact_icon, grayscale_icon

                            hbox:
                                spacing 1
                                xalign 0.5
                                text "💗" size 16 color "#FF70A6" yalign 0.5
                                bar:
                                    value amizade_developer_ai
                                    range 10
                                    xmaximum 80
                                    ymaximum 10
                                    left_bar (
                                        "#44D067" if amizade_developer_ai == 10 else
                                        "#A4EB9E" if amizade_developer_ai >= 8 else
                                        "#FFEB3B" if amizade_developer_ai >= 5 else
                                        "#FFA149" if amizade_developer_ai >= 3 else
                                        "#FF5353"
                                    )
                                    right_bar "#eee"
                                    thumb None
                                    yalign 0.5

                    # Coding (Joseph)
                    if contato_developer_coding:
                        vbox:
                            spacing 3
                            xalign 0.5
                            if disponivel_developer_coding:
                                imagebutton:
                                    idle "developer_coding portrait"
                                    hover "developer_coding portrait"
                                    at contact_icon
                                    hovered [SetVariable("selected_contact_description", "{b}%s{/b}\\nDesenvolvedor sênior, crítico e experiente, já liderou vários projetos." % NOME_DEVELOPER_CODING)]
                                    unhovered [SetVariable("selected_contact_description", "")]
                                    action [SetVariable("amigo_selecionado", "developer_coding"), Hide("contacts_screen"), Jump("chat_amigo")]
                            else:
                                imagebutton:
                                    idle "developer_coding portrait"
                                    at contact_icon, grayscale_icon

                            hbox:
                                spacing 1
                                xalign 0.5
                                text "💗" size 16 color "#FF70A6" yalign 0.5
                                bar:
                                    value amizade_developer_coding
                                    range 10
                                    xmaximum 80
                                    ymaximum 10
                                    left_bar (
                                        "#44D067" if amizade_developer_coding == 10 else
                                        "#A4EB9E" if amizade_developer_coding >= 8 else
                                        "#FFEB3B" if amizade_developer_coding >= 5 else
                                        "#FFA149" if amizade_developer_coding >= 3 else
                                        "#FF5353"
                                    )
                                    right_bar "#eee"
                                    thumb None
                                    yalign 0.5

                    # Management (Robert)
                    if contato_developer_management:
                        vbox:
                            spacing 3
                            xalign 0.5
                            if disponivel_developer_management:
                                imagebutton:
                                    idle "developer_management portrait"
                                    hover "developer_management portrait"
                                    at contact_icon
                                    hovered [SetVariable("selected_contact_description", "{b}%s{/b}\nGerente jovem, organizado, querido pela equipe." % NOME_DEVELOPER_MANAGEMENT)]
                                    unhovered [SetVariable("selected_contact_description", "")]
                                    action [SetVariable("amigo_selecionado", "developer_management"), Hide("contacts_screen"), Jump("chat_amigo")]
                            else:
                                imagebutton:
                                    idle "developer_management portrait"
                                    at contact_icon, grayscale_icon

                            hbox:
                                spacing 1
                                xalign 0.5
                                text "💗" size 16 color "#FF70A6" yalign 0.5
                                bar:
                                    value amizade_developer_management
                                    range 10
                                    xmaximum 80
                                    ymaximum 10
                                    left_bar (
                                        "#44D067" if amizade_developer_management == 10 else
                                        "#A4EB9E" if amizade_developer_management >= 8 else
                                        "#FFEB3B" if amizade_developer_management >= 5 else
                                        "#FFA149" if amizade_developer_management >= 3 else
                                        "#FF5353"
                                    )
                                    right_bar "#eee"
                                    thumb None
                                    yalign 0.5

                    # Requirements (Emily)
                    if contato_developer_requirements:
                        vbox:
                            spacing 3
                            xalign 0.5
                            if disponivel_developer_requirements:
                                imagebutton:
                                    idle "developer_requirements portrait"
                                    hover "developer_requirements portrait"
                                    at contact_icon
                                    hovered [SetVariable("selected_contact_description", "{b}%s{/b}\\nEspecialista em requisitos, comunicativa, detalhista e proativa." % NOME_DEVELOPER_REQUIREMENTS)]
                                    unhovered [SetVariable("selected_contact_description", "")]
                                    action [SetVariable("amigo_selecionado", "developer_requirements"), Hide("contacts_screen"), Jump("chat_amigo")]
                            else:
                                imagebutton:
                                    idle "developer_requirements portrait"
                                    at contact_icon, grayscale_icon

                            hbox:
                                spacing 1
                                xalign 0.5
                                text "💗" size 16 color "#FF70A6" yalign 0.5
                                bar:
                                    value amizade_developer_requirements
                                    range 10
                                    xmaximum 80
                                    ymaximum 10
                                    left_bar (
                                        "#44D067" if amizade_developer_requirements == 10 else
                                        "#A4EB9E" if amizade_developer_requirements >= 8 else
                                        "#FFEB3B" if amizade_developer_requirements >= 5 else
                                        "#FFA149" if amizade_developer_requirements >= 3 else
                                        "#FF5353"
                                    )
                                    right_bar "#eee"
                                    thumb None
                                    yalign 0.5

                    # Quality (Daiana)
                    if contato_developer_quality:
                        vbox:
                            spacing 3
                            xalign 0.5
                            if disponivel_developer_quality:
                                imagebutton:
                                    idle "developer_quality portrait"
                                    hover "developer_quality portrait"
                                    at contact_icon
                                    hovered [SetVariable("selected_contact_description", "{b}%s{/b}\nApaixonada por ensinar e qualidade de software." % NOME_DEVELOPER_QUALITY)]
                                    unhovered [SetVariable("selected_contact_description", "")]
                                    action [SetVariable("amigo_selecionado", "developer_quality"), Hide("contacts_screen"), Jump("chat_amigo")]
                            else:
                                imagebutton:
                                    idle "developer_quality portrait"
                                    at contact_icon, grayscale_icon

                            hbox:
                                spacing 1
                                xalign 0.5
                                text "💗" size 16 color "#FF70A6" yalign 0.5
                                bar:
                                    value amizade_developer_quality
                                    range 10
                                    xmaximum 80
                                    ymaximum 10
                                    left_bar (
                                        "#44D067" if amizade_developer_quality == 10 else
                                        "#A4EB9E" if amizade_developer_quality >= 8 else
                                        "#FFEB3B" if amizade_developer_quality >= 5 else
                                        "#FFA149" if amizade_developer_quality >= 3 else
                                        "#FF5353"
                                    )
                                    right_bar "#eee"
                                    thumb None
                                    yalign 0.5

                    # Project (Heitor)
                    if contato_developer_project:
                        vbox:
                            spacing 3
                            xalign 0.5
                            if disponivel_developer_project:
                                imagebutton:
                                    idle "developer_project portrait"
                                    hover "developer_project portrait"
                                    at contact_icon
                                    hovered [SetVariable("selected_contact_description", "{b}%s{/b}\nArquiteto de software e bancos, fala pouco, mas certeiro." % NOME_DEVELOPER_PROJECT)]
                                    unhovered [SetVariable("selected_contact_description", "")]
                                    action [SetVariable("amigo_selecionado", "developer_project"), Hide("contacts_screen"), Jump("chat_amigo")]
                            else:
                                imagebutton:
                                    idle "developer_project portrait"
                                    at contact_icon, grayscale_icon

                            hbox:
                                spacing 1
                                xalign 0.5
                                text "💗" size 16 color "#FF70A6" yalign 0.5
                                bar:
                                    value amizade_developer_project
                                    range 10
                                    xmaximum 80
                                    ymaximum 10
                                    left_bar (
                                        "#44D067" if amizade_developer_project == 10 else
                                        "#A4EB9E" if amizade_developer_project >= 8 else
                                        "#FFEB3B" if amizade_developer_project >= 5 else
                                        "#FFA149" if amizade_developer_project >= 3 else
                                        "#FF5353"
                                    )
                                    right_bar "#eee"
                                    thumb None
                                    yalign 0.5

                    # Security (Mateus)
                    if contato_developer_security:
                        vbox:
                            spacing 3
                            xalign 0.5
                            if disponivel_developer_security:
                                imagebutton:
                                    idle "developer_security portrait"
                                    hover "developer_security portrait"
                                    at contact_icon
                                    hovered [SetVariable("selected_contact_description", "{b}%s{/b}\nSenior, fala devagar e preza segurança dos sistemas." % NOME_DEVELOPER_SECURITY)]
                                    unhovered [SetVariable("selected_contact_description", "")]
                                    action [SetVariable("amigo_selecionado", "developer_security"), Hide("contacts_screen"), Jump("chat_amigo")]
                            else:
                                imagebutton:
                                    idle "developer_security portrait"
                                    at contact_icon, grayscale_icon

                            hbox:
                                spacing 1
                                xalign 0.5
                                text "💗" size 16 color "#FF70A6" yalign 0.5
                                bar:
                                    value amizade_developer_security
                                    range 10
                                    xmaximum 80
                                    ymaximum 10
                                    left_bar (
                                        "#44D067" if amizade_developer_security == 10 else
                                        "#A4EB9E" if amizade_developer_security >= 8 else
                                        "#FFEB3B" if amizade_developer_security >= 5 else
                                        "#FFA149" if amizade_developer_security >= 3 else
                                        "#FF5353"
                                    )
                                    right_bar "#eee"
                                    thumb None
                                    yalign 0.5

                    # Test (César)
                    if contato_developer_test:
                        vbox:
                            spacing 3
                            xalign 0.5
                            if disponivel_developer_test:
                                imagebutton:
                                    idle "developer_test portrait"
                                    hover "developer_test portrait"
                                    at contact_icon
                                    hovered [SetVariable("selected_contact_description", "{b}%s{/b}\nJovem prodígio dos testes, faz tudo com eficiência." % NOME_DEVELOPER_TEST)]
                                    unhovered [SetVariable("selected_contact_description", "")]
                                    action [SetVariable("amigo_selecionado", "developer_test"), Hide("contacts_screen"), Jump("chat_amigo")]
                            else:
                                imagebutton:
                                    idle "developer_test portrait"
                                    at contact_icon, grayscale_icon
                            hbox:
                                spacing 1
                                xalign 0.5
                                text "💗" size 16 color "#FF70A6" yalign 0.5
                                bar:
                                    value amizade_developer_test
                                    range 10
                                    xmaximum 80
                                    ymaximum 10
                                    left_bar (
                                        "#44D067" if amizade_developer_test == 10 else
                                        "#A4EB9E" if amizade_developer_test >= 8 else
                                        "#FFEB3B" if amizade_developer_test >= 5 else
                                        "#FFA149" if amizade_developer_test >= 3 else
                                        "#FF5353"
                                    )
                                    right_bar "#eee"
                                    thumb None
                                    yalign 0.5


                    if contato_doutora_1:
                        vbox:
                            spacing 3
                            xalign 0.5
                            if disponivel_doutora_1:
                                imagebutton:
                                    idle "doutora_1 portrait"
                                    hover "doutora_1 portrait"
                                    at contact_icon
                                    hovered [SetVariable("selected_contact_description", "{b}%s{/b}\nExperiente médica." % NOME_DOUTORA_1)]
                                    unhovered [SetVariable("selected_contact_description", "")]
                                    action [SetVariable("amigo_selecionado", "doutora_1"), Hide("contacts_screen"), Jump("chat_amigo")]
                            else:
                                imagebutton:
                                    idle "doutora_1 portrait"
                                    at contact_icon, grayscale_icon
                            hbox:
                                spacing 1
                                xalign 0.5
                                text "💗" size 16 color "#FF70A6" yalign 0.5
                                bar:
                                    value amizade_doutora_1
                                    range 10
                                    xmaximum 80
                                    ymaximum 10
                                    left_bar (
                                        "#44D067" if amizade_doutora_1 == 10 else
                                        "#A4EB9E" if amizade_doutora_1 >= 8 else
                                        "#FFEB3B" if amizade_doutora_1 >= 5 else
                                        "#FFA149" if amizade_doutora_1 >= 3 else
                                        "#FF5353"
                                    )
                                    right_bar "#eee"
                                    thumb None
                                    yalign 0.5



                    if contato_doutora_2:
                        vbox:
                            spacing 3
                            xalign 0.5
                            if disponivel_doutora_2:
                                imagebutton:
                                    idle "doutora_2 portrait"
                                    hover "doutora_2 portrait"
                                    at contact_icon
                                    hovered [SetVariable("selected_contact_description", "{b}%s{/b}\nJovem médica." % NOME_DOUTORA_2)]
                                    unhovered [SetVariable("selected_contact_description", "")]
                                    action [SetVariable("amigo_selecionado", "amizade_doutora_2"), Hide("contacts_screen"), Jump("chat_amigo")]
                            else:
                                imagebutton:
                                    idle "doutora_2 portrait"
                                    at contact_icon, grayscale_icon

                            hbox:
                                spacing 1
                                xalign 0.5
                                text "💗" size 16 color "#FF70A6" yalign 0.5
                                bar:
                                    value amizade_doutora_2
                                    range 10
                                    xmaximum 80
                                    ymaximum 10
                                    left_bar (
                                        "#44D067" if amizade_doutora_2 == 10 else
                                        "#A4EB9E" if amizade_doutora_2 >= 8 else
                                        "#FFEB3B" if amizade_doutora_2 >= 5 else
                                        "#FFA149" if amizade_doutora_2 >= 3 else
                                        "#FF5353"
                                    )
                                    right_bar "#eee"
                                    thumb None
                                    yalign 0.5

            frame:
                background "#222a"
                xsize 725
                yalign 0.0

                text "[selected_contact_description]":
                    color "#fff"
                    size 20
                    xalign 0.5

            textbutton "Fechar" action Return() xalign 0.5


init python:
    def add_contact(contact_id):
        # Inicializa o set de contatos se não existir
        if not hasattr(store, 'contacts'):
            store.contacts = set()
        # Adiciona ao set, se ainda não estiver
        if contact_id not in store.contacts:
            store.contacts.add(contact_id)
            # Tenta setar a variável booleana global correspondente (ex: contato_developer_ai)
            var_name = "contato_" + contact_id
            if hasattr(store, var_name):
                setattr(store, var_name, True)
            # Notifica nome amigável, se possível
            try:
                nome = AMIGOS_DATA[contact_id]["name"]
                renpy.notify(f"Contato adicionado: {nome}")
            except:
                renpy.notify(f"Contato adicionado: {contact_id.replace('_',' ').capitalize()}")
        else:
            renpy.notify("Contato já adicionado.")


    def add_friendship_point(character_id, amount=0.5):
        """
        Adiciona pontos de amizade ao personagem e notifica o jogador.
        Exemplo: $ add_friendship_point("developer_requirements")
        """
        var_name = "amizade_" + character_id
        if hasattr(store, var_name):
            current = getattr(store, var_name)
            new_value = current + amount
            setattr(store, var_name, new_value)
            # Notificação: tenta usar nome bonito se existir em AMIGOS_DATA
            try:
                nome = AMIGOS_DATA[character_id]["name"]
                renpy.notify(f"Pontos de amizade com {nome} +{amount} (Total: {new_value})")
            except:
                renpy.notify(f"Pontos de amizade com {character_id.replace('_',' ').capitalize()} +{amount} (Total: {new_value})")
            # Debug opcional no log
            renpy.log(f"Pontos de amizade de {var_name}: {new_value}")
        else:
            renpy.log(f"Personagem não encontrado: {var_name}")

    def get_friendship_point(character_id):
        """
        Retorna os pontos de amizade do personagem.
        """
        var_name = "amizade_" + character_id
        if hasattr(store, var_name):
            return getattr(store, var_name)
        else:
            renpy.log(f"Personagem não encontrado: {var_name}")
            return 0