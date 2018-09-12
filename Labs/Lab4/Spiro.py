import turtle
import random
turtle.speed(1000)
turtle.delay(1)
def spiro(sides,amount,size):
    number = 360/amount
    for x in range(0,amount):
        angle = x*number
        r = random.random()*.8
        g = random.random()*.8
        b = random.random()*.8
        turtle.color(r, g, b)
        turtle.right(angle)
        turtle.begin_fill()
        turtle.forward(size)
        for x in range(0,sides-1):
            turtle.left(360/sides)
            turtle.forward(size)
        turtle.setheading(0)
        turtle.end_fill()
    turtle.hideturtle()
    turtle.done()
