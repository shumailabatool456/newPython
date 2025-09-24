from turtle import Turtle, Screen
import turtle as t
import random
timmy = t.Turtle()
t.colormode(255)


def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    color = (r,g,b,)
    return color
timmy.speed("fastest")
def draw_spirograph(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        timmy.color(random_color())
        timmy.circle(100)
        timmy.setheading(timmy.heading() + 10)
draw_spirograph(5)
print(timmy.heading())
screen = t.Screen()
screen.exitonclick()