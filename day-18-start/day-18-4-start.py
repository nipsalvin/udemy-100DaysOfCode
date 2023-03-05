import turtle as t
from turtle import Screen
import random

kamtu = t.Turtle()
kamtu.hideturtle()
# kamtu.shape("turtle")

#TODO Challenge 4 - Random Walk ########
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
directions = [0, 90, 180, 270]
kamtu.speed("fastest")
kamtu.pensize(10)

for i in range(100):
    kamtu.forward(30)
    kamtu.setheading(random.choice(directions))
    kamtu.color(random.choice(colours))



screen = Screen()
screen.exitonclick()