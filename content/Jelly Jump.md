---
aliases:
  - Gummi Jump
  - Gummy Jump
  - Gummi
  - Gummy
---
Depending on which release of the game you have, these have a variety of shapes, sizes, and names (see [here](https://tcrf.net/Croc_2_(Windows,_PlayStation)#Regional_Differences) on TCRF)

Most runners tend to run on a US PC version, so these usually are referred to as blue, green, and purple gummi jumps

![[Pasted image 20240630203500.png]]

Green and purple actually bounce you up the exact same height. The difference is that purple gives you a big horizontal speed boost

When you do a gummi jump, the following memory addresses are written as so:

|     | Address    | Blue         | Green        | Purple       |
| --- | ---------- | ------------ | ------------ | ------------ |
| A   | `0x622C34` | 675          | 787          | 787          |
| B   | `0x622C40` | `0xFFFFF000` | `0xFFFFF000` | `0xFFFFF000` |
| C   | `0x622CEC` | `0x0`        | `0x0`        | `0x1000`     |

(addresses are probably different for the EU version...)

To manually trigger a gummi jump where/whenever you wish, simply set the 3 addresses above accordingly using [[Cheat Engine]] (I imagine you could write a script to set the addresses, and assign it to a hotkey!)
### Address A
Usually, this address is 0. But when you do a gummi jump, it gets written with a value corresponding to the strength (as in vertical height) of the gummi jump. When you hit the ground, the value returns to 0

Simply using [[Cheat Engine]] to write a value to this address will cause croc to do a gummi jump (assuming you have the other addresses set appropriately)

As an aside, this address is used for other jumps too! For example, the hippo jumps in Sailor and the jelly jumps / cave exits in [[2-1 Save the Ice Trapped Gobbos!|Iceblock]])
### Address B
As mentioned above, Address A isn't just used for gummi jumps. Address B seems to determine what type of jump you do when Address A is set. For gummi jumps, it should be set to `0xFFFFF000`.

When you die / enter a level, the value seems to reset to 0. Once the value is set, it will stay there until overwritten (ex by using a hippo jump, exiting a cave in [[2-1 Save the Ice Trapped Gobbos!|Iceblock]], dying, changing maps, etc)
### Address C
This address is typically 0, but when you use a purple jump it is set to `0x1000` until you hit the ground.

When set, you get a massive horizontal speed boost!

Unfortunately, you can not [[Hazard Jump]] on the ground to maintain the super speed, but that would be sick (perhaps [[TAS]] would beeline for a purple gummi and hazard jump the entire game lol)

Try freezing the value using [[Cheat Engine]]; croc walks around with super speed and it is quite fun ^^

---
Blurb from the US PC manual:

![[Pasted image 20240701202018.png]]

---
Need to implement this info from [[hdc0]] into this note:
> `Croc2.exe+222C34` (aka `0x622C34`) is `WorldGlobals[14]`
> 
> [link](https://discord.com/channels/313375426112389123/408694062862958592/676384276257701918)
> 
> [link](https://discord.com/channels/313375426112389123/408694062862958592/676486927796535326)
> 
> &mdash; <cite>[[hdc0]]</cite> ([source](https://discord.com/channels/313375426112389123/408694062862958592/1256565484615237754))

> It seems \[the gummi jump system] is implemented in the map script rather than in the engine. So you would have to decompile the map script to understand how the jump system works.
> 
> `0x622C34` (the memory that you modified in CE) is a global script variable. They start at address `0x622BFC` and each entry is 4 bytes. So `0x622C34` is `Global[14]`. That's very interesting. It would be nice if we could create a table that maps global variable indices to their meaning for each map.
> 
> &mdash; <cite>[[hdc0]]</cite> ([source](https://discord.com/channels/313375426112389123/408694062862958592/676486690671689728))