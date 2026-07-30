import time
from turtle import Screen
from level import Level
from player import Player
from cars import CarManager

screen = Screen()
screen.setup(width=800,height=600)
screen.colormode(255)
screen.tracer(0)

level = Level()
player= Player()
car_manager = CarManager()

screen.listen()
screen.onkeypress(player.start_forward,"Up")
screen.onkeyrelease(player.stop_forward,"Up")


game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    player.move()

    car_manager.create_car()
    car_manager.move_cars()

    for car in car_manager.all_cars:
        if car.distance(player) <=18:
            game_on = False
            level.game_over()

            break

    if player.ycor() > 275:
        player.level_up()
        level.increase_level()
        car_manager.increase_speed()





screen.exitonclick()
