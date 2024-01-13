from turtle import Screen
from ball import Ball
from paddle import Paddle
from bricks import Bricks
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor('black')
screen.title(titlestring='Break Out Game')
screen.setup(width=600, height=800)
screen.tracer(0)

paddle = Paddle(x=0, y=-300)
ball = Ball()
scores = Scoreboard()
bricks = Bricks()
bricks.create_bricks()

screen.listen()
screen.onkey(paddle.go_left, 'Left')
screen.onkey(paddle.go_right, 'Right')

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.xcor() > 280 or ball.xcor() < -280:
        ball.bounce_x()
    
    # Detect collision with paddle
    if ball.distance(paddle) < 30 and ball.ycor() > -300:
        ball.bounce_y()
        
    if ball.ycor() < -300:
        ball.reset_position()
        scores.update_lives()
        if scores.lives == 0:
            scores.gameover()
            game_is_on = False

    # Detect collision with brick
    for brick in bricks.all_bricks:
        if ball.distance(brick) < 30:
            ball.bounce_y()
            brick.hideturtle()
            bricks.all_bricks.remove(brick)
            scores.update_points()


screen.exitonclick()