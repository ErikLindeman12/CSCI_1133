import random
import turtle
turtle1 = turtle.Turtle()
turtle2 = turtle.Turtle()
turtle3 = turtle.Turtle()
startingPoint = -470
gap = 50
turtle1.shape('turtle')
turtle1.color('green')
turtle1.penup()
turtle1.goto(startingPoint,0)
turtle2.shape('turtle')
turtle2.color('red')
turtle2.penup()
turtle2.goto(startingPoint,gap)
turtle3.shape('turtle')
turtle3.color('blue')
turtle3.penup()
turtle3.goto(startingPoint,-gap)
start = 0
while((turtle1.xcor()<470)and(turtle2.xcor()<470)and(turtle3.xcor()<470)):
  randomInteger = random.randint(1,15)
  if(start%3 == 0):
      turtle1.forward(randomInteger)
  if(start%3 == 1):
      turtle2.forward(randomInteger)
  if(start%3 == 2):
      turtle3.forward(randomInteger)
  start+=1
turtle.done()
