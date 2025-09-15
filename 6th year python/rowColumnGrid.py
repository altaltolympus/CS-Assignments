cols = 5
rows = 4
for rowIndex in range(rows):
    for colIndex in range(cols): # this loop prints an asterisk in every column
        print("*", end = "")
    print() # this print() function moves down to the next row
print("If cols = 50 and rows = 10, the grid would look like this:")
cols = 50
rows = 10
for rowIndex in range(rows):
    for colIndex in range(cols): # this loop prints an asterisk in every column
        print("*", end = "")
    print()