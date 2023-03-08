from turtle import Turtle, Screen

kamtu = Turtle()
screen = Screen()


def move_forwards():
    kamtu.forward(10)
#TODO Create an onkey event with 'w' as forward 's' as back 'a' as anti-clockwise 'd' clockwise
def move_bacwards():
    kamtu.backward(10)

def turn_right():
    kamtu.right(45)

def turn_left():
    kamtu.left(45)

def reset():
    """Delete the turtle's drawings from the screen, re-center the turtle and set variables to the default values"""
    kamtu.reset()

def clear():
    """Delete the turtle's drawings from the screen. Doesn't move turtle. 
    State and position of the turtle as well as drawings of other turtles are not affected."""
    kamtu.clear()
    kamtu.penup()
    kamtu.home()
    kamtu.pendown()

screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_bacwards)
screen.onkey(key="d", fun=turn_right) #you can either use this format
screen.onkey(turn_left, "a") #or this format
screen.onkey(reset, "r")
screen.onkey(clear, "c")
screen.exitonclick()