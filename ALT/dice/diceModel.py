from random import *

def dieRoll(amount, size):
    diceResult = []
    for die in range(amount):
        diceResult.append(randint(1, size))
    return diceResult

def modelRun(amount, size, iterations):
    manyResults = []
    for run in range(iterations):
        output = dieRoll(amount, size)
        manyResults.append([output, sum(output)])
    return manyResults

def probabilityCheck(amount, size, iterations):
    inputMatrix = modelRun(amount, size, iterations)
    allSums = []
    for item in inputMatrix:
        allSums.append(item[1])
    allSums.sort()
    print(allSums)
    return allSums


def test():
    # print(dieRoll(8, 6)) # 3rd-level fireball
    # print(dieRoll(1, 20)) # skill check
    # print(modelRun(2, 6, 4)) # 3rd-level scorching ray
    print(probabilityCheck(3, 10, 2)) # action surge eldritch blast

test()