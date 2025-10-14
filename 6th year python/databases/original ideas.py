import csv
header = ["firstName", "lastName", "phoneNum", "DOB", "age"]
records = [ #ages changed to be accurate as of october 2025
    ["Joan", "Byrne", "0871112233", "2/2/75", 50],
    ["Gideon", "Jones", "0874445566", "4/7/59", 66],
    ["Noor", "Patel", "0877778899", "3/6/03", 22]
]
file = open("patients.csv", "a", newline="")
db = csv.writer(file)
db.writerow(header)
for item in records: db.writerow(item)