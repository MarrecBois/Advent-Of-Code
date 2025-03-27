#2024 Day 8
import os
import copy

os.chdir("c:/Users/marre/OneDrive/Documents/Advent of Code 2024/Day 8")
file = open("2024_day_8.txt")

grid = []

for line in file:
    line = line.strip()
    row = []
    for char in line:
        row.append(char)
    
    grid.append(row)

#Part 1
# height = len(grid) - 1
# width = len(grid[0]) - 1

# print(height)
# print(width)
# antennas = []
# antinodes = []

# for i in range(height):
#     for j in range(width):

#         #If find a NEW letter/number for an antenna
#         if grid[i][j] != '.' and grid[i][j] not in antennas:
#             char = grid[i][j]
#             antennas.append(char)
#             coords = []

#             #Loop through to find the location of all matching antennae
#             for restOfi in range(i, height):
#                 for k in range(width):
#                     if grid[restOfi][k] == char:
#                         coords.append([restOfi, k])
            
#             #Loop through the matching antennae
#             for antenna1 in range(len(coords)):
#                 for antenna2 in range(antenna1 + 1, len(coords)):
#                     antenna1_x = coords[antenna1][0]
#                     antenna1_y = coords[antenna1][1]
#                     antenna2_x = coords[antenna2][0]
#                     antenna2_y = coords[antenna2][1]

#                     x_diff = abs(antenna1_x - antenna2_x)
#                     y_diff = abs(antenna1_y - antenna2_y)
#                     minx = min([antenna1_x, antenna2_x])
#                     miny = min([antenna1_y, antenna2_y])

#                     if minx == antenna1_x:
#                         pos1x = antenna1_x - x_diff
#                         pos2x = antenna2_x + x_diff

#                         if miny == antenna1_y:
#                             pos1y = antenna1_y - y_diff
#                             pos2y = antenna2_y + y_diff
#                         else:
#                             pos1y = antenna1_y + y_diff
#                             pos2y = antenna2_y - y_diff
                    
#                     else:
#                         pos1x = antenna1_x + x_diff
#                         pos2x = antenna2_x - x_diff

#                         if miny == antenna1_y:
#                             pos1y = antenna1_y - y_diff
#                             pos2y = antenna2_y + y_diff
#                         else:
#                             pos1y = antenna1_y + y_diff
#                             pos2y = antenna2_y - y_diff

#                     pos1 = [pos1x, pos1y]
#                     pos2 = [pos2x, pos2y]

#                     if pos1 not in antinodes and pos1x >= 0 and pos1x <= width and pos1y >= 0 and pos1y <= height + 1:
#                         antinodes.append(pos1)
                    
#                     if pos2 not in antinodes and pos2x >= 0 and pos2x <= width and pos2y >= 0 and pos2y <= height + 1:
#                         antinodes.append(pos2)

# print(len(antinodes))

#Part 2
height = len(grid) - 1
width = len(grid[0]) - 1

print(height)
print(width)
antennas = []
antinodes = []
antenna_spots = []

for i in range(height):
    for j in range(width):

        #If find a NEW letter/number for an antenna
        if grid[i][j] != '.':
            antenna_spots.append([i, j])
        if grid[i][j] != '.' and grid[i][j] not in antennas:
            char = grid[i][j]
            antennas.append(char)
            coords = []

            #Loop through to find the location of all matching antennae
            for restOfi in range(i, height):
                for k in range(width):
                    if grid[restOfi][k] == char:
                        coords.append([restOfi, k])
            
            #Loop through the matching antennae
            if len(coords) > 1:
                for antenna1 in range(len(coords)):
                    for antenna2 in range(antenna1 + 1, len(coords)):
                        antenna1_x = coords[antenna1][0]
                        antenna1_y = coords[antenna1][1]
                        antenna2_x = coords[antenna2][0]
                        antenna2_y = coords[antenna2][1]

                        x_diff = abs(antenna1_x - antenna2_x)
                        y_diff = abs(antenna1_y - antenna2_y)
                        minx = min([antenna1_x, antenna2_x])
                        miny = min([antenna1_y, antenna2_y])

                        if minx == antenna1_x:
                            pos1x = antenna1_x - x_diff
                            pos2x = antenna2_x + x_diff

                            if miny == antenna1_y:
                                pos1y = antenna1_y - y_diff
                                pos2y = antenna2_y + y_diff
                                for count in range(100):
                                    pos1 = [antenna1_x - count * x_diff, antenna1_y - count * y_diff]
                                    pos2 = [antenna2_x + count * x_diff, antenna2_y + count * y_diff]
                                    if pos1 not in antinodes and pos1[0] >= 0 and pos1[0] <= width and pos1[1] >= 0 and pos1[1] <= height:
                                        antinodes.append(pos1)
                                    
                                    if pos2 not in antinodes and pos2[0] >= 0 and pos2[0] <= width and pos2[1] >= 0 and pos2[1] <= height:
                                        antinodes.append(pos2)

                            else:
                                pos1y = antenna1_y + y_diff
                                pos2y = antenna2_y - y_diff
                                for count in range(100):
                                    pos1 = [antenna1_x - count * x_diff, antenna1_y + count * y_diff]
                                    pos2 = [antenna2_x + count * x_diff, antenna2_y - count * y_diff]
                                    if pos1 not in antinodes and pos1[0] >= 0 and pos1[0] <= width and pos1[1] >= 0 and pos1[1] <= height:
                                        antinodes.append(pos1)
                                    
                                    if pos2 not in antinodes and pos2[0] >= 0 and pos2[0] <= width and pos2[1] >= 0 and pos2[1] <= height:
                                        antinodes.append(pos2)
                        
                        else:
                            pos1x = antenna1_x + x_diff
                            pos2x = antenna2_x - x_diff

                            if miny == antenna1_y:
                                pos1y = antenna1_y - y_diff
                                pos2y = antenna2_y + y_diff
                                for count in range(100):
                                    pos1 = [antenna1_x + count * x_diff, antenna1_y - count * y_diff]
                                    pos2 = [antenna2_x - count * x_diff, antenna2_y + count * y_diff]
                                    if pos1 not in antinodes and pos1[0] >= 0 and pos1[0] <= width and pos1[1] >= 0 and pos1[1] <= height:
                                        antinodes.append(pos1)
                                    
                                    if pos2 not in antinodes and pos2[0] >= 0 and pos2[0] <= width and pos2[1] >= 0 and pos2[1] <= height:
                                        antinodes.append(pos2)
                            else:
                                pos1y = antenna1_y + y_diff
                                pos2y = antenna2_y - y_diff

                                for count in range(100):
                                    pos1 = [antenna1_x + count * x_diff, antenna1_y + count * y_diff]
                                    pos2 = [antenna2_x - count * x_diff, antenna2_y - count * y_diff]
                                    if pos1 not in antinodes and pos1[0] >= 0 and pos1[0] <= width and pos1[1] >= 0 and pos1[1] <= height:
                                        antinodes.append(pos1)
                                    
                                    if pos2 not in antinodes and pos2[0] >= 0 and pos2[0] <= width and pos2[1] >= 0 and pos2[1] <= height:
                                        antinodes.append(pos2)

count = 0
for antinode in antinodes:
    if antinode[0] < 0 or antinode[0] > 49:
        count += 1
        print(antinode)
    if antinode[1] < 0 or antinode[1] > 49:
        count += 1
        print(antinode)

for antenna in antenna_spots:
    if antenna not in antinodes:
        print(grid[antenna[0]][antenna[1]])

print(len(antinodes))
print(len(antinodes) - count)