label scene_21_avaliacao_final:
    # Transição: Manhã no escritório
    scene bg escritorio_interior_manha
    with fade

    "O último dia começa. O escritório está mais silencioso que o normal; todos preparam documentos e apresentações para o grande encontro de entrega."

    show developer_management serious at left_zoom
    developer_management "Pessoal, caprichem na apresentação. É nossa chance de mostrar o valor do nosso trabalho ao Instituto!"

    "Você confere os slides, o protótipo rodando e revisa as anotações no notebook."

    # Transição: trajeto até o instituto
    scene bg transito_tarde
    with dissolve
    play sound "audio/onibus.ogg"
    "Após o almoço, a equipe pega o ônibus rumo ao Instituto. O trânsito do Rio de Janeiro, como sempre, é imprevisível. Todos revisam mentalmente os pontos principais da apresentação."

    # Chegada ao Instituto
    scene bg fachada_instituto_tarde
    with fade
    play sound "audio/passos.ogg"
    "Você desce do ônibus e segue com o grupo até a sala de reuniões do Instituto, sentindo a responsabilidade pesar — e o orgulho também."

    # Sala de reunião: início da apresentação
    scene bg sala_reuniao_tarde
    with dissolve

    show developer_requirements enthusiastic at left_zoom
    developer_requirements "Sejam bem-vindos! Dr. Almeida e Enfermeira Marta estão aguardando. Respirem fundo — vocês estão prontos!"

    show expression "images/npcs/dr_almeida.png" as doutora_1 at right_zoom
    show expression "images/npcs/enf_marta.png" as doutora_2 at right_zoom2

    "A equipe se organiza. Você apresenta o sistema, mostrando as principais funcionalidades, relatórios, telas e os diferenciais do projeto. Os stakeholders acompanham atentos."

    # Apresentação: decisões técnicas e flags
    if "docker" in inventario or "badge_devops" in inventario:
        "Você destaca a adoção de Docker e CI/CD, explicando como isso facilita manutenção e escalabilidade."
        $ resultado_tech = "DevOps"
    elif "badge_team_work" in inventario:
        "Destaca o trabalho em equipe na resolução dos desafios, principalmente os bugs de última hora."
        $ resultado_tech = "Teamwork"
    else:
        "Enfatiza a documentação clara, testes e processo colaborativo da equipe."
        $ resultado_tech = "Padrao"

    # Stakeholders avaliam (final alternativo)
    show doutora_1 at right_zoom
    doutora_1 "Fiquei impressionado com o resultado! O sistema está prático e visualmente agradável. Muito obrigado pelo empenho, pessoal."

    if resultado_tech == "DevOps":
        doutora_1 "Adotar automação e práticas modernas como Docker nos dá confiança para crescer no futuro. Ótima visão!"
    elif resultado_tech == "Teamwork":
        doutora_2 "O apoio de todos ficou claro. Gostei de ver a colaboração e preocupação em resolver rapidamente os problemas dos usuários!"
    else:
        doutora_2 "Ter uma documentação clara e processos bem definidos faz toda diferença. Fica muito mais fácil treinar a equipe aqui no hospital."

    # Feedback técnico/detalhado com base em bugs/qualidade
    if "selo_codigo_sem_bugs" in inventario and "conquista_bug_vuln" in inventario:
        doutora_2 "Testamos vários cenários críticos e tudo funcionou bem. O sistema está estável e seguro, parabéns!"
        doutora_1 "Vocês pensaram em cada detalhe. A confiabilidade é visível."
    else:
        doutora_2 "Notamos alguns pontos que podem ser melhorados, mas o essencial está bem implementado."
        doutora_1 "Vamos ajustar juntos com o tempo. A evolução é parte do processo!"

    # Stakeholder faz convite e reconhecimento
    doutora_1 "Gostaríamos de manter contato com todos. Estão convidados a colaborar em futuros projetos da instituição!"
    show developer_requirements positive at left_zoom
    developer_requirements "Fico feliz demais pelo reconhecimento. Parabéns, [player_name] — seu desenvolvimento ficou claro do início ao fim."

    # Mini feedback da equipe
    show developer_coding positive at left_zoom
    developer_coding "Mandou bem! Que venha o próximo desafio!"
    show developer_test positive at right_zoom2
    developer_test "Que orgulho do time. Fomos além de bugs e entregamos valor!"

    # Padding: clima de celebração e encerramento da reunião
    play sound "audio/aplausos.ogg"
    "A reunião termina em clima de vitória. Fotos, abraços, contatos trocados — e a certeza de que o semestre foi transformador."

    # Transição: volta para casa, reflexões finais
    scene bg transito_noite
    with fade
    "No ônibus, a cidade passa pela janela. Você pensa em tudo que viveu: erros, acertos, amizades, superações, aprendizado e, principalmente, confiança em si mesmo."

    scene bg quarto_noite
    with dissolve
    "De volta ao quarto, fecha o notebook e sente um misto de alívio, orgulho e vontade de recomeçar — já imaginando o próximo projeto."

    window hide
    pause 1.1
    window show

    "Fim da Semana 8 — Projeto entregue, ciclo concluído.\n\nVocê percebeu que a prática consolidou tudo que aprendeu na universidade, e que está pronto(a) para os próximos desafios."

    return
