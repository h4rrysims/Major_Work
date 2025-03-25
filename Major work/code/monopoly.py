import pygame
from os.path import join
import random 

class Space(pygame.sprite.Sprite):
    def __init__(self, groups, image, location, position):
        super().__init__(groups)
        self.image = image
        self.rect = location
        self.postion = position

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
        self.rect = self.image.get_frect(center = (350, 80))
        self.speed = 200
        self.target_position = self.rect.center
        self.traveling = False 

    def update(self, dt):  
        if self.traveling:
            target_x, target_y = self.target_position
            direction = pygame.math.Vector2(int(target_x) - int(self.rect.centerx), int(target_y) - int(self.rect.centery))
            if direction.length() > 1:
                direction.normalize_ip()
                self.rect.centerx += direction.x * self.speed * dt
                self.rect.centery += direction.y * self.speed * dt
            else:
                self.rect.center = self.target_position
                self.traveling = False  # Stop moving once we reach the target

    def move_to_square(self, square_index):
        self.target_position = space_positions[square_index]
        self.traveling = True

def dice_timer(roll):
    global dice_rolling, dice, last_roll, travel
    dice_rolling = True
    dice = True
    last_roll = roll
    travel = True
    player.move_to_square(roll) 
    

def variable_setup():
    global player
    global space_positions
    space_positions = [
        (460, 80),
        (550, 80),
        (640, 80), 
        (725, 80),
        (815, 80),
        (925, 190) 
    ]

    go_surf = pygame.image.load(join('images', 'spaces' ,'go.png')).convert_alpha()
    go_rect = go_surf.get_frect(topleft = (288, 10))
    go = Space(all_spaces, go_surf, go_rect, (380, 80))

    chance1_surf = pygame.image.load(join('images', 'spaces' ,'chance1.png')).convert_alpha()
    chance1_rect = chance1_surf.get_frect(topleft = (399, 10))
    chance1 = Space(all_spaces, chance1_surf, chance1_rect, (460, 80))

    chance2_surf = pygame.image.load(join('images', 'spaces' ,'chance2.png')).convert_alpha()
    chance2_rect = chance1_surf.get_frect(topright = (995, 120))
    chance2 = Space(all_spaces, chance2_surf, chance2_rect, (920, 220))

    luxury_tax_surf = pygame.image.load(join('images', 'spaces' ,'luxury_tax.png')).convert_alpha()
    luxury_tax_rect = luxury_tax_surf.get_frect(topleft = (487, 10))
    luxury_tax1 = Space(all_spaces, luxury_tax_surf, luxury_tax_rect, (550, 80))

    com_chest_surf = pygame.image.load(join('images', 'spaces' ,'com_chest1.png')).convert_alpha()
    com_chest_rect = com_chest_surf.get_frect(topleft = (575, 10))
    com_chest1 = Space(all_spaces, com_chest_surf, com_chest_rect, (640, 80))

    income_tax_surf = pygame.image.load(join('images', 'spaces' ,'income_tax.png')).convert_alpha()
    income_tax_rect = income_tax_surf.get_frect(topleft = (663, 10))
    income_tax1 = Space(all_spaces, income_tax_surf, income_tax_rect, (725, 80))

    free_perk_surf = pygame.image.load(join('images', 'spaces' ,'free_perk.png')).convert_alpha()
    free_perk_rect = free_perk_surf.get_frect(topleft = (754, 10))
    income_tax1 = Space(all_spaces, free_perk_surf, free_perk_rect, (815, 80))

    go1_surf = pygame.image.load(join('images', 'spaces' ,'go.png')).convert_alpha()
    go1_rect = go1_surf.get_frect(topleft = (861, 10))
    go1 = Space(all_spaces, go1_surf, go1_rect, (930, 80))

    player = Player(all_sprites)
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

board_surf = pygame.Surface((703, 700))
board_surf.fill('darkseagreen2')
board_rect = board_surf.get_frect(center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))

dice_surf = pygame.image.load(join('images', 'dice' ,'dice1.png')).convert_alpha()
dice_rect = dice_surf.get_frect(center = middle)

all_sprites = pygame.sprite.Group()
all_spaces = pygame.sprite.Group()

variable_setup()



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