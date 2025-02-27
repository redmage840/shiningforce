<b>TACTICS GAME!</b><br>
<br> note: game not complete but first few levels should be complete enough although will certainly change<br>
<br>
<b>Quickstart</b>: Use left-click or arrow keys to move cursor around map. Right-click a unit on the map, or press 'a' when the cursor is over it, to select the unit. The selected unit's information appears in the left-hand menu. Pressing the 'more info' button, or 'i' hotkey, gives more detailed information.<br>
Right-click a button to see a description of the spell/action. The hotkey 'q' cancels most actions, while 'a' confirms.<br>
Protagonist may place one Tomb, using the spell 'Entomb' from the arcane menu, every turn. At the beginning of the turn, the protagonist(s) or Witch units, receive magick equal to 3 times the number of owned tombs, plus their own magick regeneration rate. Your witch may cast as many spells from the arcane menu as can be afforded. <br>
All units may move equal to their 'moves' value, and use actions equal to 'acts'. Actions are any attack/spell buttons that are NOT from the witch arcane menu.<br>
Many more things implemented in game than listed in remainder of readme. Descriptions of most everything is in game help popup menus. Use r-click on actions to see descriptions and use 'more-info' button on your own and enemy units.<br>
<br>
<br>
-Units controlled by you will have a list of available actions in context menu<br>
-Number hotkeys (1-9) are assigned to actions and spells in the context menu<br>
-Cycle through your units with ',' and 'l', cycle through enemies with '.' and ';'<br>
<br>
<b>Constraints:</b><br>
-Player starts most levels with only witch<br>
-Witch death ends game<br>
-Summons are capped according to the witch (start at 6), means you can summon 6 times per level<br>
-Summon death does not 'lower' summon limit cap<br>
-Most units that are not 'flying' type or not using a teleport-type movement action (or leap) are impeded<br>
by other units and walls and obstacles, meaning that they must move 'around' obstacles and cannot necessarily<br>
move to any empty square within their 'maximum range'.<br>
-Can use 2 player mode but networking not yet implemented. Test out concept by battling 2 witches against each<br>
other on the same machine. Only can currently use basic summons/spells for 2 player mode. Upgrades (new spells,<br>
stat and summon cap changes) are gained in 1 player mode. Multiplayer ideally will support networked play and<br>
allowing the players to agree on the amount/type of spells/summons/abils used, as well as the choice of a few maps.<br>
No current plans of level editors or 'use-map-settings' type goals for multiplayer beyond basically 1v1 deathmatch.<br>
<br>
<b>Stat Descriptions:</b><br>
-Attacks/spells determine what stats are used, (melee attacks often used strength, but not necessarily)<br>
-Relative value/use of stats is determined by what attacks you are using and what is being used against you<br>
-For example, some enemies may check your unit's psyche in order 'to hit' and then check your endurance<br>
to determine damage<br>
-In general, strength is used for determining damage, endurance is used for resisting damage or poison, agility<br>
determines 'to hit' for melee and ranged attacks or evading melee attacks, dodge is used for evading ranged attacks,<br>
psyche is often used for magick-based attacks (either using or resisting), spirit is like hit-points with<br>
reduction to zero being instant death with no resurrection, magick are finite magick points spent on arcane spells<br>
-Some spells/abilities allow for 'saves' that check a stat (with optional modifier)<br>
-The save formula is simply the stat value times 10 equals probability of success. For example, a unit with a dodge<br>
stat of 7 will have a 70 percent chance of succeeding the save. Units with stats of 10 or greater will always<br>
succeed an unmodified save. Stats cannot be reduced below 1, but modifiers can push a save to below 10 percent.<br>
<br>
<b>Game Concepts:</b><br>
-Anything causing damage has a type, 'melee', 'ranged', 'poison', or 'magick'<br>
-Units can accumulate effects on their attack, defense, move range, any stat, or even their death<br>
-Spells/abilities may affect an action based on its type, this will be noted in the specific spell/ability<br>
-Effects can also affect the game state at either the start-of-turn or end-of-turn<br>
-For example, a unit may gain an effect that does 2 damage at the end-of-turn (after passing to the opposing player)<br>
or they could gain a bonus to movement range at the start-of-turn<br>
-Global effects are not tied to a unit, but have some effect on the environment.<br>
-Global effects currently changing to being tied to locations. Only a cantrip gained later (Foul Familiar)<br>
grants access to the units implementing global effects, but expect them to change.<br>
-All effects have a 'level' determined by their caster that determine the difficulty of undoing them (dispel-like)<br>
-Effects accumulated by a unit will be noted by name in the unit's context menu<br>
-Damage formula: damage = 5+attacker_stat minus defender_stat with minimum 1. So equal stats tend to do 5 damage.<br>
-Distributions of stats average around 5 for most units, with 10 being a soft limit of common units. Stats over 10<br>
happen with exceptional/'boss' units and after stat boosting. This means that damage for most units ranges from<br>
many 1's as weaker units try to damage exceptional units, 3-7 as fairly equal units trade damage, and 9-14 as<br>
exceptional units attack normal units. There is no random factor for most damaging effects.<br>
-To hit formula: 50 plus (attacker_stat minus defender_stat) times five = probability of chance<br>
-This means equal stats have 50 percent chance of hitting, with each point of difference in stats contributes 5<br>
percent difference probability. To hit draws a random number to determine this probability of hitting. The stat<br>
distributions of units means that many attacks center around a 50 percent chance of hitting, with extremes near<br>
less than 5 percent or greater than 95 being very rare.<br>
-The level of an effect determines its difficulty for dispelling (cancelling/removing). The probability of<br>
resisting the dispel is the effect's level times 10. Some dispel effects may provide a modifier.<br>
-The duration of effects is described as lasting some amount of turns. An effect's duration is decremented at the<br>
end of the turn of the player controlling the unit it affects. So an effect with a duration of 3 that is cast on an<br>
enemy unit during your turn will expire after that unit has had the opportunity to act through 3 of its turns. Cast<br>
on one's own unit, that same effect will last through your current turn and expire when you end your turn after the<br>
next one.<br>
-An Effect may make more than one change to a unit. It may affect the unit's movement and also do some damage at<br>
the start of the turn or give it a bonus during melee attacks. An Effect(non-global), is something that is<br>
represented by a name that appears in the context menu of the affected unit, such as 'ghoul poison' or 'gravity'.<br>
A single spell/ability may cause multiple Effects on one or more units. A single Effect can make multiple changes<br>
to the affected unit. The thing that is dispelled (canceled by Bard's Esuna or something else) is the name in the<br>
context menu, depending on its own level. Dispelling removes all the 'effects' caused by that Effect on a single unit.
<br>
<br>
<b>Basic Summons: (exact descriptions of abilities listed in 'Summon Abilities' section)</b><br>
-Warrior: High spirit and good melee atk and def. Guard lets a Warrior take damage for others. Move type is unique<br>
charge-type that, although only allowing movement in a straight line, is resistant to effects that affect 'normal'<br>
movement types. When combined with leap (a 'free' move action that is unobstructed by obstacles),<br>
the Warrior is uniquely mobile and your main tank, making good use of agility enhancements. The Warrior<br>
is hampered by very low psyche and low dodge, making many magick or ranged attacks hit easily. Although<br>
the Warrior's high endurance reduces the damage of many ranged attacks.<br>
-Shadow: Has two forms, switched between with 'Phase Shift'(counts as action). Shadow Wolf has a decent ranged<br>
attack and uses Dark Shroud to protect allies, acting as a secondary healer and ranged support. The Shadow Mist<br>
form has higher psyche but lower physical stats, making it less suited for dealing or receiving physical attacks<br>
but more resistant to magick. Muddle confuses enemies with low psyche while Drain Life damages a target and<br>
heals the Shadow. The Shadow Mist form is good against enemies with low psyche, especially when they are slow.<br>
-Trickster: Physically vulnerable but with good dodge and psyche, the Trickster is a powerful and versatile support<br>
that must be kept out of direct action. Simulacrum provides a powerful stat boost for attack or defense.<br>
Pyrotechnics and mortar provide an interesting trade-off in ranged physical attacks. Gate can teleport enemy OR<br>
friendly units to an empty square within 5 of the Trickster, which can have important defensive and offensive<br>
applications.<br>
-Bard: Similarly to the Trickster, the Bard does best when kept back as a support unit relying on its magick based<br>
Discord attack as a last resort. The Bard heals others with Moonlight and is the only basic summon that can<br>
dispel effects with Esuna. Unholy Chant boosts all nearby friendly unit stats for the turn.<br>
-Plaguebearer: Your secondary tank unit (besides the warrior), a Plaguebearer is slow moving but can have<br>
devastating effects on crowded enemies. With less hp and agility than the Warrior, the Plaguebearer makes up with<br>
both high endurance and psyche, making most sources deal little damage. Pox poisons all adjacent enemies while<br>
Paralyze stops a low endurance enemy from functioning for an entire turn. When the Plaguebearer is killed, it<br>
spreads a powerful contagion effect that significantly lowers the physical stats of adjacent enemies.<br>
<br>
Agnes' Cantrips:<br>
-Psionic Push: choose any unit within range 4, then choose any empty square within range 2 of that unit with an<br>
unobstructed path from the target (or the same square the unit is currently on ). Unit is 'pushed' to that<br>
square. If there are any adjacent units to the chosen square, moved unit and any adjacent units make an agility<br>
save or take damage based on the moved target's strength compared to each unit's endurance. Target does not receive<br>
damage if ending square has no adjacent units.<br>
-Scrye: Any unit gets +2 agility and +2 psyche for this turn<br>
-Energize: Any summon may move again if it has already moved this turn.<br>
<br>
Agnes' Arcane:<br>
-Plague: Any target in range 5 gets -3 to a random stat (not spir/mag). Plague RECURSIVELY affects adjacent units,<br>
stopping on any units that already have Plague effect. Will spread to both enemy and friendly units. Use Psionic<br>
Push to set up chains of adjacent enemies. Lasts 6 turns. Level equal to caster psyche (on cast).<br>
-Pestilence: target takes magick damage using damage formula where attacker-stat is Caster psyche, defender stat is<br>
(defender psyche plus defender endurance) divided by 2 rounded down. Units within range 3 of target take damage<br>
in the same manner except that they subtract (their distance from the target)times 2. So units that are 3 squares<br>
away from target take 6 less damage, ... 2 squares away take 4 less damage, 1 square away takes 2 less. Target<br>
also gets pestilence effect that does 1 damage at end of turn. If a unit with pestilence effect dies, effect<br>
is passed to each adjacent unit that does not have pestilence effect. Lasts 20 turns. Level equal to caster psyche<br>
(on cast).<br>
-Curse of Oriax: Any target in range 4 gets an effect that gives -1 to all stats and does 2 magick damage at end of<br>
turn. Lasts six turns. Level equal to caster psyche (on cast).<br>
-Gravity: Any target in range 9 gets gravity effect. Gravity places a move effect on the unit that reduces all<br>
potential movement squares to only those within distance of 2 from the unit's location. Note that this does not<br>
change the units movement range to 2 or reduce it by 2, only reducing currently legal moves to those within<br>
distance 2. Target also gets -1 to agility and -2 to dodge. Lasts 4 turns. Level equal to caster psyche (on cast).<br>
-Beleth's Command: <i>Agnes is burned at the stake. Saved by the hellish power of Beleth, a Demon Prince.<br>
He strikes a foe with a fierce bolt of lightning and makes her immune to the inferno.</i><br>
Cannot cast if caster has used her normal move this turn. Caster cannot use normal move this turn after casting<br> Beleth's Command. Any target within range 2-7 is struck by lightning which deals damage where attacker-stat is<br>
caster psyche and defender stat is (defender-psyche+defender-endurance)divided by 2 rounded down. If target fails<br>
strength save, they are stunned until their next end-of-turn (cannot make any actions/moves). If target is not<br>
already affected by Beleth's Command, it gets -1 to psyche and endurance for 5 turns at level equal to caster<br>
psyche on cast. Beleth's Command then does 9 magick damage to each unit adjacent to caster. After other effects,<br>
if caster does not already have Beleth's Command Effect, caster gets +1 to endurance and psyche for 5 turns at<br>
level equal to caster psyche (on cast).<br>
<br>
<b>Summon Abilities</b><br>
Warrior: Attack: Agility versus agility to-hit. Strength versus endurance determines damage. Range 1, type melee.<br>
Warrior: Leap: Move over obstacles to any square within range 3. Movement effects do not affect the range of Leap<br>
unless specifically noted. Does not count as either an action or a move. Can only be used once per turn.<br>
Warrior lvl2: Throw: relocate an adjacent unit to a location up to distance 3 from Warrior<br>
Warrior lvl2: Rage: Dispel current affects at +6, gain +1 str, +1 end, +4 psy, take 3 dmg on effect end, lasts 4 turns.<br>
Shadow (wolf form): Shadow Strike: Range 2-8. Agility versus dodge to-hit. Strength versus endurance determines damage.<br>
Type is ranged.<br>
Shadow (wolf form): Dark Shroud: Target Warrior, Bard, Trickster, or Plaguebearer and all other of all these types within range 3<br>
of the target heal 2 spirit up to their max spirit and receive +1 dodge if they do not already have the effect.<br>
Lasts 3 turns at level 3.<br>
Shadow lvl2 (wolf form): Darkblast: Dispel attempt one effect on a unit at +2, if unit is friendly then heal 3, if unit is<br>
enemy then attack agility vs dodge, str vs end damage.<br>
Shadow lvl2 (wolf form): Stalk: If target fails dodge save it gets defense_effect that increases ranged damage by 2, lasts 7 turns.<br>
Shadow (mist form): Muddle: If target within range 4 fails psyche save, it gets muddle effect for 3 turns. At the end of turn,<br>
the affected unit attacks itself using its own agility versus its own agility to-hit and its own strength and<br>
endurance for determining damage with type of melee. Level 5.<br>
Shadow (mist form): Drain Life: Target within range 2-5 is attacked using psyche versus psyche to-hit. Damage uses psyche<br>
versus psyche but is divided by 2 and rounded down to a minimum of 1 and then added to one (essentially about half<br>
normal damage formula with a minimum of 2). Any damage done to the defending unit that is not more than its current<br>
spirit total is added back to the caster's spirit (to a max of its starting spirit). Type magick<br>
Shadow: Phase Shift: Switch between the Shadow Wolf and Shadow Mist forms. Counts as action.<br>
Trickster: Pyrotechnics: Do 2 ranged damage to any target within range 3, auto hit.<br>
Trickster: Simulacrum: Target within range 4 gets +3 agility and +3 dodge. Lasts 3 turns at level 4. Cannot cast<br>
on target if it already has simulacrum effect.<br>
Trickster: Gate: Target unit within range 2 is teleported to any square within range 5 of the caster.<br>
Trickster: Mortar: All units within range 2 of target square within range 6-8 must make a dodge save or take a<br>
random amount of ranged damage between 1-3.<br>
Bard: Unholy Chant: All other friendly units within range 2 get +1 to all stats for the remainder of the turn at<br>
level 4.<br>
Bard: Discord: Target within range 5 is attacked using psyche versus psyche to-hit. Damage is psyche versus psyche<br>
divided by 2 rounded down and added to 1 (about half normal formula, minimum 2). Type magick.<br>
Bard: Esuna: Target within range 4 has each effect attempted to dispel/remove with no modifier.<br>
Bard: Moonlight: Target Warrior, Shadow, Plaguebearer, or Trickster is healed 4 spirit up to its max spirit.<br>
Bard lvl 2: Aura: Target Warrior, Shadow, Plaguebearer, or Trickster and all of these types within range 2 of target heal up to 3 spirit.<br>
Bard lvl 2: Tranquility: Dispel(0) attempt all effects on a location<br>
Plaguebearer: Pox: Each adjacent, non-plaguebearer, unit gets pox effect if it does not already have it. Effect<br>
causes 2 poison damage at end of turn. Lasts 4 turns at level 6.<br>
Plaguebearer: Paralyze: If target fails a strength save(-1), it gets an effect which causes melee and ranged dmg to be halved(rounded down) and its move range reduced to 1. Lasts 2 turns at level 6.<br>
Plaguebearer: Scarab Gestation: Target enemy gets a death trigger that creates a scarab under your control, scarab has str 2, agl 3<br>
end 3, dodge 3, psyche 2, spirit 9, move range 5, and bite attack agility vs agility, str vs end damage.<br>
Plaguebearer: Contagion: Plaguebearers have an innate death effect that gives each adjacent unit a contagion effect<br>
if it does not already have one. Contagion gives -3 to strength, endurance, agility, and dodge. Lasts 3 turns at<br>
level 7. This is triggered the moment a plaguebearer is reduced to zero spirit.<br>
Plaguebearer lvl 2: Spore Cloud: Target location gets effect +2 dodge, -2 ranged or melee damage, lasts 3 full turns.<br>
<br>
Coming soon: descriptions of enemy abilities, powerup spells/summons and Fakir Ali's spells already in game...<br>
<b>Fakir Ali Spells:<b><br>
Cantrips:<b>
Meditate: Caster gets +2 psyche and increase legal moves by range of 2 until next end of turn.<br>
Boiling Blood: Target Warrior gets +5 strength and endurance reduced to 1 for 4 turns at level of caster psyche<br>
(on cast). Later effects may increase endurance beyond 1.<br>
Dark Sun: Target Shadow may use an action again if it already used an action this turn.<br>
Arcane:<br>
Mummify: 