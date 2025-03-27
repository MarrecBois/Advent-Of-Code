#2024 Day 18
import os
import copy
import time
from queue import Queue

os.chdir("c:/Users/marre/OneDrive/Documents/Advent of Code 2024/Day 18 Maze Solver")
file = open("2024_day_18_test.txt")

coords = []
maze = []
q = Queue(-1)
for line in file:
    line = line.strip()
    nums = line.split(',')
    for i in range(2):
        nums[i] = int(nums[i])
    
    coords.append(nums)

for i in range(7):
    row = ['.'] * 7
    maze.append(row)

for i in range(12):
    maze[coords[i][1]][coords[i][0]] = '#'

def is_valid(x, y):
    return not maze[x][y] == '#'

def follow_path():
    x = 0
    y = 1
    return [x, y]

def checkEnd(q):
    


while not checkEnd(q):
    print("hey")



#Main loop part 1
