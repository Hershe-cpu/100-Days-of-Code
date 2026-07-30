FONT = ("Courier",30,"bold")
ALIGNMENT = "center"

from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self,post):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.score = 0
        self.goto(post)
        self.scores()

    def scores(self):
        self.write(f"{self.score}",align = ALIGNMENT,font=("Courier",40,"bold"))

    def increase_score(self):
        self.clear()
        self.score += 1
        self.scores()

    def dashed_line(self):
        self.color("white")
        self.hideturtle()
        self.speed(0)
        self.penup()
        self.pensize(5)
        self.goto(0, 300)
        self.setheading(90)
        while self.pos() != (0, -300):
            self.pendown()
            self.forward(30)
            self.penup()
            self.forward(20)


    def game_over(self,player):

        self.clear()
        self.goto(0,20)
        self.write(f"Game Over",align=ALIGNMENT,font=("Courier",20,"normal"))
        self.goto(0,-20)
        self.write(f"{player} is Winner: {self.score}",align=ALIGNMENT,font=("Courier",20,"normal"))

