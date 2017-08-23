import pygame
import sys

size = width , height = 600, 400
# maxsize = (1920, 1080)
bg = (255, 255, 255)
speed = [1, 1]

#创建时钟对象
clock = pygame.time.Clock()

#初始化游戏框架
pygame.init()
screen = pygame.display.set_mode(size, pygame.RESIZABLE)  # pygame.RESIZABLE

#设置窗口游戏名
pygame.display.set_caption("一个游戏")

#加载游戏素材(图片)
tg = tg1 = pygame.image.load("teigou.jpg")
tg2 = pygame.transform.flip(tg, True, False)



fullscreen = False

#获取图片宽高
position = tg.get_rect()

while True:
    #获取游戏事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("用户要退出游戏")
            sys.exit()

        if event.type == pygame.VIDEORESIZE:
            size = event.size
            width, height = size
            screen = pygame.display.set_mode(size, pygame.RESIZABLE)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                tg = tg2
                speed = [-1, 0]
            if event.key == pygame.K_RIGHT:
                tg = tg1
                speed = [1, 0]
            if event.key == pygame.K_UP:
                speed = [0, -1]
            if event.key == pygame.K_DOWN:
                speed = [0, 1]


            if event.key == pygame.K_F7:
                fullscreen = not fullscreen
                if fullscreen:
                    screen = pygame.display.set_mode(size)
                else:
                    #获取电脑全部窗口大小，pygame.display.list_modes()[0] 是最大的一个窗口
                    maxsize = pygame.display.list_modes()[0]
                    # print(pygame.display.list_modes())
                    screen = pygame.display.set_mode(maxsize, pygame.FULLSCREEN)




        

    position = position.move(speed)

    #位置判断
    if position.left <= 0 :
        #旋转后的图是个新的对象, 需要重新渲染
        tg = tg1 
        speed[0] = -speed[0]

    if  position.right >= width:
        tg = tg2 
        speed[0] = -speed[0]

    if position.top <= 0 or position.bottom >= height:
        speed[1] = -speed[1]

    #将背景渲染成设置的颜色
    screen.fill(bg)

    #将图片渲染到屏幕中(参数<需要渲染上的对象,渲染的起始位置>)
    screen.blit(tg, position)
    pygame.display.flip()

    #设置循环等待时间(本质上是让程序暂停)
    # pygame.time.delay(10)

    #运用时钟对象控制游戏速度(参数是1秒内切换的帧数<一般控制在60-400之间>)
    clock.tick(100)









































