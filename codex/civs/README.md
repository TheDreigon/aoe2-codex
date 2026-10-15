# Level 1 civ designs

This folder holds the **Level 1 (N1)** design of every civilization in scope: the 56 civs of Age of Empires II: Definitive Edition minus the four out of scope ([Shu, Wei, Wu and Romans](../out-of-scope.md)), so 52 files. Level 1 means *redistribute*: every change reuses something that already exists in the game ([RULES.md section 5](../RULES.md#5-rework-levels)). All files follow [RULES.md](../RULES.md) version 0.4.1 and are **drafts** (`status = "draft"`) for review with the project owner.

## Index

Grouped by the regions of [`../tools/regions.json`](../tools/regions.json). "Game name" is the civ as the game shows it now; "Name" is the redesigned civ (renamed civs carry `original_name` in their file). The window is the period the design represents.


### Britain and France

| Game name | Name | Window | Main changes | File |
|---|---|---|---|---|
| Britons | Britons | 1066–1485 | England after 1066 (core c. 1277–1453): Yeomen moves to the Town Center, the Chevauchée replaces Warwolf, dismounted men-at-arms gain armour, archers serving allies carry the team bonus, and the Mounted Crossbowman line leaves the tree as Bombard Cannon, Carrack and Crop Rotation join it. | [Britons.toml](Britons.toml) |
| Celts | **Gaels** | 563–1500 | Celts reworked as the Gaels of Ireland and Scotland (563–1500): a cattle-and-dairy economy and castle-taking infantry replace the invented siege identity, the Kern (Woad Raider renamed) is the unique unit, the Schiltron and Buannacht are the techs and the Irish missions the team bonus. | [Gaels.toml](Gaels.toml) |
| Saxons | Saxons | 449–1066 | Anglo-Saxon England (449–1066) rebuilt around the burh and the fyrd: earthwork walls and garrisoned towns replace castle arrows, the shield wall becomes a passive, the Fyrd and Edgar's Recoinage are the new techs, the continental missions the team bonus, and post-1066 items leave the tree. | [Saxons.toml](Saxons.toml) |
| Franks | Franks | 481–1500 | The Frankish kingdoms and France (481–1500): knights, mills, cheap castles and the Throwing Axeman stay, Gothic building replaces the forager bonus, the University of Paris the team bonus, Ordonnance Companies moves to the Town Center and the Bureau Brothers take Chivalry’s Castle slot. | [Franks.toml](Franks.toml) |
| Burgundians | Burgundians | 1363–1477 | Valois Burgundy (1363–1477): the economic, Cavalier and gunpowder bonuses stay, archers replace the stable discount, the Bruges trade becomes the team bonus, the 1433–34 common coinage the Town Center tech, Vineyards moves to the Mill and the Order of the Golden Fleece replaces Flemish Revolution. | [Burgundians.toml](Burgundians.toml) |

### Iberia and Italy

| Game name | Name | Window | Main changes | File |
|---|---|---|---|---|
| Spanish | **Castilians** | 1037–1504 | Spanish renamed Castilians for the medieval Crown of Castile (1037–1504): the Freire of the military orders replaces the Conquistador and Missionary, the Santa Hermandad and Bula de Cruzada replace Supremacy and Inquisition, and the Mesta, cheaper castles, Santiago's relic and the crossbow come in. | [Castilians.toml](Castilians.toml) |
| Portuguese | Portuguese | 1139–1521 | Portuguese as the medieval kingdom and its expansion (1139–1521): the Besteiro do Conto replaces the Organ Gun beside the Caravel, crossbow and fishing bonuses replace the gold and forager ones, and Aljubarrota, Lei das Sesmarias, Ordem de Cristo and Volta do Mar replace Arquebus and Circumnavigation. | [Portuguese.toml](Portuguese.toml) |
| Italians | Italians | 1000–1494 | Italians as the communes and maritime republics (1000–1494): the Genoese Crossbowman stays and becomes the team's mercenary, the Condottiero gives way to the Condotta, Silk Road becomes the Commenda, the commune takes the Town Center, banking replaces fishing and the Hussar becomes the Stradiot. | [Italians.toml](Italians.toml) |
| Sicilians | Sicilians | 1030–1266 | Sicilians as the Italo-Normans and the Kingdom of Sicily (1030–1266): the Norman charge (Imperial Age) replaces the bonus-damage bonus, a fleet bonus is added, First Crusade becomes the Magna Expeditio levy, the royal Diwan takes the Town Center and Lucera's Muslim archers replace Hauberk. | [Sicilians.toml](Sicilians.toml) |

### Central Europe

| Game name | Name | Window | Main changes | File |
|---|---|---|---|---|
| Teutons | **Germans** | 919–1500 | Teutons renamed Germans: the Teutonic Knight becomes the mounted brother-knight, German miners the team bonus and Henry I’s burgs the Town Center tech, the Hanse and the Landsknechte replace Ironclad and Crenellations, Gutenberg's Press joins, and the tree gains Arbalester and Architecture. | [Germans.toml](Germans.toml) |
| Bohemians | Bohemians | 872–1526 | Bohemians keep their Hussite core: Hussite Reforms moves to the Monastery, Charles IV’s New Town of Prague becomes the Town Center tech, the Houfnice becomes a short-range gun (Organ Gun model), Wagenburg Tactics gains armoured wagons, and the navy shrinks to a landlocked kingdom’s basic fleet. | [Bohemians.toml](Bohemians.toml) |
| Poles | Poles | 966–1500 | Poles moved back to Piast and Jagiellonian Poland: the Kopijnik replaces the Obuch and the Hussar the 17th-century Winged Hussar, Szlachta Privileges moves to the Town Center, hired companies take the Castle, fortifications replace villager regeneration, and the architecture becomes Central European. | [Poles.toml](Poles.toml) |
| Lithuanians | Lithuanians | 1236–1500 | Lithuanians recentred on the Grand Duchy from its pagan rise to the Jagiellonian union: forest and raiding bonuses replace the food and relic bonuses, the hill forts become a passive, the Boyar replaces the Leitis, Horodło and Vytautas’ Tatars are new techs, and the navy shrinks to a basic fleet. | [Lithuanians.toml](Lithuanians.toml) |
| Magyars | Magyars | 895–1526 | Magyars cover the Conquest and the kingdom to Mohács: the Huszar costs no gold, the reflex bow becomes an Imperial Age passive, Kremnica gold and castle-building replace two bonuses, Stephen I’s counties and Matthias’ Black Army are the techs, and gunpowder and Central European architecture come in. | [Magyars.toml](Magyars.toml) |

### Scandinavia, the Rus' and the Goths

| Game name | Name | Window | Main changes | File |
|---|---|---|---|---|
| Vikings | **Norwegians** | 793–1469 | Vikings renamed Norwegians (793–1469): stockfish gold, faster shepherds and settlers' sheep replace the free Wheelbarrow and Hand Cart, the Leiðangr levy becomes the Town Center tech, Berserk and Bogsveigar stay, the Halberdier replaces Chieftains, and the Varangian Guard and Cavalier leave. | [Norwegians.toml](Norwegians.toml) |
| Danes | Danes | 808–1523 | Denmark from Godfred to the end of the Kalmar Union (808–1523): Trelleborg ring forts and the Danevirke replace the invented siege identity, the Øresund toll is the Town Center tech, the Varangian Guard becomes the Housecarl, Lund's church carries the team bonus, and Kalmar-era guns and ships enter. | [Danes.toml](Danes.toml) |
| Varangians | **Swedes** | 500–1500 | Varangians renamed Swedes (500–1500): fur-hunting gold, the Jarl and Vendel Legacy stay, the Varangian Guard stays Byzantine, so its bonus and Gothikon leave, Alsnö Stadga becomes the Town Center tech, Swedish iron and copper carry the team bonus, and an armed peasantry gets a new passive. | [Swedes.toml](Swedes.toml) |
| Slavs | **Rus'** | 882–1505 | Slavs renamed Rus' (882–1505): steppe horse archery and armoured horsemen replace Arson, Gambesons and the siege discount, Poliud'e and Pomest'e become Town Center techs, the Baptism of Rus' replaces Druzhina, Novgorod's Hanse trade is the team bonus, and Muscovite guns enter. | [Rus.toml](Rus.toml) |
| Goths | Goths | 418–711 | Goths redefined as the Visigothic and Ostrogothic kingdoms (418–711): the bowless Gothic Lancer, lance cavalry, Leovigild's Host and a federate team bonus replace the infantry flood, the Liber Iudiciorum is the Town Center tech, and gunpowder, horse archers and the Trebuchet leave. | [Goths.toml](Goths.toml) |

### Byzantium, the Balkans and the Caucasus

| Game name | Name | Window | Main changes | File |
|---|---|---|---|---|
| Byzantines | Byzantines | 527–1453 | Byzantium (527–1453): walls and Cataphracts stay; a gold-income passive replaces the Imperial Age discount, the themes become the Town Center tech, Greek Fire moves to the Dock, Logistica becomes Praecepta Militaria, camels and late gunpowder leave, and horse breeding, hospitals and siege engines return. | [Byzantines.toml](Byzantines.toml) |
| Bulgarians | Bulgarians | 681–1018 and 1185–1396 | The First and Second Bulgarian Empires (681–1018, 1185–1396): Konnik, Krepost and the siege discount stay; the swordsmen go, and mountain passes, steppe archery, Vlach herding and armoured cavalry come in, with the Peace of 927, the Council of Preslav and Cuman allies as techs and a Slavonic team bonus. | [Bulgarians.toml](Bulgarians.toml) |
| Armenians | Armenians | 884–1045 | Greater Armenia (884–1045): the Cilician navy, infantry bonuses, Warrior Priest and Fereters go; the nakharar cavalry gains a gold discount, Paladin, horse archers and Sparapet, Bagratid Ani becomes the Town Center tech, stone building a passive, and the archer unique unit takes its Armenian name. | [Armenians.toml](Armenians.toml) |
| Georgians | Georgians | 1008–1490 | The Bagrationi kingdom of Georgia (1008–1490): Monaspa, mountain defence and the monastic economy stay; the aznauri become a passive, David IV's Kipchaks a second unique unit and the Castle tech, his chancellor-archbishop the Town Center tech and Gelati a University tech; the hand cannon leaves. | [Georgians.toml](Georgians.toml) |

### The Steppe

| Game name | Name | Window | Main changes | File |
|---|---|---|---|---|
| Huns | **Avars** | 567–796 | Huns redesigned as the Avar Khaganate (567–796): houseless camps, cheap horse archers, the Tarkan and Marauders stay, the trebuchet bonus moves to the traction trebuchet, Byzantine tribute becomes the Town Center tech, Slav levies a passive, and Atheism and the Dromon leave. | [Avars.toml](Avars.toml) |
| Mongols | Mongols | 1206–1368 | The Mongol Empire (1206–1368) keeps its horse archers, hunt, remounts, Mangudai and Drill and gains the Keshik, the decimal levy (Conscription free), the yam relay as the Town Center tech and the Pax Mongolica as the team bonus, while camels, the Champion and the Cannon Galleon leave. | [Mongols.toml](Mongols.toml) |
| Tatars | Tatars | 1242–1502 | Tatars refocused on the Golden Horde (1242–1502) without Timur: herds, horse archery and the Keshik stay, the Kipchak levy, Araba wagon camps, yarlyk and tamga revenues, the Beglerbeg and the Mamluk alliance enter, and the Timurid Flaming Camel and Siegecraft, the Trebuchet, guns and camels leave. | [Tatars.toml](Tatars.toml) |
| Cumans | Cumans | 1055–1241 | The Cuman-Kipchak confederation (1055–1241, diaspora to c. 1400) keeps its speed, extra Town Center, Kipchak and Cuman Mercenaries, gains herding, ransom, feigned flight, the Council of Khans and marriage alliances, and loses its invented early siege, the top siege tiers, the Trebuchet and camels. | [Cumans.toml](Cumans.toml) |

### The Islamic world and Africa

| Game name | Name | Window | Main changes | File |
|---|---|---|---|---|
| Saracens | Saracens | 632–1517 | Saracens as the Arab caliphates and Ayyubid–Mamluk Egypt and Syria (632–1517): a horse-archer Mamluk replaces the camel Mameluke, Iqta' land grants and Arabic science passed to neighbours are new, Bimaristan moves to the Town Center, and the Hand Cannoneer and Cannon Galleons leave. | [Saracens.toml](Saracens.toml) |
| Persians | Persians | 500–1507 | Persians as Iran from the late Sasanians to the Timurids (500–1507): qanat farming and fast-shooting archers become passives, Khosrow I's land tax the Town Center tech Kharaj and Persian learning the team bonus; gunpowder leaves and the architecture becomes Central Asian. | [Persians.toml](Persians.toml) |
| Turks | Turks | 1071–1526 | Turks as the Seljuks of Rum and the Ottomans (1071–1526): Sipahi moves to the Town Center as Timar, the Seljuk hans (Caravanserai) replace the gold-mining bonus, Turkish horsemen serving neighbours become the team bonus, and the Hussar and Shipwright are renamed Akıncı and Tersane. | [Turks.toml](Turks.toml) |
| Berbers | Berbers | 683–1554 | Berbers as the Amazigh of the Maghreb, centred on the Almoravids and Almohads (683–1554): the Almoravid spearmen (Murabit) replace the Camel Archer, Yusuf's black guard and Abd al-Mu'min's land survey become the techs, the Genitour a regional unit, and the Hand Cannoneer and Cannon Galleons leave. | [Berbers.toml](Berbers.toml) |
| Malians | Malians | 1235–1599 | Malians as the Mali Empire of the Mande (1235–1599): Tontajon archers replace the Gbeto, the farba governors become the Town Center tech, the salt trade and poisoned arrows passives, and gunpowder, Trebuchet, Keep, camels and cavalry archers leave, with the Halberdier and Siege Ram as substitutes. | [Malians.toml](Malians.toml) |
| Ethiopians | Ethiopians | 500–1543 | Ethiopians as the Christian highland kingdom from late Aksum to the Adal war (500–1543): chewa spearmen replace the Shotel Warrior, gult grants and the chewa regiments become the techs, mules, ambas and monasteries passives, Aksum's Red Sea trade the team bonus, and Hand Cannoneers the late element. | [Ethiopians.toml](Ethiopians.toml) |

### The Indian subcontinent

| Game name | Name | Window | Main changes | File |
|---|---|---|---|---|
| Hindustanis | Hindustanis | 1001–1526 | Hindustanis refocused on the Delhi Sultanate and its Ghaznavid and Ghurid forerunners (1001–1526): the Ghulam becomes a Turkish slave horse archer, Dagh and Tanka replace Shatagni and Grand Trunk Road, horse archers and elephants replace camels and gunpowder, and the Sufi orders are the team bonus. | [Hindustanis.toml](Hindustanis.toml) |
| Gurjaras | Gurjaras | 730–1527 | Gurjaras as the Gurjara-Pratiharas and Rajput kingdoms (730–1527): cavalry and herding stay, Kshatriyas becomes Samantas, the Knight, Cavalier and Battle Elephant enter, new bonuses render irrigation, hill-forts and Gujarat's ports, and the Chakram Thrower, Camel Scout and gunpowder go. | [Gurjaras.toml](Gurjaras.toml) |
| Bengalis | Bengalis | 750–1538 | Bengalis as Bengal from the Palas to the Sultanate (750–1538): the Paik replaces the Ratha and Hastyayurveda the Paiks tech, Shah-i Bangalah is new, cash crops and learning replace the cavalry and monk-armour bonuses, Mahayana moves to the Monastery, and Cannon Galleons, Arbalester and Trebuchet go. | [Bengalis.toml](Bengalis.toml) |
| Dravidians | **Tamils** | 575–1323 | Dravidians renamed Tamils, the Pallavas, Cholas and Pandyas (575–1323): the Velaikkarar and Kalam are the unique units, Uttaramerur and Kadaram new techs, pearls, tanks, temples and sea-borne armies the bonuses, the merchant guilds the team bonus, and gunpowder, Arbalester and Trebuchet leave. | [Tamils.toml](Tamils.toml) |

### China and its northern neighbours

| Game name | Name | Window | Main changes | File |
|---|---|---|---|---|
| Chinese | Chinese | 581–1500 | One civ for China from the Sui to the early Ming (581–1500): it gains the hand cannon and bombard, the traction pao in place of the counterweight Trebuchet, Tuntian at the Town Center and crossbow volleys in place of the fire-lancer bonus, and its team bonus now rests on schooling its neighbours. | [Chinese.toml](Chinese.toml) |
| Jurchens | Jurchens | 1114–1234 | The Jurchen Jin (1114–1234) keep cavalry, siegecraft and the Iron Pagoda; the Grenadier becomes the Bomb Thrower, Meng'an Mouke the Town Center tech and the Traction Trebuchet the heavy engine; Bombard Cannon, Rocket Carts, the Lou Chuan and the unfounded friendly-fire and line-of-sight bonuses go. | [Jurchens.toml](Jurchens.toml) |
| Khitans | Khitans | 907–1125 | The Khitan Liao empire (907–1125) as an armoured horse-archer power: the Pishi Guard replaces the Liao Dao, Bloodlines comes free, the Chanyuan Treaty becomes the Town Center tech, foraging plunder is added, and Lamellar Armor, rockets, fire lances, camels and the Mounted Trebuchet go. | [Khitans.toml](Khitans.toml) |

### East and Southeast Asia

| Game name | Name | Window | Main changes | File |
|---|---|---|---|---|
| Japanese | Japanese | 645–1600 | Japan (645–1600), on the owner’s sketch: double cropping, ō-yoroi and ashigaru replace the cheap camps, Tanegashima (the one late element) Kataparuto, Shugo-Jitō is the Town Center tech, Yasama goes, the Ming tally trade gives the team bonus, and the Traction Trebuchet replaces the Trebuchet. | [Japanese.toml](Japanese.toml) |
| Koreans | Koreans | 500–1598 | Korea from the Three Kingdoms to early Joseon (500–1598), on the owner’s sketch: the Korean bow and armoured monks join the kept bonuses, the infantry discount goes, the Gaema Musa replaces the War Wagon, Eupseong takes the walls effect, Singijeon narrows Shinkichon, and gifts to Japan give the team bonus. | [Koreans.toml](Koreans.toml) |
| Vietnamese | Vietnamese | 938–1527 | Đại Việt from Ngô Quyền to the Lê (938–1527): Red River dikes and the Bạch Đằng river fleets replace the unfounded economic and scouting bonuses, the examination state (Văn Miếu) Paper Money, guns passed to the Ming the Imperial Skirmisher, Chatras becomes Tượng Binh, and the architecture East Asian. | [Vietnamese.toml](Vietnamese.toml) |
| Khmer | Khmer | 802–1431 | The Angkorian empire (802–1431): Jayavarman VII’s hospitals (Arogyashala) replace Tusk Swords, rice, temples, spear levies and rest houses (Dharmashala) the unfounded mechanics, Khmer script passed to the Tai the Scorpion team bonus, and the tree follows Zhou Daguan: no stone-throwers, Knights or guns. | [Khmer.toml](Khmer.toml) |
| Burmese | Burmese | 1044–1599 | The Irrawaddy kingdoms from Pagan to the First Toungoo Empire (1044–1599): the War Elephant replaces the Arambai, Ahmudan and Bayingyi (the one late element) the Howdah and Manipur Cavalry, Kyaukse rice and river fleets the infantry and Lumber Camp bonuses, and monks for Sri Lanka the relic team bonus. | [Burmese.toml](Burmese.toml) |
| Malay | Malay | 671–1511 | The Malay states from Srivijaya to Malacca (671–1511): trade and Orang Laut fleets replace the age-up and armour bonuses, the Hulubalang the Karambit Warrior, Lela Thalassocracy and a religious team bonus the dock sight, Syahbandar is the Town Center tech, and the Bombard Cannon, Trebuchet and Keep leave. | [Malay.toml](Malay.toml) |

### The Americas

| Game name | Name | Window | Main changes | File |
|---|---|---|---|---|
| Aztecs | Aztecs | 1325–1521 | The Mexica and the Triple Alliance (1325–1521): chinampas, temple-burning infantry and a Tlatelolco market team bonus replace the start gold, Monk bonus and Relic gold, tribute becomes the Calpixqueh tech, and siege engines, crossbows and Imperial metal tiers give way to Slingers and local names. | [Aztecs.toml](Aztecs.toml) |
| Maya | Maya | 500–1524 | The Maya kingdoms (500–1524): scribes and astronomers replace the extra Villager, city-burning infantry the siege engines and sea trade the walls team bonus, divine kingship becomes the Town Center tech, the Plumed Archer reaches the Archery Range in the Imperial Age, and crossbows and the Keep go. | [Maya.toml](Maya.toml) |
| Inca | Inca | 1400–1533 | The Tawantinsuyu (1400–1533): the roads and the mitmaqkuna colonies become Town Center techs, fitted stonework makes buildings tougher instead of cheaper, llama herding and cloth gifts to allied lords replace the population and Llama bonuses, and siege engines, crossbows and Imperial metal tiers go. | [Inca.toml](Inca.toml) |
| Muisca | Muisca | 800–1540 | The Muisca chiefdoms (800–1540): salt and gold offerings replace the age-up and Settlement bonuses and salt trade the gold team bonus, cloth tribute becomes the Town Center tech, the Temple Guard and Huaracas are dropped, the Champi line becomes the Club line, and siege engines and stone forts go. | [Muisca.toml](Muisca.toml) |
| Mapuche | Mapuche | 1100–1598 | The Mapuche (1100–1598), recentred on their pre-Hispanic world: colihue lancers, the toqui, the assemblies, dispersed homesteads and machi healers replace the post-1541 cavalry kit, which survives only as the Kona in the Imperial Age, and siege engines, crossbows and stone building are removed. | [Mapuche.toml](Mapuche.toml) |
| Tupi | Tupi | 1000–1567 | The coastal Tupi (1000–1567): manioc farming, war-canoe fleets and allied flotillas replace the unfounded bonuses, Morubixaba and collective work (Motyrõ) become the techs, the Blackwood Archers reach the Archery Range in the Imperial Age, and slingers, Keeps, stone walls and siege engines go. | [Tupi.toml](Tupi.toml) |

## Codex-wide conventions

The regions were designed by separate teams, and a final cross-civ pass made them apply the same conventions.
Where the rules did not settle a case, the conventions below are the default applied in every file; each one,
except the level-1 wording rule (which follows from RULES 6.5), is also a question for the owner (next section),
so the default can change in one place.

- **Regional units** (the game's own regional units, such as the Elephant Archer, Varangian Guard, Camel
  Rider or Steppe Lancer, plus the Genitour by the owner's decision) never count as a civ's unique unit
  (RULES 6.1). The Varangian Guard stays with the Byzantines under its own name; other civs that use its
  model rename it (Housecarl, Galloglass).
- **Navy.** A civ without a war fleet of its own keeps only the basic navy (galleys, fire ships, the Hulk
  line, demolition ships and the Dock techs), with no Galleon, Carrack, Fast Fire Ship or siege warship. Canoe
  and raft fleets keep the generic lines without the Galleon and Carrack. Fleets of ships keep every generic
  tier. Special warships (Cannon Galleon, Catapult Galleon, Dromon, Lou Chuan, Longship, Siphons) appear only
  where the type is documented; the Cannon Galleon needs gun-armed warships inside the civ's window. The
  files of basic-navy and canoe civs name their tier (CQ1); fleets of ships keep the game's navy, and each
  file's tree basis explains any naval item it adds or removes.
- **Generic post-1500 items** of the game's skeleton (Petard, demolition ships, Heated Shot, the Galleon for
  fleets of ships) stay as flagged abstractions and never count as a civ's one late element (RULES section 2).
  Incendiaries follows its prerequisite Siphons.
- **Crossbows.** The Crossbowman is the generic Castle Age bow tier wherever the crossbow was known
  (Afro-Eurasia), until the bow and crossbow lines are split in N2; the Arbalester needs crossbow evidence. The
  pre-contact Americas, where the crossbow was unknown, have neither.
- **Thumb Ring** only where the thumb draw is attested for the civ's archers, or for an archery tradition its
  armies demonstrably used (steppe, Islamic, East Asian); not for civs whose archers used the European draw or
  whose missile troops were crossbowmen.
- **Siege engines** that never reached a civ (the counterweight Trebuchet above all) are removed; the
  Mangonel line stays as the generic stone-thrower (except for the Khmer, whose tree follows Zhou Daguan: no
  stone-throwers), and the Traction Trebuchet is given only where traction engines are attested (the Avars,
  Chinese, Japanese, Jurchens, Khitans, Koreans and Vietnamese). The American civs have no siege engines (owner's decision) and rely on existing
  anti-building effects.
- **Armour.** Plate tiers stay as generic top metal-armour tiers for civs with metal armour; the American
  civs, which had none, lose the Imperial metal tiers.
- **Mule Cart.** It stays with its four holders: the Armenians and Georgians (the game's version, which
  replaces the Lumber and Mining Camps) and the Ethiopians and Tatars (beside the camps). Extending it is an
  idea for later levels (RULES section 10).
- **Architecture** follows historical fit where the research found a clearly better set (Persians to Central
  Asian by the owner's decision; Bohemians, Poles and Magyars to Central European; others in their files); the
  steppe civs use stopgaps until a Steppe set exists (N3): the Avars move from Central to Eastern European, and
  the Mongols, Tatars and Cumans keep their sets.
- **Religious vocabulary.** The Monk, the Monastery and its techs keep the game's generic names in N1.
- **Magnitudes and ages.** No unit line goes beyond the highest value the game now gives it, except two cases
  put to the owner under CQ9 (the Castilian Elite Freire at 100 HP with Órdenes Militares; the Portuguese Ordem
  de Cristo at up to +4 warship attack). An existing effect that is moved or turned into a passive keeps the age
  at which the game makes it available, or a later one (Volta do Mar and Alsnö Stadga are Imperial instead of
  Castle Age), never an earlier one.
- **Team effects.** Identical team-wide effects held by different civs count once per team; trade-gold team
  bonuses count as one, at the highest value present.
- **Level-1 tech wording.** A level-1 unique tech is identical in play to an existing tech: its text names the
  civ's own units and leaves out targets the civ lacks, and its precedent names the existing tech (most also
  quote the game's text). Any change of effect makes it a level-2 tech.

## Codex-wide questions

Design, scope, priority and taste questions that concern many civs at once (RULES section 11). The files
point to most of them by number; their own, civ-specific questions are collected in
[`open-questions.md`](open-questions.md).

1. **CQ1 Navy rule.** Keep the three-tier navy rule above, or give every civ with a navy a siege warship (the
   Catapult Galleon as a generic substitute) and the Galleon as its Imperial warship, for playability?
2. **CQ2 Generic post-1500 items.** Keep the Petard, demolition ships, Heated Shot and Galleon as flagged
   abstractions in every tree that has them, or remove them wherever the civ never had them (which would take
   the Petard from almost every civ)?
3. **CQ3 Crossbows.** The Crossbowman as the generic bow tier in Afro-Eurasia and absent in the Americas; or
   generic for every civ, the Americas included; or based on evidence everywhere?
4. **CQ4 Mule Cart.** Keep the four holders, or extend it beside the camps to other civs whose pack transport
   or mobile camp defines them (the Portuguese *almocreves* and Castilian *arrieros* named in RULES section 10;
   the Castilian, Italian, Mongol and Cuman files also point here), now or in N2/N3?
5. **CQ5 Architecture.** Historical fit as the only criterion, or may visual distinctness keep a civ in a set
   that fits it less well? Which stopgap for the steppe civs until a Steppe set exists?
6. **CQ6 Religious vocabulary.** Keep the generic Monk, Monastery and Christian-named Monastery techs for
   every civ in N1, or design one approved vocabulary per religious tradition?
7. **CQ7 Siege engines that never reached a civ.** Remove them (the current default), or keep them as generic
   abstractions for playability?
8. **CQ8 Regional units.** Confirm that every unit the game classifies as regional, not only the three that
   RULES 6.1 names, does not count as a unique unit.
9. **CQ9 Magnitude ceiling.** Keep every unit line at or below the highest value the game now gives it?
10. **CQ10 Ages of reused effects.** Keep the game's age when an existing effect is moved or becomes a passive?
11. **CQ11 Reuse and stacking.** Is the scale of reuse acceptable (32 of the 52 team bonuses are identical to
    another design's, eight of them "Monasteries work +20% faster" and six "Universities work +80% faster"; 27
    of the 56 Town Center techs use one of four effects: Grand Trunk Road or its gold half, Kshatriyas, the
    Persian Town Center pattern and Burgundian Vineyards; each rests on the civ's own history), and do identical
    team-wide effects count once per team?
12. **CQ12 American power budget.** With no siege engines, no crossbow tiers, no Imperial metal tiers and no
    Galleon, the six American civs are clearly weaker than the rest. Accept it for N1, or restore some generic
    tiers (Imperial metal tiers, Halberdier, crossbows) or add compensating bonuses?
13. **CQ13 Long-range siege.** May a civ outside the Americas have no long-range anti-building weapon when none
    is attested? Today eleven designs have no Trebuchet, Traction Trebuchet or Bombard Cannon: the Armenians,
    Ethiopians, Goths, Khmer, Malay, Malians, Saxons and Tatars rely on the Siege Ram, the Bengalis and Tamils on
    siege elephants, and the Cumans on the Capped Ram.
14. **CQ14 Power floor.** Should N1 compensate the kits that history leaves well below their current strength
    (Saxons, Khmer, Malay, Ethiopians, Berbers, Armenians)?
15. **CQ15 Team bonuses without an outside beneficiary.** Accept the Mapuche and Tupi team bonuses as flagged
    exceptions to RULES 6.2, or choose other effects?
16. **CQ16 Undecided civ renames.** Decide together, under one criterion, the rename proposals that the files
    leave open (Britons → English, Saracens → Arabs, Turks → Ottomans, and others)?
17. **CQ17 Renames of shared generic items.** One rule for per-civ renames of shared generic units and techs
    (the Hussar as Stradiot, Akıncı or Hobelar; the Genitour as Jinete or Ginete, and Sulica Rider if CQ23
    allows it; the Mangonel as Pocha or Whirlwind Pao; the Shipwright as Dar al-Sina'a or Tersane)?
18. **CQ18 Reused names.** May a codex unit take the name of a different existing game unit (Ghulam, Teutonic
    Knight, Houfnice)?
19. **CQ19 Labels.** Should the in-game labels follow the redesign, using only the game's label categories?
20. **CQ20 American renames beyond the agreed list.** Apply them wherever a file documents the real
    equivalent (e.g. Wheelbarrow → Tumplines), for all American civs alike?
21. **CQ21 Windows past 1500.** May a window run beyond 1500 without a late element (e.g. the Koreans to 1598),
    or should windows stop at about 1500 unless a late element needs the edge?
22. **CQ22 Romanization.** Item names in the game's plain style (no scholarly diacritics for Arabic, Persian
    and Indic; Pinyin without tones; Revised Romanization; Hepburn), with diacritics only in quoted terms? (No
    file points here yet; today the Japanese Shugo-Jitō keeps a Hepburn macron, and the Vietnamese names keep
    full Vietnamese diacritics.)
23. **CQ23 Regional Genitour.** May the regional Genitour go beyond the Berbers, Castilians and Portuguese
    (the Lithuanian Sulica Rider and the Malians' Sahelian javelin cavalry are offered as options)?
24. **CQ24 Timur's siege warfare.** Should the Persians, who carry the Timurids, take Timurid Siegecraft, or should Timur's
    siege warfare stay out of N1?
25. **CQ25 Rule interpretations.** (a) Does the chronological order of RULES 6.4 bind only two Castle techs, or
    all of a civ's unique techs? (b) May an existing unique tech that renders a long tradition stay a tech
    (Atlatl, Andean Sling, ...)? (c) Are state fortification programmes Castle techs or Town Center techs?
    (d) Does the tree follow the period a design represents, or everything attested inside the window
    (marginal gunpowder at the end of a window)?
26. **CQ26 Thumb Ring.** Keep the Thumb Ring only where the thumb draw, or a thumb-draw tradition the civ's
    armies used, is attested (the current default, which removes it from 14 designs: the Castilians, Danes,
    Ethiopians, Gurjaras, Inca, Italians, Malay, Malians, Maya, Muisca, Poles, Portuguese, Saxons and Tamils),
    or keep it as a generic archery tier wherever the game has it?

## How to read a design file

Each file follows the format of [RULES.md section 8](../RULES.md#8-files), with a few additions that the
project's later rules and the review process needed:

| Key | What it holds |
|---|---|
| `civ` | The civ's internal name in `data/data.json` (unchanged). |
| `name`, `original_name` | The displayed name; `original_name` is the game's current name, only for renamed civs (RULES section 1). |
| `status`, `label`, `summary` | `draft` for every file; the in-game label; one sentence on the main changes. |
| `ideas` | Ideas that need new mechanics or art, each tagged **N2** or **N3** (RULES section 5). |
| `contested` | Points where historians disagree, and how the design reads them (RULES 6.8, section 11). |
| `open_questions` | Design, scope, priority and taste questions for the owner (RULES section 11). Historical questions are settled in the file itself, with sources and a contested note where needed. |
| `[profile]` | Entity, region, time window (a precise year range, shown on the site), main sources and, where the design redefines the civ, `replaces` (the game's framing that it replaces). |
| `[[bonus]]`, `[team_bonus]` | Passive bonuses and the team bonus, in the game's wording, each with `level` (1), `change` (kept, changed, new), the original text it `replaces`, the existing effect it reuses (`precedent`), its historical `basis`, a one-line `relevance` statement (RULES 6.9) and, where needed, a `contested` note; passive bonuses also have a `kind` (economic, military or other). |
| `[[unique_unit]]` | The unique units, each built on an existing unit (`model`), with the `building` that trains it, `level`, `change`, `replaces`, `basis`, `relevance`, an optional `contested` note and, for a late element available only in the Imperial Age, `age`. |
| `[[unique_tech]]` | 2–4 unique techs, each with its `building`, `kind` (military or civil), `age`, `effect` (in the game's wording), `level` (1 = an existing unique tech kept, moved or renamed with an identical effect; 2 = a new tech built from existing effects, RULES 6.5), `change`, `replaces`, `precedent`, `basis`, `relevance` and an optional `contested` note. |
| `[tree]`, `[tree.basis]` | Items added to or removed from the civ's current tree, each with its basis. |
| `[[rename]]` | Per-civ renames of generic or unique items with an identical effect (RULES 6.10), each with its `basis`. |
| `[architecture]` | One of the 13 existing architecture sets, with `change`, the set it `replaces` and its `basis`. |
| `[[dropped]]` | Every current bonus, unique unit, unique tech or team bonus that the design drops, with the reason. |

## Method

**Inputs.** The verified historical-accuracy analysis of the 56 civs
([`../analysis/historical-accuracy-2026-10.json`](../analysis/historical-accuracy-2026-10.json)), the game data
of this repository (`data/data.json`, the tech trees in `data/trees/`, the English strings), the project rules
and the decisions the owner took during the work (Castilians, the regional Jinete, the Portuguese, Japanese,
Korean and Magyar outlines, the Persian architecture, the Mule Cart and American-siege questions).

**Level 1 only.** Everything in a design already exists in the game: bonuses reuse an effect that some civ,
unique tech or generic tech already has (each `precedent` names it); unique units are existing units, moved,
shared or renamed; tree changes add or remove existing items; architecture sets are reassigned. The exception
is unique techs that no existing tech can fill (above all the mandatory Town Center tech, but also some extra
techs for a distinct datable moment): these 44 techs, 38 at the Castle or Town Center and 6 at other buildings,
are recorded as **level 2**, with the existing effect each one copies. Anything that
needs new mechanics or art is listed in `ideas` for N2 and N3.

**Process.** The work ran as a multi-agent workflow, one team per region (the 11 regions of
[`../tools/regions.json`](../tools/regions.json), without the out-of-scope civs):

1. A designer per region read the analysis, the game data and the rules, checked facts and sources by web
   search, and wrote a first draft of each civ.
2. Two kinds of independent reviewers checked each region: skeptical historians (at most three civs each),
   who checked every claim, date and source and pushed back on weak links; and a rules auditor, who checked
   every level-1 constraint against the game data (precedents, item names, composition, unique-tech rules,
   duplicates).
3. The designer revised the drafts, applying or rebutting every finding with evidence. While the work ran,
   the rules moved from version 0.1 to 0.4.1 (unique techs at named buildings, where each historical trait
   goes, the relevance test, late elements, renamed civs, who decides), so this revision and the next round
   brought every file to the new rules and to the owner's newer decisions.
4. A second, independent round of historians and auditors reviewed the revised files under the new rules,
   and the designer finalised them.
5. A cross-civ consistency pass looked across all 52 civs at once (names and terms, shared and orphaned
   elements, the application of the rules, codex-wide tree policies, power budget and playability), and the
   regional designers applied its findings.
6. An editorial pass per region checked each file's statements about other civs against those files and
   removed notes about the work itself; a last round of consistency fixes per region (navy tiers, Thumb Ring
   and trebuchet evidence) closed the remaining findings, and an independent final audit checked the index,
   the owner's decisions and the repository.

Each step was committed separately, so the history of every file shows how it changed and why.

**Checks.** [`../tools/validate_civs.py`](../tools/validate_civs.py) validates every file: TOML syntax, the
composition rules, required fields (basis, precedent, relevance), item names against the game data, tree
dependencies, architecture sets, original names, and whether every current element is kept, replaced or
dropped. Run it from the repository root:

```
python -I codex/tools/validate_civs.py                 # all files
python -I codex/tools/validate_civs.py --tree Huns     # a civ's current tree (internal name)
python -I codex/tools/validate_civs.py --find "Mule Cart"
```

**Limits.** These are drafts for review with the owner, not balanced designs: level 1 makes no balance
promise (RULES 6.14) and only avoids absurdities. The game's original history texts could not be downloaded
in the environment where the designs were made, so the designs rely on the analysis for them. Web searches
had a limited budget: where a point could not be confirmed online, the file says so or words it cautiously.
