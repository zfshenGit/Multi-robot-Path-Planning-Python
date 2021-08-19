#机器人运动动态显示代码，以四机器人系统为例


#参考书：TP311.56/700
import pygame,sys
from pygame.locals import *
#导入自己编写的模块
import background
import sys
#import starttodestination
import ctl

pygame.init()#在调用任何其他的 pygame 函数之前，总是需要调用该函数

FPS = 1 #每秒 10 帧
fpsClock = pygame.time.Clock()
ENVIROMENT = pygame.display.set_mode((800,700))

#导入机器人图片
robotImg1 = pygame.image.load('robot1.png')
robotImg2 = pygame.image.load('robot2.png')
robotImg3 = pygame.image.load('robot3.png')
robotImg4 = pygame.image.load('robot4.png')
#动画显示
def cartoon(move1,move2,move3,move4):
    i1 = 0
    i2 = 0
    i3 = 0
    i4 = 0
    
    while True:
        background.back() #画背景网格
        #机器人运动轨迹
        if i1 < len(move1):
            robotx1 = move1[i1][1]*50
            roboty1 = move1[i1][0]*50
            i1 = i1+1
            ENVIROMENT.blit(robotImg1, (robotx1, roboty1))
            xf1 = robotx1
            yf1 = roboty1
        if i2 < len(move2):
            robotx2 = move2[i2][1]*50
            roboty2 = move2[i2][0]*50
            i2 = i2+1
            ENVIROMENT.blit(robotImg2, (robotx2, roboty2))
            xf2 = robotx2
            yf2 = roboty2
        if i3 < len(move3):
            robotx3 = move3[i3][1]*50
            roboty3 = move3[i3][0]*50
            i3 = i3+1
            ENVIROMENT.blit(robotImg3, (robotx3, roboty3))
            xf3 = robotx3
            yf3 = roboty3
        if i4 < len(move4):
            robotx4 = move4[i4][1]*50
            roboty4 = move4[i4][0]*50
            i4 = i4+1
            ENVIROMENT.blit(robotImg4, (robotx4, roboty4))
            xf4 = robotx4
            yf4 = roboty4
        else:
            #维持在最后一个状态
            ENVIROMENT.blit(robotImg1, (xf1, yf1))
            ENVIROMENT.blit(robotImg2, (xf2, yf2))
            ENVIROMENT.blit(robotImg3, (xf3, yf3))
            ENVIROMENT.blit(robotImg4, (xf4, yf4))
            
            #关闭窗口
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
        pygame.display.update()
        fpsClock.tick(FPS)
if __name__=='__main__':
    k1,k2,k3,k4 = ctl.total()
    print (k1)
    print(k2)
    print (k3)
    print(k4)
    cartoon(k1,k2,k3,k4)