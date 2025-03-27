file = open("2023_day_3.txt")
rows = []
nums = '0123456789'

for line in file:
    row = []
    text = line.strip()
    for char in text:
        row.append(char)
    
    rows.append(row)
    
total = 0

#for i in range(0, len(rows)):
    #row = rows[i]
    #checked = []
    
    #for j in range(0, len(row)):
        
        #if row[j] in nums and j not in checked:
            #number = ''
            #end = False
            #k = j
            #while k < len(row) and not end:
                
                #if row[k] in nums:
                    #checked.append(k)
                    #number += row[k]
                    #k += 1
                #else:
                    
                    #end = True
                    
            #k -= 1
            
            #foundSymbol = False
            
            #rowStart = i - 1
            #rowEnd = i + 1
            #colStart = j - 1
            #colEnd = k + 1
            
            #if i == 0:
                #rowStart = i
            #elif i == len(rows) - 1:
                #rowEnd = i
            #if j == 0:
                #colStart = j
            #elif k == len(row) - 1:
                #colEnd = j
                
                
            #for check1 in range(rowStart, rowEnd + 1):
                #for check2 in range(colStart, colEnd + 1):
                    #if rows[check1][check2] != '.' and rows[check1][check2] not in nums:
                        #foundSymbol = True
                        
            ##if i == 0:
                ##if j == 0:
                    ##for check in range(j, k + 2):
                        ##if rows[i+1][check] != '.':
                            ##foundSymbol = True
                    
                    ##if rows[i][k+1] != '.':
                        ##foundSymbol = True
                
                ##elif k == len(row) - 1:
                    ##for check in range(j - 1, k + 1):
                        ##if rows[i+1][check] != '.':
                            ##foundSymbol = True
                    
                    ##if rows[i][j - 1] != '.':
                        ##foundSymbol = True            
                
                ##else:
                    ##for check in range(j - 1, k + 2):
                        ##if rows[i+1][check] != '.':
                            ##foundSymbol = True
                    
                    ##if rows[i][k+1] != '.' or rows[i][j - 1] != '.':
                        ##foundSymbol = True                    
            
            ##elif i == len(rows) - 1:
                ##if j == 0:
                    ##for check in range(j, k + 2):
                        ##if rows[i-1][check] != '.':
                            ##foundSymbol = True
                    
                    ##if rows[i][k+1] != '.':
                        ##foundSymbol = True
                
                ##elif k == len(row) - 1:
                    ##for check in range(j - 1, k + 1):
                        ##if rows[i-1][check] != '.':
                            ##foundSymbol = True
                    
                    ##if rows[i][j - 1] != '.':
                        ##foundSymbol = True            
                
                ##else:
                    ##for check in range(j - 1, k + 2):
                        ##if rows[i-1][check] != '.':
                            ##foundSymbol = True
                    
                    ##if rows[i][k+1] != '.' or rows[i][j - 1] != '.':
                        ##foundSymbol = True     
            
            ##elif j == 0:
                ##for check in range(j, k+2):
                    ##if rows[i-1][check] != '.' or rows[i+1][check] != '.':
                        ##foundSymbol = True
                
                ##if rows[i][k+1] != '.':
                    ##foundSymbol = True       
        
            ##elif k == len(rows) - 1:
                ##for check in range(j - 1, k+1):
                    ##if rows[i-1][check] != '.' or rows[i+1][check] != '.':
                        ##foundSymbol = True
                
                ##if rows[i][j - 1] != '.':
                    ##foundSymbol = True              
            
            ##else:
                ##for check in range(j - 1, k + 2):
                    ##if rows[i-1][check] != '.' or rows[i+1][check] != '.':
                        ##foundSymbol = True
                ##if rows[i][j-1] != '.' or rows[i][k+1] != '.':
                    ##foundSymbol = True
                        
                    
                
            #if foundSymbol:
                #total += int(number)
                #print(number)

        
##while pull[pos] in nums:
    ##blue = pull[pos] + blue
    ##pos -= 1
    
#print(total)
gearDict = {}
for i in range(0, len(rows)):
    for j in range(0, len(row)):
        if rows[i][j] == '*':
            gearDict[str(i) + str(j)] = []
            
print(gearDict)
        

for i in range(0, len(rows)):
    row = rows[i]
    checked = []
    
    for j in range(0, len(row)):
        
        if row[j] in nums and j not in checked:
            number = ''
            end = False
            k = j
            while k < len(row) and not end:
                
                if row[k] in nums:
                    checked.append(k)
                    number += row[k]
                    k += 1
                else:
                    
                    end = True
                    
            k -= 1
            
            foundSymbol = False
            
            rowStart = i - 1
            rowEnd = i + 1
            colStart = j - 1
            colEnd = k + 1
            
            if i == 0:
                rowStart = i
            elif i == len(rows) - 1:
                rowEnd = i
            if j == 0:
                colStart = j
            elif k == len(row) - 1:
                colEnd = j
                
                
            for check1 in range(rowStart, rowEnd + 1):
                for check2 in range(colStart, colEnd + 1):
                    if rows[check1][check2] == '*':
                        gearDict[str(check1) + str(check2)].append(int(number))

for key in gearDict:
    if len(gearDict[key]) == 2:
        total += (gearDict[key][0] * gearDict[key][1])
    
    
print(gearDict)
print(total)