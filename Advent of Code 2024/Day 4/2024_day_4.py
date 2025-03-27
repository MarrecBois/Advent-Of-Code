#2024 Day 4
import os

os.chdir("c:/Users/marre/OneDrive/Documents/Advent of Code 2024/Day 4")
file = open("2024_day_4.txt")

#Make 2d array
grid = []
for line in file:
    line = line.strip()
    row = []
    for char in line:
        row.append(char)
    
    grid.append(row)


# #Silver star
# xmas_count = 0
# for row in range(len(grid)):
#     for col in range(len(grid[0])):
#         #Check every direction if the character is an X
#         if grid[row][col] == 'X':

#             #Down
#             if row < len(grid) - 3:
#                 if grid[row + 1][col] == 'M' and grid[row + 2][col] == 'A' and grid[row+3][col] == 'S':
#                     xmas_count += 1
                
#                 #Down right
#                 if col < len(grid[0]) - 3:
#                     if grid[row + 1][col + 1] == 'M' and grid[row + 2][col + 2] == 'A' and grid[row + 3][col + 3] == 'S':
#                         xmas_count += 1
                
#                 #Down left
#                 if col > 2:
#                     if grid[row + 1][col -1] == 'M' and grid[row + 2][col - 2] == 'A' and grid[row + 3][col - 3] == 'S':
#                         xmas_count += 1
                            
#             #Up
#             if row > 2:
#                 if grid[row - 1][col] == 'M' and grid[row - 2][col] == 'A' and grid[row - 3][col] == 'S':
#                     xmas_count += 1

#                 #Up right
#                 if col < len(grid[0]) - 3:
#                     if grid[row - 1][col + 1] == 'M' and grid[row - 2][col + 2] == 'A' and grid[row - 3][col + 3] == 'S':
#                         xmas_count += 1
                
#                 #Up left
#                 if col > 2:
#                     if grid[row - 1][col - 1] == 'M' and grid[row - 2][col - 2] == 'A' and grid[row - 3][col - 3] == 'S': 
#                         xmas_count += 1
            
#             #Right
#             if col < len(grid[0]) - 3:
#                 if grid[row][col + 1] == 'M' and grid[row][col + 2] == 'A' and grid[row][col + 3] == 'S':
#                     xmas_count += 1
            
#             #Left
#             if col > 2:
#                 if grid[row][col-1] == 'M' and grid[row][col -2] == 'A' and grid[row][col - 3] == 'S':
#                     xmas_count += 1

# print(xmas_count)

#Gold star attempt 1
# xmas_count = 0
# bad_coords = []
# for row in range(len(grid)):
#     for col in range(len(grid[0])):
#         #Check every direction if the character is an M and will have to remove it from the possible coordinates to check later if find one...
#         if grid[row][col] == 'M' and [row,col] not in bad_coords:

#             #Down
#             if row < len(grid) - 2:
                
#                 #Down right
#                 if col < len(grid[0]) - 2:
#                     if grid[row + 1][col + 1] == 'A' and grid[row + 2][col + 2] == 'S':
#                         #Check both directions for the second MAS
#                         if grid[row + 2][col] == 'M' and grid[row][col + 2] == 'S':
#                             bad_coords.append([row + 2, col])
#                             xmas_count += 1
#                         elif grid[row+2][col] == 'S' and grid[row][col+2] == 'M':
#                             bad_coords.append([row, col + 2])
#                             xmas_count += 1

#                 #Down left
#                 if col > 1:
#                     if grid[row + 1][col -1] == 'A' and grid[row + 2][col - 2] == 'S':
#                         #Check both directions for the second MAS
#                         if grid[row + 2][col] == 'M' and grid[row][col - 2] == 'S':
#                             bad_coords.append([row+2, col])
#                             xmas_count += 1
#                         elif grid[row + 2][col] == 'S' and grid[row][col-2] == 'M':
#                             bad_coords.append([row, col-2])
#                             xmas_count += 1

                            
#             #Up
#             if row > 1:

#                 #Up right
#                 if col < len(grid[0]) - 2:
#                     if grid[row - 1][col + 1] == 'A' and grid[row - 2][col + 2] == 'S':
#                         #Check both directions for the second MAS
#                         if grid[row - 2][col] == 'M' and grid[row][col + 2] == 'S':
#                             bad_coords.append([row-2, col])
#                             xmas_count += 1
#                         elif grid[row -2][col] == 'S' and grid[row][col+2] == 'M':
#                             bad_coords.append([row, col + 2])
#                             xmas_count += 1
                
#                 #Up left
#                 if col > 1:
#                     if grid[row - 1][col - 1] == 'A' and grid[row - 2][col - 2] == 'S': 
#                         #Check both directions for the second MAS
#                         if grid[row][col-2] == 'M' and grid[row-2][col] == 'S':
#                             bad_coords.append([row, col-2])
#                             xmas_count += 1
#                         elif grid[row][col-2] == 'S' and grid[row-2][col] == 'M':
#                             bad_coords.append([row-2,col])
#                             xmas_count += 1
#print(xmas_count)


#Gold star attempt 2
xmas_count = 0

for row in range(1, len(grid) - 1):
    for col in range(1, len(grid[0]) - 1):
        if grid[row][col] == 'A':
            #Now check if there is an x around the A
            if ((grid[row-1][col-1] == 'M' and grid[row+1][col+1] == 'S') or (grid[row-1][col-1] == 'S' and grid[row+1][col+1] == 'M')) and ((grid[row+1][col-1] == 'M' and grid[row-1][col+1] == 'S') or (grid[row+1][col-1] == 'S' and grid[row-1][col+1] == 'M')):
                xmas_count += 1

print(xmas_count)