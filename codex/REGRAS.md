# Regras do aoe2-codex

Versão 0.1 — 15/10/2026. Este documento é a "constituição" do projeto: tudo o que fizermos às civs tem de respeitar o que está aqui. Cada decisão tem um estado:

- **[decidido]** — acordado, só muda com nova discussão;
- **[em princípio]** — aceite, mas os pormenores ainda estão em aberto;
- **[proposta]** — por discutir.

## 1. Objetivo

Mostrar, num site semelhante ao aoe2techtree.net, uma versão do Age of Empires II em que cada civilização tem bónus, unidades, tecnologias, tech tree e texto de história mais fiéis à história. O site mostra também o original e explica cada mudança, com fontes.

É um projeto de fãs, não comercial. Não tentamos convencer os developers; fazemo-lo por gosto e para outros fãs de história e de AoE2.

## 2. Âmbito

- Só o Age of Empires II: Definitive Edition base. Ficam de fora o AoE1, o Return of Rome e as Chronicles. **[decidido]**
- Janela temporal de referência: **500–1500**. Uma civ pode tocar os extremos, mas a maior parte da sua existência, ou o auge que o jogo representa, tem de cair dentro da janela. **[decidido]**

## 3. O que é uma civ

> Uma civ é um povo ou entidade política com identidade própria, ligado a um território (ou, se for nómada, a um espaço de pastoreio), que se manteve durante cerca de dois séculos, sobretudo dentro de 500–1500, e cuja forma de guerrear e de viver está documentada o suficiente para a desenhar sem inventar. **[decidido]**

Os cinco testes:

1. **Identidade.** É um povo ou um Estado. Não é uma fação de uma guerra civil, uma dinastia de passagem nem uma atividade.
2. **Continuidade.** Cerca de dois séculos (seis a oito gerações). Conta a continuidade do povo, não a do império: o Império Mongol unificado durou poucas décadas, mas os Mongóis existem antes e depois.
3. **Território.** Um núcleo territorial ou um espaço nómada definido.
4. **Janela.** Dentro de 500–1500, como na secção 2.
5. **Distinção e fontes.** Guerreava ou vivia de forma documentadamente diferente dos vizinhos, e há fontes (escritas ou arqueológicas) para o mostrar.

"Civilização", no sentido académico estrito (sociedades urbanas e letradas), deixaria de fora povos como os Tupi, os Mapuche ou os Cumans. No projeto, "civ" quer dizer **povo jogável**.

## 4. Decisões de roster

| Civ atual | Decisão | Nível | Estado |
|---|---|---|---|
| Shu, Wei, Wu | Passam para a secção **"Fora do âmbito"**, com o desenho original e uma explicação. O que tinham de documentado (Traction Trebuchet, Tuntian, marinha fluvial) passa para as civs chinesas. | — | [decidido] |
| Romans | "Fora do âmbito": anteriores à janela; os romanos medievais são os Byzantines. | — | [em princípio] |
| Huns | Substituídos pelos **Avars** (567–796), onde o Tarkan e o bónus de trabucos fazem sentido. | N1 | [em princípio] |
| Vikings | Renomeados **Norse**: "viking" era uma atividade, e Danes e Varangians já existem. | N1 | [decidido] |
| Slavs | Renomeados **Rus'**. | N1 | [em princípio] |
| Celts | Refeitos como **Gaels** (Irlanda e Escócia). | N1 | [em princípio] |
| Dravidians | Rename para um povo ou Estado concreto (Tamils ou Cholas, a decidir). | N1 | [em princípio] |
| Tatars | Separar a Horda Dourada de Timur, que a devastou em 1391 e 1395. | N1 | [em princípio] |
| Armenians | Centrados na **Arménia Maior** (Ani, Vaspurakan, cavalaria *nakharar*). A Cilícia sai do núcleo. | N1 | [decidido] |
| Goths | Mantêm-se como os reinos visigodo (418–711) e ostrogodo. | N1 | [em princípio] |
| Burgundians | Caso-limite (o Estado Valois teve quatro gerações), mas a Borgonha passa. Mantêm-se. | N1 | [em princípio] |
| Chinese | Dividir em **Tang, Song e Ming**. | N3 | [proposta] |
| (nova) | **Tibetans**: civ nova prioritária (Império Tibetano c. 618–842 e período monástico). | N3 | [decidido] |

Dividir civs em nome da fidelidade é permitido. **[decidido]**

## 5. Níveis de rework

O nível mede o **custo de implementação para um futuro modder**, não a importância histórica. **[decidido]**

| Nível | O que cabe | Regra |
|---|---|---|
| **N1 — Redistribuir** | Mudar que civ tem que unidade, tech ou edifício já existente (incluindo as únicas de outras civs). Reescrever bónus com efeitos que já existem. Renomear civs, unidades e techs. Reatribuir architecture sets que já existem. | Cada efeito tem de existir já algures no jogo. Só dados e texto. |
| **N2 — Ajustar** | O N1, mais: mudar com cuidado efeitos e custos de techs genéricas; acrescentar ou tirar algumas techs genéricas; unidades e techs únicas novas feitas a partir de mecânicas que já existem; separar linhas cujas imagens já existem (por exemplo arco e besta). | Só mecânicas que o motor já suporta, sem arte nova obrigatória. |
| **N3 — Reconstruir** | Edifícios, unidades e mecânicas novas; mudanças ao pedra-papel-tesoura; architecture sets novos; civs novas. | Liberdade total, mas cada mudança cita uma fonte. |

No site, cada mudança leva a etiqueta do seu nível.

## 6. Regras de desenho das civs

1. **Composição.** Cada civ tem **4 a 6 bónus passivos**, **1 bónus de equipa** e **2 tecnologias únicas** (uma de Castle Age e uma de Imperial Age). Entre os bónus passivos há pelo menos um económico e um militar. **[decidido]**
2. **Tecnologias únicas.** Uma UT nunca pode limitar-se a devolver algo que a árvore retirou. Se desbloqueia algo genérico, tem de trazer também um segundo efeito exclusivo. **[decidido]**
3. **Bónus repetidos.** São permitidos quando a história os justifica. A identidade de uma civ vem da combinação dos bónus, não de cada bónus ser único. **[decidido]**
4. **Fundamento.** Cada elemento (bónus, unidade, tech, mudança de árvore) indica a base histórica e, sempre que possível, uma fonte. Quando os historiadores discordam, isso fica dito. **[decidido]**
5. **Renomear ou substituir.** Renomeia-se quando a função tem um equivalente histórico (Horse Collar → *Chinampas* para os Aztecs). Substitui-se ou retira-se quando não tem: um Trebuchet com outro nome continua a ser um trebuchet. Os renames podem ser por civ. **[decidido]**
6. **Substituir em vez de só retirar.** Quando se tira algo de que a civ precisa para jogar, procura-se um substituto com a mesma função (como o Traction Trebuchet). **[em princípio]**
7. **Coerência com o texto.** A árvore não pode contradizer o nosso texto de história da civ. **[em princípio]**
8. **Ficha da civ.** Cada civ tem uma ficha com a entidade representada, a região, a janela temporal e as fontes principais. **[em princípio]**
9. **Estrutura do jogo.** Mantém-se o esqueleto do AoE2: quatro idades, o sistema de counters e um "orçamento de poder" parecido entre civs. O N1 não promete equilíbrio, mas evita absurdos óbvios. **[em princípio]**
10. **Architecture sets.** Reatribuir um set existente é N1 (Persians → Central Asian); criar um set novo é N3 (um set "Estepe" para Avars, Mongols e Cumans). **[decidido]**

## 7. Textos de história

- Escrevemos **textos nossos**, com fontes, assinalando o que é contestado. **[decidido]**
- **Não republicamos** os textos originais do jogo, que são da Microsoft. Para trabalho, ficam só localmente em `codex/.local/historia-original/` (pasta ignorada pelo git). **[decidido]**
- A análise crítica dos textos originais (afirmação, problema, correção) está em `codex/analise/`.

## 8. Ficheiros

```
codex/
  REGRAS.md                     este documento
  civs/<Civ>.toml               o desenho de cada civ (um ficheiro por civ)
  historia/<Civ>.md             o nosso texto de história de cada civ
  fora-do-ambito.md             civs excluídas e porquê
  analise/                      a análise de fidelidade das 56 civs (outubro de 2026)
  ferramentas/                  scripts (preparar dados, gerar relatório)
  .local/                       ficheiros de trabalho locais, fora do git
```

O desenho de cada civ é um ficheiro TOML (legível à mão e lido pela biblioteca padrão do Python). Os textos que vão aparecer no jogo ficam em inglês, como no original; as justificações ficam em português. Formato **[proposta]**:

```toml
civ = "Portuguese"            # nome interno em data/data.json
nome = "Portuguese"           # nome mostrado (diferente se houver rename)
estado = "rascunho"           # rascunho | revisto | aprovado
rotulo = "Archer and Naval civilization"

[ficha]
entidade = "Reino de Portugal"
regiao = "Ocidente da Península Ibérica"
janela = "1139–1521"
fontes = ["Fernão Lopes, Crónica de D. João I"]

[[bonus]]
texto = "Crossbowman and Arbalester upgrades free"
tipo = "militar"              # economico | militar | outro
nivel = 1
mudanca = "novo"              # mantido | alterado | novo
substitui = "Foragers generate wood in addition to food"
precedente = "Militia-line upgrades free (Bulgarians)"   # N1: efeito que já existe
base = "Os besteiros do conto: milícias concelhias com quotas fixas (séculos XIII–XV)."

[[unidade_unica]]
nome = "Ginete"
modelo = "Genitour"           # unidade existente usada como base
nivel = 1
mudanca = "novo"
substitui = "Organ Gun"
base = "Cavalaria ligeira à gineta, essencial na Reconquista e em Marrocos."

[[tech_unica]]
nome = "Volta do Mar"
idade = "Imperial"
efeito = "Sets the entire map to explored; Ships train +33% faster"
nivel = 1
mudanca = "alterado"
substitui = "Circumnavigation"
base = "Técnica portuguesa de regresso pelo largo do Atlântico (século XV)."

[bonus_equipa]
texto = "Technologies research +25% faster"
nivel = 1
mudanca = "mantido"
base = "Ciência náutica (Abraão Zacuto, Pedro Nunes)."

[arvore]
adicionar = ["Arrowslits", "Hoardings"]
remover = []

# Renames de techs ou unidades genéricas só para esta civ.
# Exemplo noutra civ: de = "Horse Collar", para = "Chinampas" (Aztecs).
[[renomear]]
de = "Hoardings"
para = "Hoardings"            # sem mudança nos Portuguese; fica só como exemplo do formato
nivel = 1

[arquitetura]
set = "Mediterranean"
```

## 9. Aspetos legais

- O projeto segue as [Game Content Usage Rules](https://www.xbox.com/en-us/developers/rules) da Microsoft: não comercial, com o aviso de copyright, sem sugerir ligação oficial.
- O código vem do aoe2techtree (licença MIT); o aviso de copyright do HSZemi mantém-se.
- Antes de tornar o site público, avisamos os autores do aoe2techtree (SiegeEngineers / HSZemi). **[decidido]**

## 10. Ideias guardadas para N2 e N3

- Separar Archer e Crossbowman em duas linhas (N2: as imagens já existem).
- Granularidade no ferreiro: manter a metalurgia comum e acrescentar techs de técnica por arma (lança em riste para a cavalaria, ordem de piqueiros para a infantaria).
- Techs defensivas: pez e água a ferver, fosso, talude.
- Samurai que troca entre arco e espada (como a Ratha); dardos que reduzem a armadura perfurante (efeito *pilum*).
- Sem engenhos de cerco nas Américas; substitutos como o fogo (Cuzco, 1536) e o assalto.
- Mule Cart alargado a outras civs de récuas (almocreves, arrieros); animais diferentes (lamas, camelos, iaques) são N3.
- Uma Dark Age menos "simulador de caça": séquitos guerreiros e raides. Rever o nome "Dark Age".
- Usar Houses como muralha é um truque de jogo; corrigir exige mudar o motor (N3).
- Set de arquitetura "Estepe" (N3).
