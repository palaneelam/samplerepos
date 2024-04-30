# Write a Python program to handle division by zero exception.

try:
    result = 2/0
    print("Result is: ", result)
except ZeroDivisionError as ex:
    print("Wrong denominator value provided")
    print("Error message is: ", ex)

print("All actions done")

# Write a Python program to handle file not found exception.
try:
    file_path = "c:\\text1.txt"
    file = open(file_path, "r")
    content = file.read()
    print(content)
    file.close()
# except FileNotFoundError as e:
#     print(e)
except Exception as ex:
    print("Error Message: ", ex)

# Write a Python program to handle IndexError exception.
try:
    numbers = [1,2,3,4,5]
    print("Number at 6th index is: ",numbers[6])
# except IndexError as e:
#     print("Error message is: ", e)
except Exception as ex:
    print("Error Message: ", ex)

# Write a Python program to handle KeyError exception.
try:
    dictionary = {'a':1, 'b':2, 'c':3,'d':4}
    print("Value: ", dictionary['e'])
except KeyError as e:
    print("Error: ", e)
except Exception as ex:
    print("Error Message: ", ex)

# dictionary = {'a':1, 'b':2, 'c':3,'d':4}
# print("Value: ", dictionary['e'])

# Write a Python program to demonstrate the use of try-except-else-finally blocks.
try:
    x = 10/0
except ZeroDivisionError:
    print("Error: Division by zero")
else:
    print("Result:", x)
finally:
    print("Cleanup code")




# Write a Python program to import the math module and demonstrate its usage.


# Write a Python program to create a user-defined module and import it into another Python program.
# Write a Python program to import the datetime module and demonstrate its usage.
# Write a Python program to import the random module and generate random numbers.
# Write a Python program to import a module and alias it with a different name.