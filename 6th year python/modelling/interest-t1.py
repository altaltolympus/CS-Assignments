from csv import *
salary = int(input("Net monthly salary (€): "))
p = int(input("Principal (€): "))
t = int(input("Term (years): "))
header = ["Net monthly salary €", "P €", "t years", "Approved Y or N expected", "Approved Y or N actual result"]
spreadsheet = open("mortgages-t1.csv", "w")
record = writer(spreadsheet)
record.writerow(header)
for x in range(1,7):
    output = [salary, p, t] 