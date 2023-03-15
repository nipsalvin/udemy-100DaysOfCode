from turtle import Turtle
import time

STARTING_POSITIONS = [(0,0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
    
    def create_snake(self):
        #TODO 1: Create body
        for position in STARTING_POSITIONS:
            new_position = Turtle('square')
            new_position.penup()
            new_position.color('grey')
            new_position.goto(position)
            self.segments.append(new_position)
            self.segments[0].color('red')

    def move_snake(self):
            for seg in range(len(self.segments)-1, 0, -1):
                x = self.segments[seg -1].xcor()
                y = self.segments[seg -1].ycor()
                self.segments[seg].goto(x, y)
            self.head.forward(MOVE_DISTANCE)
        
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
         

        