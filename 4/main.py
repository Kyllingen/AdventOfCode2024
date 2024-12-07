import re 

matrix = []
word = "XMAS"
word_count = 0

with open("simple_input_test.txt", "r") as file:
    lines = file.read().splitlines()

for line in lines:
    matrix.append([letter for letter in line])

print(matrix)

visited = {}
def search(matrix, word, row, col, visited, pos=0):
    ''' Use DFS style algorithm'''

    # Word match found
    if len(word) == pos:
        return True
    
    # Check out of bounds
    if row < 0 or row == len(matrix) or col < 0 or col == len(matrix[0])  \
         or word[pos] != matrix[row][col]:
        return False
    
    # No match, not the right word
    visited[(row, col)] = True
    
    #scan all direcitons for word based on current index
    #res =  search(matrix, word, row-1, col, visited, pos+1) \
    #    or search(matrix, word, row+1, col, visited, pos+1) \
    #    or search(matrix, word, row, col-1, visited, pos+1) \
    #    or search(matrix, word, row, col+1, visited, pos+1) \
    #    or search(matrix, word, row+1, col-1, visited, pos+1) \
    #    or search(matrix, word, row+1, col+1, visited, pos+1) \
    #    or search(matrix, word, row-1, col-1, visited, pos+1) \
    #    or search(matrix, word, row-1, col+1, visited, pos+1)
    if search(matrix, word, row+1, col, visited, pos+1):
        return True
    if search(matrix, word, row, col+1, visited, pos+1):
        return True
    if search(matrix, word, row-1, col, visited, pos+1):
        return True
    if search(matrix, word, row, col-1, visited, pos+1):
        return True
    if search(matrix, word, row+1, col-1, visited, pos+1):
        return True
    if search(matrix, word, row+1, col+1, visited, pos+1):
        return True
    if search(matrix, word, row-1, col-1, visited, pos+1):
        return True
    if search(matrix, word, row-1, col+1, visited, pos+1):
        return True
    
    visited[(row,col)] = False
    
    return res

# start searching for our magic word
for row in range(len(matrix)):
    for col in range(len(matrix[0])):
        if search(matrix, word, row, col, visited):
            word_count += 1
            print(row, col)

print(word_count)