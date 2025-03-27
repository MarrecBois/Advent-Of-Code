#2023 day 5 a)

file = open("2023_day_5.txt")
destinations = []
sources = []
ranges = []
starting = file.readline()

print(starting)
nums = '0123456789'

for line in file:
    print(line)
    if line[0] not in nums:
        destinations.append("x")
        sources.append("x")
        ranges.append("x")
    
    else:
        text = line.strip()
        pos1 = text.find(' ')
        pos2 = text.find(' ', pos1 + 1)
        
        dest = int(text[:pos1])
        source = int(text[pos1 + 1: pos2])
        rang = int(text[pos2 + 1:])
    
        destinations.append(dest)
        sources.append(source)
        ranges.append(rang)
    
print(destinations)
print(sources)
print(ranges)