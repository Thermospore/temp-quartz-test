---
aliases:
  - MainState
---
As the name would imply, this memory address contains an integer that represents the current state of the game (such as being on the [[Main Menu]], in-game, on the [[Options]] screen, etc)

< how does the timing compare between game versions? >
# Table
Unfortunately, the values are scrambled between [[OG-PSX]] and [[OG-PC]]. The [[HD]] version is based on [[OG-PSX]].

Here is a table that attempts to map all the game versions together

< WAIT maybe [[Rartrin]]'s de-compile can reveal more info >

< ALSO check various demo versions for clues >

| State name          | [[OG-PSX]] ([[HD]]) value | [[OG-PC]] value | Description                                                                                                                                                                                                                                          |
| ------------------- | :-----------------------: | :-------------: | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `GS_NONE`           |             0             |        0        | - OG: opening logos<br>- HD: they use `GS_SPLASH` (20) instead of this                                                                                                                                                                               |
| `GS_INIT`           |             1             |        8        | Transition from opening logos → intro cutscene where the scientist is taken by dante                                                                                                                                                                 |
| `GS_LANGUAGE`       |             2             |       13        | - PSX/HD: ??<br>- PC: accessible through memory pokes, but is [[Pasted image 20261028211117.png\|broken]] (at least on [[OG-PC#US\|OG-PC > US]])                                                                                                     |
| `GS_TITLE`          |             3             |       16        | [[Main Menu]]                                                                                                                                                                                                                                        |
| `GS_GAME`           |             4             |       11        | Includes both active gameplay and cutscenes                                                                                                                                                                                                          |
| `GS_DEMO`           |             5             |        5        | Demos that run as an attract screen on the [[Main Menu]]                                                                                                                                                                                             |
| `GS_OPTIONS`        |             6             |       14        | - PSX: ??<br>- HD: likely unused (see: [[Options#HD\|Options > HD]])<br>- PC: [[Options#OG-PC\|Options > OG-PC]] screen accessed from the [[Main Menu]] (doesn't include the [[Pause Menu]])                                                         |
| `GS_INITIALS`       |             7             |        9        | - OG: New Game - entering initials<br>- HD: likely unused                                                                                                                                                                                            |
| `GS_CHOOSELOAD`     |             8             |        1        | - OG: Load Game save slot selection screen<br>- HD: likely unused                                                                                                                                                                                    |
| `GS_CONTINUE`       |             9             |        3        | "Continue? Yes / No" screen when you game over                                                                                                                                                                                                       |
| `GS_INTRO`          |            10             |       ??        | < maybe it's that argo message in a bottle intro that's broken on modern [[OG-PC\|PC]]s? On classic that's just 0, though >                                                                                                                          |
| `GS_GAMEOVER`       |            11             |       12        | - OG: "Game Over" screen (when you run out of lives and select "No" in `GS_CONTINUE`, OR when you exit the game via the [[Pause Menu]])<br>- HD: likely unused (selecting "No" on `GS_CONTINUE` takes you straight to [[Main Menu]])                 |
| `GS_CREDITS`        |            12             |        4        | [[Credits]]                                                                                                                                                                                                                                          |
| `GS_NEXTLEVEL`      |            13             |       ??        | ??                                                                                                                                                                                                                                                   |
| `GS_LEVELSELECT`    |            14             |       18        | [[Level Select]] (appears to be almost entirely dysfunctional on [[HD]]...?)                                                                                                                                                                         |
| `GS_GO_TO_TITLE`    |            15             |       19        | Transition from the scientist intro cutscene → Main Menu                                                                                                                                                                                             |
| `GS_GO_TO_HUB4`     |            16             |       20        | After you beat [[4-B2 Dante's Final Fight\|Dante]], the transition from the credits back into [[Inca Hub]]                                                                                                                                           |
| `GS_EXIT_SLIDESHOW` |            17             |        6        | PSX/HD: ??<br>PC Demo: the brief promo slideshow that plays when you quit ([[Features1.bmp]], [[Features2.bmp]]). When the slideshow finishes, `GameState` transitions from 6 → 7 and the game fully quits<br>- PC: When you quit from the main menu |
| `GS_BONUS_CONTENT`  |            18             |       ??        | - OG: presumably not a thing<br>- HD: [[Croc2pedia]]                                                                                                                                                                                                 |
| `GS_LOAD_SCREEN`    |            19             |       ??        | Unclear. Possibly [[HD]] only, as it comes after `GS_BONUS_CONTENT` ([[Croc2pedia]])?                                                                                                                                                                |
| `GS_SPLASH`         |            20             |       ??        | - OG: Possibly [[HD]] only, as it comes after `GS_BONUS_CONTENT` ([[Croc2pedia]])<br>- HD: company logo vids right when you boot the game                                                                                                            |

(NOTE: make sure to update mappings both here AND in the autosplitter. Or better yet, make a system with one source of truth)

How this table was constructed:
1. The state names for HD are listed in order inside [[Croc2.exe#HD PC|Croc2.exe > HD PC]], so that is used as the foundation (discovered by [[hdc0]]: [discord](https://discord.com/channels/313375426112389123/408694062862958592/1568992386514948107))
2. The values for [[OG-PC]] were then mapped to HD through observation
	- (this involved a bit of guesswork, and could have inaccuracies)
3. Descriptions for each state were added through observation

The following `GameState`s are known on [[OG-PC]], but it is unclear how they map to [[OG-PSX]] (if at all)
- 2: New Game - save slot selection screen
- 7: When the slideshow in the demo ends
# Credits hijack
In general, you can enter an arbitrary `GameState` by hijacking game code which normally takes you to the credits screen

By default, the following address contains the `GameState` for the credits screen
- [[OG-PC]] -  `Croc2.exe + 0x1AC66`
- [[HD#Steam|HD > Steam]] - `croc2.exe + 0x211718` (as of [this post](https://discord.com/channels/313375426112389123/1533834309360680970/1569183439624601662))

Poke the address for your version to contain your desired `GameState`, then enter the credits screen
- [[OG-PC]]: enter the credits [[Cheats|cheat]] on the main menu (hold A, press C, Right, C, C, Down, Left, Up, Right, T)
- [[HD]]: simply enter the credits through the options on the [[Main Menu]]

The game will now transition to whatever `GameState` you entered!

For example, we often use this method to enter the Level Select screen (18 on [[OG-PC]])
## Testing on [[HD#Steam|HD > Steam]]
Unfortunately, the method above doesn't seem to work well on [[HD]] 

< maybe can get better results with a different address / method >

Almost all of the `GameState` values (even valid ones) simply softlock you on the main menu:
![[Pasted image 20261117224330.png]]
(pressing esc / B does nothing, and you are stuck here forever)

The following values do something different:
- `GS_DEMO` (5) - behaves like normal
- `GS_CREDITS` (12) - takes you to the credits (duh; default value)
- `GS_LEVELSELECT` (14)

Dysfunctional bastard child of [[Options#HD|Options > HD]] and [[Level Select]]:
![[Pasted image 20261117230755.png]]
`NewWAD` changes when you move left/right, so some of the [[Level Select]] UI code is still there under the hood.

- `GS_BONUS_CONTENT` (18) - behaves like normal
## Testing on [[OG-PC#US|OG-PC > US]]
- 0 - appears to be a blank blue screen, with no way to exit?
- 7 - goes to a black screen and the game closes
- 10 - another blue screen dead-end
- 13 - "Choose Language" screen!! (with no options)

![[Pasted image 20261028211117.png]]

- 15 - another blue screen dead-end
- 17 - another blue screen dead-end
- 20 - fades to a blue screen, but then suddenly you enter the in-game state (11)!?
- 21 - another blue screen dead-end
- (haven't tried going higher than 21)
# Proper variable name
It seems the internal name is `GameState`, not `MainState`:

> ### hdc0 — 2021-01-18 ([Discord](https://discord.com/channels/313375426112389123/408694062862958592/800671020536561694))
> Some time ago MasterLeoBlue posted a PSX symbol file for a beta version of Croc 2. I just had a look at it. It gave use the names of almost all of the 323 engine functions that can be called by level scripts.
> 
> Only 3 or 4 camera related function names are missing. This file will be very helpful in decompiling the level scripts. It also gives us the correct names of some of the variables used by the autosplitter:
> 
> IsCheatMenuOpen -> DebugMode
> 
> GobboCounter -> ExtraCount
> 
> InGameState -> GameOver
> 
> MainState -> GameState
> 
> UsedBossWarps -> IntrosTriggered
