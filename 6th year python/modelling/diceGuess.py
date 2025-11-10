from random import *

def cappedInput(text, cap):
    num = input(text)
    if not num.isdigit():
        num = cappedInput("Sorry, I don't understand. Please input a number.\n > ", cap)
    num = int(num)
    if 1 > num > cap:
        num = cappedInput(f"Sorry, that number is too high. Please input a number between 1 and {cap}.\n > ", cap)
    return num

def ynInput(text):
    yn = input(text).lower()
    if yn != "y" and yn != "n":
        yn = ynInput("Sorry, I don't understand. Please input a Y or N for yes or no.\n > ")
        return yn

dieSize = cappedInput('What size die do you want to roll?\n > ', 100)
guess = cappedInput('What number do you guess will be rolled?\n > ', dieSize)
result = randint(1, dieSize)
print("You guessed right!") if result == guess else print(f"I rolled a {result}.")