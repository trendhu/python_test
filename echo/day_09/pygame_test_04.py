import pygame
import sys

pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

size = width, height = 600, 400
position = (50, 50)
moving = False
screen = pygame.display.set_mode(size)

pygame.display.set_caption("图形")





clock = pygame.time.Clock()

while True:
    
    position = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()


        # if event.type == pygame.MOUSEBUTTONDOWN:
        #     if event.button == 1:
        #         moving = True

        # if event.type == pygame.MOUSEBUTTONUP:
        #     if event.button == 1:
        #         moving = False

        # if moving:
        #     position = pygame.mouse.get_pos()

    screen.fill(WHITE)

    pygame.draw.rect(screen, BLACK, (50, 50, 100, 50), 1)
    # pygame.draw.rect(screen, BLACK, (50, 150, 100, 50), 0)
    # pygame.draw.rect(screen, BLACK, (50, 250, 100, 50), 6)

    pygame.draw.circle(screen, RED, position, 20,2)
    
    pygame.draw.ellipse(screen, BLUE, (50, 50, 100, 50), 1)





    pygame.display.flip()
    clock.tick(100)
















