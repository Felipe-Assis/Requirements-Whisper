# Testes no motor Ren'Py (telas, ações e estado reais). Pasta fora do build
# (build.classify em options.rpy). Para rodar, a partir da raiz do projeto:
#   & "<sdk>\lib\py3-windows-x86_64\python.exe" "<sdk>\renpy.py" "<projeto>" test --savedir "<projeto>/.test-saves" --report-detailed
testsuite global:
    teardown:
        exit


# Labels auxiliares (só existem com a pasta de testes).
label rw_teste_escrita:
    call exercicio_escrita("rw_teste", "Pedido de teste: a pessoa responsável cancela uma reserva e o horário volta a ficar livre.")
    "Fim do teste de escrita."
    return

label rw_teste_planejamento:
    call atividade_planejamento("rw_plano", ["Item A necessário", "Item B necessário", "Item C extra", "Item D extra"], [0, 1])
    "Fim do teste de planejamento."
    return
