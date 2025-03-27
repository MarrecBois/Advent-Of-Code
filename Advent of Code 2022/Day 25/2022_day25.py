#2022 Day 25
import math;
file = open("2022_day_25.txt")
rows = []


for line in file:
    rows.append(line.strip())
    
    
#total = 0
##for row in rows:
    ##for i in range(len(row) - 1, -1, -1):
        ##if row[i] == '=':
            ##total -= 2* (5**i)
        ##elif row[i] == '-':
            ##total -= 5**i
        ##else: 
            ##mult = int(row[i])
            ##total += mult * 5**i

##print(total)
    

total = 0
for row in rows:
    rowsum = 0
    for i in range(len(row) - 1, -1, -1):
        if row[len(row) - i - 1] == '=':
            rowsum -= 2* (5**i)
        elif row[len(row) - i - 1] == '-':
            rowsum -= 5**i
        else:
            mult = int(row[len(row) - i - 1])
            rowsum += mult * 5**i
    total += rowsum

print(total)

startingPower = math.ceil(math.log(total) / math.log(5))
result = ""

def numberToBase(n, b):
    if n == 0:
        return [0]
    digits = []
    while n:
        digits.append(int(n % b))
        n //= b
    return digits[::-1]


print(numberToBase(total, 5))