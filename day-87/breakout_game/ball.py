from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__(shape='circle')
        self.color('white')
        self.penup()
        self.move_speed = 0.1