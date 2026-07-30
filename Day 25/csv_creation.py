from turtle import Screen, Turtle
import pandas as pd

screen = Screen()
screen.bgpic("India Map.png")
screen.setup(width=600,height=600)

count =0
data_dict = {
            "States": [],
            "x":[],
            "y":[],
        }


data = pd.read_csv("states_data.csv")
states_list = data["States"].tolist()
state = Turtle()
state.hideturtle()
state.penup()


def write_state(x,y):
    global count
    if count >= len(states_list):
        return
    input_state = states_list[count]

    state.goto(x,y)
    state.write(input_state, align="center", font=("Arial", 10, "normal"))
    data_dict["States"].append(input_state)
    data_dict["x"].append(x)
    data_dict["y"].append(y)
    count+=1
    if count >= len(states_list):
        df = pd.DataFrame(data_dict)
        df.to_csv("working_states_data.csv", index=False)
        screen.onclick(None)
        screen.bye()


screen.onclick(write_state)
screen.mainloop()