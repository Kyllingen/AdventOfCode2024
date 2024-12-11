
trails = []
trailheads = []
total_trails = 0

def search(trails, prev_height, row, col, visited):
    ''' Use DFS style algorithm'''
     
    # Check out of bounds
    if row < 0 or row >= len(trails) or col < 0 or col >= len(trails[0]):
        return 0
    
    current_height = trails[row][col]
    
    # going down or same distance, return False
    if prev_height >= current_height or current_height > (prev_height+1):
        return 0
        
    # Word match found
    if current_height == 9:
        print("DONE TRAIL")
        return 1
    
    # ignore already visited areas on this trail
    if (row, col) in visited:
        return 0
    
    #visited 
    visited.append((row, col))
    
    #scan all direcitons for word based on current index
    res1 =  search(trails, current_height, row-1, col, visited)
    res2 = search(trails, current_height, row+1, col, visited)
    res3 = search(trails, current_height, row, col-1, visited)
    res4 = search(trails, current_height, row, col+1, visited)
     
    return res1 + res2 + res3 + res4


# read file for trails and trailhead starts
with open("input_test.txt", "r") as file:
    row = 0
    for line in file.readlines():
        line = line.rstrip()
        trails.append([int(trail) for trail in line])
        trailheads += ( [(row, i) for i, trailhead in enumerate(line) if int(trailhead) == 0])
        row += 1
        
for start in trailheads:
    total_trails += search(trails, 0, start[0]+1, start[1], [])
    #total_trails += search(trails, 0, start[0]-1, start[1], [])
    #total_trails += search(trails, 0, start[0], start[1]+1, [])
    #total_trails += search(trails, 0, start[0], start[1]-1, [])
    print ("TRAIL", start, total_trails)

  