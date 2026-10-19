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

None remain. The fix pass listed thirteen points in which it had not carried out an owner decision or sketch literally; the owner answered them on 19 October 2026, and the outcomes are in the next section.

## Settled by the owner after the fix pass

On 19 October 2026 the owner settled the English archer passive and the place of balance, and answered the fix pass's thirteen departures in one numbered list (answers 1–13). The list was read by content: answers 1–4 go to the two German and the two Rus' points, answer 5 (the armour's name) to the Tatars' tech, answer 6 to the Castilians, answers 7 (the 60%) and 8 to the Franks and Burgundians, and answers 9–13 to the last five points in order. No answer was read as addressing the Koreans, so their design stands. The owner can correct this reading. Each point gives the outcome as it now stands in the civ file.

- **English** ([English.toml](English.toml)), 19 October 2026: the archer passive is ‘Foot Archers attack +10/+20% faster in Castle/Imperial Age’, as the owner decided, as a level-2 passive (a new magnitude of the Ethiopians’ +18%).
- **Balance** ([RULES.md rule 6.14](../RULES.md#6-civ-design-rules)), 19 October 2026: realism comes first and balance second; designs keep a minimum of balance wherever history leaves a choice.
- **Germans, Teutonic Knight** ([Germans.toml](Germans.toml); answer 1). The unit is the game's Teutonic Knight with the Crusader Knight art (level 2): mounted and counted as cavalry, speed 1.2 instead of 0.8, attack 12 (Elite 15) instead of 14 (17), the game's other values, and convertible like the game's unit. Fully upgraded, the Elite tier keeps the game's 13/6, a melee armour above the mounted class ceiling: an exception by the owner's decision (RULES 6.16.11). The Landsknecht is unchanged.
- **Germans, bonuses and techs** ([Germans.toml](Germans.toml); answer 2). For now the Monks' healing-range passive stays as a fifth passive and Gutenberg's Press returns as a fourth tech (University, Imperial Age, ‘University technologies cost -25%’, level 2): 5 passives and 4 techs, the cap of 9.
- **Rus', Kalita** ([Rus.toml](Rus.toml); answer 3). On the historically best effect, Kalita takes Burgundian Vineyards' ‘Farmers slowly generate gold in addition to food’ (Town Center, Imperial Age, level 1) for the Horde's tribute, levied on a farming population and collected by Moscow in silver. With the Tatars' Yarlyk it renders the two sides of one tribute (RULES 6.7); Paper Money's lumberjack gold is set aside.
- **Rus', Pushechny Dvor** ([Rus.toml](Rus.toml); answer 4). The design's reading stands: ‘Gunpowder Units cost -20% and train +25% faster’ (Siege Workshop, Imperial Age, level 2).
- **Koreans** ([Koreans.toml](Koreans.toml); no answer read). The design stands: ‘Foot Archers +1 range starting in Castle Age; Cavalry Archers +1 range starting in Imperial Age’, since a reused effect never comes earlier than the game's age (RULES 6.16.11).
- **Tatars, Quyaq** ([Tatars.toml](Tatars.toml); answer 5). Silk Armor's effect is now named *Quyaq*, the armour of the Horde's horsemen, as the review (section 3.3) suggested (Castle, Imperial Age, level 1). The beglerbeg office stays as context, and the tech is flagged as a fallback for a long tradition (RULES 6.16.19(b)).
- **Castilians** ([Castilians.toml](Castilians.toml); answer 6). Órdenes Militares stays out: the Freire renders the military orders' knights and the castle and repoblación passives their castles and charters, so a tech would be a second high slot for one institution in a civ at the cap of 9. The Freire keeps the Monaspa's stats.
- **Franks and Burgundians** ([Franks.toml](Franks.toml), [Burgundians.toml](Burgundians.toml); answers 7 and 8). The removal of the Mounted Crossbowman line stands on the historical test; the line returns if a source shows French crossbowmen shooting from horseback. Ordonnance Companies now gives ‘Knight-line costs -30% gold’ (Town Center, Castle Age, level 2), half of Szlachta Privileges' -60%, because the Franks keep the Paladin and the mounted HP passive.
- **Gaels** ([Gaels.toml](Gaels.toml); answer 9). The Hussar's removal stands: the hobelar was a troop type of the English lordship of Ireland, and the Hussar a 15th-century Hungarian and Serbian one. Light Cavalry covers the Gaelic horsemen.
- **Byzantines** ([Byzantines.toml](Byzantines.toml); answer 10). The Traction Trebuchet stands: the traction engine served across the whole window, the counterweight engine only in its last third (from 1165 or the end of the 12th century). A Komnenian siege tech that brings back the counterweight engine stays an N2 idea.
- **Bohemians** ([Bohemians.toml](Bohemians.toml); answer 11). The window still starts in 872, with the first mention of Bořivoj I, the first historical Přemyslid, because the design represents the Přemyslid duchy; the profile records the dukes of 805 and 845.
- **Arabs** ([Arabs.toml](Arabs.toml); answer 12). The iqta' returns as a passive, ‘Mounted Units take -20% population space starting in Imperial Age’ (Aznauri Cavalry's effect, level 1): the land revenue that maintained the cavalry, a long institution without a founding act (RULES 6.2). The Dinar keeps the Town Center; 5 passives and 3 techs.
- **Tatars and Ethiopians** ([Tatars.toml](Tatars.toml), [Ethiopians.toml](Ethiopians.toml); answer 13). The Mule Cart keeps the Scenario Editor's Ox Wagon look as the Tatars' *Araba* and the Donkey look as the Ethiopians' *Baql* (level 1). The art, loads and scale must still be checked in the game.

## Fix pass

The scores, the changes of the fix pass and the cross-civ consistency check are in the review's [section 10, ‘Fix pass’](../reviews/level-1-review.md#10-fix-pass).
