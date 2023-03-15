from turtle import Turtle, Screen
import random

screen = Screen()
screen.bgcolor("black")
screen.setup(800, 600)
screen.title("Pong Game by @Nips")
screen.tracer(0)

paddle = Turtle()
paddle.color('white')
paddle.shape('square')
paddle.shapesize(5, 1)
paddle.penup()
# paddle.goto(350, 0)
paddle.setposition(350, 0)

def go_up():
    y = paddle.ycor() + 20
    paddle.goto(paddle.xcor(), y)

def go_down():
    y = paddle.ycor() - 20
    paddle.goto(paddle.xcor(), y)


screen.listen()
screen.onkey(go_up, 'Up')
screen.onkey(go_down, 'Down')

game_is_on = True
while game_is_on:
    screen.update()


screen.exitonclick()