from turtle import Turtle
import random

# TODO 3: Create food
class Food(Turtle):
    def __init__(self):
        """Creates food as a turtle object"""
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(0.5, 0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()
        
    def refresh(self):
        """changes the position of the the food object anytime it is called"""
        pos_x = random.randint(-280, 280)
        pos_y = random.randint(-280, 280)
        self.goto(pos_x, pos_y)