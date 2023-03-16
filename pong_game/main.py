from turtle import Turtle, Screen
import random
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
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

score = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, 'Up')
screen.onkey(r_paddle.go_down, 'Down')
screen.onkey(l_paddle.go_up, 'w')
screen.onkey(l_paddle.go_down, 's')

game_is_on = True
while game_is_on:
    time.sleep(0.03)
    screen.update()
    ball.move()

    # TODO 4.1: Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    
    # TODO 5.1: Detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
    
    # TODO 6: Detect if ball is out of bounds
    if ball.xcor() > 380 :
        ball.reset_position()
    
    if ball.xcor() < -380:
        ball.reset_position()
    



screen.exitonclick()