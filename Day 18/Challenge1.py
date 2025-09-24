from turtle import Turtle, Screen

timmy = Turtle()
#for i in range(4):
#    turtle.forward(100)
#    turtle.right(90)

for i in range (7):
    timmy.forward(10)
    timmy.penup()
    timmy.forward(10)
    timmy.pendown()
    timmy.forward(10)

screen = Screen()
screen.exitonclick()
#import heroes
#print(heroes.gen())
#import villains
#print(villains.gen())