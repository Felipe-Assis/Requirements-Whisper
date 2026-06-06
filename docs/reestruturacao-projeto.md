# Reestruturação / Reorganização do Projeto

> Análise gerada em 2026-06-06, no papel de engenheiro de software / especialista Ren'Py.
> As recomendações abaixo passaram por uma **revisão adversarial** que descartou propostas
> incorretas ou de "over-engineering". Leia também a seção 5 (**o que NÃO fazer**) — ela é tão
> importante quanto a 4.

## Resumo

O projeto é funcional, mas concentra **UI + lógica + dados nos mesmos arquivos** e tem
**duplicação massiva** na tela de contatos. A reorganização de **maior valor e menor risco** é
modesta: agrupar cenas em pastas, tornar a tela de contatos *data-driven*, centralizar config e
corrigir alguns bugs reais. Uma taxonomia elaborada de 6 pastas **não compensa** para um projeto
de disciplina, porque no Ren'Py **tudo vive num único `store` global** — pastas são puramente
cosméticas.

**Princípio-guia:** Ren'Py não é uma app Python comum. Labels e variáveis são resolvidos
**globalmente**; mover arquivos é seguro, **renomear label/variável quebra saves**.

---

## 1. Estrutura atual

```
game/
  script.rpy            # label start → call das cenas 1..21 → epílogo
  screens.rpy (1617)    # template padrão + 2 telas-overlay registradas
  gui.rpy (480), options.rpy
  scripts/
    characters.rpy      # Character() + NOME_*/COR_* + image maps + transforms + AMIGOS_DATA
    items.rpy, music.rpy, backgrounds.rpy
    functions.rpy       # VAZIO (0 bytes)
    variables/          # variables.rpy, amizade.rpy, progress.rpy
    mechanics/          # chat_screen.rpy (334), contacts_screen.rpy (480),
                        # inventory_screen.rpy, clock_screen.rpy
    scene_1..21_*.rpy   # 21 arquivos planos, 1 label cada
```

## 2. Problemas reais encontrados

| Severidade | Problema |
|---|---|
| 🔴 Alta | `chat_screen.rpy` mistura **UI + estilos + label + cliente HTTP completo** (requests/threading/web). |
| 🔴 Alta | `contacts_screen.rpy` repete um bloco de ~38 linhas **10 vezes** (10 contatos), com a escada de cores da barra de amizade copiada em cada um; descrições e ids hardcoded na UI em vez de virem de dados. |
| 🟠 Média | 21 cenas **planas**, sem agrupamento por ato, apesar de um arco narrativo claro. |
| 🟠 Média | Estado espalhado: `variables.rpy` (itens+contatos+relógio), `amizade.rpy`, `progress.rpy` (progresso+estado do chat). |
| 🟠 Média | **Dados x comportamento** entrelaçados: `AMIGOS_DATA` + `assistant_id` dentro de `characters.rpy`; URL do backend hardcoded em 2 lugares. |
| 🟡 Baixa | `functions.rpy` vazio (sugere um "lar" de helpers que na verdade está dentro das telas). |

## 3. 🐞 Bugs reais a corrigir (independem de arquitetura — prioridade máxima)

Estes são **crashes/erros silenciosos** confirmados, valem mais que qualquer reorg:

1. **`image bg creditos` indefinida** — usada pelo label `creditos_finais` (epílogo). Crash garantido nesse caminho.
2. **`images/characters/generic_portrait.png` ausente** — fallback do `chat_amigo`. Adicionar o asset ou repontar o fallback.
3. **Bug do contato `doutora_2`** — em `contacts_screen.rpy` a ação seta `amigo_selecionado = "amizade_doutora_2"` (com prefixo `amizade_`), então `AMIGOS_DATA.get(...)` falha e cai no portrait genérico. Corrigir para `"doutora_2"`.
4. **Caminho de áudio com barra faltando** — `audio/effectssend_email.ogg` em `scene_1` (e divergência `.wav`/`.ogg` em `computer_typing`).
5. **`image item notebook` definida duas vezes** (`items.rpy:60-61`) — a 2ª sombra a 1ª.
6. **Linha morta `inventory = []`** em `scene_1_quarto.rpy` — deletar (ver alerta no item 5.4).

## 4. Reestruturação recomendada (alto valor)

Em ordem de valor/risco. Rode `lint` após cada passo.

### 4.1 Agrupar as 21 cenas em pastas por ato 🟢 *(seguro, alto valor)*
Mover `scene_*.rpy` para `game/story/actN_*/`. **Labels resolvem globalmente → zero edição de
referências.** Aproveitar para corrigir os **nomes de arquivo** com typo (mantendo os labels):
- `scene_15_aniversario_supresa.rpy` → `...surpresa.rpy`
- `scene_18_2_codificacaso_final.rpy` → `...codificacao_final.rpy`

### 4.2 Tornar a tela de contatos *data-driven* 🟢 *(a mudança estrutural mais justificada)*
Criar uma tabela `CONTACTS` (em `init python` simples, para enxergar os `define NOME_*/COR_*`) e:
- iterar `for cid in CONTACTS_ORDER` (lista ordenada, não dict cru, para ordem estável);
- extrair `screen friendship_bar(value)` e `def friendship_color(v)` (a escada de cores hoje duplicada 10x);
- ler descrição/portrait/assistant_id da tabela; montar a imagem como `"%s portrait" % cid`.

Isso remove **~400 linhas** duplicadas **e** elimina a classe de bug que a duplicação esconde
(inclui o bug do `doutora_2` e typos `\n` literais). **Exige playtest** da tela e do chat.

### 4.3 Centralizar config do backend 🟢
URL `http://15.229.14.83:8000` está hardcoded em 2 funções. Mover para **um** ponto único — um
`define BACKEND_BASE_URL = ...` (mais simples, editável sem mexer em Python) ou um `game/python/config.py`.
Manter intactos o branch desktop/web e a mensagem "chat indisponível na web". *(Obs.: os `assistant_id`
são referências OpenAI, **não** são segredos — não inflar o tratamento de segurança.)*

### 4.4 (Opcional) Consolidar helpers fora das telas 🟡
Mover `add_friendship_point`/`get_friendship_point` (hoje no fim de um arquivo de UML de 480 linhas),
`add_contact`, `add_to_inventory` para **2-3** arquivos de lógica (não 6). São `init python` e
independentes de localização. Aproveitar para trocar `== 10` por `>= 10` na escada de cores
(igualdade exata de float acumulado com `0.5`/`1.0` é frágil).

## 5. ⛔ O que NÃO fazer (over-engineering / incorreto)

Itens explicitamente **descartados** pela revisão — fazê-los é churn ou bug:

1. **Taxonomia de 6 pastas** (`python/ data/ logic/ ui/ story/ + flow.rpy`) para uma VN de ~30
   arquivos. O `store` é único e global; as pastas dão **ilusão** de módulos que não existem. Um
   `story/` para as cenas captura ~90% do valor.
2. **Dividir os `default` de estado em 6 arquivos** — em um namespace único isso **multiplica o
   risco de colisão** (dois arquivos declarando o mesmo `default`) sem ganho de escopo. Dois arquivos bastam.
3. **Extrair o chat para `chat_client.py` "testável"** — a função bate num IP fixo numa thread e a
   web está desativada; **não há teste unitário realista**. Importa o pior gotcha do Ren'Py (thread +
   mutação de store + pyodide) em troca de uma testabilidade que nunca será exercida.
4. **🔴 Mexer no fluxo `call`/`jump` das cenas / reativar `scene_2`** — *isto está correto hoje e
   a "correção" quebraria o jogo*. O fluxo real: `scene_1` termina em `jump scene_2_escritorio`;
   `scene_2`, se `chosen_job=="saude"`, toca a intro e dá `return` (volta ao `script.rpy`, que então
   chama `scene_3`); senão, dá `jump scene_1_quarto` para o jogador **re-escolher o emprego**. Ou seja,
   `scene_2` está **intencionalmente** fora da call-chain e o jump-back é **lógica de retry**. Converter
   para call/return duplicaria `scene_2` e corromperia a pilha. `jump` dentro de um label chamado é
   Ren'Py normal e **não** corrompe save/rollback.
5. **Unificar `inventario` vs `inventory` num `add_to_inventory`** — são **três** sistemas distintos:
   `inventario` (pt) é o estado **real** (lido nas condições de vitória de `scene_21`), `inventory`
   (en) é um **órfão morto**, e os `item_*` booleanos são o sistema da **UI**. A única ação segura é
   **deletar a linha morta `inventory = []`**. **Não renomeie `inventario`** (quebra saves e a lógica de `scene_21`).
6. **`data/transforms.rpy` vs `ui/transforms.rpy`** para 6 blocos de 4 linhas — bikeshedding.

## 6. Restrições do modelo Ren'Py (respeitar sempre)

- **Namespace `store` único:** dividir arquivos **não** cria módulos. Cada variável deve ter `default`
  em **exatamente um** lugar; rode `lint` para garantir.
- **Compatibilidade de saves:** mover a **localização** de um `default` é seguro; **mudar o NOME** de
  variável **ou** de label invalida saves existentes (a pilha de `call` guarda nomes de label).
- **Labels globais:** mover `.rpy` entre pastas não afeta `jump`/`call` — por isso o reorg de cenas é seguro.
- **Ordem de init:** tabelas que referenciam `define` (ex.: `CONTACTS` usando `NOME_*`) devem ficar em
  `init python` simples (prioridade 0, roda **após** os `define`). **Não** promover para `python early`
  nem prioridade negativa (causa `NameError`). Preservar `generate_user_id` em `init -1 python` antes do `default user_id`.
- **Módulos `.py` puros:** se extrair algo para `game/python/`, **não** importe `store` no topo do
  módulo; receba `base_url`/`user_id`/`assistant_id` por **parâmetro**.

## 7. Esforço

| Tier | Conteúdo | Risco | Estimativa |
|---|---|---|---|
| Bugs | Seção 3 (crashes reais) | baixo | ~0,5 dia |
| 1 | Mover cenas p/ `story/` + renomear arquivos com typo | baixo | ~0,5 dia |
| 2 | Contatos *data-driven* (`CONTACTS` + loop + `friendship_bar`) | médio (playtest) | ~0,5–1 dia |
| 3 | Centralizar config; (opcional) consolidar helpers | baixo | ~0,5 dia |

> **Não** vale gastar tempo na taxonomia de 6 pastas, no split de estado em 6 arquivos, na extração
> do `chat_client.py` nem em qualquer mudança no fluxo de cenas.
