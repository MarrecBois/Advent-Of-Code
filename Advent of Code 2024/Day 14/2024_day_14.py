#2024 Day 14
import os
import copy
import time

os.chdir("c:/Users/marre/OneDrive/Documents/Advent of Code 2024/Day 14")
file = open("2024_day_14.txt")

positions = []
velocities = []

for line in file:
    line = line.strip()
    pos1 = line.find('=')
    pos2 = line.find(',')
    pos3 = line.find(' ')

    x_pos = int(line[pos1 + 1: pos2])
    y_pos = int(line[pos2 + 1: pos3])
    positions.append([x_pos, y_pos])

    pos4 = line.find('=', pos1 + 1)
    pos5 = line.find(',', pos2 + 1)
    x_vel = int(line[pos4 + 1: pos5])
    y_vel = int(line[pos5 + 1:])
    velocities.append([x_vel, y_vel])

print(positions)
print(velocities)

# for i in range(len(positions)):
#     x_pos = positions[i][0]
#     y_pos = positions[i][1]
#     x_vel = velocities[i][0]
#     y_vel = velocities[i][1]

#     x_pos = x_pos + 100*x_vel
#     y_pos = y_pos + 100*y_vel

#     x_pos = x_pos % 101
#     y_pos = y_pos % 103
#     positions[i] = [x_pos, y_pos]

# grid = []
# for i in range(103):
#     row = [0] * 101
#     grid.append(row)

# for row in grid:
#     print(row)


# print(positions)

# for position in positions:
#     print(position[0])
#     print(position[1])
#     grid[position[1]][position[0]] += 1

# for row in grid:
#     string = ""
#     for char in row:
#         string += str(char)
#     print(string)


# #First quadrant
# quad1 = 0
# for i in range(len(grid[0]) // 2):
#     for j in range(len(grid) // 2):
#         quad1 += grid[j][i]

# #Second quadrant
# quad2 = 0
# for i in range(len(grid[0]) // 2 + 1, len(grid[0])):
#     for j in range(len(grid) // 2):
#         quad2 += grid[j][i]

# #Third quadrant
# quad3 = 0
# for i in range(len(grid[0]) // 2):
#     for j in range(len(grid) // 2 + 1, len(grid)):
#         quad3 += grid[j][i]

# #Fourth quadrant
# quad4 = 0
# for i in range(len(grid[0]) // 2 + 1, len(grid[0])):
#     for j in range(len(grid) // 2 + 1, len(grid)):
#         quad4 += grid[j][i]

# total = quad1*quad2*quad3*quad4

# print(total)

for count in range(10000):

    for i in range(len(positions)):
        x_pos = positions[i][0]
        y_pos = positions[i][1]
        x_vel = velocities[i][0]
        y_vel = velocities[i][1]

        x_pos = x_pos + x_vel
        y_pos = y_pos + y_vel

        x_pos = x_pos % 101
        y_pos = y_pos % 103
        positions[i] = [x_pos, y_pos]

    if count >= 500:
        grid = []
        for i in range(103):
            row = [' '] * 101
            grid.append(row)



        for position in positions:
            if grid[position[1]][position[0]] == ' ':
                grid[position[1]][position[0]] = 1
            else:
                grid[position[1]][position[0]] += 1
        
        num_robots = 0
        for i in range(49, 52):
            for j in range(103):
                if grid[j][i] != ' ':
                    num_robots += 1 
        
        if num_robots > 25:
            time.sleep(0.75)
            print("Second: {}".format(count + 1))
            for row in grid:
                string = ""
                for char in row:
                    string += str(char)
                print(string)

#7753