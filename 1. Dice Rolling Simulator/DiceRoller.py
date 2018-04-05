from random import *

userInput = input("Do you want to roll the dice? (y/n)")

if (userInput == "y") or (userInput == "n"):
    print(randint(1,6))
else:
    print("Please enter 'y' or 'n'")
