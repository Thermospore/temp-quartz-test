---
aliases:
  - SMP Card
---
![[Pasted image 20240701201611.png]]

I forget, does it even actually do anything? Do you actually need it? Usually you get it right at the start of the game, but you can skip getting it by immediately using the [[Cheat Mode|Cheat Menu]] to go to a different village

Getting the Card is mechanically just another hub completion flag, no different from a minigame — it sets a bit in the [[Sailor Hub]] progress byte (`0x08`) the same way the minigames set theirs, and awards 100 [[Crystal]]s

The one real rule is that **the first completion you ever do pays nothing.** Every one after that pays 100, whichever order you do them in. So the Card looks special only because you normally pick it up first

Confirmed identical on [[PC#US]] and [[PC#EU]], all four hub minigames on a fresh save before taking the Card: 0, 100, 100, 100 — then the Card, 100. Normal order gives the mirror image: Card 0, first minigame 100

The gate is `0x2C4` in the save slot, which steps 0 → 1 → 2 during that first completion and then stays at 2

The Card appears after your first completion, whichever it was — so doing a minigame first gives you the counter at 0 without ever touching the Card. You can also shop without it, and your Crystals are banked normally

< hol up... did it change from blue on [[PS1]] to purple on [[PC]]? verify this >