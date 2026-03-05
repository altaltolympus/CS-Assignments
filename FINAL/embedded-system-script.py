"""
This is the source code for the embedded system I made as part of my project.
It will not run in a normal command line, and must be used with the MakeCode micro:bit IDE in order to work.
I add it here for the purpose of keeping it safe and allowing any who wish to use and edit it.
"""

active = False

def alarm():
    led.plot(4,0)
    music.play(music.create_sound_expression(WaveShape.SINE,
            5000,
            0,
            255,
            255,
            500,
            SoundExpressionEffect.NONE,
            InterpolationCurve.LINEAR),
        music.PlaybackMode.IN_BACKGROUND)
    led.unplot(4,0)

def toggleScreen():
    global active
    active = not active
    print(active)
    led.enable(active)
input.on_button_pressed(Button.A, toggleScreen)

def statusBar(envInput, y):
    fullLeds = envInput // 20
    for x in range(5):
        led.plot_brightness(x, y, 255) if x < fullLeds else led.unplot(x, y)
    lastBrightness = envInput % 20
    if lastBrightness > 0:
        led.plot_brightness(fullLeds, y, lastBrightness * 12.75)

def spamStatusBar(amount):
    for x in range(amount):
        humid = Environment.read_soil_humidity(AnalogPin.P2)
        statusBar(humid, 2)
        water = Environment.read_water_level(AnalogPin.P1)
        statusBar(alterCap(water, 70, 100), 4)
        basic.pause(100)

counter = 0
humid = 0
water = 0

def alterCap(var, currentCap, newCap):
    return var / currentCap * newCap

DANGER_HUMID = 100
DANGER_WATER = 70

unflood = False
floodIterations = 0

def incrementSim():
    global humid, water, unflood, floodIterations

    if humid < 100 and not unflood: # Check if conditions are right for the flood to continue increasing
        humid += 10
        water += 10

    elif humid > 0 and unflood: # Check if the flood is finished increasing or has run its course already
        print("Flood receding...")
        humid -= 10
        water -= 10
        if humid == 0:
            flood = False # exit flood simulation once levels return to zero
            print("The flood is ended")

    statusBar(humid, 2) # Update bars to match simulated values (NOT WORKING)
    statusBar(alterCap(water, 70, 100), 4) 
    floodIterations += 1
       
    if humid == 100: unflood = True
    basic.pause(250)

flood = False

def beginFlood():
    global flood, unflood, humid, water, floodIterations

    floodIterations = 0
    humid = 10
    water = 10
    spamStatusBar(1)
    print("Flood simulation beginning...")
    flood = True
    unflood = False

input.on_button_pressed(Button.B, beginFlood)

while True:
    for x in range(5):
        led.unplot(2, x)
    if active:
        
        if flood:
            serial.write_line("FLOOD!!")
            serial.write_line("Sumlation iterations: " + floodIterations)
            serial.write_line("Simulated humidity: " + humid)
            serial.write_line("Simulated water level: " + water)
            incrementSim()
            if humid == 0 and unflood:
                flood= False
                unflood = False
            serial.write_line("Flood simulation ending...")
        else: 
            spamStatusBar(5)
            led.plot(0, 0)
            humid = Environment.read_soil_humidity(AnalogPin.P2)
            water = Environment.read_water_level(AnalogPin.P1)
            spamStatusBar(5)

            serial.write_line("Iterations: " + counter)
            serial.write_line("Soil humidity: " + str(humid))
            serial.write_line("Water level: " + str(water))

            counter += 1

        led.plot(2, 0) if humid >= DANGER_HUMID or water >= DANGER_WATER else led.unplot(2, 0)
        if humid >= DANGER_HUMID and water >= DANGER_WATER:
            alarm()
        

            

        led.unplot(0, 0)
    else: 
        basic.pause(500)
        print("inactive")


    