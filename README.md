# Folt

Folt is a minimalist matching puzzle created by Daniel Lutz. This repository is a recreation of this iOS app, using Pygame.


![](https://www.r-entries.com/etuliens/img/Folt/1.png) 

![](https://www.r-entries.com/etuliens/img/Folt/2.png) 

![](https://www.r-entries.com/etuliens/img/Folt/3.png) 

```python

#level_info[x][y] = [number_of_level, nb_color_level, nb_color_in_advance, grid_size, game_mode, nb_neighbours_min, nb_cell_to_remove, nb_diamonds_on_board]
level_info[1][1] = [1, 2, 3, [5,8], game_mode_available[0], 3, 15, 0]
level_info[2][1] = [2, 2, 3, [5,8], game_mode_available[0], 3, 20, 0]
level_info[3][1] = [3, 3, 3, [5,8], game_mode_available[0], 3, 15, 0]
#...
```
