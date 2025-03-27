#2022 day 6
file = open("2022_day_6.txt")

signal = file.readline().strip()

print(signal)

#section = signal[0:4]
#spot = 4

#while section.count(section[0]) != 1 or section.count(section[1]) != 1 or section.count(section[2]) != 1:
    #spot += 1
    #section = signal[spot-4 : spot]
    
    
section = signal[0:14]
spot = 14

while section.count(section[0]) != 1 or section.count(section[1]) != 1 or section.count(section[2]) != 1 or section.count(section[3]) != 1 or section.count(section[4]) != 1 or section.count(section[5]) != 1 or section.count(section[6]) != 1 or section.count(section[7]) != 1 or section.count(section[8]) != 1 or section.count(section[9]) != 1 or section.count(section[10]) != 1 or section.count(section[11]) != 1 or section.count(section[12]) != 1 or section.count(section[13]) != 1:
    spot += 1
    section = signal[spot-14 : spot]    

print(spot)