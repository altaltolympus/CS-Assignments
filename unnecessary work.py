import matplotlib.pyplot as plot
from random import *
# random name generator
firstNames = ["john", "joe", "jane", "joan", "jennifer", "terrence"]
lastNames = ["johnson", "joeson", "insertjnamehere", "house", "nic an ghib", "pork"]
fullNames = []
for x in range(6):
    fullNames.append((firstNames[(randint(0,len(firstNames)-1))]) + " " + (lastNames[(randint(0,len(lastNames)-1))]))
# </unnecessarywork>
siblings = [1,2.5,4,3,2.5,2]
plot.bar(fullNames, siblings)
plot.title("Folks and their number of associate siblings")
plot.xlabel("folk")
plot.ylabel("associate")
plot.show()