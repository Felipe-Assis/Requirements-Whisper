label scene_13_retorno_casa_sem3:
    play music music_streets_focused fadein 1.0
    scene bg transito_noite
    with dissolve

    $ advance_minutes(32)
    "{i}Mais um fim de tarde. O ônibus está cheio, mas você encontra um assento e coloca os fones de ouvido, olhando as luzes da cidade.{/i}"
    "{i}A cabeça ainda gira com as revisões feitas na especificação dos requisitos, as dicas dos colegas e as pequenas conquistas do dia.{/i}"

    play music music_home_reflecting fadein 1.5
    scene bg quarto_noite
    with fade
    $ advance_minutes(20)

    "{i}De volta ao seu quarto, você larga a mochila e liga o notebook para revisar o documento finalizado durante o expediente.{/i}"
    show expression "images/items/notebook.png" as notebook at center_zoom
    pause 0.6

    "Ao reler cada item, você lembra de uma conversa recente com [NOME_DEVELOPER_QUALITY]:"
    window hide
    pause 0.8
    window show

    "\"Requisito bom não é só texto bonito, é clareza para todo mundo. Se o tester e o programador entendem igual, já ganhou metade da batalha!\""

    "Você aproveita para anotar algumas dicas práticas que ouviu hoje:"
    window hide
    pause 0.7
    window show

    "• Use sempre verbos no infinitivo nos requisitos (ex: 'Permitir cadastro de paciente')\n• Critérios de aceitação devem ser objetivos e fáceis de testar\n• Prefira frases curtas e sem ambiguidade\n• Separe o que é necessidade real do usuário de opiniões ou desejos"

    "Abre seu aplicativo de notas e compara com o material da disciplina de Engenharia de Software. Um trecho chama a atenção:"
    window hide
    pause 0.7
    window show

    "*‘Documentação não serve só para auditar ou apresentar: ela é memória coletiva, base para testes e para evoluir o sistema sem medo no futuro.’*"

    "{i}Você reflete sobre como a prática do projeto faz tudo aquilo fazer sentido — e que, por mais que documentar pareça trabalhoso, é o que torna o desenvolvimento possível em equipe.{/i}"

    "{i}Antes de dormir, recebe uma mensagem rápida do grupo da equipe:{/i}"
    play sound "audio/cell_vibration.ogg"
    show developer_requirements positive at left_zoom
    developer_requirements "(mensagem no grupo) Pessoal, parabéns pelo empenho hoje! Documento ficou ótimo. Amanhã, seguimos para a próxima etapa juntos!"
    hide developer_requirements

    play music music_home_dreamy fadein 1.0
    scene black
    with fade
    window hide
    pause 1.1
    window show

    "Fim da Semana 3\n\nAprendizado: A clareza na documentação é o elo entre a teoria da engenharia de software e a eficiência da equipe. Especificar bem hoje é evitar retrabalho e garantir qualidade amanhã."

    return
