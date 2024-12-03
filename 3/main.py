import re

input = open("input.txt", "r")
content = input.read()
input.close()

PATTERN = "mul\(\d+,\d+\)"
PATTERN2 = "mul\(\d+,\d+\)|do\(\)|don\'t\(\)"
sum = 0
sum2 = 0


# find all mul(<num>, <num>) patterns and multiplt
hits = re.findall(PATTERN, content)
for el in hits:
    numbers = re.findall("\d+", el)
    sum += int(numbers[0]) * int(numbers[1])

print(sum)
    
#part2: find all mul(<num>, <num>) patterns and multiply
# but disable/enable pased on do() and don't()
hits = re.findall(PATTERN2, content)
enabled = True

for el in hits:
    if el == "do()":
        enabled = True
    elif el == "don't()":
        enabled = False
    elif enabled:
        numbers = re.findall("\d+", el)
        sum2 += int(numbers[0]) * int(numbers[1])
    
print(sum2)