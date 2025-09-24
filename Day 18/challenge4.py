from turtle import Turtle, Screen
import turtle as t
import random

timmy = Turtle()
t.colormode(255)
direction=[0,90,180,270]

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    random_color = (r,g,b,)
    return random_color

for i in range(200):
    timmy.forward(30)
    timmy.setheading(random.choice(direction))
    timmy.color(random_color())
    timmy.pensize(15)
    timmy.speed("fastest")



screen= Screen()
screen.exitonclick()

