h = float(input("How tall are you in metres? "))
w = int(input("How heavy are you in kilograms? "))
bmi = w / h ** 2
print("BMI category: ", end="")
if bmi < 18.5:
    print("Underweight")
elif bmi < 24.9:
    print("Normal")
elif bmi < 29.9:
    print("Overweight")
else:
    print("Obese")