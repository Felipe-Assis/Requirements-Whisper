label scene_epilogo_conquistas_final:
    scene bg tela_conquistas
    with fade

    "Parabéns, [player_name]! Você concluiu o ciclo do projeto e deixou sua marca como engenheiro(a) de software."

    # Resumo da rota jogada (tela resumo_rota, no fim deste arquivo).
    call screen resumo_rota

#     # Tela de conquistas/troféus
#     "Veja algumas das conquistas desbloqueadas ao longo do jogo:"
#
#     if "badge_devops" in inventario:
#         "🏅 DevOps Visionário — Você liderou a adoção de automação, Docker e pipelines modernos!"
#     if "badge_bug_buster" in inventario:
#         "🔎 Caçador(a) de Bugs — Detectou e solucionou bugs críticos sob pressão."
#     if "badge_team_work" in inventario:
#         "🤝 Trabalho em Equipe — Você buscou colaboração nas horas decisivas."
#     if "badge_resiliencia" in inventario:
#         "🛡️ Resiliência — Priorizou segurança, preferindo rollback seguro a deploy apressado."
#     if "selo_codigo_sem_bugs" in inventario:
#         "✅ Código sem Bugs — Seu código passou nos testes sem falhas críticas."
#     if "conquista_bug_vuln" in inventario:
#         "🔐 Segurança de Verdade — Identificou vulnerabilidades e fortaleceu o sistema."
#     if "mindfulness_dev" in inventario:
#         "🧘 Mindfulness Dev — Soube equilibrar saúde, descanso e produtividade."
#     if "badge_pr_transparente" in inventario:
#         "📝 PR Transparente — Explicou suas decisões técnicas de modo claro para toda a equipe."
#     if "badge_demo_colaborativa" in inventario:
#         "🎤 Demo Colaborativa — Apresentou suas soluções e envolveu toda a equipe nas decisões."
#     if "checklist_qualidade" in inventario:
#         "📋 Mestre dos Checklists — Garantiu qualidade do início ao fim."
#
#     "Se não desbloqueou todos os troféus, que tal jogar novamente e buscar caminhos diferentes?"
#
#     window hide
#     pause 1.2
#     window show
#
#     # Depoimentos dos NPCs (personalizados, educativos, curtos)
#     show developer_coding positive at left_zoom
#     developer_coding "Orgulho do seu código, [player_name]! Continue buscando padrões sólidos e clareza."
#     hide developer_coding
#
#     show developer_requirements positive at right_zoom
#     developer_requirements "Ver você evoluir em requisitos e colaboração me inspira. Que venham mais projetos juntos!"
#     hide developer_requirements
#
#     show developer_ai enthusiastic at center_zoom
#     developer_ai "Adorei suas ideias inovadoras! Lembre: criatividade com responsabilidade transforma equipes e sistemas."
#     hide developer_ai
#
#     show developer_quality positive at left_zoom
#     developer_quality "Você mostrou que qualidade é hábito, não exceção. Mantenha esse espírito na sua carreira!"
#     hide developer_quality
#
#     show developer_test enthusiastic at right_zoom
#     developer_test "Aprender testando é o caminho! Espero encontrar seus códigos bem testados por aí."
#     hide developer_test
#
#     show developer_management positive at left_zoom
#     developer_management "Gestão é sobre pessoas e processos — e você mostrou maturidade em ambos. Sucesso!"
#     hide developer_management
#
#     show developer_project thinking at right_zoom
#     developer_project "Documentação, arquitetura, deploy... Você venceu cada etapa. Torcendo pelo seu próximo desafio."
#     hide developer_project
#
#     show developer_security positive at center_zoom
#     developer_security "Você nunca esqueceu da segurança. O mundo precisa de devs assim. Parabéns!"
#     hide developer_security

    # Reflexão final do protagonista e sugestão de replay
    scene bg quarto_noite
    with fade
    "Você sente orgulho de sua jornada, das amizades e de tudo que construiu — mas sabe que sempre há espaço para crescer."

    "Cada escolha levou a um final diferente. Que tal experimentar outros caminhos, focar em outras competências ou explorar alternativas técnicas na próxima vez?"

    "Obrigado por jogar! Continue aprendendo, colaborando e desenvolvendo — dentro e fora dos projetos."

    menu:
        "O que deseja fazer agora?"
        "Jogar novamente (novo ciclo, novos desafios)":
            $ renpy.full_restart()
        "Ver créditos finais":
            jump creditos_finais
        "Encerrar":
            return

label creditos_finais:
    scene bg creditos
    with fade
    "Projeto desenvolvido como Visual Novel Educacional em Engenharia de Software."
    "Roteiro: Felipe Assis| Arte: IA | Programação: Felipe Assis | Personagens e história inspirados em vivências reais."
    "Agradecimentos especiais aos colegas, professores e todos que colaboraram direta ou indiretamente."
    "Obrigado por jogar!"
    return


# -------------------------------
# Resumo da rota jogada
# -------------------------------
# Lê o contrato de logic/learning.rpy: conquistas da rota, registros do
# notebook, decisões (primeira tentativa) e exercícios de escrita.
screen resumo_rota():
    modal True
    zorder 110

    $ empresa = route_data()["empresa"]
    $ conquistas = route_achievements()
    $ obtidas = [a for a in conquistas if achievement_unlocked(a)]
    $ n_obtidas = len(obtidas)
    $ n_conquistas = len(conquistas)
    $ n_reg, total_reg = registros_contagem()
    $ adequadas, com_apoio = resumo_decisoes()
    $ confirmadas, pendentes = resumo_escritas()
    $ tam = 36 if texto_maior_ativo() else 28

    add Solid("#000000b0")

    frame:
        style "nb_painel"
        align (0.5, 0.5)
        xsize 1500
        ysize 960

        vbox:
            spacing 18
            text _("Resumo da sua jornada") style "nb_titulo"
            text _("Empresa: [empresa!t]") style "nb_texto" size tam

            viewport:
                style_prefix "nb"
                id "resumo_lista"
                ysize 640
                xfill True
                mousewheel True
                draggable True
                pagekeys True
                scrollbars "vertical"
                vscrollbar_unscrollable "hide"

                vbox:
                    spacing 14
                    xsize 1360

                    text _("Conquistas: [n_obtidas] de [n_conquistas]") style "nb_texto" size tam color gui.accent_color bold True
                    if obtidas:
                        for a in obtidas:
                            text (__(a["title"]) + " · " + __(a["desc"])) style "nb_texto" size tam xmaximum 1340
                    else:
                        text _("Nenhuma conquista nesta rota. Outros caminhos levam a outras.") style "nb_texto" size tam

                    null height 6
                    text _("Notebook: [n_reg] de [total_reg] registros") style "nb_texto" size tam color gui.accent_color bold True id "resumo_registros"

                    null height 6
                    text _("Decisões com feedback") style "nb_texto" size tam color gui.accent_color bold True
                    if adequadas or com_apoio:
                        text _("Adequadas na primeira tentativa, sem apoio: [adequadas]") style "nb_texto" size tam
                        text _("Ajustadas depois de uma revisão orientada: [com_apoio]") style "nb_texto" size tam
                    else:
                        text _("Nenhuma decisão com feedback registrada nesta rota.") style "nb_texto" size tam

                    null height 6
                    text _("Exercícios de escrita") style "nb_texto" size tam color gui.accent_color bold True
                    text _("Confirmados por você: [confirmadas] · Pendentes: [pendentes]") style "nb_texto" size tam

                    null height 12
                    text _("Este resumo descreve o que aconteceu no jogo. Ele não certifica domínio de engenharia de software: escolher bem aqui não substitui a prática com pessoas reais, a revisão da equipe e o retorno de quem usa o sistema."):
                        style "nb_texto"
                        size tam
                        color "#cccccc"
                        xmaximum 1340

            textbutton _("Continuar"):
                style "nb_botao"
                xalign 1.0
                id "resumo_continuar"
                default_focus True
                action Return()
