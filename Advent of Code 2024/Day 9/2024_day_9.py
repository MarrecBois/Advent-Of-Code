#2024 Day 9
import os
import copy

os.chdir("c:/Users/marre/OneDrive/Documents/Advent of Code 2024/Day 9")
file = open("2024_day_9.txt")

for line in file:
    text = line.strip()

numbers = []
spaces = []
memory = []

for i in range(len(text)):
    if i % 2 == 0:
        numbers.append(int(text[i]))
        for j in range(numbers[-1]):
            memory.append(i//2)
    else:
        spaces.append(int(text[i]))
        for j in range(spaces[-1]):
            memory.append('.')

print(memory)
#Now reshuffle everything to get rid of the empty space!
'''
Find the first non '.' from the right...
Save that index
Find the first '.' from the left
if second index > first then exit...
otherwise swap them
'''
# isSpace = True
# while isSpace:
#     num_check = -1
#     while memory[num_check] == '.':
#         num_check -= 1
    
#     num_check = len(memory) + num_check
#     space_check = 0
#     while memory[space_check] != '.':
#         space_check += 1

#     if space_check > num_check:
#         isSpace = False
#     else:
#         memory[space_check] = memory[num_check]
#         memory[num_check] = '.'


#Part 2 loop
'''
Get the index of the first number from the left...
Add that number to a list of numbers to avoid...
if not in that list, check how many spaces it needs (size)
from the left and check if there is a space big enough to move it
check until etiher you find a space OR index > the index of the number ur moving
'''
for number in range(len(numbers) - 1, -1, -1):
    index = memory.index(number)
    other_end = index
    while other_end < len(memory) and memory[other_end] == number:
        other_end += 1
    
    size = other_end - index

    found_space = False
    check = 0
    while not found_space and check < index:
        if memory[check] == '.':
            count = 1
            check += 1
            while memory[check] == '.' and count != size:
                 count += 1
                 check += 1
                
            if count == size:
                found_space = True
                check -= 1
                for i in range(size):
                    memory[check - i] = number
                    memory[index + i] = '.'

        else:
            check += 1
    
    print(memory)

print(memory)

        

#Calculate the checksum
pos = 0
total = 0
for pos in range(len(memory)):
    if memory[pos] != '.':
        total += pos * memory[pos]
        pos += 1

print(total)