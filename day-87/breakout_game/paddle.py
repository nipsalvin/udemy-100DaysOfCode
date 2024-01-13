from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.color('white')
        self.shape('square')
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.penup()
        self.setposition(x=x,y=y)
    
    def go_right(self):
        if self.xcor() < 255:
            x = self.xcor() + 20
            self.goto(x=x, y=self.ycor())
        
    def go_left(self):
        if self.xcor() > -255:
            x = self.xcor() - 20
            self.goto(x=x, y=self.ycor())