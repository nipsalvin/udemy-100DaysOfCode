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
        self.move_speed = 0.1
    
    # TODO 3.2: Create ball
    def move(self):
        x = self.xcor() + self.x_move
        y = self.ycor() + self.y_move
        self.goto(x, y)
    
    # TODO 4: Detect collision with wall and bounce
    def bounce_y(self):
        """Detects collision with top wall and changes direction"""
        self.y_move *= -1
    
    # TODO 5: Detect collision with paddle and bounce
    def bounce_x(self):
        """Detects collision with paddle and changes direction"""
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset_position(self):
        self.goto(0,0)
        self.move_speed = 0.1
        self.bounce_x()
        
        

