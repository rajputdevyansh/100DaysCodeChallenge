# program to draw spiral square inside out
import turtle
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Spiral Square Inside Out")
tur = turtle.Turtle()
tur.color("red")
tur.speed(0)


def squarefun(size):
    for i in range(4):
        tur.fd(size)
        tur.left(90)
        size = size+5


squarefun(16)
squarefun(36)
squarefun(56)
squarefun(76)
squarefun(96)
squarefun(116)
squarefun(136)
squarefun(156)
turtle.done()
"""
output file added
"""
