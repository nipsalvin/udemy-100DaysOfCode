import turtle as t
from turtle import Screen
import random

kamtu = t.Turtle()
kamtu.hideturtle()
t.colormode(255)

def rand_color():
    """Generates a random RGB color to be used"""
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r,g,b)
    return color

#TODO Challenge 4 - Random Walk ########
directions = [0, 90, 180, 270]
kamtu.speed("fastest")
kamtu.pensize(10)

for i in range(100):
    # kamtu.color(random.choice(color))
    # Using random RBG colors
    kamtu.color(rand_color())
    kamtu.forward(30)
    kamtu.setheading(random.choice(directions))

screen = Screen()
screen.exitonclick()