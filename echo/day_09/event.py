import pygame
import sys

size = width , height = 600 , 400
bg = (0 , 0 , 0);
speed = [2 , 1]

clock = pygame.time.Clock();

#初始化游戏框架
pygame.init();

#设置程序窗体大小，并返回一个程序对象
screen = pygame.display.set_mode(size);

#设置游戏名字，在程序窗口处显示
pygame.display.set_caption("第一个游戏");

#加载图片资源，即加载游戏资源
wuKong = pygame.image.load("kong.jpg");

# position = wuKong.get_rect();
position = 0;
print(position);

# f = open("eventLog.txt" , "w");
#创建一个字体对象
font = pygame.font.Font(None , 20);
# 获取字体对象的行高
lineheight = font.get_linesize();

while True:
    for event in pygame.event.get():
        
        eventStr = str(event);
        #创建一个字体对象
        fontSurface = font.render(eventStr , True , (0 , 255 , 0));
        # 加载游戏资源，将字体对象加载到程序中
        screen.blit(fontSurface , (0 , position));

        position += lineheight;

        if position > height:
            position = 0;
            #加载游戏资源，将色彩加载(之后将进行渲染)到程序中
            screen.fill(bg);

        if event.type == pygame.QUIT:
            print("用户要退出游戏。。。。");
            #调用系统默认的退出程序
            sys.exit();


    # screen.fill(bg);
    # screen.blit(wuKong , position);
    
    #将游戏资源重新渲染程序
    pygame.display.flip();
    # pygame.time.delay(500);
    #设置游戏切换帧频
    clock.tick(100);

