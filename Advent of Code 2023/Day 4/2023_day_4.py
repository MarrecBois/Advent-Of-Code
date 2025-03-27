#2023 Day 4

file = open("2023_day_4.txt")
winningNumbers = []
cardNumbers = []
numScratches = []

for line in file:
    
    text = line.strip()
    pos1 = text.find(':')
    text = text[pos1 + 1:]
    pos2 = text.find('|')
    
    winningNumbers.append(text[:pos2].strip().split(' '))
    cardNumbers.append(text[pos2 + 1:].strip().split(' '))
    
#for num in winningNumbers:
    #print(num)
    #numScratches.append(1)
    
#for num in cardNumbers:
    #print(num)

total = 0

for num in winningNumbers:
    numScratches.append(1)
    for check in num:
        if check == '':
            num.remove(check)

            
print(numScratches)
            
for i in range(len(cardNumbers)):
    points = 0
    card = cardNumbers[i]
    winning = winningNumbers[i]
    for j in range(len(card)):
        if card[j] in winning:
            points += 1
    
    for k in range(i + 1, i + points + 1):
        if k < len(numScratches):
            numScratches[k] += numScratches[i]

print(sum(numScratches))