label start:
    if user_id is None:
        $ user_id = generate_user_id()
    call scene_1_quarto from _scene_1_quarto
    #call scene_2_escritorio from _scene_2_escritorio
    call scene_3_reuniao_inicial from _scene_3_reuniao_inicial
    call scene_4_retorno_casa from _scene_4_retorno_casa
    call scene_5_preparacao_entrevista from _scene_5_preparacao_entrevista
    call scene_6_entrevista_stakeholders from _scene_6_entrevista_stakeholders
    call scene_7_avaliacao_requisitos from _scene_7_avaliacao_requisitos
    call scene_8_cafe_informal from _scene_8_cafe_informal
    call scene_9_retorno_casa_sem2 from _scene_9_retorno_casa_sem2
    call scene_10_criacao_casos_uso from _scene_10_criacao_casos_uso
    call scene_11_almoco_equipe from _scene_11_almoco_equipe
    call scene_12_especificacao_requisitos from _scene_12_especificacao_requisitos
    call scene_13_retorno_casa_sem3 from _scene_13_retorno_casa_sem3
    call scene_14_discussao_arquitetura from _scene_14_discussao_arquitetura
    call scene_15_aniversario_surpresa from _scene_15_aniversario_surpresa
    call scene_16_reuniao_gerenciamento from _scene_16_reuniao_gerenciamento
    call scene_17_tarde_estudos_tecnicos from _scene_17_tarde_estudos_tecnicos
    call scene_18_codificacao_implementacao from _scene_18_codificacao_implementacao
    call scene_19_testes_seguranca from _scene_19_testes_seguranca
    call scene_20_deploy_final from _scene_20_deploy_final
    call scene_21_avaliacao_final from _scene_21_avaliacao_final
    call scene_epilogo_conquistas_final from _scene_epilogo_conquistas_final

    "Fim do jogo!"
