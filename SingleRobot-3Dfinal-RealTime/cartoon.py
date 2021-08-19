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
obstacle_list = [(3, 3, 2),(3, 3, 3), (3, 3, 4)]

def calculate_viewing_distance(fov, screen_width):
    
    d = (screen_width/2.0) / tan(fov/2.0)
    return d

def back(m1,paths):
    points = []
    start_end_points = []
    obstacle_points = []
    path_points = []
    m=m1
    path_list = paths
    
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
                    
                    start_end_list = [(1, 1, 3), (5, 5, 3)]
                    for i in range(0,len(start_end_list)):
                        start_end_points = point(start_end_points,x,y,z,start_end_list[i][0],start_end_list[i][1],start_end_list[i][2])
                    
                    for i in range(0,len(obstacle_list)):
                        obstacle_points = point(obstacle_points,x,y,z,obstacle_list[i][0],obstacle_list[i][1],obstacle_list[i][2])

                    path_points = point(path_points,x,y,z,path_list[m][0],path_list[m][1],path_list[m][2]) 
                    
    return points,start_end_points,obstacle_points,path_points

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
    
def run(paths):

    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE, 0)
    FPS = 1 #每秒 10 帧
    
        
    font = pygame.font.SysFont("courier new", 16, True)
    
    ball_back = pygame.image.load("ball_back.png").convert_alpha()
    ball_start_end = pygame.image.load("ball_start_end.png").convert_alpha()
    ball_obstacle = pygame.image.load("ball_obstacle.png").convert_alpha()
    ball_path = pygame.image.load("ball_path.png").convert_alpha()
    
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
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                quit()
                
            if event.type == KEYDOWN:
                #通过按键kq添加障碍物，障碍物坐标为(key_x0,key_y0,key_z0)
                if event.key == K_q:
                    global keydown0,key_x0,key_y0,key_z0
                    keydown0 = True
                    key_x0 = 3
                    key_y0 = 4
                    key_z0 = 4
                    obstacle_list.append((key_x0,key_y0,key_z0))
                    # rotation_direction.x = +1.0
                #通过按键ka添加障碍物，障碍物坐标为(key_x1,key_y1,key_z1)
                elif event.key == K_a:
                    global keydown1,key_x1,key_y1,key_z1
                    keydown1 = True
                    key_x1 = 3
                    key_y1 = 4
                    key_z1 = 3
                    obstacle_list.append((key_x1,key_y1,key_z1))
                    # rotation_direction.x = -1.0
        
        points,start_end_points,obstacle_points,path_points = back(len(paths)-1,paths)
        
        screen.fill((255, 255, 255))       
        
        time_passed = clock.tick()
        time_passed_seconds = time_passed / 1000.                
        
        
        
        #Adjust the rotation direction depending on key presses
        pressed_keys = pygame.key.get_pressed()
        
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
        transformed_start_end_points = []
        transformed_obstacle_points = []
        transformed_path_points = []

        # Transform all the points and adjust for camera position
        transformed_points = transformed_point(transformed_points,rotation_matrix,camera_position,points)
        transformed_points.sort(key=point_z)
        
        transformed_start_end_points = transformed_point(transformed_start_end_points,rotation_matrix,camera_position,start_end_points)
        transformed_start_end_points.sort(key=point_z)
        
        transformed_obstacle_points = transformed_point(transformed_obstacle_points,rotation_matrix,camera_position,obstacle_points)
        transformed_obstacle_points.sort(key=point_z)
        
        transformed_path_points = transformed_point(transformed_path_points,rotation_matrix,camera_position,path_points)
        transformed_path_points.sort(key=point_z)
      
        # Perspective project and blit all the points
        draw_point(transformed_points,center_x,center_y,viewing_distance,ball_back,ball_center_x,ball_center_y,screen)
        draw_point(transformed_start_end_points,center_x,center_y,viewing_distance,ball_start_end,ball_center_x,ball_center_y,screen)
        draw_point(transformed_obstacle_points,center_x,center_y,viewing_distance,ball_obstacle,ball_center_x,ball_center_y,screen)
        draw_point(transformed_path_points,center_x,center_y,viewing_distance,ball_path,ball_center_x,ball_center_y,screen)
        
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
    
    
    
