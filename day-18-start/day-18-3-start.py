from turtle import Turtle, Screen
import random

kamtu = Turtle()
kamtu.shape("turtle")
kamtu.color("blue")

# def triangle():
#     kamtu.color("black")
#     kamtu.forward(100)
#     kamtu.right(120)
#     kamtu.forward(100)
#     kamtu.right(120)
#     kamtu.forward(100)
#     kamtu.right(120)

# def square():
#     kamtu.color("blue")
#     kamtu.forward(100)
#     kamtu.right(90)
#     kamtu.forward(100)
#     kamtu.right(90)
#     kamtu.forward(100)
#     kamtu.right(90)
#     kamtu.forward(100)
#     kamtu.right(90)

# def pentagon():
#     kamtu.color("red")
#     kamtu.forward(100)
#     kamtu.right(72)
#     kamtu.forward(100)
#     kamtu.right(72)
#     kamtu.forward(100)
#     kamtu.right(72)
#     kamtu.forward(100)
#     kamtu.right(72)
#     kamtu.forward(100)
#     kamtu.right(72)

# def hexagon():
#     kamtu.color("orange")
#     kamtu.forward(100)
#     kamtu.right(60)
#     kamtu.forward(100)
#     kamtu.right(60)
#     kamtu.forward(100)
#     kamtu.right(60)
#     kamtu.forward(100)
#     kamtu.right(60)
#     kamtu.forward(100)
#     kamtu.right(60)
#     kamtu.forward(100)
#     kamtu.right(60)

# triangle()
# square()
# pentagon()
# hexagon()

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
def draw_shape(num_of_sides):
    angle = 360 / num_of_sides
    for i in range(num_of_sides):
        kamtu.forward(100)
        kamtu.right(angle)

for i in range(3, 11):
    kamtu.color(random.choice(colours))
    draw_shape(i)



screen = Screen()
screen.exitonclick()
