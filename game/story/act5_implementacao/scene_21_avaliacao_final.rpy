label scene_21_avaliacao_final:
    $ disponivel_developer_ai = False
    $ disponivel_developer_coding = False
    $ disponivel_developer_management = False
    $ disponivel_developer_requirements = False
    $ disponivel_developer_project = False
    $ disponivel_developer_quality = False
    $ disponivel_developer_security = False
    $ disponivel_developer_test = False
    $ disponivel_doutora_1 = False
    $ disponivel_doutora_2 = False

    play music music_home_reflecting fadein 1.0
    # Transição: Manhã no escritório
    scene bg escritorio_interior_manha
    with fade

    $ advance_minutes(12)
    "{i}O último dia começa. O escritório está mais silencioso que o normal; todos preparam documentos e apresentações para o grande encontro de entrega.{/i}"

    show developer_management serious at left_zoom
    developer_management "Pessoal, caprichem na apresentação. É nossa chance de mostrar o valor do nosso trabalho ao Instituto!"

    "Você confere os slides, o protótipo rodando e revisa as anotações no notebook."

    # Transição: trajeto até o instituto
    scene bg transito_tarde
    with dissolve
    play sound "audio/effects/bus.ogg"
    "{i}Após o almoço, a equipe pega o ônibus rumo ao Instituto. O trânsito do Rio de Janeiro, como sempre, é imprevisível. Todos revisam mentalmente os pontos principais da apresentação.{/i}"

    # Chegada ao Instituto
    scene bg fachada_instituto_tarde
    with fade
    play sound "audio/effects/passos.ogg"
    "{i}Você desce do ônibus e segue com o grupo até a sala de reuniões do Instituto, sentindo a responsabilidade pesar — e o orgulho também.{/i}"

    # Sala de reunião: início da apresentação
    scene bg escritorio_medica
    with dissolve

    show developer_requirements enthusiastic at left_zoom
    developer_requirements "Sejam bem-vindos! Dr. Almeida e Enfermeira Marta estão aguardando. Respirem fundo — vocês estão prontos!"

    show doutora_1 portrait at right_zoom
    show doutora_2 portrait at right_zoom2

    "{i}A equipe se organiza. Você apresenta o sistema, mostrando as principais funcionalidades, relatórios, telas e os diferenciais do projeto. Os stakeholders acompanham atentos.{/i}"

    # Avaliação dos finais — sistema de pontuação/amizade
    $ amizade_total = amizade_developer_test + amizade_developer_coding + amizade_developer_management + amizade_developer_requirements + amizade_developer_ai + amizade_developer_quality + amizade_developer_project + amizade_developer_security

    if amizade_total >= 40 and "selo_codigo_sem_bugs" in inventario and "conquista_bug_vuln" in inventario:
        $ final_grade = "excelente"
    elif amizade_total >= 30:
        $ final_grade = "bom"
    else:
        $ final_grade = "ok"

    # Apresentação: decisões técnicas e flags
    if "docker" in inventario or "badge_devops" in inventario:
        "Você destaca a adoção de novas tecnologias que facilitam o uso e a manutenção do sistema, mesmo que explique de maneira simples para os presentes."
        $ resultado_tech = "DevOps"
    elif "badge_team_work" in inventario:
        "Você valoriza o trabalho em equipe, destacando que todos colaboraram para o projeto funcionar para quem realmente usa no dia a dia."
        $ resultado_tech = "Teamwork"
    else:
        "Você enfatiza como ouvir os usuários e testar junto fez toda diferença na construção do sistema."
        $ resultado_tech = "Padrao"

    # Stakeholders avaliam (final alternativo)
    show doutora_1 neutral at right_zoom
    doutora_1 "Fiquei muito satisfeita com o resultado! O sistema está fácil de usar, não precisei de manual pra achar o que eu queria. É uma grande mudança para a nossa rotina."
    show doutora_2 neutral at right_zoom2
    doutora_2 "De verdade, adorei o jeito que vocês deixaram tudo claro e simples. Preencher os dados do paciente ficou bem menos cansativo."

    # Comentários das médicas mais humanos e de rotina
    doutora_1 "Gostei que agora consigo ver os dados dos pacientes de forma rápida, sem ter que ficar abrindo várias telas. Isso vai me ajudar muito nos plantões corridos."
    doutora_2 "As notificações de retorno e de exames pendentes vão fazer diferença. Antes eu vivia esquecendo algum acompanhamento, agora recebo o aviso certinho."

    doutora_1 "Agradeço por terem paciência em ouvir nossas reclamações e sugestões. Em outros projetos, ninguém parava para perguntar o que era realmente importante para a gente."
    doutora_2 "Eu senti que nossas opiniões foram levadas a sério. Isso faz a gente se sentir parte do projeto também!"

    if resultado_tech == "DevOps":
        doutora_1 "Se vocês dizem que agora fica mais fácil pra atualizar, melhor ainda! Só não me deixem sem sistema justo no plantão, hein?"
        doutora_2 "Eu só quero continuar usando, do jeito que está, sem travar! (risos)"
    elif resultado_tech == "Teamwork":
        doutora_2 "Dá pra ver que vocês trabalharam juntos mesmo. Todo mundo ficou envolvido, e isso deixa o sistema com a cara do nosso Instituto."
        doutora_1 "Quando a equipe conversa de verdade com a gente, todo mundo ganha."
    else:
        doutora_2 "Gostei de ver que vocês testaram bastante com a gente, ficou claro no resultado. Ficou bem menos confuso que o sistema antigo."
        doutora_1 "Organização e escuta são as melhores partes desse projeto."

    # Feedback/ajustes sem termos técnicos
    if final_grade == "excelente":
        doutora_2 "Usei o sistema com pacientes de verdade e tudo funcionou. Está estável, não travou nenhuma vez!"
        doutora_1 "Fico tranquila em passar o sistema para as outras colegas."
        doutora_2 "Espero que possamos usar por muito tempo!"
    elif final_grade == "bom":
        doutora_2 "Está ótimo, só peço pra ajustar uns detalhes. Tem alguns campos que ainda geram dúvida, mas dá pra ir melhorando aos poucos."
        doutora_1 "O importante é que ficou bem melhor que o anterior. O resto a gente vai ajustando juntos!"
    else:
        doutora_2 "Sei que é difícil, mas algumas telas ainda me confundem um pouco. Mas agradeço o empenho, ficou muito melhor do que antes."
        doutora_1 "Conto com vocês para ir melhorando, porque já fez muita diferença na rotina!"

    # Lista de melhorias — agora na voz do narrador (não das doutoras)
    if final_grade != "excelente":
        "{i}Durante a avaliação, surgem algumas sugestões de melhoria na experiência:{/i}"
        "{i}• Permitir que alguns campos sejam mais flexíveis para o preenchimento (ex: profissão, escolaridade){/i}"
        "{i}• Destacar melhor o que precisa ser preenchido obrigatório{/i}"
        "{i}• Facilitar o fluxo de registro para não perder tempo pulando de tela{/i}"
        "{i}• Ajustar detalhes de botões para não confundir na hora de salvar ou cancelar informações{/i}"
        "{i}• Retirar informações desnecessárias ou que ninguém usa{/i}"

    # Encerramento afetuoso
    doutora_1 "Gostaríamos muito de continuar contando com vocês. Foi uma experiência muito boa para o Instituto."
    doutora_2 "A gente sente que agora, finalmente, fizeram um sistema para quem cuida de gente, não só para preencher papel."

    show developer_requirements positive at left_zoom
    developer_requirements "Fico feliz demais pelo reconhecimento. Parabéns, [player_name] — seu desenvolvimento ficou claro do início ao fim."

    # Mini feedback da equipe
    show developer_coding positive at left_zoom_2
    developer_coding "Mandou bem! Que venha o próximo desafio!"
    show developer_test positive at center_zoom
    developer_test "Que orgulho do time. Fomos além de bugs e entregamos valor!"

    # Final especial se amizade total máxima
    if amizade_total >= 50:
        hide developer_test
        show developer_management enthusiastic at center_zoom
        developer_management "Orgulho de ver como você evoluiu como profissional e colega. O time é a prova de que colaboração faz a diferença!"
        hide developer_management

    # Padding: clima de celebração e encerramento da reunião
    play sound "audio/effects/aplausos.ogg"
    "{i}A reunião termina em clima de vitória. Fotos, abraços, contatos trocados — e a certeza de que o semestre foi transformador.{/i}"

    # Reflexão e aprendizado final
    "{i}No ônibus, a cidade passa pela janela. Você pensa em tudo que viveu: erros, acertos, amizades, superações, aprendizado e, principalmente, confiança em si mesmo.{/i}"

    scene bg quarto_noite
    with dissolve
    "{i}De volta ao quarto, fecha o notebook e sente um misto de alívio, orgulho e vontade de recomeçar — já imaginando o próximo projeto.{/i}"

    window hide
    pause 1.1
    window show

    "{i}Fim da Semana 8 — Projeto entregue, ciclo concluído.{/i}"
    "{i}Você percebeu que a prática consolidou tudo que aprendeu na universidade, e que está pronto(a) para os próximos desafios.{/i}"
    "{i}Lembre-se: na Engenharia de Software, aprender com o time, ouvir o usuário e revisar cada detalhe são diferenciais para qualquer projeto de sucesso.{/i}"

    return
