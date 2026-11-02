# rastreabilidade_dados.rpy
# -------------------------------
# DADOS DO QUADRO DE RASTREABILIDADE (um quadro por rota)
# -------------------------------
# Conteúdo dos documentos de design de rota (docs/design/intermissoes-*.md,
# seções de rastreabilidade). Formato (docs/design/sistemas-intermissoes.md, 5.2):
#   "requisitos": [{"id", "texto"}]; "testes": [{"id", "texto"}];
#   "criterios": [{"id", "de": requisito certo, "teste": teste certo ou None
#       (só na lacuna), "texto", "dica"/"explica" (opcional: explicação quando
#       a ligação está errada)}];
#   "lacuna": id do critério sem teste; "explica_lacuna": por que é lacuna
#       (só aparece no relatório, nunca no quadro);
#   "lembrar" (opcional): texto de rast_lembrar numa cena posterior.
# Mecânica: scripts/mechanics/rastreabilidade.rpy. init 3: ROUTES nasce em init 1.

init 3 python:
    ROUTES["saude"]["rastreabilidade"] = {
        "saude_rast_acesso": {
            "requisitos": [
                {"id": "R1", "texto": _("RF02: O sistema salva o histórico de saúde durante o preenchimento e recupera o rascunho se a conexão cair.")},
                {"id": "R2", "texto": _("RF05A: O sistema calcula os escores da escala HAD e, quando falta resposta, avisa e salva o preenchimento parcial.")},
                {"id": "R3", "texto": _("SEG01: Cada perfil vê só o que precisa: a recepção cuida de agenda e cadastro; o histórico de saúde é da equipe clínica. Toda alteração no histórico registra quem, quando e o valor anterior.")},
            ],
            "criterios": [
                {"id": "C1", "de": "R1", "teste": "T1", "texto": _("Dado um histórico com três campos preenchidos, quando a conexão cai e volta, então os três campos continuam lá.")},
                {"id": "C2", "de": "R2", "teste": "T2", "texto": _("Dadas as 14 respostas da HAD, quando a médica conclui, então o sistema mostra os escores de ansiedade e de depressão, de 0 a 21 cada.")},
                {"id": "C3", "de": "R3", "teste": None, "texto": _("Dado o perfil recepção, quando abre o histórico de saúde de um paciente, então o acesso é negado.")},
                {"id": "C4", "de": "R2", "teste": "T3", "texto": _("Dadas 12 das 14 respostas, quando a médica tenta concluir, então o sistema mostra quais faltam e salva como parcial.")},
                {"id": "C5", "de": "R3", "teste": "T4", "texto": _("Dada uma médica que altera a carga tabágica, então a trilha registra quem alterou, a hora e o valor anterior.")},
            ],
            "testes": [
                {"id": "T1", "texto": _("teste_autosave_queda_conexao")},
                {"id": "T2", "texto": _("teste_had_escore_completo")},
                {"id": "T3", "texto": _("teste_had_resposta_faltando")},
                {"id": "T4", "texto": _("teste_trilha_alteracao_historico")},
            ],
            "lacuna": "C3",
            "explica_lacuna": _("Nenhum teste confere que a recepção não abre o histórico de saúde. O teste da trilha registra quem alterou; não impede quem não devia ver."),
        },
    }

    ROUTES["startup"]["rastreabilidade"] = {
        "st_rast_exclusao": {
            "requisitos": [
                {"id": "R1", "texto": _("A pessoa exclui um gasto lançado por engano, com confirmação.")},
                {"id": "R2", "texto": _("O total do mês reflete todos os gastos sincronizados.")},
                {"id": "R3", "texto": _("Um gasto reenviado não é gravado duas vezes.")},
            ],
            "criterios": [
                {"id": "C1", "de": "R1", "teste": "T1",
                 "texto": _("Dado um total de R$ 100 com um almoço de R$ 20, quando a pessoa confirma a exclusão, então o almoço sai da lista e o total passa a R$ 80."),
                 "dica": _("Confirmar a exclusão: veio do pedido de excluir com confirmação, e um teste confere a exclusão confirmada.")},
                {"id": "C2", "de": "R1", "teste": "T2",
                 "texto": _("Dado o mesmo total, quando a pessoa toca em Excluir e depois em Cancelar, então o almoço continua na lista e o total continua R$ 100."),
                 "dica": _("Cancelar também é parte da exclusão com confirmação. Procure o teste do caminho de cancelar.")},
                {"id": "C3", "de": "R3", "teste": "T3",
                 "texto": _("Dado um café de R$ 5 com o id A1, quando o mesmo pedido chega duas vezes ao servidor, então só um café é gravado."),
                 "dica": _("É o caso do túnel: reenvio. O teste é o que o Davi acrescentou depois do review.")},
                {"id": "C4", "de": "R2", "teste": None,
                 "texto": _("Dado um bandejão de R$ 4,50 lançado sem internet, quando a sincronização termina, então o total mostra o novo valor sem reabrir a tela.")},
                {"id": "C5", "de": "R2", "teste": "T4",
                 "texto": _("Dado R$ 100 no mês, quando a pessoa lança R$ 5 com internet, então o total vai para R$ 105."),
                 "dica": _("Fala do total, com internet. Qual teste confere o total online?")},
            ],
            "testes": [
                {"id": "T1", "texto": _("teste_excluir_confirmado")},
                {"id": "T2", "texto": _("teste_excluir_cancelado")},
                {"id": "T3", "texto": _("teste_sync_idempotente")},
                {"id": "T4", "texto": _("teste_total_online")},
            ],
            "lacuna": "C4",
            "explica_lacuna": _("Nenhum teste cobre o total depois da sincronização offline."),
        },
    }

    ROUTES["corporativo"]["rastreabilidade"] = {
        "co_rast_farol": {
            "requisitos": [
                {"id": "RF-01", "texto": _("O solicitante consulta o próprio chamado pelo número e vê estado, atendente e solução.")},
                {"id": "RF-03", "texto": _("O chamado só vai para Resolvido com a solução descrita.")},
                {"id": "RN-07", "texto": _("Chamados de Reset de senha sem retorno em 72 h são resolvidos pela rotina com a descrição padrão, e a trilha registra 'sistema'.")},
                {"id": "RF-05", "texto": _("O solicitante reabre um chamado resolvido informando o motivo; a solução anterior fica no histórico.")},
                {"id": "RF-06", "texto": _("Cada perfil só faz o que a matriz de permissões permite; toda tentativa negada vai para a trilha.")},
            ],
            "criterios": [
                {"id": "C1", "de": "RF-01", "teste": "T1",
                 "texto": _("Dado o chamado 48213 Resolvido com solução registrada, quando o solicitante o consulta pelo número, então vê Resolvido, o nome do atendente e o texto da solução."),
                 "explica": _("C1 descreve o que a consulta mostra: vem do RF-01. O T1 abre o 48213 e confere os três campos.")},
                {"id": "C2", "de": "RF-03", "teste": "T2",
                 "texto": _("Dado um chamado Em atendimento, quando o atendente tenta resolver com a descrição só com espaços, então o chamado continua Em atendimento e a tela orienta o preenchimento."),
                 "explica": _("C2 é o bloqueio da descrição vazia (RF-03), no caso que o Jorge apontou. O T2 tem o nome desse comportamento.")},
                {"id": "C3", "de": "RN-07", "teste": "T3",
                 "texto": _("Dado um chamado de Reset de senha sem retorno há 72 h, quando a rotina roda, então ele vai para Resolvido com a descrição padrão e a trilha registra o autor 'sistema'."),
                 "explica": _("C3 é a regra herdada da rotina (RN-07), não o bloqueio. O T3 é o teste de caracterização da rotina.")},
                {"id": "C4", "de": "RF-05", "teste": "T4",
                 "texto": _("Dado um chamado Resolvido, quando o solicitante reabre informando o motivo, então o chamado volta a Em atendimento e a solução anterior fica no histórico."),
                 "explica": _("C4 é a reabertura (RF-05). O T4 confere o estado e o histórico.")},
                {"id": "C5", "de": "RF-06", "teste": "T5",
                 "texto": _("Dado um solicitante, quando tenta consultar o chamado de outra pessoa, então recebe acesso negado e a tentativa vai para a trilha."),
                 "explica": _("C5 fala de quem é impedido, não do que a consulta mostra: vem dos perfis (RF-06). O T5 tenta e espera a negativa.")},
                {"id": "C6", "de": "RF-06", "teste": None,
                 "texto": _("Dado um atendente, quando abre pela URL a reabertura de chamado de outro setor, então recebe acesso negado e a tentativa vai para a trilha."),
                 "explica": _("C6 vem dos perfis (RF-06).")},   # a parte do teste nunca é explicada (lacuna)
            ],
            "testes": [
                {"id": "T1", "texto": _("teste_consulta_mostra_estado_atendente_e_solucao")},
                {"id": "T2", "texto": _("teste_resolver_so_com_espacos_mantem_em_atendimento")},
                {"id": "T3", "texto": _("teste_rotina_72h_grava_descricao_padrao_e_autor_sistema")},
                {"id": "T4", "texto": _("teste_reabrir_com_motivo_preserva_solucao_anterior")},
                {"id": "T5", "texto": _("teste_solicitante_chamado_de_outro_acesso_negado")},
                {"id": "T6", "texto": _("teste_atendente_nao_ve_botao_reabrir_de_outro_setor")},   # isca: confere a tela, não o acesso
            ],
            "lacuna": "C6",
            "explica_lacuna": _("Nenhum teste tenta a reabertura pela URL com o perfil atendente. O T6 só confere que o botão some da tela."),
            "lembrar": _("No quadro da semana passada, o critério do atendente que abre pela URL a reabertura de outro setor estava sem teste. Você marcou, e o Kauã escreveu o teste."),
        },
    }
