#2024 Day 1
import os

os.chdir("c:/Users/marre/OneDrive/Documents/Advent of Code 2024/Day 2")
file = open("2024_day_2.txt")

#Store all the left and right numbers into 2 lists
reports = []
nums = "0123456789"

for line in file:
    report = line.strip().split(' ')
    
    for i in range(len(report)):
        report[i] = int(report[i])
    reports.append(report)


#Silver Star
# total_valid = 0

# for report in reports:
#     valid = True

#     for i in range(len(report) - 1):
#         diff = report[i] - report[i+1]

#         if i == 0:
#             if diff < 0 and diff > -4:
#                 decreasing = False
#             elif diff > 0 and diff < 4:
#                 decreasing = True
#             else:
#                 valid = False
#                 break
        
#         else:
#             if decreasing and (diff <= 0 or diff > 3):
#                 valid = False
#                 break
#             elif not decreasing and (diff >= 0 or diff < -3):
#                 valid = False
#                 break
    
#     if valid:
#         total_valid += 1

# print(total_valid)

#Gold Star
def validate_report(report):
    ''' Validates a report that can have an item removed '''
    valid = True

    for i in range(len(report) - 1):
        diff = report[i] - report[i+1]

        if i == 0:
            if diff < 0 and diff > -4:
                decreasing = False
            elif diff > 0 and diff < 4:
                decreasing = True
            else:
                valid = False
                break
        
        else:
            if decreasing and (diff <= 0 or diff > 3):
                valid = False
                break
            elif not decreasing and (diff >= 0 or diff < -3):
                valid = False
                break

    return valid


total_valid = 0

for report in reports:
    valid = True

    for i in range(len(report) - 1):
        diff = report[i] - report[i+1]

        if i == 0:
            if diff < 0 and diff > -4:
                decreasing = False
            elif diff > 0 and diff < 4:
                decreasing = True
            else:
                valid = False
                break
        
        else:
            if decreasing and (diff <= 0 or diff > 3):
                valid = False
                break
            elif not decreasing and (diff >= 0 or diff < -3):
                valid = False
                break
    
    if not valid:
        for i in range(len(report)):
            valid = validate_report(report[:i] + report[i+1:])
            if valid:
                break

    if valid:
        total_valid += 1

print(total_valid)