from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

is_off = False
# TODO 1: Prompt user by asking “What would you like? (espresso/latte/cappuccino):
# TODO 1.1: Prompt should show every time action has completed
drink = input("What would you like? (espresso/latte/cappuccino):\n").lower()
while is_off == False:
    if drink == 'off':
        is_off = True
    elif drink == 'report':
        print('report')

# TODO 2: Turn off the Coffee Machine by entering “off” to the prompt
# TODO 3: Print report.
# TODO 4: Check resources sufficient?
# TODO 5: Process coins.
# TODO 6: Check transaction successful?
# TODO 7: Make Coffee.

