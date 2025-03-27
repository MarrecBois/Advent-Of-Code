#2024 Day 7
import os
import copy

os.chdir("c:/Users/marre/OneDrive/Documents/Advent of Code 2024/Day 7")
file = open("2024_day_7.txt")

results = []
operands = []

for line in file:
    line = line.strip()
    pos = line.find(":")
    results.append(int(line[:pos]))

    operand_part = line[pos + 1:].strip()
    operands_strings = operand_part.split(' ')
    for i in range(len(operands_strings)):
        operands_strings[i] = int(operands_strings[i])
    
    operands.append(operands_strings)

# output = 0

# for i in range(len(results)):
#     length = len(operands[i]) - 1
#     options = [[0] * length for _ in range(2 ** length)]  # Fix here


#     for j in range(len(options)):
#         for check in range(1, length + 1):
#             if j % (2**check) >= 2**(check - 1):
#                 options[j][check-1] = 1
#             else:
#                 options[j][check-1] = 0
    
#     valid = False

#     for j in range(len(options)):
#         attempt = options[j]
#         total = operands[i][0]

#         for op in range(len(attempt)):
#             if attempt[op] == 0:
#                 total += operands[i][op + 1]
#             elif attempt[op] == 1:
#                 total *= operands[i][op + 1]
#             else:
#                 first_half = str(total)
#                 second_half = str(operands[i][op + 1])
#                 total = int(first_half + second_half)
        
#         if total == results[i] and not valid:
#             output += total
#             valid = True

# print(output)



#Part 2
output = 0

for i in range(len(results)):
    length = len(operands[i]) - 1
    options = [[0] * length for _ in range(3 ** length)]  # Fix here


    for j in range(len(options)):
        for check in range(1, length + 1):
            if j % (3**check) >= 2 * 3**(check - 1):
                options[j][check-1] = 2
            elif j % (3**check) >= 3**(check - 1):
                options[j][check - 1] = 1
            else:
                options[j][check-1] = 0
    
    valid = False

    for j in range(len(options)):
        attempt = options[j]
        total = operands[i][0]

        for op in range(len(attempt)):
            if attempt[op] == 0:
                total += operands[i][op + 1]
            elif attempt[op] == 1:
                total *= operands[i][op + 1]
            else:
                first_half = str(total)
                second_half = str(operands[i][op + 1])
                total = int(first_half + second_half)
        
        if total == results[i] and not valid:
            output += total
            valid = True
            print(output)

print(output)
