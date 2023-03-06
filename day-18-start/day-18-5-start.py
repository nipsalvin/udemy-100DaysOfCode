import turtle as t
from turtle import Screen
import random

kamtu = t.Turtle()
t.colormode(255)
t.pensize(10)
t.speed('fastest')
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

#TODO Challenge 5 - Spirograph ########
kamtu.speed('fastest')
def draw_spirograph(size_of_gap):
    for i in range(int(360 / size_of_gap)):
        kamtu.setheading(kamtu.heading() + size_of_gap)
        kamtu.color(random_color())
        kamtu.circle(100)

draw_spirograph(10)


screen = Screen()
screen.exitonclick()
