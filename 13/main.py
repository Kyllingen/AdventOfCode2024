

machines = []

with open("input_test.txt", "r") as file:
    machine = []
    for line in file.readlines():
        
        input = line.rstrip().split(":")
        if input[0].startswith("Button"):
            buttons = input[1].split(",")
            button_x = buttons[0].split("+")
            button_y = buttons[1].split("+")
            machine.append([int(button_x[1]), int(button_y[1])])
            
        elif input[0].startswith("Prize"):
            prize_loc = input[1].split(",")
            prize_x = prize_loc[0].split("=")
            prize_y = prize_loc[1].split("=")
            machine.append([int(prize_x[1]), int(prize_y[1])])
            machines.append([machine[0], machine[1], machine[2]])
            machine = []
            
for machine in machines:
    print(machine)