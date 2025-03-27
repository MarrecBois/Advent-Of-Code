#2024 Day 13
import os
import copy

os.chdir("c:/Users/marre/OneDrive/Documents/Advent of Code 2024/Day 13")
file = open("2024_day_13.txt")

a_buttons = []
b_buttons = []
prizes = []

for line in file:
    line = line.strip()
    if line == "":
        pass
    elif line[0] == 'B':
        pos1 = line.find('+')
        pos2 = line.find('+', pos1 + 1)

        pos1 += 1
        first_num = ''
        while line[pos1] != ',':
            first_num += line[pos1]
            pos1 += 1
        
        pos2 += 1
        second_num = ''
        while pos2 < len(line):
            second_num += line[pos2]
            pos2 += 1
        
        first_num = int(first_num)
        second_num = int(second_num)
        if line[7] == 'A':
            a_buttons.append([first_num, second_num])
        else:
            b_buttons.append([first_num, second_num])
        
    elif line[0] == 'P':
        pos1 = line.find('=')
        pos2 = line.find('=', pos1 + 1)

        pos1 += 1
        first_num = ''
        while line[pos1] != ',':
            first_num += line[pos1]
            pos1 += 1
        
        pos2 += 1
        second_num = ''
        while pos2 < len(line):
            second_num += line[pos2]
            pos2 += 1

        first_num = int(first_num) + 10000000000000
        second_num = int(second_num) + 10000000000000
        prizes.append([first_num, second_num])


# print(a_buttons)
# print(b_buttons)
# print(prizes)
# total = 0
# for i in range(len(prizes)):
#     ax = a_buttons[i][0]
#     ay = a_buttons[i][1]
#     bx = b_buttons[i][0]
#     by = b_buttons[i][1]
#     prizex = prizes[i][0]
#     prizey = prizes[i][1]
#     options = []

#     count = 0
#     while count <= 100 and count * ax <= prizex and count * ay <= prizey:
#         leftover_x = prizex - count * ax
#         leftover_y = prizey - count * ay

#         if leftover_x // bx == leftover_y // by and leftover_x % bx == 0 and leftover_x // bx <= 100:
#             options.append(3*count + (leftover_x//bx))
        
#         count += 1
    
#     if len(options) > 0:
#         print(options)
#         print(min(options))
#         total += min(options)

# print(total)


total = 0
for i in range(len(prizes)):
    ax = a_buttons[i][0]
    ay = a_buttons[i][1]
    bx = b_buttons[i][0]
    by = b_buttons[i][1]
    prizex = prizes[i][0]
    prizey = prizes[i][1]
    options = []

    determinant = ax * by - ay * bx

    det1 = prizex * by - prizey * bx
    det2 = ax*prizey - ay * prizex

    if det1 // determinant == det1/determinant and det2// determinant == det2/determinant:
        total += (3*det1//determinant + det2//determinant)
    

print(f"Final total: {total}")
