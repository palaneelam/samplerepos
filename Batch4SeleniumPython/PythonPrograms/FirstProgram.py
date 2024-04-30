
print("Hello Oindrilla, Welcome to the class!")

message = "Welcome"
message = 'Welcome'

# b = 5
# c = 3.4
# d = "India"

b,c,d = 5,3.4,"India"

print("Type of b is: ", type(b))
print("Type of c is: ", type(c))
print("Type of d is: ", type(d))

print(f"Type of b is: {type(b)}")
print(f"Type of b is: type(b)")

#************************************************************************************
# Understanding Python data types & varibales

# 1. Numeric data-type: int, float, complex
# integer
a= 100
print(f"The type of varibale a is {type(a)}")

# float
a=10.45565
print(f"The type of varibale a is {type(a)}")

# complex
a = 100+3j
print(f"The type of varibale a is {type(a)}")

# 2. String data type
a = "Welcome to"
b = 'India'
c = 100
# using ,
print(a," country ", b," ", c, " times") # this is more preferable way
# using +
# print(a + " country " + b + " " + c + " times")

# 3. Sequence data type: list, tuple, range
# List
a = [1,1,3,4,5,6]

print(a)
b = ["hello", "and", "come", "inside"]
print(b)
c = ["hello", 123, "testing", 456]
print(c)

print(a[2])

# tuple
a=(1,1,3,4)
print(a)
print(a[0])

# Lists are mutable, meaning their elements can be changed after the list is created.
# Lists are ordered collections, meaning the order of elements is maintained.
# Lists are represented using square brackets [ ].

# Tuples are immutable, meaning their elements cannot be changed after the tuple is created.
# Tuples are ordered collections, meaning the order of elements is maintained.
# Tuples are represented using parentheses ( ).

# Practical Uses of Lists
# Storing a collection of similar items
# Keeping track of data in a specific order, like a to-do list
# Modifying, adding, or removing elements as needed

# Practical Uses of Tuples
# Storing fixed collections of data that should not change
# Returning multiple values from a function
# Using as keys in dictionaries (since they are immutable)

print(range(1,10)) # start, stop, step (increment/decrement counters)

# 4. Mapping data type: dict
dictObj = {"Name": "Neelam", "Location": "Pune", 3:"Automation Tester"}
print(dictObj["Name"])
print(dictObj[3])

# 5. Boolean type : bool
bool_var = False
print("type of bool_var is: ", type(bool_var))

# 6. Set data types: set, forzenset
# set: mutable, unordered collections of unique items
# frozenset: immutable version of set
set_var = {1,2,3,4,5,6,5,6}
print(set_var)
frozenset = frozenset({1,2,3,4,6})
print(type(set_var), type(frozenset))

# Sets are mutable, unordered collections of unique elements.
# Sets do not allow duplicate elements.
# Sets are represented using curly braces { }.

# Frozensets are immutable counterparts of sets.
# Frozensets are immutable, meaning their elements cannot be changed after the frozenset is created.
# Frozensets are represented using the frozenset() constructor.

# *************************************************************************************************

# Input function
my_name = input("What is your name?")
print("Hello ", my_name)