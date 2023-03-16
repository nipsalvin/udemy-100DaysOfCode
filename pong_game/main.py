from turtle import Turtle, Screen
import random
from paddle import Paddle
from ball import Ball
import time

# TODO 1: Create screen
screen = Screen()
screen.bgcolor("black")
screen.setup(800, 600)
screen.title("Pong Game by @Nips")
screen.tracer(0)

# TODO 2.1: Create paddle
r_paddle = Paddle(350, 0)
# TODO 2.2: Create paddle
l_paddle = Paddle(-350, 0)

# TODO 3.1: Create ball
ball = Ball()

screen.listen()
screen.onkey(r_paddle.go_up, 'Up')
screen.onkey(r_paddle.go_down, 'Down')
screen.onkey(l_paddle.go_up, 'w')
screen.onkey(l_paddle.go_down, 's')

game_is_on = True
while game_is_on:
    time.sleep(0.05)
    screen.update()
    ball.move()

    # TODO 5: Detect collision with wall
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bounce()
    


screen.exitonclick()