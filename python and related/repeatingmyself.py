import random
randomNumbers = []
for x in range(100):
    randomNumbers.append(random.randint(-100,100))
csv = open("repeatingmyself.csv", "w")
randomString = ",".join(str(e) for e in randomNumbers)
csv.write(randomString)
csv.close()