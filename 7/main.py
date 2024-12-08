
        
def calculate_answers(answer, index, current_sum, numbers):
    '''dps search for sums to equal answer'''
    if index == len(numbers):
        return [current_sum == answer, current_sum]
    
    temp_sum = current_sum + numbers[index]
    res = calculate_answers(answer, index+1, temp_sum, numbers)
    print("looping after ADD", index, current_sum, numbers, res)
    if res[0]:
        print("addition", answer, numbers)
        return res
    
    temp_sum = current_sum * numbers[index]
    res = calculate_answers(answer, index+1, temp_sum, numbers)
    print("looping after MULT", index, current_sum, numbers, res)
    if res[0]:
        print("mult", answer, numbers)
        return res
    
    #part two
    # if index+1 < len(numbers):
        
    #     new_number = int(str(numbers[index]) + '' + str(numbers[index+1]))
    #     #edge case of list initially having only 2 numbers
    #     if (new_number) == answer and len(numbers) == 2:
    #         return [True, new_number]
        
    #     numbers_list2 = numbers.copy()
    #     numbers_list2[index] = new_number
    #     del numbers_list2[index+1]
        
    #     res = calculate_answers(answer, 0, current_sum, numbers_list2)
    #     if res[0]:
    #         print("merged",answer, numbers)
    #         return res
        
    return [False, current_sum]
    

numbers_list = []
total_sum = 0

with open("input_test_simple.txt", "r") as file:
    lines = file.read().splitlines()

for line in lines:
    group = line.split(":")
    numbers = list(map(int, group[1].split()))
    #res = calculate_answers(int(group[0]), 0, 0, numbers)
    print("START-------------------")
    res = calculate_answers(int(group[0]),0, 0, numbers)
    if res[0]:
        print ("FOUND!", group[0], numbers)
        total_sum += res[1]
        #print(group[0], numbers)
    
print(total_sum)