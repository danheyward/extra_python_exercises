# Guessing Game

# Create a program that asks the user to guess a number between 1 and 100.

# Once the user guesses a number, the program should say, higher, lower, or
# tell the user that he got the number correct. The user should continue to
# make guesses until he guesses correctly. Also, once the user guesses correctly,
# the program should print the number of guesses needed to arrive at the correct answer.

# Below is sample output:


# Guess a number between 1 and 100
# 50 <-- user input
# The number is lower than 50.  Guess again
# 25
# The number is lower than 25.  Guess again
# 13
# The number is higher than 13.  Guess again
# 20
# The number is lower than 20.  Guess again
# 17
# The number is higher than 17.  Guess again
# 18
# The number is higher than 18.  Guess again
# 19
# You got it in 7 tries


# HINT:
# To get input from a user use the input() method:
# num_of_cookies = input("How many cookies should I eat?")
# num = int(num)

# This will assign the typed input value to your variable as a number


# *** your code here ***
from random import *

def guess_num():
    answer = randint(1, 100)
    guess = int(input("I'm thinking of a number between 1 and 100. What is it? "))
    turns = 1
    if guess == answer:
        print(f"That's right! The correct number is {answer}. You only needed 1 guess, well done.")
    else:
        while guess != answer:
            turns += 1
            if guess > answer:
                guess = int(input(f"The correct number is lower than {guess}! Try again."))
            else:
                guess = int(input(f"The correct number is higher than {guess}! Try again."))
        print(f"That's right! The correct number is {answer}. You only needed {turns} guesses, well done.")

guess_num()
