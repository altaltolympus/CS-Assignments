from urllib.request import *
import serial as cereal
s = cereal.Serial()
s.baudrate = 115200
s.port = "COM3"
s.open()

# number = input("Enter a number: ")
# number = str(number)
# b = urlopen(f"https://api.thingspeak.com/update?api_key=RZPSWIF804S0FTLS&field1={number}")
# print("number sent!")
# print(number)
while True:
    temp = str(s.readline())
    send = urlopen(f"https://api.thingspeak.com/update?api_key=RZPSWIF804S0FTLS&field1={temp}")
    print(temp)