# Write a Python program to get the current date and time.
import datetime
from math import gcd

print("Current date and time:",datetime.datetime.now())

# Write a Python program to add 5 days to the current date.
todays_date = datetime.date.today()
five_days = datetime.timedelta(days=5)
updated_date = todays_date+five_days
print("Updated date after 5 days: ",updated_date)

# Write a Python program to convert a string to a datetime object.
inp_date_str = "2023-03-18"
input_format = "%Y-%m-%d"
converted_date = datetime.datetime.strptime(inp_date_str, input_format)
print("Converted date:", converted_date)

# Write a Python program to format the current date in a specific format.
todays_date = datetime.datetime.now()
print("Formatted date:",todays_date.strftime("%Y - %m - %d %H:%M:%S"))


# Write a Python program to calculate the difference between two dates.
date1 = datetime.date(2022,3,10)
date2 = datetime.date(2022,1,5)
date_diff = date1 - date2
print("Difference between 2 dates:", date_diff.days, "days")

# Write a Python function to find the maximum of three numbers.
def max_of_three(a,b,c): # 2,5,8
    max_num = max(a,b,c)
    # max_num =a
    # for i in range(b,c):
    #     if i > max_num:
    #         max_num = i
    return max_num

print("Max of 3 nbr:",max_of_three(24,56,12))

# Write a Python function to check if a given number is even or odd.
def chk_nbr_evenodd(n):
    if n % 2 == 0:
        return "Nbr is even"
    else:
        return "Nbr is Odd"

print("Nbr is: ", chk_nbr_evenodd(7))

# Write a Python function to calculate the factorial of a given number.
# 5*4*3*2*1 = 120

def factorial(n):
    result = 1
    for i in range(1, n+1):
        result = result*i
    return result

print("Factorial is: ", factorial(5))

# Write a Python function to find the greatest common divisor (GCD) of two numbers.
# 12 = 2*2*3 --- product of least powers of the common factors --- 2*2*3 = 12
# 24 = 2*2*2*2*3

def gcd_oftwonbrs(a,b):
    return gcd(a,b)

print("GCD is: ", gcd_oftwonbrs(12,24))
