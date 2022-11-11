# program to draw spiral helix pattern
import turtle
screen = turtle.Screen()
screen.bgcolor('black')
tur = turtle.Turtle()
tur.color('white')
tur.speed(11)
for i in range(40):
    tur.circle(5*i)
    tur.circle(-5*i)
    tur.left(i)
turtle.exitonclick()
"""
output file added
"""
