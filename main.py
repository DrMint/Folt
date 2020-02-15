import pygame
import math
import os
import os.path
import random

#_____________________________________________[GAME_ENGINE CLASSES]_________________________________________#

class Color(object):
    '''A color set.'''
    def __init__(self, custom1 = (0,0,0), custom2 = (0,0,0), custom3 = (0,0,0)):

        self.black  = (0,0,0)
        self.white  = (255,255,255)
        self.azure  = (100,200,200)
        self.ocean  = (45,60,70)
        self.red    = (250,25,45)
        self.grey   = (70,100,100)
        self.orange = (240,75,50)
        self.yellow = (250,120,0)
        self.pink   = (255,200,200)
        self.cloud  = (240,240,250)
        self.dark   = (20,20,20)



        
color = Color()                                             # Give a name to the module's prefix

class Screen_info(object):
    '''Information on the screen / window.
    Attributes:
        x: Resolution in px.
        y: Resolution in px.
        fps: meaning frame per second, usually 60fps.
        fullscreen: True or False, use the game in fullscreen or not.
        pg: Used by pygame to refer game's window.
    '''
    def __init__(self, x = 0, y = 0, fps = 0, fullscreen = False):
        self.x = x
        self.y = y
        self.fps = fps
        self.fullscreen = fullscreen   
screen = Screen_info()                                      # Give a name to the module's prefix

class Game_info(object):
    '''Informations on the game, and his creator.
    Attributes:
        title: Title of the game 
        author: Author / creator of the game.
        year: When the game was created.
        month: When the game was created.
        day: When the game was created.
    '''
    def __init__(self, title = "", author = "", year = 1970, month = 1, day = 1):
        self.title = title
        self.author = author
        self.year = year
        self.month = month
        self.day = day
game_info = Game_info()                                      # Give a name to the module's prefix


#_________________________________________[GAME_ENGINE FUNCTIONS]___________________________________________#




#________________________________________[GAME_ENGINE CONFIGURATION]________________________________________#


# [Game informations] #

game_info.title = "Folt"
game_info.author = "Thomas Barillot"
game_info.year = 2017
game_info.month = 12
game_info.day = 18



# [Window options]

screen.x, screen.y = 576, 1024    #Portait mode
#screen.x, screen.y = 1840, 1035
screen.orientation = 'vertical' if screen.x <= screen.y else 'horizontal'
screen.fps = 60
screen.fullscreen = False



# [Pythongame related commands] | Shouldn't have to change them

screen.pg = pygame.display.set_mode((screen.x,screen.y))            # Create a window with a specific size.
pygame.display.set_icon(pygame.image.load('./image/icon.png'))      # Set an icon for the Game (by default : './image/icon.png')
pygame.mixer.pre_init(44100, -16, 1, 512)                           # Custom Audio mixer, without it audio has lattency
pygame.init()                                                       # Allow to use pygame's modules.
pygame.display.set_caption(game_info.title)                         # Change window title (Game title by default)
clock = pygame.time.Clock()                                         # Used by pygame to manage how fast the screen updates
if screen.fullscreen == True: pygame.display.toggle_fullscreen()    # Switch the game into fullscreen mode if wanted.


# [Import sound] | Usage: sound['name'] --> pygame.mixer.Sound() #

sound_directory = "./sound/"
sound = {
    'hit_wall'   : pygame.mixer.Sound("./sound/hit_wall.wav"),
    'hit_paddle' : pygame.mixer.Sound("./sound/hit_paddle.wav"),
    'win_sound'  : pygame.mixer.Sound("./sound/win.wav"),
}



# [Import font] | Usage: font['name'] --> pygame.font.Font() #


font_directory = "./font/"                                  # By default, font_directory = "./font/"
font = {

    'title'   : pygame.font.Font(font_directory + "game_font.ttf", min(screen.x, screen.y) // 4  ),
    'h1'      : pygame.font.Font(font_directory + "game_font.ttf", min(screen.x, screen.y) // 10 ),
    'h2'      : pygame.font.Font(font_directory + "game_font.ttf", min(screen.x, screen.y) // 10 ),
    'score'   : pygame.font.Font(font_directory + "game_font.ttf", min(screen.x, screen.y) // 10 ),
    'hscore'   : pygame.font.Font(font_directory + "game_font.ttf", min(screen.x, screen.y) // 15 ),
}


# [Import images] | It's important to use .convert() or .convert_alpha() to make the game run faster.


#________________________________________[GAME FONCTIONS]________________________________________#


def Test_if_stuck():

    global grid, current_pos, grid_size

    if current_pos[0] == 0:
        if current_pos[1] == 0:
            if grid[current_pos[0] + 1][current_pos[1]] != 0 and grid[current_pos[0]][current_pos[1] + 1] != 0:
                return True
        elif current_pos[1] == grid_size[1] - 1:
            if grid[current_pos[0] + 1][current_pos[1]] != 0 and grid[current_pos[0]][current_pos[1] - 1] != 0:
                return True
        else:
            if grid[current_pos[0] + 1][current_pos[1]] != 0 and grid[current_pos[0]][current_pos[1] - 1] != 0 and grid[current_pos[0]][current_pos[1] + 1] != 0:
                return True
    elif current_pos[0] == grid_size[0] - 1:
        if current_pos[1] == 0:
            if grid[current_pos[0] - 1][current_pos[1]] != 0 and grid[current_pos[0]][current_pos[1] + 1] != 0:
                return True
        elif current_pos[1] == grid_size[1] - 1:
            if grid[current_pos[0] - 1][current_pos[1]] != 0 and grid[current_pos[0]][current_pos[1] - 1] != 0:
                return True
        else:
            if grid[current_pos[0] - 1][current_pos[1]] != 0 and grid[current_pos[0]][current_pos[1] - 1] != 0 and grid[current_pos[0]][current_pos[1] + 1] != 0:
                return True
    else:
        if current_pos[1] == 0:
            if grid[current_pos[0] + 1][current_pos[1]] != 0 and grid[current_pos[0] - 1][current_pos[1]] != 0 and grid[current_pos[0]][current_pos[1] + 1] != 0:
                return True
        elif current_pos[1] == grid_size[1] - 1:
            if grid[current_pos[0] + 1][current_pos[1]] != 0 and grid[current_pos[0] - 1][current_pos[1]] != 0 and grid[current_pos[0]][current_pos[1] - 1] != 0:
                return True
        else:
            if grid[current_pos[0] + 1][current_pos[1]] != 0 and grid[current_pos[0] - 1][current_pos[1]] != 0 and grid[current_pos[0]][current_pos[1] - 1] != 0 and grid[current_pos[0]][current_pos[1] + 1] != 0:
                return True

    return False



def list_neighbours(position = [0,0]):

    global grid_size

    if position[0] == 0:
        if position[1] == 0:
            return [[position[0], position[1] + 1],[position[0] + 1, position[1]]]
        elif position[1] == grid_size[1] - 1:
            return [[position[0], position[1] - 1],[position[0] + 1, position[1]]]
        else:
            return [[position[0], position[1] - 1],[position[0], position[1] + 1],[position[0] + 1, position[1]]]
    elif position[0] == grid_size[0] - 1:
        if position[1] == 0:
            return [[position[0], position[1] + 1],[position[0] - 1, position[1]]]
        elif position[1] == grid_size[1] - 1:
            return [[position[0], position[1] - 1],[position[0] - 1, position[1]]]
        else:
            return [[position[0], position[1] - 1],[position[0], position[1] + 1],[position[0] - 1, position[1]]]
    else:
        if position[1] == 0:
            return [[position[0], position[1] + 1],[position[0] + 1, position[1]],[position[0] - 1, position[1]]]
        elif position[1] == grid_size[1] - 1:
            return [[position[0], position[1] - 1],[position[0] + 1, position[1]],[position[0] - 1, position[1]]]
        else:
            return [[position[0], position[1] - 1],[position[0], position[1] + 1],[position[0] + 1, position[1]],[position[0] - 1, position[1]]]

    return 'Error'


def Draw_everything(mode = 'game'):

    global screen, colors, color, screen, game_mode, grid_size, grid, grid_cell_size, grid_top_margin, grid_left_margin, font, nb_cell_to_remove, nb_cell_removed, nb_diamonds_get, nb_diamonds_on_board, level_grid_size, level_grid, level_grid_cell_size, level_grid_top_margin, level_grid_left_margin, level_info

    if mode == 'game':
        screen.pg.fill(color.cloud)
    elif mode == 'menu':
        screen.pg.fill(color.white)

    
    pygame.draw.rect(screen.pg, color.dark, [0,0, screen.x, screen.y * 0.1])


    if mode == 'game':
        i = -1
        for e in list_next_colors:
            i += 1
            pygame.draw.rect(screen.pg, colors[e], [0.1 * screen.y * 0.25 + i * (screen.y * 0.1 * 0.6),0.1 * screen.y * 0.25, screen.y * 0.1 * 0.5, screen.y * 0.1 * 0.5])

        if game_mode == 'remove_cell':
            score_surface = font['score'].render(str(nb_cell_removed) + '   /   ' + str(nb_cell_to_remove), True, color.white)
        elif game_mode == 'collect_diamonds':
            score_surface = font['score'].render(str(nb_diamonds_get) + '   /   ' + str(nb_diamonds_on_board), True, color.white)
        screen.pg.blit(score_surface, ((screen.x - score_surface.get_width() - (screen.y * 0.1 * 0.6 * nb_color_in_advance))/2 + (screen.y * 0.1 * 0.6 * nb_color_in_advance), (screen.y * 0.1 - score_surface.get_height())/2))

    
        #Draw the array
        pygame.draw.rect(screen.pg, color.white, [grid_left_margin, grid_top_margin, grid_cell_size * grid_size[0], grid_cell_size * grid_size[1]])
        for x in range(grid_size[0]):
            for y in range(grid_size[1]):
                if grid[x][y] != 0:
                    pygame.draw.rect(screen.pg, colors[grid[x][y]], [grid_left_margin + grid_cell_size * x, grid_top_margin + grid_cell_size * y, grid_cell_size, grid_cell_size])
                    if current_pos == [x,y]:
                        pygame.draw.circle(screen.pg, color.white, (int(grid_left_margin + grid_cell_size * (x + 0.5)),int(grid_top_margin + grid_cell_size * (y + 0.5))), int(0.10 * grid_cell_size))
                        pygame.draw.circle(screen.pg, colors[grid[x][y]], (int(grid_left_margin + grid_cell_size * (x + 0.5)),int(grid_top_margin + grid_cell_size * (y + 0.5))), int(0.10 * grid_cell_size) - 2)

                    if diamonds[x][y] == True:
                        pygame.draw.circle(screen.pg, color.white, (int(grid_left_margin + grid_cell_size * (x + 0.5)),int(grid_top_margin + grid_cell_size * (y + 0.5))), int(0.10 * grid_cell_size))
                         
    elif mode == 'menu':
        for x in range(level_grid_size[0]):
            for y in range(level_grid_size[1]):
                if level_grid[x][y] != 0:
                    pygame.draw.rect(screen.pg, colors[level_grid[x][y]], [level_grid_left_margin + level_grid_cell_size * x, level_grid_top_margin + level_grid_cell_size * y, level_grid_cell_size, level_grid_cell_size])
                    level_number_surface = font['h2'].render(str(level_info[x][y][0]), False, color.white)
                    screen.pg.blit(level_number_surface, (level_grid_left_margin + level_grid_cell_size * x + (level_grid_cell_size - level_number_surface.get_width()) / 2, level_grid_top_margin + level_grid_cell_size * y + (level_grid_cell_size - level_number_surface.get_height()) / 2))
                    if level_current_pos == [x,y]:
                        pygame.draw.rect(screen.pg, color.white, [level_grid_left_margin + level_grid_cell_size * (x + 0.1),level_grid_top_margin + level_grid_cell_size * (y + 0.85), level_grid_cell_size * 0.8, level_grid_cell_size * 0.05])
                        
                    
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()



def Grid_and_Grid_related_variable():

    global grid_size, grid, grid_cell_size, grid_left_margin, grid_top_margin, screen

    grid = [[0 for y in range(grid_size[1])] for x in range(grid_size[0])]
    
    if grid_size[1] >= grid_size[0]:
        grid_cell_size = math.ceil((0.8 * screen.y) / grid_size[1])
    else:
        grid_cell_size = math.ceil((0.8 * screen.x) / grid_size[0])

    grid_left_margin = (screen.x - (grid_cell_size * grid_size[0])) / 2
    grid_top_margin = screen.y * 0.2 - grid_left_margin


def level_Grid_and_Grid_related_variable():

    global level_grid_size, level_grid, level_grid_cell_size, level_grid_left_margin, level_grid_top_margin, screen

    level_grid = [[0 for y in range(level_grid_size[1])] for x in range(level_grid_size[0])]
    
    if level_grid_size[1] >= level_grid_size[0]:
        level_grid_cell_size = math.ceil((0.8 * screen.y) / level_grid_size[1])
    else:
        level_grid_cell_size = math.ceil((0.8 * screen.x) / level_grid_size[0])

    level_grid_left_margin = (screen.x - (level_grid_cell_size * level_grid_size[0])) / 2
    level_grid_top_margin = screen.y * 0.1 - level_grid_left_margin


def Unlock_next_level():

    global level_current_pos, level_info, level_grid_size, level_grid

    search_for_level = level_info[level_current_pos[0]][level_current_pos[1]][0] + 1

    for x in range(level_grid_size[0]):
        for y in range(level_grid_size[1]):
            if level_grid[x][y] == len(colors) - 1 and level_info[x][y][0] == search_for_level:
                level_grid[x][y] = (level_grid[level_current_pos[0]][level_current_pos[1]] % (len(colors) - 2)) + 1


#________________________________________[GAME CONFIGURATION]________________________________________#

# Here goes any settings which you want an easy access to.



#________________________________________________[GAME]______________________________________________#


# --- [ FIRST PART - Press button to continue] ---


#Set multiple variables to false
key_pressed = False
done = False
quit_all = False

while not done and not quit_all:

    # --- Quit game if cross clicked
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit_all = True    

    # --- Player input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE] or keys[pygame.K_RETURN]:
        if key_pressed == False:
            key_pressed = True
            done = True

    else:
        key_pressed = False

    #Create 
    F_title_surface = font['title'].render("F", False, color.white)
    O_title_surface = font['title'].render("O", False, color.white)
    L_title_surface = font['title'].render("L", False, color.white)
    T_title_surface = font['title'].render("T", False, color.white)
    Play_title_surface = font['h1'].render("Play", False, color.white)

    screen.pg.fill(color.cloud)

    # --- Draw the title screen
    if screen.orientation == 'horizontal':

        pygame.draw.rect(screen.pg, color.grey, [screen.x / 6, screen.y / 4, screen.x / 6 + 2, screen.x / 6])
        pygame.draw.rect(screen.pg, color.azure, [screen.x / 6 * 2, screen.y / 4, screen.x / 6 + 2, screen.x / 6])
        pygame.draw.rect(screen.pg, color.ocean, [screen.x / 6 * 3, screen.y / 4, screen.x / 6 + 2, screen.x / 6])
        pygame.draw.rect(screen.pg, color.red, [screen.x / 6 * 4, screen.y / 4, screen.x / 6 + 2, screen.x / 6])

        pygame.draw.rect(screen.pg, color.black, [screen.x / 6 * 2, screen.y / 4 + screen.x / 6 * 1.1, screen.x / 6 * 2, screen.y / 10])
    else:
        pygame.draw.rect(screen.pg, color.grey, [screen.x / 4, screen.x / 4, screen.x / 4, screen.x / 4])
        pygame.draw.rect(screen.pg, color.azure, [screen.x * 2 / 4, screen.x / 4, screen.x / 4, screen.x / 4])
        pygame.draw.rect(screen.pg, color.ocean, [screen.x / 4, screen.x / 4 * 2, screen.x / 4, screen.x / 4])
        pygame.draw.rect(screen.pg, color.red, [screen.x / 4 * 2, screen.x / 4 * 2, screen.x / 4, screen.x / 4])
        screen.pg.blit(F_title_surface, ((screen.x / 4 + (screen.x / 4 - F_title_surface.get_width()) / 2, screen.x / 4 + (screen.x / 4 - F_title_surface.get_height()) / 2)))
        screen.pg.blit(O_title_surface, ((screen.x / 4 * 2 + (screen.x / 4 - O_title_surface.get_width()) / 2, screen.x / 4 + (screen.x / 4 - O_title_surface.get_height()) / 2)))
        screen.pg.blit(L_title_surface, ((screen.x / 4 + (screen.x / 4 - L_title_surface.get_width()) / 2, screen.x / 4 * 2 + (screen.x / 4 - L_title_surface.get_height()) / 2)))
        screen.pg.blit(T_title_surface, ((screen.x / 4 * 2 + (screen.x / 4 - T_title_surface.get_width()) / 2, screen.x / 4 * 2 + (screen.x / 4 - T_title_surface.get_height()) / 2)))
        
        pygame.draw.rect(screen.pg, color.black, [screen.x / 4, screen.x / 4 * 3 + screen.y / 8, screen.x / 2, screen.x / 8])
        screen.pg.blit(Play_title_surface, ((screen.x / 4 + abs(screen.x / 2 - Play_title_surface.get_width()) / 2, screen.x / 4 * 3 + screen.y / 8 + (screen.x / 8 - Play_title_surface.get_height()) / 2)))
        
    pygame.display.flip()
    clock.tick(screen.fps)



# --- [ SECOND PART - Select level] ---

colors = [color.white, color.azure, color.red, color.ocean, color.cloud]
game_mode_available = ['remove_cell','collect_diamonds']

level_grid_size = [7,8]
level_Grid_and_Grid_related_variable()
level_current_pos = [1,1]

level_grid[1][1] = 1
level_grid[2][1] = len(colors) - 1
level_grid[3][1] = len(colors) - 1
level_grid[4][1] = len(colors) - 1
level_grid[5][1] = len(colors) - 1
level_grid[5][2] = len(colors) - 1
level_grid[5][3] = len(colors) - 1
level_grid[5][4] = len(colors) - 1
level_grid[4][4] = len(colors) - 1
level_grid[3][4] = len(colors) - 1
level_grid[2][4] = len(colors) - 1
level_grid[1][4] = len(colors) - 1
level_grid[1][5] = len(colors) - 1
level_grid[1][6] = len(colors) - 1

level_info = [[0 for y in range(level_grid_size[1])] for x in range(level_grid_size[0])]
#lvel_info[x][y] = [number_of_level, nb_color_level, nb_color_in_advance, grid_size, game_mode, nb_neighbours_min, nb_cell_to_remove, nb_diamonds_on_board]
level_info[1][1] = [1, 2, 3, [5,8], game_mode_available[0], 3, 15, 0]
level_info[2][1] = [2, 2, 3, [5,8], game_mode_available[0], 3, 20, 0]
level_info[3][1] = [3, 3, 3, [5,8], game_mode_available[0], 3, 15, 0]
level_info[4][1] = [4, 2, 3, [5,8], game_mode_available[1], 3, 0, 1]
level_info[5][1] = [5, 2, 3, [5,8], game_mode_available[0], 3, 20, 0]
level_info[5][2] = [6, 3, 3, [7,6], game_mode_available[0], 3, 20, 0]
level_info[5][3] = [7, 2, 3, [5,8], game_mode_available[1], 3, 0, 2]
level_info[5][4] = [8, 3, 3, [5,8], game_mode_available[0], 3, 35, 0]
level_info[4][4] = [9, 2, 3, [5,8], game_mode_available[1], 3, 0, 1]
level_info[3][4] = [10, 2, 3, [8,13], game_mode_available[0], 3, 50, 0]
level_info[2][4] = [11, 3, 3, [7,6], game_mode_available[0], 3, 20, 0]
level_info[1][4] = [12, 2, 3, [5,8], game_mode_available[1], 3, 0, 5]
level_info[1][5] = [13, 3, 1, [10,16], game_mode_available[1], 3, 0, 20]
level_info[1][6] = [14, 3, 1, [10,16], game_mode_available[0], 3, 100, 0]


while not quit_all:

    #Set multiple variables to false
    has_moved = False
    done = False
    
    Draw_everything('menu')
    
    while not done and not quit_all:

        #Quit game if cross clicked
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_all = True

        # --- Player input
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_UP]:
            if key_pressed == False:
                key_pressed = True
                if level_current_pos[1] - 1 >= 0 and level_grid[level_current_pos[0]][level_current_pos[1] - 1] != 0 and level_grid[level_current_pos[0]][level_current_pos[1] - 1] != len(colors) - 1:
                    level_current_pos[1] -= 1
                    has_moved = True
                    
        elif keys[pygame.K_DOWN]:
            if key_pressed == False:
                key_pressed = True
                if level_current_pos[1] + 1 < level_grid_size[1] and level_grid[level_current_pos[0]][level_current_pos[1] + 1] != 0 and level_grid[level_current_pos[0]][level_current_pos[1] + 1] != len(colors) - 1:
                    level_current_pos[1] += 1
                    has_moved = True

        elif keys[pygame.K_LEFT]:
            if key_pressed == False:
                key_pressed = True
                if level_current_pos[0] - 1 >= 0 and level_grid[level_current_pos[0] - 1][level_current_pos[1]] != 0 and level_grid[level_current_pos[0] - 1][level_current_pos[1]] != len(colors) - 1:
                    level_current_pos[0] -= 1
                    has_moved = True
                    
        elif keys[pygame.K_RIGHT]:
            if key_pressed == False:
                key_pressed = True
                if level_current_pos[0] + 1 < level_grid_size[0] and level_grid[level_current_pos[0] + 1][level_current_pos[1]] != 0 and level_grid[level_current_pos[0] + 1][level_current_pos[1]] != len(colors) - 1:
                    level_current_pos[0] += 1
                    has_moved = True
                    
        elif keys[pygame.K_SPACE] or keys[pygame.K_RETURN]:
            if key_pressed == False:
                key_pressed = True
                done = True
            
        else:
            key_pressed = False


        if has_moved == True:

            Draw_everything('menu')



    # --- [ THIRD PART - Level] ---
    
    #Colors in the game
    nb_color_level = level_info[level_current_pos[0]][level_current_pos[1]][1]
    nb_color_in_advance = level_info[level_current_pos[0]][level_current_pos[1]][2]
    list_next_colors = [random.randint(1,nb_color_level) for e in range(nb_color_in_advance)]
    
    #Grid
    grid_size = level_info[level_current_pos[0]][level_current_pos[1]][3]
    Grid_and_Grid_related_variable()
    current_pos = [int(grid_size[0] / 2),int(grid_size[1] / 2)]
    grid[current_pos[0]][current_pos[1]] = random.randint(1,nb_color_level)
    
    #Game mode and difficulty
    game_mode = level_info[level_current_pos[0]][level_current_pos[1]][4]
    nb_neighbours_min = level_info[level_current_pos[0]][level_current_pos[1]][5]
    
    # --- Game Objective
    #If the game mode is Remove Cells
    nb_cell_removed = 0
    nb_cell_to_remove = level_info[level_current_pos[0]][level_current_pos[1]][6]

    #If the game mode is Collect Diamonds
    nb_diamonds_get = 0
    nb_diamonds_on_board = level_info[level_current_pos[0]][level_current_pos[1]][7]
    diamonds = [[False for y in range(grid_size[1])] for x in range(grid_size[0])]
    if game_mode == 'collect_diamonds':
        i = 0
        while i < nb_diamonds_on_board:
            temp = [random.randint(0,grid_size[0] - 1),random.randint(0,grid_size[1] - 1)]
            if diamonds[temp[0]][temp[1]] == False and temp != current_pos:
                diamonds[temp[0]][temp[1]] = True
                grid[temp[0]][temp[1]] = random.randint(1,nb_color_level)
                i += 1

    #Set multiple variables to false
    key_pressed = False
    has_moved = False
    stuck = False
    done = False

    #First draw
    Draw_everything()


    while not done and not quit_all:
        
        # --- Quit game if cross clicked
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_all = True
                
        # --- Player input
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            if key_pressed == False:
                key_pressed = True
                if current_pos[1] - 1 >= 0 and grid[current_pos[0]][current_pos[1] - 1] == 0:
                    current_pos[1] -= 1
                    has_moved = True
                    
        elif keys[pygame.K_DOWN]:
            if key_pressed == False:
                key_pressed = True
                if current_pos[1] + 1 < grid_size[1] and grid[current_pos[0]][current_pos[1] + 1] == 0:
                    current_pos[1] += 1
                    has_moved = True

        elif keys[pygame.K_LEFT]:
            if key_pressed == False:
                key_pressed = True
                if current_pos[0] - 1 >= 0 and grid[current_pos[0] - 1][current_pos[1]] == 0:
                    current_pos[0] -= 1
                    has_moved = True
                    
        elif keys[pygame.K_RIGHT]:
            if key_pressed == False:
                key_pressed = True
                if current_pos[0] + 1 < grid_size[0] and grid[current_pos[0] + 1][current_pos[1]] == 0:
                    current_pos[0] += 1
                    has_moved = True
        else:
            key_pressed = False
            
                
        # --- Game code
        if has_moved == True:
            has_moved = False
            grid[current_pos[0]][current_pos[1]] = list_next_colors[0]

            #Shift every items of next list color, and add a new random one at the end    
            for i in range(len(list_next_colors) - 1):
                list_next_colors[i] = list_next_colors[i + 1]
            list_next_colors[len(list_next_colors) - 1] = random.randint(1,nb_color_level)

            #Create a list called List_voisin_same_color which contains cells that are neighbours to current cell and of the same color. 
            List_a_verif = [current_pos]
            List_voisin_same_color = [current_pos]
            while len(List_a_verif) > 0:
                for cell in List_a_verif:
                    for e in list_neighbours(cell):
                        if e not in List_a_verif and e not in List_voisin_same_color:
                            if grid[e[0]][e[1]] == grid[current_pos[0]][current_pos[1]]:
                                List_voisin_same_color += [e]
                                List_a_verif += [e]
                    List_a_verif.remove(cell)

            #If there is more than an certains amount of neighbours with the same color, kill them and add points
            if len(List_voisin_same_color) >= nb_neighbours_min:
                List_voisin_same_color.remove(current_pos)
                for cell in List_voisin_same_color:
                    grid[cell[0]][cell[1]] = 0
                    if game_mode == 'remove_cell':
                        nb_cell_removed += 1
                    elif game_mode == 'collect_diamonds':
                        if diamonds[cell[0]][cell[1]] == True:
                            diamonds[cell[0]][cell[1]] = False
                            nb_diamonds_get += 1

            #Test if stuck
            if Test_if_stuck() == True:
                stuck = True
                done = True

            #Test if Win
            if game_mode == 'remove_cell':
                if nb_cell_removed >= nb_cell_to_remove:
                    Unlock_next_level()
                    done = True
                    
            elif game_mode == 'collect_diamonds':
                if nb_diamonds_get >= nb_diamonds_on_board:
                    Unlock_next_level()
                    done = True

            # --- Drawing code is inside if has_moved == True
            Draw_everything() 


        #Limit to screen.fps frames per second
        clock.tick(screen.fps)
 

# Close the window and quit.
pygame.quit()
