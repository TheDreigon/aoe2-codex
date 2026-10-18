# Level-1 review

Review of the 52 level-1 drafts in `codex/civs/` (branch `level-1`, RULES v0.4.1), written by the project's historian and lead designer on 15 October 2026. Each civ was checked against the verified analysis of the original game civs (`codex/analysis/historical-accuracy-2026-10.json`), the game data and the rules, then cross-checked by region, and the 26 codex-wide questions (CQ1–CQ26) and 464 per-civ questions were triaged. Fidelity uses the analysis scale: 10 means the design faithfully captures the people's real character, 0 means arbitrary; the 56 original civs average 4.95.

## 1. Verdict

The level-1 drafts are a large, well-sourced improvement and are close to ready. No region contains a substantive factual error; the slips found are small and listed in section 3.4. All 52 files pass `validate_civs.py` with no errors.

| Measure | Result |
|---|---|
| Average fidelity, 52 civs in scope | **4.9 before → 7.2 after** |
| Distribution after rework | 16 civs at 8, 32 at 7, 4 at 6 |
| Largest gains (+4) | Gaels, Castilians, Goths, Armenians, Avars, Hindustanis |
| Smallest gains (+1) | Italians, Bohemians, Turks, Bengalis, Mapuche |
| Verdicts | 2 ready (Georgians, Persians), 49 minor fixes, 1 needs rework (Rus') |
| Design issues found | 2 major, 18 moderate, 106 minor |
| Per-civ questions | 464: 36 historical (ours), 413 take the file's default, 15 need the owner |

Every civ gains at least one point. None reaches 9: N1 itself (borrowed models, no new mechanics), umbrella civs spanning many centuries (Chinese, Franks, Gurjaras) and thin sources (Mapuche, Tupi, Muisca) hold the best designs back.

The remaining weaknesses are mostly not historical errors. There are four of them:

1. **Uneven criteria between regions.** The same evidence test gives different answers in different files: the Traction Trebuchet, river navies, northern gunpowder, the Mounted Crossbowman line.
2. **Heavy reuse of a small effect pool.** 32 of the 52 team bonuses duplicate another design's, and seven Town Center techs use the Kshatriyas effect.
3. **Two owner sketches never reached the designers.** The Rus' sketch, and a German proposal that was in fact ours.
4. **Too many questions addressed to the owner.** The files ask 464 per-civ and 26 codex-wide questions; 15 and 3 of them actually need the owner.

### Average fidelity by region

| Region | Civs | Before | After |
|---|---|---|---|
| Britain and France | 5 | 5.2 | 7.6 |
| Iberia and Italy | 4 | 5.3 | 7.5 |
| Central Europe | 5 | 5.2 | 7.0 |
| Scandinavia, the Rus' and the Goths | 5 | 4.6 | 7.2 |
| Byzantium, the Balkans and the Caucasus | 4 | 4.8 | 7.5 |
| The Steppe | 4 | 4.5 | 7.3 |
| The Islamic world and Africa | 6 | 4.8 | 7.0 |
| The Indian subcontinent | 4 | 5.0 | 7.5 |
| China and its northern neighbours | 3 | 5.0 | 7.3 |
| East and Southeast Asia | 6 | 5.0 | 7.3 |
| The Americas | 6 | 4.7 | 6.7 |

## 2. Fidelity before and after

Renamed civs are in bold. "Before" is the analysis score for the game's civ; "after" is our score for the draft.

| Game name | Codex name | Before | After | Verdict |
|---|---|---|---|---|
| Britons | Britons | 6 | 8 | minor fixes |
| Celts | **Gaels** | 3 | 7 | minor fixes |
| Saxons | Saxons | 6 | 8 | minor fixes |
| Franks | Franks | 5 | 7 | minor fixes |
| Burgundians | Burgundians | 6 | 8 | minor fixes |
| Spanish | **Castilians** | 4 | 8 | minor fixes |
| Portuguese | Portuguese | 5 | 7 | minor fixes (one major issue) |
| Italians | Italians | 6 | 7 | minor fixes |
| Sicilians | Sicilians | 6 | 8 | minor fixes |
| Teutons | **Germans** | 5 | 7 | minor fixes |
| Bohemians | Bohemians | 7 | 8 | minor fixes |
| Poles | Poles | 5 | 7 | minor fixes |
| Lithuanians | Lithuanians | 4 | 6 | minor fixes |
| Magyars | Magyars | 5 | 7 | minor fixes |
| Vikings | **Norwegians** | 6 | 8 | minor fixes |
| Danes | Danes | 5 | 7 | minor fixes |
| Varangians | **Swedes** | 4 | 7 | minor fixes |
| Slavs | **Rus'** | 5 | 7 | **needs rework** |
| Goths | Goths | 3 | 7 | minor fixes |
| Byzantines | Byzantines | 6 | 8 | minor fixes |
| Bulgarians | Bulgarians | 4 | 7 | minor fixes |
| Armenians | Armenians | 3 | 7 | minor fixes |
| Georgians | Georgians | 6 | 8 | ready |
| Huns | **Avars** | 3 | 7 | minor fixes |
| Mongols | Mongols | 6 | 8 | minor fixes |
| Tatars | Tatars | 4 | 7 | minor fixes |
| Cumans | Cumans | 5 | 7 | minor fixes |
| Saracens | Saracens | 5 | 7 | minor fixes |
| Persians | Persians | 5 | 7 | ready |
| Turks | Turks | 6 | 7 | minor fixes |
| Berbers | Berbers | 5 | 7 | minor fixes |
| Malians | Malians | 4 | 7 | minor fixes |
| Ethiopians | Ethiopians | 4 | 7 | minor fixes |
| Hindustanis | Hindustanis | 4 | 8 | minor fixes |
| Gurjaras | Gurjaras | 5 | 7 | minor fixes |
| Bengalis | Bengalis | 6 | 7 | minor fixes (8 with the Bombard Cannon) |
| Dravidians | **Tamils** | 5 | 8 | minor fixes |
| Chinese | Chinese | 5 | 7 | minor fixes |
| Jurchens | Jurchens | 6 | 8 | minor fixes |
| Khitans | Khitans | 4 | 7 | minor fixes |
| Japanese | Japanese | 5 | 7 | minor fixes |
| Koreans | Koreans | 6 | 8 | minor fixes |
| Vietnamese | Vietnamese | 5 | 7 | minor fixes |
| Khmer | Khmer | 6 | 8 | minor fixes |
| Burmese | Burmese | 4 | 7 | minor fixes |
| Malay | Malay | 4 | 7 | minor fixes |
| Aztecs | Aztecs | 5 | 7 | minor fixes |
| Maya | Maya | 4 | 7 | minor fixes |
| Inca | Inca | 6 | 8 | minor fixes |
| Muisca | Muisca | 4 | 6 | minor fixes |
| Mapuche | Mapuche | 5 | 6 | minor fixes |
| Tupi | Tupi | 4 | 6 | minor fixes |

The Rus' score measures the history, which is well sourced. The rework is needed because the file does not follow the owner's sketch (section 4).

## 3. Problems to fix

### 3.1 Fix before the drafts go back to the owner

| # | Files | Problem | Fix |
|---|---|---|---|
| 1 | `Rus.toml`, `Swedes.toml`, `README.md` | The composition ignores the owner's Rus' sketch. | Rebuild on the sketch (section 4). |
| 2 | `Portuguese.toml` | **Ordem de Cristo** gives up to +4 attack to every warship from the Castle Age. With four Relics the Fire Galley goes from 2 to 6 and the Fire Ship from 3 to 7 (both fire every 0.25 s), and the Caravel goes from 4 to 8. The game's highest Galley-line bonus is +2 (the Romans' Ballistas). | Galley line only, at most +2 (CQ9). The effect comes from the owner's sketch, so the owner confirms. |
| 3 | `Bengalis.toml` | The file drops every gun for lack of "lasting fame". The Sultanate's artillery is well attested from the 1510s to 1538: Barros, Babur in 1529, the Buranjis for 1532–33, and surviving Husain Shahi cannon. RULES section 2 asks for clear fame, and contemporary witnesses supply it. | Add the Bombard Cannon as the one late element. |
| 4 | `Tatars.toml` | All long-range siege is removed, although the file itself cites the Horde's engines at Caffa (destroyed in 1344; man-powered, per Zanders). Batu's army also used *poroki* at Vladimir (1238) and Kiev (1240). | Add the Traction Trebuchet, as for the Avars. |
| 5 | `Germans.toml`, `Poles.toml` | Burgenordnung copies the Italians' Comune. The kingdom's own knighthood has no element, and the Hanseatic civ lacks Shipwright. | Replace Burgenordnung with the **Golden Bull** (1356), with a new effect. Ius Teutonicum is a poor replacement: it is team-bonus material, it already grounds the Farms passive, and its stone effect would duplicate the Magyars' Royal Counties. Add the **Ministerialen** as the Castle Age Castle tech (Arnold 1985); the slot is free if the Landsknecht becomes a unit, otherwise we propose which tech yields. Add Shipwright and Light Cavalry. Both files should note that Danzig was under the Polish crown from 1454; the Peter von Danzig fits the Germans better (the Hanse's war with England, 1470–74). |
| 6 | `Bulgarians.toml` | Bagains is a rank used as a tech, and it repeats the Konnik's basis. Krum's siege train (812–814) has no slot. | Replace it with Krum's siege train: Ironclad renamed, Castle Age, level 1. Take 812–814 out of the siege passive's basis. |
| 7 | `Swedes.toml` | Guns are dropped because "no specific Swedish case" exists, but at Brunkeberg (1471) a Swedish hook-gun shot knocked out some of Christian I's teeth. Block Printing is missing, although Johann Snell printed at Stockholm in 1483. | Add Block Printing, by the same printing-date rule that keeps it for the Danes (Odense, 1482). Settle gunpowder for the Danes, Swedes, Norwegians and Rus' together under CQ25(d). Our reading: the Swedes get at least the Hand Cannoneer (Brunkeberg), and further gun items only on Swedish evidence; the Norwegians, whose window ends in 1469, stay without guns. |

### 3.2 Cross-civ consistency (historical calls we make in the fix pass)

- **Traction Trebuchet.** Write one test into the README. The Mangonel line is the light stone-thrower everywhere. The Traction Trebuchet is given wherever heavy stone-throwing engines are attested before the counterweight era.
  - The README should call the Japanese case a documented transfer (Goguryeo's gift of 618) and the Vietnamese case an inference. A check of the Yongzhou siege (1076) found towers and ramps but no stone-throwers.
  - Judge the Armenians by the Vietnamese standard. This is a historical question, so it is ours, not the owner's.
- **River navies (CQ1).** Classify navies by vessel, not by water: planked war galleys or ships count as a fleet of ships, dugouts and light boats as the boat tier. On that test:
  - The Rus' (monoxyla) stay in the boat tier.
  - The Khmer keep the full navy, with a basis line (the war galleys of the Bayon).
  - The Burmese and Bengalis need a basis line naming their war vessels, or drop to the boat tier.
  - The Magyars' full navy needs a basis line.
- **Mounted Crossbowman.** The Britons drop the line because their mounted archers shot on foot. The Franks and Burgundians keep it for the same kind of troops. Write one shared basis: keep the line only where shooting from the saddle is documented.
- **Americas.** Rest the Halberdier removal (Maya, Inca, Mapuche, Tupi) on the playability line of CQ12, not on its "European" name, since the files keep the Pikeman. The Inca have the strongest case for restoring it: Xerez (1534) describes axes "como alabarda" and pikes thirty palms long. Coinage is unflagged in four civs that had no coins (Inca, Muisca, Mapuche, Tupi): flag it as an abstraction or remove it (CQ20).
- **Islamic world.** Treadmill Crane is dropped for the Saracens but kept for the Berbers, Turks and Malians: make one choice for all four. Give the Saracens and Turks a shared contested note on timar origins (*pronoia*, Ostrogorsky; İnalcık).
- **Missing basis lines:**
  - Arbalester: Japanese (*ōyumi*) and Khmer (Bayon crossbows).
  - Navy tier: Persians (Dmitriev 2017; Daryaee) and Ethiopians (Kaleb's ten ships; raids to 702).
  - Thumb Ring: the Armenians need the historical reason, not the power reason, and must not present the Sasanian draw as settled.
  - Elite Battle Elephant: for the Gurjaras and Hindustanis, say that its absence is a design choice.
  - Counterweight Trebuchet: Bulgarians and Georgians (optional).
- **Other consistency points:**
  - The Portuguese (to 1521) and Berbers (to 1554) should point to CQ21.
  - One sentence in the README Method should make narrowed targets or lower magnitudes of an existing effect level 1. About a dozen designs already rely on it.
  - The Gaels should say why the Schiltron is a datable tech when the Saxons' shield wall is a passive.
  - Reserve trade gold for the Burgundians: drop the Britons' Calais Staple and the Franks' Champagne-fairs alternatives.

### 3.3 Reuse and homogeneity

Reuse is acceptable for N1 (CQ11), because each copy rests on its own history (RULES 6.7). The largest clusters go to a dedicated N2 pass:

| Reused element | Holders |
|---|---|
| Team bonus "Monasteries work +20% faster" | 8 designs |
| Kshatriyas effect at the Town Center | 7 designs |
| Team bonus "Universities work +80% faster" | 6 designs |
| Grand Trunk Road effect | 6 designs |
| Kamayuk unit model | 4 designs |
| Kipchak unit model | 4 designs, plus the Bulgarians through Cuman Alliance |

Cheap fixes worth making now:

- **Saracens:** five of the region's seven Town Center techs are land-revenue grants. Saracens Q8 (Abd al-Malik's reform) breaks that pattern. It also removes the Mamluk-with-Iqta' copy of the Hindustanis' Ghulam-with-Dagh; the Hindustani file already offers "Mounted Units +15% HP" for that.
- **Tatars:** their team bonus duplicates the Magyars' and Turks', so it counts once on a shared team. Give them a distinct team bonus and a different Beglerbeg effect (e.g. Silk Armor renamed *Quyaq*), which also stops the Rus' copying two Tatar effects.
- **Lithuanians:** raiding fills two slots and recreates the Britons' Chevauchée, while Europe's last pagan state has no element. Give one of those slots to paganism. Conversion resistance is acceptable here beside the Germans', since the readings differ (faith versus vows).
- **Bohemians:** the Czech mercenaries spread the wagon fort and handguns to Hungary, Poland and the Order (Marienburg 1457). They are a weightier team bonus than the groschen.
- **Elephants:** the Vietnamese get the largest Battle Elephant buff (Tượng Binh, +100 HP), although their own file calls their elephants secondary. The Khmer, for whom elephants were the royal arm, keep only +10% speed. Revisit Tượng Binh, and strengthen the Khmer elephant if the Khmer are strengthened.

### 3.4 Factual and wording corrections

| File | Correction |
|---|---|
| `Britons.toml` | The range basis projects the dismounted system of the 1330s back onto Falkirk (1298). |
| `Gaels.toml` | The Bruce raids and Bannockburn are overstated. The Hobelar was a troop type of the English lordship of Ireland, not a Gaelic one. |
| `Franks.toml` | Plate and barding are over-generalised. |
| `Bohemians.toml` | The Bohemian dukes are first mentioned in 845 (Annals of Fulda), not 872. |
| `Poles.toml` | The handgun breakthrough came only in the 1490s (Grabarczyk 2021). |
| `Rus.toml` | Pushechny Dvor: date it from Fioravanti's arrival in 1475 and the cannon house of 1488 (Ulyanov 2015), not 1479. Team bonus: add the treaties of 911 and 944 and *De Administrando Imperio* 9. Kalita: add a contested note on the tribute right of 1328/1331. |
| `Byzantines.toml` | The camel evidence omits the 6th-century camel riders. |
| `Avars.toml`, `Tatars.toml` | Theodor (not "A.") Mayer. The 2023 *Bulletin* article is Matt Field's, quoting Zanders, whose own paper dates from 2021. |
| `Saracens.toml` | The team bonus cites Avicenna's *Canon*, which was written at Iranian (Persian) courts; cite Abbasid or Fatimid works. |
| `Jurchens.toml` | The contested note says the Jin shi names the *zhentianlei* only at Kaifeng (1232), but the Jin shi also records it fired from boats at Hezhong (1231). |
| `Khitans.toml`, `Chinese.toml` | The Khitans field the Mangonel line as the Whirlwind Pao, a name from Song manuals, while the Chinese, who keep the Rocket Cart, lack that line. Add one clause saying that the one-blast-weapon convention mirrors the game's Rocket Cart civs. |
| `Aztecs.toml` | The famine origin of the flower wars is Ixtlilxóchitl's (doubted by Hicks 1979). Durán credits Tlacaelel under Moctezuma I. |
| `Inca.toml` | Team bonus: add the alliance of Viracocha Inca with Cari of Chucuito (Cieza, part II, chapters 42–43). Use Xerez (1534) to replace the equipment hedges. |
| `Tupi.toml` | Tumplines lacks a coastal source. At Igarassu the Caeté identification is Burton's footnote, not Staden's. |
| `Cumans.toml`, `Tatars.toml` | No "Qazaq" rename: the horseman sense of the word post-dates 1241. |

## 4. Civs that need rework

**Rus' (`Rus.toml`).** The history is good, but the file neither records nor follows the owner's Rus' sketch (chat, 15 October 2026), which the README Method omits while crediting the Japanese, Korean and Magyar outlines. Rus' question 1 thus asks the owner to approve a composition that departs from the owner's sketch in most slots without saying so.

The sketch predates RULES v0.4.1, which gave the Varangian elements to the Swedes. Only one point collides with that decision: the Knight-line trample (the Swedes' Vendel Legacy). Everything else should simply follow the sketch:

| Slot | Draft | Rebuild |
|---|---|---|
| Passives | Farmers +15%, Cavalry Archers -10/20%, Knight-line +1 pierce armour, Monks +20% speed | Farmers, Detinets (moved from a tech), Monks, fur-hunting gold (shared with the Swedes, RULES 6.7), and the Cavalry Archer discount as a fifth passive; the Knight-line armour passive leaves, since it would stack with the trample on the same line |
| Castle | Detinets | Druzhina (Castle Age; Knight-line trample is level 1, adding the Boyar makes it level 2) |
| Town Center | Poliud'e, Pomest'e (both Imperial Age) | Kalita (Imperial Age) |
| Monastery | Baptism of Rus' | Baptism of Rus' (the sketch's effect, if the owner fixed one) |
| Siege Workshop | — | Pushechny Dvor (Imperial Age, level 2, with an exclusive effect such as "Siege Workshop units cost -15%") |
| Ideas | — | Poliud'e and Pomest'e |

That is 5 passives and 4 techs, within the proposed cap of 9. The specific effects (Kalita's gold trickle, the Baptism's -50% Monastery techs, a team bonus from the Byzantine treaties and the Hanse trade) come from the chat proposal of 15 October 2026, which the owner liked. The only real question for the owner is the trample, asked together with Swedes question 2.

No other civ needs rework. The four civs at 6 are limited by sources or by N1, not by design errors:

- **Lithuanians:** the pagan-state slot (3.3).
- **Muisca:** a mostly generic military, the güechas' darts waiting for N2, and a Relic bonus that inverts the direction of the offerings.
- **Mapuche:** institutions inferred backwards from post-1541 sources.
- **Tupi:** thin passives, and capture warfare waiting for N2.

## 5. How the owner's sketches were handled

| Sketch or decision | Status |
|---|---|
| Castilians (debate sketch, regional Jinete, military-order knight) | Followed, with justified departures: Mesta as gold (the owner's shepherd effect stays available), cheaper Town Centers for the *repoblación*, and the Almogàver left to the future Aragonese. Open: the Castle tech (question 1), since the orders now fill both the unit and a tech. |
| Portuguese (Besteiro do Conto, Ordem de Cristo) | Followed; the magnitude of Ordem de Cristo must come down (3.1). |
| Japanese outline | Followed; question 3 on the passive count. |
| Korean outline | Followed; the Traction Trebuchet, Eupseong wording and renames are justified departures. |
| Magyar outline | Followed closely. |
| Armenians (Greater Armenia) | Followed; question 6 on the unique unit. |
| Persians (Central Asian architecture) | Implemented. |
| Americas without siege engines | Implemented; the rest of the American power budget is CQ12. |
| Avars' trebuchet bonus (RULES section 4) | Implemented, but the sources contradict the accuracy effect. Archbishop John contrasts the inaccurate Avar engines with accurate Roman torsion artillery (McCotter 2003). Question 1. |
| **Rus' sketch** | **Not passed to the designers**; rework (section 4). |
| **German sketch** | This was our own chat proposal, which the owner liked. It never reached the designers, so the file's departures are alternatives, not violations. The identity points become one owner question (Teutonic Knight model, Landsknecht unit); the rest are our historical calls (Golden Bull, Ministerialen, Shipwright, Light Cavalry). |

Lesson for the process: every sketch the owner approves in chat should be written into the repository before design work starts, and the README Method should list all of them.

## 6. Codex-wide questions

The README makes every convention a question for the owner, which conflicts with RULES section 11. Only three codex-wide questions need the owner. The rest should go into RULES v0.5 as decided conventions the owner can overrule, which removes the "pending the owner" boilerplate from about 40 file notes.

### Settled by us

| CQ | Decision |
|---|---|
| CQ1 Navy | Keep the three tiers and classify by vessel (3.2). Ask the owner only if they want playability on water maps to outrank history. |
| CQ2 Post-1500 skeleton items | Keep the Petard, demolition ships, Heated Shot and Galleon as flagged abstractions that do not count as the late element. |
| CQ3 Crossbows | Keep the generic Old World tier and none in the Americas; reword the convention as "Old World civs, as an abstraction". |
| CQ4 Mule Cart | Keep the four holders; any extension waits for N2/N3. |
| CQ5 Architecture | Historical fit decides. Keep the steppe stopgaps until the N3 Steppe set. |
| CQ6 Religious vocabulary | Generic names in N1; the site notes that "Monk" fits Muslim civs worst. |
| CQ7 Unreached siege engines | Remove them. The counterweight trebuchet appears in the 1160s–1180s and reached China in 1273. |
| CQ8 Regional units | No game-classified regional unit counts as a unique unit. |
| CQ9 Magnitude ceiling | Measure the ceiling per unit class. The Freire stands; Ordem de Cristo at +4 does not. |
| CQ10 Ages of reused effects | Keep the game's age or a later one, labelled on the site as a game constraint. |
| CQ11 Reuse | Accept it for N1. Identical team effects count once. Plan an N2 diversification pass. |
| CQ13 Long-range siege | Accept civs without it, and apply the traction test consistently. Nine designs remain without long-range siege after the Tatar and Bengali fixes. |
| CQ14 Power floor | No blanket compensation. Add only historically grounded extras (the Berbers' *tabiya* walls). |
| CQ15 Mapuche and Tupi team bonuses | Keep both and drop the "exception" label: alliances between autonomous polities are alliances between independent allies (RULES 6.2). |
| CQ17 Renames of shared items | Rename only when the item has the same function inside the window, the name is a period term, and the generic name is foreign or anachronistic. "Qazaq" fails, and "Sulica Rider" is flagged as a modern coinage. |
| CQ18 Reused names | Allowed (Ghulam, Teutonic Knight, Houfnice), with notes on the site. |
| CQ19 Labels | Follow the redesign, using the game's categories. |
| CQ20 American renames | Apply RULES 6.10 everywhere, including Coinage. |
| CQ21 Windows past 1500 | Allowed up to a terminal event soon after 1500, with a stated core. The Koreans and Malians state theirs. |
| CQ22 Romanization | Plain style for non-Latin scripts (Shugo-Jito, Pinyin without tones, Revised Romanization). Latin-script languages keep their diacritics. |
| CQ24 Timurid Siegecraft | Not for the Persians. Its best home is a Mongol Huihui Pao (1273), which is a design option. |
| CQ25 Rule interpretations | Codify the defaults: (a) chronological order binds only the two Castle techs; (b) a tradition stays a tech only as a flagged fallback; (c) defence lines go to the Castle, fortified towns to the Town Center; (d) the tree follows the represented period. |
| CQ26 Thumb Ring | Evidence-based; the 14 removals hold. |

### For the owner

| CQ | Our recommendation |
|---|---|
| CQ12 American power budget | Keep the removals of siege engines, crossbows, the Halberdier and the Galleon. Restore Blast Furnace, Plate Mail Armor and Ring Archer Armor as generic equipment levels, renamed where a documented equivalent exists: the kept Forging, Scale Mail and Chain Mail rest on the same non-historical footing. Reassess after the N2 bow split. |
| CQ16 Civ renames | Rename only where standard English scholarship does not use the game's name for the design's entity. Britons → English; Saxons → Anglo-Saxons (decided as a pair, the term flagged as contested); Saracens → Arabs. The others keep their names. |
| CQ23 Genitour beyond Iberia and the Maghreb | Extend it to the Lithuanians, whose javelin light horse was the core of their raiding. Not to the Malians. |

## 7. Per-civ questions for the owner

Of the 464 per-civ questions, 15 need the owner, and two of them form one decision. They are ordered by how much they change a civ's identity.

| Civ | Question | Our recommendation |
|---|---|---|
| Rus' Q1 + Swedes Q2 | Who gets the Knight-line trample? | The Rus' Druzhina, as in the owner's sketch. The Swedes take an Engelbrekt/Sture peasant-army tech, and the Alsnö Stadga returns to the Castle Age. |
| Germans Q2 | (a) Teutonic Knight on the Boyar or the Monaspa model; (b) Landsknecht as a unit or a tech? | (a) Monaspa: the model the owner liked, which pairs the two military-order units and avoids mirroring both the Rus' and the Lithuanians. (b) The owner's call: a unit is more visible and frees a slot for the Ministerialen, but the Condottiero's anti-gunpowder role misrepresents a pike-and-shot block. |
| Gaels Q1 | Include the kingdom of Scotland? | Yes. Bruce's war had a Gaelic side, and without Scotland the civ loses its Castle tech and its only long-range siege. |
| Britons Q2 | Range or rate of fire? | Keep range once, through Yeomen, and make the passive "Foot Archers attack +10/+20% faster" (Strickland and Hardy; Curry). |
| Portuguese Q5 | Ordem de Cristo magnitude | Galley line only, at most +2. |
| Avars Q1 | Trebuchet accuracy or cost? | "Traction Trebuchets cost -25%": the sources stress the number of engines, not their accuracy. |
| Saracens Q8 | Early caliphate at the Town Center? | Yes: Abd al-Malik's coinage and diwan reform (696–700), "All gold income +10% faster" (level 2), with Bimaristan moved to the Monastery. |
| Mapuche Q1 | Confirm the pre-Hispanic recentring? | Confirm it, with the Kona as the one late element. |
| Castilians Q1 | Castle tech | (b) The *caballería de cuantía* (Cortes of Alcalá 1348, precursor at Burgos 1338). |
| Italians Q7 | Arsenale at the Dock? | Yes (level 2). Naval primacy otherwise rests on half a passive. It takes the civ to the cap of 9. |
| Armenians Q6 | Agheghnavor or a cavalry unique unit? | Keep the Agheghnavor for N1 and plan the N2 lance-and-bow noble horseman. Do not share the Cataphract. |
| Khitans Q2 | Chanyuan Treaty or the dual administration? | The dual administration (level 2, Town Center), with the Chanyuan Treaty moved to the Market. Keep the Chanyuan Treaty only if the owner wants to limit level-2 items. |
| Japanese Q3 | Passive count | Drop "Cavalry Archers +2 attack vs. Ranged" and add Genkō Bōrui (1276) as the Castle Age Castle tech. |
| Malay Q1 | Scope without Java | Accept it, and record a Javanese civ (Mataram–Majapahit) as an N3 roster proposal. |

**All other per-civ questions take the recommended default.** The 36 historical ones are ours: they are settled in the files with sources and contested notes. The other 413 take the file's default or follow the codex-wide question they point to. The owner can reopen any of them, but none waits on the owner.

## 8. Next steps

1. **Owner answers** CQ12, CQ16 and CQ23 and the per-civ list above. The first eight rows are the ones that change identity.
2. **Fix pass (ours).** Rebuild the Rus'. Apply sections 3.1, 3.2 and 3.4 and the cheap fixes of 3.3. Then fold in the owner's answers.
3. **README.** List every owner sketch in the Method. Reword the Traction Trebuchet, navy and crossbow conventions. Add the level-1 narrowing rule. Remove the line that makes every convention an owner question.
4. **RULES v0.5.** Promote the settled codex-wide defaults (section 6) to decided conventions, with the owner's overrule kept.
5. **Prune `open-questions.md`** down to the owner's list. Record the defaults as decisions in the files, keeping the contested notes.
6. **Re-validate and re-score** the changed files, then move them from `draft` to `reviewed`.
7. **Then:** the history texts (`codex/history/`), the site, and N2 planning. The first N2 tasks are a diversification pass for team bonuses and Town Center techs, the bow/crossbow split, and the N2 units the files already propose (Besteiro, the Armenian noble horseman, the Muisca dart-thrower, an armoured Ghulam).

## 9. Decisions taken after the review (15 October 2026)

The owner accepted every recommendation of sections 6 and 7. The decisions below are final for the fix pass; the owner can still overrule any of them.

### Owner decisions

| Item | Decision |
|---|---|
| Rus' Q1 + Swedes Q2 | The Knight-line trample goes to the Rus' Druzhina. The Swedes replace Vendel Legacy with an Engelbrekt/Sture peasant-army tech; the Alsnö Stadga returns to the Castle Age. |
| Germans Q2 | The Teutonic Knight becomes mounted, modelled on the **Crusader Knight** (see below), not the Monaspa. The Landsknecht is a unit; the Ministerialen take the Castle Age Castle tech. |
| Portuguese Q5 | Ordem de Cristo: Galley line only, at most +2. |
| Britons Q2 | Range stays once, through Yeomen; the passive becomes "Foot Archers attack +10/+20% faster". |
| Japanese Q3 | Drop "Cavalry Archers +2 attack vs. Ranged"; add Genkō Bōrui (1276) as the Castle Age Castle tech. |
| CQ12 Americas | Keep the removals of siege engines, crossbows, the Halberdier and the Galleon; restore Blast Furnace, Plate Mail Armor and Ring Archer Armor as generic equipment levels, renamed where a documented equivalent exists. |
| CQ23 Genitour | Extend the regional Genitour to the Lithuanians (not the Malians). |
| Italians Q7 | Add the Arsenale at the Dock (level 2). |

### Historical calls (settled by Claude, RULES section 11)

| Item | Decision |
|---|---|
| CQ16 renames | Britons → **English**; Saxons → **Anglo-Saxons** (term flagged as contested); Saracens → **Arabs**. The other civs keep their names. |
| Avars Q1 | The trebuchet effect becomes "Traction Trebuchets cost -25%" (RULES section 4 is updated accordingly). |
| Gaels Q1 | The medieval kingdom of Scotland is included. |
| Saracens Q8 | Abd al-Malik's coinage and diwan reform (696–700) at the Town Center; Bimaristan moves to the Monastery. |
| Mapuche Q1 | The pre-Hispanic recentring stands, with the Kona as the one late element. |
| Castilians Q1 | The *caballería de cuantía* (1338/1348) is the Castle tech. |
| Armenians Q6 | Keep the Agheghnavor in N1; the noble horseman is an N2 idea. |
| Khitans Q2 | The dual administration is the Town Center tech (level 2); the Chanyuan Treaty moves to the Market. |
| Malay Q1 | Scope without Java; a Javanese civ (Mataram–Majapahit) is recorded as an N3 roster proposal. |
| All other questions | Sections 6 and 7 apply as written: every other codex-wide and per-civ question takes the recommended default. |

### Scenario Editor units are existing content

The game contains units that no civ can train in normal play but that exist, with art and data, in campaigns and the Scenario Editor. They are existing game content, so a Level 1 design may use them as models (RULES section 5, implementation cost). The owner pointed out the first case: the **Crusader Knight** (Dawn of the Dukes) is a mounted knight in white robes with the black cross of the Teutonic Order and cannot be converted, which makes it the natural model for the mounted Teutonic Knight. The full list is in [`../tools/scenario-units.md`](../tools/scenario-units.md). Candidates worth checking in the fix pass (each still needs the usual historical review):

- **Mounted Samurai**: the Heian–Kamakura mounted warrior for the Japanese.
- **Pagan Priest**: the missing pagan slot of the Lithuanians (section 3.3).
- **Canoe**: the boat tier of canoe navies (CQ1), in the Americas and elsewhere.
- **Heavy Crossbowman**, **Heavy Pikeman**, **Heavy Swordsman**, **Eastern Swordsman**, **Norse Warrior**, **Khan**, **Sogdian Cataphract**, **Flamethrower**: possible models where a current borrowing fits poorly (for example the Landsknecht, the Tamil or Chinese fire weapons, the Armenian or Persian heavy horse).
- **Donkey**, **Ox Cart**, **Ox Wagon**: pack and draught animals for the Mule Cart idea (CQ4, later levels).
- **Iroquois Warrior**: a model for a future North American civ.

### Owner sketches not passed to the designers

These two sketches come from the chat of 15 October 2026 and are now recorded here, as section 5 recommends.

**Rus'** (window from c. 882): passives Farmers +15%, hunting also generates gold (the fur trade), Detinets as a passive (a structural wooden-fortification tradition), Monks +20% speed; Boyar kept; techs Druzhina (Vendel Legacy's trample for the Boyar and the Knight line, Castle), Kalita (Town Center, a small gold trickle like the Feitoria; Ivan I's collection of the Horde's tribute), Baptism of Rus' (Monastery, Monastery technologies -50%), Pushechny Dvor (Siege Workshop, cheaper and faster gunpowder units, dated per section 3.4); team bonus trade gold for allies (the treaties with Byzantium of 911 and 944, Novgorod's trade with the Hanse); tree adds the Hand Cannoneer, Bombard Cannon, Bombard Tower, Thumb Ring and Bracer, removes the Cannon Galleon.

**Germans** (window 919–1500): mounted Teutonic Knight and Landsknecht as unique units; passives Burgen garrison, +1/+2 melee armour, Farms -40% (Ostsiedlung), conversion resistance moved from the team bonus to a passive; techs Ministerialen (Castle), a Town Center tech (now the Golden Bull, per section 3.1), Hanse (Dock); team bonus Bergrecht (German miners abroad); tree adds Arbalester, Gold Shaft Mining, Architecture, Treadmill Crane, Dry Dock, Shipwright and Light Cavalry.

## 10. Fix pass

The fix pass of sections 3, 4, 6, 7 and 9 was carried out between 15 and 18 October 2026 on branch `level-1`. After it, every file passes `validate_civs.py`, every file has `open_questions = []`, and all 52 files have `status = "reviewed"`.

### Result

| Measure | Result |
|---|---|
| Average fidelity, 52 civs | **4.9 in the game → 7.2 in the review → 7.5 after the fix pass** (7.46) |
| Distribution | 27 civs at 8, 22 at 7, 3 at 6 |
| Changed scores | 12 civs gain a point (Italians, Germans, Lithuanians, Swedes, Bulgarians, Avars, Arabs, Berbers, Bengalis, Khitans, Japanese, Aztecs); none loses one |
| Questions for the owner | none ([`../civs/open-questions.md`](../civs/open-questions.md) lists the departures from the owner's decisions) |

Each region was scored blind by two independent scorers on the analysis scale; a third scorer decided where they disagreed (Lithuanians, Rus', Avars, Gurjaras, Bengalis, Khitans, Maya). The scorers also judged whether each file could be marked reviewed. Five files were held back by concrete blockers (Avars, Vietnamese, Gurjaras, Bengalis, Maya); commit 040f9b9 resolved them, and an independent check confirmed it.

| Region | Civs | Game | Review | Fix pass |
|---|---|---|---|---|
| Britain and France | 5 | 5.2 | 7.6 | 7.6 |
| Iberia and Italy | 4 | 5.3 | 7.5 | 7.8 |
| Central Europe | 5 | 5.2 | 7.0 | 7.4 |
| Scandinavia, the Rus' and the Goths | 5 | 4.6 | 7.2 | 7.4 |
| Byzantium, the Balkans and the Caucasus | 4 | 4.8 | 7.5 | 7.8 |
| The Steppe | 4 | 4.5 | 7.3 | 7.5 |
| The Islamic world and Africa | 6 | 4.8 | 7.0 | 7.3 |
| The Indian subcontinent | 4 | 5.0 | 7.5 | 7.8 |
| China and its northern neighbours | 3 | 5.0 | 7.3 | 7.7 |
| East and Southeast Asia | 6 | 5.0 | 7.3 | 7.5 |
| The Americas | 6 | 4.7 | 6.7 | 6.8 |


Bold codex names are renamed civs; bold scores changed in the fix pass.

| Game name | Codex name | Game | Review | Fix pass |
|---|---|---|---|---|
| Britons | **English** | 6 | 8 | 8 |
| Celts | **Gaels** | 3 | 7 | 7 |
| Saxons | **Anglo-Saxons** | 6 | 8 | 8 |
| Franks | Franks | 5 | 7 | 7 |
| Burgundians | Burgundians | 6 | 8 | 8 |
| Spanish | **Castilians** | 4 | 8 | 8 |
| Portuguese | Portuguese | 5 | 7 | 7 |
| Italians | Italians | 6 | 7 | **8** |
| Sicilians | Sicilians | 6 | 8 | 8 |
| Teutons | **Germans** | 5 | 7 | **8** |
| Bohemians | Bohemians | 7 | 8 | 8 |
| Poles | Poles | 5 | 7 | 7 |
| Lithuanians | Lithuanians | 4 | 6 | **7** |
| Magyars | Magyars | 5 | 7 | 7 |
| Vikings | **Norwegians** | 6 | 8 | 8 |
| Danes | Danes | 5 | 7 | 7 |
| Varangians | **Swedes** | 4 | 7 | **8** |
| Slavs | **Rus'** | 5 | 7 | 7 |
| Goths | Goths | 3 | 7 | 7 |
| Byzantines | Byzantines | 6 | 8 | 8 |
| Bulgarians | Bulgarians | 4 | 7 | **8** |
| Armenians | Armenians | 3 | 7 | 7 |
| Georgians | Georgians | 6 | 8 | 8 |
| Huns | **Avars** | 3 | 7 | **8** |
| Mongols | Mongols | 6 | 8 | 8 |
| Tatars | Tatars | 4 | 7 | 7 |
| Cumans | Cumans | 5 | 7 | 7 |
| Saracens | **Arabs** | 5 | 7 | **8** |
| Persians | Persians | 5 | 7 | 7 |
| Turks | Turks | 6 | 7 | 7 |
| Berbers | Berbers | 5 | 7 | **8** |
| Malians | Malians | 4 | 7 | 7 |
| Ethiopians | Ethiopians | 4 | 7 | 7 |
| Hindustanis | Hindustanis | 4 | 8 | 8 |
| Gurjaras | Gurjaras | 5 | 7 | 7 |
| Bengalis | Bengalis | 6 | 7 | **8** |
| Dravidians | **Tamils** | 5 | 8 | 8 |
| Chinese | Chinese | 5 | 7 | 7 |
| Jurchens | Jurchens | 6 | 8 | 8 |
| Khitans | Khitans | 4 | 7 | **8** |
| Japanese | Japanese | 5 | 7 | **8** |
| Koreans | Koreans | 6 | 8 | 8 |
| Vietnamese | Vietnamese | 5 | 7 | 7 |
| Khmer | Khmer | 6 | 8 | 8 |
| Burmese | Burmese | 4 | 7 | 7 |
| Malay | Malay | 4 | 7 | 7 |
| Aztecs | Aztecs | 5 | 7 | **8** |
| Maya | Maya | 4 | 7 | 7 |
| Inca | Inca | 6 | 8 | 8 |
| Muisca | Muisca | 4 | 6 | 6 |
| Mapuche | Mapuche | 5 | 6 | 6 |
| Tupi | Tupi | 4 | 6 | 6 |

The scores still stop at 8 for the reasons of section 1: level 1 itself, umbrella windows and thin sources. The Muisca, Mapuche and Tupi stay at 6 for the reasons of section 4.

### What changed

- **Rules and tools.** RULES v0.5: the codex-wide questions became decided conventions (6.16, with the traction-test readings and the one-heavy-engine rule in 6.16.5, and bonus stacks in 6.16.12). Units of the campaigns and the Scenario Editor count as existing content, and the owner's art-reuse rule sets the levels: as it is N1, with adapted stats N2, new art N3. Narrowed or weaker passive and team effects are level 1. Section 4 records the three renames, the Avars' cheaper traction trebuchets, and the Mississippians and Javanese as N3 proposals; section 12 is the changelog. `validate_civs.py` accepts Scenario Editor models and level-2 units with a `stats` key. The base stats of the Scenario Editor units are in [`../tools/scenario-units-stats.md`](../tools/scenario-units-stats.md).
- **Renames.** Britons → **English**, Saxons → **Anglo-Saxons** (the term is flagged as contested), Saracens → **Arabs**, with `original_name` and renamed files.
- **Rus' rebuilt on the owner's sketch.** The passives are Farmers, hunting gold (the fur trade), Detinets, Monks and the Cavalry Archer discount. The techs are the Druzhina (trample for the Boyar and the Knight line), Kalita, the Baptism of Rus' (Monastery technologies -50%) and Pushechny Dvor, dated from the cannon house of 1488. Poliud'e and Pomest'e become ideas, and the team bonus adds the treaties of 911 and 944.
- **Swedes.** Engelbrekt's Rising replaces Vendel Legacy, Alsnö Stadga returns to the Castle Age, and the Hand Cannoneer (Brunkeberg, 1471) and Block Printing (Stockholm, 1483) join the tree.
- **Germans on the German sketch.** The Teutonic Knight uses the Crusader Knight art and the Landsknecht the Heavy Pikeman art, both at level 2 with adapted stats: as they are, the first exceeded the cavalry attack ceiling and the second was weaker than the Halberdier. Ministerialen is the Castle tech and the Golden Bull the Town Center tech. The Hanse moves to the Dock, Light Cavalry and Shipwright join, the Peter von Danzig moves here, and Gutenberg's Press becomes an idea.
- **Owner decisions and our historical calls executed.**
  - English: rate of fire in place of range.
  - Portuguese: Ordem de Cristo for the Galley line, +2.
  - Japanese: Genko Borui.
  - Italians: the Arsenale, and the Cannon Galleon restored on Chioggia (1379–80).
  - Khitans: the dual administration, with the Chanyuan Treaty at the Market.
  - Arabs: Abd al-Malik's Dinar, with Bimaristan at the Monastery.
  - Castilians: the caballería de cuantía.
  - Avars: Traction Trebuchets cost -25%.
  - Gaels: Scotland included.
  - Americas: Blast Furnace, Plate Mail Armor and Ring Archer Armor restored.
  - Lithuanians: the Genitour (Sulica Rider) and a pagan conversion-resistance passive.
  - Bengalis: the Bombard Cannon.
  - Tatars: the Traction Trebuchet, a church-patent team bonus and Silk Armor's effect as the Beglerbeg.
  - Bulgarians: Krum's Siege Train.
  - Bohemians: the Czech mercenaries as the team bonus.
  - Malay: the Javanese civ recorded as an N3 proposal.
- **Shared tests applied across the codex.**
  - Navies are classified by vessel: the Magyars and Burmese drop to the boat tier, and the Canoe look goes to the Aztecs, Maya, Mapuche, Tupi, Malians and Avars.
  - The traction test: the Armenians (a flagged inference) and the Byzantines (one heavy engine for their core) take the Traction Trebuchet.
  - The Mounted Crossbowman stays only where shooting from the saddle is documented, which leaves only the Germans; the Franks' Ordonnance Companies now cheapens the Knight line.
  - The Treadmill Crane has one reading for the Islamic world, and the Inca rename it Mit'a.
  - Gunpowder follows the represented period (6.16.19(d)): the Vietnamese lose the Cannon Galleon, while the Burgundians keep theirs on a gun-armed galley of 1445.
  - The Avars lose the Hussar.
- **Scenario Editor units.**
  - Adopted where they fit: the Crusader Knight, Heavy Pikeman, Canoe, Ox Wagon (the Tatars' Araba) and Donkey (the Ethiopians' Baql).
  - Weighed and declined: the Mounted Samurai, a melee unit while the Heian–Kamakura warrior was a mounted archer; the Pagan Priest, kept as an N2 idea; and others, with the reasons in the files.
- **Corrections and questions.** Every correction of section 3.4 is applied. The claims the historians could not confirm are reworded or flagged in the files. The 464 per-civ and 26 codex-wide questions are recorded as decisions with their contested notes. The README index, conventions and method are rewritten.

### Departures and open points

There are no questions left for the owner. [`../civs/open-questions.md`](../civs/open-questions.md) lists 14 departures from the owner's decisions or sketches, each with its reason, for the owner to confirm or overrule. The main ones:

- the English passive is +10/+18%, because a level-1 passive cannot exceed the game's existing +18%;
- the two German units are at level 2;
- the Germans keep a fifth passive (Monks heal at range);
- the effects chosen for the Rus' Kalita and Pushechny Dvor;
- the Franks' and Burgundians' Mounted Crossbowman line is removed.

### Process

1. RULES v0.5 groundwork.
2. One fixer per region; per region, one or two skeptical historians (web search allowed) and a rules auditor. The fixer applied or rebutted every finding, then an independent verifier and a final fix (11 regions, about 400 findings).
3. A cross-civ check with 13 independent lenses: six on cross-references, three on conventions, a completeness critic and three on unconfirmed claims. A cross-civ fix round per region followed, with its own verification.
4. The README and `open-questions.md` were rewritten.
5. Blind re-scoring with adjudication; the last blockers were fixed and checked.

Each step was committed separately.

### Limits and next steps

- The fandom wiki was blocked and direct page fetches often failed from the cloud, so many checks rest on search results. Points that could not be confirmed at first hand are flagged in the files.
- The level-2 unit stats, the Scenario Editor looks and the bonus stacks are untested in the game.
- Reuse remains high for N1 (the Monasteries and trade team bonuses, the Grand Trunk Road, Kshatriyas and Persian Town Center effects, the Kamayuk and Kipchak models). This is the first task of the N2 diversification pass.
- Next: the history texts (`codex/history/`), the site's historical mode and N2 planning (section 8, step 7).
