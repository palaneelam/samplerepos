# Importing Modules / package
# Write a Python program to import the math module and demonstrate its usage.

import math as m
import random
from datetime import datetime

# class TestOne:
# print("Square root is:",math.sqrt(36))
# print("Pi value is:",math.pi)

# Write a Python program to create a user-defined module and import it into another Python program.
def greet(name):
    print("Hello ", name,"!")

# Write a Python program to import the datetime module and demonstrate its usage.
print("Current date and time: ",datetime.now())

# Write a Python program to import the random module and generate random numbers.
random_number = random.random() # generate random nbrs between 0 and 1
print("Random number:", random_number)

random_number = random.randint(0,1)
print("Random number:", random_number)

random_choice = random.choice(['apple','banana','watermelon', 'mango'])
print("Random choice:", random_choice)


# Write a Python program to import a module and alias it with a different name.
print("Square root is:",m.sqrt(36))
print("Pi value is:",m.pi)

#**********************************************************************************************************
# Project:
# Function to check user's guess against actual answer  ---- done
# Choosing a random number between 1 and 100.
# Make function to set difficulty ---- done
# Let the user guess a number
# Function to check user's guess against actual answer
# Track the number of turns and reduce by 1 if they get it wrong.
# Repeat the guessing functionality if they get it wrong.
# ***********************************************************************************************

def set_difficulty():
    difficulty = input("Choose difficulty level: 'easy' or 'hard': ").lower()
    if difficulty == 'easy':
        # chances = 10
        return 10
    elif difficulty == 'hard':
        return 5
    else:
        print("Invalid difficulty level! Setting to default (easy).")
        return 10


def check_guess(number, guess, turns):
    if guess == number:
        print(f"Congratulation! You guessed number {number} correctly!")
        return True
    elif guess < number:
        print("Too low, Guess again!")
    else:
        print("Too high, Guess again!")
    return False

def guess_the_number():
    """This is Guess the number Game. Play it and enjoy it! """
    print("Welcome to Guess the number game!")
    print("Hey Buddy, I am thinking of a number between 1 and 100.... \n Now I have made a choice.")
    number = random.randint(1,100)
    turns = set_difficulty()

    while turns > 0:
        print(f"You have {turns} attempts remaining to guess the number.")
        guess = int(input("Make a guess:"))
        if check_guess(number, guess, turns):
            break
        turns -= 1
    else:
        print(f"Sorry, you have run out of attempts. The correct number was {number}")


guess_the_number()

# https://hangmanwordgame.com/?fca=1&success=0#/round-results

word_list = ['apple','banana','watermelon', 'mango']
chosen_word = random.choice(word_list)
print("chosen word:", chosen_word)
display=[]
for letter in chosen_word:
    display += '_'
print(display)