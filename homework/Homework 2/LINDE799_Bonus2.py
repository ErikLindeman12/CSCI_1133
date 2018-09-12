#CSCI 1133 Homework 2
#Erik Lindeman
#Problem D

shapeBoolean = False

def drawTri(size):
    turtle.right(angle)
    if(fill == 1):
        turtle.begin_fill()
    turtle.forward(size)
    turtle.left(120)
    turtle.forward(size)
    turtle.left(120)
    turtle.forward(size)
    turtle.setheading(0)
    if(fill == 1):
        turtle.end_fill()

def drawSqr(size):
    turtle.right(angle)
    if(fill == 1):
        turtle.begin_fill()
    turtle.forward(size)
    turtle.left(90)
    turtle.forward(size)
    turtle.left(90)
    turtle.forward(size)
    turtle.left(90)
    turtle.forward(size)
    turtle.setheading(0)
    if(fill == 1):
        turtle.end_fill()

def drawOct(size):
    turtle.right(angle)
    if(fill == 1):
        turtle.begin_fill()
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
    if(fill == 1):
        turtle.end_fill()

while(shapeBoolean == False):
    shape = input("What kind of shape do you want to draw? ")
    if(shape.lower() == "square" or shape.lower() == "triangle" or shape.lower() == "octagon"):
        shapeBoolean = True
    else:
        print("ERROR:", shape, "is not a valid choice.  Please enter triangle, square, or octagon")

amount = int(input("How many would you like to draw? "))
size = int(input("How big should the shapes be? "))
increment = int(input("How much larger should each successive Shape get? "))

number = 360/amount
import turtle
turtle.speed(100)
for x in range(0,amount):
    angle = x*number
    size = size+x*increment
    color = (x%7)+1
    fill = x%2

    if(color == 1):
        turtle.color('red','grey')
    elif(color == 2):
        turtle.color('orange','grey')
    elif(color == 3):
        turtle.color('yellow','grey')
    elif(color == 4):
        turtle.color('green','grey')
    elif(color == 5):
        turtle.color('blue','grey')
    elif(color == 6):
        turtle.color('indigo','grey')
    elif(color == 7):
        turtle.color('violet','grey')

    if (shape.lower() == "square"):
        drawSqr(size)
    elif (shape.lower() == "triangle"):
        drawTri(size)
    elif(shape.lower() == "octagon"):
        drawOct(size)

turtle.hideturtle()
turtle.done()
