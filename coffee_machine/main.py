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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
more_orders = True
# TODO 1: Prompt user by asking “What would you like? (espresso/latte/cappuccino):
def coffee():
    global more_orders
    # TODO 1.1: Prompt should show every time action has completed
    while more_orders:
        order = input(f"What would you like? (espresso ${MENU['espresso']['cost']}/latte ${MENU['espresso']['cost']}/cappuccino ${MENU['espresso']['cost']})? : \n").lower()
        # TODO 2: Turn off the Coffee Machine by entering “off” to the prompt
        if order == 'off':
            more_orders = False
            return
        # TODO 3: Print report.
        elif order == 'report':
            print(f"Water is {resources['water']}")
            print(f"Milk is {resources['milk']}")
            print(f"Coffee is {resources['coffee']}")
        # print (f"you have ordered: {order}")
        
def coins(quaters, dimes, nickels, pennies):
    quaters = 100 / 4
    d = 100 / 10
    n = 100 / 20
    p = 100 / 100


# TODO 4: Check resources sufficient?
# TODO 5: Process coins.
# TODO 6: Check transaction successful?
# TODO 7: Make Coffee.
coffee()

