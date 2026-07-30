import csv

FONT = ("Courier",20,"normal")
ALIGNMENT = "center"

from turtle import Turtle
class Scoreboard(Turtle):
    score = 0
    def __init__(self):
        super().__init__()
        with open ("my_file.txt","r") as f:
            data = f.read()
        self.high_score = data
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0,270)
        self.scores()

    def scores(self):
        self.clear()
        self.write(f"Score: {Scoreboard.score} High Score: {self.high_score}",align=ALIGNMENT,font=FONT)

    def update_score(self):
        Scoreboard.score += 1
        self.scores()

    # def game_over(self):
    #     self.clear()
    #     self.goto(0,20)
    #     self.write(f"Game Over",align=ALIGNMENT,font=FONT)
    #     self.goto(0,-20)
    #     self.write(f"Final Score: {Scoreboard.score}",align=ALIGNMENT,font=FONT)


    def reset(self):
        if Scoreboard.score > int(self.high_score):
            self.high_score = self.score
            with open("my_file.txt","w") as f:
                f.write(f"{self.high_score}")
        Scoreboard.score = 0
        self.scores()

