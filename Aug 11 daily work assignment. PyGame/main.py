import pygame, sys, random
from pygame.locals import *

def ball_animation():
    global  ball_speed_x
    global ball_speed_y

    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.top <= 0 or ball.bottom >= scrH:
        ball_speed_y *= -1
    if ball.left <= 0:
        global score
        score += 1
        ball_Restart()
    if ball.right >= scrW:
        global score2
        score2 += 1
        ball_Restart()
    if ball.colliderect(player) or ball.colliderect(opponent):
        ball_speed_x *= -1
def player_animation():
    player.y += player_speed
    if player.top <= 0:
        player.top = 0
    if player.bottom >= scrH:
        player.bottom = scrH
def opponent_animation():
    if opponent.top < ball.y:
        opponent.top += opponent_speed
    if opponent.bottom > ball.y:
        opponent.bottom -= opponent_speed
    if opponent.top <= 0:
        opponent.top = 0
    if opponent.bottom >= scrH:
        opponent.bottom = scrH
def ball_Restart():
    global  ball_speed_y,ball_speed_x
    ball.center = (scrW/2, scrH/2)
    ball_speed_y *= random.choice((1,-1))
    ball_speed_x *= random.choice((1,-1))



pygame.init()
clock = pygame.time.Clock()




# Initializing surface
scrW = 1280
scrH = 750
screen = pygame.display.set_mode((scrW, scrH))






pygame.display.set_caption("Pong Game")

ball = pygame.Rect(scrW/2 - 15,scrH/2 - 15,30,30)
player = pygame.Rect(scrW - 20, scrH/2 - 70, 10, 140)
opponent = pygame.Rect(10, scrH/2 - 70, 10, 140)

bg_color = pygame.Color('gray12')
light_grey = (200,200,200)




score = 0
score2 = 0









ball_speed_x = 7 * random.choice((1,-1))
ball_speed_y = 7 * random.choice((1,-1))
player_speed = 0
opponent_speed = 7
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player_speed += 7
            if event.key == pygame.K_UP:
                player_speed -= 7
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                player_speed -= 7
            if event.key == pygame.K_UP:
                player_speed += 7
    ball_animation()
    player_animation()
    opponent_animation()



    # Visuals
    screen.fill(bg_color)
    pygame.draw.rect(screen, light_grey, player)
    pygame.draw.rect(screen, light_grey, opponent)
    pygame.draw.ellipse(screen, light_grey , ball)
    pygame.draw.aaline(screen, light_grey, (scrW/2,0), (scrW/2,scrH))

    font = pygame.font.Font('freesansbold.ttf', 32)
    text = font.render(f"{score2}:{score}", True, "black", "white")
    textRect = text.get_rect()
    textRect.center = (scrW // 2, scrH // 2)
    screen.blit(text, textRect)
    pygame.display.flip()
    clock.tick(60)