from turtle import Turtle
import random

class Obstacle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("blue")
        self.shapesize(stretch_wid=1, stretch_len=3)
        x = random.randint(-200, 200)
        y = random.randint(-200, 200)
        self.goto(self.xcor(), self.ycor())
