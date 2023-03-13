from turtle import Turtle, Screen
import random
import time
from snake import Snake

screen = Screen()
screen.setup(600, 600)
screen.bgcolor('black')
screen.title('My snake game')
screen.tracer(0)

starting_positions = [(0,0), (-20, 0), (-40, 0)]
segments = []

snake = Snake()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# TODO 2: Move snake
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move_snake()
    

       

screen.exitonclick()
