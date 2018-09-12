#CSCI 1133 Homework 1
#Erik Lindeman
#Problem 1C
import turtle
def square(width, height):
    turtle.forward(width)
    turtle.left(90)
    turtle.forward(height)
    turtle.left(90)
    turtle.forward(width)
    turtle.left(90)
    turtle.forward(height)
    turtle.left(90)
    turtle.penup()
    turtle.hideturtle()

def triangle(width, height):
    turtle.showturtle()
    turtle.goto(width*2,0)
    turtle.pendown()
    turtle.forward(width)
    turtle.left(90)
    turtle.forward(height)
    turtle.goto(width*2,0)
    turtle.hideturtle()
    turtle.done()

width = float(input("Enter a width: "))
height = float(input("Enter a height: "))

square(width, height)
triangle(width, height)
