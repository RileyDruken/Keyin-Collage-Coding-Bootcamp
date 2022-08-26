import sys
import pygame

pygame.init()
clock = pygame.time.Clock()
screen_width = 888
screen_height = 688
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Hello World")

rectangle = pygame.Rect(0, 0, 100, 100)
rectangle2 = pygame.Rect(888 - 100, 0, 100, 100)
rectangle3 = pygame.Rect(0, 590, 100, 100)
rectangle4 = pygame.Rect(888 - 100, 688 - 200 + 100, 100, 100)



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill("CornFlowerBlue")

#shapes
    pygame.draw.rect(screen,"orange",rectangle)
    pygame.draw.rect(screen, "orange", rectangle2)
    pygame.draw.rect(screen, "orange", rectangle3)
    pygame.draw.rect(screen, "orange", rectangle4)

    pygame.display.flip()
    clock.tick(60)