# Mapa original recuperado: cidade, pessoas e tempo livre

Fonte correta: `C:/Users/Felipe/Documents/GitHub/Renpy Projects/Requirements-Whisper`, branch `main`, commit **d6b9403**, de 02/11/2026. Levantamento estático em 09/11/2026. Nenhum arquivo do original foi alterado; nenhum SDK ou jogo foi iniciado.

**Correção da auditoria anterior:** o jogo original possui world map, ônibus, metrô, agendas de NPCs, energia, relógio e intermissões nas três rotas. A auditoria inicial examinou outro checkout, incompleto, em `C:/Users/Felipe/Documents/GitHub/Requirements-Whisper` (`c934289`), que não contém esse histórico. Este documento substitui aquele diagnóstico. As três miniatividades feitas no checkout incompleto não substituem as rotas e o mapa originais.

## Evidência histórica

| Fonte / versão | Arquivos e contrato | Situação |
| --- | --- | --- |
| Original `a11bd39`, 02/11/2026 15h59 | Adiciona `game/data/mapa_cidade.rpy`, dados das três intermissões, `logic/intermissao.rpy`, `logic/energia.rpy`, `scripts/mechanics/mapa_screen.rpy` e `intermissao_fluxo.rpy` | Implementa cidade em camadas, deslocamentos, energia e intermissões. |
| Original `ae69430` | Arte do mapa e sprites dos lugares | Material visual existente na fonte correta. |
| Original `d6b9403`, 02/11/2026 20h37 | Conteúdo das intermissões das três rotas; ajustes de mapa, relógio, energia e pontos de parada | Última versão encontrada; mapa conectado às três histórias. |
| Checkout incompleto `c934289` | Scripts curtos sem pasta `game/`, campanha isolada e mapa local de laboratório criado em `4a9981f` | Não representa o alcance do original. Os 11 commits desse checkout foram examinados; o original não estava nele. |
| Trabalho `campanha-completa`, não commitado | Hub de miniprojetos e cidade opcional Campus/Oficina; `Start("campaign_start")` pula preparação | Fluxo novo, que não recupera a cidade, as agendas nem as três rotas originais. |

Não há evidência de que `d6b9403` tenha perdido seu mapa. A falha foi trabalhar no checkout incompleto e tratá-lo como o jogo inteiro.

## Contrato da experiência original

Há **oito intermissões por rota**, entre cenas obrigatórias. O jogador escolhe onde passar o tempo livre, com quem conversar, quem ajudar e o que observar, estudar ou descansar. Lugares e pessoas mudam conforme a semana. O cartão de abertura avisa que não cabe fazer tudo e que as atividades obrigatórias de aprendizagem continuam nas cenas.

O mapa mostra base ilustrada, 12 sprites de lugares, marcador “Você”, balões de pessoas e atividades, painel de ações e barra com semana/dia/hora/minutos livres/energia/local atual. Lugar fechado recebe foco para explicar o motivo; lugares de outras rotas ficam apagados e sem foco. Há modo lista equivalente, automático com texto maior, salvo em `persistent.im_mapa_lista`. Os estados são escritos, além de usar cor e ícones.

Fontes principais:

- `game/data/mapa_cidade.rpy`: geografia, coordenadas, arte, trajetos e modos.
- `game/data/intermissoes_{saude,startup,corporativo}.rpy`: salas, semanas, agendas, pistas, mentorias e extras.
- `game/logic/intermissao.rpy`: custos, disponibilidade, energia, tempo, repetição e recompensas.
- `game/logic/energia.rpy`: energia semanal.
- `game/scripts/mechanics/mapa_screen.rpy`: mapa, balões, painéis, lista, transições, resumos e pontos de parada.
- `game/scripts/mechanics/intermissao_fluxo.rpy`: fluxo e labels.
- `game/story/intermissoes/`: conteúdo real de cada escolha.

## Custos e consequências

| Ação | Minutos da ação | Energia | Resultado |
| --- | --- | --- | --- |
| Conversar | 30 | 0 | +0,5 amizade e conversa daquela semana. |
| Observar o uso | 90 | −1 | Pista quando definida e +0,5 amizade. |
| Estudar | 60 | −1 | Registro extra daquela semana no notebook. |
| Descansar | 60 | +2 | Recuperação de energia. |
| Ajudar | 90 | −2 | +1 amizade e pista técnica quando definida. |
| Mentoria | 90 | −1 | +1 amizade e próximo encontro do arco. |

O custo exibido soma ação e deslocamento. Uma ação é bloqueada, com motivo escrito, quando já feita naquele bloco, quando falta tempo ou quando falta energia. Conversar e ajudar podem ocorrer uma vez por pessoa; observar, uma vez por local; estudar, descansar e mentoria, uma vez no total por intermissão. O teto de amizade é +1 por pessoa e +2 no bloco; o teto avisa, mas não bloqueia a conversa.

Energia começa em **8/10**: Alta 8–10, Boa 4–7, Cansaço 2–3, Exaustão 0–1. Cansaço retira 30 min do próximo bloco e exaustão 60. Hora extra pode retirar até mais 60 min; o bloco preserva mínimo de 60. Energia baixa não causa game over nem altera sozinha conquistas ou final. Descansar aparece primeiro e recomendado quando há cansaço.

Ir para casa com pelo menos 60 min sobrando dá +1 energia. Encerrar o bloco recupera +3 de fim de semana, limitado a 10. O relógio avança pelo deslocamento e pela ação. Com `mesmo_dia`, uma cena que termina tarde não faz o relógio voltar: o bloco começa na hora atual e mantém seu fim, com mínimo de 90 min antes dos descontos.

## Fluxo, saídas e transporte

Confirmar um prédio abre o painel sem cobrar tempo. Confirmar uma ação devolve `("acao", poi, acao, alvo)`. Fluxo:

`im_intermissao → im_mapa → im_executar → im_deslocar → im_trajeto_telas → im_pagar_deslocamento → im_pagar_acao → im_mostrar_local → conteúdo → im_aplicar_recompensa → mapa`.

O marcador anda até o destino em aproximadamente 1 s. A transição mostra meio de transporte, origem, destino, minutos e relógio animado. Duração: 1 s para 0 min, 1,5 s até 10 min, 1,8 s até 25 min e 2 s acima disso. Clique/Enter/Espaço pulam a apresentação preservando o custo. Transições desligadas mostram cartão textual pulável de 1 s, sem caminhada ou imagem.

| Meio | Imagem real, relativa a `game/` | Som |
| --- | --- | --- |
| Ônibus | `images/bg/transicao_onibus.png` | `audio/effects/bus.ogg` |
| Metrô | `images/bg/transicao_metro.png` | `bus.ogg` a 60%; som próprio ainda não existe. |
| A pé | `images/bg/transicao_calcada.png` | `passos.ogg` |
| A pé pelo campus | `images/bg/transicao_campus.png` | `steps.ogg` |
| Elevador | `images/bg/transicao_elevador.png` | `ambiente_reuniao.ogg`; som próprio ainda não existe. |
| Escada do casarão | `images/bg/transicao_escada.png` | `passos.ogg` |

Mesmo POI: nenhum trajeto. Outra sala do mesmo prédio: 0 min, com elevador na torre, escada no casarão e dissolução no prédio da Saúde. Lugares diferentes no mesmo bairro: 10 min a pé, com a apresentação específica de campus na Cidade Universitária. Exceção: Café da esquina ↔ Casarão custa 0 min e mostra escada.

Exemplos: Startup mesa→bandejão custa 30 min de ônibus; mentoria e observação ali somam 30+90+90=210 min nas semanas 2–4. Saúde mesa→ambulatório custa 10 min pelo campus; mentoria e observação somam 190 de 210. Corporativo torre→Aterro custa 15 min a pé; descansar ali custa 75 min, em vez de 60 no café.

Chegar ao POI café toca `xicara_cafe.ogg`; chegar de outro lugar a um prédio toca `abrindo_porta.ogg`. Lugar que abre naquela semana produz aviso e `cell_vibration.ogg`. Não há seleção de linha nem condução de veículo: são deslocamentos calculados entre atividades, com arte, som e efeito no relógio.

“Ir para casa” na República e “Encerrar o tempo livre” devolvem `"encerrar"`: aplicam eventual bônus de saída cedo e chamam `im_ir_para_casa`. A volta usa ônibus/metrô conforme o par de lugares, porém **não cobra minutos nem avança o relógio**, pois encerrou o bloco. Sem ação que caiba, o fluxo fecha e mostra resumo. É possível pular o bloco no cartão de abertura ou por preferência.

O resumo mostra ações, pistas, registros, amizade, energia e tempo no caminho. `im_ponto_parada` faz autosave e oferece Continuar/Salvar/Voltar ao menu nas semanas 1–7. A história longa prossegue na mesma partida.

## Abertura, bloqueios e variantes

Saúde: sete POIs; ambulatório abre S2 e servidores S6. Startup: sete POIs; bandejão abre S2, aceleradora S6; terraço fecha S4 para a festa; bandejão fecha S6 à noite. Corporativo: oito POIs; Aterro abre S2, CAB S5, servidores S7; refeitório fecha S8 após 18h e servidores ficam reservados para a janela das 23h30.

A Subestação é sempre restrita. Edson aparece no balão “em campo, sem sinal” quando já é contato e não está na agenda daquela semana. Isso não libera visita ou conversa.

A base do mapa não tem variante noturna separada: recebe `TintMatrix("#aab8ff") * BrightnessMatrix(-0.12)` quando a **hora inicial prevista** do bloco é 18h ou mais — Startup S6 e Corporativo S8. A tonalização não depende da hora atual após ações.

Os POIs trocam explicitamente para `startup_coworking_noite` na Startup S6, `escritorio_interior_noite` na baia Corporativo S8 e `transito_noite` no Aterro S8. O terraço usa `startup_terraco_noite` mesmo em bloco diurno. Não inferir outras trocas automáticas.

Outras variantes existentes e usadas pelas cenas incluem quarto manhã/noite; trânsito manhã/tarde/noite; empresa exterior manhã/noite; escritório manhã/tarde/noite; café manhã/tarde; sala de reuniões manhã/tarde; coworking manhã/tarde/noite; central de atendimento manhã/tarde. Os fundos são definidos em `game/data/backgrounds.rpy`, com recorte central 16:9 de artes 3:2 para evitar distorção.

## Pessoas, balões e conteúdo

Nomes vêm de `game/data/character_names.rpy`; retratos e papéis, de `AMIGOS_DATA`. O balão agrupa pessoas por lugar, com a sala em que estão. O painel mostra retratos, papel e ações. Ícone sempre acompanha texto: programando, em reunião, tomando café, conversando, descansando, observando usuários, atendendo, estudando, no celular ou no computador. ★ mentoria e “aceita ajuda” são marcas escritas.

Na Startup há frases semanais próprias. S1 Davi espera o build no celular que trava e Vinícius ensaia para vasos; S2 Bia estuda Cálculo com suco; S3 está no subsolo estudando para prova; S4 mostra o app à república; S5 ajuda Rayane; S6 Bia, Joana e Rayane testam a versão nova no café; S7 Bia está na fila do bandejão; S8 ajuda calouros da monitoria. O manifesto contém todas as frases.

As três mentorias têm cinco encontros, com semana mínima 2/3/4/5/6, e um encontro por intermissão:

| Rota / mentor | Arco | Conteúdo |
| --- | --- | --- |
| Saúde / Dra. Nathalia | Um dia de ambulatório | Triagem/escala no papel; retorno de paciente; quem vê o quê; consulta de 15 min; paciente testa protótipo. Pistas `saude_p_had` e `saude_p_papeis`. |
| Startup / Lorena | Clube das Testers | Apresentar beta; cinco tarefas cronometradas; leitor de tela de Joana; calouros e pico; primeiro relato de bug. Pista `st_p_leitor`. |
| Corporativo / Jorge | Causos do SGC | Caneca de 2008 e Tia Neide; codificação de 2014; fuso do Norte; causo no wiki; mapa dos causos. Pistas `co_p_acentos` e `co_p_norte`. |

Exemplos implementados: `game/story/intermissoes/saude/s02.rpy` permite ajudar Joseph a escrever/revisar o README. Observar o ambulatório apresenta Sônia, um paciente sem CPF, papéis “cadastrar depois” e Nathalia explicando os cadastros duplicados. Em `startup/s02.rpy`, ajudar Otávio reconstrói decisões arquiteturais e seus custos; observar Bia gera pistas que reaparecem nas decisões pedagógicas.

Labels seguem `im_<rota>_s<N>_<acao>_<alvo>`, depois conteúdo compartilhado da rota; o motor registra quando usa fallback genérico. Esta auditoria não executou cada escolha para certificar cobertura integral.

## Recuperação e apresentação

A base para continuidade é o original **d6b9403**, com sua abertura, inventário, personagens, três histórias, agendas, mapa, energia e transporte. O HTML deve explicar essa experiência usando seus assets e estados. Melhorias devem entrar nas cenas e contratos existentes, preservando-os; não trocar a cidade por um hub de exercícios nem apresentar Campus/Oficina do checkout incompleto como mundo original.

Antes de integrar runtime, comparar cada acréscimo com o correspondente original e decidir seu ponto narrativo concreto. Preservar IDs/defaults/labels usados nos saves, custos e trajetos, agendas, retornos ao mapa, conteúdo obrigatório e pontos de parada. Um mapa local adicional só deve aprofundar um lugar existente quando houver requisito concreto.

O manifesto estático `X:/dev-tmp/Requirements-Whisper/atlas-original/map-manifest.json` contém geografia, 21 trajetos, exceção de percurso, custos, 22 personagens, três rotas/24 agendas, mentorias, pistas, extras, estados e 28 recursos do mapa. Todos esses 28 arquivos foram conferidos e existem. A extração usa AST/literais e a tradução como identidade; não executa Ren'Py nem código do projeto, não inclui assistant IDs.

As tabelas seguintes foram extraídas dos dados de d6b9403. Estados de disponibilidade ainda dependem de tempo, energia e ações já feitas. A marca `is_mentor` do manifesto identifica o mentor; não certifica que o próximo passo esteja liberado.

## Inventario exato dos 12 lugares


| ID | Nome | Bairro | Ancora | Largura | Rotas | Asset |
| --- | --- | --- | --- | --- | --- | --- |
| republica | República das Amendoeiras | Laranjeiras | 620,800 | 220 | saude, startup, corporativo | `game/images/mapa/lugares/republica.png` |
| predio_projeto | Prédio da equipe (Polo de Tecnologia) | Cidade Universitária | 1960,585 | 300 | saude | `game/images/mapa/lugares/predio_projeto.png` |
| praca_campus | Praça das Palmeiras | Cidade Universitária | 2130,690 | 220 | saude | `game/images/mapa/lugares/praca_campus.png` |
| instituto | Instituto (ambulatório) | Cidade Universitária | 2390,520 | 270 | saude | `game/images/mapa/lugares/instituto.png` |
| bandejao | Bandejão da universidade | Cidade Universitária | 2370,700 | 230 | startup | `game/images/mapa/lugares/bandejao.png` |
| casarao | Casarão amarelo (Trocado) | Botafogo | 1000,1090 | 330 | startup | `game/images/mapa/lugares/casarao.png` |
| cafe_esquina | Café da esquina | Botafogo | 1225,1120 | 170 | startup | `game/images/mapa/lugares/cafe_esquina.png` |
| orla | Orla de Botafogo | Botafogo | 1440,1260 | 280 | startup | `game/images/mapa/lugares/orla.png` |
| aterro | Parque do Aterro | Aterro | 1420,860 | 300 | corporativo | `game/images/mapa/lugares/aterro.png` |
| torre_vertice | Torre do Grupo Vértice | Centro | 1180,600 | 270 | corporativo | `game/images/mapa/lugares/torre_vertice.png` |
| aceleradora | Aceleradora Maré | Cais da Maré | 1590,470 | 320 | startup | `game/images/mapa/lugares/aceleradora.png` |
| subestacao | Subestação Caju | Caju | 1380,270 | 260 | corporativo | `game/images/mapa/lugares/subestacao.png` |


## Todos os trajetos entre bairros


| Origem | Destino | Minutos | Meio |
| --- | --- | --- | --- |
| Laranjeiras | Botafogo | 15 | Ônibus |
| Laranjeiras | Aterro | 15 | Ônibus |
| Laranjeiras | Centro | 20 | Metrô |
| Laranjeiras | Cais da Maré | 25 | Metrô |
| Laranjeiras | Cidade Universitária | 40 | Ônibus |
| Laranjeiras | Caju | 35 | Ônibus |
| Botafogo | Aterro | 15 | A pé |
| Botafogo | Centro | 20 | Metrô |
| Botafogo | Cais da Maré | 25 | Metrô |
| Botafogo | Cidade Universitária | 30 | Ônibus |
| Botafogo | Caju | 40 | Ônibus |
| Aterro | Centro | 15 | A pé |
| Aterro | Cais da Maré | 20 | Ônibus |
| Aterro | Cidade Universitária | 35 | Ônibus |
| Aterro | Caju | 30 | Ônibus |
| Centro | Cais da Maré | 15 | A pé |
| Centro | Cidade Universitária | 30 | Ônibus |
| Centro | Caju | 20 | Ônibus |
| Cais da Maré | Cidade Universitária | 25 | Ônibus |
| Cais da Maré | Caju | 15 | Ônibus |
| Cidade Universitária | Caju | 20 | Ônibus |


## Elenco presente nas agendas


| ID | Nome | Papel | Retrato |
| --- | --- | --- | --- |
| developer_ai | Lucas | Especialista em IA e ML. Animado, detalhista, sempre com ideias inovadoras. | `game/images/characters/developer_ai/portrait.png` |
| developer_requirements | Emily | Especialista em requisitos, comunicativa, detalhista e proativa. | `game/images/characters/developer_requirements/portrait.png` |
| developer_coding | Joseph | Desenvolvedor sênior, crítico e experiente, já liderou vários projetos. | `game/images/characters/developer_coding/portrait.png` |
| developer_management | Robert | Gerente jovem, organizado, querido pela equipe. | `game/images/characters/developer_management/portrait.png` |
| developer_quality | Daiana | Apaixonada por ensinar e qualidade de software. | `game/images/characters/developer_quality/portrait.png` |
| developer_project | Heitor | Arquiteto de software e bancos, fala pouco, mas certeiro. | `game/images/characters/developer_project/portrait.png` |
| developer_security | Mateus | Senior, fala devagar e preza segurança dos sistemas. | `game/images/characters/developer_security/portrait.png` |
| developer_test | César | Jovem prodígio dos testes, faz tudo com eficiência. | `game/images/characters/developer_test/portrait.png` |
| doutora_1 | Dra. Michelle | Experiente médica. | `game/images/characters/doutora_1/portrait.png` |
| doutora_2 | Dra. Nathalia | Jovem médica. | `game/images/characters/doutora_2/portrait.png` |
| st_mentora | Tainá | Head de produto. Te ajuda a transformar queixa em requisito. | `game/images/characters/st_mentora/portrait.png` |
| st_techlead | Otávio | CTO e cofundador. Arquitetura, dados e segurança. | `game/images/characters/st_techlead/portrait.png` |
| st_mobile | Davi | Dev mobile. Topa um pair programming a qualquer hora. | `game/images/characters/st_mobile/portrait.png` |
| st_qualidade | Lorena | Qualidade e pesquisa com usuários. Lê todas as avaliações da loja. | `game/images/characters/st_qualidade/portrait.png` |
| st_ceo | Vinícius | CEO da Trocado. Sempre com um investidor na outra linha. | `game/images/characters/st_ceo/portrait.png` |
| st_estudante | Bia | Estudante e beta tester. Anota tudo, até o cafezinho. | `game/images/characters/st_estudante/portrait.png` |
| co_mentora | Valéria | Analista sênior de requisitos. Sua mentora no Projeto Farol. Começou atendendo telefone na central. | `game/images/characters/co_mentora/portrait.png` |
| co_legado | Jorge | Desenvolvedor do SGC desde 2008. Sabe onde cada regra nasceu. Caneca de 2008 inclusa. | `game/images/characters/co_legado/portrait.png` |
| co_dev | Kauã | Dev do módulo Farol. Fã de código novo, aprendendo a respeitar o velho. Topa pair a qualquer hora. | `game/images/characters/co_dev/portrait.png` |
| co_qualidade | Ingrid | Qualidade, testes e gestão de mudanças. Se não está registrado, não aconteceu. | `game/images/characters/co_qualidade/portrait.png` |
| co_supervisora | Rosângela | Supervisora da central de atendimento. Conhece cada fila do SGC e cada número do SLA. | `game/images/characters/co_supervisora/portrait.png` |
| co_solicitante | Edson | Coordenador de manutenção de campo. Abre chamado toda semana e quer saber o que foi feito. | `game/images/characters/co_solicitante/portrait.png` |


## Rota saude - todos os POIs e oito agendas


| POI | Nome / sub-local | Lugar | Abre | Acoes fixas | Fundo / variantes |
| --- | --- | --- | --- | --- | --- |
| mesa | Mesa da equipe / 3º andar · mesa da equipe | predio_projeto | 1 | pessoas da agenda | escritorio_interior_tarde |
| sala_reunioes | Sala de reuniões / 3º andar · sala de reuniões | predio_projeto | 1 | estudar | sala_reunioes_tarde |
| cafe | Café / 2º andar · copa | predio_projeto | 1 | descansar | empresa_cafe_tarde |
| refeitorio | Refeitório / térreo · refeitório | predio_projeto | 1 | pessoas da agenda | refeitorio_tarde |
| praca | Praça em frente / praça em frente ao prédio | praca_campus | 1 | descansar | empresa_exterior_manha |
| ambulatorio | Ambulatório do Instituto / ambulatório | instituto | 2 | observar | escritorio_medica |
| servidores | Sala de servidores / subsolo · sala de servidores | predio_projeto | 6 | pessoas da agenda | sala_servidores |


| Semana | Dia | Inicio | Minutos base | Pessoas por sala | Ajudar / pista | Observar / pista | Registro de estudo | Fechamentos |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Primeiro dia | 16:00 | 120 | mesa: Emily, Joseph<br>sala_reunioes: Robert<br>cafe: Lucas, César<br>refeitorio: Daiana, Heitor<br>praca: Mateus | - | - | saude_extra_glossario | - |
| 2 | Sexta | 16:00 | 210 | mesa: Joseph, Mateus<br>sala_reunioes: Robert, Heitor<br>cafe: Emily<br>refeitorio: Daiana, César<br>praca: Lucas<br>ambulatorio: Dra. Nathalia, Dra. Michelle | Joseph | ambulatorio [saude_p_cpf] | saude_extra_fluxos | - |
| 3 | Sexta | 15:00 | 210 | mesa: Daiana, Lucas<br>sala_reunioes: Emily, Robert<br>cafe: Joseph, César<br>refeitorio: Heitor, Mateus<br>ambulatorio: Dra. Nathalia | Robert | ambulatorio [saude_p_autosave] | saude_extra_acoplamento | - |
| 4 | Sexta | 11:30 | 210 | mesa: Mateus<br>sala_reunioes: Robert, Heitor<br>cafe: Emily, Daiana<br>refeitorio: Joseph, César, Lucas<br>ambulatorio: Dra. Nathalia, Dra. Michelle | César | ambulatorio [saude_p_autosave] | saude_extra_estimativa | - |
| 5 | Sexta | 16:00 | 210 | mesa: Joseph, César<br>sala_reunioes: Robert, Emily<br>cafe: Lucas<br>refeitorio: Daiana, Heitor<br>praca: Mateus<br>ambulatorio: Dra. Nathalia | Joseph [saude_p_memoria], Mateus [saude_p_papeis] | ambulatorio [sem nova pista] | saude_extra_revisao | - |
| 6 | Dia da codificação | 16:00 | 210 | mesa: Joseph, Lucas<br>sala_reunioes: Heitor<br>cafe: Emily, Daiana<br>refeitorio: Robert<br>praca: César<br>ambulatorio: Dra. Nathalia<br>servidores: Mateus | Joseph [saude_p_memoria], Mateus [saude_p_backup] | ambulatorio [sem nova pista] | saude_extra_piramide | - |
| 7 | Dia dos testes | 15:30 | 210 | mesa: César, Daiana<br>sala_reunioes: Robert, Heitor<br>cafe: Joseph<br>refeitorio: Lucas, Emily<br>ambulatorio: Dra. Nathalia, Dra. Michelle<br>servidores: Mateus | César [saude_p_memoria], Mateus [saude_p_backup] | ambulatorio [sem nova pista] | saude_extra_rollback | - |
| 8 | Último dia | 09:30 | 210 | mesa: Emily, Robert<br>sala_reunioes: Heitor, Daiana<br>cafe: Lucas, Joseph<br>praca: César<br>ambulatorio: Dra. Nathalia<br>servidores: Mateus | - | ambulatorio [sem nova pista] | - | - |


## Rota startup - todos os POIs e oito agendas


| POI | Nome / sub-local | Lugar | Abre | Acoes fixas | Fundo / variantes |
| --- | --- | --- | --- | --- | --- |
| mesa | Mesa da equipe / 2º andar · mesa da equipe | casarao | 1 | pessoas da agenda | startup_coworking_tarde / {"6": "startup_coworking_noite"} |
| sala_vidro | Sala de vidro / 2º andar · sala de vidro | casarao | 1 | estudar | sala_reunioes_tarde |
| cafe | Café da esquina / térreo, na esquina | cafe_esquina | 1 | descansar | empresa_cafe_tarde |
| terraco | Terraço / terraço | casarao | 1 | descansar | startup_terraco_noite |
| ponto | Ponto de ônibus / ponto do calçadão | orla | 1 | descansar | transito_tarde |
| bandejao | Bandejão da universidade / salão do bandejão | bandejao | 2 | observar | refeitorio_tarde |
| aceleradora | Aceleradora Maré / auditório do galpão | aceleradora | 6 | pessoas da agenda | demo_day_auditorio |


| Semana | Dia | Inicio | Minutos base | Pessoas por sala | Ajudar / pista | Observar / pista | Registro de estudo | Fechamentos |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Sexta | 15:00 | 120 | mesa: Davi, Otávio<br>sala_vidro: Tainá<br>cafe: Lorena<br>terraco: Vinícius | Davi | - | st_extra_kanban | - |
| 2 | Sexta | 15:00 | 210 | mesa: Otávio, Davi<br>sala_vidro: Vinícius<br>cafe: Tainá<br>bandejao: Bia, Lorena | Otávio | bandejao [st_p_cancelar] | st_extra_episodio | - |
| 3 | Sexta | 15:00 | 210 | mesa: Davi, Tainá<br>sala_vidro: Otávio<br>cafe: Vinícius<br>bandejao: Bia, Lorena | - | bandejao [st_p_tunel] | st_extra_invest | - |
| 4 | Sexta | 14:30 | 210 | mesa: Davi<br>sala_vidro: Vinícius, Tainá<br>cafe: Otávio<br>bandejao: Bia, Lorena | - | bandejao [st_p_bolsa] | st_extra_idempotencia | terraco: Fechado: arrumando a festa |
| 5 | Segunda | 16:00 | 210 | mesa: Otávio, Davi<br>sala_vidro: Tainá<br>cafe: Vinícius<br>bandejao: Bia, Lorena | Otávio [st_p_conexoes], Davi [st_p_logs] | bandejao [sem nova pista] | st_extra_coorte | - |
| 6 | Terça | 18:00 | 180 | mesa: Davi, Otávio<br>cafe: Bia<br>terraco: Tainá, Lorena<br>aceleradora: Vinícius | Davi [st_p_loja], Otávio [st_p_conexoes], Vinícius [st_p_retencao] | cafe [sem nova pista] | st_extra_carga | bandejao: Fechado à noite |
| 7 | Quarta | 11:30 | 180 | mesa: Otávio<br>sala_vidro: Davi<br>cafe: Tainá<br>bandejao: Bia, Lorena<br>aceleradora: Vinícius | Davi [st_p_loja], Vinícius [st_p_retencao] | bandejao [sem nova pista] | st_extra_rollout | - |
| 8 | Quarta | 13:30 | 210 | mesa: Davi, Otávio<br>sala_vidro: Tainá<br>bandejao: Bia, Lorena<br>aceleradora: Vinícius | Vinícius [st_p_retencao] | bandejao [sem nova pista] | - | - |


### Frases de atividade por semana na Startup


| Semana | Pessoa | Atividade | Frase |
| --- | --- | --- | --- |
| 1 | Davi | programando | Davi esperando o build no celular que trava |
| 1 | Otávio | programando | Otávio revisando um PR, caneca na mão |
| 1 | Tainá | estudando | Tainá reorganizando a coluna de descoberta |
| 1 | Lorena | tomando café | Lorena lendo avaliações com um café |
| 1 | Vinícius | no celular | Vinícius ensaiando o pitch para os vasos de planta |
| 2 | Otávio | programando | Otávio passando decisões antigas a limpo |
| 2 | Davi | no celular | Davi testando o app no Tijolo |
| 2 | Vinícius | em reunião | Vinícius saindo de uma call com o fundo |
| 2 | Tainá | tomando café | Tainá relendo as anotações da entrevista |
| 2 | Bia | estudando | Bia estudando Cálculo com um suco |
| 2 | Lorena | observando usuários | Lorena com a Bia e duas amigas dela |
| 3 | Davi | programando | Davi ligando o protótipo da confirmação |
| 3 | Tainá | estudando | Tainá escrevendo critérios |
| 3 | Otávio | programando | Otávio cruzando registros do servidor |
| 3 | Vinícius | estudando | Vinícius lendo um livro de métricas |
| 3 | Bia | estudando | Bia no subsolo, estudando para a prova |
| 4 | Davi | programando | Davi montando a fila com id único |
| 4 | Vinícius | em reunião | Vinícius e Tainá escrevendo o post dos mil |
| 4 | Otávio | tomando café | Otávio fugindo do barulho com um café |
| 4 | Bia | no celular | Bia mostrando o app para a república |
| 5 | Otávio | programando | Otávio olhando o painel do banco da noite da festa |
| 5 | Davi | programando | Davi caçando um erro na fila de sincronização |
| 5 | Tainá | estudando | Tainá atualizando a lista de riscos |
| 5 | Vinícius | no celular | Vinícius refazendo o slide principal |
| 5 | Bia | atendendo | Bia ajudando a Rayane com o app |
| 6 | Davi | programando | Davi tirando prints para as lojas |
| 6 | Otávio | programando | Otávio preparando o teste de carga |
| 6 | Bia | observando usuários | Bia, Joana e Rayane testando a versão nova |
| 6 | Tainá | descansando | Tainá respirando depois de uma reunião |
| 6 | Lorena | estudando | Lorena anotando o teste com calouros |
| 6 | Vinícius | em reunião | Vinícius ensaiando o pitch no palco |
| 7 | Otávio | programando | Otávio comendo marmita de olho no teste de carga |
| 7 | Davi | programando | Davi preenchendo os formulários das lojas |
| 7 | Tainá | estudando | Tainá reescrevendo o texto de exclusão de conta |
| 7 | Bia | no celular | Bia na fila do bandejão |
| 7 | Vinícius | em reunião | Vinícius no segundo ensaio |
| 8 | Davi | no celular | Davi de olho no painel |
| 8 | Otávio | programando | Otávio com o painel e a caneca |
| 8 | Tainá | estudando | Tainá rascunhando a retrospectiva |
| 8 | Bia | atendendo | Bia com os calouros da monitoria |
| 8 | Lorena | observando usuários | Lorena observando calouros |
| 8 | Vinícius | em reunião | Vinícius no ensaio geral |


## Rota corporativo - todos os POIs e oito agendas


| POI | Nome / sub-local | Lugar | Abre | Acoes fixas | Fundo / variantes |
| --- | --- | --- | --- | --- | --- |
| baia | Baia do Farol / 12º andar · baia do Farol | torre_vertice | 1 | pessoas da agenda | escritorio_interior_tarde / {"8": "escritorio_interior_noite"} |
| central | Central de atendimento / 3º andar · central de atendimento | torre_vertice | 1 | observar | central_atendimento_tarde |
| cafe | Café do térreo / térreo · café | torre_vertice | 1 | descansar | empresa_cafe_tarde |
| refeitorio | Refeitório / 2º andar · refeitório | torre_vertice | 1 | descansar | refeitorio_tarde |
| arquivo | Sala do arquivo / subsolo · arquivo | torre_vertice | 1 | estudar | sala_arquivo_tarde |
| sala_cab | Sala do CAB / 15º andar · sala do CAB | torre_vertice | 5 | pessoas da agenda | sala_reunioes_tarde |
| servidores | Sala de servidores / subsolo · servidores | torre_vertice | 7 | pessoas da agenda | sala_servidores |
| aterro | Parque do Aterro / beira da baía | aterro | 2 | descansar | transito_tarde / {"8": "transito_noite"} |


| Semana | Dia | Inicio | Minutos base | Pessoas por sala | Ajudar / pista | Observar / pista | Registro de estudo | Fechamentos |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Sexta | 15:00 | 120 | baia: Kauã<br>central: Rosângela<br>cafe: Valéria<br>arquivo: Jorge | Kauã | central [co_p_ligacoes] | co_extra_itil | - |
| 2 | Sexta | 16:30 | 180 | baia: Kauã, Ingrid<br>central: Rosângela<br>cafe: Edson<br>refeitorio: Valéria<br>arquivo: Jorge | - | central [co_p_vazio] | co_extra_reversa | - |
| 3 | Sexta | 15:00 | 180 | baia: Valéria<br>central: Rosângela, Edson<br>cafe: Kauã<br>refeitorio: Ingrid<br>arquivo: Jorge | - | central [sem nova pista] | co_extra_casos_uso | - |
| 4 | Sexta | 13:00 | 180 | baia: Jorge<br>central: Rosângela<br>cafe: Valéria, Ingrid<br>refeitorio: Kauã | - | central [sem nova pista] | co_extra_anticorrupcao | - |
| 5 | Sexta | 15:00 | 180 | baia: Kauã<br>central: Rosângela, Edson<br>cafe: Valéria<br>arquivo: Jorge<br>sala_cab: Ingrid | Ingrid [co_p_botao] | central [sem nova pista] | co_extra_rfc | - |
| 6 | Sexta | 15:00 | 180 | baia: Kauã, Valéria<br>central: Rosângela<br>cafe: Edson<br>arquivo: Jorge<br>sala_cab: Ingrid | Kauã [co_p_senha], Ingrid [co_p_botao] | central [sem nova pista] | co_extra_caracterizacao | - |
| 7 | Quinta | 14:00 | 180 | baia: Kauã<br>central: Rosângela<br>cafe: Valéria<br>refeitorio: Edson<br>arquivo: Jorge<br>servidores: Ingrid | Ingrid [co_p_parada] | central [sem nova pista] | co_extra_parada | - |
| 8 | Sexta | 18:00 | 180 | baia: Kauã, Ingrid<br>cafe: Valéria<br>arquivo: Jorge | - | central [sem nova pista] | - | refeitorio: Fechado depois das 18h, servidores: Reservada para a janela (abre às 23h30) |


## Conferencia dos assets do mapa


| Arquivo relativo ao original | Existe |
| --- | --- |
| `game/images/mapa/cidade_base.png` | True |
| `game/images/mapa/voce.png` | True |
| `game/images/mapa/lugares/republica.png` | True |
| `game/images/mapa/lugares/predio_projeto.png` | True |
| `game/images/mapa/lugares/praca_campus.png` | True |
| `game/images/mapa/lugares/instituto.png` | True |
| `game/images/mapa/lugares/bandejao.png` | True |
| `game/images/mapa/lugares/casarao.png` | True |
| `game/images/mapa/lugares/cafe_esquina.png` | True |
| `game/images/mapa/lugares/orla.png` | True |
| `game/images/mapa/lugares/aterro.png` | True |
| `game/images/mapa/lugares/torre_vertice.png` | True |
| `game/images/mapa/lugares/aceleradora.png` | True |
| `game/images/mapa/lugares/subestacao.png` | True |
| `game/images/mapa/icones/conversando.png` | True |
| `game/images/mapa/icones/estudando.png` | True |
| `game/images/mapa/icones/reuniao.png` | True |
| `game/images/mapa/icones/celular.png` | True |
| `game/images/mapa/icones/descansando.png` | True |
| `game/images/mapa/icones/observando.png` | True |
| `game/images/mapa/icones/programando.png` | True |
| `game/images/mapa/icones/cafe.png` | True |
| `game/images/bg/transicao_onibus.png` | True |
| `game/images/bg/transicao_metro.png` | True |
| `game/images/bg/transicao_calcada.png` | True |
| `game/images/bg/transicao_campus.png` | True |
| `game/images/bg/transicao_elevador.png` | True |
| `game/images/bg/transicao_escada.png` | True |
