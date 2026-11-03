---
aliases:
  - GameState
---
Every game state (such as being on the main menu, in-game, the game over screen, etc) is assigned a unique number. There is an address in memory which contains the current game state. For a list of all the game states, see the autosplitter (maybe should move that list here, where we have access to better text formatting and more space...)
# Entering an arbitrary `MainState`
You can enter whatever state you want by hi-jacking the credits [[Cheats|cheat]]! For [[PC]]:
1. Poke the address `0x41AC66` to contain the state # you wish to enter
	- by default, the address contains the state # for the credits screen, as of course this is intended to take you to the credits
	- (we have long known putting 18 here takes you to the [[Level Select]] screen)
2. Enter the credits cheat
	- (on the main menu: `hold A, press C, Right, C, C, Down, Left, Up, Right, T`)
3. The game will now transition to whatever state # you entered!
# Testing unknown `MainState`s
Testing various state numbers (og [[PC]]), by hijacking the credits cheat as described above.
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