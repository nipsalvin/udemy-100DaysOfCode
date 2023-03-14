from turtle import Turtle, Screen
import random
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(600, 600)
screen.bgcolor('black')
screen.title('My snake game')
screen.tracer(0)

starting_positions = [(0,0), (-20, 0), (-40, 0)]
segments = []
score = 0

snake = Snake()
food = Food()
score = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move_snake()

    # TODO 4: Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        score.count()
        snake.extend()

    # TODO 6: Detect collision with food
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        score.game_over()
    
    # TODO 7: Detect collision with self
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            score.game_over()


       

screen.exitonclick()
