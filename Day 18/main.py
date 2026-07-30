import turtle
import random
turtle.colormode(255)
screen = turtle.Screen()
tim = turtle.Turtle()
tim.hideturtle()
tim.speed("fastest")
tim.teleport(-200,-200)

screen.title("Hirst Spot Painting")


rgb_color = [(184, 148, 94), (152, 104, 46), (178, 150, 22), (83, 34, 27)]

def draw_dots(tell):
    for _ in range(10):
        color = random.choice(tell)
        tim.penup()
        tim.dot(20, color)
        tim.forward(50)



for _ in range(5):
    draw_dots(rgb_color)
    tim.back(50)
    tim.left(90)
    tim.forward(50)
    tim.left(90)
    draw_dots(rgb_color)
    tim.back(50)
    tim.right(90)
    tim.forward(50)
    tim.right(90)

screen.exitonclick()