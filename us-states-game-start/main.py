import turtle
import pandas

IMAGE = "blank_states_img.gif"

screen = turtle.Screen()
screen.title("U.S States Game")
screen.addshape(IMAGE)
turtle.shape(IMAGE)

guessed_state = []
score = 0
while len(guessed_state) < 50:
    t = turtle.Turtle()
    t.penup()
    t.hideturtle()
    answer_state = screen.textinput(f"{len(guessed_state)}/50 states correct", "What's another state's name?").title()
    data = pandas.read_csv("50_states.csv")
    for check in data.state:
        if answer_state == check and answer_state not in guessed_state:
            guessed_state.append(answer_state)
            score += 1
            """Get the row of data"""
            state_data = data[data.state == answer_state]
            t.goto(int(state_data.x), int(state_data.y))
            # print(score)
            # print(correct_answers)
            t.write(answer_state)

    # print(answer_state)
    # print(state)
screen.exitonclick()