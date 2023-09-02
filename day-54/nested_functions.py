## ********Day 54 Start**********
## Functions can have inputs/functionality/output
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

#******************************************#
##Functions are first-class objects, can be passed around as arguments e.g. int/string/float etc.
#******************************************#

def calculate(calc_function, n1, n2):
    return calc_function(n1, n2)

result = calculate(subtract, 2, 3)
print(result)

#******************************************#
##Functions can be nested in other functions
#******************************************#

def outer_function():
    print("I'm outer") #1 First output when outer_function in called

    def nested_function(): 
        print("I'm inner") #3. I'm inner is printed when nested function is called

    nested_function() #2. Nested function is called

outer_function()

#******************************************#
## Functions can be returned from other functions
#******************************************#

def outer_function():
    print("I'm outer") #2. I'm outer is printed out

    def nested_function():
        print("I'm inner") #5. I'm inner is printed out

    return nested_function #3 nested function is returned and assigned to variable `inner function`

inner_function = outer_function() #1. Outer function is called and assigned to variable `inner function`
inner_function() #4. inner_function (which now contains `nested function`) is called


#******************************************#
## Simple Python Decorator Functions
#******************************************#

import time

def delay_decorator(function):
    def wrapper_function():
        time.sleep(2)
        #Do something before
        function()
        function()
        #Do something after
    return wrapper_function

@delay_decorator
def say_hello():
    print("Hello")

#With the @ syntactic sugar
@delay_decorator
def say_bye():
    print("Bye")

#Without the @ syntactic sugar
def say_greeting():
    print("How are you?")
decorated_function = delay_decorator(say_greeting) # `decorated_function` variable is assinged `delay_decorator` function with `say_greeting` funtion as the argument
decorated_function() # `decorated_function` is called

