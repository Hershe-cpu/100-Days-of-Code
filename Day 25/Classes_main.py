from turtle import Screen
from oop_Model import StateGame
import pandas as pd

screen = Screen()
screen.setup(width=600,height=600)
screen.bgpic("India Map.png")

game = StateGame()
guessed_states = []

data = pd.read_csv("working_states_data.csv")
states = data.States.tolist()

user_state = screen.textinput(" State input","Enter the state.")
i = 0
while user_state and i<len(data)-1:
    user_state = user_state.title()
    if user_state == "Exit":
        screen.bye()
    elif user_state not in states :
        user_state = screen.textinput(" State doesn't exist. Try Again. ","Enter the state.")
        continue
    elif user_state in guessed_states:
        user_state = screen.textinput(" Already Guessed ","Enter another state.")
        continue
    else:
        some = data[data.States == user_state]
        game.go_pos(some.x.iloc[0],some.y.iloc[0])
        game.write(user_state)
        guessed_states.append(user_state)
        i+=1
        user_state = screen.textinput(" State input", "Enter the state.")

screen.exitonclick()