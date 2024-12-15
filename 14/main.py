#Global params to set right board size and loops
import math

X_MAX = 101
Y_MAX = 103
MAX_SECONDS = 100

X_MAX_TEST = 11
Y_MAX_TEST = 7

TEST = False
TEST_SIMPLE = False

robots = []

def move_robot(position: tuple, velocity: tuple):
    ''' move robot to new position, warping if out of bounds'''
    new_x = position[0] + velocity[0]
    new_y = position[1] + velocity[1]
    if new_x >= X_MAX:
        new_x = new_x - X_MAX
    if new_x < 0:
        new_x = X_MAX + new_x
    if new_y >= Y_MAX:
       new_y = new_y - Y_MAX
    if new_y < 0:
        new_y = Y_MAX + new_y
       
    return (new_x, new_y)

def move_robots(robots: list):
    ''' go through all robots and move them'''
    for robot in robots:
        position = robot[0]
        velocity = robot[1]
        robot[0] = move_robot(position, velocity)
        
def count_robots_in_quadrants():
    ''' split board in 4 quadrants, middle rows ignored
        then count number of robots in each'''
    
    x_first_quad = math.floor(X_MAX/2)
    x_second_quad = math.ceil(X_MAX/2)
    y_first_quad = math.floor(Y_MAX/2)
    y_second_quad = math.ceil(Y_MAX/2)
    
    quad_1_count = 0
    quad_2_count = 0
    quad_3_count = 0
    quad_4_count = 0
    
    for robot in robots:
        position = robot[0]
        
        if position[0] < x_first_quad:
            if position[1] < y_first_quad:
                quad_1_count += 1
            elif position[1] >= y_second_quad:
                quad_2_count += 1
        elif position[0] >= x_second_quad:
            if position[1] < y_first_quad:
                quad_3_count += 1
            elif position[1] >= y_second_quad:
                quad_4_count += 1
                
    return quad_4_count * quad_1_count * quad_3_count * quad_2_count
            
        
# simplify parameter setting
if TEST:
    file_name = 'input_test.txt'
    X_MAX = X_MAX_TEST
    Y_MAX = Y_MAX_TEST
elif TEST_SIMPLE:
    file_name = 'input_test_simple.txt'
    X_MAX = X_MAX_TEST
    Y_MAX = Y_MAX_TEST
    MAX_SECONDS = 5
else:
    file_name = "input.txt" 
      
#read file and create robots
with open(file_name, "r") as file:
    for line in file.readlines():
        pos_and_velo = line.split(" ")
        position = pos_and_velo[0].split("=")
        position = position[1].split(",")
        velocity = pos_and_velo[1].split("=")
        velocity = velocity[1].split(",")
        
        robots.append([ (int(position[0]), int(position[1])) \
                       ,(int(velocity[0]), int(velocity[1])) ])
      
print(robots)  
for i in range(0, MAX_SECONDS):
    move_robots(robots)
    

security_count = count_robots_in_quadrants()
print(security_count)