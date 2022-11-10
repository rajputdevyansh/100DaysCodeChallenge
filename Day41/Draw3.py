# program to create a simple pizza
import turtle

BACKGROUND_COLOR = "#9EC388"
CRUST_COLOR = "#ECA84F"
SAUCE_COLOR = "#AD0509"
CHEESE_COLOR = "#FB70F"
PEPPERONI = [
    [-70, 105],
    [-85, 175],
    [-25, 50],
    [-15, 100],
    [-25, 150],
    [-30, 205],
    [15, 50],
    [20, 120],
    [20, 200],
    [60, 156],
    [71, 215],
    [80, 90],
    [95, 150]
]
screen = turtle.Screen()
screen.bgcolor(BACKGROUND_COLOR)
screen.title("Pizza")
tur = turtle.Turtle()
tur.pensize(10)
tur.shape("circle")


def draw_cir(radius, line_color, fill_color):
    tur.color(line_color)
    tur.fillcolor(fill_color)
    tur.begin_fill()
    tur.circle(radius)
    tur.end_fill()


def move_turtle(x, y):
    tur.up()
    tur.goto(x, y)
    tur.down()


draw_cir(150, CRUST_COLOR, CRUST_COLOR)
move_turtle(0, 25)
draw_cir(125, SAUCE_COLOR, CHEESE_COLOR)

for location in PEPPERONI:
    move_turtle(location[0], location[1])
    draw_cir(10, SAUCE_COLOR, SAUCE_COLOR)

move_turtle(0, 150)
tur.color(BACKGROUND_COLOR)

for x in range(0, 8):
    tur.pendown()
    tur.left(45)
    tur.forward(150)
    tur.penup()
    tur.backward(150)

turtle.done()
"""
output added in same folder
"""
