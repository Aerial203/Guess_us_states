import turtle
import pandas
screen = turtle.Screen()
screen.title("U.S. states game")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
guessed_state = []

states_data = pandas.read_csv("50_states.csv")
all_states = states_data.state.to_list()

total_answer = len(all_states)
t = turtle.Turtle()
t.penup()
t.hideturtle()


while len(guessed_state) < 50:
    answer_state = turtle.textinput(title=f"{len(guessed_state)}/{total_answer} states correct",
                                    prompt="What's another state's name?").title()

    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in guessed_state]
        missing_data = pandas.DataFrame(missing_states)
        missing_data.to_csv("state_to_learn.csv")
        break

    if answer_state in all_states:
        guessed_state.append(answer_state)
        data = states_data[states_data["state"] == answer_state]
        x_cor = int(data.x)
        y_cor = int(data.y)
        t.goto(x_cor, y_cor)
        t.write(answer_state)
