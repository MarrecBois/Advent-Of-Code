#2024 Day 12
import os
import copy

os.chdir("c:/Users/marre/OneDrive/Documents/Advent of Code 2024/Day 12")
file = open("2024_day_12_test.txt")

grid = []

for line in file:
    line = line.strip()
    row = []
    for char in line:
        row.append(char)

    grid.append(row)

print(grid)