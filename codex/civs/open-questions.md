# Open questions for the owner

This file lists the design, scope, priority and taste questions that the level-1 designs leave to the owner ([RULES.md section 11](../RULES.md#11-who-decides)). Historical questions are settled in the civ files, with sources and contested notes.

The [level-1 review](../reviews/level-1-review.md) of 15 October 2026 triaged the 26 codex-wide questions (CQ1–CQ26) and the 464 per-civ questions of the drafts, and the owner accepted its recommendations. The decisions are now recorded in three places:

- **Each civ file** records its former questions as decisions in the elements they concern, and keeps the contested notes. Every file now has `open_questions = []`.
- **[RULES.md rule 6.16](../RULES.md#6-civ-design-rules)** holds the codex-wide conventions.
- **The review's [section 6](../reviews/level-1-review.md#6-codex-wide-questions), [section 7](../reviews/level-1-review.md#7-per-civ-questions-for-the-owner) and [section 9](../reviews/level-1-review.md#9-decisions-taken-after-the-review-15-october-2026)** give the recommendations and the owner's decisions.

The owner can reopen any of these decisions.

## Questions for the owner

None. None of the 52 civ files has an open question, and no design, scope, priority or taste question is waiting for the owner. New questions go here, under the civ's name and with a link to its file.

## Departures from the owner's decisions

In the points below, the fix pass did not carry out an owner decision or an owner sketch literally. The civ files give the reasons. Each departure stands until the owner confirms or overrules it.

- **English** ([English.toml](English.toml)). The archer passive is ‘Foot Archers attack +10/+18% faster in Castle/Imperial Age’, not the decided +10/+20% (review section 9, Britons Q2). A level-1 passive may only narrow an existing effect or lower its magnitude ([RULES.md section 5](../RULES.md#5-rework-levels)), and the highest existing attack-speed effect for Foot Archers is the Ethiopians' +18%. At +20% the passive would be level 2. Yeomen keeps the range as decided, and the N2 Longbowman rebalance can restore the two points.
- **Germans, unique units** ([Germans.toml](Germans.toml)). The mounted Teutonic Knight uses the Crusader Knight art and the Landsknecht the Heavy Pikeman art. Both are level 2 with adapted stats, as the owner's art-reuse rule allows (RULES section 5).
  - *Teutonic Knight.* The Crusader Knight's campaign values (18 attack, 4/4 armour) would break the class ceiling for mounted melee units and make the unit stronger than the Knight. The adapted stats are anchored on the Boyar. The unit keeps the model's speed of 1.2 and its immunity to conversion, and it gets an Elite tier through the game's Elite Teutonic Knight upgrade.
  - *Landsknecht.* The Heavy Pikeman's own stats would make it weaker than the Halberdier. The Landsknecht is anchored on the Elite Kamayuk and the Halberdier, costs the Condottiero's 50 food and 35 gold, and has no Elite tier.
- **Germans, bonuses and techs** ([Germans.toml](Germans.toml)). ‘Monks +100% healing range’ is kept as a fifth passive beside the four of the sketch, for the Order's origin as a hospital. That makes 5 passives and 3 techs, 8 in total, within the cap of 9. Gutenberg's Press, a fourth tech in the draft that the review left to the fix pass, is now an N2 idea, so the techs are the sketch's three.
- **Rus', Kalita** ([Rus.toml](Rus.toml)). The sketch asks for a small, flat gold trickle like the Feitoria's, but no tech gives one. Kalita takes the effect of Paper Money instead: ‘Lumberjacks slowly generate gold in addition to wood’ (Imperial Age, level 1). The Vietnamese design drops that tech. Burgundian Vineyards (Farmers) is not used, because it is the Tatars' Yarlyk. Beside the Cavalry Archer discount, it would make the Rus' copy two Tatar effects again, which the review (section 3.3) set out to end.
- **Rus', Pushechny Dvor** ([Rus.toml](Rus.toml)). The sketch asks for ‘cheaper and faster gunpowder units’. The design reads this as ‘Gunpowder Units cost -20% and train +25% faster’ (Imperial Age, level 2): faster training, not faster movement. It does not use the review's example effect, ‘Siege Workshop units cost -15%’.
- **Koreans** ([Koreans.toml](Koreans.toml)). The owner's sketch starts the whole range bonus in the Castle Age. In the design, the Cavalry Archer half starts in the Imperial Age: ‘Foot Archers +1 range starting in Castle Age; Cavalry Archers +1 range starting in Imperial Age’. The only existing range effect for mounted archers is the Magyars' Recurve Bow, an Imperial Age tech, and a reused effect never comes earlier than the game's age (RULES 6.16.11).
- **Tatars** ([Tatars.toml](Tatars.toml)). The review (section 3.3) suggested Silk Armor renamed *Quyaq*. The design keeps Silk Armor's effect under the name *Beglerbeg* (Castle, Imperial Age, level 1). Armour alone fails the relevance test (RULES 6.9), while the datable office that commanded the Horde's hosts passes it.
- **Castilians** ([Castilians.toml](Castilians.toml)). As decided (Castilians Q1), the *caballería de cuantía* is the Castle Age Castle tech, with ‘Stables work +20% faster’ (level 2). Órdenes Militares leaves the design instead of moving to another building, because with 6 passives and 3 techs the civ is at the cap of 9. The Elite Freire at 100 HP, which CQ9 would have allowed, therefore no longer arises: the Freire keeps the Monaspa's stats.
- **Franks and Burgundians** ([Franks.toml](Franks.toml), [Burgundians.toml](Burgundians.toml)).
  - *The line.* The review's shared test (section 3.2) keeps the Mounted Crossbowman line only where shooting from the saddle is documented. No French or Burgundian source used for these designs shows it. The Franks therefore lose the Mounted Crossbowman, the Heavy Mounted Crossbowman and Cranequins, and the Burgundians lose the Mounted Crossbowman. This reverses the accepted default of Burgundians Q4, under which the line stayed Frankish.
  - *Ordonnance Companies.* The Franks' tech now gives ‘Knight-line costs -60% gold’ (Szlachta Privileges shared; Town Center, Castle Age, level 1) for the men-at-arms of the 1445 companies.
  - *Return.* The line returns if a source shows French crossbowmen shooting from horseback.
- **Gaels** ([Gaels.toml](Gaels.toml)). The accepted default of Gaels Q3 renamed the Hussar ‘Hobelar’. The review (section 3.4) found that the hobelar was a troop type of the English lordship of Ireland, not a Gaelic one, so the name goes. The Hussar, a 15th-century Hungarian and Serbian type, is then removed rather than kept unrenamed, as in the Anglo-Saxon and Burgundian designs. Light Cavalry covers the Gaelic horsemen.
- **Byzantines** ([Byzantines.toml](Byzantines.toml)). The tree has the Traction Trebuchet instead of the counterweight Trebuchet that the draft kept.
  - *A game-role choice.* The counterweight engine did reach Byzantium: by 1165 on Chevedden's reading, at the end of the 12th century on Fulton's. Its removal is therefore not a CQ7 finding but a game-role choice. The two engines share one Imperial Age slot, and the core period (c. 670–1100) breaks the tie.
  - *In RULES.* RULES 6.16.5 now states this reading. The Chinese also keep the traction engine; the Bulgarians and Mongols keep the counterweight engine.
  - *N2.* A Komnenian siege tech that brings back the counterweight engine is an N2 idea.
- **Bohemians** ([Bohemians.toml](Bohemians.toml)). The window still starts in 872, although the review (section 3.4) noted that Bohemian dukes are first mentioned in 845. The start is now tied to the first mention of Bořivoj I, the first historical Přemyslid, because the design represents the Přemyslid duchy. The links between the dukes of 805 and 845 and that duchy are unknown. The profile records both dates.
- **Arabs** ([Arabs.toml](Arabs.toml)). Under Saracens Q8, the Dinar replaced Iqta' at the Town Center, and Iqta' is dropped as an element. The Sipahi effect stays with the Turks' Timar and the Hindustanis' Dagh. The design does not use the ‘Mounted Units +15% HP’ passive that the review pointed to (section 3.3): it would stack with ‘Camel Units +25% HP’, and a datable institution belongs in a tech (RULES 6.2). The iqta' history stays in the basis of the Heavy Cavalry Archer bonus.
- **Tatars and Ethiopians** ([Tatars.toml](Tatars.toml), [Ethiopians.toml](Ethiopians.toml)). Section 9 named the Scenario Editor's Ox Wagon and Donkey for the Mule Cart idea at later levels. The fix pass already uses them at level 1:
  - The Tatars' Mule Cart takes the Ox Wagon look as the *Araba*.
  - The Ethiopians' Mule Cart takes the Donkey look as the *Baql*.

  Both civs already hold the Mule Cart, so only its look and name change (RULES section 5). This is not the extension that CQ4 defers. The art, loads and scale must still be checked in the game.

## Fix pass

The scores, the changes of the fix pass and the cross-civ consistency check are in the review's [section 10, ‘Fix pass’](../reviews/level-1-review.md#10-fix-pass).
