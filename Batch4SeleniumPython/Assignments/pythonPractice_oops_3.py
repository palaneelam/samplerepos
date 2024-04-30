# Create a Python class representing a car with attributes like make, model, and color.
class Car:
    def __init__(self, makes, model, color):
        self.make = makes
        self.model = model
        self.color = color

car1 = Car("Toyota", "Camry", "Red")
car2 = Car("Honda", "Accord", "Blue")

# Add methods to the car class to start the car, stop the car, and accelerate.
# class Car:
#     def __init__(self, makes, model, color):
#         self.make = makes
#         self.model = model
#         self.color = color
#         self.is_running = False
#
#     def start(self, model):
#         self.is_running = True
#         print(model,"Car started")
#
#     def stop(self):
#         self.is_running = False
#         print("Car Stopped")
#
#     def accelerate(self):
#         if self.is_running:
#             print("Car is accelrating")
#         else:
#             print("Some Issue, Car cannot accelearte")
#
#
# # car1 = Car("Toyota", "Camry", "Red")
# # car1.start()
# # car1.accelerate()
# # car1.stop()
#
# # Create instances of the car class and demonstrate method calls.
# car1 = Car("Toyota", "Camry", "Red")
# car2 = Car("Honda", "Accord", "Blue")
# car1.start("Camry")
# car1.accelerate()
# car1.stop()
#
# car2.start("Accord")
# car2.accelerate()
# car2.stop()

# Write a Python program to demonstrate inheritance with a base class and a derived class.
class Vehicle:
    def __init__(self, make, model, color):
        self.make = make
        self.model = model
        self.color = color

    def start(self):
        print("Vehicle started")

class Car(Vehicle):
    def accelerate(self):
        print("Car accelerating")

car = Car("Toyota", "Camry", "Red")
car.start()
car.accelerate()

# Write a Python program to demonstrate polymorphism with class methods.
class Animal:
    def speak(self):
        print("Animal barks")

class Dog(Animal):
    # pass
    def speak(self):
        print("Dog barks")


class Cat(Animal):
    def speak(self):
        print("Cat meows")

dog = Dog()
cat = Cat()
dog.speak()
cat.speak()
