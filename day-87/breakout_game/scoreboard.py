from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.lives = 3
        self.update()
    
    def update(self):
        self.clear()
        self.goto