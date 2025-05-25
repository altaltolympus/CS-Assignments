import matplotlib.pyplot as plot
import csv
import statistics as stats
sheet = open("spreadsheet.csv", "r")
data = list(csv.reader(sheet, delimiter=",")) #This gets me the entire file, headings and all, but I only want the data
sheet.close()
timeBrackets = ["00:00", "00:30", "01:00", "01:30", "02:00", "02:30", "03:00", "03:30", "04:00", "04:30", "05:00", "05:30", 
                "06:00", "06:30", "07:00", "07:30", "08:00", "08:30", "09:00", "09:30", "10:00", "10:30", "11:00", "11:30", 
                "12:00", "12:30", "13:00", "13:30", "14:00", "14:30", "15:00", "15:30", "16:00", "16:30", "17:00", "17:30", 
                "18:00", "18:30", "19:00", "19:30", "20:00", "20:30", "21:00", "21:30", "22:00", "22:30", "23:00", "23:30"]
timeValues = []
for i in range(48): timeValues.append([]) # This loop fills timeValues with 48 empty lists, which I will use to store the energy values for each time of day
# The sub-lists are associated with each time bracket; for instance, timeValues[0] is 00:00 - 00:30, timeValues[1] is 00:30 - 01:00 and so on

averageEnergyValues = [] # Once the average energy value for each time of day is calculated, it will go here

# This is a function which will take a given value for time and energy and add the energy value to the list corresponding to the time value
"""
 ↑ Left that comment in for the sake of preserving history. That function is gone now. I have replaced it with this dictionary, which maps each time of day to the corresponding sub-list 
 in timeValues
"""

timeMatch =  {
    "00:00  <  00:30": 0,
    "00:30  <  01:00": 1,
    "01:00  <  01:30": 2,
    "01:30  <  02:00": 3,
    "02:00  <  02:30": 4,
    "02:30  <  03:00": 5,
    "03:00  <  03:30": 6,
    "03:30  <  04:00": 7,
    "04:00  <  04:30": 8,
    "04:30  <  05:00": 9,
    "05:00  <  05:30": 10,
    "05:30  <  06:00": 11,
    "06:00  <  06:30": 12,
    "06:30  <  07:00": 13,
    "07:00  <  07:30": 14,
    "07:30  <  08:00": 15,
    "08:00  <  08:30": 16,
    "08:30  <  09:00": 17,
    "09:00  <  09:30": 18,
    "09:30  <  10:00": 19,
    "10:00  <  10:30": 20,
    "10:30  <  11:00": 21,
    "11:00  <  11:30": 22,
    "11:30  <  12:00": 23,
    "12:00  <  12:30": 24,
    "12:30  <  13:00": 25,
    "13:00  <  13:30": 26,
    "13:30  <  14:00": 27,
    "14:00  <  14:30": 28,
    "14:30  <  15:00": 29,
    "15:00  <  15:30": 30,
    "15:30  <  16:00": 31,
    "16:00  <  16:30": 32,
    "16:30  <  17:00": 33,
    "17:00  <  17:30": 34,
    "17:30  <  18:00": 35,
    "18:00  <  18:30": 36,
    "18:30  <  19:00": 37,
    "19:00  <  19:30": 38,
    "19:30  <  20:00": 39,
    "20:00  <  20:30": 40,
    "20:30  <  21:00": 41,
    "21:00  <  21:30": 42,
    "21:30  <  22:00": 43,
    "22:00  <  22:30": 44,
    "22:30  <  23:00": 45,
    "23:00  <  23:30": 46,
    "23:30  <  00:00": 47,
}
matchingTime = 0
for row in range(1, (len(data)-1)): # This loop goes through every row in the spreadsheet, picks out the time and energy percentage values, and passes them into the time matching function
    matchingTime = timeMatch[data[row][2]]
    print(matchingTime)
    timeValues[matchingTime].append(int(data[row][4]))
print(f"timevalues[0] = {timeValues[0]}")
# print(f"timeValues[48] = {timeValues[48]}")
print(f"len(timeValues) = {len(timeValues)}")
for item in timeValues: # This loop gets the average for every time of day and adds them to a list
    # print(item)
    averageEnergyValues.append(stats.mean(item))

# while counter < len(timeValues):
#     averageEnergyValues.append((sum(timeValues[counter]) / len(timeValues[counter])))
#     print(f"sum of the list ({sum(timeValues[counter])}) divided by length of the list ({len(timeValues[counter])}) equals {stats.mean(timeValues[counter])}")
#     counter += 1

print(f"averageEnergyValues = {averageEnergyValues}")

# fig, ax = plot.subplots(figsize = (5,4), layout="constrained")