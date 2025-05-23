import matplotlib.pyplot as plot
from random import * # make lists  of coordinates
x = []
y= []
rand = 0
for tweezers in range(200):
    rand = randint(0,100)
    if (tweezers < 100):
        x.append(rand)
    else:
        y.append(rand)
plot.scatter(x,y)
plot.show()