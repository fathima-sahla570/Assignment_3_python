# # Exercise 1:
# month_names = {
#     1: "January", 2: "February", 3: "March", 4: "April",
#     5: "May", 6: "June", 7: "July", 8: "August",
#     9: "September", 10: "October", 11: "November", 12: "December"
# }
#
# month = int(input("Enter the month: "))
# if month in month_names:
#     print(f"Month {month} is {month_names[month]}")
# else:
#     print("Invalid month. Please enter a number between 1 and 12.")
# # # # Exercise 2:
# age = int(input("Enter your age: "))
# if age < 16:
#     print("Your ticket costs £3.00")
# elif age <= 60:
#     print("Your ticket costs £6.00")
# else:
#     print("Your ticket costs £2.00")
# # # Exercise 3
# weight = float(input("Enter your weight in (kg): "))
# height = float(input("Enter your height in (m): "))
# bmi = weight / (height ** 2)
# if bmi < 18.5:
#     print( " you are in Underweight")
# elif 18.5 <= bmi < 25:
#     print(" you are in Normal")
# elif 25 <= bmi < 30:
#     print(" you are in Overweight")
# else:
#     print(" you are in obese")
# # # Exercise 4
# num1 = float(input("Enter the first number: "))
# num2 = float(input("Enter the second number: "))
# num3 = float(input("Enter the third number: "))
# if num1 >= num2 and num1 >= num3:
#     print(" The greatest numbers i=",num1)
# elif num2 >= num1 and num2 >= num3:
#     print("The greatest number =" ,num2)
# else:
#     print("The greatest number=", num3)
# # # Exercise 5
# num = int(input("Enter a number to find its factorial: "))
# if num < 0:
#     print("Factorial is not defined for negative numbers.")
# elif num == 0 or num == 1:
#     print(f"The factorial of {num} is : 1")
# else:
#     factorial = 1
#     for i in range(1,num + 1):
#         factorial *= i
#     print(f"The factorial of {num} is {factorial}")
# # # Exercise 6
# num = int(input("Enter a number to reverse: "))
# reversed_num = 0
#
# while num != 0:
#     digit = num % 10
#     reversed_num = reversed_num * 10 + digit
#     num //= 10
# print(f"The reversed number is {reversed_num}")
# # # Exercise 7
# num = int(input("Enter a number to find its multiples: "))
# limit = int(input("Enter the range limit: "))
#
# for i in range(1, limit + 1):
#     print(f"{i} * {num} = {i * num}")
# # Exercise 8
while True:
    value = input(":")
    if value== 'done':
        print("Done")
        break
    print(value)
# Exercise 9
for i in range(1,11):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
# # Exercise 10
for i in range(5, 0, -1):
    for j in range(i, 0, -1):
        print(j, end=" ")
    print()
#
#
#
#
#
