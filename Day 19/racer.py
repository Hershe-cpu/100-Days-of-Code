import random
from turtle import Screen, Turtle
Screen().setup(width=800, height=600)

class Racer:

    def __init__(self):
        self.all_participants = []
        self.all_turtles = []
        self.height = 600
        self.width = 800
        self.user_guess = ""


    def register(self):
        while True:
            participant = Screen().textinput(
                title="Register Your Turtle for the race.",
                prompt="Enter the participant name."
            )
            if participant is None:
                break
            elif participant in self.all_participants:
                print("Participant already registered.")

            elif participant.lower() == "done":
                if not self.all_participants:
                    print("No participants registered.")
                    continue
                self.user_guess = Screen().textinput("Take your Bid", "Please guess the winner of the race.")

                break
            self.all_participants.append(participant)

        return f"Your guess: {self.user_guess} \nAll Participants: {self.all_participants}"

    def create_turtle(self):
        colors = ["red", "green", "blue", "yellow", "orange", "purple", "brown","pink","black"]
        for i,participant in enumerate(self.all_participants):
            turtle = Turtle()
            turtle.penup()
            turtle.shape("turtle")
            turtle.color(colors[i])
            turtle.participant_name = participant
            self.all_turtles.append(turtle)

        return self.all_turtles

    def assign_position(self):

        no_of_participants = len(self.all_turtles)
        if no_of_participants == 1:
            self.all_turtles[0].goto(-((self.width/2)-50),0)
        else:
            y_cor = -250
            calc = (self.height - 100) / (no_of_participants-1)
            for turtle in self.all_turtles:
                turtle.goto(-((self.width/2)-50),y_cor)
                y_cor+=calc

    def start_race(self):
        race_on = True
        while race_on:
            for racer in self.all_turtles:
                racer.forward(random.randint(0, 50))

                if racer.xcor() >= (self.width/2)-20:
                    race_on = False
                    if self.user_guess.lower() == racer.participant_name.lower():
                        return f"You WIN.\nThe Winner is {racer.participant_name}"
                    return f"You lose.\nThe Winner is {racer.participant_name}"

