from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffeemaker = CoffeeMaker()
moneymachine = MoneyMachine()

is_off = False

while is_off == False:
    # TODO 1: Prompt user by asking “What would you like? (espresso/latte/cappuccino):
    # TODO 1.1: Prompt should show every time action has completed
    choice = input(f"What would you like? {menu.get_items()}:\n").lower()
    # TODO 2: Turn off the Coffee Machine by entering “off” to the prompt
    if choice == 'off':
        is_off = True
    # TODO 3: Print report.
    elif choice == 'report':
        coffeemaker.report()
        moneymachine.report()
    else:
        drink = menu.find_drink(choice)
        # TODO 4: Check resources sufficient? # TODO 5: Process coins. # TODO 6: Check transaction successful?
        if coffeemaker.is_resource_sufficient(drink) and moneymachine.make_payment(drink.cost):
            # TODO 7: Make Coffee.
            coffeemaker.make_coffee(drink)


