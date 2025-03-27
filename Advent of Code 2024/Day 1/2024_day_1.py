#2024 Day 1
import os

os.chdir("c:/Users/marre/OneDrive/Documents/Advent of Code 2024/Day 1")
file = open("2024_day_1.txt")

#Store all the left and right numbers into 2 lists
lefts = []
rights = []
nums = "0123456789"

for line in file:
    pos = 0
    number = ""
    while line[pos] in nums:
        number = number + line[pos]
        pos += 1
    
    lefts.append(int(number))
    
    while line[pos] not in nums:
        pos += 1
    
    number = line[pos:].strip()
    
    rights.append(int(number))
    

print("Left array: {}".format(lefts))
print("Right array: {}".format(rights))

lefts.sort()
rights.sort()

#Silver Star
# total = 0
# for i in range(len(rights)):
#     total += (abs(lefts[i] - rights[i]))

# print(total)

#Gold Star
total = 0
for i in range(len(rights)):
    total += lefts[i] * rights.count(lefts[i])

print(total)