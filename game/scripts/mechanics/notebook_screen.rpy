# notebook_screen.rpy
# -------------------------------
# NOTEBOOK: registros da rota atual
# -------------------------------
# Aberto pelo tile "notebook" da Mochila. Lista os 8 registros da rota com o
# estado escrito ("registrado" / "pendente"), não só pela cor. Dados e
# registrar() em logic/learning.rpy; textos em ROUTES[rota]["records"].
#
# A Mochila abre por ShowMenu (contexto de menu): ali, fechar = Return(), que
# encerra o menu. Fora dele (Show direto, testes), fechar = Hide.

# Estilos nb_*: painel das telas de mecânica (notebook, atividades, resumo do
# epílogo, Mochila, contatos e chat). Fundo opaco atrás de todo texto; o
# estado de botões e marcas vem escrito no texto, não só na cor.
style nb_painel is frame:
    background Solid("#101820")
    padding (48, 40)

style nb_titulo is text:
    color gui.accent_color
    size 44
    bold True

style nb_texto is text:
    color "#ffffff"
    size 28

style nb_secao is nb_texto:
    color gui.accent_color
    bold True

style nb_dica is nb_texto:
    size 22
    color "#c0c8d0"

style nb_cartao is frame:
    background Solid("#1f2730")
    padding (28, 22)
    xfill True

# Barra de rolagem desenhada com cores sólidas: as imagens gui/scrollbar só
# têm os estados idle/hover, e o motor também pede selected/insensitive.
style nb_vscrollbar is vscrollbar:
    xsize 14
    base_bar Solid("#ffffff1a")
    thumb Solid(gui.accent_color)
    unscrollable "hide"

# Foco (teclado ou mouse) = fundo na cor de destaque com texto escuro.
# Marcado = fundo azul-acinzentado; desabilitado = mais escuro, texto apagado.
# selected_hover é explícito para o foco continuar visível num item marcado.
style nb_botao is button:
    background Solid("#2a333d")
    hover_background Solid(gui.accent_color)
    selected_background Solid("#285a85")
    selected_hover_background Solid(gui.accent_color)
    insensitive_background Solid("#171f27")
    padding (28, 16)

style nb_botao_text is text:
    color "#ffffff"
    hover_color "#101820"
    selected_hover_color "#101820"
    insensitive_color "#7d8894"
    size 28

screen notebook_registros():
    tag notebook
    modal True
    zorder 120

    $ fechar = If(_menu, Return(), Hide("notebook_registros"))
    $ dados = registros_rota()
    $ descobertos, total = registros_contagem()
    $ empresa = route_data()["empresa"]
    $ tam_texto = 34 if texto_maior_ativo() else 28

    key "game_menu" action fechar
    key "K_n" action fechar

    add Solid("#000000b0")

    frame:
        style "nb_painel"
        align (0.5, 0.5)
        xsize 1500
        ysize 940

        vbox:
            spacing 18

            hbox:
                xfill True
                text _("Notebook · registros do projeto") style "nb_titulo" yalign 0.5
                textbutton _("Fechar (Esc ou N)"):
                    style "nb_botao"
                    xalign 1.0
                    id "notebook_fechar"
                    default_focus True
                    action fechar

            text _("[empresa!t] · [descobertos] de [total] registros"):
                style "nb_texto"
                id "notebook_progresso"

            viewport:
                style_prefix "nb"
                id "notebook_lista"
                ysize 680
                xfill True
                mousewheel True
                draggable True
                pagekeys True
                scrollbars "vertical"
                vscrollbar_unscrollable "hide"

                vbox:
                    spacing 14
                    xsize 1360

                    if not dados:
                        text _("Esta rota ainda não tem registros.") style "nb_texto"

                    for rec, ok in dados:
                        frame:
                            style "nb_cartao"
                            vbox:
                                spacing 8
                                if ok:
                                    text (__(rec["title"]) + __(" · registrado")):
                                        style "nb_texto"
                                        color gui.accent_color
                                        bold True
                                        size (tam_texto + 2)
                                    text rec["text"] style "nb_texto" size tam_texto xmaximum 1300
                                else:
                                    text (__(rec["title"]) + __(" · pendente")):
                                        style "nb_texto"
                                        color "#c0c8d0"
                                        bold True
                                        size (tam_texto + 2)
                                    text _("Continue a história para registrar este conteúdo.") style "nb_texto" color "#c0c8d0" size tam_texto

            text _("Role com a roda do mouse ou Page Up / Page Down."):
                style "nb_dica"
