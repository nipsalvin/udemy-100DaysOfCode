import random
from art import logo

print (logo)
EASY = 10
HARD = 5
level = int(input("Choose a level. 1 for easy and 2 for hard \n"))
number = random.randint(1, 100)  # generate a random number between 1 and 100

if level == 1:
    chances = EASY
elif level == 2:
    chances = HARD

def guess_number():
    global chances
    guess = None
    while guess != number and chances >= 1:
        guess = int(input("Guess a number between 1 and 100: "))
        print(f'guess is {guess}')
        if guess < number:
            print("Too low! Guess again.")
            chances -= 1
            print(f"You have {chances} remaining")
        elif guess > number:
            print("Too high! Guess again.")
            chances -= 1
            print(f"You have {chances} remaining")
    if chances == 0:
        print(f"Game over you have {chances} remaining")
    else:
        print(f"Congratulations! The number was {number}.")

guess_number()