(check the manual / in game dialogue for the proper name for everything. also eu/us differences...)

Usually, `Croc2.exe+222C34` is 0. But when you do a jelly jump, it gets written with a value corresponding to the strength of the jelly jump. When you hit the ground, the value returns to 0. Simply using [[Cheat Engine]] to write a value to the address will cause croc to do a jelly jump.

each color jelly was tested on each color base (3x3=9 total tests):
- blue base in last room of [[1-1 Find the Key! Save the Gobbo!|Cage]]
- green base near the start of [[3-2 Find the Wheels in the Mine!|Mines]]
- purple base near start of [[2-1 Save the Ice Trapped Gobbos!|Iceblock]]

| jelly  | value | max height gain |
| ------ | ----- | --------------- |
| blue   | 675   | ~6500           |
| green  | 787   | ~8800           |
| purple | 787   | ~8800           |

so a given jelly works the same on any color base. but ***uhhhhhhhhh green and purple are the same!!?!?!***

Well, you can make the gap in [[2-1 Save the Ice Trapped Gobbos!|Iceblock]] on a purple but not on a green, even though your height is the same. Purple seems to allow more horizontal distance. So clearly `Croc2.exe+222C34` doesn't tell the whole story

will need some more investigation!

manually setting the value to 787 with [[Cheat Engine]] gives a result similar to a green jump