from random import *
from matplotlib.pyplot import *
diceNotation = ""

def dieRoll(amount, size):
    diceResult = []
    for die in range(amount):
        diceResult.append(randint(1, size))
    return diceResult

def diceRollLoop(amount, size, iterations):
    manyResults = []
    for run in range(iterations):
        output = dieRoll(amount, size)
        manyResults.append([output, sum(output)])
    diceNotation = f"{amount}d{size} rolled {iterations} time(s)"
    # print(manyResults)
    return manyResults

def probabilityCheck(amount, size, iterations):
    inputMatrix = diceRollLoop(amount, size, iterations)
    allSums = []
    for item in inputMatrix:
        allSums.append(item[1])
    allSums.sort()
    # print(allSums)
    return allSums

def consolidate(list):
    counter = 0
    frequencies = []
    while counter < list[-1]:
        valueFrequency = [counter, 0]
        for item in list:
            if item == counter: valueFrequency[1] += 1
        frequencies.append(valueFrequency)
        counter += 1
    print(frequencies)
    return frequencies

def coordinateify(matrix):
    x = []
    y = []
    for item in matrix:
        x.append(item[0])
        y.append(item[1])
    return [x, y]

def runEverything(amount, size, iterations):
    return coordinateify(consolidate(probabilityCheck(amount, size, iterations)))


def test():
    # print(consolidate(probabilityCheck(3, 10, 1000))) # action surge eldritch blast
    # print(dieRoll(8, 6)) # 3rd-level fireball
    # print(diceRollLoop(2, 6, 4)) # 3rd-level scorching ray   
    # print(probabilityCheck(2, 4, 100)) # greatclub attack
    # print(f"\n{runEverything(15, 8, 1000000)}") # finger of death
    output = runEverything(2, 6, 1000000)
    print(output)
    # scatter(output[0], output[1])
    plot(output[1], marker=".")
    show()

test()