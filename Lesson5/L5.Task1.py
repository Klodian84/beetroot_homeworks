
# The Guessing program.

import random

secret_number = random.randint(1, 10)

user_guess = int(input("Guess a number between 1 and 10: "))

if user_guess != secret_number:
    print("Your guess is wrong. Try again.")

elif user_guess == secret_number:
    print("Congrats! You guessed the correct number!")


