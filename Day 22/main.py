SCREEN_DIMENSION = {"width":800, "height":600}

from turtle import Screen, Turtle
from ball import Ball
from scoreboard import Scoreboard
from paddle import Paddle
import time

screen = Screen()

screen.setup(SCREEN_DIMENSION["width"], SCREEN_DIMENSION["height"])
screen.bgcolor("black")
screen.title("Pong Game")
left_player = screen.textinput("Player Entry", "Enter Left Player name")
right_player = screen.textinput("Player Entry", "Enter Right Player name")

screen.tracer(0)

def dashed_line():
    line= Turtle()
    line.hideturtle()
    line.color("white")
    line.speed(0)
    line.penup()
    line.pensize(3)
    line.goto(0, SCREEN_DIMENSION["height"]/2)
    line.seth(270)
    while line.ycor() >= -SCREEN_DIMENSION["height"]/2:
        line.pendown()
        line.forward(30)
        line.penup()
        line.forward(20)

dashed_line()


ball = Ball()
Lscoreboard1 = Scoreboard((-100,240))
Rscoreboard2 = Scoreboard((+100, 240))
Rplayer1 = Paddle((350,0))
Lplayer2 = Paddle((-350,0))


screen.listen()

screen.onkeypress(Rplayer1.start_forward, "w")
screen.onkeyrelease(Rplayer1.stop_forward,"w")
screen.onkeypress(Rplayer1.start_backward, "s")
screen.onkeyrelease(Rplayer1.stop_backward,"s")


screen.onkeypress(Lplayer2.start_forward, "Up")
screen.onkeyrelease(Lplayer2.stop_forward,"Up")
screen.onkeypress(Lplayer2.start_backward, "Down")
screen.onkeyrelease(Lplayer2.stop_backward,"Down")

if left_player and right_player:
    game_on = True
    while game_on:
        time.sleep(ball.move_speed)
        screen.update()
        Rplayer1.move()
        Lplayer2.move()
        ball.move()

        if ball.distance(Lplayer2) < 50 and ball.xcor() <-320 :
            ball.bounce_x()

        elif ball.distance(Rplayer1) < 50 and ball.xcor() >320 :
            ball.bounce_x()


        if ball.xcor()<-410:
            Rscoreboard2.increase_score()
            ball.reset()
        if ball.xcor()>410:
            Lscoreboard1.increase_score()
            ball.reset()

        if ball.ycor() > 280 or ball.ycor() < -280:
            ball.bounce_y()

        if Lscoreboard1.score == 10:
            Lscoreboard1.game_over(left_player)
            game_on = False
        if Rscoreboard2.score == 10:
            Rscoreboard2.game_over(right_player)
            game_on = False

screen.exitonclick()