#2024 Day 1
import os

os.chdir("c:/Users/marre/OneDrive/Documents/Advent of Code 2024/Day 3")
file = open("2024_day_3.txt")

#Store all the left and right numbers into 2 lists
lines = []
nums = "0123456789"

#Function to see if the mull operation is valid
def check_for_mul(line, pos, enabled):
    '''
        -> check for first number
        -> if encounter space, return false
        -> check for comma
        -> check for second number
        -> check for final bracket
    '''
    if not enabled:
       return 0

    count = 0
    number1 = ""
    
    while line[pos] in nums:
        count += 1
        number1 = number1 + line[pos]
        pos += 1
    
    if count > 3 or line[pos] != ',':
       return 0
    else:
       count = 0
       number2 = ""
       pos += 1

    while line[pos] in nums:
       count += 1
       number2 = number2 + line[pos]
       pos += 1
    
    if count > 3 or line[pos] != ')':
       return 0
    else:
       return int(number1) * int(number2)

total = 0
enabled = True

for line in file:
    print(line.strip())
    for pos in range(len(line) - 7):
      if line[pos: pos+4] == "do()":
         enabled = True
      elif line[pos: pos+7] == "don't()":
         enabled = False
      elif line[pos: pos+4] == 'mul(':
         total += check_for_mul(line, pos + 4, enabled)

print(total)
