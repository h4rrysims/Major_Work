import pygame
import random 

pygame.init()

# Setup 
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720 
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
running = True
clock = pygame.time.Clock()

board_surf = pygame.Surface((700, 700))
board_surf.fill('darkseagreen2')
board_rect = board_surf.get_frect(center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))

surf = pygame.Surface((60, 60))
surf.fill('darkorchid4')
rect = surf.get_frect(center = (205, 20))

while running:
    dt = clock.tick(60) / 1000

    # Event loops
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    screen.fill('black')
    screen.blit(board_surf, board_rect)
    screen.blit(surf, rect)
    

    pygame.display.update()
    
pygame.quit()