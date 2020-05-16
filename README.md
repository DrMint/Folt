# Folt

Folt is a minimalist matching puzzle created by Daniel Lutz. This repository is a recreation of this iOS app, using Pygame.

## Splash screen
![](https://www.r-entries.com/etuliens/img/Folt/1.png) 

## Level selection
![](https://www.r-entries.com/etuliens/img/Folt/2.png) 

## Level
![](https://www.r-entries.com/etuliens/img/Folt/3.png) 

```python

game_mode_available = ['remove_cell','collect_diamonds']
#level_info[x position on grid][y position] = [level_number, nb_color_level, nb_color_in_advance, grid_size, game_mode, nb_neighbours_min, nb_cell_to_remove, nb_diamonds_on_board]
level_info[1][1] = [1, 2, 3, [5,8], game_mode_available[0], 3, 15, 0]
level_info[2][1] = [2, 2, 3, [5,8], game_mode_available[0], 3, 20, 0]
level_info[3][1] = [3, 3, 3, [5,8], game_mode_available[0], 3, 15, 0]
#...
```
