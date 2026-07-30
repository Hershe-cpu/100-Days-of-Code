from turtle import Screen
Screen().setup(width=800, height=600)
from racer import Racer

Race1 = Racer()
print(Race1.register())
Race1.create_turtle()
Race1.assign_position()
print(Race1.start_race())


Screen().exitonclick()