#2022 day 1

file = open("2022_day_1.txt")
all_nums = []
elf = []


for line in file:
    if line[0] in '123456789':
        elf.append(int(line.strip()))
    else: 
        all_nums.append(sum(elf))
        elf = []
    

print(all_nums)

all_nums.sort()
all_nums.reverse()
print(all_nums)
print(max(all_nums))

print(all_nums[0] + all_nums[1] + all_nums[2])
