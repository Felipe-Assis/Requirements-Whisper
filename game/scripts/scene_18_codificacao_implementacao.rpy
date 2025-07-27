label scene_18_codificacao_implementacao:
    play music music_office_concentrated_1 fadein 1.0
    scene bg escritorio_interior_manha
    with dissolve

    $ advance_minutes(14)
    play sound "audio/teclado.ogg"
    "{i}O dia começa com a equipe focada: hoje é o grande momento da codificação.{/i}"
    "{i}Você se senta ao lado de [NOME_DEVELOPER_CODING] e [NOME_DEVELOPER_TEST]. Ambos já estão imersos no projeto.{/i}"

    show developer_coding serious at left_zoom
    show developer_test enthusiastic at right_zoom

    developer_coding "Vamos direto ao ponto, [player_name]. Aqui o código precisa ser limpo, eficiente e seguro. Nada de 'gambiarra' ou copia e cola!"
    hide developer_test
    show developer_test confident at right_zoom
    developer_test "Qualquer coisa, já me chama — quero testar cada pedaço assim que ficar pronto!"

    # Placeholder de UI: Exibe tela de cadastro de paciente após início da codificação
    show expression "images/ui/placeholder_cadastro_paciente.png" as tela_ui at center_zoom
    "{i}Você revisa o layout da tela de cadastro de paciente, planejando cada campo e interação conforme os requisitos levantados. Essa interface será seu desafio do dia!{/i}"
    hide tela_ui
    pause 0.8

    # Mini-game: Escolha de abordagem técnica
    "{i}Você recebe a tarefa de implementar o cadastro de pacientes. Há algumas formas diferentes de resolver o problema. Como você prefere abordar?{/i}"

    $ tempo_gasto = 0
    $ bugs_detectados = 0
    $ feedback_coding = ""
    $ finalizou_no_escritorio = False

    menu:
        "Escolha sua abordagem:"
        "Implementar rápido, mas sem muitos comentários e testes.":
            $ tempo_gasto += 2
            $ bugs_detectados += 2
            $ feedback_coding = "Desempenho foi bom, mas a qualidade deixou a desejar. Prepare-se para corrigir bugs depois!"
            hide developer_coding
            show developer_coding serious at left_zoom
            developer_coding "Esse código tá rodando, mas falta clareza. Se eu não entender, ninguém mais vai!"
            hide developer_test
            show developer_test thinking at right_zoom
            developer_test "Já achei alguns bugs nos testes automatizados. Bora corrigir juntos?"
        "Seguir à risca as boas práticas: testes, documentação, padrão, mas demora mais.":
            $ tempo_gasto += 3
            $ bugs_detectados += 0
            $ feedback_coding = "Trabalho impecável, mas demorou além do previsto. O prazo ficou apertado!"
            hide developer_coding
            show developer_coding positive at left_zoom
            developer_coding "Excelente padrão! Esse código serve de exemplo pra equipe toda. Mas cuidado com o relógio, o prazo não perdoa."
            hide developer_test
            show developer_test enthusiastic at right_zoom
            developer_test "Testar código assim é uma alegria. Quase não achei falhas!"
        "Buscar ajuda do time, fazer pair programming por notebook/telefone.":
            $ tempo_gasto += 2
            $ bugs_detectados += 1
            $ feedback_coding = "Colaboração rendeu bons resultados, mas ainda restam detalhes para revisar."
            play sound "audio/cell_vibration.ogg"
            show developer_ai positive at center_zoom
            developer_ai "Se precisar de snippet pra validação de dados ou até automação, te mando agora!"
            show developer_quality thinking at right_zoom2
            developer_quality "Aproveita pra usar o checklist de qualidade! Diminui o risco de bug bobo."
            hide developer_ai
            hide developer_quality
            hide developer_coding
            show developer_coding thinking at left_zoom
            developer_coding "O código ficou bom, mas revise mais uma vez para garantir clareza e padrão."
            hide developer_test
            show developer_test confident at right_zoom
            developer_test "Alguns bugs menores surgiram, mas nada grave. Fique atento!"
        "Tentar uma solução super inovadora, mas mais arriscada e difícil de manter.":
            $ tempo_gasto += 4
            $ bugs_detectados += 2
            $ feedback_coding = "Ideia criativa! Mas o código ficou difícil de entender e corrigir."
            hide developer_coding
            show developer_coding serious at left_zoom
            developer_coding "Inovação é legal, mas aqui precisamos de previsibilidade. Vai ter que explicar essa abordagem para o time todo!"
            hide developer_test
            show developer_test thinking at right_zoom
            developer_test "Detectei falhas inesperadas. Melhor simplificar antes de entregar!"

    # Simulação de avanço do tempo
    if tempo_gasto <= 2:
        "{i}Você termina sua implementação ainda durante a tarde, com tempo para revisar e discutir com a equipe.{/i}"
        $ finalizou_no_escritorio = True
    elif tempo_gasto <= 3:
        "{i}O tempo voa! Quando percebe, já é fim de tarde, mas ainda dá para fazer uma revisão rápida antes do expediente acabar.{/i}"
        $ finalizou_no_escritorio = True
    else:
        "{i}Você se empenha tanto que só percebe quando já anoiteceu no escritório. Não conseguiu terminar tudo a tempo...{/i}"
        $ finalizou_no_escritorio = False

    # Feedback dinâmico com developer_coding e developer_test
    hide developer_coding
    show developer_coding neutral at left_zoom
    developer_coding "[feedback_coding]"
    if bugs_detectados > 0:
        hide developer_test
        show developer_test thinking at right_zoom
        developer_test "Vamos ajustar esses bugs juntos antes de fechar o dia?"
    else:
        hide developer_test
        show developer_test enthusiastic at right_zoom
        developer_test "Perfeito! Com esse código, os testes passaram de primeira!"

    # Placeholder de UI: tela final após revisão
    show expression "images/ui/placeholder_listagem_paciente.png" as tela_ui_final at center_zoom
    "{i}Após os ajustes e revisões, você confere na tela a listagem dos pacientes, já refletindo os dados inseridos — é a confirmação visual do progresso!{/i}"
    hide tela_ui_final
    pause 0.7

    # Decisão: se não finalizou no escritório, ramifica para trabalhar em casa ou terminar no próximo dia
    if not finalizou_no_escritorio:
        play sound "audio/porta_abrindo.ogg"
        scene bg transito_noite
        with fade
        "{i}Já é noite quando você deixa o escritório, cansado(a) e levando o notebook para casa. Ainda falta terminar parte do módulo...{/i}"
        menu:
            "Como prefere lidar com o trabalho restante?"
            "Virar a noite e entregar tudo ainda hoje.":
                "{i}Você trabalha até tarde, mas termina a implementação. No dia seguinte, chega exausto(a), mas orgulhoso(a) do resultado.{/i}"
                $ energia_diaria = 1
            "Deixar para finalizar pela manhã, descansando e evitando erros por cansaço.":
                "{i}Você prioriza o descanso, acordando cedo para revisar com calma no escritório. Chega mais disposto(a) para encarar os testes finais.{/i}"
                call scene_18_2_codificacao_final from _scene_18_2_codificacao_final
                return

    # Feedback positivo extra de outros NPCs, caso termine no escritório
    if finalizou_no_escritorio:
        show developer_quality positive at right_zoom
        developer_quality "Ótimo trabalho, [player_name]! Código limpo e bem testado é sinal de equipe madura."
        hide developer_quality
        show developer_ai enthusiastic at center_zoom
        developer_ai "Se quiser automatizar build e deploy, me chama! Podemos otimizar o processo juntos."
        hide developer_ai

    "{i}Você percebe como cada escolha de implementação influencia não só o produto final, mas todo o andamento do projeto — inclusive sua rotina, saúde e a relação com os colegas.{/i}"

    # Estatísticas/mini ranking do dia
    "{i}Resumo da codificação:{/i}"
    "{i}• Tempo gasto: [tempo_gasto] unidades{/i}"
    "{i}• Bugs detectados: [bugs_detectados]{/i}"
    if bugs_detectados == 0:
        "{i}• Parabéns! Ganhou o selo 'Código sem Bugs' no inventário.{/i}"
        $ inventario.append("selo_codigo_sem_bugs")

    play sound "audio/feedback_positive.ogg"
    scene bg escritorio_interior_noite
    with fade
    $ advance_minutes(21)
    "{i}O expediente termina com aquele misto de alívio e aprendizado. Você está se tornando cada vez mais profissional e preparado(a) para os próximos desafios.{/i}"

    play music music_home_reflecting fadein 1.3
    scene bg quarto_noite
    with fade
    $ advance_minutes(17)
    "{i}Em casa, você relembra como aplicar conceitos avançados de programação, testabilidade e boas práticas mudou o resultado do projeto.{/i}"
    "{i}A teoria da faculdade, finalmente, faz sentido na prática.{/i}"

    window hide
    pause 1.1
    window show

    "{i}Fim da Semana 6\n\nAprendizado: Conceitos avançados de programação e atenção à qualidade tornam o desenvolvimento mais eficiente e menos estressante. Aplicar teoria na prática transforma desafios em crescimento real.{/i}"

    return
