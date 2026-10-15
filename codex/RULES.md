# aoe2-codex rules

Version 0.3, 15 October 2026. This document is the project's constitution: everything we do to the civilizations must follow it. Each decision has a status:

- **[decided]**: agreed; changes only after a new discussion.
- **[in principle]**: accepted, but the details are still open.
- **[proposal]**: still to be discussed.

## 1. Goal

Show, on a site similar to aoe2techtree.net, a version of Age of Empires II in which every civilization has bonuses, units, technologies, a tech tree and a history text that are more faithful to history. The site also shows the original and explains every change, with sources.

This is a non-commercial fan project. We are not trying to convince the developers; we do it for fun and for other history and AoE2 fans.

## 2. Scope

- Age of Empires II: Definitive Edition base game only. Age of Empires I, Return of Rome and Chronicles are out. **[decided]**
- Reference time frame: **500–1500**. A civ may touch the edges, but most of its existence, or the peak the game represents, must fall inside it. **[decided]**

## 3. What a civ is

> A civ is a people or polity with its own identity, tied to a territory (or, for nomads, a defined grazing range), that lasted about two centuries, mostly within 500–1500, and whose way of fighting and living is documented well enough to design it without inventing. **[decided]**

The five tests:

1. **Identity.** It is a people or a state. Not a faction in a civil war, a passing dynasty or an activity.
2. **Continuity.** About two centuries (six to eight generations). What counts is the continuity of the people, not of the empire: the united Mongol Empire lasted only a few decades, but the Mongols exist before and after it.
3. **Territory.** A core territory or a defined nomadic range.
4. **Time frame.** Within 500–1500, as in section 2.
5. **Distinctiveness and sources.** It fought or lived in a documented way that differed from its neighbours, and there are sources (written or archaeological) to show it.

"Civilization" in the strict academic sense (urban, literate societies) would exclude peoples such as the Tupi, the Mapuche or the Cumans. In this project, "civ" means **a playable people**.

## 4. Roster decisions

| Current civ | Decision | Level | Status |
|---|---|---|---|
| Shu, Wei, Wu | Move to the **"Out of scope"** section, with the original design and an explanation. Their documented elements (Traction Trebuchet, Tuntian, river navy) go to the Chinese civs. | — | [decided] |
| Romans | "Out of scope": earlier than the time frame; the medieval Romans are the Byzantines. | — | [in principle] |
| Huns | Replaced by the **Avars** (567–796), where the Tarkan and the trebuchet bonus make sense. | N1 | [in principle] |
| Vikings | Renamed **Norse**: "viking" was an activity, and the Danes and Varangians already exist. | N1 | [decided] |
| Slavs | Renamed **Rus'**. | N1 | [in principle] |
| Celts | Reworked as **Gaels** (Ireland and Scotland). | N1 | [in principle] |
| Dravidians | Renamed to a concrete people or state (Tamils or Cholas, to be decided). | N1 | [in principle] |
| Tatars | Separate the Golden Horde from Timur, who devastated it in 1391 and 1395. | N1 | [in principle] |
| Armenians | Centred on **Greater Armenia** (Ani, Vaspurakan, *nakharar* cavalry). Cilicia leaves the core identity. | N1 | [decided] |
| Goths | Kept as the Visigothic (418–711) and Ostrogothic kingdoms. | N1 | [in principle] |
| Burgundians | Borderline case (the Valois state lasted four generations), but Burgundy passes. Kept. | N1 | [in principle] |
| Chinese | Split into **Tang, Song and Ming**. | N3 | [proposal] |
| (new) | **Tibetans**: top-priority new civ (Tibetan Empire c. 618–842 and the monastic period). | N3 | [decided] |

Splitting civs for the sake of accuracy is allowed. **[decided]**

## 5. Rework levels

The level measures the **implementation cost for a future modder**, not historical importance. **[decided]**

| Level | What fits | Rule |
|---|---|---|
| **N1: Redistribute** | Change which civ has which existing unit, tech or building (including other civs' unique ones). Rewrite bonuses using effects that already exist. Rename civs, units and techs. Reassign existing architecture sets. | Every effect must already exist somewhere in the game. Data and text only. |
| **N2: Adjust** | N1, plus: carefully change effects and costs of generic techs; add or remove a few generic techs; new unique units and techs built from mechanics that already exist; split lines whose graphics already exist (for example bow and crossbow). | Only mechanics the engine already supports, with no new art required. |
| **N3: Rebuild** | New buildings, units and mechanics; changes to the rock-paper-scissors counter system; new architecture sets; new civs. | Full freedom, but every change cites a source. |

On the site, every change carries its level label.

## 6. Civ design rules

1. **Composition.** Every civ has:
   - **4 to 6 passive bonuses**, with at least one economic and one military bonus. Unique buildings ("Can build X") and starting bonuses ("Start with X") count as passive bonuses. **[decided]**
   - **2 to 4 unique technologies.** One at the **Castle** and one at the **Town Center** are mandatory. Up to two more can be researched at other main buildings: Castle, Town Center, Market, Monastery, University, Dock, Mill, Lumber Camp, Mining Camp, Barracks, Archery Range, Stable, Siege Workshop. **[decided]**
   - **1 team bonus.** Whether some civs may have two is still open. **[proposal]**
   - **1 or 2 unique units.** A naval unique unit counts. Regional units (Steppe Lancer, Genitour/Jinete, Mounted Crossbowman) do not. **[in principle]**
   - A combined cap of **passive bonuses + unique techs ≤ 9**, so that no civ has both the most bonuses and the most techs. **[proposal]**
2. **Where each historical trait goes.** Ask these questions in order: **[decided]**
   1. Did it benefit neighbours or allies (trade, transferred techniques, mercenaries, alliances, religious influence)? Then it is the **team bonus**. A trait that only benefited the civ itself is never a team bonus.
   2. Is it **structural** (geography, environment, economic base, social structure, a long military tradition)? Then it is a **passive bonus**.
   3. Is it **datable** (a reform, invention, institution or adopted technique, usually with a proper name)? Then it is a **unique technology**: military or royal at the **Castle**; state or government at the **Town Center**; other themes at the building where they belong (trade at the Market, religion at the Monastery, knowledge and writing at the University, the sea at the Dock, farming at the Mill, and so on).
   4. The size of the effect only breaks ties: a very strong effect suits a tech (its cost and delay act as a brake); a small, continuous edge suits a passive. History decides first.
3. **Number of datable moments.** Extra unique techs exist only for distinct datable moments, never one reform split in two. If a civ has more moments than slots, the rest become age-gated passives ("starting in the Imperial Age") or N2 ideas. If it has too few, a structural trait with a recognisable moment of formalisation can be promoted (the Castilian municipal militias, formalised as the Santa Hermandad in 1476). For peoples without a state, the Town Center tech represents a community institution; if its historical basis is weak, we say so. **[in principle]**
4. **Ages of unique techs.** With two techs at the Castle, one is Castle Age and one Imperial Age, in chronological order within the civ's own time window. Techs at the Town Center and at civil buildings: Feudal Age at the earliest, never Dark Age. Military techs outside the Castle (Barracks, Archery Range, Stable, Siege Workshop, Dock): Castle Age at the earliest. **[in principle]**
5. **Levels of unique techs.** Moving an existing unique tech to another building, or renaming it, is N1. Creating a new tech, even with an effect that already exists elsewhere, is N2. **[in principle]**
6. **Unique technologies never just give things back.** A unique tech must never merely give back something the tree took away. If it unlocks something generic, it must also bring a second, exclusive effect. **[decided]**
7. **Repeated bonuses.** Allowed when history justifies them. A civ's identity comes from the combination of its bonuses, not from each bonus being unique. **[decided]**
8. **Grounding.** Every element (bonus, unit, tech, tree change) states its historical basis and, whenever possible, a source. Where historians disagree, we say so. **[decided]**
9. **Relevance test.** Every bonus, team bonus, unique unit and unique tech must pass this test: *if we erased this trait from the civ's real history, would its course or its identity change?* If not, the trait is irrelevant and does not deserve a special slot, however well documented it is. Avoid traits that are only details (one arrow type, one architectural feature, one battle anecdote) when the civ has weightier traits available. What counts is historical weight, not fame: something unknown to most players can pass (the Mesta, the Inca *qullqa* storehouses, the Tuntian colonies), and something famous can fail. The higher the slot (team bonus, unique unit, unique tech), the higher the bar. If a civ runs short of relevant traits, prefer repeating a broad, well-founded bonus (rule 7) to using an obscure detail. **[decided]**
10. **Rename or replace.** Rename when the function has a historical equivalent (Horse Collar → *Chinampas* for the Aztecs). Replace or remove when it doesn't: a renamed trebuchet is still a trebuchet. Renames can be per civ. **[decided]**
11. **Replace rather than only remove.** When we remove something the civ needs in order to play, we look for a substitute with the same function (as the Traction Trebuchet does). **[in principle]**
12. **Consistency with the text.** The tree must not contradict our history text for the civ. **[in principle]**
13. **Civ profile.** Every civ has a profile with the entity it represents, its region, its time window and its main sources. **[in principle]**
14. **Game structure.** We keep the AoE2 skeleton: four ages, the counter system and a similar "power budget" across civs. N1 does not promise balance, but it avoids obvious absurdities. **[in principle]**
15. **Architecture sets.** Reassigning an existing set is N1 (Persians → Central Asian); creating a new set is N3 (a "Steppe" set for Avars, Mongols and Cumans). **[decided]**

## 7. History texts

- We write **our own texts**, with sources, flagging what is contested. **[decided]**
- We **do not republish** the game's original texts, which belong to Microsoft. For working purposes they stay local, in `codex/.local/original-history/` (ignored by git). **[decided]**
- The critical analysis of the original texts (claim, problem, correction) is in `codex/analysis/`.

## 8. Files

```
codex/
  RULES.md                      this document
  civs/<Civ>.toml               the design of each civ (one file per civ)
  history/<Civ>.md              our history text for each civ
  out-of-scope.md               excluded civs and why
  analysis/                     the historical-accuracy analysis of the 56 civs (October 2026)
  tools/                        scripts (prepare working data, render the report)
  .local/                       local working files, outside git
```

All project files are written in English. **[decided]**

Each civ design is a TOML file (readable by hand and parsed by Python's standard library). Format **[proposal]**:

```toml
civ = "Portuguese"            # internal name in data/data.json
name = "Portuguese"           # displayed name (different if renamed)
status = "draft"              # draft | reviewed | approved
label = "Archer and Naval civilization"

[profile]
entity = "Kingdom of Portugal"
region = "Western Iberian Peninsula"
window = "1139–1521"
sources = ["Fernão Lopes, Chronicle of King John I"]

[[bonus]]
text = "Crossbowman and Arbalester upgrades free"
kind = "military"             # economic | military | other
level = 1
change = "new"                # kept | changed | new
replaces = "Foragers generate wood in addition to food"
precedent = "Militia-line upgrades free (Bulgarians)"   # N1: an effect that already exists
basis = "The besteiros do conto: municipal crossbow militias with fixed quotas (13th–15th centuries)."

[[unique_unit]]
name = "Ginete"
model = "Genitour"            # existing unit used as the base
level = 1
change = "new"
replaces = "Organ Gun"
basis = "Light cavalry riding à la gineta, central to the Reconquista and the Moroccan wars."

[[unique_tech]]
name = "Volta do Mar"
building = "Dock"             # Castle | Town Center | Market | Monastery | University | Dock | Mill | ...
kind = "civil"                # military | civil
age = "Imperial"
effect = "Sets the entire map to explored; Ships train +33% faster"
level = 1                     # an existing tech moved and renamed
change = "changed"
replaces = "Circumnavigation"
basis = "The Portuguese technique of returning through the open Atlantic (15th century)."

[[unique_tech]]
name = "Lei das Sesmarias"
building = "Town Center"
kind = "civil"
age = "Castle"
effect = "Farmers work +15% faster"
level = 2                     # a new tech, with an effect that exists elsewhere
change = "new"
precedent = "Farmers work +15% faster (Slavs)"
basis = "The 1375 law of King Ferdinand I forcing abandoned land back into cultivation."

[team_bonus]
text = "Technologies research +25% faster"
level = 1
change = "kept"
basis = "Nautical science (Abraham Zacuto, Pedro Nunes)."

[tree]
add = ["Arrowslits", "Hoardings"]
remove = []

# Renames of generic techs or units for this civ only.
# Example for another civ: from = "Horse Collar", to = "Chinampas" (Aztecs).
[[rename]]
from = "Hoardings"
to = "Hoardings"              # no change for the Portuguese; here only to show the format
level = 1

[architecture]
set = "Mediterranean"
```

## 9. Legal

- The project follows Microsoft's [Game Content Usage Rules](https://www.xbox.com/en-us/developers/rules): non-commercial, with the copyright notice, without suggesting any official link.
- The code comes from aoe2techtree (MIT licence); HSZemi's copyright notice stays.
- Before making the site public, we tell the aoe2techtree authors (SiegeEngineers / HSZemi). **[decided]**

## 10. Ideas kept for N2 and N3

- Split Archer and Crossbowman into two lines (N2: the graphics already exist).
- Blacksmith granularity: keep metallurgy shared and add technique techs per arm (couched lance for cavalry, pike drill for infantry).
- Defensive techs: boiling water and pitch, moat, talus (sloped wall base).
- A Samurai that switches between bow and sword (like the Ratha); javelins that reduce pierce armour (the *pilum* effect).
- No siege engines for the American civs; substitutes such as fire (Cuzco, 1536) and assault.
- Mule Cart extended to other pack-animal civs (Portuguese *almocreves*, Castilian *arrieros*); different animals (llamas, camels, yaks) are N3.
- A Dark Age that is less of a "hunting simulator": war bands and raids. Reconsider the name "Dark Age".
- Using Houses as walls is a gameplay exploit; fixing it requires engine changes (N3).
- A "Steppe" architecture set (N3).
