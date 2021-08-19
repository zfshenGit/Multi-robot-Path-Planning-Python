#机器人运动动态显示代码


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
#动画显示
def cartoon(move1):
    i1 = 0
    
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
        else:
            #维持在最后一个状态
            ENVIROMENT.blit(robotImg1, (xf1, yf1))
            
            #关闭窗口
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
        pygame.display.update()
        fpsClock.tick(FPS)
if __name__=='__main__':
    k1 = ctl.total()
    print (k1)
    cartoon(k1)