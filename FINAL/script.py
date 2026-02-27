import serial as cereal
from csv import *
s = cereal.Serial()
s.baudrate = 115200
s.port = "COM3"
s.open()
file = open("soilmoisture.csv", "w", newline="")
spreadsheet = writer(file)
spreadsheet.writerow(["Iterations", "Soil humidity", "Water level"])
matchInputs = {
    "Iterations": 0,
    "Soil humidity": 1,
    "Water level": 2
}
inputList = []

with open("soilmoisture.csv", "a", newline="") as file:
    while True:
        inputLine = str(s.readline())[2:-6].rstrip()
        print(inputLine)

        inputLine = inputLine.split(": ")
        inputList.append(inputLine[1])
        
        if len(inputList) == 3:
            print(f"Full list: {inputList}")
            spreadsheet = writer(file)
            spreadsheet.writerow(inputList)
            inputList = []