from player import Turtle

class Level(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.level = 1
        self.goto(-320,250)
        self.write_level()


    def write_level(self):
        self.write(f"Level: {self.level}",align="center",font=("Courier",20,"normal"))


    def increase_level(self):
        self.clear()
        self.level += 1
        self.write_level()

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over",align="center",font=("Courier",25,"normal"))

