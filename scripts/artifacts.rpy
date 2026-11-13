# O jogo mantém sua moldura; cada atividade abre um artefato legível por dentro.
style artifact_paper is frame:
    background Solid("#f4f0e6")
    padding (22, 18)

style artifact_card is frame:
    background Solid("#ffffff")
    padding (18, 16)

style artifact_ink is lab_body:
    color "#23343b"

style artifact_muted is lab_note:
    color "#52656b"

style artifact_heading is rw_heading:
    color "#1b3039"
    size 30
    bold True

style artifact_note is lab_note:
    color "#8a5623"

style artifact_button is lab_button:
    background Solid("#dce6e5")
    hover_background Solid("#b9d8d2")
    selected_background Solid("#286b66")
    insensitive_background Solid("#e5e9e7")
    padding (18, 12)
    yminimum 60

style artifact_button_text is lab_button_text:
    color "#163b3f"
    hover_color "#102e31"
    selected_color "#ffffff"
    insensitive_color "#657572"

style artifact_primary is artifact_button:
    background Solid("#286b66")
    hover_background Solid("#195750")

style artifact_primary_text is artifact_button_text:
    color "#ffffff"
    hover_color "#ffffff"

screen artifact_bar(title, detail):
    frame:
        background Solid("#dce6e5")
        padding (20, 12)
        xfill True
        vbox:
            spacing 5
            text title style "artifact_heading" size 28
            text detail style "artifact_muted" size 22
