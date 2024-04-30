# Write a Python program to get the current date and time.
import datetime
from math import gcd

print("current date time:", datetime.datetime.now())

try:
    # Write a Python program to add 5 days to the current date.
    current_date = datetime.date.today()
    print("Todays date: ", current_date)
    five_days = datetime.timedelta(days=-5)
    updated_date = current_date + five_days
    print("Updated date is: ", updated_date)

    # Write a Python program to convert a string to a datetime object.
    input_date = "2023-03-19"
    input_format = "%Y-%m-%d"
    converted_date = datetime.datetime.strptime(input_date, input_format)
    print("converted date: ", converted_date)

    # Write a Python program to format the current date in a specific format.
    current_time = datetime.datetime.now()
    formatted_date = current_time.strftime("%d-%m-%Y %H:%M:%S")
    print("formatted time: ", formatted_date)

    # Write a Python program to calculate the difference between two dates.
    date1 = datetime.date(2023,3,10)
    date2 = datetime.date(2022,1,5)
    date_diff = date1-date2
    print("Diff date:", date_diff.days, "days")

    # Write a Python function to find the maximum of three numbers.
    def max_of_three_nbrs(a,b,c):
        return max(a,b,c)

    print("Max of 3 nbrs: ",max_of_three_nbrs(23,45,12))

    # Write a Python function to check if a given number is even or odd.
    def is_even(n):
        return n%2 == 0

    print("Is nbr even: ", is_even(4))

    # Write a Python function to calculate the factorial of a given number.
    def factorial(n):
        result = 1
        for i in range(1, n+1):
            result = result * i
        return result

    print("Factorial is: ", factorial(10))

    # Write a Python function to find the greatest common divisor (GCD) of two numbers.
    # 12, 24
    # 12 = 2*2*3 = 2(power2) * 3(power1)
    # 24 = 2*2*2*2*3 = 2(power4)*3(power1)
    # GCD = 4*3 =12
    def gcd_of_two(a,b):
        return gcd(a,b)

    print("GCD is: ", gcd_of_two(12,24))

    # Write a Python program to demonstrate the use of lambda functions.
    def add_nbrs(a,b):
        sum=a+b
        return sum

    result = lambda a,b : a+b
    print("Sum is:", result(3,5))

    square = lambda x: x**2
    print("Sqaure is:", square(9))

    is_even = lambda n: n%2 == 0
    print("Is even nbr? ", is_even(10))

except Exception as e:
    print("Exception is: ",e)

