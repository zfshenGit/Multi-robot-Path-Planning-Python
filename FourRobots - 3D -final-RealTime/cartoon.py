import pygame
from pygame.locals import *
from gameobjects.vector3 import Vector3
from gameobjects.matrix44 import Matrix44 as Matrix
from math import *
from random import randint

SCREEN_SIZE =  (1280, 720)
CUBE_SIZE = 36
CUBE_NUMBER = 7

keydown0 = False
keydown1 = False
key_x0,key_y0,key_z0 = None,None,None
key_x1,key_y1,key_z1 = None,None,None
obstacle_list = [(1, 3, 2),(1, 3, 3), (1, 3, 4)]

def calculate_viewing_distance(fov, screen_width):
    
    d = (screen_width/2.0) / tan(fov/2.0)
    return d

def back(m1,paths1,paths2,paths3,paths4):
    points = []
    start_end_points1 = []
    start_end_points2 = []
    start_end_points3 = []
    start_end_points4 = []
    obstacle_points = []
    path_points1 = []
    path_points2 = []
    path_points3 = []
    path_points4 = []
    m=m1
    path_list1 = paths1
    path_list2 = paths2
    path_list3 = paths3
    path_list4 = paths4
    
    # Create a list of points along the edge of a cube
    for x in range(0, CUBE_SIZE+1, 2):
        edge_x = x == 0 or x == CUBE_SIZE
        
        for y in range(0, CUBE_SIZE+1, 2):
            edge_y = y == 0 or y == CUBE_SIZE
            
            for z in range(0, CUBE_SIZE+1, 2):
                edge_z = z == 0 or z == CUBE_SIZE
                
                if sum((edge_x, edge_y, edge_z)) >= 2:
                                 
                    for i in range(1, CUBE_NUMBER + 1):
                        for j in range(1, CUBE_NUMBER + 1):
                            for k in range(1, CUBE_NUMBER + 1):
                                points = point(points,x,y,z,i-1,j-1,k-1)
                    
                    start_end_list1 = [(3, 1, 2),(3, 5, 2)]
                    start_end_list2 = [(1, 1, 2),(1, 5, 2)]
                    start_end_list3 = [(1, 1, 4),(1, 5, 4)]
                    start_end_list4 = [(3, 1, 4),(3, 5, 4)]
                    for i in range(0,len(start_end_list1)):
                        start_end_points1 = point(start_end_points1,x,y,z,start_end_list1[i][0],start_end_list1[i][1],start_end_list1[i][2])
                    for i in range(0,len(start_end_list2)):
                        start_end_points2 = point(start_end_points2,x,y,z,start_end_list2[i][0],start_end_list2[i][1],start_end_list2[i][2])
                    for i in range(0,len(start_end_list3)):
                        start_end_points3 = point(start_end_points3,x,y,z,start_end_list3[i][0],start_end_list3[i][1],start_end_list3[i][2])
                    for i in range(0,len(start_end_list4)):
                        start_end_points4 = point(start_end_points4,x,y,z,start_end_list4[i][0],start_end_list4[i][1],start_end_list4[i][2])
                    
                    for i in range(0,len(obstacle_list)):
                        obstacle_points = point(obstacle_points,x,y,z,obstacle_list[i][0],obstacle_list[i][1],obstacle_list[i][2])

                    path_points1 = point(path_points1,x,y,z,path_list1[m][0],path_list1[m][1],path_list1[m][2])
                    path_points2 = point(path_points2,x,y,z,path_list2[m][0],path_list2[m][1],path_list2[m][2])
                    path_points3 = point(path_points3,x,y,z,path_list3[m][0],path_list3[m][1],path_list3[m][2])
                    path_points4 = point(path_points4,x,y,z,path_list4[m][0],path_list4[m][1],path_list4[m][2]) 
                    
    return points,start_end_points1,start_end_points2,start_end_points3,start_end_points4,obstacle_points,path_points1,path_points2,path_points3,path_points4

def point(points,x,y,z,i,j,k):
    
    point_x = float(x) - CUBE_SIZE/2 + CUBE_SIZE*(i)
    point_y = float(y) - CUBE_SIZE/2 + CUBE_SIZE*(j)
    point_z = float(z) - CUBE_SIZE/2 + CUBE_SIZE*(k)
                                                   
    points.append(Vector3(point_x, point_y, point_z))
    return points

def transformed_point(transformed_points,rotation_matrix,camera_position,points):
    for point in points:
            
            p = rotation_matrix.transform_vec3(point) - camera_position            
            transformed_points.append(p)
            
    return transformed_points

def draw_point(transformed_points,center_x,center_y,viewing_distance,ball,ball_center_x,ball_center_y,screen):
    for x, y, z in transformed_points:            
            
            if z < 0:
                x = center_x + x * -viewing_distance / z
                y = center_y + -y * -viewing_distance / z
            
                screen.blit(ball, (x-ball_center_x, y-ball_center_y))
    
def run(paths1,paths2,paths3,paths4):

    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE, 0)
    FPS = 1 #每秒 10 帧
    
        
    font = pygame.font.SysFont("courier new", 16, True)
    
    ball_back = pygame.image.load("ball_back.png").convert_alpha()
    ball_start_end1 = pygame.image.load("ball_start_end1.png").convert_alpha()
    ball_start_end2 = pygame.image.load("ball_start_end2.png").convert_alpha()
    ball_start_end3 = pygame.image.load("ball_start_end3.png").convert_alpha()
    ball_start_end4 = pygame.image.load("ball_start_end4.png").convert_alpha()
    ball_obstacle = pygame.image.load("ball_obstacle.png").convert_alpha()
    ball_path1 = pygame.image.load("ball_path1.png").convert_alpha()
    ball_path2 = pygame.image.load("ball_path2.png").convert_alpha()
    ball_path3 = pygame.image.load("ball_path3.png").convert_alpha()
    ball_path4 = pygame.image.load("ball_path4.png").convert_alpha()
    
    fov = 115. # Field of view
    viewing_distance = calculate_viewing_distance(radians(fov), SCREEN_SIZE[0])
    
    def point_z(point):
        return point[2]
    
    center_x, center_y = SCREEN_SIZE
    center_x /= 2
    center_y /= 2
    
    ball_w, ball_h = ball_back.get_size()
    ball_center_x = ball_w / 2
    ball_center_y = ball_h / 2
    
    camera_position = Vector3(0.0, 0.0, 600.)
        
    rotation = Vector3()
    rotation_speed = Vector3(radians(20), radians(20), radians(20))
    
    clock = pygame.time.Clock()
    
    # Some colors for drawing
    red = (255, 0, 0)
    green = (0, 255, 0)
    blue = (0, 0, 255)    
    white = (255, 255, 255)
    black = (0, 0, 0)
    
    # Labels for the axes
    x_surface = font.render("X", True, black)
    y_surface = font.render("Y", True, black)
    z_surface = font.render("Z", True, black)
    
    x_rotation_number = 0
    y_rotation_number = 0
    z_rotation_number = 0
    num = 1
    
    #num使循环执行一次
    while num == 1:
        
        
        rotation_direction = Vector3()
        # rotation_direction.y = +2.0
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                quit()
                
            if event.type == KEYDOWN:
                #通过按键kq添加障碍物，障碍物坐标为(key_x0,key_y0,key_z0)
                if event.key == K_q:
                    global keydown0,key_x0,key_y0,key_z0
                    keydown0 = True
                    key_x0 = 2
                    key_y0 = 4
                    key_z0 = 2
                    obstacle_list.append((key_x0,key_y0,key_z0))
                    # rotation_direction.x = +1.0
                #通过按键ka添加障碍物，障碍物坐标为(key_x1,key_y1,key_z1)
                elif event.key == K_a:
                    global keydown1,key_x1,key_y1,key_z1
                    keydown1 = True
                    key_x1 = 2
                    key_y1 = 3
                    key_z1 = 3
                    obstacle_list.append((key_x1,key_y1,key_z1))
                    # rotation_direction.x = -1.0
                # elif event.key == K_w:
                    # rotation_direction.x = +1.0
        
        points,start_end_points1,start_end_points2,start_end_points3,start_end_points4,obstacle_points,path_points1,path_points2,path_points3,path_points4 = back(len(paths1)-1,paths1,paths2,paths3,paths4)
        
        screen.fill((255, 255, 255))       
        
        time_passed = clock.tick()
        time_passed_seconds = time_passed / 1000.                
        
        
        
        #Adjust the rotation direction depending on key presses
        pressed_keys = pygame.key.get_pressed()
        
        rotation_direction.y = -5
        
        # if x_rotation_number <= 0:
            # rotation_direction.x = +1
            # x_rotation_number += 1
        # elif pressed_keys[K_a]:
            # rotation_direction.x = -1.0
        
        
        # if y_rotation_number <= 0:
            # rotation_direction.y = -1
            # y_rotation_number += 1
        # elif pressed_keys[K_s]:
            # rotation_direction.y = -1.0
        
        # if pressed_keys[K_e]:
            # rotation_direction.z = +1.0
        # elif pressed_keys[K_d]:
            # rotation_direction.z = -1.0
        
        # Apply time based movement to rotation
        rotation += rotation_direction * rotation_speed * time_passed_seconds
        
        # Build the rotation matrix
        rotation_matrix = Matrix.x_rotation(rotation.x)
        rotation_matrix *= Matrix.y_rotation(rotation.y)
        rotation_matrix *= Matrix.z_rotation(rotation.z)        
        
        transformed_points = []
        transformed_start_end_points1 = []
        transformed_start_end_points2 = []
        transformed_start_end_points3 = []
        transformed_start_end_points4 = []
        transformed_obstacle_points = []
        transformed_path_points1 = []
        transformed_path_points2 = []
        transformed_path_points3 = []
        transformed_path_points4 = []

        # Transform all the points and adjust for camera position
        transformed_points = transformed_point(transformed_points,rotation_matrix,camera_position,points)
        transformed_points.sort(key=point_z)
        
        transformed_start_end_points1 = transformed_point(transformed_start_end_points1,rotation_matrix,camera_position,start_end_points1)
        transformed_start_end_points1.sort(key=point_z)
        
        transformed_start_end_points2 = transformed_point(transformed_start_end_points2,rotation_matrix,camera_position,start_end_points2)
        transformed_start_end_points2.sort(key=point_z)
        
        transformed_start_end_points3 = transformed_point(transformed_start_end_points3,rotation_matrix,camera_position,start_end_points3)
        transformed_start_end_points3.sort(key=point_z)
        
        transformed_start_end_points4 = transformed_point(transformed_start_end_points4,rotation_matrix,camera_position,start_end_points4)
        transformed_start_end_points4.sort(key=point_z)
        
        transformed_obstacle_points = transformed_point(transformed_obstacle_points,rotation_matrix,camera_position,obstacle_points)
        transformed_obstacle_points.sort(key=point_z)
        
        transformed_path_points1 = transformed_point(transformed_path_points1,rotation_matrix,camera_position,path_points1)
        transformed_path_points1.sort(key=point_z)
        
        transformed_path_points2 = transformed_point(transformed_path_points2,rotation_matrix,camera_position,path_points2)
        transformed_path_points2.sort(key=point_z)
        
        transformed_path_points3 = transformed_point(transformed_path_points3,rotation_matrix,camera_position,path_points3)
        transformed_path_points3.sort(key=point_z)
        
        transformed_path_points4 = transformed_point(transformed_path_points4,rotation_matrix,camera_position,path_points4)
        transformed_path_points4.sort(key=point_z)
      
        # Perspective project and blit all the points
        draw_point(transformed_points,center_x,center_y,viewing_distance,ball_back,ball_center_x,ball_center_y,screen)
        draw_point(transformed_start_end_points1,center_x,center_y,viewing_distance,ball_start_end1,ball_center_x,ball_center_y,screen)
        draw_point(transformed_start_end_points2,center_x,center_y,viewing_distance,ball_start_end2,ball_center_x,ball_center_y,screen)
        draw_point(transformed_start_end_points3,center_x,center_y,viewing_distance,ball_start_end3,ball_center_x,ball_center_y,screen)
        draw_point(transformed_start_end_points4,center_x,center_y,viewing_distance,ball_start_end4,ball_center_x,ball_center_y,screen)
        draw_point(transformed_obstacle_points,center_x,center_y,viewing_distance,ball_obstacle,ball_center_x,ball_center_y,screen)
        draw_point(transformed_path_points1,center_x,center_y,viewing_distance,ball_path1,ball_center_x,ball_center_y,screen)
        draw_point(transformed_path_points2,center_x,center_y,viewing_distance,ball_path2,ball_center_x,ball_center_y,screen)
        draw_point(transformed_path_points3,center_x,center_y,viewing_distance,ball_path3,ball_center_x,ball_center_y,screen)
        draw_point(transformed_path_points4,center_x,center_y,viewing_distance,ball_path4,ball_center_x,ball_center_y,screen)
        
        # Function to draw a single axes, see below
        def draw_axis(color, axis, label):
            
            axis = rotation_matrix.transform_vec3(axis * 150.)
            SCREEN_SIZE =  (640, 480)
            center_x = SCREEN_SIZE[0] / 2.0
            center_y = SCREEN_SIZE[1] / 2.0
            x, y, z = axis - camera_position
                
            x = center_x + x * -viewing_distance / z
            y = center_y + -y * -viewing_distance / z
            
            pygame.draw.line(screen, color, (center_x, center_y), (x, y), 2)
            
            w, h = label.get_size()
            screen.blit(label, (x-w/2, y-h/2))
        
        # Draw the x, y and z axes
        x_axis = Vector3(1, 0, 0)
        y_axis = Vector3(0, 1, 0)
        z_axis = Vector3(0, 0, 1)        
        
        draw_axis(red, x_axis, x_surface)
        draw_axis(green, y_axis, y_surface)
        draw_axis(blue, z_axis, z_surface)
            
        # Display rotation information on screen
        degrees_txt = tuple(degrees(r) for r in rotation)
        rotation_txt = "Rotation: Q/A %.3f, W/S %.3f, E/D %.3f" % degrees_txt
        txt_surface = font.render(rotation_txt, True, white)
        screen.blit(txt_surface, (5, 5))
        
        # Displat the rotation matrix on screen
        matrix_txt = str([rotation_matrix])
        txt_y = 25
        for line in matrix_txt.split('\n'):
            txt_surface = font.render(line, True, white)
            screen.blit(txt_surface, (5, txt_y))
            txt_y += 20
        
        num = num + 1
        pygame.display.update()
        clock.tick(FPS)
        
if __name__ == "__main__":
    run()
    
    
    
