# Folt

Folt is a minimalist matching puzzle created by Daniel Lutz. This repository is a recreation of this iOS app, using Pygame.

Using only the arrows keys, you can move your position on the grid. By doing so, it will also place a colored square on your new position. The color of the cube is given by the top left color. The next three colors are actually displayed up there, along your current score and score to reach. Your current position in displayed as a hollow white circle.

When at least three square of the same colors are connected, they all disappear (except the one you are standing on). In normal levels, the goal is to make a given number of square dissapear. In "Collect the diamonds" levels, the player must remove pre-placed squares marked by a white filled circle (those are called diamonds).

A number of parameters can be tweak on a per-level basis:
- The coordinates of the level on the "Level selection menu".
- Its level number
- The number of colors the player is able to know in advance
- The size of the grid
- The game mode (currently limited to "remove_cell" aka normal mode and "collect_diamonds")
- The number of connected squares of the same color necessary to make them dissapear (by default 3)
- The score target. When in "Collect the diamonds" mode, it's the number of randomly placed diamonds.

Here is what setting up the levels look like in the code:
```python
game_mode_available = ['remove_cell','collect_diamonds']
#level_info[x position on grid][y position] = [level_number, nb_color_level, nb_color_in_advance, grid_size, game_mode, nb_neighbours_min, nb_cell_to_remove, nb_diamonds_on_board]
level_info[1][1] = [1, 2, 3, [5,8], game_mode_available[0], 3, 15, 0]
level_info[2][1] = [2, 2, 3, [5,8], game_mode_available[0], 3, 20, 0]
level_info[3][1] = [3, 3, 3, [5,8], game_mode_available[0], 3, 15, 0]
level_info[4][1] = [4, 2, 3, [5,8], game_mode_available[1], 3, 0, 1]
#...
```

## Splash screen
![](https://r-entries.com/etuliens/img/Folt/1.png) 

## Level selection
![](https://r-entries.com/etuliens/img/Folt/2.png) 

## Level
![](https://r-entries.com/etuliens/img/Folt/3.png) 
