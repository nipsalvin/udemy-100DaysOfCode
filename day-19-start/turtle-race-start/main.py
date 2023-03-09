from turtle import Turtle, Screen
import random

racing = False
screen = Screen()
# screen.setup(width=1000, height=1000) ##Using key-value arguments
screen.setup(1000, 1000) ##Using poaitional arguments
# user_choice = screen.textinput(title='Make your bet', prompt='Which turtle will win the race? \n') ##Using key-value arguments
user_choice = screen.textinput('Make your bet', 'Which turtle will win the race? \n') ##Using poaitional arguments
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
y_cor = [-120, -80, -40, 0, 40, 80, 120]
athletes = []
print (user_choice)
# This is for printing multiple turtle objects
for turtles in range(0, 7):
    runner = Turtle("turtle")
    runner.color(colors[turtles])
    runner.speed('fastest')
    runner.penup()
    runner.goto(x=-400, y=y_cor[turtles])
    athletes.append(runner)

if user_choice:
    racing = True

while racing == True:
    for turtle in athletes:
        forward = random.randint(0, 10)
        turtle.forward(forward)
        if turtle.xcor() > 480:
            racing = False
            winner = turtle.pencolor()
            if user_choice == winner:
                print(f'You won! The winning turtle color is the {winner} turtle')
            else:
                print(f'You lost! The winning turtle color is the {winner} turtle')
        


screen.exitonclick()