#CSCI 1133 Homework 2
#Erik Lindeman
#Problem D

shapeBoolean = False

def drawTri(size):
    turtle.right(angle)
    turtle.forward(size)
    turtle.left(120)
    turtle.forward(size)
    turtle.left(120)
    turtle.forward(size)
    turtle.setheading(0)

def drawSqr(size):
    turtle.right(angle)
    turtle.forward(size)
    turtle.left(90)
    turtle.forward(size)
    turtle.left(90)
    turtle.forward(size)
    turtle.left(90)
    turtle.forward(size)
    turtle.setheading(0)

def drawOct(size):
    turtle.right(angle)
    turtle.forward(size)
    turtle.left(45)
    turtle.forward(size)
    turtle.left(45)
    turtle.forward(size)
    turtle.left(45)
    turtle.forward(size)
    turtle.left(45)
    turtle.forward(size)
    turtle.left(45)
    turtle.forward(size)
    turtle.left(45)
    turtle.forward(size)
    turtle.left(45)
    turtle.forward(size)
    turtle.setheading(0)

while(shapeBoolean == False):
    shape = input("What kind of shape do you want to draw? ")
    if(shape.lower() == "square" or shape.lower() == "triangle" or shape.lower() == "octagon"):
        shapeBoolean = True
    else:
        print("ERROR:", shape, "is not a valid choice.  Please enter triangle, square, or octagon")

amount = int(input("How many would you like to draw? "))
size = int(input("How big should the shapes be? "))

number = 360/amount
import turtle
for x in range(0,amount):
    angle = x*number
    if (shape.lower() == "square"):
        drawSqr(size)
    elif (shape.lower() == "triangle"):
        drawTri(size)
    elif(shape.lower() == "octagon"):
        drawOct(size)


turtle.hideturtle()
turtle.done()
