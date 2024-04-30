# If else in python

# Conditional Statements:
# 1. if-elif-else

# x = 10
# if x > 10:
#     print("x is greater than 10")
# elif x == 10:
#     print("x is exactly 10")
# else:
#     print("x is less than 10")
#
# # shortcut for comment / uncomment : ctrl + /
# # if: check condition is true
# # elif: stands for "else if". It checks addtional conditions if the previous ones are false
# # else: executes when none of the previous conditions are true
#
#
# # ********************************* Exercise  **************************************************************************
# # Write a program that interprets the Body Mass Index (BMI) based on a user's weight and height
# # It should tell them the interpretation of their# comparison Operators:
# # # > greater than
# # # < less than
# # # >= greater than or equal to
# # # <= less than or equals to
# # # == equals to
# # # != not equals to BMI based on the BMI value.
# #        Under 18.5 they are underweight
# #        Over 18.5 but below 25 they have a normal weight
# #        Over 25 but below 30 they are slightly overweight
# #        Over 30 but below 35 they are obese
# #        Above 35 they are clinically obese
# # *********************************************************************************************************************
#
# height = int(input("Enter your height: "))
# weight = int(input("Enter your weight: "))
#
# bmi = weight / (height*height)
# print("calculated BMI is: ", bmi)
#
# if bmi < 18.5:
#     # print("Your BMI is ",bmi, " and you are overweight")
#     print(f"Your BMI is {bmi} and you are overweight")
# elif bmi < 25:
#     print(f"Your BMI is {bmi} and you have normal weight")
# elif bmi < 30:
#     print(f"Your BMI is {bmi} and you are slightly overweight")
# elif bmi <35:
#     print(f"Your BMI is {bmi} and you are obese")
# else:
#     print(f"Your BMI is {bmi} and you are slightly over-weight")

# ********************************* Exercise  **************************************************************************
# Write a program that works out whether if a given year is a leap year.
# A normal year has 365 days, leap year have 366 with an extra day in february.
# This is how you work out whether if a particular year is a leap year
#     on every year that is divisible by 4 with no remainder --- year % 4 == 0
#     except every year that is evenly divisible by 100 with no remainder --- year % 100 == 0
#     unless the year is also divisible by 400 with no remainder --- year % 400 == 0
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

# Loops
# 2. for loop:
# fruits = ["apple", "banana", "cherry"] # list
#
# for fruit in fruits:
#     print(fruit)
#
# # for: iterates over a sequence (like list, tuple or string, or range)
# # fruit: variable that holds each item in the list during each iteration
#
# # 3. while loop:
# num = 0
# while num <= 5:  # while loop is mostly used, to check if the condition is true
#     print(num)
#     num = num+1
#
# # control statement:
# # 4. break:
# for num in range(10):
#     if num == 5:
#         break
#     print(num)
#
# # break: terminates the loop pre-maturely when a condition is met
#
# # 5. continue:
# for num in range(10):
#     if num == 5:
#         continue
#     print(num)
#
# #continue: skip the rest of the current iteration and continues witht he next iteration of the loop
#
# #************************************ Exercise ****************************************************
# # Write a program that calculates the average student height from a list of heights.
# # student_heights = [180,120,165,173,189,169,146]
# # The average height can be calculated by adding all the heights together and dividing by the total
# # number of heights. Then average it to nearest whole number
#
# student_heights = [180,120,165,173,189,169,146]
# total_height=0
# for height in student_heights:
#     # total_height = total_height + height
#     total_height += height
#
# print("total height",total_height)
# nbr_of_students = len(student_heights)
# average_height = int(total_height / nbr_of_students)
# print("Average Height is: ", average_height)

#****************************** Exercise 2 *****************************************
# Write a program that calculates the highest score from a list of scores
# eg. - student_scores = [78,65,89,86,55,91,64,89]
# Output shd be - The highest score in the class is: x

# assume highest_score = 0
# compare highest_score with each item in the list
# when u find any item bigger than zero, then replace highest_score with that value

#************************** Exercise 3 **********************************************************
# Write a program that calculates the sum of all the even numbers from 1 to X. If X is 100 then
# the first even number would be 2 and the last one is 100.
# 2+4+6+8+10+...+98+100

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

# def greet():
#     print("Hello Oindrilla, Welcome to the class!")
#
# greet()
#
#
# def greet(name):
#     """
#     This method is used to print a message
#     :param name: name of the person we want to greet
#     :return: None
#     """
#     print("Hello ",name, " Welcome to the class!")
#
# greet("Oindrila")
# greet("Neelam")
#
# # def: Keyword used to define a function.
# # greet: Name of the function.
# # (name): Parameter(s) the function accepts.
# # """docstring""": Optional documentation string describing the function's purpose and usage.
#
# # 2. Returning values:
# def add(x,y):
#     sum = x+y
#     # return x+y
#     return sum
#
# print("Result is: ",add(100,300))
#
# sum_of_two_nbrs = add(500,600)
# print(f"Result is: {sum_of_two_nbrs}")

# return: Statement used to return a value from a function.

# 3. Returning multiple values
# def operations(num1, num2):
#     sum = num1+num2
#     subtract = num2-num1
#     product = num1*num2
#     division = num2/num1
#
#     return sum, subtract,product,division
#
# add, diff, multiply, divide = operations(200,400)
# print(f"Sum: {add}, Difference: {diff}, Product: {multiply}, Division: {divide}")

# def greet(*name):
#     """
#     This method is used to print a message
#     :param name: name of the person we want to greet
#     :return: None
#     """
#     print("Hello ",name, " Welcome to the class!")
#
# greet("Oindrila", "Madhuri", "Neelam")

def create_dictionary():
    dictObj = {"Name": "Neelam", "Location": "Pune", 3:"Automation Tester"}
    return dictObj

result = create_dictionary()
print(result)
print(result["Name"])











