import pygame
import traceback
import sys

from pygame.locals import *

import myPlane
import enemy
import bullet


pygame.init()

#加载音频资源
pygame.mixer.init()

gameMusic= pygame.mixer.music.load("mp3/game_music.mp3")
pygame.mixer.music.set_volume(1)

# bullet = pygame.mixer.Sound("music/bullet.wav")
# # 设置音乐音量
# bullet.set_volume(.6)

# gameMusic= pygame.mixer.Sound("mp3/game_music.mp3")
# gameMusic.set_volume(0.3)
# gameMusic.play()

bullet = pygame.mixer.Sound("music/bullet.wav")
bullet.set_volume(.6)
enemy1_down = pygame.mixer.Sound("music/enemy1_down.wav")
enemy1_down.set_volume(.6)
enemy3_down = pygame.mixer.Sound("music/enemy2_down.wav")
enemy3_down.set_volume(.6)
enemy3_out = pygame.mixer.Sound("music/enemy2_out.wav")
enemy3_out.set_volume(.6)
enemy2_down = pygame.mixer.Sound("music/enemy3_down.wav")
enemy2_down.set_volume(.6)
game_over = pygame.mixer.Sound("music/game_over.wav")
game_over.set_volume(.6)


bg_size = width, height = 320, 568
screen = pygame.display.set_mode(bg_size)
pygame.display.set_caption("飞机大战")

#convert_alpha()转换像素资源
background = pygame.image.load("gameArts/gameArts/background_2.png").convert_alpha()


def add_small_enemies(group1, group2, num):
    for i in range(num):
        e = enemy.SamllEnemy(bg_size)
        group1.add(e)
        group2.add(e)
def add_mid_enemies(group1, group2, num):
    for i in range(num):
        e = enemy.MidEnemy(bg_size)
        group1.add(e)
        group2.add(e)
        
def add_big_enemies(group1, group2, num):
    for i in range(num):
        e = enemy.BigEnemy(bg_size)
        group1.add(e)
        group2.add(e)
    









def main():
    clock = pygame.time.Clock()

    #用于切换图片
    switchImage = True

    #用于延迟图片切换
    delay = 100


    #开始播放音频资源(-1表示循环播放)
    pygame.mixer.music.play(-1)
    runing = True

    #创建我方英雄飞机对象
    me = myPlane.MyPlane(bg_size)

    #创建敌人飞机容器
    enemies = pygame.sprite.Group()
    #生成敌方小型飞机
    small_enemies = pygame.sprite.Group()
    add_small_enemies(enemies, small_enemies, 15)
    #生成敌方中型飞机
    mid_enemies = pygame.sprite.Group()
    add_mid_enemies(enemies, mid_enemies, 4)
    #生成敌方大型飞机
    big_enemies = pygame.sprite.Group()
    add_big_enemies(enemies, big_enemies, 2)

    #中弹图片索引
    e1_destroy_index = 0
    e2_destroy_index = 0
    e3_destroy_index = 0
    me_destroy_index = 0

    while runing:
        
        #关闭程序
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("正在关闭程序")
                pygame.quit()
                sys.exit()

        #检测用户的键盘操作
        key_pressed = pygame.key.get_pressed()

        if key_pressed[K_w] or key_pressed[K_UP]:
            me.moveUp()
        if key_pressed[K_s] or key_pressed[K_DOWN]:
            me.moveDown()
        if key_pressed[K_a] or key_pressed[K_LEFT]:
            me.moveLeft()
        if key_pressed[K_d] or key_pressed[K_RIGHT]:
            me.moveRight()

        screen.blit(background, (0, 0))

        #绘制小飞机
        for each in small_enemies:
            if each.active:
                each.move()
                screen.blit(each.image, each.rect)
            else:
                if not (delay % 4):
                    screen.blit(each.destroy_images[e1_destroy_index], each.rect)
                    e1_destroy_index = (e1_destroy_index + 1) % 4
                    if e1_destroy_index == 0:
                        each.reset()

        #绘制中飞机
        for each in mid_enemies:
            if each.active:
                each.move()
                screen.blit(each.image, each.rect)
            else:
                if not (delay % 4):
                    screen.blit(each.destroy_images[e2_destroy_index], each.rect)
                    e2_destroy_index = (e2_destroy_index + 1) % 4
                    if e2_destroy_index == 0:
                        each.reset()

        #绘制大飞机
        for each in big_enemies:
            if each.active:
                each.move()
                if switchImage:
                    screen.blit(each.image1, each.rect)
                else:
                    screen.blit(each.image2, each.rect)
                
                if each.rect.bottom > -50:
                    enemy3_out.play()
            else:
                #毁灭
                if not (delay % 4):
                    if e3_destroy_index == 0:
                        enemy3_down.play()
                    screen.blit(each.destroy_images[e3_destroy_index], each.rect)
                    e3_destroy_index = (e3_destroy_index + 1) % 7
                    if e3_destroy_index == 0:
                        enemy3_down.stop()
                        each.reset()


        #将我方飞机绘制到屏幕中
        # screen.blit(me.image1, me.rect)

        #飞机碰撞检测
        # enemies_down = pygame.sprite.spritecollide(me, enemies, False)
        enemies_down = pygame.sprite.spritecollide(me, enemies, False, pygame.sprite.collide_mask)
        if enemies_down:
            me.active = False
            for e in enemies_down:
                e.active = False


        #绘制英雄机
        if me.active:
            if switchImage:
                screen.blit(me.image1, me.rect)
            else:
                screen.blit(me.image2, me.rect)
        else:
            if not (delay % 10):
                    screen.blit(me.destroy_images[me_destroy_index], me.rect)
                    me_destroy_index = (me_destroy_index + 1) % 4
                    if me_destroy_index == 0:
                        me.reset()

        if not (delay % 10):
            switchImage = not switchImage

        delay -= 1
        if not delay:
            delay = 100
        pygame.display.flip()

        clock.tick(100)



if __name__ == "__main__":
    main()





