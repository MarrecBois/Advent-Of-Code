file = open("2022_day_4.txt")
pair_1 = []
pair_2 = []


for line in file:
    line = line.strip()
    pos = line.find(',')
    pair_1.append(line[:pos])
    pair_2.append(line[pos + 1:])
                  
print(pair_1)
print(pair_2)
group_1 = []
group_2 = []
count = 0

for i in range(0, len(pair_1)):
    pos_1 = pair_1[i].find('-')
    beginning = int(pair_1[i][:pos_1])
    end = int(pair_1[i][pos_1 +1:])
    a = []
    for j in range(beginning, end+1):
        a.append(j)
    group_1.append(a)
    
    pos_2 = pair_2[i].find('-')
    beginning = int(pair_2[i][:pos_2])
    end = int(pair_2[i][pos_2 + 1:])
    b = []
    for j in range(beginning, end+1):
        b.append(j)
    group_2.append(b)    

#for i in range(0, len(group_1)):
    #if len(group_1[i]) > len(group_2[i]):
        #good = 0
        #for j in range(0, len(group_2[i])):
            
            #if group_2[i][j] in group_1[i]:
                #good += 1
        #if good == len(group_2[i]):
          
            #count += 1
    
    #else:
        #good = 0
        #for j in range(0, len(group_1[i])):
            
            #if group_1[i][j] in group_2[i]:
                #good += 1
                
        #if good == len(group_1[i]):
            #count += 1     

for i in range(0, len(group_1)):
    if len(group_1[i]) > len(group_2[i]):
        good = True
        for j in range(0, len(group_2[i])):
            
            if group_2[i][j] in group_1[i] and good:
                print(group_2[i])
                count += 1
                good = False
            
            
       
    
    else:
        good = True
        for j in range(0, len(group_1[i])):
            
            if group_1[i][j] in group_2[i] and good:
                print(group_1[i])
                count += 1
                good = False
            
 


print(count)
    
    
#for i in range(1, len(all_lines)):
    #if i % 3 == 1:
        #seconds.append(all_lines[i])
    #elif i % 3 == 2:
        #thirds.append(all_lines[i])
    #else:
        #firsts.append(all_lines[i])