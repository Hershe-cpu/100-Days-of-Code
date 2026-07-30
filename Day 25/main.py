from turtle import Screen,Turtle
import pandas as pd


screen = Screen()
screen.setup(width=600,height=600)
screen.bgpic("India Map.png")

data = pd.read_csv("working_states_data.csv")
states = data["States"].tolist()
guessed_states = []

t=Turtle()
t.hideturtle()
t.penup()

def game_function():

    user_state = screen.textinput(f"{len(guessed_states)}/{len(data)} State Guessed","Enter the state.")

    while user_state and len(guessed_states)<len(states):

        user_state = user_state.title()
        if user_state == "Exit":
            break

        elif user_state not in states or user_state in guessed_states:
            user_state = screen.textinput("State Input","Try Again. Enter the state.")
            continue
        else:
            xyz = data[data["States"] == user_state]

            x = xyz["x"].iloc[0]
            y = xyz["y"].iloc[0]


            t.goto(x,y)
            t.write(user_state,align="center",font=("Times New Roman",10,"normal"))
            guessed_states.append(user_state)

            user_state = screen.textinput(f"{len(guessed_states)}/{len(data)} State Guessed","Enter the state.")


    missed_states = [state for state in states if state not in guessed_states]
    df = pd.DataFrame(missed_states)
    df.to_csv("states_to_learn.csv",index=False)


game_function()
