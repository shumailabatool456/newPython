from turtle import Screen
from scoreboard import Scoreboard
from obstacle import Obstacle
from food import Food
from snake import Snake
from powerups import Powerup
import time

food_counter = 0
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()


def change_snake_color():
    for seg in snake.segments:
        seg.color("cyan")


def change_theme():
    screen.bgcolor("pink")

powerups = []

obstacles = [Obstacle() for _ in range(5)]

# controls
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
screen.onkey(snake.restart, "R")
screen.onkey(change_snake_color, "c")
screen.onkey(change_theme, "t")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # wall collision
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

    # food collision
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
        food_counter += 1
        

        if food_counter % 5 == 0:
            powerup = Powerup()
            powerups.append(powerup)

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()


    for obs in obstacles:
        if snake.head.distance(obs) < 20:
            game_is_on = False
            scoreboard.game_over()

    for power in powerups:
        if snake.head.distance(power) < 20:
            power.hideturtle()
            powerups.remove(power)

            scoreboard.increase_powerup_score()

screen.exitonclick()
