from turtle import Turtle, Screen
import random

screen = Screen()
is_race_on = False
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
print(user_bet)

color_list = ["red", "blue", "green", "yellow", "purple", "pink"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []

# Create turtles
for index in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(color_list[index])   # fixed: avoid random.choice here for predictability
    new_turtle.goto(x=-230, y=y_positions[index])
    all_turtles.append(new_turtle)

# Start race
if user_bet:
    is_race_on = True

while is_race_on:

    for racer in all_turtles:
        if racer.xcor() > 230:   # finish line
            is_race_on = False
            winning_color = racer.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")

        # Move turtles forward randomly
        rand_distance = random.randint(0, 10)
        racer.forward(rand_distance)

screen.exitonclick()



