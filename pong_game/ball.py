from turtle import Turtle

# TODO 3: Create ball
class Ball(Turtle):
    def __init__(self):
        super().__init__('circle')
        self.color('white')
        # self.shapesize(20, 20)
        self.penup()
        self.goto(0,0)
        self.x_move = 5
        self.y_move = 5
    
    # TODO 3.2: Create ball
    def move(self):
        x = self.xcor() + self.x_move
        y = self.ycor() + self.y_move
        self.goto(x, y)
    
    # TODO 4: Detect collision with wall and bounce
    def bounce(self):
        """Detects collision with top wall and changes direction"""
        # x = self.xcor() + self.x_move
        # bounce_y = self.ycor() + self.y_move
        # self.goto(x, bounce_y)
        self.y_move *= -1
        
