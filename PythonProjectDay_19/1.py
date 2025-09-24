from turtle import Turtle, Screen
tim = Turtle()
screen = Screen()
def move_forward():
    tim.forward(10)

def move_backward():
    tim.backward(10)

def turn_left():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)

def turn_right():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)
screen.listen()
def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.onkey(move_forward, "f")
screen.onkey(move_backward, "b")
screen.onkey(turn_right, "r")
screen.onkey(turn_left, "l")
screen.onkey(clear, "c")


screen.exitonclick()