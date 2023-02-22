# Calculator
from art import logo
#add
def add(n1, n2):
    return n1 + n2


# Subtract
def subtract(n1, n2):
    return n1 - n2


# Multiply
def multiply(n1, n2):
    return n1 * n2


# Divide
def divide(n1, n2):
    return n1 / n2


operands = {'+': add, '-': subtract, '*': multiply, '/': divide}


def calculator():
    print(logo)
    num1 = float(input("What's the first number ?\n"))
    continuation = True

    for op in operands:
        print(op)

    while continuation == True:
        operation = input("Pick an operation?\n")
        num2 = float(input("What's the next number ?\n"))
        calculation = operands[operation]
        answer = calculation(num1, num2)
        print(f"{num1} {operation} {num2} = {answer}")
        cont = input(
            'Do you want to add another operation?\n y for yes n for no and r for restart\n'
        )
        if cont == 'n':
            continuation = False
        elif cont == 'r':
            calculator()
        else:
            num1 = answer
calculator()