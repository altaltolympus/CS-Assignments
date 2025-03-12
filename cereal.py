import serial as cereal
s =  cereal.Serial()
s.baudrate = 115200
s.port = "COM3"
s.open()
while True:
    compass = (str(s.readline())[2:][:-31])
    print(compass)