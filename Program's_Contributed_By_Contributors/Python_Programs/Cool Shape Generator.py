# Created by @Mattjava

# This is a small project that will make a shape out of 360 polygons
# It will first as the user to input the shape they want the program to draw
# It will then ask the user to turn on color mode. If the user inputs "yes", each polygon will be a
# different color.
# Finally, it will output the product as a circle made up of 360 polygons of the user's choice

from turtle import Turtle, Screen
import turtle
import random

turtle.colormode(255)

# Creates a polygon with all of its sides being equivalent to one another
def make_shape(sides, side_length):
    degree = 360 / sides
    for i in range(sides):
        turtle.forward(side_length)
        turtle.left(degree)


# Creates and returns a new color in RGB color code
def make_new_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    return (r, g, b)


# A shape hashmap containing polygons and their number of sides.
shapes = {
    "triangle": 3,
    "square": 4,
    "pentagon": 5,
    "hexagon": 6,
    "heptagon": 7,
    "octagon": 8,
    "nonagon": 9,
    "decagon": 10
}
# Gets the user's input for what kind of polygon they want to draw and if color mode should be turned on.
user_shape = input("What polygon do you want to use? ").lower()
user_color_mode = input("Do you want to turn on color mode? Yes or no? ").lower()

# Sets the variable "sides" to the number of sides in the user's shape.
# If the user's shape isn't in the "shapes" map, it will set sides to 4, creating a square.
if user_shape in shapes:
    num_of_sides = shapes[user_shape]
else:
    num_of_sides = 4


# Sets up screen
screen = Screen()
screen.bgcolor("black")

# Sets up turtle
turtle = Turtle()
turtle.hideturtle()
turtle.color("white")
turtle.speed("fastest")

# For-loop to create a circle made up of 360 polygons
for i in range(360):
    if user_color_mode == "yes":
        turtle.color(make_new_color())
    make_shape(num_of_sides, 100)
    turtle.right(1)

screen.exitonclick()
