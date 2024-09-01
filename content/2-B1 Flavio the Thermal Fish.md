---
aliases:
  - Flavio
---

There is a set list of locations icecubes can spawn, ordered in a clockwise direction. At the start of the fight, the icecube will spawn in the same top right location. Every time a new icecube spawns, the following code is run
```
WPNext
if (rnd(10) < 5)
WPNext
endif
if (rnd(10) < 5)
WPNext
endif
```
The spawn location will move forward 1 slot. Then there is a 50% chance it will move forward 1 more slot. Then there is another 50% chance it will move forward 1 more slot. This results in there being a 25% chance to move 1 slot, 50% to move 2 slots, and 25% to move 3 slots.

[[Rartrin]] posted a "rough decompile of the icecube's strat code" [here](https://discord.com/channels/313375426112389123/416998863467970583/1199163872515477544)
