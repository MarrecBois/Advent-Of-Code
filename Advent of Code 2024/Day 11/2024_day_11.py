#2024 day 11

text = "9759 0 256219 60 1175776 113 6 92833"

stones = text.split(" ")

print(stones)

stone_dict = {}
for stone in stones:
    if stone not in stone_dict:
        stone_dict[stone] = 1
    else:
        stone_dict[stone] += 1

for i in range(75):
    changes = {}
    for key in list(stone_dict.keys()):
        if key == '0':
            if '1' in changes:
                changes['1'] += stone_dict[key]
            else:
                changes['1'] = stone_dict[key]
            if '0' in changes:
                changes['0'] -= stone_dict[key]
            else:
                changes['0'] = -stone_dict[key]

        elif len(key) % 2 == 0:
            half = len(key) // 2
            first_half = key[:half]

            if first_half in changes:
                changes[first_half] += stone_dict[key]
            else:
                changes[first_half] = stone_dict[key]
            
            if key in changes:
                changes[key] -= stone_dict[key]
            else:
                changes[key] = -stone_dict[key]

            second_half = key[half:]
            while second_half[0] == '0' and len(second_half) > 1:
                second_half = second_half[1:]
            
            if second_half in changes:
                changes[second_half] += stone_dict[key]
            else:
                changes[second_half] = stone_dict[key]
            
        else:
            multiplied = str(int(key) * 2024)
            if multiplied not in changes:
                changes[multiplied] = stone_dict[key]
            else:
                changes[multiplied] = changes[multiplied] + stone_dict[key]
            
            if key in changes:
                changes[key] -= stone_dict[key]
            else:
                changes[key] = -stone_dict[key]
    
    for key in list(changes.keys()):
        if key in stone_dict:
            stone_dict[key] += changes[key]
        else:
            stone_dict[key] = changes[key]
        

    print(i)
    print(stone_dict)

count = 0
for key in stone_dict:
    count += stone_dict[key]

print(count)