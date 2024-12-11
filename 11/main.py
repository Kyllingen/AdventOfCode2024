import math


stones = []
    
def blink(stones: list):
    ''' Go through list of stones and apply blinking rules.
        
        Very much a naive method of filtering through the stones
        Simple to do, but will struggle/fail on larger iterations'''
    
    new_stones = []
    i = 0
    for stone in stones:
        if stone == 0:
            new_stones.append(1)
        elif (int(math.log10(stone))+1) % 2 == 0:
            half_digits = int( ((math.log10(stone))+1)/2)
            
            stone1 = str(stone)[0:half_digits]
            stone2 = str(stone)[half_digits:]
            new_stones.append(int(stone1))
            new_stones.append(int(stone2))
        else:
            new_stones.append(stone * 2024)
    
    return new_stones


if __name__ == "__main__":
    with open("input.txt", "r") as file:
        input = file.read().rstrip()
        stones = [int(stone) for stone in input.split()]

    for i in range(0, 25):
        stones = blink(stones)
        print ("LAP", i)

    print(len(stones))