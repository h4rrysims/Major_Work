import pygame
import random

# general setup
pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Major Work")
running = True
clock = pygame.time.Clock()
a = -1
b = 1

# plain surface

surf = pygame.Surface((100, 200))
surf.fill('orange')
x = 100

# importing an image
player_surf = pygame.image.load('images/player.png').convert_alpha()
player_rect = player_surf.get_frect(center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))
player_direction = pygame.math.Vector2(25, -10)
player_speed = 20

star_surface = pygame.image.load('images/star.png').convert_alpha()
star_postions = [(random.randint(0, 1280), random.randint(0, 720)) for i in range (20)]

meteor_surf = pygame.image.load('images/meteor.png').convert_alpha()
meteor_rect = meteor_surf.get_frect(center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))

laser_surf = pygame.image.load('images/laser.png').convert_alpha()
laser_rect = laser_surf.get_frect(bottomleft = (WINDOW_WIDTH - 1260, WINDOW_HEIGHT - 20))


while running:
    dt = clock.tick(60) / 1000

    # event loops
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if pygame.key.get_pressed()[pygame.K_ESCAPE]:
            running = False

    # draw the game

    screen.fill('magenta')
    for pos in star_postions:
        screen.blit(star_surface, pos)

    screen.blit(player_surf, player_rect)
    screen.blit(laser_surf, laser_rect)

    # player movement
    if player_rect.right > WINDOW_WIDTH or player_rect.left < 0:
        player_direction.x *= -1
    if player_rect.bottom > WINDOW_HEIGHT or player_rect.top < 0:
        player_direction.y *= -1
    player_rect.center += player_direction * player_speed * dt
    screen.blit(meteor_surf, meteor_rect)
    
    pygame.display.update()
    
    
pygame.quit()