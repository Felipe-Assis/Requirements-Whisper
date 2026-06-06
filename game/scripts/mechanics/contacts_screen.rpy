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


# Um único tile de contato, parametrizado por cid (id canônico do contato).
# Lê o estado via getattr(store, ...) e os dados (nome/desc) de AMIGOS_DATA.
# Substitui os 10 blocos copy-paste que existiam antes.
screen contact_tile(cid):
    $ _contato = getattr(store, "contato_" + cid)
    if _contato:
        $ _disponivel = getattr(store, "disponivel_" + cid)
        $ _amizade = getattr(store, "amizade_" + cid)
        $ _nome = AMIGOS_DATA[cid]["name"]
        $ _desc = AMIGOS_DATA[cid]["desc"]
        vbox:
            spacing 3
            xalign 0.5
            if _disponivel:
                imagebutton:
                    idle "%s portrait" % cid
                    hover "%s portrait" % cid
                    at contact_icon
                    hovered [SetVariable("selected_contact_description", "{b}%s{/b}\n%s" % (_nome, _desc))]
                    unhovered [SetVariable("selected_contact_description", "")]
                    action [SetVariable("amigo_selecionado", cid), Hide("contacts_screen"), Jump("chat_amigo")]
            else:
                imagebutton:
                    idle "%s portrait" % cid
                    at contact_icon, grayscale_icon

            hbox:
                spacing 1
                xalign 0.5
                text "💗" size 16 color "#FF70A6" yalign 0.5
                bar:
                    value _amizade
                    range 10
                    xmaximum 80
                    ymaximum 10
                    left_bar friendship_color(_amizade)
                    right_bar "#eee"
                    thumb None
                    yalign 0.5


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

            text _("Contatos") size 40 color "#fff"

            hbox:
                spacing 50

                grid 5 2 spacing 30:  # Aumente a grid se quiser mais linhas/colunas

                    for cid in CONTACTS_ORDER:
                        use contact_tile(cid)

            frame:
                background "#222a"
                xsize 725
                yalign 0.0

                text "[selected_contact_description]":
                    color "#fff"
                    size 20
                    xalign 0.5

            textbutton _("Fechar") action Return() xalign 0.5