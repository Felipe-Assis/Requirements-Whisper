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

# Tile de contato: com foco (mouse ou teclado), fundo na cor de destaque.
# Nome, disponibilidade e amizade vêm escritos; o cinza do retrato
# indisponível é só reforço.
style contato_tile is button:
    background Solid("#1f2730")
    hover_background Solid(gui.accent_color)
    insensitive_background Solid("#171f27")
    padding (10, 12)
    xsize 210

style contato_tile_text is nb_texto:
    size 22
    hover_color "#101820"
    xalign 0.5
    text_align 0.5

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
        button:
            style "contato_tile"
            alt (_nome if _disponivel else __("{nome}, indisponível agora").format(nome=_nome))
            if _disponivel:
                hovered [SetVariable("selected_contact_description", "{b}%s{/b}\n%s" % (_nome, _desc))]
                unhovered [SetVariable("selected_contact_description", "")]
                # Call, não Jump: aberta por "call screen" numa cena, o
                # return de chat_amigo volta para a cena; com Jump ele
                # encerrava a cena e pulava o resto dela.
                action [SetVariable("amigo_selecionado", cid), Hide("contacts_screen"), Call("chat_amigo")]
            else:
                action None
            vbox:
                spacing 4
                xalign 0.5
                if _disponivel:
                    add ("%s portrait" % cid) at contact_icon xalign 0.5
                else:
                    add ("%s portrait" % cid) at contact_icon, grayscale_icon xalign 0.5
                text _nome style "contato_tile_text" bold True
                if _disponivel:
                    text _("Disponível") style "contato_tile_text" size 20
                else:
                    text _("Indisponível agora") style "contato_tile_text" size 20 color "#c0c8d0"
                hbox:
                    spacing 6
                    xalign 0.5
                    text "♥" size 18 color "#FF70A6" yalign 0.5
                    bar:
                        value _amizade
                        range 10
                        xsize 80
                        ysize 10
                        left_bar friendship_color(_amizade)
                        right_bar "#55606b"
                        thumb None
                        yalign 0.5
                    text ("%d/10" % round(_amizade)) style "contato_tile_text" size 18 yalign 0.5


screen contacts_screen():
    tag contacts
    modal True
    zorder 110

    $ ordem = route_contacts_order()
    # 3 colunas para as rotas de 6 contatos; 5 para a saúde (10 contatos).
    $ colunas = 3 if len(ordem) <= 6 else 5
    $ largura = colunas * 210 + (colunas - 1) * 20

    key "game_menu" action Return()

    add Solid("#000000b0")

    frame:
        style "nb_painel"
        align (0.5, 0.5)

        vbox:
            spacing 18
            xsize largura

            hbox:
                xfill True
                text _("Contatos") style "nb_titulo" yalign 0.5
                textbutton _("Fechar"):
                    style "nb_botao"
                    xalign 1.0
                    id "contatos_fechar"
                    action Return()

            hbox:
                box_wrap True
                spacing 20
                box_wrap_spacing 20
                xsize largura
                for cid in ordem:
                    use contact_tile(cid)

            frame:
                style "nb_cartao"
                ysize 110
                if selected_contact_description:
                    text "[selected_contact_description]" style "nb_texto" size 22
                else:
                    text _("Escolha alguém disponível para conversar. Quem está indisponível não pode receber mensagem agora.") style "nb_texto" size 22 color "#c0c8d0"

            text _("Setas escolhem, Enter abre a conversa, Esc fecha."):
                style "nb_dica"
