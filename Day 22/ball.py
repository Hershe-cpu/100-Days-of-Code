from turtle import Turtle

class Ball(Turtle):


    def __init__(self):
        super().__init__()
        self.speed("normal")
        self.shape("circle")
        self.color("white")
        self.penup()
        #self.shapesize(stretch_wid=0.7, stretch_len=0.7)
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1


    def move(self):
        self.goto(self.xcor()+self.x_move, self.ycor()+self.y_move)


    def reset(self):
        self.goto(0,0)
        self.move_speed = 0.1
        self.bounce_x()


    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9


    def bounce_y(self):
        self.y_move *= -1


