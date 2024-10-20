---
aliases:
  - Gem
  - Colour Crystal
---
(also see: [[Crystal]])

![[Pasted image 20240701204704.png]]

We almost always call these "gems", for whatever reason

`0x52AECC` contains the number of gems you have collected in the current level (independent of save slot). As you would expect, it starts at 0 and goes up to 5.

There is another address which contains the same information, but with benefits we will get to later. However, it is not a static address and reaching it via pointers might not be possible (see [here](https://discord.com/channels/313375426112389123/408694062862958592/1259072388969136201)). The good news is, you can find it easily by searching memory for:
```
63 72 79 73 74 61 6C 00 47 47 45 66 66 65 63 74
```
(the strings "crystal" and "GGEffect") while inside a level. The address is located `0x24` bytes back from the start of the strings (the red address in the screenshot below)

![[Pasted image 20240706220032.png]]

The number of gems is stored shifted over by 12 bits (which doesn't seem to be uncommon in this game; see [this](https://discord.com/channels/313375426112389123/408694062862958592/1259448437032751134) comment from [[hdc0]]). So the screenshot above shows 2 gems collected (value of `0x2000`; in the screenshot the least significant byte is on the left)

The advantage of this address over the more convenient `0x52AECC` address is that you can set it to 4 gems (`0x4000`), then collect just one gem to conveniently spawn the [[Golden Gobbo]] for testing, without having to collect all 5 gems

[Here](https://discord.com/channels/313375426112389123/408694062862958592/1259448437032751134) is a convenient Lua script written by [[hdc0]] that automates setting the value

(note that while you *can* simply freeze the value at 4 gems, this could have unintended effects when leaving/re-entering the level, because the address is not static...)