 # Exercise 3
weight = float(input("Enter your weight in (kg): "))
height = float(input("Enter your height in (m): "))
bmi = weight / (height ** 2)
if bmi < 18.5:
    print( " you are in Underweight")
elif 18.5 <= bmi < 25:
    print(" you are in Normal")
elif 25 <= bmi < 30:
    print(" you are in Overweight")
else:
    print(" you are in obese")