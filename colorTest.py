import pygame 
pygame.init()

color_to_test = (200, 140, 132) # Change this variable with the color in rgb
window_size = (600, 400)
screen = pygame.display.set_mode(window_size)
def run():
     """" Creates a empty window with an specific color
          Use this file to test colors."""
     running = True
     while running:
          for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                # Happens when the player quits the game
                running = False
          screen.fill(color_to_test)
          pygame.display.update()
run()