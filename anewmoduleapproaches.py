import statistics as stats
ages = [32,31,30,37,37,33]
earnings =[1270,7980,4700,1810,750,1100]
ages.sort()
earnings.sort()
print(f"Minimum age: {ages[0]}\nMaximum age: {ages[-1]}\nMean average age: {stats.mean(ages)}\nMinimum earnings: {earnings[0]}\nMaximum earnings: {earnings[-1]}\nMean average earnings: {stats.mean(earnings)}")
# print(ages)
# print(earnings)