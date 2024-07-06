---
aliases:
  - Gem
---
(also see: [[Crystal]])

![[Pasted image 20240701204704.png]]

We almost always call these "gems", for whatever reason

`0x52AECC` contains the number of gems you have collected in the current level (independent of save slot). As you would expect, it starts at 0 and goes up to 5.

There is another address which contains the same information, but with benefits we will get to later. However, it is a dynamic address and finding a pointer has proven difficult (see [here](https://discord.com/channels/313375426112389123/408694062862958592/1259072388969136201)). The good news is, you can find it easily by searching memory for `63 72 79 73 74 61 6C 00 47 47 45 66 66 65 63 74` (the strings "crystal" and "GGEffect") while inside a level. It is located `0x24` bytes back from the start of the strings (the red address in the screenshot below)

![[Pasted image 20240706220032.png]]

The number of gems is stored shifted for some reason. The screenshot above shows 2 gems collected (value of `0x2000`; in the screenshot the least significant byte is on the left)

The advantage of this address over the more convenient `0x52AECC` address is that you can set it to 4 gems (`0x4000`), then collect just one gem to conveniently spawn the [[Golden Gobbo]] for testing, without having to collect all the gems

Further, you can just freeze the value at 4 gems so you don't have to set it each time you re-enter the level, and it still works (though, this could have unintended effects when leaving the level, since the address is dynamic...)