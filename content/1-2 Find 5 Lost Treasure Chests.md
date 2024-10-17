---
aliases:
  - Chests
---
# Paths
## Right
This path (along with the left) is subject to an [[1-2 Find 5 Lost Treasure Chests#Elevator platform|Elevator platform]] cycle. When doing the right path first (or immediately after a [[Death Abuse|DA]]) you have tons of leeway to make the cycle, and it is likely impossible to make a better cycle

The timing is a little tricky, but at the start you can do lil [[Minecart]] hops [[chests_lilspeedhops.mp4|like so]] to maintain your speed up the slope
- actually, you don't even have to *hold* left/right like in the vid, even just lil taps are good enough to grab the left/right crystals
- alas, this strat is unneeded when doing right path first (or immediately after a [[Death Abuse|DA]]) because of the [[1-2 Find 5 Lost Treasure Chests#Elevator platform|Elevator platform]] cycle

No practical use, but you *can* front flip up [[Pasted image 20240627203846.png|this]] wall (find video evidence)

([[Thermospore|thermo]] note: I vaguely recall front flipping up [[Pasted image 20240626211758.png|this]] wall at some point...)

[[Pasted image 20240709193812.png|Here]] in the last room of the path, you can do a purple [[Gummi Buffer]] into the [[Golden Gobbo]] warp (any categories where this saves time?)

After grabbing the yellow [[Color Crystal|Gem]], you can quickly [[Death Abuse|DA]] back to the entrance by bouncing under the bridge ([video](https://www.youtube.com/watch?v=veTZwTu4wj0&t=79)). [[Paulmall]] timed this to be about 1 second faster than taking the [[Minecart]] back ([source](https://discord.com/channels/313375426112389123/408694062862958592/602070812693889037)). It could potentially save even more time if you use a purple [[Jelly Jump|Gummi]] (horizontal speed boost)
## Middle
[[limbus]] found a weird frontflip stomp jump strat with the [[Minecart]] elevator. Perhaps it could be abused to grab all the [[Crystal]]s in one trip, or to [[Death Abuse|DA]].
- [on the way in](https://discord.com/channels/313375426112389123/408694062862958592/1279769934536249380)
- [on the way out](https://youtu.be/JLR4RQwyErE?si=iJ_i1C9CyPnp3jaS&t=533)
- ([[Thermospore|thermo]] thought he got a [[Death Abuse|DA]] but it turned out he just accidentally enabled noclip in [[Cheat Engine]] lol... [video](https://discord.com/channels/313375426112389123/408694062862958592/1292824735586979842))

To collect all the [[Crystal]]s on the [[Minecart]] track, it seems to require at least two trips. After taking one trip in and collecting the chest, you have two options
1. [[Death Abuse|DA]] to the level entrance, and take another two trips on the [[Minecart]] (there + back)
2. backtrack and take one trip on the [[Minecart]], back to the level entrance
	- this seems faster ([link](https://discord.com/channels/313375426112389123/408694062862958592/1287289751467987014)), but it hasn't been timed

By jumping about [[Pasted image 20241007223617.png|here]] (on the ridge) you can easily grab the rear two [[Crystal]]s on the way in, then grab the first one on the way back out ([video](https://youtu.be/JLR4RQwyErE&t=461))

(vaguely remember there is something you can do on those zapper crystal [[Conveyor belt]] things to hard crash the game, but I forget)
## Left
This path (along with the right) is subject to an [[1-2 Find 5 Lost Treasure Chests#Elevator platform|Elevator platform]] cycle

The green [[Color Crystal|Gem]] on [[PS1]] is harder to collect than on [[PC]]; it is behind a tight turn like the purple [[Color Crystal|Gem]] ([video](https://youtu.be/wJ1YUwekFSs&t=263))

For [[Pasted image 20241006215824.png|the 2nd]] [[Minecart]] section, [[Thermospore]] finds [this](https://youtu.be/Wp1JCvygw-M?si=1_YfBMTB6kN-nEFW&t=200) strat pretty easy / consistent

< is it possible to do that [[Minecart]] section in one trip??? >

< what are the best strats for the various phases of [[Pasted image 20240626212515.png|this]] [[1-2 Find 5 Lost Treasure Chests#Elevator platform|Elevator platform]] cycle?? >

[[chests_shover_clip.mov|Here]] is a funky [[OoB]] [[Thermospore|thermo]] got on the shover thingy
# Elevator platform
[[Pasted image 20240626212046.png|These]] elevator things are present on both the left and right side. Their movement cycle has the following characteristics:
- starts from the moment you enter the level
- does not pause, even if you go far away
	- (the model will disappear when far enough away, but this is purely cosmetic)
- resets when you die

For each path, here is the memory address that stores the height (y) of the first platform:
- [[Pasted image 20240626212515.png|left]] - `Croc2.exe+2240D0`
- [[Pasted image 20240626212046.png|right]] - `Croc2.exe+2245A0`
# Minecart Crystal jankiness
The [[Crystal]]s on the [[Minecart]] tracks are notoriously difficult to grab, and some sections seem to require multiple trips. [[limbus]] suspects the developers placed the Crystals before the Minecart jumping mechanic was even fully developed, and they never got around to fully finishing the mechanic. Apparently in an April 1999 build of the game the Minecart jumping mechanic was entirely unfinished, yet the Crystals had already been placed. (discussion starts [here](https://discord.com/channels/313375426112389123/408694062862958592/1285460048243327018))