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
DANGER_HUMID = 70 # Simulated thresholds to represent when there is danger of a flood
DANGER_WATER = 100
floodLevel = 0
FLOOD_LEVELS = ("None", "Risk", "In progress", "Simulation")


while True:
    with open("soilmoisture.csv", "a", newline="") as file:
        inputLine = str(s.readline())[2:-6].rstrip()
        print(inputLine)
        if inputLine.lower().__contains__("floo"): continue

        inputLine = inputLine.split(": ")
        inputList.append(inputLine[1])

        if inputLine[0].lower().__contains__("humidity"):
            if int(inputLine[1]) >= DANGER_HUMID:
                floodLevel += 1
        if inputLine[0].lower().__contains__("water"):
            if int(inputLine[1]) >= DANGER_WATER:
                floodLevel += 1

        if inputLine[0].lower().__contains__("simulated"):
            floodLevel = 3
        

        if len(inputList) == 3:
            inputList.append(FLOOD_LEVELS[floodLevel])
            print(f"Full list: {inputList}")

            spreadsheet = writer(file)
            spreadsheet.writerow(inputList)

            inputList = []
            floodLevel = 0