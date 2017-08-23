import pygame
from random import *

class SamllEnemy(pygame.sprite.Sprite):
    hp = 1

    def __init__(self, bg_size):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load("gameArts/gameArts/enemy1_fly_1.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.width, self.height = bg_size[0], bg_size[1]
        self.speed = 2
        self.active = True
        self.hp = SamllEnemy.hp
        self.score = 1

        self.destroy_images = []
        self.destroy_images.extend([
            pygame.image.load("gameArts/gameArts/enemy1_blowup_1.png").convert_alpha(),
            pygame.image.load("gameArts/gameArts/enemy1_blowup_2.png").convert_alpha(),
            pygame.image.load("gameArts/gameArts/enemy1_blowup_3.png").convert_alpha(),
            pygame.image.load("gameArts/gameArts/enemy1_blowup_4.png").convert_alpha()
        ])

        #通过图片对象制作面具
        self.mask = pygame.mask.from_surface(self.image)
        
        self.rect.left, self.rect.top = randint(0, self.width - self.rect.width), randint(-5*self.height, 0)


    def move(self):
        if self.rect.top < self.height:
            self.rect.top += self.speed
        else:
            self.reset()
        

    def reset(self):
        self.active = True
        self.hp = SamllEnemy.hp
        self.rect.left, self.rect.top = randint(0, self.width - self.rect.width), randint(-5*self.height, 0)
        

class MidEnemy(pygame.sprite.Sprite):
    hp = 8

    def __init__(self, bg_size):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load("gameArts/gameArts/enemy3_fly_1.png").convert_alpha()
        self.image_hit = pygame.image.load("gameArts/gameArts/enemy3_hit_1.png").convert_alpha()
        self.hit = False
        self.rect = self.image.get_rect()
        self.width, self.height = bg_size[0], bg_size[1]
        self.speed = 1
        self.active = True
        self.hp = MidEnemy.hp
        self.score = 5

        self.destroy_images = []
        self.destroy_images.extend([
            pygame.image.load("gameArts/gameArts/enemy3_blowup_1.png").convert_alpha(),
            pygame.image.load("gameArts/gameArts/enemy3_blowup_2.png").convert_alpha(),
            pygame.image.load("gameArts/gameArts/enemy3_blowup_3.png").convert_alpha(),
            pygame.image.load("gameArts/gameArts/enemy3_blowup_4.png").convert_alpha()
        ])

        self.mask = pygame.mask.from_surface(self.image)


        self.rect.left, self.rect.top = randint(0, self.width - self.rect.width), randint(-10*self.height, 0)


    def move(self):
        if self.rect.top < self.height:
            self.rect.top += self.speed
        else:
            self.reset()
        

    def reset(self):
        self.active = True
        self.hp = MidEnemy.hp
        self.rect.left, self.rect.top = randint(0, self.width - self.rect.width), randint(-10*self.height, 0)
          
class BigEnemy(pygame.sprite.Sprite):
    hp = 20

    def __init__(self, bg_size):
        pygame.sprite.Sprite.__init__(self)

        self.image1 = pygame.image.load("gameArts/gameArts/enemy2_fly_1.png").convert_alpha()
        self.image2 = pygame.image.load("gameArts/gameArts/enemy2_fly_2.png").convert_alpha()
        self.image_hit = pygame.image.load("gameArts/gameArts/enemy2_hit_1.png").convert_alpha()        
        self.hit = False
        self.rect = self.image1.get_rect()
        self.width, self.height = bg_size[0], bg_size[1]
        self.speed = 1
        self.active = True
        self.hp = BigEnemy.hp
        self.score = 10

        self.destroy_images = []
        self.destroy_images.extend([
            pygame.image.load("gameArts/gameArts/enemy2_blowup_1.png").convert_alpha(),
            pygame.image.load("gameArts/gameArts/enemy2_blowup_2.png").convert_alpha(),
            pygame.image.load("gameArts/gameArts/enemy2_blowup_3.png").convert_alpha(),
            pygame.image.load("gameArts/gameArts/enemy2_blowup_4.png").convert_alpha(),
            pygame.image.load("gameArts/gameArts/enemy2_blowup_5.png").convert_alpha(),
            pygame.image.load("gameArts/gameArts/enemy2_blowup_6.png").convert_alpha(),
            pygame.image.load("gameArts/gameArts/enemy2_blowup_7.png").convert_alpha()
        ])

        self.mask = pygame.mask.from_surface(self.image1)

        self.rect.left, self.rect.top = randint(0, self.width - self.rect.width), randint(-15*self.height, -5*self.height)


    def move(self):
        if self.rect.top < self.height:
            self.rect.top += self.speed
        else:
            self.reset()
        

    def reset(self):
        self.active = True
        self.hp = BigEnemy.hp
        self.rect.left, self.rect.top = randint(0, self.width - self.rect.width), randint(-15*self.height, -5*self.height)











