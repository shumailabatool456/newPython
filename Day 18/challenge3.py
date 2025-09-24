from turtle import Turtle, Screen
import random
timmy = Turtle()
colors = ["red", "blue", "green", "orange", "purple", "yellow", "pink", "cyan"]
def draw_shape(num_sides):
    angle = 360 / num_sides
    for i in range(num_sides):
        timmy.forward(100)
        timmy.left(angle)

for shape_side in range(3,10):
    timmy.color(random.choice(colors))
    draw_shape(shape_side)
screen = Screen()
screen.exitonclick()
