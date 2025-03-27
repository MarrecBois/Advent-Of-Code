#2022 day 5

file = open("2022_day_5.txt")

rows = [[],[],[],[],[],[],[],[],[]]
moves = []
froms = []
tos = []
moving = False
print(rows)

for line in file:
    if len(line) > 1 and line[1] == '1':
        moving = True
        skip = file.readline()
   
    if not moving: 
        for i in range(1, len(line), 4):
            if line[i] != ' ':
                rows[(i-1)//4].append(line[i])
    
    if moving and line[0] != ' ':
        line = line.strip()
        pos_f = line.find('f')
        pos_t = line.find('t')
        
        moves.append(int(line[5: pos_f - 1]))
        froms.append(int(line[pos_f + 5: pos_t - 1]) - 1)
        tos.append(int(line[pos_t + 3:]) - 1)
        
#Part 1 work
#for i in range(0, len(moves)):
    #frm = froms[i]
    #to = tos[i]
    #for j in range(0, moves[i]):
        #value = rows[frm][0]
        #rows[frm].pop(0)
        #rows[to].insert(0, value)

#Part 2 work
for i in range(0, len(moves)):
    frm = froms[i]
    to = tos[i]
    #stack = rows[frm][0:moves[i]]
    #print(stack)
    
    for j in range(0, moves[i]):
        value = rows[frm][moves[i] - j - 1]
        rows[frm].pop(moves[i] - j - 1)
        rows[to].insert(0, value)        
        





answer = ''

for i in range(0, len(rows)):
    answer += rows[i][0]

print(answer)
                    
