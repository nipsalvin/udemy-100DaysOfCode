from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__(shape='circle')
        self.color('white')
        self.penup()
        self.goto(x=0, y=0)
        self.x_move = 5
        self.y_move = 5
        self.move_speed = 0.1
    
    def move(self):
        '''Gets current coordinates of the ball and moves it according to the y_move variable'''
        x = self.xcor ()+ self.x_move
        y = self.ycor() + self.y_move
        self.goto(x=x, y=y)
    
    def bounce_y(self):
        '''This function changes vertical direrection of the ball when called'''
        self.y_move *= -1
        self.move_speed *= 0.95

    def bounce_x(self):
        '''This function changes the lateral direction of the ball when called'''
        self.x_move *= -1

    def reset_position(self):
        self.goto(x=0,y=-280)
        self.move_speed = 0.1
        self.bounce_y()

