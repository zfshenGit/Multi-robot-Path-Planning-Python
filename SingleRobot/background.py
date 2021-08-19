#机器人运动环境绘制代码

import pygame

#set up the window
ENVIROMENT = pygame.display.set_mode((800,700))#返回的 pygame.Surface 对象，存储在名为 ENVIROMENT 的变量中
pygame.display.set_caption("robots")#设置窗口名

#set up the colors
BLACK = ( 0, 0, 0)
WHITE = (255,255,255)
BLUE = ( 0, 0,255)
GREEN = ( 0,255, 0)
RED = (255, 0, 0)
YELLOW = (227,255, 0)

def back():
    #draw on the surface object
    ENVIROMENT.fill(WHITE) #画图背景填充为白色
    
    #横线
    pygame.draw.line(ENVIROMENT, BLACK, (0, 0), (400, 0), 4)#左上角为（0,0）
    pygame.draw.line(ENVIROMENT, BLACK, (0, 50), (400, 50), 4)
    pygame.draw.line(ENVIROMENT, BLACK, (0, 100), (400, 100), 4)
    pygame.draw.line(ENVIROMENT, BLACK, (0, 150), (400, 150), 4)
    pygame.draw.line(ENVIROMENT, BLACK, (0, 200), (400, 200), 4)
    pygame.draw.line(ENVIROMENT, BLACK, (0, 250), (400, 250), 4)
    pygame.draw.line(ENVIROMENT, BLACK, (0, 300), (400, 300), 4)
    
    #竖线
    pygame.draw.line(ENVIROMENT, BLACK, (0, 0), (0, 300), 4)
    pygame.draw.line(ENVIROMENT, BLACK, (50, 0), (50, 300), 4)
    pygame.draw.line(ENVIROMENT, BLACK, (100, 0), (100, 300), 4)
    pygame.draw.line(ENVIROMENT, BLACK, (150, 0), (150, 300), 4)
    pygame.draw.line(ENVIROMENT, BLACK, (200, 0), (200, 300), 4)
    pygame.draw.line(ENVIROMENT, BLACK, (250, 0), (250, 300), 4)
    pygame.draw.line(ENVIROMENT, BLACK, (300, 0), (300, 300), 4)
    pygame.draw.line(ENVIROMENT, BLACK, (350, 0), (350, 300), 4)
    pygame.draw.line(ENVIROMENT, BLACK, (400, 0), (400, 300), 4)
    
    
    #障碍区域
    pygame.draw.polygon(ENVIROMENT, BLACK, ((200, 50), (200, 200),(250,200),(250,50)))
    
    # robot1 起点
    pygame.draw.line(ENVIROMENT, GREEN, (100, 100), (150, 100),5)
    pygame.draw.line(ENVIROMENT, GREEN, (100, 100), (100, 150), 5)
    pygame.draw.line(ENVIROMENT, GREEN, (100, 150), (150, 150), 5)
    pygame.draw.line(ENVIROMENT, GREEN, (150, 150), (150, 100), 5)
    # robot1 终点
    pygame.draw.line(ENVIROMENT, GREEN, (300, 100), (350, 100), 5)
    pygame.draw.line(ENVIROMENT, GREEN, (300, 100), (300, 150), 5)
    pygame.draw.line(ENVIROMENT, GREEN, (300, 150), (350, 150), 5)
    pygame.draw.line(ENVIROMENT, GREEN, (350, 150), (350, 100), 5)
