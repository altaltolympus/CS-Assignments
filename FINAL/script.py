import serial as cereal
from csv import *
s = cereal.Serial()
s.baudrate = 115200
s.port = "COM3"
s.open()
file = open("soilmoisture.csv", "w", newline="")
spreadsheet = writer(file)
spreadsheet.writerow(["Iterations", "Soil humidity", "Water level", "Flood status"])
inputList = []
DANGER_HUMID = 100
DANGER_WATER = 100
floodLevel = 0
FLOOD_LEVELS = ("None", "Imminent", "In progress")


while True:
    with open("soilmoisture.csv", "a", newline="") as file:
        inputLine = str(s.readline())[2:-6].rstrip()
        print(inputLine)

        inputLine = inputLine.split(": ")
        inputList.append(inputLine[1])

        if inputLine[0].lower() == "soil humidity":
            if int(inputLine[1]) >= DANGER_HUMID:
                floodLevel += 1
        if inputLine[0].lower() == "water level":
            if int(inputLine[1]) >= DANGER_WATER:
                floodLevel += 1

        inputList.append(FLOOD_LEVELS[floodLevel])
        
        
        if len(inputList) == 4:
            print(f"Full list: {inputList}")
            spreadsheet = writer(file)
            spreadsheet.writerow(inputList)
            inputList = []