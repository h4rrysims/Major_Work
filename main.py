import pygame
import time

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
color = True

logo = pygame.image.load("/Users/tomcarson/Desktop/coding/Major_Work_Pygame/download.jpeg")

x, y = 200, 200

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False



    # fill the screen with a color to wipe away anything from last frame
    if color:
        screen.fill("red")
        time.sleep(0.0002)
    else: 
        screen.fill("white")
    
    color = not color

    # RENDER YOUR GAME HERE
    screen.blit(logo, (x, y))
    x += 1
    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(120)  # limits FPS to 60
    
pygame.quit()

##x, y = 200, 200
#ovement_direction = ?

#if at_left_border:
 ##### move_in_same_direction()