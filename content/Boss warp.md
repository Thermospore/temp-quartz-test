Once you have unlocked the final boss for a tribe, the game will automatically warp you into it. This is often desirable, because it means you don't have to walk across the map to the boss.
# Bug
[[OG]] has a bug where the boss warp flags (`IntrosTriggered`) are not reset upon exiting to the main menu. This means if you reset a run after getting a boss warp, you will not get a boss warp in your next run (= huge time loss). To prevent the bug, simply restart your game to reset the boss warp flags.

Thankfully the bug is fixed in [[HD]]:

> The PSX version has a function called `init_gamestate`. In the remaster it was extended so that the very first thing that happens when `GameState == GS_TITLE` is to set `IntrosTriggered = 0`. ([source](https://discord.com/channels/313375426112389123/1533834309360680970/1574080218992218116))
# Delay / prevention
If you want to delay/prevent the boss warp (ex for routing reasons), you can exit the final level of the tribe using [[Game Over Abuse|GOA]]. You will still get the boss warp the next time you exit a level without [[Game Over Abuse|GOA]].