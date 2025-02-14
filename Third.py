import random
import pygame
pygame.init()

#Variable definitions
TYF = [False, True]
bBlack = (0,0,22) #blueblack
lred = (255, 160, 143) #light red
lgreen = (192,255,211) #light green
lbrown = (254, 191, 1) #light brown
blue_grey = (128, 128,150)
width, height = 700, 600
til_size = 20
grid_h = height // til_size
grid_w = width  // til_size

FPS = 60

screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

class cells:
    """ Manage cells. Type is a boolean value
    that determines they way each cell grows.
    Rules: 1. Not 2 types of cells in the same cell.
    2. type 0 cells grow vertically and type 1 vertically
    upwards and backwards. Type 2 creates 1 - 3 type 0 cells.
    """
    def __init__(self, type):
        self.type = type
    def ad_grid(self):
        'Adds cells to the simulation vertically, horizontally and diagonally depending of the type.'
        #Avoid changing the self.position since it causes a runtime error
        new_pos = set()
        match self.type:
            case 0:
                for pos in self.position:
                    x, y = pos
                    # adds cell up
                    if y - 1 >= 0 and (x, y - 1) not in self.position:
                        new_pos.add((x, y - 1))
                    #Adds new cell down
                    if y + 1 < grid_h and (x, y + 1) not in self.position:
                        new_pos.add((x, y + 1))
            case 1:
                for pos in self.position:
                    x, y = pos
                    for dx in [-1, 1]:
                        for dy in [1, 0, - 1]:
                            # grows cell horizontally, and diagonally up
                            ran = random.randint(0,1)
                            check = TYF[ran]
                            nPos = (x +dx, y+dy)
                            if check:
                                if nPos not in self.position and nPos not in new_pos:
                                    new_pos.add(nPos)
            case 2:
                returnset = set()
                for pos in self.position:
                    f =  seedgen(pos)
                    for x in f:
                        if x not in returnset:
                            returnset.add(x)
                return returnset
        for x in new_pos: #Use a for loop to make it hashable  
            self.position.add(x)    
        return None
    #Variables
    position = set()
    
def draw_grid(positions, position2, position3):
    "This function draws the grid"
    for post in position2:
        col, row = post
        pygame.draw.rect(screen, lgreen,(*(col*til_size,row*til_size), til_size, til_size))
        
    for post in positions:
        col, row = post
        topLeft = (col * til_size, row * til_size)
        pygame.draw.rect(screen, lred, (*topLeft, til_size, til_size))
    
    for post in position3:
        col, row = post
        pygame.draw.rect(screen, lbrown,(*(col*til_size,row*til_size), til_size, til_size))

    for row in range(grid_h): 
        pygame.draw.line(screen, bBlack, (width, row * til_size), (0, row * til_size))

    for col in range(grid_w):
        pygame.draw.line(screen, bBlack, (col * til_size, 0), (col * til_size, height))
def add_leaves(positions):
    # adds leaves
    newleaves = set()
    for pos in positions:
        x, y = pos 
        d = x +1
        while d in positions:
            d += 1
        newleaves.add((d, y)) 
        d = x -1
        while d in positions:
            d -= 1
        newleaves.add((d, y))
        
    return newleaves
def not_repeat(set1, set2):
    set1new = set()
    set2new = set()
    for x in set1:
        set1new.add(x)
    for x in set2:
        if x not in set1:
            set2new.add(x)
    return set1new, set2new
def getpos():
    x, y = pygame.mouse.get_pos()
    col = x // til_size
    row = y // til_size
    pos = (col, row)
    return pos
def seedgen(pos):
    f = set()
    x, y = pos
    onetofive = random.randint(0, 5)
    match onetofive:
        # case 0: 3 trunks
        # case 1, 2: 2 trunks in each side
        case 0:
            dx = x + 1
            fx = x - 1
            f = {(dx, y), (fx, y), (x, y)}
        case 1:
            dx = x + [-1, 1][random.randint(0,1)]
            f = {(dx, y),(x, y)}

        case 2:
            dx = x + [-1, 1][random.randint(0,1)]
            f = {(dx, y), (x, y)}
        case 3:
            f = {(x, y)}
        case 4:
            a = [-1, -2, 2, 1][random.randint(0, 3)]
            f = {(x - a, y)}
    return f
def run():
    "This function run the simulation"
    #Vars
    count = 0
    running = True
    playing = False
    up_frecuency = 32
    leavespawn = 0
    leavespwanable = 0 
    #class objects
    trunk = cells(0)
    leaves = cells(1)
    seed = cells(2)
    trunk.position, leaves.position, seed.position = set(), set(), set() #Solves issue related to both trunk and leaves being placed at same time.

    #position are the cells that are displayed
    
    while running:
        clock.tick(FPS)
        #Each game "year" happens when the counter gets to the up_frecuency
        if playing == True:
            
            count += 1
             
        if count >= up_frecuency: #controls update time
            if seed.position != set():
                s = seed.ad_grid()
                for x in s:
                    trunk.position.add(x)
                seed.position = set()
            if len(trunk.position) > 0 and leavespawn == 0:
               #Add leaves at the start on the first
               leaves.position = add_leaves(trunk.position)
               leavespawn = 1
               leavespwanable = 0 # makes sure leaves don't spawn twice on an update
            count = 0
            trunk.ad_grid()
            if leavespwanable == 1:
                leaves.ad_grid()
                trunk.position, leaves.position = not_repeat(trunk.position, leaves.position)
            print(trunk.position)
            print("--------------")
            print(leaves.position)
            leavespwanable = 1
            
        pygame.display.set_caption('Playing' if playing else "paused")
        
        #Mouse actions

     

        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                # Happens when the player quits the game
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = getpos()
                if event.button == 1:
                    if pos in trunk.position:
                        trunk.position.remove(pos)
                    else:
                        trunk.position.add(pos)
                if event.button == 2:
                    if pos in seed.position:
                        seed.position.remove(pos)
                    else:
                        seed.position.add(pos)
                if event.button == 3:
                    if pos in leaves.position:
                        leaves.position.remove(pos)
                    else:
                        leaves.position.add(pos)
            if event.type == pygame.KEYDOWN: 
            # when pressing space it pauses or plays the simulation.
                if event.key == pygame.K_SPACE: 
                    playing = not playing
                if event.key == pygame.K_c:
                    print("Game cleaned!!!!\n")
                    trunk.position, leaves.position, seed.position = set(), set(), set()
                    leavespawn = 0
                    count = 0
                    playing = False
        screen.fill(blue_grey)
        draw_grid(trunk.position, leaves.position, seed.position)
        pygame.display.update()
    pygame.quit()
run()