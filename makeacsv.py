import random # weee generate a random list
values = []
for x in range(20):
    values.append(random.randint(-100,100))
spreadsheet = open("interestingspreadsheet.csv", "w")
spreadsheet.write(str(values))
values.sort(reverse=True)
print(f"the highest one is {values[0]}\nthe lowest one is {values[-1]}")