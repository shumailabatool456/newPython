from turtle import Turtle, Screen

timmy = Turtle()
for i in range(4):
    timmy.forward(100)
    timmy.left(90)
timmy.penup()
timmy.forward(200)
timmy.pendown()
for i in range(5):
    timmy.forward(100)
    timmy.left(72)
timmy.penup()
timmy.forward(200)
timmy.pendown()
sides = 10
angle = 360 / sides

for _ in range(sides):
    timmy.forward(100)
    timmy.right(angle)

screen = Screen()
screen.exitonclick()

screen = Screen()
screen.exitonclick()
