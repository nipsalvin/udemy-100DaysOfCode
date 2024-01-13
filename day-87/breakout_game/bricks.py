from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]

class Bricks(Turtle):
    def __init__(self):
        super().__init__()
        self.all_bricks = []
        self.hideturtle()
    
    def create_bricks(self):
        y = 100
        for color in COLORS:
            x = -265
            y += 25
            while x < 300:
                brick = Turtle(shape='square')
                brick.color(color)
                brick.shapesize(stretch_wid=1, stretch_len=3)
                brick.penup()
                brick.goto(x,y)
                self.all_bricks.append(brick)
                x += 65

