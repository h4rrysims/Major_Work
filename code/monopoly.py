import pygame
import os
from os.path import join
import random 

class Space(pygame.sprite.Sprite):
    def __init__(self, groups, image, location, position):
        super().__init__(groups)
        self.image = image
        self.rect = location
        self.postion = position

    def get_position(self):
        return self.postion
        

class AnimatedDice(pygame.sprite.Sprite):
    def __init__(self, frames, pos, groups, dice_timer):
        super().__init__(groups)
        self.frames = frames
        self.frame_index = 0
        self.image = self.frames[self.frame_index]
        self.rect = self.image.get_frect(center=pos)
        self.dice_timer = dice_timer
        self.time_passed = 0

    def update(self, dt):
        self.frame_index += 9 * dt 
        self.time_passed += dt
        if self.frame_index < len(self.frames):
            if self.time_passed > 0.1:
                self.image = self.frames[random.randint(0, len(self.frames) - 1)]
                self.time_passed -= 0.1

            self.rect.centery += -100 * dt
            if self.frame_index > 5:
                self.rect.centery += 200 * dt
        else:
            self.kill()   # Remove the dice after animation
            roll = random.randint(0, 5)
            self.dice_timer(roll)  # Notify that animation is complete
            
class Player(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        self.image = pygame.image.load(join('images','player.png')).convert_alpha()
        self.rect = self.image.get_frect(center = (355, 80))
        self.speed = 50
        self.target_position = self.rect.center
        self.traveling = False 
        self.space_location = 0
        self.x_first = False
        self.y_first = False
        self.first = False


    def update(self, dt):  
        if self.traveling:
            target_x, target_y = self.target_position
            direction = pygame.math.Vector2(int(target_x) - int(self.rect.centerx), int(target_y) - int(self.rect.centery))
            if direction.length() > 1:
                direction.normalize_ip()
                if self.x_first:
                    direction.x = 1
                    direction.y = 0
                    self.rect.centerx += direction.x * self.speed * dt
                    if self.rect.centerx >= target_x:
                        self.x_first = False
                        direction.x = 1
                else:
                    self.rect.centerx += direction.x * self.speed * dt
                    self.rect.centery += direction.y * self.speed * dt
                if self.y_first:
                    direction.y = 1
                    direction.x = 0
                    self.rect.centery += direction.y * self.speed * dt
                    if self.rect.centery >= target_y:
                        self.y_first = False
                        direction.y = 1
                else:
                    self.rect.centerx += direction.x * self.speed * dt
                    self.rect.centery += direction.y * self.speed * dt
                if self.first:
                    print(direction)
                    direction.x = -1
                    direction.y = 0
                    self.rect.centerx += direction.x * self.speed * dt
                    if self.rect.centerx <= target_x:
                        self.first = False
                        direction.x = -1
                else:
                    self.rect.centerx += direction.x * self.speed * dt
                    self.rect.centery += direction.y * self.speed * dt
            else:
                self.traveling = False  # Stop moving once we reach the target

    def move_to_square(self, space_index, space_position):
        if space_position[0] > 920:
            self.x_first = True
            print('x')
        else:
            self.x_first = False
        if space_position[1] > 635:
            self.y_first = True
            print('y')
        else:
            self.y_first + False
        if space_position[0] < 360 and space_position[1] < 635:
            self.first = True
            self.y_first = False
            self.x_first = False
            print('boom')
        else:
            self.first = False
        self.target_position = space_position
        self.space_location += space_index
        self.traveling = True
        
def dice_timer(roll):
    global dice_rolling, dice, last_roll, rolls
    dice_rolling = True
    dice = True
    last_roll = roll
    rolls += roll + 1
    if rolls > 23:
        print(rolls)
        rolls -= 24
        print(rolls)
    print(rolls, (all_spaces.sprites()[rolls]).get_position())
    player.move_to_square(roll+1, (all_spaces.sprites()[rolls]).get_position()) 
    
def variable_setup():
    global player, spots

    spots = []
    spots_rects = []

    go_surf = pygame.image.load(join('images', 'spaces' ,'go.png')).convert_alpha()
    go_rect = go_surf.get_frect(topleft = (288, 10))
    go = Space(all_spaces, go_surf, go_rect, (350, 80))

    for i in range(5):
        if i == 3 or 4:
            num = 89
        else:
            num = 90
        spots.append(pygame.image.load(join('images', 'spaces', f'{i}.png')).convert_alpha())
        spots_rects.append(spots[i].get_frect(topleft = ((398 + num*i), 10)))
        Space(all_spaces, spots[i], spots_rects[i], (460+90*i, 80))

    go1_surf = pygame.image.load(join('images', 'spaces' ,'go1.png')).convert_alpha()
    go1_rect = go_surf.get_frect(topleft = (861, 10))
    go1 = Space(all_spaces, go1_surf, go1_rect, (925, 80))

    for i in range(5, 10):
        spots.append(pygame.image.load(join('images', 'spaces', f'{i}.png')).convert_alpha())
        spots[i] = pygame.transform.rotate(spots[i], 270)
        spots_rects.append(spots[i].get_frect(topleft = (861, 120 + 89*(i-5))))
        Space(all_spaces, spots[i], spots_rects[i], (925, 185 + 90*(i-5)))

    go2_surf = pygame.image.load(join('images', 'spaces' ,'go1.png')).convert_alpha()
    go2_rect = go_surf.get_frect(topleft = (861, 580))
    go2 = Space(all_spaces, go2_surf, go2_rect, (925, 640))

    for i in range (10, 15):
        spots.append(pygame.image.load(join('images', 'spaces', f'{i}.png')).convert_alpha())
        spots_rects.append(spots[i].get_frect(topleft = (752 - 89*(i-10), 580)))
        Space(all_spaces, spots[i], spots_rects[i], (815 - 90*(i-10), 640))

    go3_surf = pygame.image.load(join('images', 'spaces' ,'go1.png')).convert_alpha()
    go3_rect = go_surf.get_frect(topleft = (288, 580))
    go3 = Space(all_spaces, go3_surf, go3_rect, (350, 640))

    for i in range (15, 20):
        spots.append(pygame.image.load(join('images', 'spaces', f'{i}.png')).convert_alpha())
        spots[i] = pygame.transform.rotate(spots[i], 90)
        spots_rects.append(spots[i].get_frect(topleft = (288, 470 - 89*(i-15))))
        Space(all_spaces, spots[i], spots_rects[i], (355, 535- 90*(i-15)))


    player = Player(all_sprites)

os.environ['SDL_AUDIODRIVER'] = 'dummy'
pygame.init()

# Setup 
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720 
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
running = True
clock = pygame.time.Clock()
middle = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2)
dice_rolling = True
dice = True
last_roll = 0
rolls = 0

board_surf = pygame.Surface((703, 700))
board_surf.fill('darkseagreen2')
board_rect = board_surf.get_frect(center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))

dice_surf = pygame.image.load(join('images', 'dice' ,'dice1.png')).convert_alpha()
dice_rect = dice_surf.get_frect(center = middle)

all_sprites = pygame.sprite.Group()
all_spaces = pygame.sprite.Group()

variable_setup()

roll_frames = [pygame.image.load(join('images', 'dice', f'dice{i}.png')).convert_alpha() for i in range(1, 7)]

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

    # Draw the board and spaces
    screen.blit(board_surf, board_rect)

    if dice:
        screen.blit(roll_frames[last_roll], dice_rect)


    all_spaces.draw(screen)
    all_sprites.draw(screen)

    pygame.display.update()

pygame.quit()