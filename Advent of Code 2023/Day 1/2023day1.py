#2023 Day 1

file = open("2023_day_1.txt")
all_lines = []


for line in file:
    all_lines.append(line.strip())

total = 0
nums_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
nums_dict = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9
    }




for i in range(0, len(all_lines)):
    #found = False
    #for j in range (0, len(all_lines[i])):
        #line = all_lines[i]
        #if line[j] in '0123456789otfsen':
            #if line[j] not in '123456789':
                #if 'one' in line[j:j+3]
            #last = char
            #print(last)
            #if found == False:
                #first = char
                #print(first)
                #found = True
    line = all_lines[i]
    firstFound = True
    lastFound = True
    end = 1
    begin = len(line) - 1
    while firstFound:
        for num in nums_list:
            if num in line[:end]:
                firstFound = False
                first = str(nums_dict[num])
        end += 1
    
    while lastFound:
        for num in nums_list:
            if num in line[begin:]:
                lastFound = False
                last = str(nums_dict[num])
        begin -= 1
    
    num = int(first+last)
    print(num)
    
    total+= num
        
print(total)