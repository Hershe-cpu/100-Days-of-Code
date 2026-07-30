MOVING_SPEED = 5

from turtle import Turtle

class Paddle(Turtle):

    def __init__(self,pos):
        super().__init__()
        self.shape("square")
        self.MOVING_FORWARD = False
        self.MOVING_BACKWARD = False
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=5,stretch_len=1)
        self.goto(pos)



    def move(self):

        if self.MOVING_FORWARD:
            self.sety(self.ycor() + MOVING_SPEED)

        elif self.MOVING_BACKWARD:
            self.sety(self.ycor() - MOVING_SPEED)



    def start_forward(self):

        self.MOVING_FORWARD = True

    def stop_forward(self):

        self.MOVING_FORWARD = False

    def start_backward(self):

        self.MOVING_BACKWARD = True

    def stop_backward(self):

        self.MOVING_BACKWARD = False

