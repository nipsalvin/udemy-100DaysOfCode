import turtle
import pandas

IMAGE = "blank_states_img.gif"

screen = turtle.Screen()
screen.title("U.S States Game")
screen.addshape(IMAGE)
turtle.shape(IMAGE)

game_on = True

correct_answers = []
while game_on:
    answer_state = screen.textinput("Guess the state", "What's another state's name?").title()
    data = pandas.read_csv("50_states.csv")
    answer_state in data["state"]
    # print(correct_answers)
    # print(answer_state)
    # print(state)
screen.exitonclick()