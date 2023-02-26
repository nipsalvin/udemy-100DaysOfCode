MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

# TODO 4: Check resources sufficient?
def resources_sufficient(order_ingredients):
    """Checks whether there are enough resources for the ordered drink"""
    for ingredient in order_ingredients:
        if order_ingredients[ingredient] >= resources[ingredient]:
            print(f"Sorry there is not enough {ingredient}.")
            return False
    return True

# TODO 5: Process coins.
def coins():
    """Returns total value of coins inserted"""
    print('Please insert coins')
    quaters = int(input('how many quarters?:')) *0.25
    dimes = int(input('how many dimes?:')) *0.10
    nickels = int(input('how many nickels?:')) *0.05
    pennies = int(input('how many pennies?:')) *0.01
    total = round(sum([quaters, dimes, nickels, pennies]), 2)
    return total

# TODO 7: Make Coffee.
def make_coffee(drink_ordered, ingredients):
    """Deducts ingredients used from resources"""
    for ingredient in ingredients:
        resources[ingredient] -= ingredients[ingredient]
    print(f"Here is your {drink_ordered}")

# TODO 6: Check transaction successful?
def is_transaction_successful(money_received, drink_cost):
    """Checks if coins inputed are enough and adds to profits. Returns false if money is insufficient"""
    global profit
    if money_received > drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} dollars in change.")
        profit += drink_cost
        return True
    else:
        print(f"Sorry that's not enough money. ${money_received} refunded.")

is_on = True
# TODO 1: Prompt user by asking “What would you like? (espresso/latte/cappuccino):
def coffee():
    global is_on
    # TODO 1.1: Prompt should show every time action has completed
    while is_on:
        order = input(f"What would you like? (espresso ${MENU['espresso']['cost']}/latte ${MENU['latte']['cost']}/cappuccino ${MENU['cappuccino']['cost']})? : \n").lower()
        # TODO 2: Turn off the Coffee Machine by entering “off” to the prompt
        if order == 'off':
            is_on = False
            return
        # TODO 3: Print report.
        elif order == 'report':
            print(f"Water is {resources['water']} ml")
            print(f"Milk is {resources['milk']} ml")
            print(f"Coffee is {resources['coffee']} ml")
            print(f"Money is ${profit}")
        # print (f"you have ordered: {order}")
        else:
            drink = MENU[order]
            if resources_sufficient(drink['ingredients']):
            # if (MENU[order]['ingredients']['water'] < resources["water"] and
            #     MENU[order]['ingredients']['milk'] < resources["milk"]and
            #     MENU[order]['ingredients']['coffee'] < resources["coffee"]):
                # print(f"{drink['ingredients']}")
                payment = coins()
                print (f"Total cash received is ${payment}")
                if is_transaction_successful(payment,MENU[order]["cost"]):
                    make_coffee(order, drink["ingredients"])
        # print(coins())

# TODO 7: Make Coffee.
# coffee()
coffee()


