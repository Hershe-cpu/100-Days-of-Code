from turtle import Turtle

STARTING_POS = (0,-275)
MOVING_SPEED = 5



class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.setheading(90)
        self.penup()
        self.goto(STARTING_POS)
        self.moving_right = False
        self.moving_left = False
        self.moving_forward = False
        self.moving_backward = False
        self.moving_speed = MOVING_SPEED

    def move(self):
        if self.moving_forward:
            self.sety(self.ycor() + self.moving_speed)

        elif self.moving_backward:
            self.sety(self.ycor() - self.moving_speed)

        elif self.moving_left:
            self.setpos(self.xcor() - self.moving_speed,self.ycor())

        elif self.moving_right:
            self.setpos(self.xcor() + self.moving_speed,self.ycor())

    def start_forward(self):
        self.moving_forward = True

    def stop_forward(self):
        self.moving_forward = False

    def start_backward(self):
        self.moving_backward = True

    def stop_backward(self):
        self.moving_backward = False

    def start_left(self):
        self.moving_left = True

    def stop_left(self):
        self.moving_left = False

    def start_right(self):
        self.moving_right = True

    def stop_right(self):
        self.moving_right = False


    def level_up(self):
        self.goto(STARTING_POS)
