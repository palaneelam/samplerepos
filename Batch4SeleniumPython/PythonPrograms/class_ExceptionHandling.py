# Exception handling is a crucial aspect of Python programming, allowing you to gracefully
# manage errors and unexpected situations that may arise during program execution. Let's delve
# into exception handling in detail, along with examples:

#Error Handling:
try:
    file_path = ""
    file = open(file_path, "r")
    content = file.read()
    print(content)
    file.close()
except FileNotFoundError as e:
    print(e)
except Exception as ex:
    print("Error Message: ", ex)

# file_path = ""
# file = open(file_path, "r")
# print("Hi")
# content = file.read()
# print(content)
# file.close()

# try, except, else, finally

try:
    result = 10/0
except ZeroDivisionError as e:
    print("Error:", e)
else:
    print("result:", result)
    print("Division successful")
finally:
    print("Cleanup code here")

# Explanation:
# try: Encloses the code that may raise an exception.
# except: Catches specific exception(s) and handles them.
# else: Optional block executed if no exception occurs.
# finally: Optional block always executed, regardless of whether an exception occurred.

# catch multiple exception
try:
    result = int("abc")
except (ValueError, TypeError) as e:
    print(e)

# raising exception:

def validate_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    elif age < 18:
        raise ValueError("Must be 18 years or older")


try:
    validate_age(5)
except ValueError as e:
    print("errorMessage:", e)


# Custom Exceptions:
class CustomError(Exception):
    def __init__(self, message):
        self.message = message

try:
    raise CustomError("This is a custom error.")
except CustomError as e:
    print(e)

