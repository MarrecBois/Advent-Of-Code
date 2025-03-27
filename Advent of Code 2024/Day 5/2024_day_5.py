#2024 Day 5
import os

os.chdir("c:/Users/marre/OneDrive/Documents/Advent of Code 2024/Day 5")
file = open("2024_day_5.txt")

orders = []
updates = []
firsts = []
is_order = True
numbers = "0123456789"

for line in file:
    if line[0] not in numbers:
        is_order = False
    elif is_order:
        line = line.strip()
        order = line.split('|')
        for i in range(len(order)):
            order[i] = int(order[i])
        
        firsts.append(order[0])
        orders.append(order)

    else:
        line = line.strip()
        update = line.split(',')
        for i in range(len(update)):
            update[i] = int(update[i])
        
        updates.append(update)


#Silver star
# print(orders)
# print(updates)
# total = 0

# for update in updates:
#     isValid = True

#     for pos in range(len(update)):
#         for order in orders:
#             if update[pos] == order[1]:
#                 if update.count(order[0]) == 1 and update[:pos].count(order[0]) == 0:
#                     isValid = False

    
#         if not isValid:
#             break
    
#     if isValid:
#         total += update[len(update)//2]

# print(total)


#gold star
total = 0
invalidUpdates = []
for update in updates:
    isValid = True

    for pos in range(len(update)):
        for order in orders:
            if update[pos] == order[1]:
                if update.count(order[0]) == 1 and update[:pos].count(order[0]) == 0:
                    isValid = False

    
        if not isValid:
            break
    
    if not isValid:
        invalidUpdates.append(update)

#Fix the invalid updates, then add the middle one
for update in invalidUpdates:
    positions = {}
    for i in range(len(update)):
        number = update[i]
        positions[number] = len(update) - 1
        for j in range(len(update)):
            if i != j and [update[i], update[j]] in orders:
                positions[number] = positions[number] - 1
        
    
    for i in range(len(update)):
        if positions[update[i]] == len(update) // 2:
            total += update[i]




print(total)