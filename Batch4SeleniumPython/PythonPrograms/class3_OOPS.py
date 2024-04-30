
# model a waiter - there 2 things -- what waiter has & what it does
# has : is_holding_plate = True
#       is_holding_diary = True
#       tables_responsibile = [4,5,6]
# does: def take_order(table, order):
#             do something
#       def take_payment(amount):
#           do something

# In programming world, we implement what a model has by VARIABLES / ARGUMENTS / PARAMETERS
# we implement what it does by defining METHODS / FUNCTIONS

# waiter - Ram & Shyam
# waiter is the CLASS / BLUEPRINT
# RAM & SHYAMA - Objects

#*****************************************************************************************************

class Animal:
    def __init__(self, species, age):
        self.species = species
        self.age = age
        print("hi")

    def make_sound(self, param):
        """
            just outputs the sound an animal makes

              param
                some random varibale

        """
        self.param = param
        sound = "Some sound"
        # print(sound)
        # return sound
        return param
        # pass

    def get_info(self):
        return f"I am a {self.species} and I am {self.age} years old"


lion = Animal("Lion", 14)
# elephant = Animal("Elephant", 10)

print(lion.make_sound())
# print(lion.get_info())
# print(elephant.get_info())

#*****************************************************************************************************

# str = "Hello, World!"
# print(str.upper())
# print(str.lower())
#
# str = " Hello, World!     "
# print(str.strip())
# print(str.lstrip())
# print(str.rstrip())
#
# text = "apple, cherry, pie, banana"
# fruits = text.split(",")
# print(fruits)
#
# delimiter = "-"
# new_text = delimiter.join(fruits)
# print(new_text)
#
# str = "Hello, World!"
# print(str.startswith("Fell"))
# print(str.endswith("World!"))
#
# print(str.replace("World", "Universe"))
#
# # slicing
# print(str[::-1])

#**************************************************************************