import turtle
import random
import math
turtle.speed(1000)
turtle.delay(1)
circle = 0
tries = 0
turtle.penup()
turtle.forward(150)
turtle.left(90)
turtle.pendown()
turtle.forward(150)
turtle.left(90)
turtle.forward(300)
turtle.left(90)
turtle.forward(300)
turtle.left(90)
turtle.forward(300)
turtle.left(90)
turtle.forward(150)
turtle.penup()
turtle.goto(0,-150)
turtle.right(90)
turtle.pendown()
turtle.circle(150)

while(tries < 1000):
  xcoordinate = random.uniform(-1,1)*150
  ycoordinate = random.uniform  (-1,1)*150
  turtle.penup()
  turtle.goto(xcoordinate,ycoordinate)
  radius = math.sqrt(xcoordinate*xcoordinate + ycoordinate*ycoordinate)
  if radius<150:
      circle += 1
      turtle.dot(5, "green")
  else:
      turtle.dot(5, "red")
  tries += 1

Pi = circle/250

Value = "Value of Pi: " + str(Pi)
turtle.goto(-200,200)
turtle.write(Value, font=("Arial", 15, "normal"))
turtle.hideturtle()
turtle.done()
