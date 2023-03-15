from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, x, y):
        """Takes X and Y co-ordinates e.g {name = Paddle(180, 0)}"""
        super().__init__()
        self.color('white')
        self.shape('square')
        self.shapesize(5, 1)
        self.penup()
        # paddle.goto(350, 0)
        self.setposition(x, y)
        

    def go_up(self):
        if self.ycor() < 255:
            y = self.ycor() + 20
            self.goto(self.xcor(), y)

    def go_down(self):
        if self.ycor() > -255:
            y = self.ycor() - 20
            self.goto(self.xcor(), y)

