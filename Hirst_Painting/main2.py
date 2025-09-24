import colorgram

#rgb_colors =[]
#colors = colorgram.extract('image.jpg', 30)
#for color in colors:
    #r = color.rgb.r
    #g = color.rgb.g
    #b = color.rgb.b
    #new_color = (r, g, b)
    #rgb_colors.append(new_color)
#print(rgb_colors)
import turtle as turtle_module
from turtle import Screen
import random
import turtle as turtle_module
from turtle import Screen
import random
turtle_module.colormode(255)
timmy = turtle_module.Turtle()
timmy.hideturtle()
timmy.penup()
color_list = [ (216, 237, 248), (234, 220, 96), (174, 81, 22), (236, 48, 85), (233, 162, 89), (69, 187, 230), (171, 54, 106), (250, 54, 16), (93, 197, 129), (231, 128, 155), (111, 218, 246), (123, 233, 208), (19, 126, 212), (51, 121, 41), (249, 222, 0), (22, 178, 214), (247, 144, 156), (54, 177, 84), (83, 24, 34), (95, 39, 18), (29, 88, 36), (187, 23, 13), (30, 65, 37), (186, 18, 32), (245, 160, 151), (178, 135, 38), (254, 5, 18)]
timmy.setheading(225)
timmy.forward(300)
timmy.setheading(0)
timmy.speed("fastest")
no_of_dots = 100

for dot_count in range(1, no_of_dots+1):
    timmy.dot(20, random.choice(color_list))
    timmy.forward(30)
    if dot_count % 10 == 0:
        timmy.setheading(90)
        timmy.forward(30)
        timmy.setheading(180)
        timmy.forward(300)
        timmy.setheading(0)

screen = Screen()
screen.exitonclick()
