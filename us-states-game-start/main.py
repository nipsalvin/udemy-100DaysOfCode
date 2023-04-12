import turtle
import pandas

IMAGE = "blank_states_img.gif"

screen = turtle.Screen()
screen.title("U.S States Game")
screen.addshape(IMAGE)
turtle.shape(IMAGE)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []
score = 0

while len(guessed_states) < 50:
    t = turtle.Turtle()
    t.penup()
    t.hideturtle()
    answer_state = screen.textinput(f"{len(guessed_states)}/50 states correct", "What's another state's name?").title()
    if answer_state == 'Exit':

        missing_states = [state for state in all_states if state not in guessed_states]
        # missing_states = []
        # for state in all_states:
        #     if state not in guessed_states:
        #         missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv('states_to_learn.csv')
        break
    for check in data.state:
        if answer_state == check and answer_state not in guessed_states:
            guessed_states.append(answer_state)
            score += 1
            """Get the row of data"""
            state_data = data[data.state == answer_state]
            t.goto(int(state_data.x), int(state_data.y))
            # print(score)
            # print(correct_answers)
            t.write(answer_state)

    # print(answer_state)
    # print(state)