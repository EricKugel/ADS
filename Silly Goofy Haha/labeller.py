import pygame

WIDTH = 360
HEIGHT = 480
FPS = 30

# Define Colors 
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

## initialize pygame and create window
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Fun Labeller Game!!")
clock = pygame.time.Clock()

i = 0
running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(BLACK)
    imp = pygame.image.load("C:\\Users\\DELL\\Downloads\\gfg.png").convert()
    
    # Using blit to copy content from one surface to other
    screen.blit(imp, (0, 0))

    pygame.display.update()       
pygame.quit()