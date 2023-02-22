from random import randint
import art

EASY_LIVES = 10
HARD_LIVES = 5

def level():
    """User selects a level"""
    level = int(input("Choose a level: For Easy Level type 1. For Hard Level type 2 \n"))
    if level == 1:
        return EASY_LIVES
    elif level == 2:
        return HARD_LIVES
    else:
        print('Invalid Input')

def compare(guess, ans, chances):
        """Compares user answer vs random answer"""
        if guess < ans:
            print('Too low, Try again')
            return chances - 1
        elif guess > ans:
            print('Too high, Try again')
            return chances -1
        else:
            print(f"You got it. The answer was {ans}")

def game():
    print(art.logo)
    print("Welcome to the number guessing game")
    print("I'm thinking of a number between 1 and 100")
    #Choosing a random number between 1 and 100.
    ans = randint(1,100)
    chances = level()
    guess = 0
    while guess != ans:
        print(f"You have {chances} remaining")
        #Let the user guess a number.
        guess = int(input("Make a guess: "))
        #Track the number of turns and reduce by 1 if they get it wrong.
        chances = compare(guess, ans, chances)
        if chances == 0:
            print(f"You've run out of guesses. The answer was {ans}. you lose.")
            return
        elif guess != ans:
            print("Guess again.")
        
game()
        
