# A program to create a line star
import turtle

screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Drawing")
my_turtle = turtle.Turtle()
my_turtle.color("red")
for i in range(0, 8):
    my_turtle.forward(100)
    my_turtle.backward(100)
    my_turtle.left(45)
my_turtle.hideturtle()
turtle.done()
"""
Output file added in same folder
"""
