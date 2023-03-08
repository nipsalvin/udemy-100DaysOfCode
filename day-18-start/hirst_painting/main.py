# import colorgram
import turtle as t
from turtle import Screen
import random
# rgb_colors = []
# colors = colorgram.extract('hirst.jpg', 7)

# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)

# print(rgb_colors)

### My solution ###
# color_list = [(199, 175, 117), 
#               (124, 36, 24), (210, 221, 213), (168, 106, 57), (222, 224, 227)]

# kamtu = t.Turtle()
# t.colormode(255)
# y_cor = 20
# for i in range(10):
#     kamtu.penup()
#     kamtu.goto(0,y_cor)
#     y_cor += 50
#     for i in range (10):
#         color = random.choice(color_list)
#         kamtu.dot(20, color)
#         kamtu.forward(50)
    
# # print(kamtu)

# screen = Screen()
# screen.exitonclick()

####### Udemy solution #######
import turtle as turtle_module
import random

turtle_module.colormode(255)
tim = turtle_module.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()
color_list = [(202, 164, 109), (238, 240, 245), (150, 75, 49), (223, 201, 135),
              (52, 93, 124), (172, 154, 40), (140, 30, 19), (133, 163, 185),
              (198, 91, 71), (46, 122, 86), (72, 43, 35), (145, 178, 148),
              (13, 99, 71), (233, 175, 164), (161, 142, 158), (105, 74, 77),
              (55, 46, 50), (183, 205, 171), (36, 60, 74), (18, 86, 90),
              (81, 148, 129), (148, 17, 20), (14, 70, 64),
              (107, 127, 153), (174, 94, 97), (176, 192, 209)]
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen = turtle_module.Screen()
screen.exitonclick()
