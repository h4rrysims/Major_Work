import pygame
import random

# general setup
pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Major Work")
running = True
end = False
clock = pygame.time.Clock()


# making character
ball_surf = pygame.Surface((10, 10))
ball_surf.fill('white')
ball_rect = ball_surf.get_frect(center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))
ball_direction = pygame.math.Vector2(25, -10)
ball_speed = 10

mid_line_surf = pygame.Surface((10, 720))
mid_line_rect = mid_line_surf.get_frect(center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))
mid_line_surf.fill('white')

player1_surf = pygame.Surface((10, 115))
player1_surf.fill('white')
player1_rect = player1_surf.get_frect(center = (WINDOW_WIDTH -1180, WINDOW_HEIGHT / 2))
player1_direction = pygame.math.Vector2(0, 0)
player1_points = 0

player2_surf = pygame.Surface((10, 115))
player2_surf.fill('white')
player2_rect = player2_surf.get_frect(center = (WINDOW_WIDTH -100, WINDOW_HEIGHT / 2))
player2_direction = pygame.math.Vector2(0, 0)
player2_points = 0


player_font = pygame.font.Font('freesansbold.ttf', 45)
player_win_font = pygame.font.Font('freesansbold.ttf', 200)

player1_win_text = player_font.render('Player 1 wins!', True, 'white')
player1_win_rect = player1_win_text.get_frect(center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))

player2_win_text = player_font.render('Player 2 wins!', True, 'white')
player2_win_rect = player2_win_text.get_frect(center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))

player_speed = 10


while running:
    dt = clock.tick(60) / 1000
    player1_points_text = player_font.render(str(player1_points), True, 'white')
    player1_points_rect = player1_points_text.get_frect(center = (WINDOW_WIDTH / 4, WINDOW_HEIGHT - 680))

    player2_points_text = player_font.render(str(player2_points), True, 'white')
    player2_points_rect = player2_points_text.get_frect(center = (WINDOW_WIDTH - 320, WINDOW_HEIGHT - 680))

    # event loops
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # player movement
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_s:
                player1_direction.y = 0.5
            if event.key == pygame.K_w:
                player1_direction.y = -0.5
            if event.key == pygame.K_DOWN:
                player2_direction.y = 0.5
            if event.key == pygame.K_UP:
                player2_direction.y = -0.5

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_s:
                player1_direction.y = 0
            if event.key == pygame.K_w:
                player1_direction.y = 0
            if event.key == pygame.K_DOWN:
                player2_direction.y = 0
            if event.key == pygame.K_UP:
                player2_direction.y = 0


    # game end/win
    if player1_points >= 11 and player2_points < player1_points - 1:
        running = False
        end = True
    if player2_points >= 11 and player1_points < player2_points - 1:
        running = False
        end = True
        


    # player collisions
    if player1_rect.top < 0:
        player1_rect.top = 0.1
    if player1_rect.bottom > WINDOW_HEIGHT:
        player1_rect.bottom = 719.9
    if player2_rect.top < 0:
        player2_rect.top = 0.1
    if player2_rect.bottom > WINDOW_HEIGHT:
        player2_rect.bottom = 719.9

    # draw the game

    screen.fill('black')
    screen.blit(player1_points_text, player1_points_rect)
    screen.blit(player2_points_text, player2_points_rect)
    screen.blit(ball_surf, ball_rect)
    screen.blit(player1_surf, player1_rect)
    screen.blit(player2_surf, player2_rect)
    screen.blit(mid_line_surf, mid_line_rect)


    # ball movement
    if ball_rect.colliderect(player1_rect):
        ball_direction.x *= -1
        ball_speed += 2.5

    if ball_rect.colliderect(player2_rect):
        ball_direction.x *= -1
        ball_speed += 2.5
        
    if ball_rect.right > WINDOW_WIDTH:
        ball_speed = 10
        player1_points += 1
        ball_rect.center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2)

    if ball_rect.left < 0:
        ball_speed = 10
        player2_points += 1
        ball_direction = pygame.math.Vector2(-25, -10)
        ball_rect.center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2)

    if ball_rect.bottom > WINDOW_HEIGHT or ball_rect.top < 0:
        ball_direction.y *= -1

    ball_rect.center += ball_direction * ball_speed * dt
    player1_rect.center += player1_direction * player_speed
    player2_rect.center += player2_direction * player_speed
    pygame.display.update()

while end:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            end = False

    if player1_points >= 11 and player2_points < player1_points - 1:
        screen.fill('black')
        screen.blit(player1_win_text, player1_win_rect)
    elif player2_points >= 11 and player1_points < player2_points - 1:
        screen.fill('black')
        screen.blit(player2_win_text, player2_win_rect)
    
    pygame.display.update()

pygame.quit()