# this bit sets up the list that will have things removed from it
import random
longList = []
for x in range(100):
    longList.append(random.randint(-100,100))
print(longList)
#this bit does the actual task
listCounter = 0
# for item in longList:
while listCounter < len(longList):
    if longList[listCounter] < 0:
        print(f"{longList[listCounter]} was marked to be removed from the list")
        longList.remove(longList[listCounter])
    else:
        print(f"{longList[listCounter]} was not removed from the list")
        listCounter += 1
print(longList)
#this bit checks if i fucked up
errors = 0
for item in longList:
    if item < 0:
        errors += 1
print(f"{errors} erroneous values were skipped.", end=" ")
print("ya numpty.") if errors > 1 else print("good job.")