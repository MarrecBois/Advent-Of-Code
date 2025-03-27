#2022 day 2
file = open("2022_day_2.txt")
firsts = []
seconds = []


for line in file:
    firsts.append(line[0])
    seconds.append(line[2])

print(firsts)
print(seconds)
score = 0
for i in range(0, len(firsts)):
    if firsts[i] == 'A':
        if seconds[i] == 'X':
            score += 3
        elif seconds[i] == 'Y':
            score += 4
        else:
            score += 8
    elif firsts[i] == 'B':
        if seconds[i] == 'X':
            score += 1
        elif seconds[i] == 'Y':
            score += 5
        else:
            score += 9
    else:
        if seconds[i] == 'X':
            score += 2
        elif seconds[i] == 'Y':
            score += 6
        else:
            score += 7        
print(score)