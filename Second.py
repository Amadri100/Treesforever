import random
import pygame
pygame.init()

#Variable definitions
TYF = [False, True]
bBlack = (0,0,22) #blueblack
lred = (255, 160, 143) #light red
lgreen = (192,255,211) #light green
blue_grey = (128, 128,150)
width, height = 700, 600
til_size = 20
grid_h = height // til_size
grid_w = width  // til_size
print(grid_h)

FPS = 60

screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

class cells:
    """ Manage cells. Type is a boolean value
    that determines they way each cell grows.
    """
    def __init__(self, type):
        self.type = type
    def ad_grid(positions):
        'Adds cells to the simulation vertically, horizontally and diagonally upwards'
        new_pos = set(positions)  
        for pos in positions:
            x,y = pos
            # adds cell up
            if y - 1 >= 0 and (x, y - 1) not in positions:
                new_pos.add((x, y - 1))
            #Adds new cell down
            if y + 1 < grid_h and (x, y + 1) not in positions:
                print(y)
                new_pos.add((x, y + 1))
            for dx in [-1, 1]:
                for dy in [0, - 1]:
                    # grows cell horizontally, and diagonally up
                    ran = random.randint(0,1)
                    check = TYF[ran]
                    nPos = (x +dx, y+dy)
                    if check:
                        if nPos not in positions:
                            new_pos.add(nPos)
                                
        return new_pos
    #Variables
    position = set()
    
def draw_grid(positions):
    "This function draws the grid"
    
    for post in positions:
        col, row = post
        topLeft = (col * til_size, row * til_size)
        pygame.draw.rect(screen, lred, (*topLeft, til_size, til_size))

    for row in range(grid_h): 
        pygame.draw.line(screen, bBlack, (width, row * til_size), (0, row * til_size))

    for col in range(grid_w):
        pygame.draw.line(screen, bBlack, (col * til_size, 0), (col * til_size, height))

def run():
    "This function run the simulation"
    #Vars
    count = 0
    running = True
    playing = False
    up_frecuency = 80
    #class objects
    trunk = cells(0)
    leaves = cells(1)
    #position are the cells that are displayed
    
    while running:
        clock.tick(FPS)
        #Each game "year" happens when the counter gets to the up_frecuency
        if playing == True:
            
            count += 1
        
        if count >= up_frecuency:
            count = 0
            trunk.position =  cells.ad_grid(trunk.position)
            print(trunk.position)
        
        pygame.display.set_caption('Playing' if playing else "paused")
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                # Happens when the player quits the game
                running = False
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                #Takes the position and make the cube
                x, y = pygame.mouse.get_pos()
                col = x // til_size
                row = y // til_size
                pos = (col, row)

                if pos in trunk.position:
                    trunk.position.remove(pos)
                else:
                    trunk.position.add(pos)
            if event.type == pygame.KEYDOWN: 
                # when pressing space it pauses or plays the simulation.
                if event.key == pygame.K_SPACE:
                    playing = not playing
               
        screen.fill(blue_grey)
        draw_grid(trunk.position)
        pygame.display.update()
    pygame.quit()
run()