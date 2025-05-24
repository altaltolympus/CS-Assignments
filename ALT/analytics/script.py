import matplotlib.pyplot as plot
import csv
sheet = open("spreadsheet.csv", "r")
data = list(csv.reader(sheet, delimiter=",")) #This gets me the entire file, headings and all, but I only want the data
sheet.close()
#This next section is just a bunch of lists, to which I will add each value from their associated time of day
time0000 = []
time0030 = []
time0100 = []
time0130 = []
time0200 = []
time0230 = []
time0300 = []
time0330 = []
time0400 = []
time0430 = []
time0500 = []
time0530 = []
time0600 = []
time0630 = []
time0700 = []
time0730 = []
time0800 = []
time0830 = []
time0900 = []
time0930 = []
time1000 = []
time1030 = []
time1100 = []
time1130 = []
time1200 = []
time1230 = []
time1300 = []
time1330 = []
time1400 = []
time1430 = []
time1500 = []
time1530 = []
time1600 = []
time1630 = []
time1700 = []
time1730 = []
time1800 = []
time1830 = []
time1900 = []
time1930 = []
time2000 = []
time2030 = []
time2100 = []
time2130 = []
time2200 = []
time2230 = []
time2300 = []
time2330 = []
# print(data[0:2])
# fullSheet = file.read()
# print(fullSheet)
#This is a function which will run through each row from the .csv file, take the time and energy percentage values, and append the energy percentage to the right time
def timeMatch(time, value):
    if time == "00:00  <  00:30":
        time0000.append(value)
    elif time == "00:30  <  01:00":
        time0030.append(value)
    elif time == "01:00  <  01:30":
        time0100.append(value)
    elif time == "01:30  <  02:00":
        time0130.append(value)
    elif time == "02:00  <  02:30":
        time0200.append(value)
    elif time == "02:30  <  03:00":
        time0230.append(value)
    elif time == "03:00  <  03:30":
        time0300.append(value)
    elif time == "03:30  <  04:00":
        time0330.append(value)
    elif time == "04:00  <  04:30":
        time0400.append(value)
    elif time == "04:30  <  05:00":
        time0430.append(value)
    elif time == "05:00  <  05:30":
        time0500.append(value)
    elif time == "05:30  <  06:00":
        time0530.append(value)
    elif time == "06:00  <  06:30":
        time0600.append(value)
    elif time == "06:30  <  07:00":
        time0630.append(value)
    elif time == "07:00  <  07:30":
        time0700.append(value)
    elif time == "07:30  <  08:00":
        time0730.append(value)
    elif time == "08:00  <  08:30":
        time0800.append(value)
    elif time == "08:30  <  09:00":
        time0830.append(value)
    elif time == "09:00  <  09:30":
        time0900.append(value)
    elif time == "09:30  <  10:00":
        time0930.append(value)
    elif time == "10:00  <  10:30":
        time1000.append(value)
    elif time == "10:30  <  11:00":
        time1030.append(value)
    elif time == "11:00  <  11:30":
        time1100.append(value)
    elif time == "11:30  <  12:00":
        time1130.append(value)
    elif time == "12:00  <  12:30":
        time1200.append(value)
    elif time == "12:30  <  13:00":
        time1230.append(value)
    elif time == "13:00  <  13:30":
        time1300.append(value)
    elif time == "13:30  <  14:00":
        time1330.append(value)
    elif time == "14:00  <  14:30":
        time1400.append(value)
    elif time == "14:30  <  15:00":
        time1430.append(value)
    elif time == "15:00  <  15:30":
        time1500.append(value)
    elif time == "15:30  <  16:00":
        time1530.append(value)
    elif time == "16:00  <  16:30":
        time1600.append(value)
    elif time == "16:30  <  17:00":
        time1630.append(value)
    elif time == "17:00  <  17:30":
        time1700.append(value)
    elif time == "17:30  <  18:00":
        time1730.append(value)
    elif time == "18:00  <  18:30":
        time1800.append(value)
    elif time == "18:30  <  19:00":
        time1830.append(value)
    elif time == "19:00  <  19:30":
        time1900.append(value)
    elif time == "19:30  <  20:00":
        time1930.append(value)
    elif time == "20:00  <  20:30":
        time2000.append(value)
    elif time == "20:30  <  21:00":
        time2030.append(value)
    elif time == "21:00  <  21:30":
        time2100.append(value)
    elif time == "21:30  <  22:00":
        time2130.append(value)
    elif time == "22:00  <  22:30":
        time2200.append(value)
    elif time == "22:30  <  23:00":
        time2230.append(value)
    elif time == "23:00  <  23:30":
        time2300.append(value)
    elif time == "23:30  <  00:00":
        time2330.append(value)
for row in range(1, (len(data)-1)):
# counter = 1
# for item in data:
        timeMatch(data[row][2], data[row][4])
        # counter += 1