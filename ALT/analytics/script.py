import matplotlib.pyplot as plot
import csv
import statistics as stats
sheet = open("spreadsheet.csv", "r")
data = list(csv.reader(sheet, delimiter=",")) #This gets me the entire file, headings and all, but I only want the data
sheet.close()
#This next section is just a bunch of lists, to which I will add each value from their associated time of day
timeBrackets = ["00:00", "00:30", "01:00", "01:30", "02:00", "02:30", "03:00", "03:30", "04:00", "04:30", "05:00", "05:30", 
                "06:00", "06:30", "07:00", "07:30", "08:00", "08:30", "09:00", "09:30", "10:00", "10:30", "11:00", "11:30", 
                "12:00", "12:30", "13:00", "13:30", "14:00", "14:30", "15:00", "15:30", "16:00", "16:30", "17:00", "17:30", 
                "18:00", "18:30", "19:00", "19:30", "20:00", "20:30", "21:00", "21:30", "22:00", "22:30", "23:00", "23:30"]
timeValues = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
averageEnergyValues = [] # Once the average energy value for each time of day is calculated, it will go here
# The sub-lists are associated with each time bracket; for instance, timeValues[0] is 00:00 - 00:30, timeValues[1] is 00:30 - 01:00 and so on
# time0000 = []
# time0030 = []
# time0100 = []
# time0130 = []
# time0200 = []
# time0230 = []
# time0300 = []
# time0330 = []
# time0400 = []
# time0430 = []
# time0500 = []
# time0530 = []
# time0600 = []
# time0630 = []
# time0700 = []
# time0730 = []
# time0800 = []
# time0830 = []
# time0900 = []
# time0930 = []
# time1000 = []
# time1030 = []
# time1100 = []
# time1130 = []
# time1200 = []
# time1230 = []
# time1300 = []
# time1330 = []
# time1400 = []
# time1430 = []
# time1500 = []
# time1530 = []
# time1600 = []
# time1630 = []
# time1700 = []
# time1730 = []
# time1800 = []
# time1830 = []
# time1900 = []
# time1930 = []
# time2000 = []
# time2030 = []
# time2100 = []
# time2130 = []
# time2200 = []
# time2230 = []
# time2300 = []
# time2330 = []
# print(data[0:2])
# fullSheet = file.read()
# print(fullSheet)
#This is a function which will take a given value for time and energy and add the energy value to the list corresponding to the time value
def timeMatch(time, value):
    if time == "00:00  <  00:30":
        timeValues[0].append(int(value))
    elif time == "00:30  <  01:00":
        timeValues[1].append(int(value))
    elif time == "01:00  <  01:30":
        timeValues[2].append(int(value))
    elif time == "01:30  <  02:00":
        timeValues[3].append(int(value))
    elif time == "02:00  <  02:30":
        timeValues[4].append(int(value))
    elif time == "02:30  <  03:00":
        timeValues[5].append(int(value))
    elif time == "03:00  <  03:30":
        timeValues[6].append(int(value))
    elif time == "03:30  <  04:00":
        timeValues[7].append(int(value))
    elif time == "04:00  <  04:30":
        timeValues[8].append(int(value))
    elif time == "04:30  <  05:00":
        timeValues[9].append(int(value))
    elif time == "05:00  <  05:30":
        timeValues[10].append(int(value))
    elif time == "05:30  <  06:00":
        timeValues[11].append(int(value))
    elif time == "06:00  <  06:30":
        timeValues[12].append(int(value))
    elif time == "06:30  <  07:00":
        timeValues[13].append(int(value))
    elif time == "07:00  <  07:30":
        timeValues[14].append(int(value))
    elif time == "07:30  <  08:00":
        timeValues[15].append(int(value))
    elif time == "08:00  <  08:30":
        timeValues[16].append(int(value))
    elif time == "08:30  <  09:00":
        timeValues[17].append(int(value))
    elif time == "09:00  <  09:30":
        timeValues[18].append(int(value))
    elif time == "09:30  <  10:00":
        timeValues[19].append(int(value))
    elif time == "10:00  <  10:30":
        timeValues[20].append(int(value))
    elif time == "10:30  <  11:00":
        timeValues[21].append(int(value))
    elif time == "11:00  <  11:30":
        timeValues[22].append(int(value))
    elif time == "11:30  <  12:00":
        timeValues[23].append(int(value))
    elif time == "12:00  <  12:30":
        timeValues[24].append(int(value))
    elif time == "12:30  <  13:00":
        timeValues[25].append(int(value))
    elif time == "13:00  <  13:30":
        timeValues[26].append(int(value))
    elif time == "13:30  <  14:00":
        timeValues[27].append(int(value))
    elif time == "14:00  <  14:30":
        timeValues[28].append(int(value))
    elif time == "14:30  <  15:00":
        timeValues[29].append(int(value))
    elif time == "15:00  <  15:30":
        timeValues[30].append(int(value))
    elif time == "15:30  <  16:00":
        timeValues[31].append(int(value))
    elif time == "16:00  <  16:30":
        timeValues[32].append(int(value))
    elif time == "16:30  <  17:00":
        timeValues[33].append(int(value))
    elif time == "17:00  <  17:30":
        timeValues[34].append(int(value))
    elif time == "17:30  <  18:00":
        timeValues[35].append(int(value))
    elif time == "18:00  <  18:30":
        timeValues[36].append(int(value))
    elif time == "18:30  <  19:00":
        timeValues[37].append(int(value))
    elif time == "19:00  <  19:30":
        timeValues[38].append(int(value))
    elif time == "19:30  <  20:00":
        timeValues[39].append(int(value))
    elif time == "20:00  <  20:30":
        timeValues[40].append(int(value))
    elif time == "20:30  <  21:00":
        timeValues[41].append(int(value))
    elif time == "21:00  <  21:30":
        timeValues[42].append(int(value))
    elif time == "21:30  <  22:00":
        timeValues[43].append(int(value))
    elif time == "22:00  <  22:30":
        timeValues[44].append(int(value))
    elif time == "22:30  <  23:00":
        timeValues[45].append(int(value))
    elif time == "23:00  <  23:30":
        timeValues[46].append(int(value))
    elif time == "23:30  <  00:00":
        timeValues[47].append(int(value))
counter = 0
for row in range(1, (len(data)-1)): # This loop goes through every row in the spreadsheet, picks out the time and energy percentage values, and passes them into the time matching function

# for item in data:
        timeMatch(data[row][2], data[row][4])
# print(timeValues)
print(f"timevalues[0] = {timeValues[0]}")

# for item in timeValues: # This loop gets the average for every time of day and adds them to a list
#     averageEnergyValues.append(stats.mean(item))
while counter > len(timeValues):
    averageEnergyValues.append(sum(timeValues[counter] / len(timeValues[counter])))
    print(stats.mean(timeValues[counter]))
    counter += 1
print(averageEnergyValues)
# fig, ax = plot.subplots(figsize = (5,4), layout="constrained")