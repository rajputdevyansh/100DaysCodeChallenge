# program to draw a rainbow benzene
import turtle
colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']
tur = turtle.Turtle()
screen = turtle.Screen()
screen.bgcolor('black')
screen.title('Rainbow benzene')
tur.speed(100)
for x in range(360):
    tur.pencolor(colors[x % 6])
    tur.width(x//100+1)
    tur.forward(x)
    tur.left(59)
turtle.done()
"""
output file added
"""
