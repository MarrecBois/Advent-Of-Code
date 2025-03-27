#2024 Day 6
import os
import copy

os.chdir("c:/Users/marre/OneDrive/Documents/Advent of Code 2024/Day 6")
file = open("2024_day_6.txt")

rows = []

for line in file:
    row = line.strip()
    rowchars = []
    for char in row:
        rowchars.append(char)

    rows.append(rowchars)


for i in range(len(rows)):
    for j in range(len(rows[i])):
        if rows[i][j] == '^':
            start_location = [i, j]

print(rows[start_location[0]][start_location[1]])

def check_grid(grid, location, wall_location):
    if grid[wall_location[0]][wall_location[1]] != '.':
        return 0
    else:
        grid[wall_location[0]][wall_location[1]] = '#'

    isOnMap = True
    total = 1
    count = 0
    loc = location[ : ]

    while isOnMap and count < 100000:
        char = grid[loc[0]][loc[1]]

        #If facing upwards, either move up or turn to face right
        if char == '^':
            if loc[0] == 0:
                isOnMap = False
            elif grid[loc[0] - 1][loc[1]] == '#':
                grid[loc[0]][loc[1]] = '>'
            else:
                if grid[loc[0] - 1][loc[1]] == '.':
                    total += 1
                
                grid[loc[0]][loc[1]] = 'X'
                loc[0] -= 1
                grid[loc[0]][loc[1]] = char

        #If facing right, either move right or turn to face downwards
        elif char == '>':
            if loc[1] == len(grid[0]) - 1:
                isOnMap = False
            elif grid[loc[0]][loc[1] + 1] == '#':
                grid[loc[0]][loc[1]] = 'v'
            else:
                if grid[loc[0]][loc[1] + 1] == '.':
                    total += 1
                
                grid[loc[0]][loc[1]] = 'X'
                loc[1] += 1
                grid[loc[0]][loc[1]] = char
    
        #If facign left, either move left or turn to face upwards
        elif char == '<':
            if loc[1] == 0:
                isOnMap = False
            elif grid[loc[0]][loc[1] - 1] == '#':
                grid[loc[0]][loc[1]] = '^'
            
            else:
                if grid[loc[0]][loc[1] - 1] == '.':
                    total += 1
                
                grid[loc[0]][loc[1]] = 'X'
                loc[1] -= 1
                grid[loc[0]][loc[1]] = char

        #If facing down, either move down or turn to face left
        elif char == 'v':
            if loc[0] == len(grid) - 1:
                isOnMap = False
            elif grid[loc[0] + 1][loc[1]] == '#':
                grid[loc[0]][loc[1]] = '<'
            else:
                if grid[loc[0] + 1][loc[1]] == '.':
                    total += 1
                
                grid[loc[0]][loc[1]] = 'X'
                loc[0] += 1
                grid[loc[0]][loc[1]] = char
        
        count += 1
    
    if count == 100000:
        return 1
    else:
        return 0


spots = 0

for i in range(len(rows)):
    for j in range(len(rows[0])):
        prev_spots = spots
        grid = copy.deepcopy(rows)
        spots += check_grid(grid, start_location, [i, j])

        if prev_spots < spots:
            print(spots)
        else:
            print("not a good spot")


print(spots)