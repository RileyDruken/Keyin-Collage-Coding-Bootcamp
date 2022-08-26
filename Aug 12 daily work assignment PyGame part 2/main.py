import sys
import pygame

pygame.init()
clock = pygame.time.Clock()
screen_width = 888
screen_height = 688
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Hello World")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill("CornFlowerBlue")
    pygame.display.flip()
    clock.tick(60)