---
aliases:
  - Soveena
  - Squid
---
It is possible to clip into the door early, as discovered by [[Paulmall]] [2019-11-26](https://discord.com/channels/313375426112389123/408694062862958592/648824097597423636)
- it is also possible (with the same technique or no?) for Secret Soveena ([discord](https://discord.com/channels/313375426112389123/408694062862958592/600156093435478048))
- did anyone find better / more consistent technique? what about [[PS1]]?
- (incorporate [this](https://discord.com/channels/313375426112389123/408694062862958592/1286287017843494973) info)

Bonkers [[Individual Level|IL]] strat, but you can do a big chain of [[Hazard Jump]]s to collect the [[Crystal]]s under the [[Monkey Bars]] more quickly

It's possible to [[Cutscene Break|CSB]] when entering the boss area, but you can't seem to skip a cycle with it :SnowSad:

Normally you can't throw the bomb box while you are jumping in the air. And if you land in the [[Water]] with it you drop it and it blows up. It would be sick if you could like throw it on a [[Hazard Jump]] frame when landing in the water, but it doesn't seem possible.

The address for Soveena's lives is in your save slot for some reason. For the first save slot (save slot 0) the address is `Croc2.exe+20432C`. It is possible to give her more than 3 lives lol

![[Pasted image 20240918213051.png]]

It turns out this is a generic **boss HP** field rather than a Soveena-specific one: it lives at offset `0x26C` inside the save slot and is reused by every boss. Save slots are `0x2000` bytes each, so:
- [[PC#US]]: `Croc2.exe+2040C0` + (slot × `0x2000`) + `0x26C`
- [[PC#EU]]: `Croc2.exe+20B2B0` + (slot × `0x2000`) + `0x26C`

Outside of a boss fight the value sits at 2. It is set to 3 at the start of a fight and decrements with each hit. Setting it to 0 externally is not the same as killing the boss: the death animation plays, but the transition never fires and the game softlocks. The transition seems to be triggered by the damage handler decrementing the value, not by the value itself

It would be nice if we could find a consistent way to get the final bomb throw super tight. Currently we pretty much play a game of chicken and pray we don't throw it too early

> the way I time it is if the green of croc's muzzle is over the fence, you can throw
> 
> &mdash; <cite>[[limbus]]</cite>, 2024-09-22 (in Twitch chat during a [[Thermospore|thermo]] [[Max%]] run)

(this seems useful; how does it account for the bobbing of the barrel or the variability in Croc's position standing on it, though? Also Croc's angle?)