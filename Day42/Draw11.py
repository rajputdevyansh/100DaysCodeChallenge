# program to draw a circle spiro graph
import turtle
tur = turtle.Turtle()
screen = turtle.Screen()
screen.bgcolor("black")
tur.pensize(2)
tur.speed(0)
for i in range(6):
    for colors in ["red", "blue", "magenta", "green", "yellow", "white"]:
        tur.color(colors)
        tur.circle(120)
        tur.left(10)

tur.hideturtle()
turtle.done()
"""
output file added
"""
