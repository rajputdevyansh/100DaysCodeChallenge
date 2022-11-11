# program to draw vibrate circle
import turtle
tur = turtle.Turtle()
screen = turtle.Screen()
screen.bgcolor('black')
tur.pencolor('red')
x = 0
y = 0
tur.speed(0)
tur.penup()
tur.goto(0, 200)
tur.pendown()
while True:
    tur.forward(x)
    tur.right(y)
    x += 3.5
    y += 1
    if y == 210:
        break
    tur.hideturtle()
turtle.done()
"""
output file added
"""
