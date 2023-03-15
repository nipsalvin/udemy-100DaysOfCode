from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__('circle')
        self.color('white')
        # self.shapesize(20, 20)
        self.penup()
        self.goto(0,0)
    
    def move(self):
        x = self.xcor() + 5
        y = self.ycor() + 5
        if self.xcor() < 390 and self.ycor() < 280:
            self.goto(x, y)