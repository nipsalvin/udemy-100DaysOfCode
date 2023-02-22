import random
from art import logo, vs
from game_data import data
# from replit import clear


# 3. format account
def get_data(account):
    """formats the account to a printable format"""
    name = account['name']
    desc = account['description']
    country = account['country']
    return f"{name}, a {desc} from {country}"


# 4. if statement to check if user is correct
def check(ans, a_followers, b_followers):
    """Checks user guess and follower account to compare whether they got it right"""
    if a_followers > b_followers:
        return ans == 'a'
    else:
        return ans == 'b'


def game():
    print(logo)
    game_end = False
    score = 0
    # 8. make option b become a
    ## have b outside the function. then assign it to a
    b = random.choice(data)

    # 7 repeat game
    while game_end == False:
        # 2. generate random account
        ## a gets assigned b and  while in the loop it will always keep geting the previous b while b gets a random value
        a = b
        b = random.choice(data)
        while a == b:
            b = random.choice(data)
        # 1. display logo
        print(f"Compare A: {get_data(a)}")
        print(vs)
        print(f"Against B: {get_data(b)}")
        # 4. ask user for guess
        ans = input("Who has more followers? Type 'A' or 'B': \n").lower()
        # 5. check if answer is correct
        # # get follower count
        a_followers = a['follower_count']
        b_followers = b['follower_count']
        # print(f'{a}, {a_followers}, \n{b}, {b_followers}')

        # 4. if statement to check if user is correct
        is_correct = check(ans, a_followers, b_followers)
        #  print(is_correct)
        # 8. clear the screen
        # clear()
        print(logo)
        # 5. give user feedback
        # 6. keep score
        if is_correct:
            score += 1
            print(f"You're right! Current score:{score}.")
        else:
            print(f"Sorry, that's wrong. Final score: {score}")
            game_end = True


game()
