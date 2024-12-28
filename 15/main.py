
map = []
directions = []
robot_position = None

def move_robot(old_position: tuple, dir):
    
    new_position = map[next_position[0]][next_position[1]]
    
    if map[next_position[0]][next_position[1]] == '.':
        map[next_position[0]][next_position[1]] = '@'
    else:
        while True:
            next_position = (old_position[0+dir[0]],old_position[1+dir[1]])
    return new_position

def check_route(current_position: tuple, dir: tuple):
    if map[current_position[0+dir[0]]][current_position[1+dir[1]]] == '#':
        return False
    elif map[current_position[0+dir[0]]][current_position[1+dir[1]]] == 'O':
        new_position = (current_position[0]+dir[0], current_position[1]+dir[1])
        return check_route(new_position, dir, True)
    if map[current_position[0+dir[0]]][current_position[1+dir[1]]] == '.':
        return True
        
            
def set_direction(direction: str, robot_position: tuple):
    print(direction, robot_position)
    dir_x = 0
    dir_y = 0
    if direction == "<":
        dir_y = -1
    elif direction == ">":
        dir_y = 1
    if direction == "^":
        dir_x = -1
    if direction == "v":
        dir_x = 1
    
    possible_move = check_route(robot_position, (dir_x, dir_y) )
    if possible_move:
        return move_robot(robot_position, (dir_x, dir_y))
    
        

with  open("input_test_simple.txt", "r") as file:
    read_map = True
    row = 0
    for line in file:
        if line == "\n":
            read_map = False
        elif read_map:
            if line.find("@") != -1:
                robot_position = (row, line.index("@"))
            map.append([char for char in line.rstrip()])
        else:
            directions = [dir for dir in line]
        row += 1
            
for dir in directions:
    print(dir, robot_position)
    robot_position = set_direction(dir, robot_position)
    print("return", robot_position)