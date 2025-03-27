#2022 day 8

def check_row(row, pos):
    '''
    Insert docstring here
    '''
    left = False
    right = False
    
    if row[pos] == max(row[:pos + 1]) and row[:pos + 1].count(row[pos]) == 1:
        left = True
    
    if row[pos] == max(row[pos:]) and row[pos:].count(row[pos]) == 1:
        right = True
    
    return left or right

def check_column(col, pos):
    '''
    insert docstring
    '''

    up = False
    down = False

    
    if col[pos] == max(col[:pos + 1]) and col[:pos + 1].count(col[pos]) == 1:
        up = True
    
    if col[pos] == max(col[pos:]) and col[pos:].count(col[pos]) == 1:
        down = True    
    
    return up or down

def left_score(row, pos):
    new_row = row[:pos + 1]
    new_row.reverse()
    view = 1
    if len(new_row) == 1:
        return 0
    
    while new_row[view] < row[pos]:
        view += 1
        if view == len(new_row):
            return view
    return view

def right_score(row, pos):
    new_row = row[pos:]
    view = 1
    if len(new_row) == 1:
        return 0
    
    while new_row[view] < row[pos]:
        view += 1
        if view == len(new_row):
            return view
    return view


def up_score(col, pos):
    new_col = col[:pos + 1]
    new_col.reverse()
    view = 1
    if len(new_col) == 1:
        return 0
    
    while new_col[view] < col[pos]:
        view += 1
        if view == len(new_col):
            return view
    return view
    

def down_score(col, pos):
    new_col = col[pos:]
    view = 1
    if len(new_col) == 1:
        return 0
    
    while new_col[view] < col[pos]:
        view += 1
        if view == len(new_col):
            return view
    return view    

    
def scenic_score(row, col, row_pos, col_pos):
    left = left_score(row, row_pos)
    right = right_score(row, row_pos)
    up = up_score(col, col_pos)
    down = down_score(col, col_pos)
    return left * right * up * down



file = open("2022_day_8_test.txt")
row = 1
columns = []
rows = [[]]
line_1 = file.readline().strip()

for i in range(0, len(line_1)):
    columns.append([])
    rows[0].append(int(line_1[i]))
    columns[i].append(int(line_1[i]))


for line in file:
    line = line.strip()
    rows.append([])
    for i in range(0, len(line)):
        columns[i].append(int(line[i]))
        rows[row].append(int(line[i]))
    row += 1

#Part 1
#count = 0
#for row in range(0, len(rows)):
    #for col in range(0, len(columns)):
        
        #horiz_check = check_row(rows[row], col)
        #vert_check = check_column(columns[col], row)
        
        #if horiz_check or vert_check:
            #count += 1
            
#print(count)

#part 2
all_scores = []
for row in range(0, len(rows)):
    for col in range(0, len(columns)):
        if row == 1 and col == 2:
            print(left_score(rows[row], col))
            print(right_score(rows[row], col))
            print(up_score(columns[col], row))
            print(down_score(columns[col], row))
            print()
            print()
        if row == 3 and col == 2:
            print(left_score(rows[row], col))
            print(right_score(rows[row], col))
            print(up_score(columns[col], row))
            print(down_score(columns[col], row))
        score = scenic_score(rows[row], columns[col], col, row)
        all_scores.append(score)

print(max(all_scores))