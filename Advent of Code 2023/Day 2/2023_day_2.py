# for marrec is dumb

#file = open("2023_day_2.txt")
#all_lines = []


#for line in file:
    #line = line.strip()
    #index = line.find(':')
    #line = line[index+1:]
    #game = line.split(';')

    #all_lines.append(game)

#total = 0
#nums = '0123456789'

#for i in range(1, len(all_lines) + 1):
    #j = 0
    #valid = True
    #greens = []
    #blues = []
    #reds = []
    #while j < len(all_lines[i-1]) and valid:
        #pull = all_lines[i - 1][j]
        #print(pull)
        #if 'green' in pull:
            #green = ''
            #pos = pull.find('green') - 2
            #while pull[pos] in nums:
                #green = pull[pos] + green
                #pos -= 1
            #print(green)
            #if int(green.strip()) > 13:
                #valid = False
                
        #if 'blue' in pull:
            #blue = ''
            #pos = pull.find('blue') - 2
            #while pull[pos] in nums:
                #blue = pull[pos] + blue
                #pos -= 1
            #print(blue)
            #if int(blue.strip()) > 14:
                #valid = False
                
        #if 'red' in pull:
            #red = ''
            #pos = pull.find('red') - 2
            #while pull[pos] in nums:
                #red = pull[pos] + red    
                #pos -= 1
                #print(red)
            #if int(red.strip()) > 12:
                #valid = False      
        #j += 1
    
    #if valid:
        #total += i
        
#print(total)


#PART 2
file = open("2023_day_2.txt")
all_lines = []


for line in file:
    line = line.strip()
    index = line.find(':')
    line = line[index+1:]
    game = line.split(';')

    all_lines.append(game)

total = 0
nums = '0123456789'

for i in range(1, len(all_lines) + 1):
    j = 0
    valid = True
    greens = []
    blues = []
    reds = []
    while j < len(all_lines[i-1]) and valid:
        pull = all_lines[i - 1][j]
        print(pull)
        if 'green' in pull:
            green = ''
            pos = pull.find('green') - 2
            while pull[pos] in nums:
                green = pull[pos] + green
                pos -= 1
            
            greens.append(int(green))
                
        if 'blue' in pull:
            blue = ''
            pos = pull.find('blue') - 2
            while pull[pos] in nums:
                blue = pull[pos] + blue
                pos -= 1
            blues.append(int(blue))
                
        if 'red' in pull:
            red = ''
            pos = pull.find('red') - 2
            while pull[pos] in nums:
                red = pull[pos] + red    
                pos -= 1
            reds.append(int(red))   
        j += 1
    
    power = max(greens) * max(blues) * max(reds)
    total += power
        
print(total)