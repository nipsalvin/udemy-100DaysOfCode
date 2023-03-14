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
        """USes create_snake function to create an snake"""
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
    
    #TODO 1: Create body
    def create_snake(self):
        """Created the segments of the snake and their characteristics"""
        for position in STARTING_POSITIONS:
            self.add_segment(position)
            

    def add_segment(self, position):
        new_position = Turtle('square')
        new_position.penup()
        new_position.color('grey')
        new_position.goto(position)
        self.segments.append(new_position)
        self.segments[0].color('red')

    def extend(self):
        self.add_segment(self.segments[-1].position())

    # TODO 2: Move snake
    def move_snake(self):
            """moves the snake by moving the `behind` segment to the position of the segment infront of it """
            for seg in range(len(self.segments)-1, 0, -1):
                x = self.segments[seg -1].xcor()
                y = self.segments[seg -1].ycor()
                self.segments[seg].goto(x, y)
            self.head.forward(MOVE_DISTANCE)
        
    def up(self):
        """If the direction is DOWN then UP won't work"""
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    
    def down(self):
        """If the direction is UP then DOWN won't work"""
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        """If the direction is RIGHT then LEFT won't work"""
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        """If the direction is LEFT the RIGHT won't work"""
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
         

        