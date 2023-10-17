import turtle
from turtle import Turtle, Screen
import pandas as pd

# Screen setup
screen = Screen()
screen.title("U.S. States Game")
screen.setup(730, 495)
image = "blank_states_img.gif"
screen.addshape(image)
# Makes background USA
turtle.shape(image)

# Reads CSV FILE
data = pd.read_csv("50_states.csv")

# Starts turtle to make it as text and variable to store amount of right answers
state = Turtle()
count = 0
states_guessed = []

game_is_on = True
while game_is_on:

    user_answer = turtle.textinput(f"{count}/50 States Correct ", "Enter state: ").title()
    # Checks if answer from user is true
    answer_true = data.state.isin([user_answer]).any()

    if answer_true:
        count += 1
        states_guessed.append(user_answer)
        # Gets the data from the state
        state_data = data[data.state == user_answer]
        x_coordinates = state_data["x"].values[0]
        y_coordinates = state_data["y"].values[0]
        state.hideturtle()
        state.penup()
        state.goto(x_coordinates, y_coordinates)
        state.write(user_answer)
    elif user_answer == "Exit" or count > 49:
        states_not_guessed = data[~data['state'].isin(states_guessed)]
        states_to_learn = pd.DataFrame(states_not_guessed, columns=["state"])
        states_to_learn.to_csv("states_to_learn.csv", index=False)
        game_is_on = False
        break

screen.bye()