---
aliases:
  - Plane
---
crackpot theory to investigate: croc seems to lag behind a bit when you pause the game. I wonder if you could like turbo-spam pause and slow croc down enough to get a triple cycle?
# Double Cycle
It is possible to hit Dante twice in one cycle, saving a huge chunk of time.
## Setup
Basically, you just have to make sure Croc is within a certain area on screen, and continuously fire bullets. To get right in the center of the valid range, you can line up using Croc's white eyeballs like so:
- x: line his eyeballs up with that cloud (tall dotted red line in the graphic)
- y: get about one eyeball length below the cloudline

![[Pasted image 20240825213121.png]]

Previous setups used Croc's bullet stream to line up, but you can line up with waaaaaay more precision using the position of Croc himself relative to the clouds!!

Also when you let off the controls, Croc still has a ton of residual inertia. If you look directly at Croc it is much easier to kill this inertia and ensure you don't drift out of range.
## Valid range
In order to get the double cycle, the white of Croc's eyes must be entirely in this purple blob (in the graphic, Croc is right on the bottom edge of the valid range)

![[ingame_valid_range.png]]

To find this valid range, over 100 x/y positions were tested and plotted in [this](https://docs.google.com/spreadsheets/d/11w86lGmExnKJyR_1F1PdaP2b6hGk1G4u8yd5vO4toUA/edit?usp=sharing) Google Sheet (Discord discussion starts [here](https://discord.com/channels/313375426112389123/408694062862958592/1276811925048787024)). The scatter plot is oriented the same way as the game screen. The blue area shows the valid range, yellow is unknown, and red is invalid. The green dot right in the center is at `(85750, 18875)`. The setup should get you very close to the green dot with minimal hassle

![[Pasted image 20240825224313.png]]

Adding more test points could reveal other valid ranges or interesting structures