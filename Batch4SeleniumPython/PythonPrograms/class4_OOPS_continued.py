# Encapsulation: is the practice of bundling data and methods that operate on the data within a single unit.
# it will help in organising code and preventing accidental modification of data.

# Inheritance: allows a class to inherit properties and behaviours from another class.

from PythonPrograms.BaseClass import TestOne


class TestInheritance(TestOne):
    aa = TestOne(2)
    aa.printMessage()
    print("Welcome to Main Class")

# Polymorphism: is the ability of different objects to responds to the same methods
# overloading & overriding

# class Animal:
#     def speak(self):
#         print("Animal speaks")
#
# class Dog(Animal):
#     def speak(self):
#         print("Dog braks")
#
# class Cat(Animal):
#     def speak(self):
#         print("Cat meows")
#
# dog = Dog()
# dog.speak()
# cat = Cat()
# cat.speak()