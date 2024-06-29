(check the manual / in game dialogue for the proper name for everything. also eu/us differences...)

(need to clean this up; kind of a scratch pad right now)

Usually, `Croc2.exe+222C34` is 0. But when you do a gummy jump, it gets written with a value corresponding to the strength of the gummy jump. When you hit the ground, the value returns to 0. Simply using [[Cheat Engine]] to write a value to the address will cause croc to do a gummy jump.

(as an aside, this address is used for other jumps too! for example, the hippo jumps in Sailor and the jelly jumps in [[2-1 Save the Ice Trapped Gobbos!|Iceblock]])

For the table below, each color gummy was tested on each color base:
- blue base in last room of [[1-1 Find the Key! Save the Gobbo!|Cage]]
- green base near the start of [[3-2 Find the Wheels in the Mine!|Mines]]
- purple base near start of [[2-1 Save the Ice Trapped Gobbos!|Iceblock]]

($3\times 3=9$ total tests)

| gummy  | value | max height gain |
| ------ | ----- | --------------- |
| blue   | 675   | ~6500           |
| green  | 787   | ~8800           |
| purple | 787   | ~8800           |

so a given gummy works the same on any color base. but ***uhhhhhhhhh green and purple are the same!!?!?!***

Well, you can make the gap in [[2-1 Save the Ice Trapped Gobbos!|Iceblock]] on a purple but not on a green, even though your height is the same. Purple seems to allow more horizontal distance. So clearly `Croc2.exe+222C34` doesn't tell the whole story

will need some more investigation!

manually setting the value to 787 with [[Cheat Engine]] gives a result similar to a green jump

also implement this info from [[hdc0]] into this note:
> `Croc2.exe+222C34` (aka `0x622C34`) is `WorldGlobals[14]`
> 
> [link](https://discord.com/channels/313375426112389123/408694062862958592/676384276257701918)
> 
> [link](https://discord.com/channels/313375426112389123/408694062862958592/676486927796535326)
> 
> &mdash; <cite>[[hdc0]]</cite> ([source](https://discord.com/channels/313375426112389123/408694062862958592/1256565484615237754))

> It seems \[the gummy jump system] is implemented in the map script rather than in the engine. So you would have to decompile the map script to understand how the jump system works.
> 
> `0x622C34` (the memory that you modified in CE) is a global script variable. They start at address `0x622BFC` and each entry is 4 bytes. So `0x622C34` is `Global[14]`. That's very interesting. It would be nice if we could create a table that maps global variable indices to their meaning for each map.
> 
> &mdash; <cite>[[hdc0]]</cite> ([source](https://discord.com/channels/313375426112389123/408694062862958592/676486690671689728))

I found a nearby address that is 0 when doing a green gummy jump and 4096 when doing a purple gummy jump!
`Croc2.exe+222CEC`

if you start a green gummy jump then quickly edit that address to 4096, it acts like a purple!

I was hoping you could simply set `Croc2.exe+222C34` to 787 and `Croc2.exe+222CEC` to 4096 to get a purple gummy jump wherever / whenever you want, but it's inconsistent :SnowSad:

oh! I think there are just some additional addresses that need to be set. you can do one legit gummy jump to set the additional addresses, then by setting `Croc2.exe+222C34` to 787 and `Croc2.exe+222CEC` to 4096 you can do purple gummies to your hearts content (until the additional addresses get reset by something lol)!

could probably make a script for it in [[Cheat Engine]] and add it as a hotkey (like the save / load position or no clip ones)!