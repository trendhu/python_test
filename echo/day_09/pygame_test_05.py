import pygame
import sys


pygame.init()


size = width, height = 800, 500
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

target_size = 50 
target_x = 100
target_y = 100
speed = [2, 1]


score = 0
number  = 10


screen = pygame.display.set_mode(size)

pygame.display.set_caption("打靶")




clock = pygame.time.Clock()

while True:
    
    position = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("即将关闭程序")
            sys.exit()

        # if event.type == pygame.MOUSEBUTTONDOWN:

    screen.fill(WHITE)
    pygame.draw.circle(screen, BLACK, (target_x, target_y), target_size, 2)
    pygame.draw.circle(screen, RED, (target_x, target_y), int((target_size / 10) * 8), 2)
    pygame.draw.circle(screen, BLACK, (target_x, target_y), int((target_size / 10) * 6), 2)
    pygame.draw.circle(screen, RED, (target_x, target_y), int((target_size / 10) * 4), 2)
    pygame.draw.circle(screen, BLACK, (target_x, target_y), int((target_size / 10) * 2), 2)
    pygame.draw.circle(screen, RED, (target_x, target_y), 2, 2)
    
    target_x += speed[0]
    target_y += speed[1] 

    #位置判断
    if target_x <= target_size or target_x >= (width - target_size):
        speed[0] = -speed[0]
    if target_y <= target_size or target_y >= (height - target_size):
        speed[1] = -speed[1]
            




    pygame.display.flip()
    clock.tick(100)