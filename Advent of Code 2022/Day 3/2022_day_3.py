#2022 day 3

#file = open("2022_day_3.txt")
#first_half = []
#second_half = []


#for line in file:
    #print(len(line.strip()))
    #print(line)
    #print(len(line.strip())/2)
    #first_half.append(line[0:len(line.strip())//2])
    #second_half.append(line[len(line.strip())//2:])

#print(first_half)
#print(second_half)
#string = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
#finals = ''
#for i in range(0, len(first_half)):
    #for j in range(0, len(first_half[i])):
        #if first_half[i][j] in second_half[i]:
            #finals += first_half[i][j]
            #break
            
#score = 0
#for i in range(0, len(finals)):
    #pos = string.find(finals[i])
    #score += pos + 1

#print(finals)
#print(score)

file = open("2022_day_3.txt")
all_lines = []
firsts = []
seconds = []
thirds = []


for line in file:
    all_lines.append(line.strip())

firsts.append(all_lines[0])
for i in range(1, len(all_lines)):
    if i % 3 == 1:
        seconds.append(all_lines[i])
    elif i % 3 == 2:
        thirds.append(all_lines[i])
    else:
        firsts.append(all_lines[i])

finals = ''
for i in range(0, len(firsts)):
    for j in range(0, len(firsts[i])):
        if firsts[i][j] in seconds[i] and firsts[i][j] in thirds[i]:
            finals += firsts[i][j]
            break





string = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'


score = 0
for i in range(0, len(finals)):
    pos = string.find(finals[i])
    score += pos + 1

print(finals)
print(score)