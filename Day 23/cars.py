import time
from turtle import Turtle,Screen
import random

STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 3


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_chance = random.randint(1,6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.penup()
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            y_cor = random.randint(-230, 250)
            new_car.goto(430, y_cor)
            self.all_cars.append(new_car)


    def move_cars(self):
        for car in self.all_cars:
            car.goto(car.xcor()-self.speed, car.ycor() )

    def increase_speed(self):
        self.speed += MOVE_INCREMENT