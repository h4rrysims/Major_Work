import pygame
from os.path import join
import time
import random 

class Space(pygame.sprite.Sprite):
    def __init__(self, groups, image, location):
        super().__init__(groups)
        self.image = image
        self.rect = location

class AnimatedDice(pygame.sprite.Sprite):
    def __init__(self, frames, pos, groups, dice_timer):
        super().__init__(groups)
        self.frames = frames
        self.frame_index = 0
        self.image = self.frames[self.frame_index]
        self.rect = self.image.get_frect(center=pos)
        self.dice_timer = dice_timer

    def update(self, dt):
        self.frame_index += 9 * dt 
        if self.frame_index < len(self.frames):
            self.image = self.frames[int(self.frame_index)]
            self.rect.centery += -100 * dt
            if self.frame_index > 5:
                self.rect.centery += 200 * dt
        else:
            self.kill()   # Remove the dice after animation
            self.dice_timer()  # Notify that animation is complete


def dice_timer():
    global dice_rolling, dice
    dice_rolling = True
    dice = True
    
pygame.init()

# Setup 
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720 
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
running = True
clock = pygame.time.Clock()
middle = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2)
dice_rolling = True
dice = True

board_surf = pygame.Surface((710, 700))
board_surf.fill('darkseagreen2')
board_rect = board_surf.get_frect(center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))

dice_surf = pygame.image.load(join('images', 'dice1.png')).convert_alpha()
dice_rect = dice_surf.get_frect(center = middle)


surf2 = pygame.Surface((90, 130))
surf3 = pygame.Surface((90, 130))
surf4 = pygame.Surface((90, 130))
surf5 = pygame.Surface((90, 130))
surf6 = pygame.Surface((130, 130))

surf2.fill('orange')
surf3.fill('red')
surf4.fill('white')
surf5.fill('green')
surf6.fill('yellow')

rect2 = surf2.get_frect(topleft = (505, 10))
rect3 = surf3.get_frect(topleft = (595, 10))
rect4 = surf4.get_frect(topleft = (685, 10))
rect5 = surf5.get_frect(topleft = (775, 10))
rect6 = surf6.get_frect(topleft = (865, 10))

all_sprites = pygame.sprite.Group()
all_spaces = pygame.sprite.Group()

chance1_surf = pygame.image.load('images/chance1.png').convert_alpha()
chance1_rect = chance1_surf.get_frect(topleft = (396, 10))
chance1 = Space(all_spaces, chance1_surf, chance1_rect)

chance2_surf = pygame.image.load('images/chance2.png').convert_alpha()
chance2_rect = chance1_surf.get_frect(topright = (995, 120))
chance2 = Space(all_spaces, chance2_surf, chance2_rect)

go_surf = pygame.image.load('images/go.png').convert_alpha()
go_rect = go_surf.get_frect(topleft = (285, 10))
go = Space(all_spaces, go_surf, go_rect)    

roll_frames = [pygame.image.load(join('images', 'dice', f'{i}.png')).convert_alpha() for i in range(9)]




while running:
    dt = clock.tick(60) / 1000

    # Event loops
    for event in pygame.event.get():
        recent_keys = pygame.key.get_just_pressed()
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if dice_rolling: 
                    dice = False
                    AnimatedDice(roll_frames, middle, all_sprites, dice_timer)
                    dice_rolling = False

    # Update sprites
    all_sprites.update(dt)

    # Drawing
    screen.fill('#892bad')
    pygame.draw.rect(surf3, 'black' , pygame.FRect(0, 0, 90, 130),  2)
    pygame.draw.rect(surf4, 'black' , pygame.FRect(0, 0, 90, 130),  2)
    pygame.draw.rect(surf5, 'black' , pygame.FRect(0, 0, 90, 130),  2)
    pygame.draw.rect(surf6, 'black' , pygame.FRect(0, 0, 130, 130),  2)

    # Draw the board and spaces
    screen.blit(board_surf, board_rect)
    screen.blit(surf2, rect2)
    screen.blit(surf3, rect3)
    screen.blit(surf4, rect4)
    screen.blit(surf5, rect5)
    screen.blit(surf6, rect6)

    if dice:
        screen.blit(dice_surf, dice_rect)


    all_spaces.draw(screen)
    
    all_sprites.draw(screen)

    pygame.display.update()

pygame.quit()
