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
    pygame.draw.line(ENVIROMENT, BLACK, (0, 0), (800, 0), 4)#左上角为（0,0）
    pygame.draw.line(ENVIROMENT, BLACK, (0, 50), (800, 50), 4)
    pygame.draw.line(ENVIROMENT, BLACK, (0, 100), (800, 100), 4)
    pygame.draw.line(ENVIROMENT, BLACK, (0, 150), (800, 150), 4)
    pygame.draw.line(ENVIROMENT, BLACK, (0, 200), (800, 200), 4)
    pygame.draw.line(ENVIROMENT, BLACK, (0, 250), (800, 250), 4)
    pygame.draw.line(ENVIROMENT, BLACK, (0, 300), (800, 300), 4)
    pygame.draw.line(ENVIROMENT, BLACK, (0, 350), (800, 350), 4)
    pygame.draw.line(ENVIROMENT, BLACK, (0, 400), (800, 400), 4)
    pygame.draw.line(ENVIROMENT, BLACK, (0, 450), (800, 450), 4)
    pygame.draw.line(ENVIROMENT, BLACK, (0, 500), (800, 500), 4)
    pygame.draw.line(ENVIROMENT, BLACK, (0, 550), (800, 550), 4)
    pygame.draw.line(ENVIROMENT, BLACK, (0, 600), (800, 600), 4)
    
    #竖线
    pygame.draw.line(ENVIROMENT, BLACK, (0, 0), (0, 600), 4)
    pygame.draw.line(ENVIROMENT, BLACK, (50, 0), (50, 600), 4)
    pygame.draw.line(ENVIROMENT, BLACK, (100, 0), (100, 600), 4)
    pygame.draw.line(ENVIROMENT, BLACK, (150, 0), (150, 600), 4)
    pygame.draw.line(ENVIROMENT, BLACK, (200, 0), (200, 600), 4)
    pygame.draw.line(ENVIROMENT, BLACK, (250, 0), (250, 600), 4)
    pygame.draw.line(ENVIROMENT, BLACK, (300, 0), (300, 600), 4)
    pygame.draw.line(ENVIROMENT, BLACK, (350, 0), (350, 600), 4)
    pygame.draw.line(ENVIROMENT, BLACK, (400, 0), (400, 600), 4)
    pygame.draw.line(ENVIROMENT, BLACK, (450, 0), (450, 600), 4)
    pygame.draw.line(ENVIROMENT, BLACK, (500, 0), (500, 600), 4)
    pygame.draw.line(ENVIROMENT, BLACK, (550, 0), (550, 600), 4)
    pygame.draw.line(ENVIROMENT, BLACK, (600, 0), (600, 600), 4)
    pygame.draw.line(ENVIROMENT, BLACK, (650, 0), (650, 600), 4)
    pygame.draw.line(ENVIROMENT, BLACK, (700, 0), (700, 600), 4)
    pygame.draw.line(ENVIROMENT, BLACK, (750, 0), (750, 600), 4)
    pygame.draw.line(ENVIROMENT, BLACK, (800, 0), (800, 600), 4)
    
    #障碍区域
    pygame.draw.polygon(ENVIROMENT, BLACK, ((250, 250), (250, 300),(350,300),(350,250)))
    
    # robot1 起点
    pygame.draw.line(ENVIROMENT, GREEN, (150, 250), (200, 250),5)
    pygame.draw.line(ENVIROMENT, GREEN, (150, 250), (150, 300), 5)
    pygame.draw.line(ENVIROMENT, GREEN, (150, 300), (200, 300), 5)
    pygame.draw.line(ENVIROMENT, GREEN, (200, 300), (200, 250), 5)
    # robot1 终点
    pygame.draw.line(ENVIROMENT, GREEN, (550, 250), (600, 250), 5)
    pygame.draw.line(ENVIROMENT, GREEN, (550, 250), (550, 300), 5)
    pygame.draw.line(ENVIROMENT, GREEN, (550, 300), (600, 300), 5)
    pygame.draw.line(ENVIROMENT, GREEN, (600, 300), (600, 250), 5)
    # robot2 起点
    pygame.draw.line(ENVIROMENT, YELLOW, (50, 250), (100, 250), 5)
    pygame.draw.line(ENVIROMENT, YELLOW, (50, 250), (50, 300), 5)
    pygame.draw.line(ENVIROMENT, YELLOW, (50, 300), (100, 300), 5)
    pygame.draw.line(ENVIROMENT, YELLOW, (100, 300), (100, 250), 5)
    # robot2 终点
    pygame.draw.line(ENVIROMENT, YELLOW, (450, 250), (500, 250), 5)
    pygame.draw.line(ENVIROMENT, YELLOW, (450, 250), (450, 300), 5)
    pygame.draw.line(ENVIROMENT, YELLOW, (450, 300), (500, 300), 5)
    pygame.draw.line(ENVIROMENT, YELLOW, (500, 300), (500, 250), 5)
    # robot3 起点
    pygame.draw.line(ENVIROMENT, RED, (50, 350), (100, 350), 5)
    pygame.draw.line(ENVIROMENT, RED, (50, 350), (50, 400), 5)
    pygame.draw.line(ENVIROMENT, RED, (50, 400), (100, 400), 5)
    pygame.draw.line(ENVIROMENT, RED, (100, 400), (100, 350), 5)
    # robot3 终点
    pygame.draw.line(ENVIROMENT, RED, (450, 350), (500, 350), 5)
    pygame.draw.line(ENVIROMENT, RED, (450, 350), (450, 400), 5)
    pygame.draw.line(ENVIROMENT, RED, (450, 400), (500, 400), 5)
    pygame.draw.line(ENVIROMENT, RED, (500, 400), (500, 350), 5)
    # robot4 起点
    pygame.draw.line(ENVIROMENT, BLUE, (150, 350), (200, 350),5)
    pygame.draw.line(ENVIROMENT, BLUE, (150, 350), (150, 400), 5)
    pygame.draw.line(ENVIROMENT, BLUE, (150, 400), (200, 400), 5)
    pygame.draw.line(ENVIROMENT, BLUE, (200, 400), (200, 350), 5)
    # robot4 终点
    pygame.draw.line(ENVIROMENT, BLUE, (550, 350), (600, 350), 5)
    pygame.draw.line(ENVIROMENT, BLUE, (550, 350), (550, 400), 5)
    pygame.draw.line(ENVIROMENT, BLUE, (550, 400), (600, 400), 5)
    pygame.draw.line(ENVIROMENT, BLUE, (600, 400), (600, 350), 5)