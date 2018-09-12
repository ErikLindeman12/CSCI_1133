#CSCI  1133 Homework 1
#Erik Lindeman
#Bonus Problem 1

def focalLength(obj, im):
    focal = (1/((1/obj)+(1/im)))
    return focal

def genDiagram(obj, im):

    absIm = abs(im)
    absObj = abs(obj)
    absFoc = abs(focalLength(obj,im))

    turtle.goto(-obj,0)
    turtle.goto(im,0)
    turtle.goto(.5,0)

    turtle.color('grey')
    turtle.begin_fill()
    turtle.goto(.5,150)
    turtle.goto(-.5,150)
    turtle.goto(-.5,-150)
    turtle.goto(.5,-150)
    turtle.goto(.5,0)

    turtle.penup()
    turtle.goto(-obj,0)
    turtle.color('black','red')
    turtle.pendown()
    turtle.begin_fill()
    turtle.goto(-obj,10)
    turtle.goto(-obj+10,10)
    turtle.goto(-obj+10,0)
    turtle.goto(-obj,0)
    turtle.goto(-obj,0)
    turtle.end_fill()

    turtle.penup()
    turtle.goto(-obj,12)
    turtle.write("Object", font=("Arial", 7, "normal"))

    turtle.penup()
    turtle.goto(im,0)
    turtle.color('black','blue')
    turtle.pendown()
    turtle.begin_fill()
    turtle.goto(im,10)
    turtle.goto(im-10,10)
    turtle.goto(im-10,0)
    turtle.goto(im,0)
    turtle.end_fill()

    turtle.penup()
    turtle.goto(im-(im/20),12)
    turtle.write("Image", font=("Arial", 7, "normal"))

    turtle.penup()
    turtle.goto(absFoc,0)
    turtle.pendown()
    turtle.color("black", "green")
    turtle.begin_fill()
    turtle.circle(5)
    turtle.end_fill()

    turtle.penup()
    turtle.goto(absFoc,-15)
    turtle.write("Focal Point", font=("Arial", 7, "normal"))

    turtle.goto(-absFoc,0)
    turtle.pendown()
    turtle.begin_fill()
    turtle.color("black", "green")
    turtle.circle(5)
    turtle.end_fill()

    turtle.penup()
    turtle.goto(-absFoc,-15)
    turtle.write("Focal Point", font=("Arial", 7, "normal"))

    turtle.hideturtle()
    turtle.done()


print('Welcome to the Lens Diagram Program')
obj = float(input('Enter an object distance in mm: '))
im = float(input('Enter an image distance in mm: '))
print('The focal Length of your Lens is: ', focalLength(obj, im),'mm')

import  turtle
genDiagram(obj,im)
