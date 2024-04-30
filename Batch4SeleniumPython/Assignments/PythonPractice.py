# TODO 1 - Write a Python program to print the numbers from 1 to 10 using a for loop.
# Algorithm:
# 1. use a for loop to iterate from 1 to 10 --- start a for loop with range 1 to 11
# 2. Print each number in the loop

# for num in range(1,11):
#     print("Inside loop:",num)
# print("Outside loop:",num)

# TODO 2 - Write a Python program to find the sum of all numbers from 1 to 100 using a while loop.
# Algorithm:
# 1. Initialise a variable to store the sum and set it to 0. --- sum = 0
# 2. Use a while loop to iterate from 1 to 100 -- num = 1, condiiton: num<=100
# 3. Add each number to the sum ---- within the loop, add num to sum and increment num by 1
# 4. Print the sum

# sum = 0
# num = 1
# while num <= 100:
#     # sum = sum+num
#     sum += num
#     # num = num+1
#     num += 1
# print(f"Sum of numbers from 1 to {num-1}:", sum)

# Another way of writing the same program without using loops
# numbers = range(1,101)
# result = sum(numbers)
# print("Sum:",result)

# TODO 3 - Write a Python program to print the multiplication table of a given number using a for loop.
# Algorithm:
# 1. Take input for the number
# 2. Start a for loop with a range 1 to 11
# 3. Multiply the number by each iteration value
# 4. Print the multiplication result

# number = int(input("Enter a number for which you want to see the multiplication table:"))
# for i in range(1,11):
#     result = number*i
#     # print(result)
#     print(number, "x", i ,"=", result)

# TODO 4 - Write a Python program to find the factorial of a given number using a while loop
# Algorithm:
# 1. Take input for the number
# 2. Initialise a variable to store the factorial and set it to 1
# 3. Initialise a variable num to 1
# 4. Enter a while loop, with the condition num <= given number
# 5. within loop, multiply factorial by numand incrmeent num by 1
# 6. Print the factorial

# number = int(input("Enter a number whose factorial is to be calculated:"))
# factorial = 1
# num = 1
# while num <= number:
#     factorial *= num
#     num += 1
# print(f"Factorial of {number} is {factorial}")

# TODO 5 - Write a Python program to check if a given number is prime or not using a for loop.
# Alogrithm:
# 1. Take input from the user
# 2. Inititalise a variable factors_count to 0
# 3. start for loop with a range from 1 to given number
# 4. if the number is divisible by the iteration value, increment factors_count
# 4. after the loop, if factors_count is greater than 2, print "Not prime", else "Prime"
#
# number = int(input("Enter number which you want to check for prime or not?: "))
# factors_count = 0   # assignment operator
# for i in range(1, number+1):
#     if number % i == 0:   # comparison operator
#         factors_count += 1
#
# if factors_count > 2:
#     print(number, " is not a prime number")
# else:
#     print(number, " is a prime number")

# TODO 6 - Write a Python program to print the Fibonacci sequence up to a given number using a while loop.
# 0,1, 1,2,3,5,8....
#Algorithm:
# 1. Take input for the number
# 2. Initialise varibales for the first 2 terms of the fibonacci
# 3. Print first 2 numbers
# 4. Use a while loop to generate and print the subsequent terms until next terms exceeds the given number
#       Enter a while loop with the condition first term+ second term <= given number
#       within the loop, calculate the next terms by adding first term and second term
#       print the next terms and update values of first term and second term

# number = int(input("Enter number: "))
# first_term, second_term = 0, 1
# print(first_term, second_term, end=",")
# while first_term + second_term <= number:
#     next_term = first_term+second_term
#     print(next_term, end = ",")
#     first_term = second_term
#     second_term = next_term

#  TODO 7 - Write a Python program to find the sum of all even numbers from 1 to 50 using a for loop.
# Algorithm:
# 1. Initialise a variable sum_even to 0
# 2. Use for loop to iterate from 1 to 51
# 3. If the current number is even, add it to the sum
# 4. Print the sum

# sum_even = 0
# # for num in range(2,51,2):
# for num in range(1,51):
#     # if num%2 == 0:
#     sum_even += num
# print("Sum of even numbers from 1 to 50 is: ", sum_even)

# 8. Write a Python program to print the pattern:

# A:
# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5

# B:
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

# C:
# 1
# 2 1
# 3 2 1
# 4 3 2 1
# 5 4 3 2 1

print("Pattern A:")
for i in range(1,6):
    for j in range(1, i+1):
        print(i, end=" ")
        # print("*", end=" ")
    print()


print("Pattern B:")
for i in range(1,6):
    for j in range(1, i+1):
        print(j, end=" ")
        # print("*", end=" ")
    print()

print("Pattern C:")
for i in range(1,6):
    for j in range(i,0,-1):
        print(j, end=" ")
        # print("*", end=" ")
    print()

#**********************************************************************************************************************
































