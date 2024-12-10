

def createBlocks(sections: list):
    ''' create the block with numbers and empty slots'''
    id = 0
    blocks = []
    
    for i in range(0, len(sections)):
        if i % 2 == 0:
            blocks.extend( [id] * sections[i])
            id += 1
        else:
            blocks.extend( [-1] * sections[i])
    print("ID", id)
    return blocks

def findOccurrences(blocks: list, empty_slots: bool):
    ''' find occurrences of empty slots or non-empty slots'''
    if empty_slots:
        return [i for i, num in enumerate(blocks) if num == -1]
    else:
        return [i for i, num in enumerate(blocks) if num != -1]

def fillEmptySlots(blocks: list, empty_slots:list, filled_slots:list):
    '''fill up empty slots with filled_slots (reverse). 
       Assumes empty_slots is smaller than filled_slots'''
  
    for i in range(0, len(empty_slots)):
        filled_index =filled_slots[-(1+i)]
        empty_index = empty_slots[i]
        
        # all numbers contingous
        if empty_index >= filled_index:
            break
        
        blocks[empty_index] = blocks[filled_index]
        blocks[filled_index] = -1
   
    return blocks

def fillEmptySlotsContingous(blocks:list, empty_slots:list, filled_slots:list):
    #NOT DONE YET
    for i in range(0, len(filled_slots)):
        
        filled_index =filled_slots[-(1+i)]
        empty_index = empty_slots[i]
        
        # all numbers contingous
        if empty_index >= filled_index:
            break
        
        blocks[empty_index] = blocks[filled_index]
        blocks[filled_index] = -1
   
    return blocks    

def sum_block(block: list):
    '''calculate sum by summing number * index'''
    total_sum = 0
    for i in range(0,len(block)):
        if block[i] == -1: # at the end
            break
        
        total_sum += i * block[i]
        
    return total_sum

with open("input.txt", "r") as file:
    input =file.read()
    
sections = [int(num) for num in input]
blocks = createBlocks(sections)
empty_slots = findOccurrences(blocks, True)
filled_slots = findOccurrences(blocks, False)

reordered_blocks = fillEmptySlots(blocks, empty_slots, filled_slots)
reordered_blocks_part2 = fillEmptySlots(blocks, empty_slots, filled_slots, True)

total_sum = sum_block(reordered_blocks)
total_sum2 = sum_block(reordered_blocks_part2)

print(total_sum)
print(total_sum2)