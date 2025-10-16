from csv import *
newCar = ["Polestar", "4", "221-WW-8901"]
file = open("myGarage.csv", "a", newline="\n")
garage = writer(file)
garage.writerow(newCar)