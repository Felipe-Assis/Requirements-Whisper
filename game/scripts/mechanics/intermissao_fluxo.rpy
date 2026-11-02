# intermissao_fluxo.rpy
# -------------------------------
# FLUXO DO TEMPO LIVRE: im_intermissao, im_executar, deslocamento, ponto de
# parada, pista_lembrar e as falas genéricas
# -------------------------------
# Lógica e dados em logic/intermissao.rpy; telas em mapa_screen.rpy.
#
# Nas cenas (etapa de conteúdo, E5):
#   call im_intermissao(3) from _im_startup_s3      # tempo livre da semana 3
#   call im_ponto_parada(3) from _pp_startup_s3     # depois do cartão "Fim da Semana 3"
#   call pista_lembrar("st_p_tunel") from _pl_st13  # antes de um menu pedagógico
#   menu:
#       "Opção que já existe":
#           ...
#       "Contar o que você viu" (tipo="pista") if pista_tem("st_p_retencao"):
#           $ pista_usar("st_p_retencao")
#
# Conteúdo das ações: labels com nome por convenção (ver im_label_conteudo).
# Eles rodam sobre o fundo do local, podem ler im_op (a opção escolhida),
# im_semana_atual e energia_cansaco(), e terminam com return. Não aplicam
# recompensa: o motor faz isso depois.

label im_intermissao(semana):
    if not im_dados(semana):
        $ renpy.log("im_intermissao: rota %s sem dados da semana %s" % (current_route(), semana))
        return
    $ renpy.dynamic("im_musica_antes")
    $ im_musica_antes = renpy.music.get_playing()
    $ im_iniciar(semana)
    if persistent.im_pular:
        $ im_pular(semana)
        $ im_encerrar(semana)
        return
    $ im_tocar_musica()
    call screen im_abertura_cartao(semana)
    if _return == "pular":
        $ im_pular(semana)
        $ im_encerrar(semana)
        $ im_restaurar_musica(im_musica_antes)
        return
    call expression im_label_abertura(semana) from _im_abertura_conteudo
    $ im_avisar_novos(semana)

label .mapa:
    if not im_opcoes(semana):
        jump .fim
    call screen im_mapa(semana)
    if _return == "encerrar":
        $ im_encerrar_cedo(semana)
        call im_ir_para_casa from _im_ir_para_casa
        jump .fim
    call im_executar(semana, _return) from _im_executar_acao
    jump .mapa

label .fim:
    call screen im_resumo(semana)
    $ im_encerrar(semana)
    $ im_restaurar_musica(im_musica_antes)
    return


label im_executar(semana, valor):
    # Deslocamento (tempo e transição), custo da ação, conteúdo e recompensa.
    $ renpy.dynamic("im_op")
    $ im_op = im_preparar(semana, valor)
    if im_op is None:
        return
    call im_deslocar(im_op) from _im_deslocar_acao
    $ im_pagar_acao(im_op)
    $ im_mostrar_local(im_op)
    call expression im_label_conteudo(im_op) from _im_conteudo_acao
    $ im_aplicar_recompensa(im_op)
    return


label im_deslocar(op):
    # O marcador anda no mapa (~1 s), depois a tela de transição (1-2 s) com
    # som e relógio correndo (mapa-cidade.md §7). Clique, Enter ou Espaço
    # pulam. Com "Transições: desligadas": sem caminhada nem imagem, só um
    # cartão de texto de 1 s.
    $ renpy.dynamic("im_desl")
    $ im_desl = im_deslocamento_info(op)
    if im_desl is None:
        return
    call im_trajeto_telas(im_desl) from _im_trajeto_telas_acao
    $ im_pagar_deslocamento(op, im_desl)
    $ im_tocar_som(im_desl["som_chegada"])
    return


label im_ir_para_casa:
    # "Encerrar o tempo livre" = ir para casa: mesma sequência, sem cobrar
    # minutos (o tempo livre acabou), com a porta no fim.
    $ renpy.dynamic("im_desl")
    $ im_desl = im_deslocamento_casa_info()
    if im_desl is None:
        return
    call im_trajeto_telas(im_desl) from _im_trajeto_telas_casa
    $ im_tocar_som(im_desl["som_chegada"])
    return


label im_trajeto_telas(desl):
    # Caminhada do marcador e tela do meio (som com fade de 0,2 s), ou o
    # cartão de texto com as transições desligadas.
    if im_transicoes_ligadas():
        if desl["marcador"]:
            $ IM_DIAG.telas.append("deslocamento")
            call screen im_deslocamento(im_semana_atual, desl)
        if desl["tela"]:
            $ IM_DIAG.telas.append("transicao")
            $ im_tocar_som(desl["som"], desl["volume"], 0.2)
            call screen im_transicao(desl)
            $ renpy.sound.stop(fadeout=0.2)
    elif desl["tela"]:
        $ IM_DIAG.telas.append("cartao")
        call screen im_transicao(desl, cartao=True)
    return


label im_ponto_parada(semana):
    # Fim de cada semana (1 a 7): autosave, nome do save e a tela com o
    # resumo e os botões Continuar / Salvar / Voltar ao menu.
    $ renpy.dynamic("im_parada_novos")
    $ im_parada_novos = im_parada_preparar(semana)
    $ renpy.force_autosave()
    call screen im_parada(semana, im_parada_novos)
    return


label pista_lembrar(pid):
    # Formato 1 (§3.3): antes de um menu pedagógico. Sem a pista (ou já
    # usada), não mostra nada. O menu seguinte não muda.
    if not pista_disponivel(pid):
        return
    $ renpy.dynamic("pl_titulo", "pl_texto")
    $ pl_titulo = pista_dados(pid)["titulo"]
    $ pl_texto = pista_dados(pid)["texto"]
    menu:
        "Lembrar: [pl_titulo!t]" (tipo="pista"):
            $ pista_usar(pid)
            "{i}[pl_texto!t]{/i}"
        "Seguir sem lembrar" (tipo="pista"):
            pass
    return


# -------------------------------
# Falas genéricas: usadas quando o label de conteúdo ainda não existe.
# O nome que faltou vai para o log e para IM_DIAG.genericos.
# -------------------------------
label im_generico_abertura:
    if im_semana_atual == 1:
        "{i}Tempo livre. No mapa, cada lugar mostra quem está lá e o que dá para fazer. Toda ação custa minutos, e o tempo não cobre tudo: escolher também é deixar algo de fora.{/i}"
        "{i}Ajudar, observar e estudar cansam; descansar recupera. Nada aqui é obrigatório para aprender: é o seu tempo.{/i}"
    elif energia_cansaco():
        "{i}A semana pesou. Hoje o tempo livre é mais curto.{/i}"
    return

label im_generico_conversar:
    $ renpy.say(None, im_fala_generica(im_op))
    $ renpy.dynamic("im_g_fala")
    $ im_g_fala = im_fala_offline(im_op["alvo"])
    if im_g_fala:
        $ renpy.say(im_g_fala[0], im_g_fala[1])
    return

label im_generico_observar:
    $ renpy.say(None, im_fala_generica(im_op))
    return

label im_generico_estudar:
    $ renpy.say(None, im_fala_generica(im_op))
    return

label im_generico_descansar:
    $ renpy.say(None, im_fala_generica(im_op))
    return

label im_generico_ajudar:
    $ renpy.say(None, im_fala_generica(im_op))
    return

label im_generico_mentoria:
    $ renpy.say(None, im_fala_generica(im_op))
    return
