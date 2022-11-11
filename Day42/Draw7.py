# program to draw spiral square outside in
import turtle
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Spiral Square Outside In")
tur = turtle.Turtle()
tur.color("red")


def squarefun(size):
    for i in range(4):
        tur.fd(size)
        tur.left(90)
        size = size-5


squarefun(155)
squarefun(136)
squarefun(116)
squarefun(96)
squarefun(76)
squarefun(56)
squarefun(36)
turtle.done()
"""
output file added
"""
