# Program Flow Control
# Descision Making statements - if else in python
# num = 1
#
# if num == 1:
#     print("Verified")
# else:
#     print("Not Verified")
#
# x = 10
#
# if x > 10:
#     print("x is greater than 10")
# elif x == 10:
#     print("x is exactly 10")
# else:
#     print("x is less than 10")
#
# # Explanation:
# # if: Checks if a condition is true.
# # elif: Stands for "else if". It checks additional conditions if the previous ones are false.
# # else: Executes when none of the previous conditions are true.
#
# # Loops statement:
# # 1. for loop:
# fruits = ["apple", "banana", "cherry"]
# for fruit in fruits:
#     print(fruit)
#
# # Explanation:
# # for: Iterates over a sequence (like a list, tuple, or string).
# # fruit: Variable that holds each item in the sequence during each iteration.
#
# # while loop:
# # num = 0  # initialise
# # while num < 5: # termination condition
# #     print(num)
# #     num = num+1     #step / increment / decrement condition
#
# # Explanation:
# # while: Continuously executes a block of code as long as a condition is true.
# # num < 5: Condition to check if the loop should continue.
#
# # Control statements:
# # break:
# # for num in range(10): # stop/termination condition num < 10
# #     print(num)
# #     if num == 5:
# #         break
#
# # Explanation:
# # break: Terminates the loop prematurely when a condition is met.
#
# # continue:
# # for num in range(10): # stop/termination condition num < 10
# #     if num == 5:
# #         continue
# #     print(num)
#
# # Explanation:
# # continue: Skips the rest of the current iteration and continues with the next iteration of the loop.
# # These control structures provide the flexibility to create complex logic and handle various scenarios
# # within your Python programs. Mastering them is essential for writing efficient and readable code.
#
# #******************************************************************************************************
# # comparison Operators:
# # > greater than
# # < less than
# # >= greater than or equal to
# # <= less than or equals to
# # == equals to
# # != not equals to
#
# # ********************************* Exercise  **************************************************************************
# # Write a program that interprets the Body Mass Index (BMI) based on a user's weight and height
# # It should tell them the interpretation of their BMI based on the BMI value.
# #        Under 18.5 they are underweight
# #        Over 18.5 but below 25 they have a normal weight
# #        Over 25 but below 30 they are slightly overweight
# #        Over 30 but below 35 they are obese
# #        Above 35 they are clinically obese
# # *********************************************************************************************************************
# height = int(input("Enter your height: "))
# weight = int(input("Enter your weight: "))
#
# bmi = weight / (height*height)
# print("BMI is: ", bmi)
# # print(f"BMI is: {bmi}")
# if bmi < 18.5:
#     print(f"Your BMI is {bmi}, you are underweight.")
# elif bmi < 25:
#     print(f"Your BMI is {bmi}, you are normal weight.")
# elif bmi < 30:
#     print(f"Your BMI is {bmi}, you are slightly overweight.")
# elif bmi < 35:
#     print(f"Your BMI is {bmi}, you are obese.")
# else:
#     print(f"Your BMI is {bmi}, you are clinically obese.")
#
# # ********************************* Exercise  **************************************************************************
# # Write a program that works out whether if a given year is a leap year.
# # A normal year has 365 days, leap year have 366 with an extra day in february.
# # This is how you work out whether if a particular year is a leap year
# #     on every year that is divisible by 4 with no remainder --- %
# #     except every year that is evenly divisible by 100 with no remainder
# #     unless the year is also divisible by 400 with no remainder
# # *********************************************************************************************************************
#
# n = input("Enter year")
# if n % 4 == 0:
#     print("Leap year", n)
# elif n % 100 == 0:
#     print("Leap year", n)
# elif n % 400 == 0:
#     print("Leap year", n)
# else:
#     print("Not a leap year")

# ********************************* Exercise  **************************************************************************
# Build an automatic pizza order program.
# Based on user's order, work out their final bill.
# Small pizza($)(S) : $15
# Medium pizza($)(M) : $20
# Large pizza($)(L) : $25
# Add pepperoni for Small pizza($) (Y or N) : $2
# Add pepperoni for medium or large pizza(Y or N) : $3
# Add extra cheese for any size (Y or N) pizza($) : $1
# *********************************************************************************************************************

# ******************************* LOVE CALCULATORS **********************************************************************
# Write a program that tests the compatiability between two people
# To work out the love score between two people:
#   1. Take both people's name and check for the number of times th letters in the word TRUE occurs.
#   2. Then check for the number of times the letters in the work LOVE occurs.
#   3. Then combine these numbers to make a 2 digit number.
# For Love scores less than 10 or greater than 90, the message should be:
# "Your score is 'x' you go together like coke and mentos
# For love scores between 40 and 50, the message should be:
# "Your score is 'x' you are alright together.
# otherwise, the message will just be their score. e.g: "Your score is z"

# logic
# ex.- str = neelammanpreet
# count nbr of time t comes in above string - 1 --- str.count("t")
# count nbr of time r comes in above string - 1
# count nbr of time u comes in above string - 0
# count nbr of time e comes in above string - 4.
# sum of all digits in true = 6
# count nbr of time l comes in above string - 1
# count nbr of time o comes in above string - 0
# count nbr of time v comes in above string - 0
# count nbr of time e comes in above string - 4
# sum of all digits in love = 5
# score = 65
# *********************************************************************************************************************

#************************************ Exercise 4 ********************************************
# Write a program that automatically prints the solution to the FizzBuzz game.
# These are the rules of the FizzBuzz game:
#   a. Your program should print each number from 1 to 100 in turn and include number 100
#   b. When the number is divisible by 3 then instead of printing the number it should print "Fizz"
#   c. When the number is divisible by 5, then instead of printing the number it should print "Buzz"
#   d. And if the number is divisible by both 3 and 5. eg. 15 then instead of the number it should print
#        "FizzBuzz"

# Output - 1,2,"Fizz",4,"Buzz","Fizz",7,8,"Fizz","Buzz",11,"Fizz",13,14,"FizzBuzz",16,17,"Fizz",19,"Buzz"..... "Buzz"
#****************************************************************************************************************

# Functions / Methods:
# Functions and modules are crucial concepts in Python that help organize code, promote
# reusability, and enhance maintainability.

# 1. defining functions

# def greet():
#     print("Welcome Madhuri!")
#
# greet()
# greet()
# greet()
# greet()
# greet()

def greet(name="ABC"):
    ''' Prints a greeting message to the name provided'''
    print(f"Welcome {name}!")

greet("Neelam")
greet("Manpreet")
greet("Shivam")
greet()

# def: Keyword used to define a function.
# greet: Name of the function.
# (name): Parameter(s) the function accepts.
# """docstring""": Optional documentation string describing the function's purpose and usage.


# 2. Returning values
def add(num1, num2):
    # sum = num1+num2
    # return sum
    return num1+num2

# result = add(100,200)
# print("Sum of 2 nbrs:", result)
print("Sum of 2 nbrs:", add(100,200))

# 3. Returning multiple values
def operation(num1, num2):
    # sum = num1+num2
    # return sum
    return num1+num2 , num1-num2, num1*num2, num1/num2

add, subtract, product, division = operation(800,200)
print("Results are: ", add, subtract, product, division)
# result = add(100,200)
# print("Sum of 2 nbrs:", result)

# Aritrary arguments

def greet(*name):
    ''' Prints a greeting message to the name provided'''
    print(f"Welcome {name}!")

greet("Neelam", "Manpreet", "Shivam")

# *args: Allows the function to accept a variable number of arguments.
