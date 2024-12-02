import pandas
import numpy
import math

def validate_row(list_row):
    ''' Check if sequence pans out'''
    if all( (list_row[i+1] - list_row[i]) <= 3 and (list_row[i+1] - list_row[i]) > 0  for i in range(len(list_row)-1)):
        return True
    elif all( (list_row[i+1] - list_row[i]) >= -3 and (list_row[i+1] - list_row[i]) < 0  for i in range(len(list_row)-1)):
        return True
    
    return False

input_file = pandas.read_table("input.txt", sep="\s+", header=None)

safe_list = 0
#sort and then find range between two values  (PART 1)
for row in input_file.itertuples():
    list_row = [val for val in row if not math.isnan(val) ]
    list_row = list_row[1:]

    if validate_row(list_row):
        safe_list += 1

print(safe_list)

# include problem dampener (PART 2)
safe_list_dampener = 0
for row in input_file.itertuples():
    full_row = [val for val in row if not math.isnan(val) ]
    full_row = full_row[1:]
    
    if validate_row(full_row):
        safe_list_dampener += 1
    else:
        # remove an item at a time in the list and check if it works
        for i in range(0, len(full_row)):
            list_row = full_row.copy()
            del list_row[i]
            if validate_row(list_row):
                safe_list_dampener += 1
                break
        print(full_row)
            
        
print(safe_list_dampener)
    
    
    
    