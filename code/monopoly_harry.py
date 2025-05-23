import pygame
import os
from os.path import join
import random 
from math import ceil

TAX_SQUARE_INCOME = 3
TAX_SQUARE_LUXURY = 15
FREE_VOTES_SQUARE_1 = 6
FREE_VOTES_SQUARE_2 = 23

pygame.display.set_caption("Politician Monopoly")

class Space(pygame.sprite.Sprite):
    def __init__(self, groups, num, image, location, position, cost, text_pos, party, party_pos, name, colour):
        super().__init__(groups)
        self.image = image
        self.number = num
        self.name = name
        self.rect = location
        self.postion = position
        self.colour = colour
        self.cost = cost
        self.space = 0
        self.text_pos = text_pos
        self.displayed = False
        self.bought = True
        self.party = party
        self.party_pos = party_pos
        self.font = pixel_font.render(self.name, True, self.colour)
        self.party_font = pixel_font.render('—', True, self.party)
        self.bold_font = bold_font.render('-', True, self.party)
        self.font_270 = pygame.transform.rotate(self.bold_font, 270)
        self.font_90 = pygame.transform.rotate(self.bold_font, 90)
        self.parties = ['Greens', 'Liberals', 'Labor']

    def get_position(self):
        return self.postion

    def set_buy(self, is_bought):
        self.bought = is_bought

    def get_buy(self):
        return self.bought

    def get_cost(self):
        return self.cost
    
    def display(self):
        self.displayed = True

    def update(self, dt):
        for i in range(len(self.parties)):
            if party == self.parties[i]:
                if self.party == party_colour: 
                    screen.blit(self.font, (1000, self.text_pos))     

        if self.number in [1, 2, 4, 5, 11, 12, 14]:
            screen.blit(self.bold_font, self.party_pos)
        elif self.number in [6, 9, 10]:
            screen.blit(self.font_270, self.party_pos)
        elif self.number in [16, 17, 19]:
            screen.blit(self.font_90, self.party_pos)
            
        if self.displayed:
            screen.blit(self.font, (1000, self.text_pos))     
                
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            if self.cost != 0:
                property_name = pixel_font.render(self.name, True, 0)
                cost_text = pixel_font.render("Property Cost: $"+ str(self.cost), True, 0)
                ROI_text = pixel_font.render("ROI:", True, 0)
                set_bonus_text = pixel_font.render("Set Bonus:", True, 0)
                pygame.draw.rect(screen, (170 , 170, 170), [20, 120, 250, 220])
                screen.blit(property_name, (30, 130))
                screen.blit(cost_text, (30, 150))
                screen.blit(ROI_text, (30, 170))
                screen.blit(set_bonus_text, (30, 190))

class AnimatedDice(pygame.sprite.Sprite):
    def __init__(self, frames, pos, groups, dice_timer, roll_index):
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
            self.kill()
            roll = random.randint(0, 5)
            self.dice_timer(roll) 
            print(str(Influence_points))
            print(str(Votes))
            
class Player(pygame.sprite.Sprite):
    def __init__(self, groups, hat):
        super().__init__(groups)
        self.image = pygame.image.load(join('images', hat)).convert_alpha()
        self.rect = self.image.get_frect(center = (355, 80))
        self.speed = 200
        self.target_position = self.rect.center
        self.traveling = False 
        self.space_location = 0
        self.top_right = False
        self.bottom_right = False
        self.bottom_left = False
        self.top_left = False


    def update(self, dt):  
        if self.traveling:
            target_x, target_y = self.target_position
            direction = pygame.math.Vector2(int(target_x) - int(self.rect.centerx), int(target_y) - int(self.rect.centery))
            if direction.length() > 1:
                direction.normalize_ip()
                if self.top_right:
                    direction.x = 1
                    direction.y = 0
                    self.rect.centerx += direction.x * self.speed * dt
                    if self.rect.centerx >= target_x:
                        self.top_right = False

                elif self.bottom_right:
                    direction.y = 1
                    direction.x = 0
                    self.rect.centery += direction.y * self.speed * dt
                    if self.rect.centery >= target_y:
                        self.bottom_right = False

                elif self.bottom_left:
                    direction.x = -1
                    direction.y = 0
                    self.rect.centerx += direction.x * self.speed * dt
                    if self.rect.centerx <= target_x:
                        self.bottom_left = False

                elif self.top_left:
                    direction.y = -1
                    direction.x = 0
                    self.rect.centery += direction.y * self.speed * dt
                    if self.rect.centery <= target_y:
                        self.top_left = False
                        redo = False
                else:
                    self.rect.centerx += direction.x * self.speed * dt
                    self.rect.centery += direction.y * self.speed * dt
            else:
                self.traveling = False  # Stop moving once we reach the target

    def move_to_square(self, space_position):
        if space_position[0] > 920:
            self.top_right = True
        elif space_position[1] > 635:
            self.bottom_right = True
        elif space_position[0] < 360 and 100 < space_position[1] < 635:
            self.bottom_left = True
        elif redo:
            self.top_left = True
        else:
            self.top_right = False
            self.bottom_right = False
            self.bottom_left = False
            self.top_left = False
        self.target_position = space_position
        self.traveling = True
        
def dice_timer(roll):
    global dice_rolling, dice, last_roll, rolls, redo, roll_button_idx
    dice_rolling = True
    dice = True
    last_roll = roll
    rolls += roll + 1
    if rolls > 23:
        redo = True 
        rolls -= 24
    player.move_to_square((all_spaces.sprites()[rolls]).get_position()) 
    print(rolls, (all_spaces.sprites()[rolls]).get_position())
    roll_button_idx = 0
    
def variable_setup():
    global player, spots

    spots = []
    spots_rects = []
    property_values = [50, 50, 0, 150, 200, 300, 0, 0, 400, 450, 550, 600, 0, 650, 0, 700, 700, 0, 750, 0]
    text_positions = [45, 70, 0, 95, 120, 145, 0, 0, 170, 195, 220, 245, 0, 270, 0, 295, 320, 0, 345, 0]
    colours = [(150, 75, 0), (150, 75, 0), (0, 0, 0), (100, 216, 255), (100, 216, 255), (255, 165, 0), (0, 0, 0), (0, 0, 0), (29, 233, 182), (29, 233, 182), (255, 0, 0), (255, 0, 0), (0, 0, 0), (255, 215, 0), (0, 0, 0), (160, 140, 255), (160, 140, 255), (0, 0, 0), (0, 0, 255), (0, 0, 0)]
    names = ["Brooky", "Manly Vale", "Income Tax", "Belrose", "Terrey Hills", "Dee Why", "Com Chest", "Chance", "Cromer", "Forest", "Alambie", "Beacon Hill", "Luxury Tax", "Sea Forth", "Com Chest", "Curly", "Freshy", "Chance", "Manly", "Free Perk"]
    party_values = ['springgreen4', 'springgreen4', 'white', 'springgreen4', 'firebrick1', 'firebrick1', 'white', 'white', 'springgreen4', 'deepskyblue3', 'springgreen4', 'firebrick1', 'white', 'springgreen4', 'white', 'deepskyblue3', 'deepskyblue3', 'white', 'firebrick1', 'white']
    party_positions = [(425, -70), (514, -70), (0, 0), (693, -70), (782, -70), (908, 145), (0, 0), (0, 0), (908, 412), (908, 502), (780, 498), (691, 498), (0, 0), (513, 498), (0, 0), (206, 498), (206, 410), (0, 0), (206, 232),(0, 0)]
    set = { 
            "brown": ["Brooky", "Manly Vale"],
            "blue": ["Belrose", "Terrey Hills"],
            "yellow": ["Dee Why"],
            "pink": ["Cromer", "Forest"],
            "red": ["Alambie", "Beacon Hill"],
            "gold": ["Sea Forth"],
            "purple": ["Curl Curl", "Freshy"],
            "turquoise": ["Manly"]
            }
    set_bonus = {
                "brown": 5,
                "blue": 15,
                "yellow": 30,
                "pink": 40,
                "red": 55, 
                "gold": 65,
                "purple": 70,
                "turquoise": 75
    }
    
    go_surf = pygame.image.load(join("images", "spaces", "go.png")).convert_alpha()
    go_rect = go_surf.get_rect(topleft=(288, 10))
    go = Space(all_spaces, 0, go_surf, go_rect, (350, 80), 0, 0, 'white', (0,0), None, 'black')

    for i in range(5):
        if i == 3 or 4:
            num = 89
        else:
            num = 90
        spots.append(
            pygame.image.load(join("images", "spaces", f"{i}.png")).convert_alpha()
        )
        spots_rects.append(spots[i].get_rect(topleft=((398 + num * i), 10)))
        Space(all_spaces, i+1, spots[i], spots_rects[i], (460 + 90 * i, 80), property_values[i], text_positions[i], party_values[i], party_positions[i], names[i], colours[i])

    free_perk_surf = pygame.image.load(join("images", "spaces", "free_perk.png")).convert_alpha()
    free_perk_rect = go_surf.get_rect(topleft=(861, 10))
    free_perk = Space(all_spaces, 0, free_perk_surf, free_perk_rect, (925, 80), 0, 0, 'white', (0,0), None, 'black')

    for i in range(5, 10):
        spots.append(
            pygame.image.load(join("images", "spaces", f"{i}.png")).convert_alpha()
        )
        spots[i] = pygame.transform.rotate(spots[i], 270)
        spots_rects.append(spots[i].get_rect(topleft=(861, 120 + 89 * (i - 5))))
        Space(all_spaces, i+1, spots[i], spots_rects[i], (925, 185 + 90 * (i - 5)), property_values[i], text_positions[i], party_values[i], party_positions[i], names[i], colours[i])


    go1_surf = pygame.image.load(join("images", "spaces", "go1.png")).convert_alpha()
    go1_rect = go_surf.get_rect(topleft=(861, 580))
    go1 = Space(all_spaces, 0, go1_surf, go1_rect, (925, 640), 0, 0, 'white', (0,0), None, 'black')

    for i in range(10, 15):
        spots.append(
            pygame.image.load(join("images", "spaces", f"{i}.png")).convert_alpha()
        )
        spots_rects.append(spots[i].get_rect(topleft=(752 - 89 * (i - 10), 580)))
        Space(all_spaces, i+1, spots[i], spots_rects[i], (815 - 90 * (i - 10), 640), property_values[i], text_positions[i], party_values[i], party_positions[i], names[i], colours[i])

    go3_surf = pygame.image.load(join("images", "spaces", "go1.png")).convert_alpha()
    go3_rect = go_surf.get_rect(topleft=(288, 580))
    go3 = Space(all_spaces, 0, go3_surf, go3_rect, (350, 640), 0, 0, 'white', (0,0), None, 'black')

    for i in range(15, 20):
        spots.append(
            pygame.image.load(join("images", "spaces", f"{i}.png")).convert_alpha()
        )
        spots[i] = pygame.transform.rotate(spots[i], 90)
        spots_rects.append(spots[i].get_rect(topleft=(288, 470 - 89 * (i - 15))))
        Space(all_spaces, i+1, spots[i], spots_rects[i], (355, 535 - 90 * (i - 15)), property_values[i], text_positions[i], party_values[i], party_positions[i], names[i], colours[i])

    player = Player(all_sprites, hat)

pygame.init()
pygame.font.init()

# Setup 
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720 
party = None
party_colour = None
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
running = True
clock = pygame.time.Clock()
middle = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2)
dice_rolling = True
dice = True
last_roll = 0
rolls = 0
redo = False
class_select = True
colour = "deepskyblue3"
property_price = 0
Influence_points = 1500
Votes = 0
current_time = pygame.time.get_ticks()
R0i = 0
chance_chest = ["Gain influence points","Gain votes","Add extra time to pass Go","Move backward","Lose influence points","Lose votes","Remove extra time to pass Go","Move forward"]
Dice = [1,2,3,4,5,6]
choice = ""
card = True

liberal_surf = pygame.image.load(join('images', 'liberal.png')).convert_alpha()
liberal_rect = liberal_surf.get_frect(center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))

labor_surf = pygame.image.load(join('images', 'labor.png')).convert_alpha()
labor_rect = labor_surf.get_frect(center = (WINDOW_WIDTH / 4, WINDOW_HEIGHT / 2))

greens_surf = pygame.image.load(join('images', 'greens.png')).convert_alpha()
greens_rect = greens_surf.get_frect(center = (WINDOW_WIDTH * 0.75, WINDOW_HEIGHT / 2))

bold_font = pygame.font.Font('Pixel.ttf', 150)
pixel_font = pygame.font.Font('Pixel.ttf')
bold_pixel_font = pygame.font.Font('Pixel.ttf', 25)
bold_pixel_font.set_bold(True)
bold_font.set_bold(True)


font = pygame.font.Font('font.otf', 60)
text = font.render("Please Choose a Party", False, 0)
properites_text = bold_pixel_font.render("Your Properties:", True, 0)
text_rect = text.get_frect(center = (WINDOW_WIDTH / 2, 100))

while class_select:
    for event in pygame.event.get():
        recent_keys = pygame.key.get_just_pressed()
        if event.type == pygame.QUIT:
            class_select = False
            running = False
        if labor_rect.collidepoint(pygame.mouse.get_pos()):
            labor_surf.set_alpha(200)
        else:
            labor_surf.set_alpha(255)

        if liberal_rect.collidepoint(pygame.mouse.get_pos()):
            liberal_surf.set_alpha(200)
        else:
            liberal_surf.set_alpha(255)

        if greens_rect.collidepoint(pygame.mouse.get_pos()):
            greens_surf.set_alpha(200)
        else:
            greens_surf.set_alpha(255)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if labor_rect.collidepoint(event.pos):
                hat = 'player_red.png'
                party = 'Labor'
                party_colour = 'firebrick1'
                class_select = False
            if liberal_rect.collidepoint(event.pos):
                hat = 'player_blue.png'
                party = 'Liberals'
                party_colour = 'deepskyblue3'
                class_select = False
            if greens_rect.collidepoint(event.pos):
                hat = 'player_green.png'
                party = 'Greens'
                party_colour = 'springgreen4'
                class_select = False

    screen.fill(colour)
    screen.blit(liberal_surf, liberal_rect)
    screen.blit(labor_surf, labor_rect)
    screen.blit(greens_surf, greens_rect)
    screen.blit(text, text_rect)


    pygame.display.update()



button_images = [pygame.image.load(f"images/button/roll_button{i}.png") for i in range(2)]
roll_button_idx = 0
buy_button_idx = 0

roll_button = pygame.Rect(80, WINDOW_HEIGHT - 130, 170, 80)
button_text = pixel_font.render("Press to Roll", True, 'black')
roll_button_img_rect = button_images[roll_button_idx].get_rect(topleft=roll_button.topleft)
button_text_rect = button_text.get_rect(center=roll_button_img_rect.center)

buy_button = pygame.Rect(80, WINDOW_HEIGHT - 240, 170, 80)
buy_text = pixel_font.render("Can't Buy", False, 'black')
buy_pos = (140, 515)

board_surf = pygame.Surface((703, 700))
board_surf.fill('darkseagreen2')
board_rect = board_surf.get_frect(center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))

dices = [pygame.image.load(join('images', 'dice', f'dice{i}.png')).convert_alpha() for i in range(1, 7)]
dice_rect = dices[1].get_frect(center = middle)

all_sprites = pygame.sprite.Group()
all_spaces = pygame.sprite.Group()

variable_setup()

influence_squares = {
    TAX_SQUARE_INCOME: lambda x: max(x - 100, 0),
    TAX_SQUARE_LUXURY: lambda x: max(x - 50, 0)
}

vote_squares = {
    FREE_VOTES_SQUARE_1: lambda x: x + 20,
    FREE_VOTES_SQUARE_2: lambda x: x + 20   
}

roll_frames = [pygame.image.load(join('images', 'dice', 'roll',  f'{i}.png')).convert_alpha() for i in range(0, 8)]

while running:
    dt = clock.tick(60) / 1000
    choice_text = pixel_font.render(choice, True, 'black')
    influence_text = pixel_font.render("Influence Points: " + str(Influence_points), True, 'black')
    votes_text = pixel_font.render("Votes: " + str(Votes), True, 'black')

    # Event loops
    for event in pygame.event.get():
        recent_keys = pygame.key.get_just_pressed()
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and dice_rolling and not player.traveling:
            if roll_button.collidepoint(event.pos):
                if dice_rolling and not player.traveling:
                    dice = False
                    AnimatedDice(roll_frames, middle, all_sprites, dice_timer, last_roll)
                    dice_rolling = False
                    roll_button_idx = 1
                    if rolls == 8 or rolls == 9 or rolls == 17 or rolls == 21:
                        print("Card")
                        choice = random.choice(chance_chest)
                        print(choice)
                        if choice == "Gain influence points":
                            Influence_points = Influence_points + 100
                            print(str(Influence_points))
                        if choice == "Gain votes":
                            Votes = Votes + 10
                        if choice == "Add extra time to pass Go":
                            pass
                        if choice == "Move backward":
                            rolls -= random.choice(Dice)
                            player.move_to_square((all_spaces.sprites()[rolls]).get_position()) 
                        if choice == "Lose influence points":
                            Influence_points = Influence_points - 100
                            print(str(Influence_points))
                        if choice == "Lose votes":
                            Votes = Votes - 10
                        if choice == "Remove extra time to pass Go":
                            pass
                        if choice == "Move forward":
                            rolls += random.choice(Dice)
                            if rolls > 23:
                                rolls -= 24
                            player.move_to_square((all_spaces.sprites()[rolls]).get_position()) 
                        choice_text = pixel_font.render(choice, True, 'black')
                    else:
                        choice = ""
                        choice_text = pixel_font.render(choice, True, 'black')
            if buy_button.collidepoint(event.pos):
                current_time = pygame.time.get_ticks()
                buy_button_idx = 1
                if property_price != 0:
                    if (all_spaces.sprites()[rolls]).get_buy():
                        Influence_points -= property_price
                        (all_spaces.sprites()[rolls]).display()
                        (all_spaces.sprites()[rolls]).set_buy(False)

            if rolls in influence_squares:
                Influence_points = influence_squares[rolls](Influence_points)

            if rolls in vote_squares:
                Votes = vote_squares[rolls](Votes)

        
            


    if pygame.time.get_ticks() > current_time + 200:
        buy_button_idx = 0 

    if all_spaces.sprites()[rolls].get_cost() != 0:
        property_price = all_spaces.sprites()[rolls].get_cost()
        buy_text = pixel_font.render("Buy Property: $" + str(property_price), True, "black")
        buy_pos = (105, 515)
    else:
        property_price = 0
        buy_text = pixel_font.render("Can't Buy", True, 'black')
        buy_pos = (140, 515)

    # Update sprites
    all_sprites.update(dt)

    # Drawing
    screen.fill('plum1')
    screen.blit(button_images[roll_button_idx], roll_button)
    screen.blit(button_text, button_text_rect)
    screen.blit(button_images[buy_button_idx], buy_button)
    screen.blit(buy_text, buy_pos)
    screen.blit(properites_text, (1000, 15))

    if dice:
        screen.blit(dices[last_roll], dice_rect)

    screen.blit(influence_text, (20, 20))
    screen.blit(votes_text, (20, 40))
    
    all_spaces.draw(screen) 
    all_sprites.draw(screen)
    all_spaces.update(dt)
    if rolls == 8 or rolls == 9 or rolls == 17 or rolls == 21:
    #if rolls > 0:
        screen.blit(choice_text, (550, 475))

    pygame.display.update()
pygame.font.quit()
pygame.quit()
