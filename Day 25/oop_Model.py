from turtle import Turtle

class StateGame(Turtle):
    def __init__(self):
        super().__init__()
        self.count = 0
        self.penup()
        self.hideturtle()



    def go_pos(self,x,y):

        self.goto(x,y)


    def state_write(self,entry):
        self.write(entry,align="center",font=("Times New Roman",10,"normal"))