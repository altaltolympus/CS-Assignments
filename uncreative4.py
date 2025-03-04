randomList = open("repeatingmyself.csv", "r")
csvString = randomList.read()
csvList = csvString.split(",")
print(csvList)
integers = [int(item) for item in csvList]
print(integers)
integers.sort()
print(integers)