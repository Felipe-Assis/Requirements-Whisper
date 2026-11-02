# s08.rpy
# -------------------------------
# TEMPO LIVRE DA SAÚDE · SEMANA 8 (Último dia, manhã antes da apresentação)
# -------------------------------
# Conteúdos próprios da semana (docs/design/intermissoes-saude.md, S8). Sem
# estudar e sem pistas nesta semana. As conversas de fio e os descansos ficam
# em comum.rpy. O motor aplica as recompensas depois de cada label.

label im_saude_abertura_8:
    show developer_management serious at left_zoom
    developer_management "A apresentação está pronta. Até o almoço, cada um faz o que precisa."
    if energia_cansaco():
        developer_management "E quem estiver no limite: hoje não precisa provar nada."
    hide developer_management
    return


# Conversar com Emily: "O caderno". O menu só muda a resposta dela.
label im_saude_s8_conversar_developer_requirements:
    show developer_requirements neutral at left_zoom
    with dissolve
    "{i}[NOME_DEVELOPER_REQUIREMENTS] fecha o notebook quando você chega. Ao lado do teclado há um caderno pequeno, de capa verde.{/i}"
    developer_requirements "Último dia. Eu sempre faço a mesma pergunta para quem passa por aqui."
    developer_requirements "O que você leva destas oito semanas? Uma coisa só."
    menu (tipo="conversa"):
        "Ouvir casos reais. Quase tudo de importante veio de alguém contando o que aconteceu.":
            show developer_requirements enthusiastic
            developer_requirements "A entrevista com as doutoras, lembra? O roteiro tinha um monte de perguntas, e o que salvou a gente foi uma história de plantão."
            developer_requirements "A lista de funções a pessoa inventa na hora. A história ela viveu."
        "Escrever o que dá para conferir. 'Rápido' e 'prático' não dizem nada até virarem número.":
            show developer_requirements positive
            developer_requirements "Essa me deixa orgulhosa. No começo, 'o cadastro deve ser prático' ia direto para o documento."
            developer_requirements "Se ninguém consegue testar, ninguém consegue cobrar. Nem a gente de nós mesmos."
        "Não fazer nada sozinho. Toda vez que travei, alguém do time já tinha passado por aquilo.":
            show developer_requirements positive
            developer_requirements "E toda vez que alguém do time travou, você estava por perto. Isso também conta."
            developer_requirements "Requisito bom nunca é de uma pessoa só. É de quem perguntou, de quem respondeu e de quem testou."
    show developer_requirements neutral
    developer_requirements "Toma. Comprei dois na papelaria da esquina, e esse ficou sobrando."
    "{i}Ela empurra o caderno verde para o seu lado da mesa. As páginas estão em branco, menos a primeira.{/i}"
    "{i}Na letra redonda dela: 'Anota do jeito que a pessoa falou. Resumo você faz depois.'{/i}"
    developer_requirements "Foi a primeira coisa que me ensinaram, num suporte por telefone, muito antes de eu saber o que era requisito."
    developer_requirements "O resumo perde a dor. 'O sistema apresentou instabilidade' não é a mesma coisa que 'eu perdi tudo'."
    show developer_requirements enthusiastic
    developer_requirements "Agora vai. Hoje à tarde as doutoras vão falar, e você vai querer anotar cada palavra."
    hide developer_requirements
    with dissolve
    return


# Observar no ambulatório: "O sistema novo no ambulatório" (só cena, Dra. Nathalia).
label im_saude_s8_observar_ambulatorio:
    "{i}Você atravessa a praça das palmeiras até o Instituto. Hoje não é dia de entrevista nem de teste: é dia de consulta comum.{/i}"
    show doutora_2 positive at right_zoom
    with dissolve
    doutora_2 "Chegou na hora certa! Primeiro paciente da manhã no sistema novo. Paciente de verdade, não o [NOME_DEVELOPER_TEST] fingindo que tem sessenta anos."
    "{i}O paciente deixa você ficar num canto, sem anotar nome. Você senta perto da estante e só olha.{/i}"
    "{i}A [NOME_DOUTORA_2] abre o ByeByeFumo. A ficha aparece com o último retorno no topo: cigarros por dia, estágio de motivação, a data da consulta anterior.{/i}"
    doutora_2 "Olha só. Antes eu folheava três fichas para saber isso."
    "{i}Ela conversa olhando para o paciente e digita em rajadas curtas, entre uma resposta e outra. No canto da tela, uma frase pequena muda sozinha: 'Salvo às 10:42'.{/i}"
    "{i}Você percebe que ela olha para aquele canto duas vezes. Na segunda, os ombros descem um pouco.{/i}"
    "{i}Chega a escala HAD. O paciente responde rápido, hesita numa pergunta e diz que prefere pular.{/i}"
    doutora_2 "Tudo bem. A gente volta nela outro dia."
    "{i}Ela tenta concluir. A tela não trava nem apaga nada: só avisa 'Faltam 2 respostas' e oferece salvar como parcial.{/i}"
    "{i}A [NOME_DOUTORA_2] sorri para a tela, como quem sorri para um colega que lembrou de uma coisa importante.{/i}"
    "{i}Então vem o único tropeço da manhã. No fim do formulário, o botão Cancelar fica colado no Salvar. O mouse dela para em cima do Cancelar, e ela recua no último segundo.{/i}"
    doutora_2 "Opa. Quase."
    "{i}Você anota: 'Cancelar e Salvar muito próximos; quase clique errado no fim da consulta.' Sem nome, com a hora. Vai para a avaliação da tarde.{/i}"
    "{i}O paciente sai com o próximo retorno marcado. Ela se vira para você, com o café que sempre aparece do nada.{/i}"
    doutora_2 "E aí? O que você viu?"
    "{i}Você conta: o 'Salvo às 10:42', o aviso da HAD e o botão Cancelar.{/i}"
    doutora_2 "O botão eu nem ia lembrar de falar. Ia só reclamar baixinho daqui a um mês."
    doutora_2 "Na primeira semana você ouviu como deveria ser. Hoje viu como é."
    hide doutora_2
    with dissolve
    return
