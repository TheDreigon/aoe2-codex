# Level 1 civ designs

This folder holds the **Level 1 (N1)** design of every civilization in scope: the 56 civs of Age of Empires II: Definitive Edition minus the four out of scope ([Shu, Wei, Wu and Romans](../out-of-scope.md)), so 52 files. Level 1 means *redistribute*: every change reuses something that already exists in the game, the units of campaigns and the Scenario Editor included ([RULES.md section 5](../RULES.md#5-rework-levels)). All files follow [RULES.md](../RULES.md) version 0.5. They were written as drafts, reviewed in October 2026 ([`../reviews/level-1-review.md`](../reviews/level-1-review.md)) and revised in the fix pass that followed. A file that passed the final review of the fix pass has `status = "reviewed"` (see the review's "Fix pass" section, section 10); a file that has not yet passed it is still a `draft`.

## Index

Grouped by the regions of [`../tools/regions.json`](../tools/regions.json). "Game name" is the civ as the game shows it now; "Name" is the redesigned civ, in bold where it is renamed (renamed civs carry `original_name` in their file). "Window" is the year range of the file's profile window, the period the design represents; the file also states its core.

### Britain and France

| Game name | Name | Window | Main changes | File |
|---|---|---|---|---|
| Britons | **English** | 1066–1485 | Britons renamed English for England after 1066 (core c. 1277–1453): faster shooting replaces the archers’ range passive, Yeomen moves to the Town Center, the Chevauchée replaces Warwolf, dismounted men-at-arms gain armour, archers serving allies carry the team bonus, and the Mounted Crossbowman line leaves the tree as Bombard Cannon, Carrack and Crop Rotation join it. | [English.toml](English.toml) |
| Celts | **Gaels** | 563–1500 | Celts reworked as the Gaels of Ireland and Scotland with the medieval Scottish kingdom (563–1500): a cattle-and-dairy economy and castle-taking infantry replace the invented siege identity, the Kern (Woad Raider renamed) is the unique unit, the Galloglass joins the Barracks, the Schiltron and Buannacht are the techs and the Irish missions the team bonus. | [Gaels.toml](Gaels.toml) |
| Saxons | **Anglo-Saxons** | 449–1066 | Saxons renamed Anglo-Saxons for England from the settlement to Hastings (449–1066), rebuilt around the burh and the fyrd: earthwork walls and garrisoned towns replace castle arrows, the shield wall becomes a passive, the Fyrd and Edgar's Recoinage are the new techs, the continental missions the team bonus, and post-1066 items leave the tree. | [AngloSaxons.toml](AngloSaxons.toml) |
| Franks | Franks | 481–1500 | The Frankish kingdoms and France (481–1500): knights, mills, cheap castles and the Throwing Axeman stay, Gothic building replaces the forager bonus, the University of Paris the team bonus, Ordonnance Companies moves to the Town Center and makes the men-at-arms cheaper, the Bureau Brothers take Chivalry’s Castle slot and the Mounted Crossbowman line leaves the tree. | [Franks.toml](Franks.toml) |
| Burgundians | Burgundians | 1363–1477 | Valois Burgundy (1363–1477): the economic, Cavalier and gunpowder bonuses stay, archers replace the stable discount, the Bruges trade becomes the team bonus, the 1433–34 common coinage the Town Center tech, Vineyards moves to the Mill and the Order of the Golden Fleece replaces Flemish Revolution, while the Mounted Crossbowman leaves the tree. | [Burgundians.toml](Burgundians.toml) |

### Iberia and Italy

| Game name | Name | Window | Main changes | File |
|---|---|---|---|---|
| Spanish | **Castilians** | 1037–1504 | Spanish renamed Castilians for the medieval Crown of Castile (1037–1504): the Freire of the military orders replaces the Conquistador and Missionary, the caballería de cuantía takes the Castle, the Santa Hermandad and Bula de Cruzada replace Supremacy and Inquisition, and the Mesta, cheaper castles, Santiago's relic and the foot crossbow come in while the mounted crossbow line leaves. | [Castilians.toml](Castilians.toml) |
| Portuguese | Portuguese | 1139–1521 | Portuguese as the medieval kingdom and its expansion (1139–1521): the Besteiro do Conto replaces the Organ Gun beside the Caravel, crossbow and fishing bonuses replace the gold and forager ones, Aljubarrota, Lei das Sesmarias, Ordem de Cristo and Volta do Mar replace Arquebus and Circumnavigation, and the Mounted Crossbowman leaves the tree. | [Portuguese.toml](Portuguese.toml) |
| Italians | Italians | 1000–1494 | Italians as the communes and maritime republics (1000–1494): the Genoese Crossbowman stays and becomes the team's mercenary, the Condottiero gives way to the Condotta, Silk Road becomes the Commenda, the commune takes the Town Center, the Arsenal of Venice comes to the Dock, banking replaces fishing, the Hussar becomes the Stradiot, and the Mounted Crossbowman leaves the tree. | [Italians.toml](Italians.toml) |
| Sicilians | Sicilians | 1030–1266 | Sicilians as the Italo-Normans and the Kingdom of Sicily (1030–1266): the Norman charge (Imperial Age) replaces the bonus-damage bonus, a fleet bonus is added, First Crusade becomes the Magna Expeditio levy, the royal Diwan takes the Town Center, Lucera's Muslim archers replace Hauberk and the mounted crossbow line leaves the tree. | [Sicilians.toml](Sicilians.toml) |

### Central Europe

| Game name | Name | Window | Main changes | File |
|---|---|---|---|---|
| Teutons | **Germans** | 919–1500 | Teutons renamed Germans (919–1500): the Teutonic Knight becomes the mounted brother-knight (Crusader Knight art) and the Landsknecht a second unique unit (Heavy Pikeman art), both with adapted stats, the Ministerialen, the Golden Bull and the Hanse replace Ironclad and Crenellations, conversion resistance becomes a passive, German miners the team bonus, and the tree gains Arbalester, Light Cavalry, Architecture and the mining and shipyard upgrades. | [Germans.toml](Germans.toml) |
| Bohemians | Bohemians | 872–1526 | Bohemians keep their Hussite core: Hussite Reforms moves to the Monastery, Charles IV’s New Town of Prague becomes the Town Center tech, the Houfnice becomes a short-range gun (Organ Gun model), Wagenburg Tactics gains armoured wagons, the Czech mercenaries replace the groschen as the team bonus, the navy shrinks to a landlocked kingdom’s basic fleet, and the architecture becomes Central European. | [Bohemians.toml](Bohemians.toml) |
| Poles | Poles | 966–1500 | Poles moved back to Piast and Jagiellonian Poland: the Kopijnik replaces the Obuch and the Hussar the 17th-century Winged Hussar, Szlachta Privileges moves to the Town Center, hired companies take the Castle, fortifications replace villager regeneration, and the architecture becomes Central European. | [Poles.toml](Poles.toml) |
| Lithuanians | Lithuanians | 1236–1500 | Lithuanians recentred on the Grand Duchy from its pagan rise to the Jagiellonian union: forest foraging and a pagan resistance to conversion replace the food and relic bonuses, the hill forts become a passive, the Boyar replaces the Leitis, the regional javelin horse arrives as the Sulica Rider, Horodło and Vytautas’ Tatars are new techs, and the navy shrinks to a basic fleet. | [Lithuanians.toml](Lithuanians.toml) |
| Magyars | Magyars | 895–1526 | Magyars cover the Conquest and the kingdom to Mohács: the Huszar costs no gold, the reflex bow becomes an Imperial Age passive, Kremnica gold and castle-building replace two bonuses, Stephen I’s counties and Matthias’ Black Army are the techs, gunpowder and Central European architecture come in, and the Danube flotilla takes the boat tier. | [Magyars.toml](Magyars.toml) |

### Scandinavia, the Rus' and the Goths

| Game name | Name | Window | Main changes | File |
|---|---|---|---|---|
| Vikings | **Norwegians** | 793–1469 | Vikings renamed Norwegians (793–1469): stockfish gold, faster shepherds and settlers' sheep replace the free Wheelbarrow and Hand Cart, the Leiðangr levy becomes the Town Center tech, Berserk and Bogsveigar stay, the Halberdier replaces Chieftains, and the Varangian Guard and Cavalier leave. | [Norwegians.toml](Norwegians.toml) |
| Danes | Danes | 808–1523 | Denmark from Godfred to the end of the Kalmar Union (808–1523): Trelleborg ring forts and the Danevirke replace the invented siege identity, the Øresund toll is the Town Center tech, the Varangian Guard becomes the Housecarl, Lund's church carries the team bonus, Kalmar-era guns and ships enter, and the mounted crossbow line leaves. | [Danes.toml](Danes.toml) |
| Varangians | **Swedes** | 500–1500 | Varangians renamed Swedes (500–1500): fur-hunting gold and the Jarl stay, the Varangian Guard stays Byzantine, so its bonus and Gothikon leave, Vendel Legacy gives way to Engelbrekt's Rising, Alsnö Stadga becomes the Town Center tech, Swedish iron and copper carry the team bonus, an armed peasantry gets a new passive, and hand guns and printing enter. | [Swedes.toml](Swedes.toml) |
| Slavs | **Rus'** | 882–1505 | Slavs renamed Rus' (882–1505), on the owner's sketch: fur-hunting gold and cheaper horse archers replace Arson, Gambesons and the siege discount, Detinets becomes a passive, Druzhina gives the Boyar and Knight line trample, Kalita's tribute is the Town Center tech, the Baptism of Rus' and Ivan III's gun foundry are new techs, trade with Byzantium and the Hanse is the team bonus, and Muscovite guns enter. | [Rus.toml](Rus.toml) |
| Goths | Goths | 418–711 | Goths redefined as the Visigothic and Ostrogothic kingdoms (418–711): the bowless Gothic Lancer, lance cavalry, Leovigild's Host and a federate team bonus replace the infantry flood, the Liber Iudiciorum is the Town Center tech, and gunpowder, horse archers and the Trebuchet leave. | [Goths.toml](Goths.toml) |

### Byzantium, the Balkans and the Caucasus

| Game name | Name | Window | Main changes | File |
|---|---|---|---|---|
| Byzantines | Byzantines | 527–1453 | Byzantium (527–1453): walls and Cataphracts stay; a gold-income passive replaces the Imperial Age discount, the themes become the Town Center tech, Greek Fire moves to the Dock, Logistica becomes Praecepta Militaria, camels and late gunpowder leave, the Traction Trebuchet replaces the Trebuchet, and horse breeding, hospitals and siege engines return. | [Byzantines.toml](Byzantines.toml) |
| Bulgarians | Bulgarians | 681–1018 and 1185–1396 | The First and Second Bulgarian Empires (681–1018, 1185–1396): Konnik, Krepost and the siege discount stay; the swordsman bonuses go, and mountain passes, steppe archery and Vlach herding come in, with Krum's siege train, the Peace of 927, the Council of Preslav and Cuman allies as techs and a Slavonic team bonus. | [Bulgarians.toml](Bulgarians.toml) |
| Armenians | Armenians | 884–1045 | Greater Armenia (884–1045): the Cilician navy, infantry bonuses, Warrior Priest and Fereters go; the nakharar cavalry gains a gold discount, Paladin, horse archers and Sparapet, Bagratid Ani becomes the Town Center tech, stone building a passive, the Traction Trebuchet replaces the Trebuchet, and the archer unique unit takes its Armenian name. | [Armenians.toml](Armenians.toml) |
| Georgians | Georgians | 1008–1490 | The Bagrationi kingdom of Georgia (1008–1490): Monaspa, mountain defence and the monastic economy stay; the aznauri become a passive, David IV's Kipchaks a second unique unit and the Castle tech, his chancellor-archbishop the Town Center tech and Gelati a University tech; the hand cannon leaves. | [Georgians.toml](Georgians.toml) |

### The Steppe

| Game name | Name | Window | Main changes | File |
|---|---|---|---|---|
| Huns | **Avars** | 567–796 | Huns redesigned as the Avar Khaganate (567–796): houseless camps, cheap horse archers, the Tarkan and Marauders stay, the trebuchet bonus becomes cheaper traction trebuchets, Byzantine tribute becomes the Town Center tech, Slav levies a passive, the Galley line takes the look of the Slav dugouts (the Scenario Editor's Canoe), and Atheism, the Dromon and the Hussar leave. | [Avars.toml](Avars.toml) |
| Mongols | Mongols | 1206–1368 | The Mongol Empire (1206–1368) keeps its horse archers, hunt, remounts, Mangudai and Drill and gains the Keshik, the decimal levy (Conscription free), the yam relay as the Town Center tech and the Pax Mongolica as the team bonus, while camels, the Champion and the Cannon Galleon leave. | [Mongols.toml](Mongols.toml) |
| Tatars | Tatars | 1242–1502 | Tatars refocused on the Golden Horde (1242–1502) without Timur: herds, horse archery and the Keshik stay, the Kipchak levy, Araba wagon camps, yarlyk and tamga revenues, the Beglerbeg (Silk Armor renamed), the traction trebuchet and the khans' patents to the Russian Church enter, and the Timurid Flaming Camel and Siegecraft, the counterweight Trebuchet, guns and camels leave. | [Tatars.toml](Tatars.toml) |
| Cumans | Cumans | 1055–1241 | The Cuman-Kipchak confederation (1055–1241, diaspora to c. 1400) keeps its speed, extra Town Center, Kipchak and Cuman Mercenaries, gains herding, ransom, feigned flight, the Council of Khans and marriage alliances, and loses its invented early siege, the top siege tiers, the Trebuchet and camels. | [Cumans.toml](Cumans.toml) |

### The Islamic world and Africa

| Game name | Name | Window | Main changes | File |
|---|---|---|---|---|
| Saracens | **Arabs** | 632–1517 | Saracens renamed Arabs for the Arab caliphates and Ayyubid–Mamluk Egypt and Syria (632–1517): a horse-archer Mamluk replaces the camel Mameluke, Abd al-Malik's coinage and diwan reform (Dinar) becomes the Town Center tech, Bimaristan moves to the Monastery, Arabic science passed to neighbours is the team bonus, and the Hand Cannoneer and Cannon Galleons leave. | [Arabs.toml](Arabs.toml) |
| Persians | Persians | 500–1507 | Persians as Iran from the late Sasanians to the Timurids (500–1507): qanat farming and fast-shooting archers become passives, Khosrow I's land tax the Town Center tech Kharaj and Persian learning the team bonus; gunpowder leaves and the architecture becomes Central Asian. | [Persians.toml](Persians.toml) |
| Turks | Turks | 1071–1526 | Turks as the Seljuks of Rum and the Ottomans (1071–1526): Sipahi moves to the Town Center as Timar, the Seljuk hans (Caravanserai) replace the gold-mining bonus, Turkish horsemen serving neighbours become the team bonus, and the Hussar and Shipwright are renamed Akıncı and Tersane. | [Turks.toml](Turks.toml) |
| Berbers | Berbers | 683–1554 | Berbers as the Amazigh of the Maghreb, centred on the Almoravids and Almohads (683–1554): the Almoravid spearmen (Murabit) replace the Camel Archer, Yusuf's black guard and Abd al-Mu'min's land survey become the techs, rammed-earth (tabiya) walls a passive, the Genitour a regional unit, and the Hand Cannoneer and Cannon Galleons leave. | [Berbers.toml](Berbers.toml) |
| Malians | Malians | 1235–1599 | Malians as the Mali Empire of the Mande (1235–1599): Tontajon archers replace the Gbeto, the farba governors become the Town Center tech, the salt trade and poisoned arrows passives, war canoes (the Scenario Editor's Canoe) the Galley line, and gunpowder, Trebuchet, Keep, camels and cavalry archers leave, with the Halberdier and Siege Ram as substitutes. | [Malians.toml](Malians.toml) |
| Ethiopians | Ethiopians | 500–1543 | Ethiopians as the Christian highland kingdom from late Aksum to the Adal war (500–1543): chewa spearmen replace the Shotel Warrior, gult grants and the chewa regiments become the techs, mules, ambas and monasteries passives, Aksum's Red Sea trade the team bonus, and Hand Cannoneers the late element. | [Ethiopians.toml](Ethiopians.toml) |

### The Indian subcontinent

| Game name | Name | Window | Main changes | File |
|---|---|---|---|---|
| Hindustanis | Hindustanis | 1001–1526 | Hindustanis refocused on the Delhi Sultanate and its Ghaznavid and Ghurid forerunners (1001–1526): the Ghulam becomes a Turkish slave horse archer, Dagh and Tanka replace Shatagni and Grand Trunk Road, horse archers and elephants replace camels and gunpowder, and the Sufi orders are the team bonus. | [Hindustanis.toml](Hindustanis.toml) |
| Gurjaras | Gurjaras | 730–1527 | Gurjaras as the Gurjara-Pratiharas and Rajput kingdoms (730–1527): cavalry and herding stay, Kshatriyas becomes Samantas, the Knight, Cavalier and Battle Elephant enter, new bonuses render irrigation, hill-forts and Gujarat's ports, and the Chakram Thrower, Camel Scout and gunpowder go. | [Gurjaras.toml](Gurjaras.toml) |
| Bengalis | Bengalis | 750–1538 | Bengalis as Bengal from the Palas to the Sultanate (750–1538): the Paik replaces the Ratha and Hastyayurveda the Paiks tech, Shah-i Bangalah is new, cash crops and learning replace the cavalry and monk-armour bonuses, Mahayana moves to the Monastery, the Sultanate's Bombard Cannon is the late element, Cannon Galleons, Arbalester and Trebuchet go, and the river fleets make the boat tier. | [Bengalis.toml](Bengalis.toml) |
| Dravidians | **Tamils** | 575–1323 | Dravidians renamed Tamils, the Pallavas, Cholas and Pandyas (575–1323): the Velaikkarar and Kalam are the unique units, Uttaramerur and Kadaram new techs, pearls, tanks, temples and sea-borne armies the bonuses, the merchant guilds the team bonus, and gunpowder, Arbalester and Trebuchet leave. | [Tamils.toml](Tamils.toml) |

### China and its northern neighbours

| Game name | Name | Window | Main changes | File |
|---|---|---|---|---|
| Chinese | Chinese | 581–1500 | One civ for China from the Sui to the early Ming (581–1500): it gains the hand cannon and bombard, the traction pao in place of the counterweight Trebuchet, Tuntian at the Town Center and crossbow volleys in place of the fire-lancer bonus, and its team bonus now rests on schooling its neighbours. | [Chinese.toml](Chinese.toml) |
| Jurchens | Jurchens | 1114–1234 | The Jurchen Jin (1114–1234) keep cavalry, siegecraft and the Iron Pagoda; the Grenadier becomes the Bomb Thrower, Meng'an Mouke the Town Center tech and the Traction Trebuchet the heavy engine; Bombard Cannon, Rocket Carts, the Lou Chuan and the unfounded friendly-fire and line-of-sight bonuses go. | [Jurchens.toml](Jurchens.toml) |
| Khitans | Khitans | 907–1125 | The Khitan Liao empire (907–1125) as an armoured horse-archer power: the Pishi Guard replaces the Liao Dao, Bloodlines comes free, the dual administration becomes the Town Center tech and the Chanyuan Treaty a Market tech, foraging plunder is added, and Lamellar Armor, rockets, fire lances, camels and the Mounted Trebuchet go. | [Khitans.toml](Khitans.toml) |

### East and Southeast Asia

| Game name | Name | Window | Main changes | File |
|---|---|---|---|---|
| Japanese | Japanese | 645–1600 | Japan (645–1600), on the owner’s sketch: double cropping, ō-yoroi and ashigaru replace the cheap camps, the Cavalry Archer attack bonus goes, Genko Borui (the Hakata Bay wall of 1276) and Tanegashima (the one late element) replace Yasama and Kataparuto, Shugo-Jito is the Town Center tech, the Ming tally trade gives the team bonus, and the Traction Trebuchet replaces the Trebuchet. | [Japanese.toml](Japanese.toml) |
| Koreans | Koreans | 500–1598 | Korea from the Three Kingdoms to early Joseon (500–1598), on the owner’s sketch: the Korean bow and armoured monks join the kept bonuses, the infantry discount goes, the Gaema Musa replaces the War Wagon, Eupseong takes the walls effect, Singijeon narrows Shinkichon, and gifts to Japan give the team bonus. | [Koreans.toml](Koreans.toml) |
| Vietnamese | Vietnamese | 938–1527 | Đại Việt from Ngô Quyền to the Lê (938–1527): Red River dikes and the Bạch Đằng river fleets replace the unfounded economic and scouting bonuses, the examination state (Văn Miếu) Paper Money, guns passed to the Ming the Imperial Skirmisher, Chatras becomes a lighter Tượng Binh, the Traction Trebuchet (an inference) replaces the Trebuchet, the Cannon Galleon leaves, and the architecture becomes East Asian. | [Vietnamese.toml](Vietnamese.toml) |
| Khmer | Khmer | 802–1431 | The Angkorian empire (802–1431): Jayavarman VII’s hospitals (Arogyashala) replace Tusk Swords, rice, temples, spear levies and rest houses (Dharmashala) the unfounded mechanics, Khmer script passed to the Tai the Scorpion team bonus, and the tree follows Zhou Daguan: no stone-throwers, Knights or guns. | [Khmer.toml](Khmer.toml) |
| Burmese | Burmese | 1044–1599 | The Irrawaddy kingdoms from Pagan to the First Toungoo Empire (1044–1599): the War Elephant replaces the Arambai, Ahmudan and Bayingyi (the one late element) the Howdah and Manipur Cavalry, Kyaukse rice and river fleets the infantry and Lumber Camp bonuses, monks for Sri Lanka the relic team bonus, and the navy drops to the boat tier of the Irrawaddy war boats. | [Burmese.toml](Burmese.toml) |
| Malay | Malay | 671–1511 | The Malay states from Srivijaya to Malacca (671–1511): trade and Orang Laut fleets replace the age-up and armour bonuses, the Hulubalang the Karambit Warrior, Lela Thalassocracy and a religious team bonus the dock sight, Syahbandar is the Town Center tech, and the Bombard Cannon, Trebuchet and Keep leave. | [Malay.toml](Malay.toml) |

### The Americas

| Game name | Name | Window | Main changes | File |
|---|---|---|---|---|
| Aztecs | Aztecs | 1325–1521 | The Mexica and the Triple Alliance (1325–1521): chinampas, temple-burning infantry and a Tlatelolco market team bonus replace the start gold, Monk bonus and Relic gold, tribute becomes the Calpixqueh tech, siege engines and crossbows give way to Slingers, and the galleys become war canoes. | [Aztecs.toml](Aztecs.toml) |
| Maya | Maya | 500–1524 | The Maya kingdoms (500–1524): scribes and astronomers replace the extra Villager, city-burning infantry the siege engines and sea trade the walls team bonus, divine kingship becomes the Town Center tech, the Plumed Archer reaches the Archery Range in the Imperial Age, the galleys become war canoes, and crossbows, the Halberdier and the Keep go. | [Maya.toml](Maya.toml) |
| Inca | Inca | 1400–1533 | The Tawantinsuyu (1400–1533): the roads and the mitmaqkuna colonies become Town Center techs, fitted stonework makes buildings tougher instead of cheaper, llama herding and cloth gifts to allied lords replace the population and Llama bonuses, and siege engines, crossbows, the Halberdier and the sailing warships go. | [Inca.toml](Inca.toml) |
| Muisca | Muisca | 800–1540 | The Muisca chiefdoms (800–1540): salt and gold offerings replace the age-up and Settlement bonuses and salt trade the gold team bonus, cloth tribute becomes the Town Center tech, the Temple Guard and Huaracas are dropped, the Champi line becomes the Club line, and siege engines and stone forts go. | [Muisca.toml](Muisca.toml) |
| Mapuche | Mapuche | 1100–1598 | The Mapuche (1100–1598), recentred on their pre-Hispanic world: colihue lancers, the toqui, the assemblies, dispersed homesteads and machi healers replace the post-1541 cavalry kit, which survives only as the Kona in the Imperial Age, the galleys become canoes, and siege engines, crossbows, the Halberdier and stone building are removed. | [Mapuche.toml](Mapuche.toml) |
| Tupi | Tupi | 1000–1567 | The coastal Tupi (1000–1567): manioc farming, war-canoe fleets and allied flotillas replace the unfounded bonuses, Morubixaba and collective work (Motyrõ) become the techs, the Blackwood Archers reach the Archery Range in the Imperial Age, and slingers, Keeps, stone walls and siege engines go. | [Tupi.toml](Tupi.toml) |

## Codex-wide conventions

The regions were designed by separate teams, and these conventions make every file apply the same tests. They
summarise the decided conventions of [RULES 6.16](../RULES.md#6-civ-design-rules), which the level-1 review
settled (section 6) and the owner accepted, plus the level rules of RULES section 5 and the Mounted Crossbowman
test of the review (section 3.2). RULES is authoritative wherever this summary is shorter, and the owner can
overrule any convention (RULES section 11).

- **Navy** (6.16.1). Navies are classified by vessel, not by water. Planked war galleys or ships make a
  **fleet of ships**, which keeps every generic tier. Dugouts, rafts and light boats make the **boat tier**,
  which keeps the generic lines without the Galleon and Carrack. A civ without a war fleet of its own keeps the
  **basic navy** (galleys, fire ships, the Hulk line, demolition ships and the Dock techs), without the Galleon,
  Carrack, Fast Fire Ship or a siege warship. Special warships (Cannon Galleon, Catapult Galleon, Dromon,
  Longship, Lou Chuan, Turtle Ship) appear only where the type is documented, and the Cannon Galleon needs
  gun-armed warships inside the window. Every file names its tier and the vessels it rests on. Where a civ's war
  craft were dugouts, the Galley line takes the look of the Scenario Editor Canoe (renamed Canoe and War Canoe,
  level 1, with the Galley's stats): the Aztecs, Maya, Mapuche, Tupi, Malians and Avars. The other boat-tier and
  basic-navy designs, among them the raft navies of the Inca and Muisca, keep the Galley's look.
- **Generic post-1500 items** (6.16.2). The Petard, demolition ships, Heated Shot and the Galleon of a fleet of
  ships stay as flagged abstractions of the game's skeleton and never count as a civ's one late element (RULES
  section 2). Incendiaries follows its prerequisite, Siphons.
- **Crossbows** (6.16.3). In Old World civs the Crossbowman is the generic Castle Age bow tier, as an
  abstraction, until the bow and crossbow lines are split in N2. The Arbalester needs crossbow evidence. The
  pre-contact Americas have neither.
- **Mounted Crossbowman** (review, section 3.2). One shared test: the line stays only where shooting from the
  saddle is documented. Only the Germans keep it, on thin and flagged evidence (Hans Talhoffer's fight book of
  1467); the other fourteen designs whose game civ has it drop it, since their sources show mounted crossbowmen
  at most as troops who rode to the fight.
- **Thumb Ring** (6.16.4). Only where the thumb draw is attested for the civ's archers, or for an archery
  tradition its armies demonstrably used (steppe, Islamic, East Asian); not for civs whose archers used the
  European draw or whose missile troops were crossbowmen.
- **Siege engines** (6.16.5). Engines that never reached a civ are removed; the counterweight Trebuchet appears
  in the 1160s–1180s and reached China only in 1273. One test then decides the stone-throwers. The Mangonel line
  is the light stone-thrower everywhere outside the Americas (the Khmer have none, on Zhou Daguan's evidence,
  and the Chinese and Jurchens lack the line, as in the game, beside their own blast weapons). The Traction
  Trebuchet is given wherever heavy stone-throwing engines are attested before the counterweight era (the
  traction test). The Japanese case is a documented transfer: Goguryeo's gift of stone-throwers to the Japanese
  court in 618. The Vietnamese and Armenian cases are inferences from the civ's wars and its neighbours'
  engines, admitted only because they are flagged (no Vietnamese source names a stone-thrower, and the accounts
  of the Yongzhou siege of 1076 record towers and ramps instead). Both engines fill one Imperial Age slot, so a
  design has one heavy engine at most: where the window spans both eras, the design keeps the engine of the
  period its siege evidence falls in, or of its core (the Byzantines and Chinese keep the traction engine, the
  Bulgarians and Mongols the counterweight one). The Traction Trebuchet's holders are the Armenians, Avars,
  Byzantines, Chinese, Japanese, Jurchens, Khitans, Koreans, Tatars and Vietnamese. A civ may have no long-range
  anti-building weapon when none is attested: the Anglo-Saxons, Cumans, Ethiopians, Goths, Khmer, Malay,
  Malians and Tamils. The American civs have no siege engines (owner's decision) and rely on existing
  anti-building effects.
- **Americas** (6.16.6). The removals of siege engines, crossbows, the Halberdier and the Galleon stay. Blast
  Furnace, Plate Mail Armor and Ring Archer Armor are restored as generic equipment levels wherever the game
  gives them (owner's decision, CQ12), on the same footing as Forging, Scale Mail and Chain Mail; they are
  renamed only with a documented period term, which no file has found yet, and are otherwise flagged as
  abstractions. Other generic items are renamed under rule 6.10 wherever a file documents the real equivalent,
  Coinage included; an item kept without one is flagged as an abstraction.
- **Mule Cart** (6.16.7). It stays with its four holders: the Armenians and Georgians (the game's version, which
  replaces the Lumber and Mining Camps) and the Ethiopians and Tatars (beside the camps, renamed Baql and Araba,
  with the look of the Scenario Editor's Donkey and Ox Wagon). Extending it waits for N2 or N3 (RULES section
  10).
- **Architecture** (6.16.8). Historical fit decides: the Persians move to Central Asian (owner's decision), the
  Bohemians, Poles and Magyars to Central European, the Anglo-Saxons to Northern European, the Goths and
  Bulgarians to Mediterranean and the Vietnamese to East Asian. The steppe civs keep stopgap sets until a Steppe
  set exists (N3): the Avars move from Central to Eastern European, and the Mongols, Tatars and Cumans keep
  their sets.
- **Religious vocabulary** (6.16.9). The Monk, the Monastery and its techs keep the game's generic names in N1;
  the site notes that "Monk" fits Muslim civs worst.
- **Regional units** (6.16.10). No unit the game classifies as regional counts as a unique unit (RULES 6.1). The
  Genitour, regional by the owner's decision, serves the Berbers, Castilians (Jinete), Portuguese (Ginete) and
  Lithuanians (Sulica Rider), not the Malians. The Varangian Guard stays with the Byzantines under its own name;
  the Anglo-Saxons and Danes rename it Housecarl, the Gaels Galloglass.
- **Magnitudes and ages** (6.16.11). The ceiling is measured per unit class: no unit line goes beyond the
  highest value the game gives that class. The two exceptions the drafts put to the owner no longer exist:
  Órdenes Militares, which took the Castilian Elite Freire to 100 HP, has left the design, and Ordem de Cristo
  gives the Galley line at most +2 attack. A unit whose Scenario Editor model would go beyond the ceiling takes
  adapted stats at level 2 (the Germans' Teutonic Knight). An existing effect that is moved or becomes a
  passive keeps the game's age or a later one, never an earlier one (Volta do Mar and the Tatars' Beglerbeg are
  Imperial instead of Castle Age); the site labels this as a game constraint.
- **Team effects and reuse** (6.16.12). Reused effects are accepted in N1, each resting on its own history (rule
  6.7). Identical team effects held by different civs count once per team, and trade-gold team bonuses count once,
  at the highest value present. A civ's own bonus and an ally's identical team bonus stack as the game stacks
  them (for example relic gold for the Muisca with a Tatar ally); N1 accepts these stacks, listed below. A
  diversification pass for team bonuses and Town Center techs, planned for N2, revisits them. The stacks of a
  civ's own bonus or unique tech with an ally's identical team bonus are:
  - Docks cost -15%: the Italians' Arsenale with a Norwegian ally.
  - Monasteries work +20% faster: the Maya passive with an Anglo-Saxon, Bulgarian, Burmese, Danish, Gaelic,
    Hindustani, Khitan or Malay ally (the Maya's Universities +33% half also adds to the Universities +80% team
    bonus below).
  - Monks heal +100% faster: the Mapuche passive with a Byzantine ally.
  - Relics generate +33% gold: the Muisca passive with a Tatar ally.
  - Stables work +20% faster: the Castilians' Caballería de Cuantía and the Germans' Ministerialen with an Avar
    ally.
  - Technologies research +25% faster: the Vietnamese Văn Miếu with an Arab ally.
  - Trade Units generate +10% food in addition to gold: the Malian passive with a Bengali or Muisca ally.
  - Trade Units generate +15% gold: the Berber passive with a Burgundian or Gurjara ally.
  - Trade Units generate +25% gold: the Tatars' Tamga with a Castilian or Mongol ally.
  - Units more resistant to conversion: the German and Lithuanian passives and the Sicilians' Magna Expeditio
    with an Inca ally.
  - Universities work +80% faster: the Georgians' Gelati Academy with a Chinese, Frankish, Khmer, Malian,
    Persian or Polish ally.
- **Power floor** (6.16.13). No blanket compensation for kits that history leaves weak; only historically
  grounded extras (the Berbers' *tabiya* walls).
- **Alliances of autonomous polities** (6.16.14). Alliances between autonomous polities of one people (the
  Mapuche, the Tupi) are alliances between independent allies, so their team bonuses satisfy rule 6.2.
- **Names** (6.16.15). A civ is renamed only where standard English scholarship does not use the game's name
  for the design's entity (RULES section 4). A shared generic item is renamed for one civ only when it has the
  same function inside the window, the new name is a period term and the generic name is foreign or
  anachronistic to the civ; modern coinages are flagged. A codex unit may take the name of a different game unit
  (Ghulam, Teutonic Knight, Houfnice), with a note on the site. Names from non-Latin scripts use a plain
  romanization (Shugo-Jito; Pinyin without tones; Revised Romanization; no scholarly diacritics for Arabic,
  Persian and Indic); Latin-script languages, Vietnamese among them, keep their diacritics.
- **Labels** (6.16.16). The in-game label follows the redesign, using the game's label categories.
- **Windows past 1500** (6.16.17). A window may run to a terminal event soon after 1500, with a stated core
  inside the time frame.
- **Timurid Siegecraft** (6.16.18). Not for the Persians; its best home is a possible Mongol Huihui Pao (1273),
  a design option.
- **Rule readings** (6.16.19). (a) The chronological order of rule 6.4 binds only the two Castle techs. (b) An
  existing unique tech that renders a long tradition stays a tech only as a flagged fallback. (c) Defence lines
  go to the Castle, fortified towns to the Town Center. (d) The tree follows the period the design represents,
  not everything attested at the edge of the window.
- **Levels** (RULES section 5 and rule 6.5). A passive bonus or team bonus that applies an existing effect to a
  narrower set of targets, or at a lower magnitude, is level 1 (the narrowing rule). A unique tech is level 1
  only when it is identical in play to an existing tech: its text names the civ's own units and leaves out
  targets the civ lacks, and its precedent names the existing tech. Any other unique tech, even one built from
  existing effects, is level 2.
- **Scenario Editor units and art reuse** (RULES section 5). Units of the campaigns and the Scenario Editor
  ([`../tools/scenario-units.md`](../tools/scenario-units.md), base stats in
  [`../tools/scenario-units-stats.md`](../tools/scenario-units-stats.md)) count as existing content, used only
  where one fits a civ better than the current borrowing. Any existing unit's art may be reused: as it is, with
  only a new name, it is **N1** (the Canoe, Donkey and Ox Wagon looks above); with a new name and adapted
  stats, recorded in a `stats` key, it is **N2** (the Germans' Teutonic Knight on the Crusader Knight and
  Landsknecht on the Heavy Pikeman); with new art or animations it is **N3**.

## Codex-wide questions

The drafts raised 26 codex-wide questions (CQ1–CQ26). The level-1 review settled them (section 6), the owner
accepted its recommendations, including those on the three questions that needed the owner (CQ12, CQ16 and CQ23;
review section 9), and they are now the decided conventions of RULES 6.16, summarised above. What still needs
the owner is collected in [`open-questions.md`](open-questions.md).

## How to read a design file

Each file follows the format of [RULES.md section 8](../RULES.md#8-files), with a few additions that the
project's later rules and the review process needed:

| Key | What it holds |
|---|---|
| `civ` | The civ's internal name in `data/data.json` (unchanged). |
| `name`, `original_name` | The displayed name; `original_name` is the game's current name, only for renamed civs (RULES section 1), and the site shows it next to the new one. |
| `status`, `label`, `summary` | `status` is `draft`, `reviewed` (the file passed the final review of the fix pass) or `approved` (by the owner); the in-game label (RULES 6.16.16); one sentence on the main changes. |
| `ideas` | Ideas that need new mechanics, adapted stats or new art, each tagged **N2** or **N3** (RULES section 5). |
| `contested` | Points where historians disagree, and how the design reads them (RULES 6.8, section 11). |
| `open_questions` | Design, scope, priority and taste questions for the owner (RULES section 11). Normally empty now: the review settled the drafts' questions, the decisions are recorded in the files, and what still needs the owner is in [`open-questions.md`](open-questions.md). Historical questions are settled in the file itself, with sources and a contested note where needed. |
| `[profile]` | Entity, region, time window (a precise year range, shown on the site, with its core), main sources and, where the design redefines the civ, `replaces` (the game's framing that it replaces). |
| `[[bonus]]`, `[team_bonus]` | Passive bonuses and the team bonus, in the game's wording, each with `level` (1, narrowed targets and lower magnitudes included), `change` (kept, changed, new), the original text it `replaces`, the existing effect it reuses (`precedent`), its historical `basis`, a one-line `relevance` statement (RULES 6.9) and, where needed, a `contested` note; passive bonuses also have a `kind` (economic, military or other). |
| `[[unique_unit]]` | The unique units, each built on an existing unit (`model`), a unit of the campaigns or the Scenario Editor included, with the `building` that trains it, `level` (1 = the model as it is, under a new name; 2 = adapted stats), `change`, `replaces`, `basis`, `relevance`, an optional `contested` note and `age` for a unit available only from a later age. A level-2 unit records its adapted values (hit points, attack, armour, speed, cost, training time and bonuses, for each tier) in a `stats` key. |
| `[[unique_tech]]` | 2–4 unique techs, each with its `building`, `kind` (military or civil), `age`, `effect` (in the game's wording), `level` (1 = an existing tech identical in play, kept, moved or renamed; 2 = a new tech built from existing effects, RULES 6.5), `change`, `replaces`, `precedent`, `basis`, `relevance` and an optional `contested` note. |
| `[tree]`, `[tree.basis]` | Items added to or removed from the civ's current tree, each with its basis. Each file also names its navy tier and the vessels it rests on (RULES 6.16.1), usually in the tree basis. |
| `[[rename]]` | Per-civ renames of generic or unique items with an identical effect (RULES 6.10, 6.16.15), each with `level` and its `basis`. An optional `model` gives a renamed generic unit the look of a Scenario Editor or other existing unit (the Canoe for the Galley line, the Donkey and Ox Wagon for the Mule Cart), at level 1. |
| `[architecture]` | One of the 13 existing architecture sets, with `change`, the set it `replaces` and its `basis`. |
| `[[dropped]]` | Every current bonus, unique unit, unique tech or team bonus that the design drops, with the reason. |

## Method

**Inputs.** The verified historical-accuracy analysis of the 56 civs
([`../analysis/historical-accuracy-2026-10.json`](../analysis/historical-accuracy-2026-10.json)), the game data
of this repository (`data/data.json`, the tech trees in `data/trees/`, the English strings), the project rules,
and every sketch and decision of the owner, which the designs follow:

- the Castilians (the debate sketch, the regional Jinete, the military-order knight);
- the Portuguese (the Besteiro do Conto, Ordem de Cristo);
- the Japanese, Korean and Magyar outlines;
- the Armenians centred on Greater Armenia;
- the Persians' Central Asian architecture;
- the Americas without siege engines;
- the Avars' trebuchet bonus (RULES section 4), now "Traction Trebuchets cost -25%";
- the Mule Cart's four holders;
- the owner's Rus' sketch (chat, 15 October 2026), which did not reach the drafts and is recorded in the level-1
  review, section 9;
- the German sketch, our own chat proposal that the owner liked, also recorded in review section 9;
- the decisions taken after the review (review section 9): the renames (Britons → English, Saxons →
  Anglo-Saxons, Saracens → Arabs); the Crusader Knight as the model of the mounted Teutonic Knight; the
  Landsknecht as a unit; the Knight-line trample to the Rus' (Druzhina), with Engelbrekt's Rising for the
  Swedes; the rate of fire of the English (the game's Britons), at +10/+18% instead of +20% so that the passive
  stays level 1; the Japanese Genko Borui; the Italians' Arsenale; the Portuguese Ordem de Cristo, limited to
  the Galley line at +2; CQ12 (the American removals kept, the armour tiers restored) and CQ23 (the Genitour for
  the Lithuanians);
- the owner's rule on reusing unit art, with the Scenario Editor units counted as existing content (RULES
  section 5).

Where a design does not carry out a sketch or decision literally, [`open-questions.md`](open-questions.md) lists
the departure and the civ file gives the reason.

**Level 1 only.** Everything in a design already exists in the game: bonuses reuse an effect that some civ,
unique tech or generic tech already has (each `precedent` names it); unique units are existing units, moved,
shared or renamed, the units of campaigns and the Scenario Editor included; tree changes add or remove existing
items; architecture sets are reassigned. A passive bonus or team bonus that applies an existing effect to fewer
targets, or at a lower magnitude, stays level 1 (the narrowing rule, RULES section 5); a unique tech is level 1
only when it is identical in play to an existing tech. Two kinds of element are recorded as **level 2**: unique
techs that no existing tech can fill (above all the mandatory Town Center tech, but also some extra techs for a
distinct datable moment), 50 of the 133 unique techs, 42 at the Castle or Town Center and 8 at other buildings,
each with the existing effect it copies; and the two unique units that reuse existing art with adapted stats,
the Germans' Teutonic Knight and Landsknecht. Anything that needs new mechanics or art is listed in `ideas` for
N2 and N3.

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
7. The level-1 review ([`../reviews/level-1-review.md`](../reviews/level-1-review.md), 15 October 2026) scored
   every draft, listed the fixes and settled the codex-wide and per-civ questions; the owner then took the
   decisions recorded in its section 9.
8. The fix pass applied the review. RULES v0.5 laid the groundwork (the Scenario Editor rule, the narrowing rule
   and the levels of unit-art reuse in section 5, the 26 settled conventions as rule 6.16, and a changelog in
   section 12). Then one fixer per region applied the review, skeptical historians and a rules auditor checked
   the result, and the fixer's revision was verified and given its final fixes.
9. A cross-civ consistency check read all 52 files through independent lenses: six cross-reference lenses
   (what each file says about other civs), three convention lenses (navy and ranged units; siege, gunpowder,
   late elements and the Americas; reuse, levels, magnitudes, names and unit models), a completeness critic and
   three lenses on unconfirmed claims. A cross-civ fix round per region applied the findings, and each round was
   verified.

Each step was committed separately, so the history of every file shows how it changed and why.

**Checks.** [`../tools/validate_civs.py`](../tools/validate_civs.py) validates every file: TOML syntax, the
composition rules, required fields (basis, precedent, relevance), item names against the game data, tree
dependencies, architecture sets, original names, and whether every current element is kept, replaced or
dropped. It accepts the units of the campaigns and the Scenario Editor
([`../tools/scenario-units.md`](../tools/scenario-units.md)) as the models of unique units and renames, and
level-2 unique units with a `stats` key. Run on several files, it also lists the unit models and effects that
more than one design uses. Run it from the repository root:

```
python -I codex/tools/validate_civs.py                 # all files
python -I codex/tools/validate_civs.py --tree Huns     # a civ's current tree (internal name)
python -I codex/tools/validate_civs.py --find "Mule Cart"
python -I codex/tools/validate_civs.py --names         # every unit, tech and building name
```

**Limits.** These are level-1 designs, not balanced ones: level 1 makes no balance promise (RULES 6.14) and only
avoids absurdities, and the look and role of reused art and of adapted stats must still be checked in the game.
The game's original history texts could not be downloaded in the environment where the designs were made, so
the designs rely on the analysis for them. The web research ran in a cloud environment where the fandom wiki was
blocked and direct page fetches often failed, so many web checks rest on search results; where a point could not
be confirmed, the file flags it or words it cautiously.
