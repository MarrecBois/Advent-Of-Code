#2024 Day 10
import os
import copy

os.chdir("c:/Users/marre/OneDrive/Documents/Advent of Code 2024/Day 10")
file = open("2024_day_10.txt")

grid = []

for line in file:
    line = line.strip()
    row = []
    for num in line:
        row.append(int(num))

    grid.append(row)

for row in grid:
    print(row)


def check_surroundings(grid, row, col, number, coords):
    if number == 9 and grid[row][col] == number:
        coords.append([row,col])
    elif grid[row][col] == number:
        #Do checks in every direction
        if row != 0:
            check_surroundings(grid, row-1, col, number + 1, coords)
        if row != len(grid) - 1:
            check_surroundings(grid, row+1, col, number + 1, coords)
        if col != 0:
            check_surroundings(grid, row, col-1, number + 1, coords)
        if col != len(grid[0]) - 1:
            check_surroundings(grid, row, col+1, number + 1, coords)
    else:
        return
        
total_scores = 0
#GRAPHHHHHHH THEORY
for row in range(len(grid)):
    for col in range(len(grid[0])):
        if grid[row][col] == 0:
            coords = []
            check_surroundings(grid, row, col, 0, coords)
            unique_coords = []
            for coord in coords:
                if coord not in unique_coords:
                    unique_coords.append(coord)
            
            score = len(coords)
            total_scores += score
            print("Score: {}".format(score))

print("Total score: {}".format(total_scores))
            