import random
import pygame
pygame.init()

#Variable definitions
TYF = [False, True]
bBlack = (0,0,22) #blueblack
lred = (245, 230, 230) #light red
blue_grey = (128, 128,150)
width, height = 700, 600
til_size = 20
grid_h = height // til_size
grid_w = width  // til_size

FPS = 60

screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

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


def ad_grid(positions, finish_state):
    'Adds cells to the simulation vertically, horizontally and diagonally upwards'
   
    new_pos = set(positions)  
    for pos in positions:
        x,y = pos
        dx = [-1, 1][random.randint(0, 1)]
        dy = random.randint(-1, 0)
        nPos = (x +dx, y+dy)
        if nPos not in positions:
                new_pos.add(nPos)
                            
    return new_pos, finish_state



def run():
    "This function run the simulation"
    
    count = 0
    running = True
    playing = False
    up_frecuency = 40
    finish_state = True
    #posts are the squares
    posts = set()
    while running:
        clock.tick(FPS)
        #Each game "year" happens when the counter gets to the up_frecuency
        if playing == True:
            
            count += 1
        
        if count >= up_frecuency:
            count = 0
            posts, finish_state = ad_grid(posts, finish_state)
            print(posts)
        
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

                if pos in posts:
                    posts.remove(pos)
                else:
                    posts.add(pos)
            if event.type == pygame.KEYDOWN: 
                # when pressing space it pauses or plays the simulation.
                if event.key == pygame.K_SPACE:
                    playing = not playing
            
        screen.fill(blue_grey)
        draw_grid(posts)
        pygame.display.update()
    pygame.quit()
run()